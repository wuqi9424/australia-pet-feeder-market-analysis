# Portable Public Modules

Run from the repository root with Python3.10 or newer. Only Python's standard library is needed; no credentials, API calls or network connection are used.

| Command | Module purpose | What it does not do |
| --- | --- | --- |
| `python -m src.data_processing.supply_summary` | Typed CSV loading, canonical-key checks, three-state features, ordinary-offer reconstruction and descriptive pricing | Does not discover products, resolve new identities or refresh prices |
| `python -m src.consumer_analysis.aspect_summary` | Reconcile aspect aggregate numerators/denominators; reproduce positive/negative leaders and corrected severity-row total | Does not classify text, recover unique critical reviews from aggregates, or claim coding accuracy |
| `python -m src.demand_analysis.trends_summary` | Reproduce within-request means, first/last periods, nonzero coverage and monthly profiles | Does not combine request scales, acquire new data or infer absolute search volume |
| `python -m src.opportunity_synthesis.recommendation_summary` | Check and display frozen selection and proposed feature groups | Does not select a new winner, compute an Opportunity Score or validate commercial feasibility |

All commands print JSON to standard output and leave input files unchanged. Shared CSV helpers preserve blank as null and reject invalid Boolean text. Relative bundled data locations are resolved from the repository directory, so commands do not depend on the original author's machine.

The modules are curated portable adaptations of the existing analytical rules, rather than wholesale copies of acquisition/internal build scripts. They expose product/offer separation, inclusive price percentiles, three-state features, aspect denominators, compatible-request summaries and frozen qualitative decisions.

## Reproducibility boundary

The included inputs reproduce the public descriptive outputs and checks. They do not reproduce the full acquisition process, private review corpus, semantic AI-assisted coding, human adjudication or source-sensitive review reprocessing. Consumer inputs are already corrected aggregates. The workflow is **AI-assisted analytical work with targeted human adjudication, manual QA and frozen outputs**, not autonomous analysis or a trained sentiment model.

Run meaningful boundary and frozen-output checks with `python -m unittest discover -s tests`. No dependency installation is required.
