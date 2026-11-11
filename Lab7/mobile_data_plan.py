
import math


def parse_plan(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if text.count(':') != 1:
        raise ValueError("Expected format: plan:data")

    plan, gb = text.split(':')

    if not plan.strip() or not gb.strip():
        raise ValueError("Plan name and data amount are required")

    try:
        gb = float(gb)
    except ValueError:
        raise ValueError("Data amount must be numeric") from None

    if not math.isfinite(gb) or gb < 0:
        raise ValueError("Data amount must be finite and non-negative")

    return plan.strip().title(), gb


def usage_average(usage_csv):
    if not isinstance(usage_csv, str):
        raise ValueError("Input must be a string")

    parts = usage_csv.split(',')

    if not parts or any(not p.strip() for p in parts):
        raise ValueError("Usage values cannot be empty")

    try:
        values = [int(r.strip()) for r in parts]
    except ValueError:
        raise ValueError("Usage must contain integers only") from None

    if any(v < 0 for v in values):
        raise ValueError("Usage cannot be negative")

    return sum(values) // len(values)


def payable_bill(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if text.count('|') != 1:
        raise ValueError("Expected format: bill|discount")

    bill, discount = text.split('|')

    if not bill.strip() or not discount.strip():
        raise ValueError("Bill and discount are required")

    try:
        bill = float(bill)
        discount = float(discount)
    except ValueError:
        raise ValueError("Bill and discount must be numeric") from None

    if not math.isfinite(bill) or not math.isfinite(discount):
        raise ValueError("Values must be finite numbers")

    if bill < 0 or discount < 0:
        raise ValueError("Bill and discount cannot be negative")

    total = bill * 1.18 - discount
    return max(total, 0)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter plan:data in GB (e.g. standard:5): ")

    try:
        result = parse_plan(user_input)
        print("Plan and Data:", result)
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running usage_average ====")
    user_input = input("Enter daily usage in MB as CSV (e.g. 300,450,800): ")

    try:
        result = usage_average(user_input)
        print("Average Usage:", result)
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 399|50): ")

    try:
        result = payable_bill(user_input)
        print("Payable Bill:", result)
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
