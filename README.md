# Contact Manager CLI

A command-line contact management application built with Python and SQLite.

This application allows users to add, view, search, update, and delete contacts using a persistent SQLite database.

---

## Features

- Add new contacts
- View all saved contacts
- Search contacts by name
- Update contact phone numbers
- Delete contacts
- Persistent SQLite database storage
- Case-insensitive contact searching
- Menu-driven command-line interface

---

## Technologies Used

- Python
- SQLite
- Git & GitHub

---

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd contact-manager
```

3. Run the application

```bash
python main.py
```

---

## Project Structure

```text
contact-manager/
│
├── main.py
├── contacts.db
├── README.md
└── .gitignore
```

---

## CRUD Operations Implemented

| Operation | Description |
|---|---|
| Create | Add new contacts |
| Read | View all contacts |
| Search | Find contacts by name |
| Update | Modify contact phone numbers |
| Delete | Remove contacts |

---

## Concepts Practiced

- CRUD operations
- SQLite database integration
- SQL queries
- Python functions
- Loops and conditionals
- Parameterized SQL queries
- Database connection management
- Resource cleanup using `conn.close()`

---

## Example Menu

```text
Contact Manager CLI

1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Update Contact
6. Exit
```

---

## Future Improvements

- Phone number validation
- Duplicate contact prevention
- Export contacts to CSV
- Graphical user interface (GUI)
- Object-oriented programming (OOP) refactor
- Contact sorting options

---

## Author

Julian Gonzalez

GitHub: https://github.com/jjuuls