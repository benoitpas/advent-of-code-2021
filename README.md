# advent-of-code-2021

[![Build Status](https://travis-ci.com/benoitpas/advent-of-code-2021.svg?branch=main)](https://app.travis-ci.com/benoitpas/advent-of-code-2021)

my solutions for https://adventofcode.com/2021

I initially decided to use python but for the first puzzles I used a spreadsheet as it did the job quickly and efficiently ;-).

# Day 1
All spreadsheets !

# Day 2
Same !

# Day 3
Still can do part 1 with spreadsheet but part 2 is so much easier with recursion that I use python

# Day 4
Python again but trying to be more idiomatic than in day 3 and using generators.
They are quite a pain to debug as they are lazy but with no caching, i.e. can only be evaluated once. Feel a bit like a half baked lazy list implementation. I can certainly understand it is more efficient to execute but to quickly develop a working solution, it is probably better to stick to lists. And then optimize with generators if necessary.

I'm getting a better grasp of the VS code debug mode for Python which is actually great.

# Day 5
side effects galore ! tripped by .sort()

# Day 6
nice one

# Day 7
All with the spreadsheet

# Day 8
part1 with spreadsheet, part 2 with python (brute force, not really smart)

# Day 9
Part 1 could have been done with a spreadsheet but as I had doubt for part 2 I did all in Python.

# Day 10
I'm getting the hang of python, there are still a few things that annoy me like:
* mutable operations on collections, like [reverse](https://github.com/benoitpas/advent-of-code-2021/blob/939d2329301b6a4736aebb6bad5955aa459dc4f5/day10.py#L24) or [sort](https://github.com/benoitpas/advent-of-code-2021/blob/939d2329301b6a4736aebb6bad5955aa459dc4f5/day10.py#L39) on a list.
* also because it is an interpreted language, I only find out if I forgot the '()' at the end of ``reverse()`` or ``sort()`` when I run the program. That wouldn't happen with a statically typed language.

Anyway, I think I still prefer immutable collections, operations are more succinct and less error prone.