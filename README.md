# Bank Management System

A Python-based command-line banking application that demonstrates Object-Oriented Programming (OOP), JSON data persistence, authentication using account number and PIN, and basic banking operations.

## Features

- Create new bank accounts
- Secure PIN hashing using bcrypt
- Deposit money
- Withdraw money
- View account details (Passbook)
- Update account information
- Close bank accounts
- Persistent storage using JSON

## Tech Stack

- Python
- JSON
- bcrypt
- pathlib
- datetime

## Project Structure

```text
Bank-Management-System/
├── main.py
├── data.json
└── README.md
```

## Installation

### Clone the repository

```bash
git clone https://github.com/manthanstar1-coder/Bank-Management-System.git
cd Bank-Management-System
```

### Install dependencies

```bash
pip install bcrypt
```

## Run the project

```bash
python main.py
```

## Application Menu

```text
1. Open Account
2. Deposit Money
3. Whidhraw Money
4. View Passbook
5. Update Details
6. Close Account
0. Exit
```

## Account Data Format

```json
{
  "Name": "CUSTOMER NAME",
  "DOB": "DD/MM/YYYY",
  "Age": 20,
  "Gender": "MALE",
  "Email": "customer@example.com",
  "Account No.": "123456789012345",
  "PIN": "bcrypt-hash",
  "Balance": 0
}
```

## Security

- PINs are not stored in plain text.
- bcrypt is used for hashing and verification.
- Authentication requires account number and PIN.

## Concepts Demonstrated

- Object-Oriented Programming
- File Handling
- JSON Serialization
- Authentication Systems
- Input Validation
- CRUD Operations
- Exception Handling

## Future Improvements

- Transaction history
- Fund transfer
- Stronger input validation
- SQLite/MySQL integration
- Unique account number validation
- Admin dashboard
- Unit testing

## Repository

GitHub Repository:
https://github.com/manthanstar1-coder/Bank-Management-System

## License

No license has been specified yet.