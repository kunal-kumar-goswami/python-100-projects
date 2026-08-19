def formate_name(f_name , l_name):
    if f_name == "" or l_name == "":
        return "You did not provide any inputs ."
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

print(formate_name(input("Write your name : "), input("Write your last name : ")))

export = len("KuNaL")

def operator_01(text):
    return text + text

def operator_02(text):
    return text.title()

output = operator_01(operator_02("this is python programing ."))
print(output)


