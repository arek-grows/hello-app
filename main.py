from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


# if and for statements
@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks=score)


@app.route('/result')
def result():
    dict = {'Physics': 50, "Chemistry": 60, "Algebra": 70}
    return render_template('result.html', result=dict)


# temperature converter
@app.route("/converter")
def converter():
    celsius = request.args.get("celsius", "")  # dictionary method get(). if celsius doesn't exist, return ""
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return render_template('converter.html', celsius=celsius, fahrenheit=fahrenheit)


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
