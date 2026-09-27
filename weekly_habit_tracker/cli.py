"""Command-line interface for the weekly habit tracker."""
from .tracker import HabitEntry, new_habit_entry, mark_day, unmark_day, summarize, entries_for_week
from typing import List
import sys


def demo():
    entries: List[HabitEntry] = []
    entries.append(new_habit_entry("Exercise", 32))
    entries.append(new_habit_entry("Read", 32))
    entries[0] = mark_day(entries[0], 0)  # Monday
    entries[0] = mark_day(entries[0], 2)  # Wednesday
    entries[1] = mark_day(entries[1], 1)  # Tuesday

    for e in entries_for_week(entries, 32):
        print(summarize(e))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        print("Usage: python cli.py demo")
