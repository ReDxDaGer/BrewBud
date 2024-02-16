
# from flask import Flask, render_template, request

# app = Flask(__name__)

# stored_input = None  

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     global stored_input
#     user_input = request.form['user_input']
#     stored_input = user_input
#     print(f'The input from the user is: {user_input}. It has been stored.')
#     return f'The input from the user is: {user_input}. It has been stored.'

# if __name__ == '__main__':
#     app.run(debug=True)





import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


stored_data = []  
csv_filename = 'user_data.csv'

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
    
    print(f'The input from the user is: {user_data}. It has been stored.')

    # Update the CSV file with the new data
    update_csv()

    return f'The input from the user has been stored.'

def update_csv():
    global stored_data
    df = pd.DataFrame(stored_data)
    df.to_csv(csv_filename, index=False)
    print(f'Data has been written to {csv_filename}.')


if __name__ == '__main__':
    app.run(debug=True)
