import sys
sys.path.append("src")

import os
import csv
from fixdates.main import fix_month_name

def read_sample_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def test_fix_month_name(filename="fixable_month_names.csv"):
    sample_data = read_sample_data("tests/data/" + filename)
    failed_results = []

    for row in sample_data:
        date_column = row[0]
        expected_result = row[1]

        # Assuming 'fixdate' function processing and validation
        result = fix_month_name(date_column)

        if result != expected_result.strip():
            failed_results.append((date_column, expected_result, result))

    if failed_results:
        # Save failed results to a file in reports directory
        os.makedirs("tests/reports", exist_ok=True)
        report_file = "tests/reports/fixable_dates_failures.txt"
        with open(report_file,"w") as file:
            file.write("Failed results:\n")
            for failed_result in failed_results:
                file.write(f"{failed_result[0]} --> Expected: {failed_result[1]}, Actual: {failed_result[2]}\n")

        assert False, f"Failed results saved to {report_file}"