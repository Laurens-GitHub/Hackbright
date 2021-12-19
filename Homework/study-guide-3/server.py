from flask import Flask, render_template, session, request
from random import choice
app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################

@app.route('/save-name', methods=["POST"])
def save_name():
    name = request.form.get('name')
    session['name'] = name
    return render_template('homepage.html')

@app.route('/form')
def show_form():

    return render_template('form.html')

@app.route('/results')
def show_results():
    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')

    if honest and cheery and dreary:
        result = "There exists a light and dark within all of us. What matters is the part we choose to act on."
    elif honest and cheery and not dreary:
        result = "You've got a great personality!"
    elif honest and dreary and not cheery:
        result = "You're gonna get what's coming to you."
    elif dreary and cheery and not honest:
        result = "You're gonna suffer, but you're gonna be happy about it."
    elif not honest and not cheery and dreary:
        result = "There was a man in a black hooded cloak carrying a sythe who was looking for you..."
    elif not dreary and not honest:
        result = "I can make all your troubles dissapear."
    else:
        result = "You need to make a choice."

    return render_template('results.html', message=result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
