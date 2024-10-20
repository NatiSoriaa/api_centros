# INSTANCIAS Y RUTAS

from flask import Flask, request, jsonify
from bd import (
    llamadaCentroEducacion,
    llamadaCentroSanidad,
    insertarCentroEducacion,
    actualizarCentroEducacion,
    borrarCentroEducacion,
    actualizarCentroSanidad,
    insertarCentroSanidad,
    borrarCentroSanidad,
)
from auth import validarApiKey

app = Flask(__name__)



# RUTA A CENTRO EDUCACION



# RUTA A CENTRO EDUCACION
@app.route('/centro_educacion', methods=['GET','POST','PUT','DELETE'])
def ObtenerCentroEducacion():
    if not validarApiKey(request):
        return jsonify({"error": "Acceso no autorizado"}), 401

    # GET: obtener centro educativo
    if request.method == 'GET':
        codigoPostalE = request.args.get('codigo_postal_educacion')
        nombreE = request.args.get('nombre_educacion')
        fechaInicioE = request.args.get('fecha_inicio')

        # Si no se proporciona ningún filtro, devolver todos los centros
        if not codigoPostalE and not nombreE and not fechaInicioE:
            respuesta = llamadaCentroEducacion(None, None, None)  # Llamada sin parámetros
            if respuesta:
                return jsonify(respuesta), 200
            else:
                return jsonify({"error": "No se encuentran centros educativos"}), 404

        # Si hay filtros, se pasa a la función con los parámetros
        respuestaE = llamadaCentroEducacion(codigoPostalE, nombreE, fechaInicioE)
        if respuestaE:
            return jsonify(respuestaE), 200
        else:
            return jsonify({"error": "No se encuentra el centro educativo con los filtros proporcionados"}), 404

    # POST: insertar nuevo centro educativo
    elif request.method == 'POST':
        data = request.get_json()
        nombreE = data.get('nombre_educacion')
        codigoPostalE = data.get('codigo_postal_educacion')
        fechaInicioE = data.get('fecha_inicio')

        # Validar campos requeridos
        if not nombreE or not codigoPostalE or not fechaInicioE:
            return jsonify({"error": "faltan campos requeridos"}), 400

        try:
            insertarCentroEducacion(nombreE, codigoPostalE, fechaInicioE)
            return jsonify({"mensaje": "Centro educativo agregado"}), 201
        except ValueError as error:
            return jsonify({"error": "error al agregar"}), 500

    # PUT: actualizar fecha de inicio del centro educativo
    elif request.method == 'PUT':
        data = request.get_json()
        IdCentro = data.get('id_educacion')  
        nuevaFecha = data.get('fecha_inicio')

        # Validar campos requeridos
        if not IdCentro or not nuevaFecha:
            return jsonify({"mensaje": "faltan campos requeridos"}), 400

        try:
            actualizarCentroEducacion(IdCentro, nuevaFecha)
            return jsonify({"mensaje": "Fecha de inicio actualizada"}), 200
        except ValueError as error:
            return jsonify({"error": "error al actualizar"}), 500

    # DELETE: borrar centro educativo por ID
    elif request.method == 'DELETE':
        data = request.get_json()
        IdEducacion = data.get('id_educacion')

        # Validar campos requeridos
        if not IdEducacion:
            return jsonify({"mensaje": "faltan campos requeridos"}), 400

        try:
            borrarCentroEducacion(IdEducacion)
            return '', 204
        except ValueError as error:
            return jsonify({"error": "error al borrar"}), 500


# RUTA A CENTRO SANIDAD



@app.route('/centro_sanidad', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ObtenerCentroSanidad():
    if not validarApiKey(request):
        return jsonify({"error": "Acceso no autorizado"}), 401
    
    # GET: obtener centro sanitario
    if request.method == 'GET':
        codigoPostalS = request.args.get('codigo_postal_sanidad')
        nombreS = request.args.get('nombre_sanidad')
        barrioS = request.args.get('nombre_barrio')
        respuestaS = llamadaCentroSanidad(codigoPostalS, nombreS, barrioS)
        if respuestaS is not None:
            return jsonify(respuestaS), 200
        else:
            return jsonify({"error": "no se encuentra el centro de sanidad"}), 404

    # POST: insertar nuevo centro sanitario  
    elif request.method == 'POST':
        data = request.get_json()
        nombreS = data.get('nombre_sanidad')

        if not nombreS:
            return jsonify({"error": "faltan campos requeridos"}), 400
        try:
            insertarCentroSanidad(nombreS)
            return jsonify({"mensaje": "centro sanitario agregado"}), 201
        except ValueError as error:
            return jsonify({"error": "error al agregar"}), 500
    
    # PUT: actualizar centro sanitario
    elif request.method == 'PUT':
        data = request.get_json()
        idSanidad = data.get('id_sanidad')

        if not idSanidad:
            return jsonify({"error": "faltan campos requeridos"}), 400
        try:
            actualizarCentroSanidad(idSanidad)
            return jsonify ({"mensaje": "nombre del barrio actualizado"}), 200
        except ValueError as error:
            return jsonify({"error": "error al actualizar"}), 500
        
    # DELETE: eliminar centro sanitario
    elif request.method == 'DELETE':
        data = request.get_json()
        idSanidad = data.get('id_sanidad')

        if not idSanidad:
            return jsonify({"error":"faltan campos requeridos"}), 400
        try:
            borrarCentroSanidad(idSanidad)
            return '', 204
        except ValueError as error:
            return jsonify({"error": "error al eliminar"}), 500



if __name__ == '__main__':
    app.run(port=5001)


    
    


