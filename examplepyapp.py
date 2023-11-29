from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Virtual Machine!'

@app.route('/about')
def about():
    return 'About page.'

@app.route('/contact')
def contact():
    return 'Contact us at burner@email.com'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
