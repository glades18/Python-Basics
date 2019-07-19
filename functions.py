def recursion(num, count):
        while num != 0:
            count += 1
            recursion(num - 1)

        return count

print(recursion(num, count))
    
    
def encapsulation(string, num, my_list):
        def inner_function(num, my_list):
            while num != 0:
                for index in string:
                    my_list.append(index)
                    inner_function(num - 1)
                
            print(my_list)
    
encapsulation(string, num, my_list)


def print_string(string):
        print(string)

print_string(string)


def add_num(x, y):
        return x + y

print(add_num(x, y))


def subtract_num(x, y):
        return x - y

print(subtract_num(x, y))


def print_char_in_string(string):
        for char in string:
            print(char)

print_char_in_string(string)


def multiple_num(x, y):
        return x * y

print(multiple_num(x * y))


def character_count(string):
        for char in string:
            length += 1
            print(length)

character_count(string)


def print_string_list(string_list):
        for index in string_list:
            print(string_list[index])

print_string_list(string_list)


def specify_index_list(my_list):
        index = my_list[1]

        return index

print(specify_index_list(my_list))


    
            
        












    
            