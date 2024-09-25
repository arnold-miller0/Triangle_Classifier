# test_triangle_suite_2.py
# Test Suite 2: Error Handling

from help_test_triangle import input_outerr

def test_2_01_missing_two_sides_only(monkeypatch, capsys):
    input_list = ["1.1\n"]
    output_list = [""]
    error_list = ["Error: Two sides missing\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_02_missing_one_sides_only(monkeypatch, capsys):
    input_list = ["5.6  10\n"]
    output_list = [""]
    error_list = ["Error: One side missing\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_03_missing_three_sides_only(monkeypatch, capsys):
    input_list = ["    \n"]
    output_list = [""]
    error_list = ["Error: Three sides missing\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_04_more_than_3_sides_numbers(monkeypatch, capsys):
    input_list = ["1 2 3.1 5.6\n"]
    output_list = [""]
    error_list = ["Error: More than Three words provided\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_05_invalid_three_non_numbers(monkeypatch, capsys):
    input_list = ["all three\t words\n"]
    output_list = [""]
    error_list = ["Error: Three sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_06_invalid_two_non_numbers(monkeypatch, capsys):
    input_list = ["only 2two\n"]
    output_list = [""]
    error_list = ["Error: Three sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_07_more_than_3_non_numbers(monkeypatch, capsys):
    input_list = ["More	1than	three3	inputs\n"]
    output_list = [""]
    error_list = ["Error: More than Three words provided\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_08_missing_one_sides_with_non_number(monkeypatch, capsys):
    input_list = ["5.6 number 10\n"]
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_09_missing_two_sides_with_1_non_number(monkeypatch, capsys):
    input_list = ["non\t    1.1\n"]
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_2_10_missing_two_sides_with_2_non_numbers(monkeypatch, capsys):
    input_list = ["1.1 non\t number\n"]
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)
