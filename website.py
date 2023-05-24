from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/verification')
def verif():
    return render_template("verification.html")


@app.route('/', methods=['POST', 'GET'])
def log_in():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        with open('logs.txt') as f:
            logs = f.readlines()
            print(logs)
            if logs[0][:-1] == username and logs[1] == password:
                return redirect('/verification') # перенаправление на другую страницу
            else:
                error = "Неправильный логин или пароль. Попробуйте снова."
                return render_template('log_in.html', error=error)

    else:
        return render_template("log_in.html")


def start():
    app.run(debug=True)