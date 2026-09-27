"""Practice sets and lists with a school snack counter."""


def build_snack_counter():
    """Create snack boxes and calculate the final snack counts."""
    box_one = {"chips", "juice", "cookies"}
    box_two = {"juice", "cookies", "fruit"}

    box_one.add("granola bar")
    box_two.add("pretzels")

    shared_snacks = box_one & box_two

    snack_counts = [4, 7, 3, 7, 5]
    snack_counts.append(6)
    snack_counts.extend([2, 8])
    count_of_seven = snack_counts.count(7)
    snack_counts.reverse()

    return box_one, box_two, shared_snacks, snack_counts, count_of_seven


def main():
    box_one, box_two, shared_snacks, snack_counts, count_of_seven = build_snack_counter()

    print("===== SCHOOL SNACK COUNTER =====")
    print("Snack box 1:", box_one)
    print("Snack box 2:", box_two)
    print("Shared snacks:", shared_snacks)
    print("Final snack counts:", snack_counts)
    print("Number of snacks with a count of 7:", count_of_seven)


if __name__ == "__main__":
    main()
