from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Any string you wish, but KEEP DO NOT SHARE IT'

# Renders index.html at http://localhost:5000/
@app.route('/')
def run_html():
    return render_template('index.html')

# Gathers user's input at http://localhost:5000/process_money, stores in session and redirects to http://localhost:5000/show
# NOTE: Always Redirect on a POST, never render
@app.route('/process_money', methods=['POST'])
def process_money():
    print('Got Post Info')
    if 'gold' not in session:
        session['gold'] = 0
    if request.form['building'] == 'farm':
        session['gold'] += (random.randint(10, 20))
        if session['gold'] > 2000:
            return redirect('/you_won')
        if session['gold'] < -2000:
            return redirect('/game_over')
        else:
            return redirect('/earn')
    if request.form['building'] == 'cave':
        session['gold'] += (random.randint(0, 100))
        if session['gold'] > 2000:
            return redirect('/you_won')
        if session['gold'] < -2000:
            return redirect('/game_over')
        else:
            return redirect('/earn')
    if request.form['building'] == 'casino':
        session['gold'] += (random.randint(-2000, 2000))
        if session['gold'] > 2000:
            return redirect('/you_won')
        if session['gold'] < -2000:
            return redirect('/game_over')
        else:
            return redirect('/earn')
    if request.form['building'] == 'house':
        session['gold'] += (random.randint(2, 5))
        if session['gold'] > 2000:
            return redirect('/you_won')
        if session['gold'] < -2000:
            return redirect('/game_over')
        else:
            return redirect('/earn')
    return redirect('/')

@app.route("/earn")
def run_earn_html():
    return render_template('earn.html')

@app.route("/return")
def goback():
    return redirect('/')

@app.route("/game_over")
def run_game_over_html():
    return render_template('game_over.html')

@app.route("/you_won")
def run_you_won_html():
    return render_template('you_won.html')

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)