def count_item(my_list, item):
        count = my_list.count(item)
            
        return count

print(count_item(my_list, item))


def concatenate_list(first_list, second_list):
        whole_list = second_list.append(first_list)

        return whole_list

print(concatenate_list(first_list, second_list))


def reverse_list(my_list):
        return my_list.reverse()

print(reverse_list(my_list))


def insert_list(my_list, index, word):
        return my_list.insert(index, word)

print insert_list(my_list, index, word)


def sort_list(my_list):
        return my_list.sort()

print(sort_list(my_list))


def index_item(my_list, item):
        return my_list.index(item)

print(check_value(my_list, item))


def pop_item(my_list, index):
        final_list = my_list.pop(index)

        return final_list

print(pop_item(my_list, index))


def change_item(my_list, value, index):
        my_list[index] = value
        print(my_list)

change_item(my_list, value, index)


def remove_item(my_list, item):
        for index in my_list:
            if item in my_list:
                my_list.remove(item)
                print(my_list)
            else:
                print('Item not found.')

remove_item(my_list, item)


def copy_list(my_list):
        new_list = my_list.copy()

        return new_list

print(copy_list(my_list))


            






