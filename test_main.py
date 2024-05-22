import unittest
from datetime import datetime
from main import calculate_age

class TestCalculateAge(unittest.TestCase):

    def test_calculate_age(self):
        test_cases = [
            ("1990-01-01", 34),  # Standard case
            ("2000-02-29", 24),  # Leap year birthdate
            (datetime.today().strftime('%Y-%m-%d'), 0),  # Birthday today
            ("1985-12-31", 38),  # End of year birthdate
            ("2023-12-31", 0),  # Edge case birthdate
            ("1820-4-10",204), # Age greather then 100
        ]
        
        for birthdate_str, expected_age in test_cases:
            with self.subTest(birthdate=birthdate_str):
                birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
                age = calculate_age(birthdate)
                self.assertEqual(age, expected_age)

if __name__ == "__main__":
    unittest.main()
