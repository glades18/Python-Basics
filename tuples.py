def convert_to_tuple(my_list):
        new_tuple = tuple(my_list)
        print(new_tuple)

convert_to_tuple(my_list)


def length_tuple(my_tuple):
        return len(my_tuple)

print(length_tuple(my_tuple))


def min_tuple(my_tuple):
        return min(my_tuple)

min_tuple(my_tuple)


def remove_tuple(my_tuple):
        del my_tuple

remove_tuple(my_tuple)


def check_item(my_tuple, item):
        if item in my_tuple:
            return True
        else:
            return False

print(check_item(my_tuple, item))


def count_item(my_tuple, item):
        count = my_tuple.count(item)

        return count

print(count_item(my_tuple, item)


def first_value_of(my_tuple, item):
        first_value = my_tuple.index(item)

        return first_value

 print(first_value_of(my_tuple, item)


def determine_first_value(my_tuple, item):
        if item in my_tuple:
            first_value = my_tuple.index(item)
            print('First value of ' + item + ' is in index ' + first_value)
        else:
            print('item is not present in tuple')

determine_first_value(my_tuple, item)


def display_count_tuple(my_tuple, item):
        for index in my_tuple:
            print index

        count = my_tuple.count(item)
        print('Value ' + item + ' occurs ' + count + ' times in the tuple.')

display_count_tuple(my_tuple, item)


def check_remove_tuple(my_tuple, item):
        if item in my_tuple:
            print('The item is in the tuple.')
        else:
            del my_tuple

check_remove_tuple(my_tuple, item)
