    def show_list(name_list):
            for name in namelist:
                    print (name + ' ')


    def determine_age(age):
            while age < 18:
                    print('You are still a minor')
                    age += 1
    

    def count_character(word):
            length = 0
            for count in word:
                    length += 1

            print(length)


    def check_value(arr_number):
            value = 20

            for num in arr_number:
                if num == value:
                        print(value + ' is in the list')
                else:
                        print('The value is not in the list')


    def repeat_defeat(score):
            while score < 75:
                    print('Defeat')
                    score += 1
            
            else:
                    print('Success')


    def print_character(word):
            for char in word:
                    print(char)


    def banner(word):
            count= 0
            while count < 1:
                    print('Go Jaguars!!')

            for char in word:
                    print(char)


    def print_list(name):
            string_list = ['one', 'two', 'three']

            print('Hi ' + 'name ' + '! These are the values of your list')

            for index in range(len(string_list)):
                    print('Index: ' + index + ' Value: ' + string_list[index])


    def add_all_values_in_list(num_list):
            total = 0 
            for index in range(len(num_list)):
                    total = num_list[index] + num_list[index + 1]
                    total += total

            print('The total sum of your num list is ' + total)


   def display_num_list(num_list):
           for index in num_list:
                   print(index)

            
             



    
            