import Main
import unittest
from ddt import ddt, data

from statistics import mean


@ddt
class Tester(unittest.TestCase):

    def setUp(self):
        self.q_one = Main.QuestionOne()
        self.q_two = Main.QuestionTwo()
        self.q_three = Main.QuestionThree()
        self.q_four = Main.QuestionFour()

    @data(3, 6, 12, 99)
    def test_q_one_correctly_returns_fizz(self, sample_value):
        self.assertTrue(self.q_one.get_value(sample_value) == "Fizz")

    @data(5, 10, 50, 100)
    def test_q_one_correctly_returns_buzz(self, sample_value):
        self.assertTrue(self.q_one.get_value(sample_value) == "Buzz")

    @data(15, 30, 75, 90)
    def test_q_one_correctly_returns_fizzbuzz(self, sample_value):
        self.assertTrue(self.q_one.get_value(sample_value) == "FizzBuzz")

    @data(15, 30, 45, 60)
    def test_q_one_doesnt_switch_fizzbuzz_with_fizz_or_buzz(self, sample_value):
        self.assertTrue(self.q_one.get_value(sample_value) != "Fizz" and
                        self.q_one.get_value(sample_value) != "Buzz")

    @data(1, 2, 4, 8, 88, 98)
    def test_q_one_correctly_returns_numbers(self, sample_value):
        self.assertTrue(self.q_one.get_value(sample_value) == str(sample_value))

    @data([1, 2, 3], [-1, 0, 1], [0], [1.2, 1.4, -0.01])
    def test_q_two_correctly_returns_lowest_number(self, number_list):
        self.assertTrue(self.q_two.get_results(number_list)['lowest'] == min(number_list))

    @data([1, 2, 3], [-1, 0, 1], [0], [1.2, 1.4, -0.01])
    def test_q_two_correctly_returns_highest_number(self, number_list):
        self.assertTrue(self.q_two.get_results(number_list)['highest'] == max(number_list))

    @data([1, 2, 3], [-1, 0, 1], [0], [1.2, 1.4, -0.01])
    def test_q_two_correctly_returns_average_number(self, number_list):
        self.assertTrue(self.q_two.get_results(number_list)['average'] == mean(number_list))

    @data([])
    def test_q_two_correctly_handles_empty_lists(self, number_list):
        self.assertTrue(self.q_two.get_results(number_list) is None)

    @data([2, 2], [4, 2], [15, 5], [9, 3], [45, 5], [600851475143, 6857])
    def test_q_three_correctly_returns_largest_prime_factor(self, sample_values):
        self.assertTrue(self.q_three.find_largest_prime_factor(sample_values[0]) == sample_values[1])

    @data(45, 2, 321)
    def test_q_three_returns_result_that_is_a_factor(self, sample_value):
        self.assertTrue(sample_value % self.q_three.find_largest_prime_factor(sample_value) == 0)

    @data(2, 4, 78, 300)
    def test_q_three_returns_result_that_is_prime(self, sample_value):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        self.assertTrue(self.q_three.find_largest_prime_factor(sample_value) in prime_list)

    @data([2, [1, 1]], [3, [2, 5]])
    def test_q_four_can_output_values_of_dice(self, sample_values):
        temp_q = Main.QuestionFour(sample_values[0])
        roll_results = temp_q.roll_dice()
        self.assertTrue(roll_results["roll"] == sample_values[1])

    @data([2, [1, 1]], [3, [2, 5]])
    def test_q_four_can_output_sum_of_dice(self, sample_values):
        temp_q = Main.QuestionFour(sample_values[0])
        roll_results = temp_q.roll_dice()
        self.assertTrue(roll_results["sum"] == sum(sample_values[1]))

    @data([2, [1, 1]])
    def test_q_four_can_print_snake_eyes(self, sample_values):
        temp_q = Main.QuestionFour(sample_values[0])
        roll_results = temp_q.roll_dice()
        self.assertTrue(roll_results["message"] == "Snake Eyes")

    @data([3, [2, 5]])
    def test_q_four_can_print_lucky_seven(self, sample_values):
        temp_q = Main.QuestionFour(sample_values[0])
        roll_results = temp_q.roll_dice()
        self.assertTrue(roll_results["message"] == "Lucky 7")


if __name__ == "__main__":
    unittest.main()
