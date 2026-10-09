"""Render the four static README figures from the bundled public tables.

Optional extra: needs matplotlib (`pip install matplotlib`). The analytical modules
and tests stay standard-library only. Run from the repository root:
    python -m src.visuals.make_figures
"""
from collections import defaultdict
from datetime import date
import statistics

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from src.common import ROOT, boolean, number, read_table
from src.data_processing.supply_summary import quantile

OUT = ROOT / 'figures'
FEATURES = ['meal_schedule', 'portion_control', 'wifi', 'app_control', 'camera',
            'multi_pet', 'microchip', 'selective_access', 'wet_food_compatibility']
LOWER_MAX, MIDDLE_MAX = 163.49, 241.47
TEST_WINDOW = (149, 199)

# Reference palette: categorical slots 1-3 (validated all-pairs), diverging blue/red, chrome.
BLUE, ORANGE, AQUA, RED = '#2a78d6', '#eb6834', '#1baf7a', '#e34948'
SURFACE, INK, INK2, MUTED, GRID, AXIS = '#fcfcfb', '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
LEVELS = [('Basic Automatic', 'Basic', BLUE), ('Smart', 'Smart', ORANGE), ('Advanced', 'Advanced', AQUA)]

plt.rcParams.update({
    'font.family': 'sans-serif', 'font.size': 10, 'text.color': INK,
    'axes.facecolor': SURFACE, 'figure.facecolor': SURFACE, 'axes.edgecolor': AXIS,
    'axes.labelcolor': INK2, 'xtick.color': MUTED, 'ytick.color': MUTED,
    'axes.spines.top': False, 'axes.spines.right': False, 'axes.grid': True,
    'grid.color': GRID, 'grid.linewidth': 0.6, 'axes.axisbelow': True,
    'legend.frameon': False, 'savefig.dpi': 200, 'savefig.bbox': 'tight',
})


def finish(fig, ax, title, subtitle, note, name, note_y=-0.02):
    ax.set_title(title, loc='left', fontsize=13, fontweight='bold', pad=26)
    ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=9.5, color=INK2, va='bottom')
    fig.text(0.01, note_y, note, fontsize=8, color=MUTED, ha='left', va='top', wrap=True)
    fig.savefig(OUT / name)
    plt.close(fig)


def ordinary_prices(rows):
    return [number(r[f'ordinary_offer_{i}_price']) for r in rows for i in range(1, 4)
            if r[f'ordinary_offer_{i}_price'] is not None]


def competitive_positioning(rows):
    fig, ax = plt.subplots(figsize=(9, 5.2))
    priced = [r for r in rows if r['canonical_reference_price'] is not None]
    stacks = defaultdict(int)
    for level, label, color in LEVELS:
        xs, ys = [], []
        for r in sorted((r for r in priced if r['product_level'] == level),
                        key=lambda r: number(r['canonical_reference_price'])):
            price = number(r['canonical_reference_price'])
            count = sum(boolean(r[f]) is True for f in FEATURES)
            # Spread products that share a feature count and a similar price.
            key = (count, round(price / 25))
            offset = (stacks[key] % 3 - 1) * 0.16
            stacks[key] += 1
            xs.append(price); ys.append(count + offset)
        n = len(xs)
        ax.scatter(xs, ys, s=46, color=color, edgecolor=SURFACE, linewidth=1.2,
                   label=f'{label} (n={n})', zorder=3)
    ax.axvline(LOWER_MAX, color=AXIS, linestyle='--', linewidth=1)
    ax.axvline(MIDDLE_MAX, color=AXIS, linestyle='--', linewidth=1)
    for x, text in [(95, 'Lower band'), ((LOWER_MAX + MIDDLE_MAX) / 2 + 22, 'Middle band'), (330, 'Upper band')]:
        ax.text(x, 7.3, text, ha='center', fontsize=8.5, color=MUTED)
    in_window = sum(TEST_WINDOW[0] <= number(r['canonical_reference_price']) <= TEST_WINDOW[1] for r in priced)
    ax.axvspan(*TEST_WINDOW, color=INK, alpha=0.06, zorder=1, linewidth=0)
    ax.text(sum(TEST_WINDOW) / 2, 6.1, f'Concept test window\nAUD149–199\n{in_window} products', ha='center',
            fontsize=8.5, color=INK)
    ax.set_xlim(20, 420); ax.set_ylim(0.4, 7.6)
    ax.set_yticks(range(1, 8))
    ax.set_xlabel('Reference price (AUD, median of eligible ordinary offers)')
    ax.set_ylabel('Explicitly listed features (of 9)')
    ax.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, -0.12), fontsize=9)
    finish(fig, ax, f'Competitive positioning: only {in_window} of {len(priced)} priced products sit at AUD149–199',
           'Basic feeders are cheap and simple. Connected Smart and Advanced feeders spread across every price band.',
           f'Source: frozen Dataset v2, {len(priced)} of 53 canonical products with an eligible ordinary price. '
           'Feature count includes only features the listing explicitly supports; unknown is not counted. '
           'The test window is illustrative, not validated willingness to pay.',
           '01_competitive_positioning.png', note_y=-0.09)


