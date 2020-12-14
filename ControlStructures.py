""" 1) Create a variable, paragraph, that has the following content:
"Python is a great language!", said Fred. "I don't ever remember
having this much fun before." """

paragraph = '"Python is a great language!", said Fred. "I don\'t ever remember \n having this much fun before."'
print(paragraph)

""" 2) Write an if statement to determine whether a variable holding a year is
a leap year. """

enter_year = int(input("Enter a year: "))

if enter_year % 400 == 0:
    print(f"{enter_year} is a leap year")
elif enter_year % 4 == 0:
    print(f"{enter_year} is a leap year")
elif enter_year % 100 == 0:
    print(f"{enter_year} is not a leap year")
else:
    print(f"{enter_year} is not a leap year")

""" 3) Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text. """

enter_paragraph = str(input("Enter a paragraph: "))

split_words = enter_paragraph.split()

anagram_list = []

for word_1 in split_words:
    for word_2 in split_words:
        if word_1 != word_2 and (sorted(word_1) == sorted(word_2)):
            anagram_list.append(word_1)

print(f"The anagrams in the paragraph are: {anagram_list}")

""" 4) Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list? """

friend_list = []
initial_id = id(friend_list)
print(f"The initial id of the list is: {initial_id}")

friend_list.append("Amar Agrawal")
friend_list.append("Ankeet Sharma")
friend_list.append("Kismat Giri")
friend_list.append("Aakrista Palikhe")
friend_list.append("Bhusan Pudasaini")

id_after_append = id(friend_list)
print(f"The id of the list after appending the names is: {id_after_append}")

if initial_id == id_after_append:
    print("The object's id didn't change after appending.")
else:
    print("The object's id changed after appending.")

print(f"The friend list before sorting: {friend_list}")
friend_list.sort()
print(f"The friend list after sorting: {friend_list}")

print(f"The first item on the list after sorting: {friend_list[0]}")
print(f"The second item on the list after sorting: {friend_list[1]}")

""" 5) Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age. """

my_tuple = ('Nhyu', 'Joshi', 21)

people = []
people.append(my_tuple)

friend_one = ('Amar', 'Agrawal', 22)
friend_two = ('Ankeet', 'Sharma', 25)
friend_three = ('Aakrista', 'Palikhe', 21)

people.append(friend_one)
people.append(friend_two)
people.append(friend_three)

print(f"List before sorting: {people}")

# Sorting by first name
people.sort(key=lambda x: x[0])
print(f"List after sorting by first name: {people}")

# Sorting by last name
people.sort(key=lambda x: x[1])
print(f"List after sorting by last name: {people}")

# Sorting by age
people.sort(key=lambda x: x[2])
print(f"List after sorting by age: {people}")

""" 6) Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it. """

list_friends = ['Amar', 'Ankeet', 'Aakrista', 'Kismat', 'Bhusan']
find_name = "John"

found = False

for i in list_friends:
    if i == find_name:
        print("Name found")
        found = True

if not found:
    print("Not found")

""" 7) Create a list of tuples of first name, last name, and age for your friends
and colleagues. If you don't know the age, put in None. Calculate the
average age, skipping over any None values. Print out each name,
followed by old or young if they are above or below the average age. """

people_list = []

friend_one = ('Amar', 'Agrawal', 22)
friend_two = ('Ankeet', 'Sharma', None)
friend_three = ('Aakrista', 'Palikhe', 21)
friend_four = ('Kismat', 'Giri', None)

people_list.append(friend_one)
people_list.append(friend_two)
people_list.append(friend_three)
people_list.append(friend_four)

sum_of_age = 0
total_number_of_age = 0

for i in people_list:
    if i[2] is None:
        pass
    else:
        sum_of_age += i[2]
        total_number_of_age += 1

average_age = sum_of_age/total_number_of_age
print(f"Given list: {people_list}")
print(f"Average age: {average_age}")

for i in people_list:
    if i[2] is None:
        print(f"{i[0]}: No age given")
    else:
        if i[2] > average_age:
            print(f"{i[0]}: Old")
        else:
            print(f"{i[0]}: Young")

