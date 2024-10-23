from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(transaction, filter_result):
    assert filter_by_state(transaction) == filter_result



def test_sort_by_date(transaction, sort_result):
    assert sort_by_date(transaction) == sort_result