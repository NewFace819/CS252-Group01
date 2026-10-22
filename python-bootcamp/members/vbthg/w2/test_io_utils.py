"""Exercise CSV failures and JSON fidelity beyond the instructor's samples."""

import json
from datetime import date

import pytest

from members.vbthg.w2.io_utils import load_tasks, save_json
from members.vbthg.w2.models import Task

HEADER = "title,importance,effort_h,deadline\n"


def test_bom_quoted_title_and_json_fields(tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_text(HEADER + '"Study, café",5,1.5,2026-10-30\n', encoding="utf-8-sig")
    tasks = load_tasks(source)
    assert tasks == [Task("Study, café", 5, 1.5, date(2026, 10, 30))]
    target = tmp_path / "tasks.json"
    save_json(tasks, target)
    assert json.loads(target.read_text(encoding="utf-8")) == [{
        "title": "Study, café", "importance": 5, "effort_h": 1.5, "deadline": "2026-10-30",
    }]


@pytest.mark.parametrize("row", [
    "Study,6,1,2026-10-30", "Study,abc,1,2026-10-30",
    "Study,3,bad,2026-10-30", "Study,3,-1,2026-10-30",
    "Study,3,nan,2026-10-30", "Study,3,inf,2026-10-30",
    "Study,3,1,2026-02-30", "Study,3,1,20261030",
    ",3,1,2026-10-30", "Study,3,1", "Study,3,1,2026-10-30,extra",
    '"unterminated,3,1,2026-10-30', "",
])
def test_bad_rows_report_line_three(tmp_path, row):
    source = tmp_path / "bad.csv"
    source.write_text(HEADER + "Valid,3,1,2026-10-30\n" + row + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="^line 3:"):
        load_tasks(source)


@pytest.mark.parametrize("content", ["", "title,effort_h,importance,deadline\n"])
def test_missing_or_wrong_header(tmp_path, content):
    source = tmp_path / "bad.csv"
    source.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError, match="^line 1:"):
        load_tasks(source)


def test_multiline_record_preserves_physical_line_numbers(tmp_path):
    source = tmp_path / "multiline.csv"
    source.write_text(HEADER + '"Two\nlines",3,1,2026-10-30\nBad,9,1,2026-10-30\n',
                      encoding="utf-8")
    with pytest.raises(ValueError, match="^line 4:"):
        load_tasks(source)


def test_empty_collection_round_trip(tmp_path):
    source = tmp_path / "empty.csv"
    source.write_text(HEADER, encoding="utf-8")
    assert load_tasks(source) == []
    target = tmp_path / "empty.json"
    save_json([], target)
    assert json.loads(target.read_text(encoding="utf-8")) == []


def test_zero_effort_is_valid(tmp_path):
    source = tmp_path / "zero.csv"
    source.write_text(HEADER + "Done,1,0,2026-10-30\n", encoding="utf-8")
    assert load_tasks(source)[0].effort_h == 0


def test_missing_file_remains_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_tasks(tmp_path / "missing.csv")
