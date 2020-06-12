import Main
import unittest


class Tester(unittest.TestCase):

    def setUp(self):
        self.q_one = Main.QuestionOne()
        self.q_two = Main.QuestionTwo()
        self.q_three = Main.QuestionThree()
        self.q_four = Main.QuestionFour()

    def q_one_correctly_returns_fizz(self):
        pass

    def q_one_correctly_returns_buzz(self):
        pass

    def q_one_correctly_returns_fizzbuzz(self):
        pass

    def q_one_doesnt_switch_fizzbuzz_with_fizz_or_buzz(self):
        pass

    def q_one_correctly_returns_numbers(self):
        pass

    def q_two_correctly_returns_lowest_number(self):
        pass

    def q_two_correctly_returns_highest_number(self):
        pass

    def q_two_correctly_returns_average_number(self):
        pass

    def q_three_correctly_returns_largest_prime_factor(self):
        pass

    def q_three_returns_result_that_is_a_factor(self):
        pass

    def q_three_returns_result_that_is_prime(self):
        pass

    def q_four_can_output_values_and_sum_of_dice(self):
        pass

    def q_four_can_print_snake_eyes(self):
        pass

    def q_four_can_print_lucky_seven(self):
        pass
