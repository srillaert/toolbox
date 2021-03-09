#!/bin/sh
gcc insert_nan_lines.c
cat insert_nan_lines.test_input.csv | ./a.out
rm a.out
