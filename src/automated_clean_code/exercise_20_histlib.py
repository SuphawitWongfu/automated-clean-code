# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt

max_k = str
min_k = str
max_c = int
min_c = int


def count_key(counter: dict[str:int]) -> (max_k, max_c, min_k, min_c):
    """Count the key for max and min."""
    max_key = None
    min_key = None
    max_counter = 0
    min_counter = 0
    for k, v in counter.items():
        if max_k is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_k is None or v < min_counter:
            min_key = k
            min_counter = v
    return {min_key: min_counter, max_key: max_counter}


def fill_up_histogram(counter: dict[str, int], args: str) -> dict[str, int]:
    """Create something."""
    for character in args:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter


if __name__ == "__main__":
    counter = {}
    fill_up_histogram(counter, "hello")
