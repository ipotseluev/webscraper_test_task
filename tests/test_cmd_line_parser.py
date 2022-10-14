import pytest

import src.cmd_line_parser as cmd_line_parser


# region get_category_name

def test_get_category_name():
    expected = "test"
    args = [expected]
    parser = cmd_line_parser.Parser(args=args)
    result = parser.get_category_name()
    assert result == expected


def test_get_category_no_arguments_exits():
    args = []
    with pytest.raises(SystemExit) as e:
        cmd_line_parser.Parser(args=args)
    assert e.type == SystemExit
    assert e.value.code == 2


def test_get_category_more_than_one_arg_exits():
    cmdline = "category bla"
    args = cmdline.split()
    with pytest.raises(SystemExit) as e:
        cmd_line_parser.Parser(args=args)
    assert e.type == SystemExit
    assert e.value.code == 2

# endregion

# region get_workers_count

def test_get_workers_count_default():
    expected_count = 1
    args = ['category']
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_workers_count() == expected_count


def test_get_workers_count_short():
    expected_count = 42
    cmdline = f"category -w {expected_count}"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_workers_count() == expected_count


def test_get_workers_count_long():
    expected_count = 42
    cmdline = f"category --workers-count {expected_count}"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_workers_count() == expected_count


def test_get_workers_count_long_abbreviated():
    expected_count = 42
    cmdline = f"category --work {expected_count}"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_workers_count() == expected_count


def test_get_workers_string_arg_negative():
    cmdline = "category --work bla"
    args = cmdline.split()
    with pytest.raises(SystemExit) as e:
        cmd_line_parser.Parser(args=args)
    assert e.type == SystemExit
    assert e.value.code == 2


def test_get_workers_no_argument_negative():
    cmdline = "category --workers"
    args = cmdline.split()
    with pytest.raises(SystemExit) as e:
        cmd_line_parser.Parser(args=args)
    assert e.type == SystemExit
    assert e.value.code == 2


@pytest.mark.parametrize(
    'count',
    [0, -1]
)
def test_get_workers_less_than_1_negative(count: int):
    cmdline = f"category --workers {count}"
    args = cmdline.split()
    with pytest.raises(SystemExit) as e:
        cmd_line_parser.Parser(args=args)
    assert e.type == SystemExit
    assert e.value.code == 2

# endregion

# region get_output_file_path

def test_get_output_file_default():
    expected_file_path = "courses.csv"
    cmdline = "category"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_output_file_path() == expected_file_path


def test_get_output_file_long():
    expected_file_path = 'blah.csv'
    cmdline = f"category --output-file {expected_file_path}"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_output_file_path() == expected_file_path


def test_get_output_file_abbreviated():
    expected_file_path = 'blah.csv'
    cmdline = f"category --output {expected_file_path}"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_output_file_path() == expected_file_path


def test_get_output_file_short():
    expected_file_path = 'blah.csv'
    cmdline = f"category -o {expected_file_path}"
    args = cmdline.split()
    parser = cmd_line_parser.Parser(args=args)
    assert parser.get_output_file_path() == expected_file_path

# endregion
