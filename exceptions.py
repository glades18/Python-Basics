def check_file_exist(filename, text_to_write):
        try:
            file = open(filename, 'w')
            file.write(text_to_write)

        except IOError:
                print('File doesn\'t exist.')

        else:
            print('Writing to file - success!')
            file.close()

check_file_exist(filename, text_to_write)


def arithmetic_error(x, y):
        try:
            result = x - y
    
        except ArithmeticError:
            print('There is an arithmettic error.')
            
        else:
            print('No problem is reaised')

arithmetic_error(x, y)


def assertion_error(x, y):
        try:
            assert x == y, 'Values don\'t match'

        except AssertionError as e:
            print(e)

assertion_error(x, y)


def type_error(string, num):
        try:
            result = string * num

        except TypeError:
            print('TypeError Exception')
            
        else:
            print('No exception occurred.')

type_error(string, num)


def value_error(num):
        try:
            var = str(num)
            print(var)

        except ValueError:
            print('Value Error Exception')

        else:
            print('No exception occurred')

value_error(num)


def zero_division_error(x, y):
        try:
            result = x / y

        except ZeroDivisionError:
            print('y should not be 0')

        else:
            print('No exception occurred')

zero_division_error(x, y)


def keyboard_interrupt():
        try:
            print('Press Ctrl + C or Del to experience exception')

        except KeyboardInterrupt:
            print('Ctrl + C or Del was pressed')

        else:
            print('No exception occurred')

keyboard_interrupt()


def name_error():
        try:
            print(string)
        
        except NameError:
            print('Variable doesn\'t exist')

        else:
            print('No exception occurred')

name_error()


def key_error(my_list):
        try:
            print(my_list['doesn\'t_exist'])
            
        except KeyError:
            print('KeyError Exception')

key_error(my_list)
result = 1


def unbound_local_error():
        try:
            result += 1

        except UnboundLocalError:
            print('Local variable not initialized')

unbound_local_error()

            
         




            


            




            