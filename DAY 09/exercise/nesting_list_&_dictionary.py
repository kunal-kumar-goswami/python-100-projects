capitals = {
    "India":"Delhi",
    "France": "Paris",
}

travel = {
    "India": ["Delhi", "Mumbi","Kolkata"],
    "France": ["Paris", "Lilla","Dijan"]
}

print(travel["France"][1])

nested_list = ["K","I",["N","G"]]
print(nested_list[2][1])

travel = {
    "India": {
        "cities_visited":["Delhi", "Mumbi","Kolkata"],
        "times_of_visited": 5
    },
    "France":{
    "cities_visited": ["Paris", "Lilla","Dijan"],
    "times_of_visited": 6
    },
}

print(travel["India"]["cities_visited"][2])