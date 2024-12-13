from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'shhhhh!!!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show_result')


@app.route('/show_result')
def show_result():
    return render_template('result.html', name=session.get('name'), location=session.get('location'), language=session.get('language'), comment=session.get('comment'))


if __name__ == '__main__':
    app.run(debug=True)
