from freeze_one import freeze_one


def test_freeze_one():
    line = freeze_one("freeze_one")

    assert "freeze_one" in line
