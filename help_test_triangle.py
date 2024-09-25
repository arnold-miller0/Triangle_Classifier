# test_triangle_class.py

from triangle_classifier import main

def input_outerr(inp_list, out_list, err_list, monkeypatch, capsys):

    expect_out = "".join(out_list)
    expect_err = "".join(err_list)

    with monkeypatch.context() as m:
        m.setattr("sys.stdin", inp_list)
        main()

    captured = capsys.readouterr()
    assert expect_out == captured.out
    assert expect_err == captured.err
