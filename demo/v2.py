"""A simple calculator module - version 2 (enhanced)."""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return math.pow(a, b)


def sqrt(a):
    """Compute square root."""
    if a < 0:
        raise ValueError("Cannot compute sqrt of negative number")
    return math.sqrt(a)


class Calculator:
    """An enhanced calculator class with undo support."""

    def __init__(self, precision=2):
        self.history = []
        self.precision = precision

    def compute(self, op, a, b=None):
        if op == "add":
            result = add(a, b)
        elif op == "subtract":
            result = subtract(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = divide(a, b)
        elif op == "power":
            result = power(a, b)
        elif op == "sqrt":
            result = sqrt(a)
        else:
            raise ValueError(f"Unknown operation: {op}")
        self.history.append({"op": op, "args": (a, b), "result": result})
        return result

    def get_history(self):
        return list(self.history)

    def clear_history(self):
        self.history.clear()

    def undo(self):
        """Remove the last operation from history."""
        if self.history:
            return self.history.pop()
        return None


def format_result(value, precision=2):
    if isinstance(value, float):
        return f"{value:.{precision}f}"
    return str(value)


def main():
    calc = Calculator(precision=4)
    print(calc.compute("add", 10, 5))
    print(calc.compute("subtract", 10, 3))
    print(calc.compute("multiply", 4, 7))
    print(format_result(calc.compute("divide", 10, 3), precision=4))
    print(calc.compute("power", 2, 10))
    print(calc.compute("sqrt", 144))
    print("History:", calc.get_history())
    calc.undo()
    print("After undo:", calc.get_history())


if __name__ == "__main__":
    main()