def price_distribution(rows):
    prices = ordinary_prices(rows)
    fig, ax = plt.subplots(figsize=(9, 4.6))
    bins = list(range(25, 426, 25))
    _, edges, patches = ax.hist(prices, bins=bins, color=BLUE, edgecolor=SURFACE, linewidth=2, zorder=3)
    median = statistics.median(prices)
    ax.set_ylim(0, 12.5)
    ax.axvline(median, color=INK, linewidth=1.5, zorder=4)
    ax.text(median - 4, 9.6, f'Median\nAUD{median:.2f}', fontsize=8.5, color=INK, ha='right')
    for x in (LOWER_MAX, MIDDLE_MAX):
        ax.axvline(x, color=MUTED, linestyle='--', linewidth=1, zorder=4)
    top = ax.get_ylim()[1]
    counts = [sum(p <= LOWER_MAX for p in prices), sum(LOWER_MAX < p <= MIDDLE_MAX for p in prices),
              sum(p > MIDDLE_MAX for p in prices)]
    for x, label, n in [(95, 'Lower ≤163.49', counts[0]), ((LOWER_MAX + MIDDLE_MAX) / 2, 'Middle', counts[1]),
                        (330, 'Upper >241.47', counts[2])]:
        ax.text(x, top * 0.86, f'{label}\n{n} quotes', ha='center', fontsize=8.5, color=INK2)
    ax.axvspan(*TEST_WINDOW, color=ORANGE, alpha=0.12, zorder=1, linewidth=0)
    ax.text(sum(TEST_WINDOW) / 2, top * 0.05, 'test\nwindow', ha='center', fontsize=8, color=INK2)
    ax.set_xlabel('Ordinary price quote (AUD)'); ax.set_ylabel('Number of quotes')
    ax.grid(axis='x', visible=False)
    q1, q3 = quantile(prices, .25), quantile(prices, .75)
    finish(fig, ax, 'Most ordinary prices cluster below AUD165',
           f'{len(prices)} eligible ordinary quotes. Mean AUD{statistics.mean(prices):.2f}, '
           f'middle 50% AUD{q1:.2f}–{q3:.2f}. Bands come from natural gaps in the observed prices.',
           'Source: frozen Dataset v2 ordinary-price panel. Member, Prime and coupon prices excluded. '
           'Unweighted sampled quotes, not sales-weighted prices; bands describe price, not quality.',
           '02_price_distribution.png')


