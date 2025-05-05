'''
STRINGS
"This is a string" or 'This is also a string'

print(name)
print(name.title())
print(name.upper())
print(name.lower())

first_name = "carlos"
last_name = "innocent"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("Gods must be crazy!")
print("\tGods must be crazy!")
print("Names:\nJob\nSimon\nJane\nHassan")
print("Names:\n\tJob\n\tSimon\n\tJane\n\tHassan")

'python' 'python ' are not the same

fav_language = ' Python '
print(fav_language)
print(fav_language.rstrip())
print(fav_language.lstrip())
print(fav_language.strip())

my_url = 'https://aci.com'
print(my_url.removeprefix('https://'))

name = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new"
message = f'{name} once said, "{quote}"'
print(message)

'''
VARIABLE 
A variable is a name given to a value that can be changed and later used in the code.
VARIABLE NAMING CONVENTIONS:
•Variables can be written with characters, symbols, underscores and numbers.
  • Variables are case sensitive meaning capital "N"is not the same as small "n".
    •Variables can start with underscores but not numbers.
    •Variables are short and descriptive.
    •Variables aren't written with spaces in between them.
VARIABLE CONVENTION TYPES:
    There are three variable convention types namely.
    •Camel case
    •pascal case
    •Snake case
    CAMEL CASE:
    Here the first letter of the second word is capitalised for instance studentsName
    PASCAL CASE:
    Same as camel case but the first letter of the word capitalised for instance StudentsName.                                               
    SNAKE CASE:
    Here each word is being separated by an underscore for instance students_name                                                 

