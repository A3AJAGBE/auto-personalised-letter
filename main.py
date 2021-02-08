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
        # Create the personalised letters
        with open(f"complete/congratulatory_letters/{name}_letter.txt", mode="w") as format_letter:
            format_letter.write(add_names)

