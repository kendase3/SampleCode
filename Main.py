from typing import List
from statistics import mean
import math
import random


class QuestionOne:
    """
        Handles FizzBuzz solution.
    """
    def __init__(self, max_num: int = 100):
        """

        :param max_num: Sets max num to which FizzBuzz is implemented; default is 100.
        """
        self.max_num = max_num + 1

    def solve(self) -> None:
        """

        :return: None. Prints each value on new lines until ``max_num``.
        """
        for count in range(1, self.max_num):
            print(self.get_value(count))

    @staticmethod
    def get_value(num: int) -> str:
        """
        Function that returns standard FizzBuzz response based on input.
        :param num: Number checked against FizzBuzz.
        :return: FizzBuzz result based on param.
        """
        if num % 15 == 0:
            return "FizzBuzz"
        elif num % 5 == 0:
            return "Buzz"
        elif num % 3 == 0:
            return "Fizz"
        else:
            return str(num)


class QuestionTwo:
    """
        Handles statistics of list of numbers, returning smallest, largest, average of list.
    """
    def solve(self, number_list: List[float]) -> None:
        """

        :param number_list: List of numbers to run statistics.
        :return: None. Prints smallest, largest, average of above param.
        """
        result = self.get_results(number_list)
        if result is None:
            print("The list you've provided is illegal.")
        else:
            for key, value in result.items():
                print(key, ":", value)

    @staticmethod
    def get_results(number_list: List[float]):
        """

        :param number_list: List of numbers to run statistics.
        :return: Dictionary of smallest, largest number, and average of all numbers.
        """
        try:
            lowest = min(number_list)
            highest = max(number_list)
            average = mean(number_list)

            return {'lowest': lowest, 'highest': highest, 'average': average}
        except ValueError:
            return None


class QuestionThree:
    """
        Supports calculation of largest prime factor of a number, if number is greater or equal to 2.
    """
    def solve(self, number: int) -> None:
        """

        :param number: Integer value being checked for its largest prime factor.
        :return: None. Prints largest prime factor of above param, if available. If not available, prints error comment.
        """
        if number > 1:
            largest_factor = self.find_largest_prime_factor(number)
            print("The largest prime factor of {0} is {1}".format(number, largest_factor))
        else:
            print("The number {0} is not supported.".format(number))

    def find_largest_prime_factor(self, upper_bound, lower_bound=2):
        """
        Recursive function used to find largest prime factor. Starting value of upper_bound is number in question.
        :param upper_bound: Upper bound for searching for prime factor. First initialization to be number in question.
        :param lower_bound: Starting point for prime factor search. Defaults to 2, but can be changed to higher numbers.
        :return:
        """
        try:
            sqrt = int(math.sqrt(upper_bound))

            for num in range(lower_bound, sqrt+1):
                if upper_bound % num == 0:
                    co_factor = int(upper_bound/num)
                    if co_factor < math.sqrt(lower_bound * upper_bound):
                        return co_factor
                    return self.find_largest_prime_factor(co_factor, lower_bound)
            return upper_bound
        except ValueError:
            return None


class QuestionFour:
    def __init__(self, seed=None):
        random.seed(seed)

    def solve(self):
        roll_results = self.roll_dice()
        print("The roll was {0} and sum is {1}".format(roll_results["roll"], roll_results["sum"]))
        if roll_results["message"] != "":
            print(roll_results["message"])

    def roll_dice(self):
        dice_roll = [random.randint(1, 6) for _ in range(2)]
        special_message = ""
        if sum(dice_roll) == 2:
            special_message = "Snake Eyes"
        elif sum(dice_roll) == 7:
            special_message = "Lucky 7"

        return {"roll": dice_roll, "sum": sum(dice_roll), "message": special_message}


def main():
    question_one = QuestionOne()
    question_two = QuestionTwo()
    question_three = QuestionThree()
    question_four = QuestionFour()

    # Arguments for calling below functions:
    q_two_list = []
    q_three_number = 1001

    print("Question 1:")
    question_one.solve()
    print("Question 2:")
    question_two.solve(q_two_list)
    print("Question 3:")
    question_three.solve(q_three_number)
    print("Question 4:")
    question_four.solve()


if __name__ == "__main__":
    main()
