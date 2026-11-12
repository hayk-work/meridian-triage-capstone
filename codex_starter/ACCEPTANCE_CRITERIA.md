# Ticket priority requirements

The application recommends a priority. A support lead still approves any real queue change.
It never sends a message, changes a support system, or calls an AI service at runtime.

## Input validation

Require a nonblank string id; category incident, access or question; impact single, team or
company; a Boolean blocked; and a finite, nonnegative number age_hours (not a Boolean).
manual_priority may be missing, null, P1, P2 or P3. Reject other values with ValueError.
notes may be missing and must not affect the rule. Do not modify the input object.

## Rules in order

1. Retain a valid manual_priority. rule is manual.
2. Otherwise, an incident that blocks the whole company is P1. rule is company_outage.
3. Otherwise, any blocked ticket is P2. rule is blocked.
4. Otherwise, a ticket at least 24 hours old is P2. rule is aging.
5. Otherwise, it is P3. rule is standard.

Return exactly id, priority, rule, reason and review_required. Provide a short, accurate,
human-readable reason. review_required is always Python True. Validate before applying any rule.

## Allowed work

Change triage.py and tests/test_learner.py. Read the other lab files, but keep the supplied
tests and sample data unchanged. Add at least two regression tests: one for the age boundary
and one for an additional risk or edge case you identify. Review the final changes yourself.
Keep the implementation within the supplied files and Python standard library. If you
identify a requirement issue, record its impact and your assumption in the report; preserve
the specified contract and supplied tests rather than adding dependencies or integrations.
