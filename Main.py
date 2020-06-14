from typing import List
from statistics import mean
import math
import random


class QuestionOne:
    def solve(self):
        for count in range(1, 101):
            print(self.get_value(count))

    @staticmethod
    def get_value(count: int) -> str:
        if count % 15 == 0:
            return "FizzBuzz"
        elif count % 5 == 0:
            return "Buzz"
        elif count % 3 == 0:
            return "Fizz"
        else:
            return str(count)


class QuestionTwo:
    def solve(self, number_list: List[float]):
        result = self.get_results(number_list)
        if result is None:
            print("The list you've provided is illegal.")
        else:
            for key, value in result.items():
                print(key, ":", value)

    @staticmethod
    def get_results(number_list: List[float]):
        try:
            lowest = min(number_list)
            highest = max(number_list)
            average = mean(number_list)

            return {'lowest': lowest, 'highest': highest, 'average': average}
        except ValueError:
            return None


class QuestionThree:
    def solve(self, number: int):
        if number > 1:
            largest_factor = self.find_largest_prime_factor(number)
            print("The largest prime factor of {0} is {1}".format(number, largest_factor))
        else:
            print("The number {0} is not supported.".format(number))

    def find_largest_prime_factor(self, upper_bound, lower_bound=2):
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
