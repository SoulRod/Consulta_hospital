from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuracion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hospital'
mysql = MySQL(app)

# Sesion Setting
app.secret_key = 'mysecretkey'

# Variables Globales
prioridad = 0
riesgo = 0
pesoestatura = 0

# Ruta Para index
@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM paciente ORDER BY riesgo DESC')
    informacion = cursor.fetchall()
    return render_template("index.html", pacientes = informacion)

# Ruta Para agregar pacientes a la agenda.
@app.route('/agregarPaciente', methods=['POST'])
def Agregar_Paciente():
    return "Agregar paciente"

# Ruta Para Listar pacientes fumadores urgentes
@app.route('/lista_pacientes_fumadores_urgentes')
def Listar_Pacientes_Fumadores_Urgentes():
    return "Lista de fumadores urgentes"

# Ruta Para Listar consulta con mas pacientes
@app.route('/consulta_pacientes')
def Consulta_mas_Pacientes_Atendidos():
    return "Pacientes Atendidos por Consulta"    

if __name__ == "__main__":
    app.run(port = 3000, debug = True)

