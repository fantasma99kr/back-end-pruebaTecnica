from flask import jsonify
from .database import db_con

#prueba con la base de datos
def datosaeropuerto():
    #conexion a la base de datos
    conn = db_con()
    if not conn:
        return jsonify({"error": "Error de conexión"}), 500
        
    #consulta a la base de datos
    try:
        cursor = conn.cursor()
            
        #aeropuerto con mayor movimiento
        cursor.execute("SELECT TOP 1 a.nombre_aeropuerto, COUNT(*) FROM vuelos v JOIN aeropuertos a ON v.id_aeropuerto = a.id_aeropuerto GROUP BY a.nombre_aeropuerto ORDER BY 2 DESC")
        r1 = cursor.fetchone()

        #aerolinea con mas vuelos
        cursor.execute("SELECT TOP 1 al.nombre_aerolinea, COUNT(*) FROM vuelos v JOIN aerolineas al ON v.id_aerolinea = al.id_aerolinea GROUP BY al.nombre_aerolinea ORDER BY 2 DESC")
        r2 = cursor.fetchone()

        #dia con mas vuelos
        cursor.execute("SELECT TOP 1 dia, COUNT(*) FROM vuelos GROUP BY dia ORDER BY 2 DESC")
        r3 = cursor.fetchone()

        #aerolineas con mas de 2 vuelos por día
        cursor.execute("SELECT TOP 2 al.nombre_aerolinea FROM vuelos v JOIN aerolineas al ON v.id_aerolinea = al.id_aerolinea GROUP BY al.nombre_aerolinea, v.dia ORDER BY COUNT(*) DESC")
        r4 = cursor.fetchall()

        return jsonify({
            "aeropuerto_mayor_movimiento": {"nombre": r1[0], "total": r1[1]},
            "aerolinea_mayor_vuelos": {"nombre": r2[0], "total": r2[1]},
            "dia_mayor_vuelos": {"fecha": str(r3[0]), "total": r3[1]},
            "aerolineas_mas_dos_vuelos": f"{r4[0][0]} y {r4[1][0]}"
        }),200


    except Exception as e:
        return jsonify({"error": str(e)}),500
    #se cierra la conexion con la base de datos
    finally:
        conn.close()