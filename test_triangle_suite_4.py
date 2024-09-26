# test_triangle_suite_4.py
# Test Suite 4: : Boundary and Edge Cases

from help_test_triangle import input_outerr

def test_4_01_Exit_then_data(monkeypatch, capsys):
    input_list = ["Exit\n",
                  "3.1 5.2 8.01\n",
                  "8.01\n"] 
    output_list = ["triangle classifier done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 15 digits all same
def test_4_02_prec_15_dig_0_dec_all_same_equ(monkeypatch, capsys):
    input_list = ["999999999999999 999999999999999 999999999999999\n"]
    output_list = ["Equilateral\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 15 digits different values so Scalene
def test_4_03_prec_15_dig_0_dec_diff_tri(monkeypatch, capsys):
    input_list = ["999999999999990 999999999999991 999999999999992\n"]
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 16 digits same first 15 digits so Isosceles
def test_4_04_prec_15_dig_0_dec_first_15_same_iso(monkeypatch, capsys):
    input_list = ["9999999999999990 9999999999999991 9999999999999992\n"]
    output_list = ["Isosceles\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 17 digits same first 16 digits so Isosceles
def test_4_05_prec_17_dig_0_dec_first_16_same_iso(monkeypatch, capsys):
    input_list = ["99999999999999990 99999999999999991 99999999999999992\n"]
    output_list = ["Isosceles\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 18 digits same first 17 digits so Equilateral
def test_4_06_prec_18_dig_0_dec_first_17_same_equ(monkeypatch, capsys):
    input_list = ["999999999999999990 999999999999999991 999999999999999992\n"]
    output_list = ["Equilateral\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 15 digits 14 decimals is triangle
def test_4_07_prec_15_dig_14_dec_tri(monkeypatch, capsys):
    input_list = ["3.00000000000001 5.000 8.00\n"] # handles at 15 precision differnce
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 16 digits 15 decimals rounds no triangle
def test_4_08_prec_16_dig_15_dec_not(monkeypatch, capsys):
    input_list = ["3.000000000000001 5.000 8.00\n"] # rounds at 16 precision differnce
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 15 digits 1 decimals vs 1 digits 0 decimals is triangle
def test_4_09_prec_15_dig_1_dec_vs_15_dig_0_dec_tri(monkeypatch, capsys):
    input_list = ["567891234567893.1 5 567891234567898\n"] # handles 15 precssion differnce
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 15 digits 2 decimals vs 1 digit 0 decimal no triangle
def test_4_10_prec_15_dig_2_dec_vs_15_dec_0_dig_not(monkeypatch, capsys):
    input_list = ["567891234567893.01 5.00 567891234567898.00\n"] # rounds at 16 precision differnce
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 16 digits 0 decimal vs 1 digit 0 decimal is triangle
def test_4_11_prec_16_dig_0_dec_vs_1_dig_0_dec_tri(monkeypatch, capsys):
    input_list = ["4567891234567890 9 4567891234567898\n"] # handles 15 precision differncee
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# 15 precision 17 digits 0 decimal vs 1 digit 0 decimal no triangle
def test_4_12_prec_17_dig_0_dec_vs_1_dig_0_dec_not(monkeypatch, capsys):
    input_list = ["34567891234567890 9 34567891234567898\n"] # rounds at 16 precision differnce
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# other input formats like arrays, list, json with special-chars
def test_4_21_other_specials_error(monkeypatch, capsys):
    input_list = ["1 9 !@#$%^&*(),.<>?/\\|`~{}[]'\"\n"] # US key-board special chars
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_22_other_list_3_num_only_error(monkeypatch, capsys):
    input_list = ["[1.5, 2.4, 3.6]\n"] 
    output_list = [""]
    error_list = ["Error: Three sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_23_other_list_3_nums_letters_error(monkeypatch, capsys):
    input_list = ["[1.5, 2.4 ,'abc']\n"] 
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_24_other_xml_tag_values_error(monkeypatch, capsys):
    input_list = ["<a>triangle 12 31 23</a>\n"] 
    output_list = [""]
    error_list = ["Error: More than Three words provided\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_25_other_json_tag_values_error(monkeypatch, capsys):
    input_list = ["{a:1, b:true, c:'string'}\n"] 
    output_list = [""]
    error_list = ["Error: Three sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

# Special backspace characters and their unicode
def test_4_30_other_backspace_error(monkeypatch, capsys):
    input_list = ["7.4\u0008 1.56\b 3.89\n"] # \u0008: backspace (BS)
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_31_other_linefeed_istriangle(monkeypatch, capsys):
    input_list = ["4.7\n 1.56\n 3.89\u000a \n"] # \u000a: linefeed (LF) or New Line
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_32_other_formfeed_istriangle(monkeypatch, capsys):
    input_list = ["4.12 4.12\f 3.89\u000c \n"]  # \u000c: form feed (FF)
    output_list = ["Isosceles\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_33_other_carriage_return_notriangle(monkeypatch, capsys):
    input_list = ["7.4\r 1.56\u000d 3.89\n"] # \u000d: carriage return (CR)
    output_list = ["NoTriangle\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_34_other_double_quote_error(monkeypatch, capsys):
    input_list = ["4.12\u0022 1.56\" 3.89\n"] # \u0022: double quote (")
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_35_other_single_quote_error(monkeypatch, capsys):
    input_list = ["4.12\' 1.56\u0027 3.89\n"] # \u0027: single quote (')
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_36_other_backslash_error(monkeypatch, capsys):
    input_list = ["4.12 1.56\\ 3.89\u005c\n"] # \u005c: backslash (\)
    output_list = [""]
    error_list = ["Error: Two sides missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_37_other_unicode_A_error(monkeypatch, capsys):
    input_list = ["4.12\u0041 1.56 3.89\n"] # \u0041: letter A
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_38_other_unicode_6_istriangle(monkeypatch, capsys):
    input_list = ["4.12 1.5\u0036 3.89\n"] # \u0036: number 6 
    output_list = ["Scalene\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_4_39_other_unicode_uk_pound_error(monkeypatch, capsys):
    input_list = ["4.12 1.56 3.89\u00A3 \n"] # \u00A3: UK Pound
    output_list = [""]
    error_list = ["Error: One side missing with Non-numeric words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)
