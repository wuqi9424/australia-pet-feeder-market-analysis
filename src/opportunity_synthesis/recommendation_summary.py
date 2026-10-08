"""Verify and display existing decisions; do not select a new winner."""
from collections import Counter
from src.common import boolean, emit, read_table, unique


def summarize(candidates, requirements):
    unique(candidates, ['candidate_id']); unique(requirements, ['feature'])
    primary = [r['candidate_id'] for r in candidates if boolean(r['selected_primary']) is True]
    secondary = [r['candidate_id'] for r in candidates if boolean(r['selected_secondary']) is True]
    if primary != ['OH1+OH2'] or secondary != ['OH3']:
        raise ValueError('Frozen selection does not match the documented recommendation')
    if any(r['recommendation_status'] != 'recommended_for_validation' for r in candidates+requirements):
        raise ValueError('Unsupported recommendation status')
    for row in requirements:
        inclusion = boolean(row['included_v1'])
        expected = None if row['feature_group']=='Optional' else row['feature_group']!='Excluded from v1'
        if inclusion is not expected:
            raise ValueError('Optional/excluded scope mismatch')
    return dict(primary=primary, deferred_secondary=secondary,
                feature_groups=dict(Counter(r['feature_group'] for r in requirements)),
                status='recommended_for_validation', price_window_status='not_WTP_not_validated_launch_price',
                limit='Checks reproduce a frozen qualitative decision, not performance, commercial proof or an opportunity score.')


if __name__ == '__main__':
    emit(summarize(read_table('opportunity_candidate_summary.csv'), read_table('final_recommendation_features.csv')))