def consumer_experience(rows):
    ranked = sorted(rows, key=lambda r: -number(r['review_mentions']))
    top = ranked[:10] + [r for r in ranked[10:] if r['aspect'] == 'connectivity']
    top = sorted(top, key=lambda r: number(r['review_mentions']))
    names = {'power_battery': 'Power / battery', 'owner_routine_relief': 'Routine relief for owner'}
    labels = [names.get(r['aspect'], r['aspect'].replace('_', ' ').capitalize()) for r in top]
    pos = [number(r['positive_reviews']) for r in top]
    neg = [number(r['negative_or_mixed_reviews']) for r in top]
    fig, ax = plt.subplots(figsize=(9, 5.6))
    y = range(len(top))
    ax.barh(y, [-n for n in neg], color=RED, height=0.62, label='Negative or mixed', zorder=3)
    ax.barh(y, pos, color=BLUE, height=0.62, label='Positive', zorder=3)
    for i, (p, n) in enumerate(zip(pos, neg)):
        ax.text(-n - 4, i, f'{n:.0f}', va='center', ha='right', fontsize=8.5, color=INK2)
        ax.text(p + 4, i, f'{p:.0f}', va='center', ha='left', fontsize=8.5, color=INK2)
    ax.axvline(0, color=AXIS, linewidth=1)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, color=INK)
    ax.set_xlim(-140, 270)
    ax.set_xticks([-100, -50, 0, 50, 100, 150, 200, 250])
    ax.set_xticklabels(['100', '50', '0', '50', '100', '150', '200', '250'])
    ax.set_xlabel('Reviews mentioning the aspect')
    ax.grid(axis='y', visible=False)
    ax.legend(loc='lower right', fontsize=9)
    finish(fig, ax, 'Owners value the routine. Reliability, setup and connectivity cause the friction',
           'The 10 most-mentioned aspects in 908 selected reviews (32 products), plus connectivity: '
           'the only one here that is mostly negative.',
           'Source: AI-assisted Aspect × Sentiment coding with targeted human adjudication (30 reviews). '
           'One review can mention several aspects. Reviewer reports, not verified defect rates; '
           'reviews are concentrated by product and source, not a representative survey.',
           '03_consumer_experience.png')


def search_trends(rows):
    series = defaultdict(list)
    for r in rows:
        if r['normalization_group'] == 'core_5y' and r['boundary_period_excluded'] == 'false':
            series[r['keyword']].append((date.fromisoformat(r['date']), number(r['interest'])))
    fig, ax = plt.subplots(figsize=(9, 4.6))
    for keyword, color in [('automatic cat feeder', BLUE), ('automatic pet feeder', ORANGE)]:
        points = sorted(series[keyword])
        values = [v for _, v in points]
        smooth = [statistics.mean(values[max(0, i - 6):i + 7]) for i in range(len(values))]
        dates = [d for d, _ in points]
        ax.plot(dates, values, color=color, linewidth=0.8, alpha=0.25)
        ax.plot(dates, smooth, color=color, linewidth=2)
        first, last = statistics.mean(values[:53]), statistics.mean(values[-52:])
        ax.text(dates[-1], smooth[-1], f'  {keyword}\n  {first:.2f} → {last:.2f}', color=INK,
                fontsize=8.5, va='center')
    ax.set_ylim(0, None)
    ax.set_ylabel('Google Trends relative interest (0–100)')
    ax.grid(axis='x', visible=False)
    ax.margins(x=0)
    finish(fig, ax, 'Search interest for "automatic cat feeder" rose; "automatic pet feeder" stayed flat',
           'Australia, web search, five years, one shared request. Bold line is a centred 13-week mean; '
           'labels show first vs last 12-month averages.',
           'Source: Google Trends, request core_5y; complete weeks only. Relative index within one request, '
           'not absolute search volume, sales or market growth.',
           '04_search_trends.png')


def main():
    OUT.mkdir(exist_ok=True)
    supply = read_table('supply_product_summary.csv')
    competitive_positioning(supply)
    price_distribution(supply)
    consumer_experience(read_table('consumer_aspect_summary.csv'))
    search_trends(read_table('demand_weekly_summary.csv'))
    print('\n'.join(sorted(p.name for p in OUT.glob('*.png'))))


if __name__ == '__main__':
    main()
