"""CSV Test Result Analyzer - Analyze test results from CSV file."""

import csv


def read_csv(filename: str) -> list:
    """Read CSV file with test results.

    Args:
        filename: Path to CSV file

    Returns:
        List of dictionaries with test data
    """
    tests = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tests = list(reader)
    return tests


def analyze_results(tests: list) -> dict:
    """Analyze test results and calculate statistics.

    Args:
        tests: List of test result dictionaries

    Returns:
        Dictionary with test statistics
    """
    if not tests:
        return {"total": 0, "passed": 0, "failed": 0, "pass_rate": 0.0}

    total = len(tests)
    passed = sum(1 for test in tests if test["Expected"] == test["Actual"])
    failed = total - passed
    pass_rate = (passed / total * 100) if total > 0 else 0

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate
    }


def get_failed_tests(tests: list) -> list:
    """Get list of failed tests.

    Args:
        tests: List of test result dictionaries

    Returns:
        List of failed test IDs
    """
    return [test["Test_ID"] for test in tests if test["Expected"] != test["Actual"]]


def generate_summary(filename: str, stats: dict, failed: list) -> None:
    """Generate summary report file.

    Args:
        filename: Output filename for summary
        stats: Test statistics dictionary
        failed: List of failed test IDs
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Test Summary Report\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total tests: {stats['total']}\n")
        f.write(f"Passed: {stats['passed']}\n")
        f.write(f"Failed: {stats['failed']}\n")
        f.write(f"Pass rate: {stats['pass_rate']:.1f}%\n")
        f.write("\nFailed tests:\n")
        for test_id in failed:
            f.write(f"  {test_id}\n")


if __name__ == "__main__":
    test_results = read_csv("test_results.csv")
    analysis = analyze_results(test_results)
    failed_tests = get_failed_tests(test_results)

    print("Test Summary")
    print("=" * 40)
    print(f"Total tests: {analysis['total']}")
    print(f"Passed: {analysis['passed']}")
    print(f"Failed: {analysis['failed']}")
    print(f"Pass rate: {analysis['pass_rate']:.1f}%")

    if failed_tests:
        print("\nFailed tests:")
        for test_id in failed_tests:
            print(f"  {test_id}")

    generate_summary("summary.txt", analysis, failed_tests)
    print("\nSummary saved to summary.txt")
