# calculator_agent.py
import math

class CalculatorAgent:
    def __init__(self):
        pass

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b

    def sqrt(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)

    def percentage(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot calculate percentage with base as zero")
        return (a / b) * 100

    def evaluate_expression(self, expression: str) -> float:
        try:
            return eval(expression)
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}. Error: {e}")

