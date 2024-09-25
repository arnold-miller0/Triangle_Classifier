# test_triangle_general.py
# General test trianle application
# Use to create the test suite files

from help_test_triangle import input_outerr

def test_scalene_ints(monkeypatch, capsys):
    input_list = ["10 5 12\n"]
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_scalene_float(monkeypatch, capsys):
    input_list = ["10.1 5.2 15.03\n"]
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_isosceles_mix(monkeypatch, capsys):
    input_list = ["10.0 10 15.03\n"]
    output_list = ["Isosceles\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_equilateral_quit(monkeypatch, capsys):
    input_list = ["10.0 10 10.000\n", "QUIT\n"]
    output_list = ["Equilateral\n", "triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_scalene_exit(monkeypatch, capsys):
    input_list = ["7 +14 11\n", "exit\n"]
    output_list = ["Scalene\n", "triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_notriangle_only(monkeypatch, capsys):
    input_list = ["71.5 140.3 30.6\n"]
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_notriangle_neg(monkeypatch, capsys):
    input_list = ["71.5 -0.1 30.6\n"]
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_one_two_only_nums(monkeypatch, capsys):
    input_list = ["2.3\n", "2 3.4\n"]
    output_list = [""]
    error_list = ["Error: Two sides missing\n",
                  "Error: One side missing\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_one_two_nums_with(monkeypatch, capsys):
    input_list = ["2.3 Quit\n", "2 3.4 hello\n", "Ef Quit 5.6\n"]
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n",
                  "Error: One side missing with Non-numeric words\n",
                  "Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_zero_nums_with(monkeypatch, capsys):
    input_list = ["    \n", "hello\n", "one two three", "Exitor Quit\n", ]
    output_list = [""]
    error_list = ["Error: Three sides missing\n",
                  "Error: Three sides missing with Non-numeric words\n",
                  "Error: Three sides missing with Non-numeric words\n",
                  "Error: Three sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_morethan_three(monkeypatch, capsys):
    input_list = ["11 8 7 6", "-1.0 7.5 +9.0 word\n", "Exit"]
    output_list = ["triangle classifier done\n"]
    error_list = ["Error: More than Three words provided\n",
                  "Error: More than Three words provided\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_float_round(monkeypatch, capsys):
    input_list = ["3.0 5.00 8.00",
                  "3.00000000001 5.000 8.00\n", # 11 decimals
                  "3.000000000001 5.000 8.00\n", # 12 decimals
                  "3.0000000000001 5.000 8.00\n", # 13 decimals
                  "3.00000000000001 5.000 8.00\n", # 14 decimals
                  "3.000000000000001 5.000 8.00\n", # 15 decimals
                  "Exit"]
    output_list = ["NoTriangle\n", "Scalene\n", "Scalene\n",
                   "Scalene\n", "Scalene\n", "NoTriangle\n",
                   "triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def list_via_file(filename):
    list = []
    with open(filename,'r') as file:
        lines = file.readlines()
        for line in lines:
            list.append(line) 
    return list
    
def test_file_1_quit(monkeypatch, capsys):
    input_list = list_via_file('triangle_1_inp.dat')
    output_list = list_via_file('triangle_1_out.dat')
    error_list = list_via_file('triangle_1_err.dat')
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_file_2_exit(monkeypatch, capsys):
    input_list = list_via_file('triangle_2_inp.dat')
    output_list = list_via_file('triangle_2_out.dat')
    error_list = list_via_file('triangle_2_err.dat')
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)