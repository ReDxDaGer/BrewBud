from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    # You can now use 'user_input' in your Python code
    return f'The input from the user is: {user_input}'
    print(user_input)

if __name__ == '__main__':
    app.run(debug=True)

