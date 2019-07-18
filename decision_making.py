    def compare_number(x):
            if x > 10: 
                    return True
            else:
                    return False


    def compare_name(x):
            if x == 'Maria':
                    print('She is ' + x)
            else:
                    print('She is not Maria')


    def empty_string(x):
            if x is None:
                    print('This is an empty string.')
            else:
                    print('This is not an empty string.')


    def show_info(x):
            address = 'Lanang, Davao City'
            email_add = 'my.email@gmail.com'
            myName = 'Xander'

            if x == 'myName':
                print(address, email_add)


    def add_number(x):
            if x < 300:
                return x + 200

    
    def discount(age, amount):
            if age == 60:
                    discounted_price = amount * .20
                    total_price = amount - discounted_price
                    print('Your total amount to be paid is ' + total_price)
            else:
                    print('You are not a candidate for Senior Citizen discount')



    def subtract_number(x):
            if x < 3: 
                    print(x - 3)


    def age(x):
            statement = ''

            if x < 18:
                    statement = 'You are still a minor'
            elif x >= 18:
                    statement = 'You are now an adult'

            return statement
                

    def product_desctiption(product_name):
            first_product = 'wine'
            second_product = 'ball'

            if product_name == first_product:
                    print ('This is a wine. It is originated from Europe and has a sour taste.')
            elif product_name == second_product:
                    print ('This is a ball. It was invented by the Ancient Mesoamericans. It is round in shape and has variety of sizes.')
            else:
                    print('The product entered is not in our list.')


    def show_price(product):
            sample_product= 'notebook'

            if product == sample_product:
                    print('This ' + product + ' is for P20.00')
            else:
                    print('The product entered is not in our list.')
            


