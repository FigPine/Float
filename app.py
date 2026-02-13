from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key'

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///float.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/savedNotes')
def saved_notes():
    notes = Note.query.all()
    return render_template('savedNotes.html', notes=notes)


@app.route('/editor', methods=['GET', 'POST'])
def editor():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('saved_notes'))
    return render_template('editor.html')

@app.route('/delete/<int:id>')
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('saved_notes'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)