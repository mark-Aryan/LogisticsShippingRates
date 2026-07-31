"""
Shipping Cost Calculator
-------------------------
A simple utility to calculate shipping cost based on package weight
and a per-kilogram shipping rate.

Author: YOUR NAME
"""


def get_positive_float(prompt: str) -> float:
    """
    Prompt the user for a positive number and validate the input.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: A validated positive number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_shipping_cost(weight: float, rate: float) -> float:
    """
    Calculate the total shipping cost.

    Args:
        weight (float): Package weight in kilograms.
        rate (float): Shipping rate per kilogram (in USD).

    Returns:
        float: Total shipping cost in USD.
    """
    return round(weight * rate, 2)


def main():
    """Run the Shipping Cost Calculator program."""
    print("=== Shipping Cost Calculator ===\n")

    weight = get_positive_float("Enter the package weight in kilograms: ")
    rate = get_positive_float("Enter the shipping rate per kilogram (USD): ")

    shipping_cost = calculate_shipping_cost(weight, rate)

    print(f"\nShipping Cost: ${shipping_cost:.2f} USD")


if __name__ == "__main__":
    main()
