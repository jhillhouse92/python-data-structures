import pytest

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # check if user in top group
    if group:
        if user in group.get_users():
            return True

        # recursively check each sub group
        for group in group.get_groups():
            return is_user_in_group(user, group)

    return False

@pytest.fixture()
def setup_user_group():
    parent = Group('parent')

    parent_user = 'parent_user'
    parent.add_user(parent_user)

    child = Group('child')
    sub_child = Group('subchild')

    sub_child_user = 'sub_child_user'
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    return parent_user, parent, sub_child_user

def test_user_in_top_group(setup_user_group):
    parent_user = setup_user_group[0]
    parent_group = setup_user_group[1]

    assert is_user_in_group(parent_user, parent_group)


def test_user_not_in_group(setup_user_group):
    parent_group = setup_user_group[1]

    assert is_user_in_group('BAD USER', parent_group) is False


def test_user_not_in_bad_group(setup_user_group):
    parent_user = setup_user_group[0]

    assert is_user_in_group(parent_user, None) is False

def test_grandchilduser_in_parent_group(setup_user_group):
    parent_group = setup_user_group[1]
    grandchild_user = setup_user_group[2]

    assert is_user_in_group(grandchild_user, parent_group)