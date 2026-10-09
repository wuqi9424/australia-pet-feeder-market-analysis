# PRD Summary

This public summary selects requirements, states, acceptance intentions and open questions from the frozen internal PRD. The internal PRD contains 38 requirements and 42 acceptance criteria; neither is implemented or passed. Full requirement and criterion ledgers are excluded from this repository. Portion ranges, clock tolerances, repetitions, food and maintenance protocols still require approval.

MVP Core covers local planning, portions, execution, editing, status, recovery and maintenance under valid power/time/configuration. Connected Support offers optional App edits, status and reminders without becoming a P0 prerequisite. Battery backup is P1 but outside baseline as a supporting experiment; P2 includes conditional sensing and expanded history. Camera/audio/microchip, wet-food refrigeration and mandatory cloud are excluded from v1.

There are 36 capability decisions: 15 P0, six P1, four P2 and 11 Out of Scope. The 38 requirements have 25 P0, nine P1 and four P2—a different unit. Four surfaces are physical device, local firmware, App and cloud transport. Locally committed configuration is execution authority; an App draft is not an active device plan.

Dispense Attempt ≠ Delivery Confirmation ≠ Pet Consumption. The 13 states/events/overlays do not form a linear success ladder. Scheduled/Pending describe intention and waiting; command, motor and attempt only describe execution evidence. Delivery Confirmed is conditional on validated sensing coverage. Delivery Unconfirmed explicitly preserves unknown output.

Potential Failure needs known errors/bounded evidence; Not executed needs valid clock/occurrence evidence. Offline and Sync Pending are connection/synchronisation overlays, not automatic feeding failures. Recovered/Synced confirms a specified recovery object; notification is not delivery. No Feeding Success Rate is defined.

Validation has four layers: concept/comprehension, prototype tasks, hardware dispensing reliability and offline/recovery, with conditional price/channel tests. All 26 records are planned/unexecuted; success_observation defines what to look for, not observed success.

Approve food, portion, timing, repetitions, safety procedures and interfaces before acceptance. Independent output measurements must check device logs. Priorities include Delivery unconfirmed comprehension, unaided setup, network/power recovery, duplicates/nonexecution, maintenance safety, request acknowledgement and version conflicts. AUD149–199 and specialist/Amazon routes test purchasing response and economics, not validated WTP or profitability. Recruitment, sample size, costs, permissions, storage/consent and key policies remain open.

Selected requirements: FR-001 persistent local plan; FR-002 scheduled execution; FR-009 acknowledgement-gated remote edits; SR-001 truthful status; ERR-003 reboot/power recovery; ERR-012 safe overrides/maintenance. Acceptance checks require inspected durable state, no blind replay, matching request/version acknowledgement, no unsupported output claims and safe maintenance under approved protocols. These are test intentions, not passed tests. Full internal requirement/criterion ledgers remain local.

[Full case study](../reports/case_study_en.md) · [Methodology](../docs/methodology.md) · [Live concept](https://australia-pet-feeder.vercel.app)

AI-assisted documentation; human-owned scope and interpretation. No raw reviews or internal acquisition evidence are included.
