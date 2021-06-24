from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


# index
@app.route('/')
def index():
    return render_template('index.html', base_url=request.base_url)


# static files
@app.route('/static_files')
def static_files():
    return render_template('static_files.html')


# login
@app.route('/login')
def login():
    return render_template('login.html', base_url=request.base_url)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/logged_in', methods=['POST', 'GET'])
def logged_in():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


# if statement
@app.route('/score', methods=['POST', 'GET'])
def scores():
    if request.method == "POST":
        try:
            score = int(request.form['score'])
        except ValueError:
            score = "error: input was not a number"
    else:
        score = "request.method != 'POST'"
    return render_template('score.html', marks=score)


# sending form data to a template and for statement
@app.route('/student')
def student():
    return render_template('student.html', base_url=request.base_url)


@app.route('/student/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        score_dict = request.form
    else:
        score_dict = {'Physics': 50, "Chemistry": 60,
                      "Algebra": 70}  # can also use a dictionary to return to a template
    return render_template('result.html', result=score_dict)


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
