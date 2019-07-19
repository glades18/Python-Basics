def count_word_in_string(string, item):
        count = string.count(item)
                
        return count

 print(count_word_in_string(string, item))


def check_if_digit(string):
        return string.isdigit() 

print(index_of_string(string))


def format_string(string):
        text = 'The apple is worth {string:.2f} pesos'
        print(text.format(price = 20))

format_string(string)


def replace_string(string, word, to_replace):
        new_string = string.replace(word, to_replace)
  
        return new_string

print(replace_string(string, word, to_replace))


def check_start_string(string):
        return string.startswith('This')

print(check_start_string(string))


def swapcase_string(string):
        new_string = string.swapcase()

        return new_string

print(swapcase_string(string))


def upper_case(string):
        upper_case_string = string.upper()
  
        return upper_case_string

print(upper_case(string))


def split_string(string):
        seperate_string = string.split('!')

        return seperate_string

print(split_string(string))


def lower_case(string):
        lower_case_string = string.lower()

        return(lower_case_string)

print(lower_case(string))


def index_word(string, word):
        index = string.index(word)

        return index

print(index_word(string, word))

