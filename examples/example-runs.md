# Example runs

Outputs captured by running these copies with Python 3.14.7. All inputs are fictional. Inputs and prompts are listed separately because redirected input is not echoed.

## Event Guide

Run `python3 event_guide.py`.

Input, one answer per line:

```text
yes
18
1
music
2
fundraiser
4
relaxed
no
5
```

Captured output:

```text
Welcome to the Event Guide!
Find an event that matches your interests.
Are you a student? (yes/no):
What is your age?
1. Get ticket price for an event
2. Check if I can attend an event
3. See event details
4. Get an event recommendation
5. Quit
Which event? (music / sports / festival / fundraiser):
Ticket price: $12.00
1. Get ticket price for an event
2. Check if I can attend an event
3. See event details
4. Get an event recommendation
5. Quit
Which event? (music / sports / festival / fundraiser):
You can attend this event!
1. Get ticket price for an event
2. Check if I can attend an event
3. See event details
4. Get an event recommendation
5. Quit
How are you feeling? (energetic / relaxed):
Are you willing to spend money? (yes/no):
We recommend: festival
1. Get ticket price for an event
2. Check if I can attend an event
3. See event details
4. Get an event recommendation
5. Quit
Thank you for using our Event Guide. Have fun!
```

## Dinner Menu Planner

Run `python3 dinner_menu_planner.py`.

Input, one answer per line:

```text
2
Guest A
pasta
soup
salad
Guest B
pasta
soup
rice
```

Captured output:

```text
How many guests are coming for dinner?
What is guest #1's name?
What are Guest A's three favorite dishes?
What is guest #2's name?
What are Guest B's three favorite dishes?
For dinner, we will have:
Pasta
Soup
```

## Party Cost Comparison

Run `python3 party_cost_comparison.py`.

Input, one answer per line:

```text
10
3
Pasta
2
4
6
yes
Salad
1
5
no
```

Captured output:

```text
What is the price of the local watch party?
How many people are going (including you)?
What dish are you making for the party?
How many ingredients does it have?
How much is ingredient #1?
How much is ingredient #2?
This dish will cost $10.00.
Is there another dish?
What dish are you making for the party?
How many ingredients does it have?
How much is ingredient #1?
This dish will cost $5.00.
Is there another dish?
Hosting your own party will be cheaper than attending one!
```

## Readings Analyzer

Run `python3 readings_analyzer.py`.

Input, one answer per line:

```text
4
5
2
8
9
5
```

Captured output:

```text
How many security readings were intercepted? Enter a security reading: Enter a security reading: Enter a security reading: Enter a security reading: Enter the threshold: Original security readings: 5 2 8 9
Readings above 5: 2
After removing the lowest reading: 5 8 9
```
