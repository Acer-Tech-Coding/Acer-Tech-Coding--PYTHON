"""Weekly Habit Tracker

Core module using tuples as main data structure.
"""
from typing import Tuple, List

# A HabitEntry is a tuple: (habit_name, week_number, days_completed)
# days_completed is a tuple of 7 booleans for Monday..Sunday
HabitEntry = Tuple[str, int, Tuple[bool, bool, bool, bool, bool, bool, bool]]


def new_habit_entry(name: str, week: int) -> HabitEntry:
    """Create a new habit entry with all days set to False."""
    return (name, week, (False, False, False, False, False, False, False))


def mark_day(entry: HabitEntry, day_index: int) -> HabitEntry:
    """Return a new HabitEntry with the day at day_index set to True.

    day_index: 0..6 for Monday..Sunday
    """
    name, week, days = entry
    if not (0 <= day_index <= 6):
        raise IndexError("day_index must be between 0 and 6")
    days_list = list(days)
    days_list[day_index] = True
    return (name, week, tuple(days_list))


def unmark_day(entry: HabitEntry, day_index: int) -> HabitEntry:
    """Return a new HabitEntry with the day at day_index set to False."""
    name, week, days = entry
    if not (0 <= day_index <= 6):
        raise IndexError("day_index must be between 0 and 6")
    days_list = list(days)
    days_list[day_index] = False
    return (name, week, tuple(days_list))


def progress(entry: HabitEntry) -> float:
    """Return completion ratio 0..1 for the week."""
    _, _, days = entry
    return sum(1 for d in days if d) / 7.0


def summarize(entry: HabitEntry) -> str:
    name, week, days = entry
    days_str = ''.join(['✅' if d else '⬜' for d in days])
    pct = int(progress(entry) * 100)
    return f"{name} (Week {week}): {days_str} {pct}%"


def entries_for_week(entries: List[HabitEntry], week: int) -> List[HabitEntry]:
    return [e for e in entries if e[1] == week]


if __name__ == "__main__":
    # quick demo
    e = new_habit_entry("Exercise", 32)
    e = mark_day(e, 0)
    e = mark_day(e, 2)
    print(summarize(e))
