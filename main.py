"""An application that personalized letter to manual formatting of a large bulk"""

# Getting the names of those that qualified
with open("names/qualified.txt", mode="r") as file:
    qualified_name = file.readlines()
    for name in qualified_name:
        print(name)
