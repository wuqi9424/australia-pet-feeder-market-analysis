# Public Derived Data

This package includes the derived/aggregated tables needed to inspect or reproduce portfolio summaries. It does not contain full consumer reviews, browser payloads or raw webpages.

| File in processed/ | Rows | Grain |
| --- | ---: | --- |
| market_context_summary.csv | 6 | Macro metric |
| supply_product_summary.csv | 53 | Canonical product; three wide slots retain57eligible ordinary offers |
| consumer_aspect_summary.csv | 32 | Substantive aspect aggregate |
| opportunity_candidate_summary.csv | 5 | Four candidates plus selected hybrid |
| final_recommendation_features.csv | 20 | Proposed design requirement |
| demand_weekly_summary.csv | 4666 | Request × keyword × week; boundary records retained |

CSV format: UTF-8 with BOM, comma-separated, quoted fields; blank=null. Preserve Boolean True/False/null. Counts, prices and rates must be parsed as numbers. Ordinary prices retain AUD denomination and original evidence timestamp, but product-page URLs and local provenance paths have been removed. Original source snapshots were not refreshed.

Market context retains official publisher URLs. Weekly demand retains request normalization, geography, original extraction time and boundary flags; it has no account/browser identifiers. Google Trends source: [Explore](https://trends.google.com/trends/explore/). Macro sources are [Animal Medicines Australia](https://animalmedicinesaustralia.org.au/resources/pets-in-australia-a-national-survey-of-pets-and-people-3/). Retail observations come from the public retailer/platform environments discussed in the methodology; review text stays private.

The supply table has53 products and42 canonical reference prices, distinct from57 ordinaryoffers. Consumer prevalence denominators are908 reviews/32 reviewed products. Summing critical aspects gives141 coded rows, not107 unique critical reviews. The weekly demand file has42 boundary records, excluded by default; independent requests remain separate.

**Third-party source data remains subject to its original source/platform terms.** Derived aggregate tables are provided for portfolio/research demonstration; the root MIT licence does not automatically license source data or grant ownership of consumer review text. Do not infer a right to reproduce original material from this package. No review snippets are included.

See [data dictionary](../docs/data_dictionary.md), [limitations](../docs/limitations.md) and [release manifest](../public_repository_manifest.md).
