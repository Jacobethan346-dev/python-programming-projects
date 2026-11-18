# Python Programming Projects

Four small command-line projects demonstrating functions, dictionaries, loops, list processing, and decision-making, with reproducible examples and automated behavior checks.

## Projects

| Project | What it does | Skills demonstrated |
| --- | --- | --- |
| [Event Guide](event_guide.py) | Looks up fictional event pricing, checks age requirements, and recommends an event | Functions, Boolean logic, menu loops, decisions |
| [Dinner Menu Planner](dinner_menu_planner.py) | Finds dishes selected by every guest, counting repeated choices only once per guest | Dictionaries, normalization, deduplication, sorting |
| [Party Cost Comparison](party_cost_comparison.py) | Totals ingredients across multiple dishes and compares hosting with attending | Nested loops, running totals, formatted currency, branching |
| [Readings Analyzer](readings_analyzer.py) | Counts values above a threshold and removes one lowest reading | Lists, strict comparisons, mutation, empty-list handling |

The Event Guide and Dinner Menu Planner are the best starting points. The readings project uses fictional numeric inputs; it is not a security-monitoring product.

## Run a project

Use Python 3.9 or later. No external packages are required. From the project folder:

```sh
python3 event_guide.py
python3 dinner_menu_planner.py
python3 party_cost_comparison.py
python3 readings_analyzer.py
```

Run one command at a time and answer the prompts. Prices and event rules are fictional demonstration data. [Actual example runs](examples/example-runs.md)

## Run the checks

```sh
python3 -m unittest discover -s tests -v
```

Sixteen tests check pricing and age boundaries, recommendations, menu recovery, repeated dish choices, sorted intersections, strict thresholds, repeated minimum values, empty readings, and three cost-comparison outcomes. These copies passed the checks with Python 3.14.7.

## Application to IT support

These projects demonstrate foundational skills useful for support scripts: organizing steps into functions, summarizing values, matching input consistently, and producing readable output. They do not claim production system administration or customer support experience.

A [Word-for-Mac support writing sample](docs/word-for-mac-save-guide.md) explains a routine task and common saving problems for a novice user.

## Preparation and limits

The published copies have descriptive filenames and documented small fixes: import guards, whitespace normalization for dish choices, recovery from an unknown event type, and safe handling of an empty readings list. [Preparation details](docs/portfolio-notes.md)

These are beginner programs. They expect sensible numeric input and do not validate every malformed or negative value. The party calculator uses ordinary floating-point arithmetic for a simple demonstration, not financial accounting.

AI assistance was used in developing some code and preparing documentation, examples, and verification. Personal identifiers and source-context labels have been removed from the published files.
