"""A simple calculator module - version 1."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """A basic calculator class."""

    def __init__(self):
        self.history = []

    def compute(self, op, a, b):
        if op == "add":
            result = add(a, b)
        elif op == "subtract":
            result = subtract(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = divide(a, b)
        else:
            raise ValueError(f"Unknown operation: {op}")
        self.history.append((op, a, b, result))
        return result

    def get_history(self):
        return list(self.history)

    def clear_history(self):
        self.history.clear()


def format_result(value):
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def main():
    calc = Calculator()
    print(calc.compute("add", 10, 5))
    print(calc.compute("subtract", 10, 3))
    print(calc.compute("multiply", 4, 7))
    print(format_result(calc.compute("divide", 10, 3)))
    print("History:", calc.get_history())


if __name__ == "__main__":
    main()
