# test_sample_loop.py

from sample_loop import main

def input_outerr(inp_list, out_list, err_list, monkeypatch, capsys):

    expect_out = "".join(out_list)
    expect_err = "".join(err_list)

    with monkeypatch.context() as m:
        m.setattr("sys.stdin", inp_list)
        main()

    captured = capsys.readouterr()
    assert expect_out == captured.out
    assert expect_err == captured.err


def test_valid_input(monkeypatch, capsys):
    input_list = ["apple banana cherry\n"]
    output_list = ["Success: input has 3 words\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)


def test_invalid_input_less_than_3_words(monkeypatch, capsys):
    input_list = ["apple\tbanana\n"]
    output_list = [""]
    error_list = ["Error: input has 2 words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)


def test_invalid_input_more_than_3_words(monkeypatch, capsys):
    input_list = ["apple banana cherry grape\n"]
    output_list = [""]
    error_list = ["Error: input has 4 words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)


def test_exit_command(monkeypatch, capsys):
    input_list = ["exit\n"]
    output_list = ["done\n"]
    error_list = [""]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_invalid_no_words(monkeypatch, capsys):
    input_list = ["\t \t\n"]
    output_list = [""]
    error_list = ["Error: input has 0 words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)
    
def test_2_inp_valid_invalid(monkeypatch, capsys):
    input_list = ["apple banana cherry\n",
                  " Words two\n"]
    output_list = ["Success: input has 3 words\n"]
    error_list = ["Error: input has 2 words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_3_inp_invalid_valid_invalid(monkeypatch, capsys):
    input_list = ["two words\n",
                  "duck duck goose\n",
                  "mpre duck duck goose\n"]
    output_list = ["Success: input has 3 words\n"]
    error_list = ["Error: input has 2 words\n",
                  "Error: input has 4 words\n"]
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)


def list_via_file(filename):
    list = []
    with open(filename,'r') as file:
        lines = file.readlines()
        for line in lines:
            list.append(line) 
    return list
    
def test_file_1_values(monkeypatch, capsys):
    input_list = list_via_file('sample_1_inp.dat')
    output_list = list_via_file('sample_1_out.dat')
    error_list = list_via_file('sample_1_err.dat')
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)

def test_file_2_values(monkeypatch, capsys):
    input_list = list_via_file('sample_2_inp.dat')
    output_list = list_via_file('sample_2_out.dat')
    error_list = list_via_file('sample_2_err.dat')
    input_outerr(input_list, output_list, error_list, monkeypatch, capsys)