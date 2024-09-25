# test_triangle_suite_1.py
# Test Suite 1: Valid Triangle Classification

from help_test_triangle import input_outerr

def test_1_01_equilateral_integer(monkeypatch, capsys):
    input_list = ["1 1 1\n"]
    output_list = ["Equilateral\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_02_isosceles_integer(monkeypatch, capsys):
    input_list = ["2  2 3\n"]
    output_list = ["Isosceles\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_03_scalene_integer(monkeypatch, capsys):
    input_list = ["5 3 4\n"]
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_04_notriangle_integer(monkeypatch, capsys):
    input_list = ["2 3 1\n"]
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_05_equilateral_float(monkeypatch, capsys):
    input_list = ["12.3\t12.3 12.3\n"]
    output_list = ["Equilateral\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_06_isosceles_float(monkeypatch, capsys):
    input_list = ["45.6 23.4 23.4 \n"]
    output_list = ["Isosceles\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_07_scalene_float(monkeypatch, capsys):
    input_list = ["3.6\t5.9\t4.8\n"]
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_08_notriangle_float(monkeypatch, capsys):
    input_list = ["7.8 1.1  2.3\n"]
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_09_notriangle_zero(monkeypatch, capsys):
    input_list = ["1.1 2\t  0.0\n"]
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_1_10_notriangle_zero(monkeypatch, capsys):
    input_list = ["7.7\t -0.13  7.8\n"]
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)
