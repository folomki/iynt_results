import os

def team_index(team_name):
    if team_name == '':
        return ''
    else:
        with open('files/teamList.txt', 'r') as file:
            k = 0

            for line in file:
                if line.strip() == '':
                    k += 1
                if line.strip() == team_name:
                    return str(k)


def teamlist(filename):
    with open(filename, 'r') as file:
        stroki = file.readlines()
        lines = [stroki[0]]
        for i in range(len(stroki) - 1):
            if stroki[i].strip() == '':
                lines.append(stroki[i + 1].strip())

    return lines


def players(team):
    with open("files/teamList.txt", 'r') as file:
        lines = file.readlines()
        players = []
        for i in range(len(lines)):
            if lines[i].strip() == team:
                i += 1
                while lines[i].strip() != "":
                    if (i + 1) == len(lines):
                        players.append(lines[i].strip())
                        i +=1
                        break
                    else:
                        players.append(lines[i].strip())
                        i += 1

    return players


def players_index(name):
    with open('files/teamList.txt', 'r') as file:
        k = 0
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].strip() == name:
                i -= 2

                while lines[i].strip() != "":
                    i -= 1
                    k += 1
                return str(k)


def jurylist(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines


def jury_index(jury_name):
    with open('files/juryList.txt', 'r') as file:

        k = 0
        for line in file:
            if line.strip() == jury_name:
                return str(k)
            else:
                k += 1


def problem_list(filename):
    with open(filename, 'r') as file:
        stroki = file.readlines()
        lines = ["None"]
        for i in range(len(stroki)):
            if stroki[i].strip() != "fakeProblem":
                lines.append(stroki[i].strip())

    return lines


def problem_index(problem):
    with open('files/problemList.txt', 'r') as file:
        k = 0

        for line in file:
            if problem == "None":
                return ""

            elif line.strip() != problem:
                k += 1
            else:
                return str(k)


def delete():
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = os.path.join(file)
            os.remove(file_path)
