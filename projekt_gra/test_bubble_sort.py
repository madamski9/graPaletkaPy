from bubble_sort import bubble_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1, 7, 3, 6, 1]) == [7, 6, 3, 1]
    assert bubble_sort([7, 7, 7, 7, 7]) == [7]
    assert bubble_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    