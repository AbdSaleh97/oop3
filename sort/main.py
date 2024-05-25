from strategy import *

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort = BubbleSort()
    insertion_sort = InsertionSort()
    selection_sort = SelectionSort()

    context = SortContext(bubble_sort)
    print("Before Bubble Sort:", data)
    print("After Bubble Sort:", context.sort(data.copy()))

    context.set_strategy(insertion_sort)
    print("Before Insertion Sort:", data)
    print("After Insertion Sort:", context.sort(data.copy()))

    context.set_strategy(selection_sort)
    print("Before Selection Sort:", data)
    print("After Selection Sort:", context.sort(data.copy()))

