"""Reconcile and rank existing aggregates, not recode private reviews."""
import math
from src.common import emit, number, read_table, unique


def summarize(rows):
    unique(rows, ['aspect_id'])
    for row in rows:
        if row['aspect'] == 'overall_evaluation':
            raise ValueError('Auxiliary aspect in business summary')
        mentions = number(row['review_mentions'])
        pairs = [('negative_rate', 'negative_or_mixed_reviews', mentions),
                 ('review_prevalence', 'review_mentions', number(row['review_denominator'])),
                 ('negative_product_prevalence', 'products_with_negative_or_mixed', number(row['reviewed_product_denominator']))]
        for rate, numerator, denominator in pairs:
            expected = number(row[numerator])/denominator if denominator else None
            actual = number(row[rate])
            if expected is None and actual is None:
                continue
            if actual is None or expected is None or not math.isclose(actual, expected, rel_tol=1e-12):
                raise ValueError('Aggregate rate/denominator mismatch')
    fields = ['aspect', 'positive_reviews', 'negative_or_mixed_reviews', 'negative_rate',
              'products_with_negative_or_mixed', 'critical_count', 'source_sensitivity']
    def top(field):
        return [{k:(r[k] if k in ['aspect', 'source_sensitivity'] else number(r[k])) for k in fields}
                for r in sorted(rows, key=lambda r:(-number(r[field]), r['aspect']))[:10]]
    return dict(business_aspect_n=len(rows), review_denominators=sorted({number(r['review_denominator']) for r in rows}),
                reviewed_product_denominators=sorted({number(r['reviewed_product_denominator']) for r in rows}),
                corrected_critical_aspect_rows=sum(number(r['critical_count']) for r in rows),
                positive_leaders=top('positive_reviews'), negative_mixed_leaders=top('negative_or_mixed_reviews'),
                limit='Aggregate rows do not recover unique critical reviews, source slices or semantic coding accuracy. Aspect counts overlap.')


if __name__ == '__main__':
    emit(summarize(read_table('consumer_aspect_summary.csv')))
