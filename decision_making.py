def compare_number(x):
            if x > 10:
                    return True
            else:
                    return False

print(compare_number(x))


def compare_name(x):
            if x == 'Maria':
                    print('She is ' + x)
            else:
                    print('She is not Maria')

compare_name(x)


def empty_string(x):
            if x is None:
                    print('This is an empty string.')
            else:
                    print('This is not an empty string.')

empty_string(x)


def show_info(x):
            if x == 'myName':
                    return True

print(show_info(x))


def add_number(x):
            if x < 300:
                    return x + 200

print(add_number(x))

    
def discount(age, amount):
            if age >= 60:
                    discounted_price = amount * .20
                    total_price = amount - discounted_price
                    print('Your total amount to be paid is ' + total_price)
            else:
                    print('You are not a candidate for Senior Citizen discount')

discount(age, amount)


def subtract_number(x):
            if x < 3:
                    print(x - 3)

subtract_number(x)


def minor_adult(x):
            if x < 18:
                    return False
            elif x >= 18:
                    return True
                
print(minor_adult(x))


def product_description(product_name):
            if product_name == 'wine':
                    print ('This is a wine. It is originated from Europe and has a sour taste.')
            elif product_name == 'ball':
                    print ('This is a ball. It was invented by the Ancient Mesoamericans. It is round in shape and has variety of sizes.')
            else:
                    print('The product entered is not in our list.')

product_description(product_name)


def show_price(product):
            if product == 'notebook':
                    print('This ' + product + ' is for P20.00')
            else:
                    print('The product entered is not in our list.')

show_price(product)
            


