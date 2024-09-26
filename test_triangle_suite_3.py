# test_triangle_suite_3.py
# Test Suite 2: Quit Exit commands

from help_test_triangle import input_outerr

def test_3_01_quit_command(monkeypatch, capsys):
    input_list = ["Quit\n"]
    output_list = ["triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_02_quit_second_word(monkeypatch, capsys):
    input_list = ["1 Quit 3\n"]
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_03_quit_first_lowercase(monkeypatch, capsys):
    input_list = ["quit\t 2 3\n"]
    output_list = ["triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_04_quit_starts_first_word(monkeypatch, capsys):
    input_list = ["Quit1 4.3 5\n"]
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_05_exit_command(monkeypatch, capsys):
    input_list = ["Exit\n"]
    output_list = ["triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_06_Exit_second_word(monkeypatch, capsys):
    input_list = ["1 A Exit\n"]
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_07_exit_first_uppercase(monkeypatch, capsys):
    input_list = ["EXIT\t 3 2\n"]
    output_list = ["triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_08_Exit_ends_first_word(monkeypatch, capsys):
    input_list = ["1Exit 4.3 5\n"]
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_09_Valid_Invalid_Quit(monkeypatch, capsys):
    input_list = ["23 34 45.6\n", 
                  "23.4 78.4 19\n",
                  "1.0 3.567\n",
                  "Quit\n"]
    output_list = ["Scalene\n",
                   "NoTriangle\n",
                   "triangle classifier done\n"]
    error_list = ["Error: One side missing\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)


def test_3_10_Valid_Invalid_Exit(monkeypatch, capsys):
    input_list = ["   \n",
                  "3.4 5.6 3.40\n",
                 "4.8\n",
                  "5.7 5.70 5.700\n",
                  "Exit\n"]
    output_list = ["Isosceles\n"
                  "Equilateral\n",
                  "triangle classifier done\n"]
    error_list = ["Error: Three sides missing\n",
                  "Error: Two sides missing\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)
