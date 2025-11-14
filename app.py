from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos en memoria (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'  # Base de datos temporal
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir un modelo de base de datos simple
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para login
@app.route('/login')
def login():
    return render_template('login.html')

# Ruta para registro
@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('registro.html')

# Ruta para dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Crear la base de datos y las tablas
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear la base de datos si no existe
    app.run(debug=True)
