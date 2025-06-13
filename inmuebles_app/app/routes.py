from flask import Blueprint, render_template, request, redirect, url_for, flash
from controlador.datos_controller import DatosController

routes_bp = Blueprint('routes', __name__)
controlador = DatosController()

@routes_bp.route('/')
def index():
    datos = controlador.listar_datos()
    return render_template('index.html', datos=datos)

@routes_bp.route('/ultimos')
def ultimos_registros():
    try:
        datos = controlador.listar_datos()
        registros = datos[-5:] if datos else []  # Últimos 5 registros desde la lista completa
        return render_template('ultimos.html', registros=registros)
    except Exception as e:
        flash(f"Error al cargar los últimos registros: {str(e)}", "error")
        return redirect(url_for('routes.index'))

@routes_bp.route('/crear', methods=['GET', 'POST'])
def crear_registro():
    if request.method == 'POST':
        try:
            registro_scuep = request.form['registro_scuep']
            anio = int(request.form['anio'])
            proyecto = request.form['proyecto']
            direccion = request.form['direccion']
            unidades = int(request.form['unidades'])
            enajenador = request.form['enajenador']

            controlador.crear_dato(registro_scuep, anio, proyecto, direccion, unidades, enajenador)
            flash("Registro creado correctamente", "success")
            return redirect(url_for('routes.index'))
        except ValueError:
            flash("Error: Año y unidades deben ser valores numéricos", "error")
        except Exception as e:
            flash(f"Error al crear el registro: {str(e)}", "error")
    return render_template('crear.html')

@routes_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_registro(id):
    if request.method == 'POST':
        try:
            nuevo_proyecto = request.form['proyecto']
            controlador.actualizar_dato(id, nuevo_proyecto)
            flash("Registro actualizado correctamente", "success")
            return redirect(url_for('routes.index'))
        except Exception as e:
            flash(f"Error al actualizar el registro: {str(e)}", "error")

    datos = controlador.listar_datos()
    registro = next((d for d in datos if d[0] == id), None)
    if not registro:
        flash("Registro no encontrado", "error")
        return redirect(url_for('routes.index'))
    return render_template('actualizar.html', registro=registro)

@routes_bp.route('/eliminar/<int:id>')
def eliminar_registro(id):
    try:
        controlador.eliminar_dato(id)
        flash("Registro eliminado correctamente", "success")
    except Exception as e:
        flash(f"Error al eliminar el registro: {str(e)}", "error")
    return redirect(url_for('routes.index'))

@routes_bp.route('/cargar', methods=['GET', 'POST'])
def cargar_datos_publicos():
    if request.method == 'POST':
        try:
            controlador.cargar_datos_publicos()
            flash("Datos públicos cargados correctamente", "success")
        except Exception as e:
            flash(f"Error al cargar datos públicos: {str(e)}", "error")
        return redirect(url_for('routes.index'))
    return render_template('cargar.html')