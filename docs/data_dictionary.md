# Public Data Dictionary

Six sanitised frozen tables are bundled in data/processed/. CSVs are UTF-8 with BOM; blank means null. No raw reviews or local provenance paths are distributed. IDs are strings,counts/prices/rates numeric,flags Boolean/null. Do not infer missing fields. Source/platform terms remain applicable.

## market_context_summary.csv

Row: One macro metric. Rows: 6.

Denominator: 6 metrics;unit-specific,not additive.

Interpretation: Official source URLs and reference year retained;not feeder TAM.

| Field | Type | Meaning |
| --- | --- | --- |
| `metric_id` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `metric` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `value` | number | Original numeric value;ownership73 in percent units,moneyAUD,populationanimals. |
| `unit` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `reference_year` | number | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `source_name` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `source_scope` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `interpretation` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `limitation` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `source_url` | text | Official macro source attribution URL;no private retail/session URLs. |
| `source_locator` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |


## supply_product_summary.csv

Row: One canonical product. Rows: 53.

Denominator: 53 products;70 listings;80 offers;57 ordinary prices;42 canonical reference prices.

Interpretation: Wide slots keep eligible offers distinct;do not count slots as products. Three-state features remain unknown when blank.

| Field | Type | Meaning |
| --- | --- | --- |
| `canonical_product_id` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `brand` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `brand_type` | text | Existing canonical classification;24 values absent remain null,not guessed. |
| `product_name` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `product_level` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `mechanism` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `canonical_reference_price` | number | Median eligible ordinary offers for this canonical,AUD;null when no eligible price. |
| `price_band` | text | Lower<=163.49;Middle>163.49<=241.47;Upper>241.47;unknown without a reference price. These are price descriptors,not quality tiers. |
| `price_band_scheme` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `price_band_stability` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `specialist_retail_flag` | Boolean/null | Observed sample presence,not marketcoverage orsales. |
| `general_retail_flag` | Boolean/null | Observed sample presence,not marketcoverage orsales. |
| `marketplace_flag` | Boolean/null | Observed sample presence,not marketcoverage orsales. |
| `amazon_flag` | Boolean/null | Observed sample presence,not marketcoverage orsales. |
| `meal_schedule` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `portion_control` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `wifi` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `app_control` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `camera` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `multi_pet` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `microchip` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `selective_access` | Boolean/null | Frozen mechanism-derived context flag,distinct from microchip support. |
| `wet_food_compatibility` | Boolean/null | Explicit frozen product feature:True/False/null. Null is unknown, not False. |
| `listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `offer_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `ordinary_eligible_offer_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `specialist_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `general_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `marketplace_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `self_operated_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `marketplace_seller_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `mixed_operation_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `unknown_operation_listing_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `ordinary_offer_1_id` | text | Frozen ordinary-offer slot 1 id;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_1_price` | number | Frozen ordinary-offer slot 1 price;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_1_retailer` | text | Frozen ordinary-offer slot 1 retailer;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_1_price_type` | text | Frozen ordinary-offer slot 1 price_type;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_1_currency` | text | Frozen ordinary-offer slot 1 currency;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_1_evidence_timestamp` | text | Frozen ordinary-offer slot 1 evidence_timestamp;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_2_id` | text | Frozen ordinary-offer slot 2 id;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_2_price` | number | Frozen ordinary-offer slot 2 price;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_2_retailer` | text | Frozen ordinary-offer slot 2 retailer;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_2_price_type` | text | Frozen ordinary-offer slot 2 price_type;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_2_currency` | text | Frozen ordinary-offer slot 2 currency;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_2_evidence_timestamp` | text | Frozen ordinary-offer slot 2 evidence_timestamp;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_3_id` | text | Frozen ordinary-offer slot 3 id;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_3_price` | number | Frozen ordinary-offer slot 3 price;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_3_retailer` | text | Frozen ordinary-offer slot 3 retailer;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_3_price_type` | text | Frozen ordinary-offer slot 3 price_type;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_3_currency` | text | Frozen ordinary-offer slot 3 currency;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |
| `ordinary_offer_3_evidence_timestamp` | text | Frozen ordinary-offer slot 3 evidence_timestamp;blank when slot unavailable. Source_url intentionally omitted;currency/time retained. |


## consumer_aspect_summary.csv

Row: One substantive aspect. Rows: 32.

Denominator: 32 aspects;908 reviews/32 reviewed products;local context453 reviews/24 products.

Interpretation: No text;corrected141 critical rows,not unique consumers. Aggregates cannot support raw brand/price/source filtering.

