### Thomas Silva
### Nov 6, 2023
### ENGR 103 Project 6 b.



def add_surname(first_names):
    kardashian_names = ["Kardashian " + name for name in first_names if name[0] == 'K']

    return kardashian_names

first_names = ["Kim", "Kourtney", "Khloe", "Kris", "John", "Kate"]
kardashian_names = add_surname(first_names)
print(kardashian_names)
