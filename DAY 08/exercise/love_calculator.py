#love calculator 
def calculate_love_score( name1, name2):

    combined_name = name1 + name2
    lower_names = combined_name.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e_true = lower_names.count("e")  # Renamed to avoid confusion
    first_digit = t + r + u + e_true

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e_love = lower_names.count("e")  # Renamed to avoid confusion
    second_digit = l + o + v + e_love


    score = int(str(first_digit) + str(second_digit))
    print (score)


calculate_love_score("Kanye West", "Kim Kardashian")