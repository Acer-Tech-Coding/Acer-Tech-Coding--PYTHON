import unittest

from snack_counter import build_snack_counter


class SnackCounterTests(unittest.TestCase):
    def test_snacks_and_counts(self):
        box_one, box_two, shared_snacks, snack_counts, count_of_seven = build_snack_counter()

        self.assertIn("granola bar", box_one)
        self.assertIn("pretzels", box_two)
        self.assertEqual(shared_snacks, {"juice", "cookies"})
        self.assertEqual(snack_counts, [8, 2, 6, 5, 7, 3, 7, 4])
        self.assertEqual(count_of_seven, 2)


if __name__ == "__main__":
    unittest.main()
