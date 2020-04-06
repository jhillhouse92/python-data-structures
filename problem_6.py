class LinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return str(self.value)

    def __init__(self, iterable = ()):
        self.head = None

        for item in iterable:
            self.append(item)

    def append(self, value):

        if self.head is None:
            self.head = self.Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = self.Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        result = []
        node = self.head

        while node:
            result.append(node.value)
            node = node.next

        return result

    @staticmethod
    def union(linked_list_1, linked_list_2):
        union_set = set()
        node = linked_list_1.head

        while node:
            union_set.add(node.value)
            node = node.next

        node = linked_list_2.head
        while node:
            union_set.add(node.value)
            node = node.next

        return LinkedList(union_set)

    @staticmethod
    def intersection(linked_list_1, linked_list_2):
        # Your Solution Here
        list1_set = set()
        result_set = set()
        node = linked_list_1.head

        while node:
            list1_set.add(node.value)
            node = node.next

        node = linked_list_2.head
        while node:
            if node.value in list1_set:
                result_set.add(node.value)
            node = node.next

        return LinkedList(result_set)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


def setup_linked_list(arr1, arr2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for item in arr1:
        linked_list_1.append(item)

    for item in arr2:
        linked_list_2.append(item)

    return linked_list_1, linked_list_2

def test_union_without_duplicates():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.union(linked_list_1, linked_list_2)

    assert sorted(result.to_list()) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    arr1 = [1, 2, 3]
    arr2 = []

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.union(linked_list_1, linked_list_2)

    assert sorted(result.to_list()) == [1, 2, 3]

def test_union_with_duplicates():
    arr1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    arr2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.union(linked_list_1, linked_list_2)

    assert sorted(result.to_list()) == [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]

def test_intersection_without_duplicates():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 8, 9, 5, 10]

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.intersection(linked_list_1, linked_list_2)

    assert sorted(result.to_list()) == [2, 5]


def test_intersection_with_no_intersection():
    arr1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    arr2 = [1, 7, 8, 9, 11, 21, 1]

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.intersection(linked_list_1, linked_list_2)

    assert result.to_list() == []

    arr1 = [1, 2, 3]
    arr2 = []

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.intersection(linked_list_1, linked_list_2)

    assert result.to_list() == []

def test_intersection_with_duplicates():
    arr1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    arr2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    linked_list_1, linked_list_2 = setup_linked_list(arr1, arr2)
    result = LinkedList.intersection(linked_list_1, linked_list_2)

    assert sorted(result.to_list()) == [4, 6, 21]
