# Project workflow

The project began with a hypothetical entrant: which Australian automatic-feeder problem should a new pet-care brand address, for whom? A bounded category made public product, feature, price and review evidence inspectable. This was a personal research and design project, not a client engagement or a measured market-size study.

The work moved through method development (source access, identity and acquisition rules), formal supply and price analysis, review coding and audit, demand signals, a qualitative choice of direction, analytical presentation and public boundaries, product definition (users, MVP, requirements, interactions and validation) and finally an online concept presentation. Research narrows the question, design states proposed capabilities, and presentation adds no evidence. The result remains recommended for further validation, without hardware, usability or launch validation.

## Evidence layers

Public desk research uses distinct evidence grains. A canonical product represents identity; a retail listing represents a channel page; a seller offer represents seller, configuration and price conditions. Brand and feature prevalence use deduplicated products, assortment uses listings, and prices use eligible ordinary offers.

Identity resolution prioritises exact GTIN, then ASIN/MPN/exact model, then brand plus normalised model, capacity and configuration, followed by manual review. An ASIN does not resolve unverified family/variant pooling. Unresolved identity remains separate and historical conflicts remain visible.

Raw and processed layers are separate. URL, timestamp, acquisition method and field provenance are retained. Automated and manually verified acquisition both require verifiable public evidence; search snippets, unverified caches and another channel’s prices cannot fill gaps. True means explicit support, false explicit contradiction, and null unknown. Silence is not false; kilograms are not converted to litres. Price eligibility requires an in-scope valid listing, clear identity/variant, current ordinary price, AUD evidence, public URL, timestamp and provenance. Unavailable/out-of-stock prices remain in the master or validation log, outside the eligible panel.

## Product and presentation

MVP Core covers local planning, portions, execution, editing, status, recovery and maintenance under valid power/time/configuration. Connected Support offers optional App edits, status and reminders without becoming a P0 prerequisite. Battery backup is P1 but outside baseline as a supporting experiment; P2 includes conditional sensing and expanded history. Camera/audio/microchip, wet-food refrigeration and mandatory cloud are excluded from v1.

There are 36 capability decisions: 15 P0, six P1, four P2 and 11 Out of Scope. The 38 requirements have 25 P0, nine P1 and four P2—a different unit. Four surfaces are physical device, local firmware, App and cloud transport. Locally committed configuration is execution authority; an App draft is not an active device plan.

Three layers separate the immutable development source archive, the bilingual final reading layer linked through a source map, and curated public GitHub research/product documentation. Raw reviews, full internal PRD, acquisition evidence and private materials stay outside the public package.

Presentation-ready dashboard tables and specifications were prepared, but no native Tableau workbook or dashboard was ultimately built; four static Python figures generated from the same tables are the final visual layer. https://australia-pet-feeder.vercel.app presents a concept, not a purchasable product, and is built automatically from `portfolio_website/` on `main`. A later website redesign was reviewed but not adopted. The prototype and five app-screen SVGs copy the simulated low-fidelity wireframes. Public documentation is curated separately from the internal archive.

[Case study](../reports/case_study_en.md) · [Product](../product/product_overview.md)
