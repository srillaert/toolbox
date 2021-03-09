#!/bin/sh
cat insert_nan_lines.test_input.csv | python insert_nan_lines.py | diff - insert_nan_lines.test_output.csv
