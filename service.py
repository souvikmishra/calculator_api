def add(first_num: int, second_num: int) -> int:
    return first_num + second_num


def subtract(first_num: int, second_num: int) -> int:
    return first_num - second_num


def divide(first_num: int, second_num: int) -> float:
    try:
        result = first_num / second_num
    except ZeroDivisionError:
        result = "can't divide with zero you dumb ass"
    return result


def multiply(first_num: int, second_num: int) -> int:
    return first_num * second_num


class OperationService:

    @staticmethod
    def calculate(data):
        print(data)
        # if operator == "+":
        #     return add(first_num, last_num)
        # elif operator == "-":
        #     return add(first_num, last_num)
        # elif operator == "*":
        #     return add(first_num, last_num)
        # elif operator == "/":
        #     return add(first_num, last_num)
        # else:
        #     return "Invalid Parameters"
