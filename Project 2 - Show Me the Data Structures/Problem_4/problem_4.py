# Problem 4: Active Directory

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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True
    else:
        list_of_groups = group.get_groups()
        for group in list_of_groups:
            if is_user_in_group(user, group):
                return True
    return False


# Test Cases

print('----- Test Case 1: The default test case -----')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
parent.add_group(child)
child.add_group(sub_child)
sub_child.add_user(sub_child_user)
print("Does {0} group have sub_child_user? {1}".format(parent.get_name(), is_user_in_group(sub_child_user, parent)))
print("Does {0} group have sub_child_user? {1}".format(child.get_name(), is_user_in_group(sub_child_user, child)))
print("Does {0} group have sub_child_user? {1}".format(sub_child.get_name(), is_user_in_group(sub_child_user, sub_child)))


print('\n----- Test Case 2: A group with several users -----')
group_1 = Group("group_1")
user_1 = "user_1"
user_2 = "user_2"
user_3 = "user_3"
user_4 = "user_4"
user_5 = "user_5"
group_1.add_user(user_1)
group_1.add_user(user_2)
group_1.add_user(user_3)
group_1.add_user(user_4)
print("Does {0} group have user_1? {1}".format(group_1.get_name(), is_user_in_group(user_1, group_1)))
print("Does {0} group have user_2? {1}".format(group_1.get_name(), is_user_in_group(user_2, group_1)))
print("Does {0} group have user_3? {1}".format(group_1.get_name(), is_user_in_group(user_3, group_1)))
print("Does {0} group have user_4? {1}".format(group_1.get_name(), is_user_in_group(user_4, group_1)))
print("Does {0} group have user_5? {1}".format(group_1.get_name(), is_user_in_group(user_5, group_1)))


print('\n----- Test Case 3: A group with no users -----')
empty_group = Group("empty")
user_1 = "user_1"
print("Does {0} group have user_1? {1}".format(empty_group.get_name(), is_user_in_group(user_1, empty_group)))