""" 8) Write a function, is_prime, that takes an integer and returns True if the
number is prime and False if the number is not prime. """


def is_prime(num):
    if num > 1:
        # check for factors
        for j in range(2, num):
            if (num % j) == 0:
                return False
                break
        else:
            return True
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False


enter_num = int(input("Enter a number: "))
if is_prime(enter_num):
    print(f"{enter_num} is a prime number.")
else:
    print(f"{enter_num} is not a prime number.")

""" 9) Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found. """


def binary_search(sorted_sequence, item):
    element_one = 0
    element_last = len(sorted_sequence) - 1
    flag = False
    print("Sorted input list:", sorted_sequence)
    while element_one <= element_last and not flag:
        mid = (element_one + element_last) // 2
        if sorted_sequence[mid] == item:
            flag = True
            return mid
        else:
            if item < sorted_sequence[mid]:
                element_last = mid - 1
            else:
                element_one = mid + 1
    return -1


num_list = [4, 6, 8, 5, 2, 1, 9, 7]
print(binary_search(sorted(num_list), 3))
print(binary_search(sorted(num_list), 9))

""" 10) Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well. """


def convert_case(inp_string, *args, **kwargs):
    snake_case_string = ""
    for l in inp_string:
        if l.isupper():
            if not snake_case_string:
                snake_case_string = snake_case_string + l.lower()
            else:
                snake_case_string = snake_case_string + "_" + l.lower()
        else:
            snake_case_string = snake_case_string + l

    # Check if args exists and if it exists convert to the case as requested.
    if args:
        argument_string = ""
        for l in inp_string:
            if l.isupper():
                if not argument_string:
                    argument_string = argument_string + l.lower()
                else:
                    argument_string = argument_string + str(args[0]) + l.lower()
            else:
                argument_string = argument_string + l
        return snake_case_string, argument_string

    return snake_case_string


enter_string = str(input("Enter a camel cased string:"))
choose_separator = input("Do you want a separator (Y/N):")
if choose_separator.upper() == "Y":
    separator = input("Enter the separator you want:")
    print(convert_case(enter_string, separator))
else:
    print(convert_case(enter_string))

""" 11) Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length? """

filename = str(input("Enter a filename with three letter extension: "))

extension_pick = slice(0, -4)
name_without_extension = filename[extension_pick]

print("Filename with extension:", filename)
print("Filename without extension:", name_without_extension)

# The code does not work on arbitrary length if the extension is of different length.
filename_one = "WordFile.docx"
name_without_extension = filename_one[extension_pick]
print("Filename with extension:", filename_one)
# The filename doesn't omit the "." which shows it is not suitable for arbitrary length.
print("Filename without extension:", name_without_extension)

""" 12) Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed. """


def is_palindrome(inp_word):
    reverse_word = inp_word[::-1]

    if reverse_word.lower() == inp_word.lower():
        return True
    else:
        return False


enter_word = str(input("Enter a string: "))
if is_palindrome(enter_word):
    print(f"{enter_word} is palindrome")
else:
    print(f"{enter_word} is palindrome")

""" 13) Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)] it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21 """


def write_csv(file_name, tuple_list):

    with open(file_name + '.csv', 'wt') as file:
        file.write("name,address,age\n")
        for k in tuple_list:
            file.write(f"{k[0]},{k[1]},{k[2]}\n")


enter_file_name = str(input("Enter filename: "))
list_tuple = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
write_csv(enter_file_name, list_tuple)

""" 14) Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}] """

import csv


def read_csv(file_name):
    final_list = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for r in csv_reader:
            final_list.append(r)
    return final_list


print(read_csv("question_13.csv"))

""" 15) Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have? """


class Bank:
    @staticmethod
    def get_account_no():
        return 'Account number : 123456'

    @staticmethod
    def get_pin_no():
        return 'Pin number for card : 123456'


