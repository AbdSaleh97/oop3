import pytest
from sort.strategy import *

# Sample data for testing
data_unsorted = [64, 34, 25, 12, 22, 11, 90]
data_sorted = [11, 12, 22, 25, 34, 64, 90]
data_empty = []
data_single = [5]
data_identical = [7, 7, 7, 7]

@pytest.fixture
def context():
    return SortContext(BubbleSort())

def test_bubble_sort(context):
    context.set_strategy(BubbleSort())
    assert context.sort(data_unsorted.copy()) == data_sorted
    assert context.sort(data_empty.copy()) == data_empty
    assert context.sort(data_single.copy()) == data_single
    assert context.sort(data_identical.copy()) == data_identical

def test_insertion_sort(context):
    context.set_strategy(InsertionSort())
    assert context.sort(data_unsorted.copy()) == data_sorted
    assert context.sort(data_empty.copy()) == data_empty
    assert context.sort(data_single.copy()) == data_single
    assert context.sort(data_identical.copy()) == data_identical

def test_selection_sort(context):
    context.set_strategy(SelectionSort())
    assert context.sort(data_unsorted.copy()) == data_sorted
    assert context.sort(data_empty.copy()) == data_empty
    assert context.sort(data_single.copy()) == data_single
    assert context.sort(data_identical.copy()) == data_identical

if __name__ == "__main__":
    pytest.main()
