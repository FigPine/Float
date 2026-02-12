from flask import Flask,render_template

app=Flask(__name__)

app.config['SECRET_KEY'] = 'dev-key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/savedNotes')
def saved_notes():
    return render_template('savedNotes.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)