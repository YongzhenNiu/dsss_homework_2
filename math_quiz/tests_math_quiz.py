import unittest
from math_quiz import random_generate_integer, random_choose_operator, create_problem_and_solution


class TestMathGame(unittest.TestCase):

    def test_random_generate_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_generate_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_choose_operator(self):
        # Test if random choose operator returns a valid operators.
        valid_operators = ['+', '-', '*', '/']
        for _ in range(1000):  # Run multiple times to test randomness
            result = random_choose_operator()
            self.assertIn(result, valid_operators)


    def test_create_problem_and_solution(self):
        """Test if create_problem_and_solution works as expected"""
        test_cases = [
                (5, 2, '+', '5 + 2', 3),
                (7, 3, '-', '7 - 3', 10),
                (4, 5, '*', '4 * 5', 20),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = create_problem_and_solution(num1, num2, operator)
                self.assertEqual(problem, expected_problem, 'Problem is incorrect')
                self.assertEqual(answer, expected_answer, 'Answer is incorrect')





if __name__ == "__main__":
    unittest.main()
