
class QuestionOne:
    def solve(self):
        for count in range(1, 101):
            print(self.get_value(count))

    def get_value(self, count: int) -> str:
        if count % 15 == 0:
            return "FizzBuzz"
        elif count % 5 == 0:
            return "Buzz"
        elif count % 3 == 0:
            return "Fizz"
        else:
            return str(count)


class QuestionTwo:
    def solve(self):
        pass


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
