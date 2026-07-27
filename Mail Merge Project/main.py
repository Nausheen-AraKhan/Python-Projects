PLACEHOLDER="[name]"
with open("./input/Names/invited_names.txt") as f:
    names=f.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt") as file:
    letter_contents=file.read()
    for name in letter_contents:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as sending_file:
            sending_file.write(new_letter)