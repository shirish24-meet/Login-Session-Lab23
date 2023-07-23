from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/',methods=['GET','POST']) # What methods are needed?
def home():
	try:
		if request.method == 'GET':
			return render_template('home.html')
		else:
			name = request.form['name']
			age = request.form['age']
			quote = request.form['quote']
			login_session['name'] = name
			login_session['age'] = age
			login_session['quote'] = quote
			return redirect(url_for('display'))
	except:
		return redirect(url_for('error'))

	return render_template('home.html')

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', name1 = login_session["name"], age1 = login_session["age"], quote1 = login_session["quote"]) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)