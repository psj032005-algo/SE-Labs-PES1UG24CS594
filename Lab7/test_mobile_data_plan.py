from hypothesis import given, strategies as st
from mobile_data_plan import parse_plan, usage_average, payable_bill


# Test 1: parse_plan
@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        parse_plan(s)
    except ValueError:
        pass


# Test 2: usage_average
@given(st.text() | st.none())
def test_usage_average_no_crash(s):
    try:
        usage_average(s)
    except ValueError:
        pass


# Test 3: payable_bill
@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except ValueError:
        pass


@given(
    plan=st.text(min_size=1).filter(lambda x: ":" not in x and x.strip() != ""),
    gb=st.floats(min_value=0, max_value=10000, allow_nan=False, allow_infinity=False),
)
def test_valid_plan(plan, gb):
    name, amount = parse_plan(f"{plan}:{gb}")
    assert name == plan.strip().title()
    assert amount == gb


@given(values=st.lists(st.integers(min_value=0, max_value=100000), min_size=1))
def test_valid_usage(values):
    csv = ",".join(map(str, values))
    assert usage_average(csv) == sum(values) // len(values)


@given(
    bill=st.floats(
        min_value=0, max_value=100000, allow_nan=False, allow_infinity=False
    ),
    discount=st.floats(
        min_value=0, max_value=100000, allow_nan=False, allow_infinity=False
    ),
)
def test_valid_bill(bill, discount):
    result = payable_bill(f"{bill}|{discount}")
    assert result == max(bill * 1.18 - discount, 0)
