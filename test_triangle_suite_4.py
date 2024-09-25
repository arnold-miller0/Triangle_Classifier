# test_triangle_suite_4.py
# Test Suite 4: : Boundary and Edge Cases

from help_test_triangle import input_outerr

def test_4_01_very_large_intergers(monkeypatch, capsys):
    input_list = ["999999999 999999999 999999999\n"]
    output_list = ["Equilateral\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_02_float_round_scalene(monkeypatch, capsys):
    input_list = ["3.00000000000001 5.000 8.00\n"] # handles 14 decimals
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_03_float_round_notriangle(monkeypatch, capsys):
    input_list = ["3.000000000000001 5.000 8.00\n"] # rounds at 15 decimals
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)
