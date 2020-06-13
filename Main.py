from typing import List, Dict
from statistics import mean


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
    @staticmethod
    def solve(number_list: List[float]):
        try:
            lowest = min(number_list)
            highest = max(number_list)
            average = mean(number_list)

            return {'lowest': lowest, 'highest': highest, 'average': average}
        except ValueError:
            return None


class QuestionThree:
    def solve(self):
        pass


class QuestionFour:
    def solve(self):
        pass


def main():
    question_one = QuestionOne
    question_two = QuestionTwo
    question_three = QuestionThree
    question_four = QuestionFour

    question_one.solve()
    question_two.solve()
    question_three.solve()
    question_four.solve()


if __name__ == "__main__":
    main()
