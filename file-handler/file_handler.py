import os

FILENAME = "notes.txt"

def write_note():
    note = input("Enter your note: ")
    with open(FILENAME, "a") as f:
        f.write(note + "\n")
    print("Note saved!")

def read_notes():
    if not os.path.exists(FILENAME):
        print("No notes found.")
        return
    with open(FILENAME, "r") as f:
        notes = f.readlines()
    if not notes:
        print("No notes found.")
    else:
        print("\nYour notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")

def delete_notes():
    if not os.path.exists(FILENAME):
        print("No notes to delete.")
        return
    confirm = input("Are you sure you want to delete all notes? (yes/no): ")
    if confirm.lower() == "yes":
        os.remove(FILENAME)
        print("All notes deleted.")
    else:
        print("Cancelled.")

while True:
    print("\n== Simple File Handler ==")
    print("1. Write a note")
    print("2. Read notes")
    print("3. Delete all notes")
    print("4. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        write_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3 or 4.")