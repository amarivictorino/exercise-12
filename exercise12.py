def calculate_income_tax(taxable_income):
    # Define tax brackets and rates
    first_bracket_limit = 10000
    second_bracket_limit = 20000
    rate_first_bracket = 0
    rate_second_bracket = 10
    rate_third_bracket = 20

    # Calculate income tax
    if taxable_income <= first_bracket_limit:
        income_tax = taxable_income * (rate_first_bracket / 100)
    elif taxable_income <= second_bracket_limit:
        income_tax = (taxable_income - first_bracket_limit) * (rate_second_bracket / 100)
    else:
        income_tax = (first_bracket_limit * (rate_first_bracket / 100)) + (second_bracket_limit - first_bracket_limit) * (rate_second_bracket / 100) + (taxable_income - second_bracket_limit) * (rate_third_bracket / 100)

    return income_tax

# Example usage
taxable_income = 45000
income_tax = calculate_income_tax(taxable_income)
print(f"The income tax payable for a taxable income of ${taxable_income:,} is ${income_tax:.2f}")

