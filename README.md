# subscription-demo
## Description

This project user subscription uses SQLite for data storage.  This project will include setting up a basic command-line interface (CLI) for subscription management, handling user input, and managing subscriptions in the SQLite database.

## Project Structure and Components
1. Database Setup:
   -  SQLite will be used to store subscription details. We'll create a table subscriptions with fields for id, user_id, start_date, end_date, and active.
2. Subscription Management Functions:
   -  Functions will be created to handle subscription creation, renewal, and retrieval from the database.
3. Command-Line Interface (CLI):
   -  We'll use argparse to create a simple CLI for interacting with the subscription management system. Users will be able to add subscriptions, renew them, and view existing subscriptions.
4. Error Handling:
   -  Basic error handling will be included to manage invalid inputs and database operations.

 ### Requirements
- Python (version X.X)
- SQLite3 (version X.X) installed on your system

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repository.git
   cd repository

### Creating a Virtual Environment
```bash
python -m venv myvenv
```
A virtual environment (myvenv) is recommended to isolate your project dependencies. Follow these steps to create and activate a myvenv for this project:

On Windows
Open a command prompt and navigate to your project directory:
```bash
myvenv\Scripts\activate
```
## Running the Project
1. Initialization: Run the database setup code (1. Setting Up the Database section) to create the SQLite database and table.
   -  Run the script to create the database
       ```bash
       py createdatabase.py
       ```

3. Subscription Management: Execute the CLI script (3. Command-Line Interface (CLI) section) to add, renew, or list subscriptions. For example:
  -  To add a subscription for user ID 1:
     ```bash 
       py subscription.py --add 1
     ```
  -  To renew a subscription with ID 1:
      ```bash
       python subscription.py --renew 1
      ```
  -  To list all subscriptions:
      ```bash
        python subscription.py --list
      ```
