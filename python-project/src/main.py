"""
Example CLI application using the mypackage module.
"""

import sys
from mypackage import Calculator, format_greeting


def main():
    """Main entry point for the CLI application."""
    print("=== Python Package Demo ===\n")

    # Greeting example
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(format_greeting(name))
    print()

    # Calculator example
    print("Calculator Examples:")
    calc = Calculator()
    
    operations = [
        (calc.add, 10, 5, "Addition"),
        (calc.subtract, 10, 5, "Subtraction"),
        (calc.multiply, 10, 5, "Multiplication"),
        (calc.divide, 10, 5, "Division"),
        (calc.power, 2, 8, "Power"),
    ]

    for func, a, b, op_name in operations:
        result = func(a, b)
        print(f"{op_name}: {a} and {b} = {result}")


if __name__ == "__main__":
    main()
