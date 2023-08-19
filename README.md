# CS50 Library Manager
#### Video Demo:  https://youtu.be/dum9I-ds3f4
#### Description:
# CS50 Library Manager

CS50 Library Manager is a Python application designed to help you efficiently manage your library collection. With its user-friendly interface and comprehensive features, this application simplifies the process of adding, deleting, and lending books. Built using the tkinter library and leveraging the capabilities of SQLite, CS50 Library Manager is a reliable tool for librarians.

## Features

### Book Management
CS50 Library Manager allows you to seamlessly add new books to your library. Simply enter the book's title, author, genre, and unique ID, and the application will store this information in its database. This feature ensures that all your books are properly cataloged, making it easier to keep track of your collection.

In addition to adding books, you can also delete books from your library. By specifying the book's ID, the application will promptly remove the book's entry from the database. This feature enables you to efficiently manage your library by removing outdated or irrelevant books.

### Book Lending
One of the key features of CS50 Library Manager is the ability to lend books. With just a few clicks, you can lend books to borrowers and keep track of the lending status. When lending a book, the application checks its availability and assigns a return date automatically. The default return date is set to 15 days from the current date, ensuring that borrowers have sufficient time to enjoy the book before returning it.

### Book Return
When a borrower returns a book, CS50 Library Manager simplifies the process by allowing you to easily mark the book as returned. By entering the book's ID, the application updates the lending status and removes it from the active loans list. This feature ensures accurate record-keeping and streamlines the book return process.

### Book Listing
CS50 Library Manager provides a convenient way to view all the books in your library. The application retrieves the information from the database and displays it in a user-friendly format. You can quickly browse through the titles, authors, genres, and IDs of the books in your collection, making it easy to find specific books or get an overview of your library.

## Getting Started
To get started with CS50 Library Manager, follow these steps:

1. Clone the repository or download the source code to your local machine.
2. Ensure that you have Python 3.x and the required libraries installed (tkinter and SQLite).
3. Run the `library_manager.py` file using Python.
4. The main window of CS50 Library Manager will open, presenting you with options to add/delete books, manage loans, and show books.
5. Follow the on-screen instructions to perform the desired actions. Use the intuitive interface to navigate through the features and manage your library efficiently.

## Contributing
Contributions to CS50 Library Manager are welcome! If you find any issues or have suggestions for new features, feel free to create an issue or submit a pull request. Please follow the code formatting and documentation guidelines provided in the repository.

## About the Author
CS50 Library Manager was developed by Karolis Jakas Stirbyte. As a passionate software developer and book lover, Karolis created this application to combine his interests and provide a practical solution for library management. With a strong focus on usability and functionality, Karolis aimed to develop a tool that empowers users to organize and enjoy their book collections.

## Acknowledgments
CS50 Library Manager was inspired by the CS50 course and the knowledge gained during its completion. Special thanks to the CS50 team for their guidance and support throughout the learning journey. Additionally, thanks to OpenAI for providing the ChatGPT model used to assist in creating this README file.