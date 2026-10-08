"""Meaningful grain/null/boundary checks against bundled frozen inputs."""
import unittest
from src.common import boolean, read_table
from src.data_processing.supply_summary import price_band, summarize as supply
from src.consumer_analysis.aspect_summary import summarize as consumer
from src.demand_analysis.trends_summary import summarize as demand
from src.opportunity_synthesis.recommendation_summary import summarize as recommendation


class PublicWorkflowTests(unittest.TestCase):
    def test_unknown_is_not_false(self):
        self.assertIsNone(boolean(None))
        self.assertIs(boolean('False'), False)
        with self.assertRaises(ValueError):
            boolean('unknown')

    def test_price_band_boundaries(self):
        self.assertEqual(price_band(None), 'Unknown')
        self.assertEqual(price_band(163.49), 'Lower')
        self.assertEqual(price_band(163.4901), 'Middle')
        self.assertEqual(price_band(241.47), 'Middle')
        self.assertEqual(price_band(241.4701), 'Upper')

    def test_distinct_product_and_offer_grains(self):
        rows = read_table('supply_product_summary.csv')
        result = supply(rows)
        self.assertEqual(result['canonical_product_n'], 53)
        self.assertEqual(result['listing_n'], 70)
        self.assertEqual(result['total_offer_n'], 80)
        self.assertEqual(result['priced_canonical_n'], 42)
        self.assertEqual(result['ordinary_price_stats']['n'], 57)
        self.assertEqual(result['ordinary_price_stats']['median'], 139.99)
        self.assertEqual(result['features']['wet_food_compatibility'], {'true':4,'false':0,'unknown':49})
        with self.assertRaises(ValueError):
            supply(rows + [rows[0]])

    def test_corrected_consumer_aggregate(self):
        result = consumer(read_table('consumer_aspect_summary.csv'))
        self.assertEqual(result['business_aspect_n'], 32)
        self.assertEqual(result['corrected_critical_aspect_rows'], 141)
        self.assertEqual(result['review_denominators'], [908])
        self.assertEqual(result['reviewed_product_denominators'], [32])

    def test_normalization_and_nonoverlapping_periods(self):
        rows = read_table('demand_weekly_summary.csv')
        series = demand(rows)['series']
        cat = next(r for r in series if r['normalization_group']=='core_5y' and r['keyword']=='automatic cat feeder')
        self.assertEqual(round(cat['first_12_month_mean'],2),18.57)
        self.assertEqual(round(cat['last_12_month_mean'],2),29.63)
        self.assertEqual((cat['first_period_n'],cat['last_period_n']),(53,52))
        self.assertTrue(all(r['first_12_month_mean'] is None for r in series if r['normalization_group']=='core_12m'))
        dirty = [dict(rows[0],normalization_group='different_request')]
        with self.assertRaises(ValueError):
            demand(dirty)

    def test_frozen_decision_and_optional_scope(self):
        result = recommendation(read_table('opportunity_candidate_summary.csv'),read_table('final_recommendation_features.csv'))
        self.assertEqual(result['primary'], ['OH1+OH2'])
        self.assertEqual(result['deferred_secondary'], ['OH3'])
        self.assertEqual(result['status'], 'recommended_for_validation')
        self.assertEqual(result['feature_groups']['Optional'],1)


if __name__ == '__main__':
    unittest.main()
