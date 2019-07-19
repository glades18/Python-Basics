def show_list(name_list):
            for name in name_list:
                    print (name + ' ')

show_list(name_list)


def determine_age(age):
            while age < 18:
                    print('You are still a minor')
                    age += 1

determine_age(age)
    

def count_character(word):
            for count in word:
                    length += 1
                    print(length)

count_character(word)


def check_value(arr_number):
            for num in arr_number:
                    if num == 20:
                            print(num + ' is in the list')
                    else:
                            print('The value is not in the list')

check_value(arr_number)


def repeat_defeat(score):
            while score < 75:
                    print('Defeat')
                    score += 1
            else:
                    print('Success')

repeat_defeat(score)


def print_character(word):
            for char in word:
                    print(char)

print_character(word)


def banner(word, count):
            while count < 1:
                    print('Go Jaguars!!')

            for char in word:
                    print(char)

banner(word, count)


def print_list(name, string_list):
            print('Hi ' + name + '! These are the values of your list')

            for index in range(0, len(string_list)):
                    print('Index: ' + index + ' Value: ' + string_list[index])

rint_list(name, string_list)


def add_all_values_in_list(num_list, total):
            for index in range(0, len(num_list)):
                    total = num_list[index] + num_list[index + 1]
                    total += total

            print('The total sum of your num list is ' + total)

add_all_values_in_list(num_list, total)


def display_num_list(num_list):
            for index in num_list:
                   print(num_list[index])

display_num_list(num_list)

            
             



    
            