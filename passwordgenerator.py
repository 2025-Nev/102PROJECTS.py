import random
import string

def generate_password(length):
    # Define a string containing all possible characters for the password
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Use random.sample() to generate a random sequence of characters of the desired length
    password = ''.join(random.sample(all_chars, length))

    return password

# Prompt the user for the desired length of the password
length = int(input("Enter the desired length of your password: "))

# Generate and print the password
password = generate_password(length)
print("Your password is:", password)

#Another way of writing a password generator code 
import random
import string

def generate_password(length):
    """
    Generates a random password with the given length.

    Args:
        length: An integer representing the desired length of the password.

    Returns:
        A string representing the generated password.
    """
    # Define the character sets to use in the password.
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine the character sets into one big set.
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    # Use random.sample to choose a random selection of characters from the set.
    password = ''.join(random.sample(all_characters, length))

    return password

    #Another way of writing a password generator
import string
import random
 
# Getting password length
length = int(input("Enter password length: "))
 
print('''Choose character set for password from these :
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
characterList = ""
 
# Getting character set for password
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif(choice == 2):
         
        # Adding digits to possible characters
        characterList += string.digits
    elif(choice == 3):
         
        # Adding special characters to possible
        # characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    # Picking a random character from our
    # character list
    randomchar = random.choice(characterList)
     
    # appending a random character to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))

#Another way of writing a password generator 
# import modules
import string
import random


# store all characters in lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")


# check this input is it number? is it more than 8?
while True:

	try:

		characters_number = int(user_input)

		if characters_number < 8:

			print("Your number should be at least 8.")

			user_input = input("Please, Enter your number again: ")

		else:

			break

	except:

		print("Please, Enter numbers only.")

		user_input = input("How many characters do you want in your password? ")


# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):

	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):

	result.append(s3[x])
	result.append(s4[x])


# shuffle result
random.shuffle(result)


# join result
password = "".join(result)
print("Strong Password: ", password)

#EXPLANATION OF EACH LINE:
#import random: This imports the random module, which provides functions for generating random numbers and selecting random items from a list or sequence.
#import string: This imports the string module, which provides a collection of constants that represent the ASCII characters. These constants can be used to build strings of specific characters, such as lowercase letters, uppercase letters, digits, and punctuation marks.
#def generate_password(length):: This defines a function called generate_password that takes a single argument length, which specifies the length of the password to be generated.
#characters = string.ascii_letters + string.digits + string.punctuation: This defines a string variable called characters that contains all possible characters that can be used to generate a password. The string.ascii_letters constant contains all the ASCII letters (both lowercase and uppercase), string.digits contains all digits from 0 to 9, and string.punctuation contains all punctuation characters.
#password = ''.join(random.choice(characters) for i in range(length)): This generates a password of the specified length by using a generator expression to randomly select characters from the characters string and join them together. The random.choice() method randomly selects a character from the characters string, and the join() method joins the selected characters together to form a single string.
#return password: This returns the generated password as the output of the generate_password function.
#password = generate_password(12): This generates a password of length 12 using the generate_password function and assigns it to a variable called password.
#print(password): This prints the generated password to the console.'''

