from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity=5, *args, **keywords):
        # Initialize class variables
        self.capacity = capacity
        super().__init__(*args, **keywords)

    def __getitem__(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            # move key to end b/c just accessed, if key not found, it will throw KeyError
            self.move_to_end(key)
            return super().__getitem__(key)
        except KeyError:
            return -1

    def __setitem__(self, key, value):
        # when: the length is greater than the capacity
        # then: remove the oldest
        if len(self) >= self.capacity:
            key, value = self.popitem(last=False)

        # set the value and move this key to the end just in case we are changing it
        super().__setitem__(key, value)
        self.move_to_end(key)


def test_lru_capacity_works():
    # initializes capacity actually sets it
    lru_cache = LRUCache(5)
    assert lru_cache.capacity == 5

    # add items past capacity
    # length still equal to capacity
    lru_cache[0] = 0
    lru_cache[1] = 1
    lru_cache[2] = 2
    lru_cache[3] = 3
    lru_cache[4] = 4
    lru_cache[5] = 5
    assert len(lru_cache) == lru_cache.capacity

    # least accessed item returns -1
    assert lru_cache[0] == -1


def test_lru_get_value_updates_access():
    lru_cache = LRUCache(5)

    lru_cache[0] = 0
    lru_cache[1] = 1
    lru_cache[2] = 2
    lru_cache[3] = 3

    assert lru_cache[0] == 0

    key, _ = lru_cache.popitem(last=False)
    assert key == 1


def test_lru_set_value_updates_access():
    lru_cache = LRUCache(5)

    lru_cache[0] = 0
    lru_cache[1] = 1
    lru_cache[2] = 2
    lru_cache[3] = 3
    lru_cache[0] = 4

    key, _ = lru_cache.popitem(last=False)
    assert key == 1


def test_lru_default_capacity():
    lru_cache = LRUCache()
    assert lru_cache.capacity == 5

    lru_cache['key1'] = None
    lru_cache['key2'] = None
    lru_cache[2] = 2
    lru_cache[3] = 3
    lru_cache['key3'] = 4
    lru_cache[5] = 5
    assert len(lru_cache) == lru_cache.capacity

    # least accessed item returns -1
    assert lru_cache['key1'] == -1
