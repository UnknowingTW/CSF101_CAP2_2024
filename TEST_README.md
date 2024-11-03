## OVERVIEW
This document describes the testing strategy for the Library System project, including resources used, justifications, and test case summaries. The tests validate core functionalities such as book borrowing, returning, and administration controls.

## Resources Used
1. Python unittest Framework: Chosen for its built-in, straightforward structure for Python testing, allowing isolated tests without external dependencies.
2. Project Classes: The Library, Book, User, and Admin classes were used directly to create realistic test scenarios reflecting actual system usage.

## Test Cases
Each test case focuses on a specific functionality or edge case:
1. Valid Book Borrowing: Ensures a user can borrow an available book.
2. Invalid Book Borrowing: Confirms a second user can't borrow an already borrowed book.
3. Valid Book Returning: Verifies a user can return a borrowed book, making it available again.
4. Invalid Book Returning: Prevents returning a book not borrowed by the user.
5. Admin Adding Books: Checks that the admin can add new books to the library.
6. Borrow All Books (Edge Case): Tests borrowing all books to ensure system handles resource limits.
7. Return Non-Borrowed Book (Edge Case): Prevents a user from returning a book borrowed by someone else.

## Conclusions
The test suite is comprehensive, covering core functionality and edge cases to ensure system robustness. Using unittest with project classes simulates realistic conditions and allows for easy test maintenance and scalability.