class Customer:
    def __init__(self, first_name, last_name, father_name, mother_name,
                 grandfather_name, current_address, permanent_address, contact_no,
                 address_detail, documentation_one, documentation_two, job_status,
                 job_type, marital_status, account_type, current_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.mother_name = mother_name
        self.grandfather_name = grandfather_name
        self.current_address = current_address
        self.permanent_address = permanent_address
        self.contact_no = contact_no
        self.address_detail = address_detail
        self.documentation_one = documentation_one
        self.documentation_two = documentation_two
        self.job_status = job_status
        self.job_type = job_type
        self.marital_status = marital_status
        self.account_type = account_type
        self.current_balance = current_balance
        self.account_no = Bank.get_account_no()
        self.is_active = True
        self.pin = Bank.get_pin_no()

    def balance_enquiry(self):
        return self.current_balance

    def deposit_money(self, deposit_amount):
        self.current_balance += deposit_amount
        return f"New balance: {self.current_balance}"

    def set_card_pin(self, pin):
        self.pin = pin

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount > self.current_balance:
            return "Insufficient balance."
        else:
            return f"Rs.{withdraw_amount} has been withdrawn from your account no. {Bank.get_account_no()}.\n" \
                   f"New Balance: {self.current_balance}"


""" 16) Imagine you are creating a Super Mario game. You need to define a
class to represent Mario. What would it look like? If you aren't familiar
with SuperMario, use your own favorite video or board game to model
a player. """


class Mario:
    def __init__(self, size, state, jump=False):
        self.size = size
        self.state = state
        self.jump = jump

    def jump(self):
        self.jump = True
        return self.jump

    def move(self):
        pass

    def attack(self):
        pass

    def die(self):
        pass


""" 17) Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors. """


def calculator(num1, get_operator, num2):

    if get_operator == "+":
        result = num1 + num2
        return result
    elif get_operator == "-":
        result = num1 - num2
        return result
    elif get_operator == "/":
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            print("Number can't be divided by zero.")
    elif get_operator == "*":
        result = num1 * num2
        return result
    else:
        return "Invalid operator"


num_1 = input("Enter first number: ")
operator = input("Enter operator: ")
num_2 = input("Enter second number: ")

if num_1.isdigit() and num_2.isdigit():
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(calculator(num_1, operator, num_2))
else:
    print("Please enter valid number")

""" 18) Find a package in the Python standard library for dealing with JSON.
Import the library module and inspect the attributes of the module.
Use the help function to learn more about how to use the module.
Serialize a dictionary mapping 'name' to your name and 'age' to your
age, to a JSON string. Deserialize the JSON back into Python. """

import json

help(json)

my_dictionary = {
    'name': 'Nhyu',
    'age': 21
}

dict_json = json.dumps(my_dictionary)
print(dict_json)

final_dict = json.loads(dict_json)
print(final_dict)

""" 19) Write a Python class to find validity of a string of parentheses, '(', ')',
'{', '}', '[' and ']. These brackets must be close in the correct order, for
example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid """


class ValidParenthesis:
    def check_parentheses_validity(self, string):
        add_brackets = []
        brackets_seq_dict = {"(": ")", "{": "}", "[": "]"}
        for bracket in string:
            if bracket in brackets_seq_dict:
                add_brackets.append(bracket)

            elif len(add_brackets) == 0 or brackets_seq_dict[add_brackets.pop()] != bracket:
                return "Invalid"
        return "Valid" if len(add_brackets) == 0 else "Invalid"


print(ValidParenthesis().check_parentheses_validity("()[]{}"))
print(ValidParenthesis().check_parentheses_validity("[)"))
print(ValidParenthesis().check_parentheses_validity("({[)]"))
print(ValidParenthesis().check_parentheses_validity("{{{"))

""" 20) Write a Python class to find the three elements that sum to zero from
a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]"""


def sum_to_zero(array):
    flag = False
    length = len(array)
    output_list = []

    for number in range(0, length - 2):
        for number2 in range(number + 1, length - 1):
            for number3 in range(number2 + 1, length):

                if array[number] + array[number2] + array[number3] == 0:
                    list_nums = [array[number], array[number2], array[number3]]
                    output_list.append(list_nums)
                    flag = True

    if not flag:
        print("Such 3 numbers doesn't exist")
    else:
        print(output_list)


input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
sum_to_zero(input_array)
