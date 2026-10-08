"""Retain independent request scales; no inferred absolute search volume."""
from collections import defaultdict
from datetime import date, timedelta
import statistics
from src.common import boolean, emit, number, read_table, unique


def summarize(rows):
    unique(rows, ['request_group', 'keyword', 'date'])
    groups = defaultdict(list)
    for row in rows:
        if row['request_group'] != row['normalization_group'] or row['geography'] != 'AU':
            raise ValueError('Inconsistent normalization or geography')
        if boolean(row['boundary_period_excluded']) is None:
            raise ValueError('Unknown boundary status')
        if not boolean(row['boundary_period_excluded']):
            groups[(row['normalization_group'], row['keyword'])].append(row)
    result = []
    for (group, keyword), records in sorted(groups.items()):
        records = sorted(records, key=lambda r:r['date'])
        observations = [(date.fromisoformat(r['date']),number(r['interest'])) for r in records]
        values = [value for _,value in observations]
        if any(value is None or not 0 <= value <= 100 for value in values):
            raise ValueError('Invalid interest index')
        first_end = observations[0][0] + timedelta(days=365)
        last_start = observations[-1][0] + timedelta(days=7-365)
        first = [value for day,value in observations if day < first_end]
        last = [value for day,value in observations if day >= last_start]
        five_year = group.endswith('5y')
        result.append(dict(normalization_group=group, keyword=keyword, n=len(values),
            mean_index=statistics.mean(values), nonzero_share=sum(v>0 for v in values)/len(values),
            first_12_month_mean=statistics.mean(first) if five_year else None,
            last_12_month_mean=statistics.mean(last) if five_year else None,
            first_period_n=len(first) if five_year else None,last_period_n=len(last) if five_year else None,
            monthly_mean_index={month:statistics.mean(value for day,value in observations if day.month==month)
                                for month in range(1,13) if any(day.month==month for day,_ in observations)}))
    return dict(series=result, limits='Compare only within normalization_group; first/last comparisons withheld for overlapping 12m export. No sales/volume/seasonality-cause inference.')


if __name__ == '__main__':
    emit(summarize(read_table('demand_weekly_summary.csv')))
