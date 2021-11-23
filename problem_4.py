# Active directory

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_users(user, users):
    return user in users


def is_user_in_group(user, group):

    if user is None or user == "":
        return False

    if is_user_in_users(user, group.get_users()):
        return True

    # scan every sub groups
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    return False


# Test 1
def test_1():
    other = Group("other")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, child))
    print(is_user_in_group(sub_child_user, sub_child))
    print(is_user_in_group(sub_child_user, parent))
    print(is_user_in_group(sub_child_user, other))

print("--- test 1 ---")
test_1()
# expected result: True True True False

# test 2
def test_2():
    other = Group("other")
    parent = Group("parent")
    child = Group("child")

    parent.add_group(child)

    child.add_user("a")
    child.add_user("b")
    child.add_user("c")
    child.add_user("d")

    print(is_user_in_group("c", child))
    print(is_user_in_group("c", parent))
    print(is_user_in_group("c", other))

print("--- test 2 ---")
test_2()
# expected result: True True False


# test 3
def test_3():
    parent = Group("parent")
    child = Group("child")
    child_2 = Group("child 2")

    parent.add_group(child)
    parent.add_group(child_2)

    child.add_user("a")
    child.add_user("b")
    child_2.add_user("c")
    child_2.add_user("d")

    print(is_user_in_group("c", child))
    print(is_user_in_group("c", parent))
    print(is_user_in_group("c", child_2))

    print(is_user_in_group("a", child))
    print(is_user_in_group("a", parent))
    print(is_user_in_group("a", child_2))

print("--- test 3 ---")
test_3()
# expected result: False True True True True False


# test 4
def test_4():
    parent = Group("parent")
    child = Group("child")
    child_2 = Group("child 2")

    parent.add_group(child)
    parent.add_group(child_2)

    child.add_user("a")
    child.add_user("b")
    child_2.add_user("c")
    child_2.add_user("d")

    print(is_user_in_group(None, parent))
    print(is_user_in_group("", child_2))

print("--- test 4 ---")
test_4()
# expected result: False False