# Random Passwork Generator

import random
import string

#characters to generate the password
characters = list(string.ascii_letters + string.digits + "!@#$%&*()")   #genrates the entire character list
alphabets = list(string.ascii_letters)                                  #alphabets
digits = list(string.digits)                                            #the numbers
special_characters = list("!@#$%&*()")                                  #other characters

#function to generate the password
def generate_random_password ():
    length = int(input("Enter password length: "))                      #length of password

    #Number of Characters 
    alphabets_count = int(input("Enter the number of letters: "))
    numbers_count = int(input("Enter the number of numbers: "))
    special_character_count = int(input("Enter the number of special characters: "))
                                                                        #Sum of character count
    characters_count = alphabets_count + numbers_count + special_character_count

    #redundancy check
    if length < characters_count:
        print("Character legnth is greater than pasword legnth ")
        return

    #initializing password
    password = []

    #picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    #picking random digits
    for i in range(numbers_count):
        password.append(random.choice(digits))

    #picking random characters
    for i in range(special_character_count):
        password.append(random.choice(special_characters))

    #if the total characters count is less than the password legnth add random characters to make it equal to the length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    #shuffle random password
    random.shuffle(password)

    #convert the list to string and printing the list
    print("".join(password))

#invoking the function
generate_random_password()