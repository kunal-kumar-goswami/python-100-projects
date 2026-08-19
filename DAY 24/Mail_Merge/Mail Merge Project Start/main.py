PLACEHOLDER = "[name]"


with open("C:/python/100 Days of Code/DAY 24/Mail_Merge/Mail Merge Project Start/Input/invited_names.txt", 'r') as names_file:
    names = names_file.readlines()
    print(names)

with open("C:/python/100 Days of Code/DAY 24/Mail_Merge/Mail Merge Project Start/Input/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
       striped_name = name.strip()
       new_letter = letter_content.replace(PLACEHOLDER, name)
       print(new_letter)
       

