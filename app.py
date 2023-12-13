from flask import Flask, render_template, request, send_file
import os
app = Flask(__name__)
app.secret_key = "anton"

@app.route("/")
def index():
    delete()

    return render_template('index.html')


@app.route("/configuration")
def config():
    delete()

    return render_template('configuration.html')


@app.route("/cdownload", methods=['POST', 'GET'])
def cdownload():
    number = int(request.form['number']) // 3 + 1
    file_name = "configuration.txt"

    with open(file_name, 'a') as file:
        file.write((str(number) + ' ')*4 + '3 ' + '1')

    return send_file(file_name, as_attachment=True)


@app.route("/intro")
def intro():
    delete()

    return render_template('intro.html')


@app.route("/idownload", methods=['POST', 'GET'])
def idownload():
    file_name = "resultsintro.txt"

    with open(file_name, 'a') as file:
        file.write('Intro\n')
        file.write(str(request.form['jury']) + '\n')

        for i in range(1, 34):
            file.write(str(request.form[('team' + str(i))]) + '\n')
            file.write(str(request.form[('mark' + str(i))]) + '\n')

    return send_file(file_name, as_attachment=True)



@app.route("/results")
def results():
    delete()

    return render_template('results.html')


@app.route("/rdownload", methods=['POST', 'GET'])
def rdownload():
    file_name = str(request.form['file_name']) + '.txt'
    number_teams = int(request.form['number_teams'])

    with open(file_name, 'a') as file:
        file.write(str(request.form['sf_name']) + '\n')
        file.write(str(request.form['teams']) + '\n')
        file.write(str(request.form['jury']) + '\n')

        file.write(str(request.form['r_problem1']) + '\n')
        file.write(str(request.form['a_problem1']) + '\n')
        file.write(str(request.form['participant1']) + '\n')
        file.write('x x x x x x x\n')
        file.write(str(request.form['repm1']) + '\n')
        file.write(str(request.form['oppm1']) + '\n')
        file.write(str(request.form['revm1']) + '\n')

        file.write(str(request.form['r_problem2']) + '\n')
        file.write(str(request.form['a_problem2']) + '\n')
        file.write(str(request.form['participant2']) + '\n')
        file.write('x x x x x x x\n')
        file.write(str(request.form['repm2']) + '\n')
        file.write(str(request.form['oppm2']) + '\n')
        file.write(str(request.form['revm2']) + '\n')

        if number_teams == 3:
            file.write(str(request.form['r_problem3']) + '\n')
            file.write(str(request.form['a_problem3']) + '\n')
            file.write(str(request.form['participant3']) + '\n')
            file.write('x x x x x x x\n')
            file.write(str(request.form['repm3']) + '\n')
            file.write(str(request.form['oppm3']) + '\n')
            file.write(str(request.form['revm3']) + '\n')

    return send_file(file_name, as_attachment=True)


def delete():
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = os.path.join(file)
            os.remove(file_path)