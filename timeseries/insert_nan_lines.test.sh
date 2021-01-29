#!/bin/bash
cat insert_nan_lines.test_input.csv | python insert_nan_lines.py > insert_nan_lines.actual_output.csv
if diff insert_nan_lines.test_output.csv insert_nan_lines.actual_output.csv; then
	echo success
else
	echo failure : actual output is different from the expected output
fi
rm insert_nan_lines.actual_output.csv
