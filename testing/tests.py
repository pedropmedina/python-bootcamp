import unittest

from activities import eat, is_funny, nap


class ActivityTest(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because it is healthy",
        )

    def test_eat_unhealthy(self):
        """eat should indicate unhealthy eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, and I don't care.",
        )

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")

    def test_long_nap(self):
        """short naps should be discouraging"""
        self.assertEqual(
            nap(3), "Ugh I overslept. I didn't mean to nap for 3 hour."
        )

    def test_is_funny_tim(self):
        # self.assertEqual(is_funny("tim"), False)
        self.assertFalse(is_funny("tim"), "Tim should not be funny")

    def test_is_funny_anyone_else(self):
        """anyone else, but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")


if __name__ == "__main__":
    unittest.main()
