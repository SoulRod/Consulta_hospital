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
    try:
        if request.method == 'POST':
            prioridad = 0
            riesgo = 0
            # Validaciones para agregar usuarios correctamente      

            if request.form.get('nombre') is None:
                flash('Favor ingresar Nombre')
                return redirect(url_for('Index'))
            else:
                nombre = request.form['nombre']
            if request.form.get('edad') is None:
                flash('Favor ingresar Edad')
                return redirect(url_for('Index'))
            else:
                edad = request.form['edad']
            if request.form.get('dieta') is None:
                dieta = "NO"
            else:
                dieta = request.form['dieta']
            if request.form.get('fumador') is None:
                fumador = 0
            else:
                fumador = request.form['fumador']
            if request.form.get('estatura') is None:
                estatura = 0
            else:
                estatura = request.form['estatura']
            if request.form.get('peso') is None:
                peso = 0
            else:
                peso = request.form['peso']

            # Validacion para estatura / peso

            if int(edad) > 0 and int(edad) <= 15:
                pesoestatura = (int(estatura) / int(peso))
            else:
                pesoestatura = 0

            # Validacion para asignar prioridad a pacientes (Niños).

            if int(edad) > 0 and int(edad) <= 5:
                prioridad = (int(estatura) - int(peso)) + 3
            elif int(edad) > 5 and int(edad) <= 12:
                prioridad = (int(estatura) - int(peso)) + 2
            elif int(edad) >= 13 and int(edad) <= 15:
                prioridad = (int(estatura) - int(peso)) + 1

            # Validacion para asignar prioridad a pacientes (Jovenes).

            if int(edad) >= 16 and int(edad) <= 40:
                if int(fumador) >0:
                    prioridad = (int(fumador) / 4) + 2
                elif int(fumador) == 0:
                    prioridad = 2

            # Validacion para asignar prioridad a pacientes (Ancianos).

            if int(edad) >= 60 and int(edad) <=100 and str(dieta.upper()) == "SI":
                prioridad = (int(edad) / 20) + 4
            elif int(edad) >= 60 and int(edad) <=100 and str(dieta.upper()) == "NO":
                prioridad = (int(edad) / 20) + 3
            elif int(edad) >= 41 and int(edad) < 60 and str(dieta.upper()) == "SI":
                prioridad = (int(edad) / 30) + 3
            elif int(edad) >= 41 and  int(edad) < 60 and str(dieta.upper()) == "NO":
                prioridad = (int(edad) / 30) + 3

            # Validacion para asignar Riesgo a pacientes.

            if int(edad) >= 0 and int(edad) <= 40:
                riesgo = (int(edad) * prioridad) / 100
            elif int(edad) >= 41:
                riesgo = (int(edad) * prioridad) / 100 + 5.3

            # Validar no asignados a pacientes

            if int(edad) >= 0 and int(edad) < 45:
                dieta = "NO"

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO paciente (nombre,edad,nhistoriaclinica,tieneDieta,relacionPeso,fumador,prioridad,riesgo ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", 
            (nombre, edad, "", dieta.upper(), pesoestatura, fumador, prioridad, riesgo))
            mysql.connection.commit()
            flash('Paciente Agregado Satisfactoriamente')
            return redirect(url_for('Index'))
    except:
        flash('Favor ingresar datos correctamente')
        return redirect(url_for('Index'))

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

