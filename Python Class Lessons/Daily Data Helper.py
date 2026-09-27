from enum import Enum


class DataType(Enum):
    """A simple enum for daily activity categories."""
    STUDY = "Study"
    FOOD = "Food"
    HEALTH = "Health"
    REST = "Rest"


class DailyRecord:
    """Stores one item in the daily log."""

    def __init__(self, activity, data_type=DataType.STUDY, value=0):
        self.activity = activity
        self.data_type = data_type
        self.value = value

    def display(self):
        return f"{self.activity} | {self.data_type.value} | {self.value}"


class DailyDataHelper:
    """A small helper to organize a day's records."""

    def __init__(self, date="2026-09-13", records=None):
        """Constructor: sets default values when an object is created."""
        self.date = date
        self.records = records if records is not None else []
        self.default_note = "Daily data summary"

    def add_record(self, activity, data_type=DataType.STUDY, value=0):
        """Adds a new DailyRecord item."""
        item = DailyRecord(activity, data_type, value)
        self.records.append(item)

    def show_records(self):
        """Prints all records in the daily log."""
        print(f"\nDaily Data Helper - {self.date}")
        for item in self.records:
            print(item.display())

    def search_records(self, keyword):
        """Uses enumerate() to search through records and show both index and value."""
        found = []
        for index, record in enumerate(self.records):
            if keyword.lower() in record.activity.lower() or keyword.lower() == record.data_type.value.lower():
                found.append((index, record))
        return found

    def print_search_result(self, keyword):
        """Displays the matched records with the enumerate index number and data values."""
        print(f"\nSearch results for '{keyword}':")
        results = self.search_records(keyword)
        if not results:
            print("No matching records found.")
            return

        for index, record in results:
            print(f"Index {index}: {record.display()}")

    def __del__(self):
        """Destructor: tells the user when the helper object ends."""
        print(f"\nDailyDataHelper object for {self.date} is ending.")


if __name__ == "__main__":
    helper = DailyDataHelper("2026-09-13")

    helper.add_record("Read Python notes", DataType.STUDY, 45)
    helper.add_record("Drink water", DataType.FOOD, 2)
    helper.add_record("Walk 30 minutes", DataType.HEALTH, 1)
    helper.add_record("Sleep 8 hours", DataType.REST, 8)

    helper.show_records()
    helper.print_search_result("Food")
    helper.print_search_result("rest")

    del helper
