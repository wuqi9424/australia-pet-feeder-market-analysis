"""Reproduce product/offer summaries; never rematch or reclassify products."""
from collections import Counter
import statistics
import math
from src.common import boolean, emit, number, read_table, unique

FEATURES = ['meal_schedule', 'wifi', 'app_control', 'camera', 'multi_pet',
            'microchip', 'selective_access', 'wet_food_compatibility']


def price_band(value):
    if value is None:
        return 'Unknown'
    return 'Lower' if value <= 163.49 else 'Middle' if value <= 241.47 else 'Upper'


def quantile(values, probability):
    """Inclusive linear interpolation at (n-1)p, retained from the analysis method."""
    values = sorted(values)
    if not values:
        return None
    rank = (len(values) - 1) * probability
    index = int(rank)
    return values[index] if index == len(values)-1 else values[index] + (rank-index)*(values[index+1]-values[index])


def price_stats(values):
    if not values:
        return dict(n=0, min=None, q1=None, median=None, mean=None, q3=None, max=None, iqr=None)
    q1, q3 = quantile(values, .25), quantile(values, .75)
    return dict(n=len(values), min=min(values), q1=q1, median=statistics.median(values),
                mean=statistics.mean(values), q3=q3, max=max(values), iqr=q3-q1)


def summarize(rows):
    unique(rows, ['canonical_product_id'])
    prices, offer_ids = [], []
    for row in rows:
        product_prices = []
        for slot in range(1, 4):
            prefix = f'ordinary_offer_{slot}_'
            price = number(row[prefix+'price'])
            if price is None:
                if row[prefix+'id'] is not None:
                    raise ValueError('Offer ID without price')
                continue
            if price <= 0 or row[prefix+'currency'] != 'AUD' or row[prefix+'price_type'] not in ['standard', 'sale']:
                raise ValueError('Invalid ordinary-price slot')
            if not row[prefix+'id'] or not row[prefix+'evidence_timestamp']:
                raise ValueError('Missing offer identity or snapshot time')
            product_prices.append(price); prices.append(price); offer_ids.append(row[prefix+'id'])
        reference = number(row['canonical_reference_price'])
        if product_prices:
            if reference is None or not math.isclose(reference, statistics.median(product_prices), rel_tol=1e-12, abs_tol=1e-12):
                raise ValueError('Canonical reference price differs from ordinary-offer median')
        elif reference is not None:
            raise ValueError('Reference price without eligible offers')
        if len(product_prices) != number(row['ordinary_eligible_offer_count']):
            raise ValueError('Offer-slot count mismatch')
    if len(offer_ids) != len(set(offer_ids)):
        raise ValueError('Duplicate ordinary offer ID')
    return dict(
        canonical_product_n=len(rows), listing_n=sum(number(r['listing_count']) for r in rows),
        total_offer_n=sum(number(r['offer_count']) for r in rows),
        priced_canonical_n=sum(r['canonical_reference_price'] is not None for r in rows),
        product_levels=dict(Counter(r['product_level'] or 'unknown' for r in rows)),
        mechanisms=dict(Counter(r['mechanism'] or 'unknown' for r in rows)),
        channel_listing_counts={k:sum(number(r[k]) for r in rows) for k in
            ['specialist_listing_count', 'general_listing_count', 'marketplace_listing_count']},
        features={feature:{'true':sum(boolean(r[feature]) is True for r in rows),
                           'false':sum(boolean(r[feature]) is False for r in rows),
                           'unknown':sum(boolean(r[feature]) is None for r in rows)} for feature in FEATURES},
        ordinary_price_stats=price_stats(prices),
        ordinary_price_bands=dict(Counter(price_band(value) for value in prices)),
        limits='Sample/snapshot structure, not sales, market shares, quality or feature causality.')


if __name__ == '__main__':
    emit(summarize(read_table('supply_product_summary.csv')))
