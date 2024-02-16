import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

csv_filename = 'user_data.csv'

def read_csv():
    try:
        df = pd.read_csv(csv_filename)
        return df.to_dict('records')
    except FileNotFoundError:
        return []

stored_data = read_csv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    global stored_data
    user_data = {
        'Name': request.form['name'],
        'Phone Number': request.form['phone'],
        'Email': request.form['email']
    }
    stored_data.append(user_data)

    # Update the CSV file with the new data
    update_csv()

    return render_template('process.html')

def update_csv():
    global stored_data
    df = pd.DataFrame(stored_data)
    df.to_csv(csv_filename, index=False)
    print(f'Data has been written to {csv_filename}.')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_code=404, error_message="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code=500, error_message="Internal Server Error"), 500

if __name__ == '__main__':
    app.run(debug=True)
