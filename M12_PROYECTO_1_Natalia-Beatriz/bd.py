# CONEXIÓN BASE DE DATOS

import mysql.connector as mysql

def conectarDB():
    try:
        db = mysql.connect(
            host = 'localhost',
            database = 'centros',
            user = 'root',
            passwd = ''
        )
        return db
    
    except mysql.Error as error:
        print(f"Error al intentar conectarse a la base de datos: {error}")
        return None


# CENTRO EDUCACION


# GET Educacion

def llamadaCentroEducacion(codigo_postal_educacion, nombre_educacion, fecha_inicio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        if codigo_postal_educacion is None and nombre_educacion is None and fecha_inicio is None:
            # Consulta para obtener todos los centros educativos
            consulta = 'SELECT codigo_postal_educacion, nombre_educacion, fecha_inicio FROM centro_educacion'
            cursor.execute(consulta)
        else:
            # Generación de condiciones para la consulta
            condiciones = []
            valores = []

            if codigo_postal_educacion:
                condiciones.append("codigo_postal_educacion = %s")
                valores.append(codigo_postal_educacion)

            if nombre_educacion:
                condiciones.append("nombre_educacion = %s")
                valores.append(nombre_educacion)

            if fecha_inicio:
                condiciones.append("fecha_inicio = %s")
                valores.append(fecha_inicio)

            consulta = 'SELECT codigo_postal_educacion, nombre_educacion, fecha_inicio FROM centro_educacion'
            
            if condiciones:
                consulta += ' WHERE ' + ' AND '.join(condiciones)

            cursor.execute(consulta, tuple(valores))
        resultado_educacion = cursor.fetchall()

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "error en consulta"}
    
    finally: 
        cursor.close()
        db.close()
    
    return resultado_educacion

# POST Educacion

def insertarCentroEducacion(nombre_educacion, nombre_barrio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = "INSERT INTO centro_educacion (nombre_educacion, nombre_barrio) VALUES (%s, %s)"
        cursor.execute(consulta, (nombre_educacion, nombre_barrio))
        db.commit()

        if cursor.rowcount > 0:
            return {"mensaje": "Centro educativo insertado"}, 201
        else:
            return {"error": "No se pudo insertar el centro educativo"}, 500
    

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "error en consulta"}
    
    finally:
        cursor.close()
        db.close()

    return {"--CENTRO DE EDUCACION INSERTADO--"}

# PUT Educacion

def actualizarCentroEducacion(id_educacion, fecha_inicio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)
    
    try:
        consulta = "UPDATE centro_educacion SET fecha_inicio = %s WHERE id_educacion = %s"
        cursor.execute(consulta, (fecha_inicio, id_educacion))
        db.commit()

    except mysql.Error as error:
        print(f"Error al actualizar centro educativo: {error}")
        return {"error": "error al actualizar"}

    finally:
        cursor.close()
        db.close()

    return {"--CENTRO DE EDUCACION ACTUALIZADO--"}

# DELETE educacion

def borrarCentroEducacion(id_educacion, nombre_educacion):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        if id_educacion:
            consulta = "DELETE FROM centro_educacion WHERE id_educacion = %s"
            cursor.execute(consulta, (id_educacion,))
        elif nombre_educacion:
            consulta = "DELETE FROM centro_educacion WHERE nombre_educacion = %s"
            cursor.execute(consulta, (nombre_educacion,))
        db.commit()

    except mysql.Error as error:
        print(f"Error al borrar centro educativo: {error}")
        return {"error": "error al borrar"}
    
    finally:
        cursor.close()
        db.close()

    return {"--CENTRO DE EDUCACION ELIMINADO--"}


# CENTRO SANIDAD

# GET Sanidad

def llamadaCentroSanidad(codigo_postal_sanidad, nombre_sanidad, nombre_barrio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        if codigo_postal_sanidad is None and nombre_sanidad is None and nombre_barrio is None:
            consulta = 'SELECT codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad'
            cursor.execute(consulta)
        else:
            if nombre_sanidad and nombre_barrio:
                consulta = 'SELECT codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad WHERE codigo_postal_sanidad = %s AND nombre_sanidad = %s AND nombre_barrio = %s'
                cursor.execute(consulta, (codigo_postal_sanidad, nombre_sanidad, nombre_barrio))
            elif nombre_sanidad:
                consulta = 'SELECT codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad WHERE codigo_postal_sanidad = %s AND nombre_sanidad = %s'
                cursor.execute(consulta, (codigo_postal_sanidad, nombre_sanidad))
            elif nombre_barrio:
                consulta = 'SELECT codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad WHERE codigo_postal_sanidad = %s AND nombre_barrio = %s'
                cursor.execute(consulta, (codigo_postal_sanidad, nombre_barrio))
            else:
                consulta = 'SELECT codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad WHERE codigo_postal_sanidad = %s'
                cursor.execute(consulta, (codigo_postal_sanidad,))
        
        resultado_sanidad = cursor.fetchall()
        

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "error en consulta"}
    
    finally:
        cursor.close()
        db.close()

    return resultado_sanidad

# POST Sanidad

def insertarCentroSanidad(nombre_sanidad, nombre_barrio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = "INSERT INTO centro_sanidad (nombre_sanidad, nombre_barrio) VALUES (%s, %s)"
        cursor.execute(consulta, (nombre_sanidad, nombre_barrio))
        db.commit()

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "error en consulta"}
    
    finally:
        cursor.close()
        db.close()

    return {"--CENTRO DE SANIDAD INSERTADO--"}

# PUT Sanidad

def actualizarCentroSanidad(nombre_sanidad, nombre_barrio, codigo_postal_sanidad):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = "UPDATE centro_sanidad SET nombre_sanidad = %s, nombre_barrio = %s WHERE codigo_postal_sanidad = %s"
        cursor.execute(consulta, (nombre_sanidad, nombre_barrio, codigo_postal_sanidad))
        db.commit()

    except mysql.Error as error:
        print(f"Error al actualizar centro sanitario: {error}")
        return {"error": "error al actualizar"}
    
    finally:
        cursor.close()
        db.close()

    return {"--CENTRO DE SANIDAD ACTUALIZADO--"}

# DELETE Sanidad

def borrarCentroSanidad(codigo_postal_sanidad):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = "DELETE FROM centro_sanidad WHERE codigo_postal_sanidad = %s"
        cursor.execute(consulta, (codigo_postal_sanidad,))
        db.commit()

    except mysql.Error as error:
        print(f"Error al borrar centro sanitario: {error}")
        return {"error": "error al borrar"}
    
    finally:
        cursor.close()
        db.close()

    return {"--CENTRO DE SANIDAD ELIMINADO--"}