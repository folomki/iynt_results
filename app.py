from flask import Flask, render_template, request, send_file
import functions


app = Flask(__name__)
app.secret_key = "anton"


# global variable for storing information and the number of teams in SF
number_of_teams = 3
number_of_jury = 0
teams_in_SF = []
players_in_sf = []


@app.route("/")
def index():
    functions.delete()
    with open("files/tournament.txt", "r") as file:
        tournament = file.readline().strip()

    return render_template('index.html', tournament=tournament)


@app.route("/configuration")
def config():
    functions.delete()

    return render_template('configuration.html')


@app.route("/cdownload", methods=['POST', 'GET'])
def cdownload():
    functions.delete()

    number_of_teams = int(request.form['number'])
    number = number_of_teams // 3 + 1 if number_of_teams % 3 != 0 else number_of_teams // 3
    file_name = "configuration.txt"

    with open(file_name, 'a') as file:
        file.write((str(number) + ' ') * 4 + '3 ' + '1')

    return send_file(file_name, as_attachment=True)


@app.route("/intro_teams")
def intro_teams():
    functions.delete()

    return render_template("introteams.html")


@app.route("/intro", methods=['POST', 'GET'])
def intro():
    functions.delete()

    global number_of_teams, number_of_jury
    number_of_teams = int(request.form['number_of_teams'])
    number_of_jury = int(request.form['number_of_jury'])

    teams = functions.teamlist("files/teamList.txt")
    jury = functions.jurylist("files/juryList.txt")

    return render_template('intro.html', teams=teams, number_of_teams=number_of_teams, number_of_jury=number_of_jury, jury=jury)


@app.route("/idownload", methods=['POST', 'GET'])
def idownload():
    functions.delete()

    file_name = "resultsintro.txt"

    with open(file_name, 'a') as file:
        file.write('Intro\n')

        global number_of_jury, number_of_teams

        for j in range(number_of_jury):
            file.write(str(functions.jury_index(request.form['jury' + str(j)])) + " ")
                       
        file.write('\n')

        for i in range(number_of_teams):
            file.write(functions.team_index(request.form[('team' + str(i))]) + ' ')
            file.write(str(request.form[('team_yc' + str(i))]) + '\n')
            file.write(str(request.form[('team_mark' + str(i))]) + '\n')

    return send_file(file_name, as_attachment=True)


@app.route("/resultsteams")
def resultsteams():
    functions.delete()

    teams = functions.teamlist("files/teamList.txt")

    return render_template("resultsteams.html", teams=teams)


@app.route("/results", methods=['POST', 'GET'])
def results():
    functions.delete()

    global number_of_jury, number_of_teams, teams_in_SF, players_in_sf
    number_of_jury = int(request.form['number_of_jury'])
    if str(request.form['team2']) == str(request.form['team3']):
        number_of_teams = 2
    else:
        number_of_teams = 3

    teams_in_SF = [request.form['team1'], request.form['team2'], request.form['team3']]
    players_in_sf = []
    players_in_sf = [functions.players(teams_in_SF[0]), functions.players(teams_in_SF[1]), functions.players(teams_in_SF[2])]

    jury = functions.jurylist("files/juryList.txt")
    problems = functions.problem_list("files/problemList.txt")

    return render_template('results.html', number_of_jury=number_of_jury, number_of_teams=number_of_teams, jury=jury, problems=problems, teams_in_SF=teams_in_SF, players_in_sf=players_in_sf)


@app.route("/rdownload", methods=['POST', 'GET'])
def rdownload():
    functions.delete()

    file_name = str(request.form['file_name']) + '.txt'

    with open(file_name, 'a') as file:
        file.write(str(request.form['sf_name']) + '\n')

        global number_of_jury, number_of_teams, teams_in_SF
        for i in range(number_of_teams):
            file.write(str(functions.team_index(teams_in_SF[i])) + ' ')
        file.write('\n')

        for j in range(number_of_jury):
            file.write(str(functions.jury_index(request.form['jury' + str(j)])) + " ")
        file.write('\n')

        for i in range(number_of_teams):
            file.write(str(functions.problem_index(request.form['r_problem0_' + str(i)])) + " " + str(functions.problem_index(request.form['r_problem1_' + str(i)])) + " " + str(functions.problem_index(request.form['r_problem2_' + str(i)])) + '\n')
            file.write(str(functions.problem_index(request.form['a_problem' + str(i)])) + '\n')
            file.write(str(functions.players_index(request.form['rep' + str(i)])) + " " + str(functions.players_index(request.form['opp' + str(i)])) + " " + str(functions.players_index(request.form['rew' + str(i)])) + '\n')
            file.write('x x x x x x x\n')
            file.write(str(request.form['repp' + str(i)]) + '\n')
            file.write(str(request.form['oppp' + str(i)]) + '\n')
            file.write(str(request.form['revp' + str(i)]) + '\n')

    return send_file(file_name, as_attachment=True)
