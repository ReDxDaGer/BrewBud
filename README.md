# BrewBud
This project is only for learning purpose 
# Getting started 

**1. Clone the Repo into your local machine**

```bash
git clone git@github.com:ReDxDaGer/Flask-Project.git
```
**2. Setup the env and download all the requirements**

```bash
python -m venv env
source env/bin/activate
pip install pandas
pip install flask

```

``Now you are ready to get started with the project``

## How it Works

1. **Initialization**: Flask application is initialized.

2. **Routes**:
   - **Index Route** (`/`): Renders the `index.html` template, which contains an HTML form for users to input their data.
   - **Process Route** (`/process`): Handles form submission via POST method. It extracts user data from the form, stores it in a dictionary, appends it to a list called `stored_data`, and then updates the CSV file with the new data.

3. **Global Variables**:
   - `stored_data`: An empty list that will store dictionaries of user data.
   - `csv_filename`: Name of the CSV file where user data will be stored.

4. **Update CSV Function** (`update_csv()`):
   - Converts the `stored_data` list into a pandas DataFrame.
   - Writes the DataFrame to a CSV file specified by `csv_filename`.
   - This function is called after each user submits the form to ensure the CSV file is updated with the latest data.

## How to Use

- Run the script.
- Access the web application via a web browser.
- Fill out the form with user data (name, phone number, email) and submit.
- The submitted data will be stored in a CSV file named `user_data.csv`.
- Each submission will append new data to the CSV file.

## Note

- This is a basic example and might need additional features for production use, such as input validation, error handling, and security measures.
- Ensure proper file permissions for writing to the CSV file.
- For deployment, consider using a more robust web server such as Gunicorn instead of Flask's built-in server.
