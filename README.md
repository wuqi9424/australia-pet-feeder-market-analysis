# Australia Automatic Pet Feeder Market & Product Opportunity Analysis

**From public market evidence to a local-first product concept and validation plan.**

[Live Product Concept Website](https://australia-pet-feeder.vercel.app) · [Full Case Study](reports/case_study_en.md) · [Product Overview](product/product_overview.md) · [PRD Summary](product/prd_summary.md) · [Executive Summary](reports/executive_summary.md)

## Business question

If a new pet-care brand enters the Australian automatic pet feeder category, which user problem should it address, with what product scope, competitive price position and channel hypothesis? This independent desk-research and product-design project links observable supply, selected consumer experience and relative search signals before translating a recommendation into requirements and interaction design. It is not a client engagement or a commercially launched product.

## Project at a glance

| Evidence | Frozen scope |
| --- | --- |
| Supply | 53 canonical products; 70 retail listings; 80 offers |
| Ordinary price analysis | 57 eligible quotes across 42 canonical products |
| Confirmed overlap | 13 cross-retailer canonical matches |
| Consumer reviews | 908 reviews; 32 reviewed products; 16 brands |
| Review taxonomy | 32 business aspects plus a separately handled auxiliary evaluation |
| Corrected critical evidence | 141 review-aspect rows across 107 reviews |
| Demand | Five-year Australian Google Trends and macro pet-category context |

These are sample and evidence counts, not national market shares. Product, listing, offer and review-aspect units are kept separate throughout.

## Research method

The pilot tested source access, field definitions, missing-value semantics and product identity before formal sampling. Its small-sample completeness findings are historical method evidence, not final market results. Formal selection was targeted by brand, channel, sophistication, mechanism and representative same-product overlap, rather than simply choosing cheap or fully populated pages.

Canonical identity uses GTIN, exact model/MPN/ASIN and verified configuration where evidence supports a match. Listings retain independent retailer identities; offers retain seller and price conditions. Unknown features remain unknown rather than false. An ordinary price needs reliable identity, a valid listing, current AUD evidence, URL, timestamp and field provenance. Member, Prime and coupon conditions are not pooled with ordinary quotes.

Reviews were coded as Aspect × Sentiment × Severity with literal evidence. Thirty reviews received targeted human adjudication: 24 accepted, six modified and zero rejected. This is AI-assisted coding with targeted adjudication, not independent inter-rater validation. A later severity audit found four insufficiently supported critical rows; corrected analysis uses the new layer without rewriting history. Auxiliary overall evaluation never enters substantive rankings.

Google Trends comparisons respect request-specific normalisation. Public rating and review counts remain platform-specific; macro pet data provides context rather than an automatic-feeder market estimate.

## Key findings

The 57 ordinary quotes have median AUD139.99, mean AUD166.81 and IQR AUD134.95. Confirmed bands are Lower ≤163.49, Middle >163.49 and ≤241.47, and Upper >241.47. These describe observed prices, not product quality.

Selected reviewers value routine relief and planned feeding. Feeding reliability is a core operational concern; setup includes both positive and negative experience, and connectivity creates substantial friction in its mentioned reviews. Complaint counts are not an opportunity score, and reviewer claims are not verified defects.

Within compatible Trends comparisons, automatic cat feeder rises from 18.57 to 29.63 in first/last 12-month relative averages; automatic pet feeder is broadly stable at 13.83 to 13.79. These are search signals, not sales growth. Australian macro pet-category context supports plausibility, while absolute keyword volume, purchase conversion and feeder market size remain unavailable.

## Opportunity and product direction

Four directions were compared qualitatively: reliability-first connected routines, simple cat-oriented routines, multi-cat selective access and timed wet-food freshness. The selected primary combines OH1+OH2 into a reliability-first, cat-oriented dry-food automatic feeder with local-first execution and lightweight optional connectivity. OH3 remains a deferred niche; OH4 needs preservation and compatibility proof. No arbitrary weighted Opportunity Score was used.

The primary persona is Routine-focused Cat Owner. MVP Core prioritises local scheduling, portion configuration, understandable execution evidence, recovery and safe maintenance. Optional App support may add remote edits/status/reminders, but cannot become a prerequisite for core feeding. Camera/audio, selective access and wet-food refrigeration stay outside v1. Battery backup is a supporting experiment outside the baseline, not an implemented promise.

Attempted dispensing is not confirmed food delivery or pet consumption. Remote App save is not device commitment; confirmation needs a matching acknowledgement. Offline views disclose stale information and conditional local continuation. Maintenance and near-meal recovery policies remain open where engineering evidence is missing.

## Selected product artifacts

- [Product overview](product/product_overview.md): user, job, principles and scope.
- [PRD summary](product/prd_summary.md): selected requirements and unexecuted acceptance intentions.
- [User flows](product/user_flows.md) and [status model](product/status_model.md): normal, offline and uncertain outcomes.
- [Key decisions](product/key_product_decisions.md): choices, trade-offs and validation needs.
- [Metrics and validation](product/metrics_and_validation.md): proposed instrumentation and tests.

The illustrative AUD149–199 validation window is not validated willingness to pay or a launch price. Specialist pet-retail pilot and controlled Amazon AU are channel hypotheses without retailer commitments or economics proof. Recommendation status remains **recommended_for_validation**.

## Methods, tools and public boundaries

Python supported evidence engineering, descriptive summaries and QA. Tableau-ready presentation tables and dashboard specifications exist; native Tableau workbook validation remains pending. The interactive website uses HTML/CSS/JavaScript and simulated low-fidelity flows. AI assisted engineering, coding support, documentation and QA; humans owned evidence rules, adjudication, interpretation, trade-offs and final decisions.

Six sanitised tables in [data](data/README.md), [methodology](docs/methodology.md), [dictionary](docs/data_dictionary.md), [workflow](docs/project_workflow.md), [limitations](docs/limitations.md), [source code](src/README.md) and [dashboard status](dashboard/README.md) preserve research visibility. Raw review text, acquisition artifacts, private preparation material and the full internal PRD are excluded.

## Limitations and next validation

Sampling is targeted; reviews are concentrated by product, source and brand. Amazon evidence is platform-global/uncertain, syndication unknown is not confirmed original, and Upper-band review coverage is sparse. No hardware validation, usability validation, live telemetry, PMF or commercial launch is claimed. Next work would test comprehension, setup, reliable output, interruption recovery and economic feasibility. The live website is a product concept, not a purchasable device.

## Repository structure and suggested reading order

1. [Executive summary](reports/executive_summary.md) — the decision, supporting evidence and validation gate.
2. [English case study](reports/case_study_en.md) — research, competitive analysis and the evidence-to-product narrative.
3. [Product overview](product/product_overview.md) → [PRD summary](product/prd_summary.md) → [decisions](product/key_product_decisions.md) → [flows](product/user_flows.md) → [metrics](product/metrics_and_validation.md).
4. [Methods](docs/methodology.md), [data dictionary](docs/data_dictionary.md), [limitations](docs/limitations.md) and [portable code](src/README.md) — inspect the analytical boundaries and reproduce public summaries.

| Directory | Public contents |
| --- | --- |
| `reports/` | English case study, executive summary and publication audit |
| `product/` | Selected product-definition and design summaries; not the full internal PRD |
| `docs/` | Methodology, dictionary, workflow and limitations |
| `data/processed/` | Six sanitised presentation tables |
| `src/`, `tests/` | AI-assisted portable descriptive modules and boundary checks |
| `dashboard/` | Tableau status and build context; native validation pending |
| `portfolio_website/` | Frozen bilingual public concept artifact, separate from English repository documentation |

Repository documentation is English-only. The separate frozen website intentionally retains Chinese and English content. Neither the code nor generated artifacts are represented as entirely independently authored: AI-assisted implementation and documentation remain subject to human decisions and QA.
