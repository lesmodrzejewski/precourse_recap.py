my_string = "My name is Lez"
random_numbers = 6589693
my_float_number = 23.2345
my_boolean = True
transportation = ['car', 'bike', 'motorbike', 'bus']
movie = 'pirates of the caribbean: the curse of the black pearl'

new_movie_title = movie.title()
print(new_movie_title)

def my_string_upper(string_1):
    new_str = string_1.upper()
    print(new_str)

my_string_upper(my_string)

def add_numbers(num_1, num_2):
    new_number = float(num_1) + num_2
    print(new_number)

add_numbers(random_numbers, my_float_number)


def add_plane(list_1):
    list_1.append('plane')
    print(list_1)

add_plane(transportation)

def is_raining(boolean_1):
    if boolean_1 == True:
        print("don't forget about your umbrella")
    else:
        print("take your sunglasses with you")

is_raining(my_boolean)



