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


def unpack_data(data):
    first_num, second_num = data["inputs"].values()
    operator = data["operator"]
    return first_num, second_num, operator


class OperationService:

    @staticmethod
    def calculate(data):
        first_num, second_num, operator = unpack_data(data)
        if operator == "+":
            return add(first_num, second_num)
        elif operator == "-":
            return subtract(first_num, second_num)
        elif operator == "*":
            return multiply(first_num, second_num)
        elif operator == "/":
            return divide(first_num, second_num)
        else:
            return "Invalid Parameters"
