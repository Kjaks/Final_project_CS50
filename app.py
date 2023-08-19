import sqlite3
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta

# Function that opens the add/delete books section
def add_delete_books():
    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        ID = id_entry.get()

        if title and author and genre and ID:
            # Connect to the database
            conn = sqlite3.connect('db/library.db')
            cursor = conn.cursor()

            # Check if the book already exists in the Books table
            cursor.execute('SELECT * FROM Books WHERE ID = ?', (ID,))
            existing_book = cursor.fetchone()

            if existing_book:
                messagebox.showerror("Error", "A book with that ID already exists.")
                clear_fields()
            else:
                # Insert a new book into the Books table
                cursor.execute('INSERT INTO Books (ID, title, author, genre) VALUES (?, ?, ?, ?)',
                               (ID, title, author, genre))
                conn.commit()

                messagebox.showinfo("Success", "The book has been successfully added.")
                clear_fields()

            # Close the database connection
            cursor.close()
            conn.close()

    def delete_book():
        delete_ID = delete_entry.get()

        if delete_ID:
            # Connect to the database
            conn = sqlite3.connect('db/library.db')
            cursor = conn.cursor()

            # Check if the book exists
            cursor.execute('SELECT * FROM Books WHERE ID = ?', (delete_ID,))
            book = cursor.fetchone()

            if book:
                # Delete the book from the Books table
                cursor.execute('DELETE FROM Books WHERE ID = ?', (delete_ID,))
                conn.commit()

                messagebox.showinfo("Success", "The book has been successfully deleted.")
                clear_fields()
            else:
                messagebox.showerror("Error", "No book found with that ID.")

            # Close the database connection
            cursor.close()
            conn.close()
        else:
            messagebox.showerror("Error", "Please enter the ID of the book you want to delete.")

    def clear_fields():
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        genre_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)
        delete_entry.delete(0, tk.END)

    # Create the window for adding or deleting books
    add_delete_window = tk.Tk()
    add_delete_window.title("Add/Delete Books")

    # Create the input fields
    title_label = tk.Label(add_delete_window, text="Title:")
    title_label.pack()
    title_entry = tk.Entry(add_delete_window)
    title_entry.pack()

    author_label = tk.Label(add_delete_window, text="Author:")
    author_label.pack()
    author_entry = tk.Entry(add_delete_window)
    author_entry.pack()

    genre_label = tk.Label(add_delete_window, text="Genre:")
    genre_label.pack()
    genre_entry = tk.Entry(add_delete_window)
    genre_entry.pack()

    id_label = tk.Label(add_delete_window, text="ID:")
    id_label.pack()
    id_entry = tk.Entry(add_delete_window)
    id_entry.pack()

    # Create the add book button
    add_button = tk.Button(add_delete_window, text="Add Book", command=add_book)
    add_button.pack()

    delete_label = tk.Label(add_delete_window, text="ID:")
    delete_label.pack()
    delete_entry = tk.Entry(add_delete_window)
    delete_entry.pack()

    # Create the delete book button
    delete_button = tk.Button(add_delete_window, text="Delete Book", command=delete_book)
    delete_button.pack()

    # Start the event loop for the add/delete books window
    add_delete_window.mainloop()

