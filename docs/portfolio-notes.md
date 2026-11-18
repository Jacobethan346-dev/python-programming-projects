# Portfolio notes

## Scope

This collection presents four small programming exercises with reproducible runs, plus a concise end-user support writing sample. Personal names, institutions, course identifiers, section numbers, assignment labels, and source dates are omitted.

## Preparation changes

| File | Changes to the portfolio copy |
| --- | --- |
| event_guide.py | Added a check for unknown event types before formatting a price or checking eligibility; made the greeting generic |
| dinner_menu_planner.py | Trimmed whitespace before matching dish names; added a main guard so importing functions does not start prompts |
| party_cost_comparison.py | Moved the existing interactive code into main() and added a main guard |
| readings_analyzer.py | Made removal safe for an empty list; added a main guard |

Core algorithms were preserved. Preparation changes, tests, and examples were developed with AI assistance.

## Behavior worth reviewing

The dinner planner counts a dish once per guest even when a guest names it repeatedly. Only dishes whose count equals the guest count are returned, sorted alphabetically.

The readings analyzer counts values strictly greater than the threshold. Removing the lowest value removes one occurrence, preserving any additional equal minimum values. An empty list is handled safely.

The event guide reuses pricing and eligibility functions across menu choices. The party comparison accumulates ingredient costs for every dish before comparing rounded totals.

## Known limits

- Numeric prompts expect valid numbers; most do not retry nonnumeric entries.
- Guest counts, ages, ingredient counts, and costs should be sensible nonnegative values; dinner examples assume at least one guest.
- Unknown event types are rejected by the interactive menu. The pricing helper itself assumes one of its documented event names.
- The party calculator uses a simple float-and-round approach.
- Automated checks verify selected behavior, not every possible input.
- The Word article is a writing sample adapted from an existing tutorial; it was not newly tested against every version of Word for Mac.
