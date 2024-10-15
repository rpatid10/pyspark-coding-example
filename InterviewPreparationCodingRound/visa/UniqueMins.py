from typing import List, Tuple
def unique_view_mins(intervals: List[Tuple[int, int]]) -> int:
    # Flatten the intervals into individual minutes
    view_mins= [minute for start, end in intervals for minute in range(start, end + 1)]

    # Remove duplicate minutes by converting to a set
    remove_duplicate_mins = set(view_mins)

    # Return the count of unique minutes
    return len(remove_duplicate_mins)


# Example usage
l1 = [(1, 15), (10, 18), (20, 25)]
print(unique_view_mins(l1))