# Function to lend a book
def open_loans():
    def lend_book():
        ID = id_entry.get()

        if ID:
            # Connect to the database
            conn = sqlite3.connect('db/library.db')
            cursor = conn.cursor()

            # Check if the book has already been lent
            cursor.execute('SELECT * FROM Loans WHERE ID = ?', (ID,))
            book_lent = cursor.fetchone()

            if book_lent:
                messagebox.showerror("Error", "This book has already been lent.")
            else:
                # Check if the book is available for lending
                cursor.execute('SELECT * FROM Books WHERE ID = ?', (ID,))
                book = cursor.fetchone()

                if book:
                    # Get the return date (15 days from the current date)
                    return_date = datetime.now() + timedelta(days=15)

                    # Insert the loan record into the Loans table
                    cursor.execute('INSERT INTO Loans (ID, return_date) VALUES (?, ?)', (ID, return_date))
                    conn.commit()

                    messagebox.showinfo("Success", "The book has been successfully lent.")
                    show_loans()
                    clear_fields()
                else:
                    messagebox.showerror("Error", "No book found with that ID.")
        else:
            messagebox.showerror("Error", "Please enter the ID of the book to lend.")

    def return_book():
        ID = id_entry.get()

        if ID:
            # Connect to the database
            conn = sqlite3.connect('db/library.db')
            cursor = conn.cursor()

            # Check if the book is in the loans list
            cursor.execute('SELECT * FROM Loans WHERE ID = ?', (ID,))
            book_lent = cursor.fetchone()

            if book_lent:
                # Delete the loan record from the Loans table
                cursor.execute('DELETE FROM Loans WHERE ID = ?', (ID,))
                conn.commit()

                messagebox.showinfo("Success", "The book has been successfully returned.")
                show_loans()
                clear_fields()
            else:
                messagebox.showerror("Error", "The book is not in the loans list.")
        else:
            messagebox.showerror("Error", "Please enter the ID of the book to return.")

    def clear_fields():
        id_entry.delete(0, tk.END)

    def show_loans():
        # Clear the current records
        records_text.delete("1.0", tk.END)

        # Connect to the database
        conn = sqlite3.connect('db/library.db')
        cursor = conn.cursor()

        # Get the loan data from the Loans and Books tables
        cursor.execute('SELECT Books.ID, Books.title, Books.author, Books.genre, DATE(Loans.return_date) FROM Books INNER JOIN Loans ON Books.ID = Loans.ID')
        loans = cursor.fetchall()

        # Show the loan data in the records
        for loan in loans:
            records_text.insert(tk.END, f"ID: {loan[0]}\n")
            records_text.insert(tk.END, f"Title: {loan[1]}\n")
            records_text.insert(tk.END, f"Author: {loan[2]}\n")
            records_text.insert(tk.END, f"Genre: {loan[3]}\n")
            records_text.insert(tk.END, f"Return Date: {loan[4]}\n")
            records_text.insert(tk.END, "-------------------------\n")

        # Close the database connection
        cursor.close()
        conn.close()

    # Create the loans window
    loans_window = tk.Tk()
    loans_window.title("Loans")

    # Create the input field
    id_label = tk.Label(loans_window, text="Book ID:")
    id_label.pack()
    id_entry = tk.Entry(loans_window)
    id_entry.pack()

    # Create the lend button
    lend_button = tk.Button(loans_window, text="Lend Book", command=lend_book)
    lend_button.pack()

    # Create the return button
    return_button = tk.Button(loans_window, text="Return Book", command=return_book)
    return_button.pack()

    # Create the records text box
    records_text = tk.Text(loans_window)
    records_text.pack()

    # Show the current loans
    show_loans()

    # Start the event loop for the loans window
    loans_window.mainloop()

def show_books():
    # Connect to the database
    conn = sqlite3.connect('db/library.db')
    cursor = conn.cursor()

    # Get all the books from the Books table
    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Create a window to show the books
    books_window = tk.Tk()
    books_window.title("List of Books")

    # Create a text widget to show the books
    books_text = tk.Text(books_window)
    books_text.pack()

    # Show the books in the text widget
    if books:
        for book in books:
            books_text.insert(tk.END, f"Title: {book[1]}\nAuthor: {book[2]}\nGenre: {book[3]}\nID: {book[0]}\n\n")
    else:
        books_text.insert(tk.END, "No books in the library.")

    # Start the event loop for the books window
    books_window.mainloop()

# Create the main window
window = tk.Tk()
window.title("CS50 Library Manager")
window.geometry("640x480")

#Create copyright label
copyright_label = tk.Label(window, text="© Karolis Jakas Stirbyte 2023")
copyright_label.pack(side= tk.BOTTOM)

# Calculate the center of the window
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
center_x = int((window.winfo_screenwidth() / 2) - (window_width / 2))
center_y = int((window.winfo_screenheight() / 2) - (window_height / 2))
window.geometry(f"+{center_x}+{center_y}")

# Load the image
image = Image.open("images/CS50.png")

# Resize the image to the desired size
width = 500
height = 310
resized_image = image.resize((width, height))

# Convert the resized image to a tkinter PhotoImage object
photo = ImageTk.PhotoImage(resized_image)

# Show the image in a Label widget
label = tk.Label(window, image=photo)
label.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Button to open the add/delete books section
add_delete_button = tk.Button(button_frame, text="Add/Delete Books", command=add_delete_books, width=20, height=2)
add_delete_button.grid(row=0, column=0, padx=10)

# Button to open the loans section
loans_button = tk.Button(button_frame, text="Loans", command=open_loans, width=20, height=2)
loans_button.grid(row=0, column=1, padx=10)

# Button to show all books
show_books_button = tk.Button(button_frame, text="Show Books", command=show_books, width=20, height=2)
show_books_button.grid(row=0, column=2, padx=10)

# Start the event loop
window.mainloop()

