# 📧 Mail Merge Project

A simple Python project that automates the process of creating personalized letters using a template and a list of names.

## 🚀 Features

* Reads a list of names from a text file.
* Uses a letter template with a placeholder.
* Replaces the placeholder with each person's name.
* Generates a personalized letter for every recipient.
* Saves all generated letters in an output folder.

## 📂 Project Structure

```text
Mail-Merge/
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   │
│   └── Letters/
│       └── starting_letter.txt
│
├── Output/
│   └── ReadyToSend/
│
├── main.py
└── README.md
```

## 🛠️ Technologies Used

* Python 3
* File Handling (`open()`)
* String Manipulation

## ▶️ How It Works

1. Read all names from `invited_names.txt`.
2. Open the letter template.
3. Replace the `[name]` placeholder with each recipient's name.
4. Create a new personalized letter.
5. Save each letter inside the `Output/ReadyToSend` folder.

## 💻 Example

### Template (`starting_letter.txt`)

```text
Dear [name],

You are invited to my birthday party this Saturday.

Hope to see you there!

Best wishes,
Angela
```

### `invited_names.txt`

```text
Alice
Bob
Charlie
```

### Generated Files

```text
letter_for_Alice.txt
letter_for_Bob.txt
letter_for_Charlie.txt
```

Each file contains a personalized version of the original letter.


## 📚 Concepts Practiced

* Reading text files
* Writing text files
* Loops
* String replacement
* Working with directories
* Automation with Python

## 🎯 Learning Outcome

This project demonstrates how Python can automate repetitive tasks like generating personalized documents, introducing essential file handling and text processing concepts used in real-world automation.

---

*This project was built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.*