| Field | Type | Meaning |
| --- | --- | --- |
| `aspect_id` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `aspect` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `review_mentions` | number | Unique reviews mentioning this aspect. |
| `review_prevalence` | number | Unique reviews mentioning aspect /908. |
| `positive_reviews` | number | Positive aspect-coded reviews. |
| `negative_or_mixed_reviews` | number | Negative/mixed aspect-coded reviews. |
| `negative_rate` | number | Negative/mixed reviews /review_mentions. |
| `products_with_negative_or_mixed` | number | Unique negatively/mixed affected reviewed canonical products. |
| `negative_product_prevalence` | number | Distinct negative/mixed affected products /32;not product-equal-weight review rate. |
| `functional_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `critical_count` | number | Corrected critical review–aspect rows,not unique reviews orverified defects. |
| `australian_context_negative_count` | number | Frozen count at the row grain;only additive where appropriate. Product counts repeat after any offer/feature pivot. |
| `source_sensitivity` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `review_denominator` | number | Fixed named population denominator;MIN/ATTR,not SUM across aspects. |
| `reviewed_product_denominator` | number | Fixed named population denominator;MIN/ATTR,not SUM across aspects. |
| `australian_context_review_denominator` | number | Fixed named population denominator;MIN/ATTR,not SUM across aspects. |
| `australian_context_product_denominator` | number | Fixed named population denominator;MIN/ATTR,not SUM across aspects. |
| `critical_count_basis` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |


## opportunity_candidate_summary.csv

Row: One candidate. Rows: 5.

Denominator: the four candidate directions, identified in the data as reliability-first connected routine (OH1), simple cat-oriented routine (OH2), multi-cat selective access (OH3) and timed wet-food freshness (OH4), plus the selected combination of the first two (OH1+OH2).

Interpretation: Qualitative frozen comparison;no opportunity score. consumer_support is a JSON text object of aspect metrics,not a universal score.

| Field | Type | Meaning |
| --- | --- | --- |
| `candidate_id` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `candidate_name` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `target_problem` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `target_user` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `price_fit` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `channel_context` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `consumer_support` | text | Serialized existing quantitative aspect metrics for reference;parse JSON if needed,not a measure or raw text. |
| `supply_support` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `demand_support` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `triangulation_status` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `selected_primary` | Boolean/null | True only for the selected reliability-first, cat-oriented combination (OH1+OH2). |
| `selected_secondary` | Boolean/null | True only for the deferred multi-cat selective-access niche (OH3), kept for later discovery. |
| `key_strength` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `key_risk` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `main_limitation` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `recommendation_status` | text | Recommended for further validation, stored as the value `recommended_for_validation`; not launch approval. |
| `candidate_decision_status` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |


## final_recommendation_features.csv

Row: One proposed requirement. Rows: 20.

Denominator: 20 rows;6 Must-have/5 Supporting/2 Differentiating/1 Optional/6 Excluded.

Interpretation: Repeated strategy fields use attributes,not summed numbers. Optional included_v1 blank=undecided.

| Field | Type | Meaning |
| --- | --- | --- |
| `feature` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `feature_group` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `requirement_class` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `included_v1` | Boolean/null | Proposed scope True;excluded False;Optional null. Not proven feature capability. |
| `positioning_role` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `reasoning` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `proof_requirement` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `evidence_boundary` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `target_user` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `jtbd` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `product_concept` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `price_position` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `illustrative_price_low_aud` | number | 149,testboundnot WTP/launch price. |
| `illustrative_price_high_aud` | number | 199,testboundnot WTP/launch price. |
| `price_window_status` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `primary_channel_hypothesis` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `secondary_channel_hypothesis` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `recommendation_status` | text | Recommended for further validation, stored as the value `recommended_for_validation`; not launch approval. |
| `positioning_status` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |


## demand_weekly_summary.csv

Row: One request × keyword × date. Rows: 4666.

Denominator: 4,666 raw records;42 boundary rows;4,624 default retained.

Interpretation: Only compatible normalization_group can share a numerical comparison. Rolling averages preserve their source raw-window policy.

| Field | Type | Meaning |
| --- | --- | --- |
| `date` | Date | Original week-start date,ISO yyyy-mm-dd. |
| `keyword` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `interest` | number | Relative 0–100within-request Google Trends index;zero may reflect sparsity. |
| `rolling_4week` | number | Frozen trailing four raw observations;first three per-series null;boundary input can contribute. |
| `request_group` | text | Original request identifier. |
| `keyword_role` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `pet_type` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `is_core_keyword` | Boolean/null | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `normalization_group` | text | Original independently normalised scale;never combine requests. |
| `boundary_period_excluded` | Boolean/null | Conservative boundary flag;True excluded by default. |
| `geography` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `search_type` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |
| `evidence_timestamp` | text | Literal frozen identity/category/context/qualitative attribute;not new classification or market claim. |

## Source and release boundaries

Macro publisher: Animal Medicines Australia,2025. Retail summaries reflect public specialist/general/marketplace environments in the methodology,not an exhaustive census. Consumer aggregate inputs are corrected AI-assisted coding with targeted human adjudication;full text remains private. Demand source: Google Trends Australia Web Search,unquoted terms;request scales separate.

Canonical→listing→offer IDs are preserved;no public rematching occurs. For ordinary prices,read the three non-null offer slots and their matching IDs/currencies/times. Do not blend canonical_reference_price into the 57-offer distribution. Wide product/listing counts are additive only in the 53-row base table.

Methods and tools are documented in methodology.md and the module README. No new data acquisition or marketanalysis occurred for this release.
