from automated_clean_code.exercise_20_histlib import count_key, fill_up_histogram


def test_fill_up_histogram():
    count = {}
    args = "hello"
    test_result = fill_up_histogram(count, args)
    assert test_result["h"] == 1
    assert test_result["e"] == 1
    assert test_result["l"] == 2
    assert test_result["o"] == 1


def test_count_key():
    count = {}
    args = "hello"
    count = fill_up_histogram(count, args)
    assert count_key(count) == {"l": 1, "o": 2}
