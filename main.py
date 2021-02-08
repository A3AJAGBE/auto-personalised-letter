"""An application that personalized letter to manual formatting of a large bulk"""
PLACEHOLDER = "[name]"

# Get the names of those that qualified
with open("names/qualified.txt", mode="r") as names_file:
    qualified_names = names_file.readlines()

# Get the contents of the template letter
with open("letter_templates/congratulation_template.txt") as template_file:
    open_template = template_file.read()
    # Add the name and format the letters
    for name in qualified_names:
        name = name.strip()
        add_names = open_template.replace(PLACEHOLDER, name)
        print(add_names)

