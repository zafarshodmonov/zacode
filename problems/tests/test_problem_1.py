import pytest

# Example for Problem 1

@pytest.mark.parametrize("input_data,expected_output", [
    ("2 3\n", "5\n"),
    ("10 20\n", "30\n"),
])
def test_problem_1(input_data, expected_output):
    from problems.solutions.problem_1 import solve
    assert solve(input_data) == expected_output
