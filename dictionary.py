def print_dictionary(my_dict):
        for index in my_dict.values():
            print index

print_dictionary(my_dict)


def print_key(my_dict):
        for index in my_dict:
            print index

print_key(my_dict)


def check_key(my_dict, key):
        if key in my_dict:
            return True
        else:
            return False

print(check_key(my_dict, key))


def length_dict(my_dict):
        return len(my_dict)

print length_dict(my_dict)


def add_dict(my_dict, key, item):
        my_dict[key] = item

add_dict(my_dict, key, item)


def remove_dict(my_dict, key):
        if key in my_dict:
            my_dict.pop(key)
        else:
            print('Key not present in dict.')

remove_dict(my_dict, key)


def remove_last_item(my_dict):
        modified = mydict.popitem()

        return modified

print(remove_last_item(my_dict))


def insert_dict(my_dict, key, item):
        my_dict.update(key, item)

        return my_dict

print(insert_dict(my_dict, key, item))


def clear_content(my_dict):
        my_dict.clear()

        return my_dict

print(clear_content(my_dict))


def get_item(my_dict, key):
        if key in my_dict:
            value = my_dict.get(key)
            return value
        else:
            print('Key doesn\'t exist')

print(get_item(my_dict, key))



            
                    
            
            