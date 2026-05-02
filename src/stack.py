import requests, datetime
from flask import jsonify

def stackOver():
    try:
        #seccion de la consulta y transformacion a un diccionario para manipular los datos
        
        respuesta = requests.get("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow")
        datos = respuesta.json()
        lista = datos['items'] #obtiene la lista dentro de items para poder recorrerlos

        #variables
        contestadas = 0
        no_contestadas = 0
        max_rep = min_vistas = vieja = actual = lista[0]

        for item in lista:
            #1 contar las preguntas que tienen respuestas
            if item.get('is_answered'):
                contestadas += 1
            else: #si no tiene respuesta suma el contador
                no_contestadas += 1

            #2 mayor reputacion va remplazando de acuerdo a la reputacion de la pregunta
            if item['score'] > max_rep['score']:
                max_rep = item
                
            #3 menor número de vistas
            if item['view_count'] < min_vistas['view_count']:
                min_vistas = item
                    
            #4 obtiene la pregunta mas vieja creation_date y la pregunta mas actual
            if item['creation_date'] < vieja['creation_date']:
                vieja = item
            if item['creation_date'] > actual['creation_date']:
                actual = item

        #punto 5 imprimir en consola
        print("\n========== CONSOLA ==========")
        print(f"2. Pregunta con Mayor Reputación.\nTitulo de la pregunta: {max_rep['title']} puntuacion: {max_rep['score']}")
        print(f"3. Pregunta con Menor número de vistas.\n Titulo de la pregunta: {min_vistas['title']} numero de visitas: {min_vistas['view_count']}")
        print(f"4. Pregunta Fecha más vieja: {datetime.datetime.fromtimestamp(vieja['creation_date'])} titulo de la pregunta: {vieja['title']}")
        print(f"4. Fecha más actual: {datetime.datetime.fromtimestamp(actual['creation_date'])} titulo de la pregunta: {actual['title']}")
        print(f"5. Imprimir en consola del punto 2 al 5")
        print("===============================\n")

        return jsonify(
            {
                "conteo": {"contestadas": contestadas, "no_contestadas": no_contestadas},
                "mayor_reputacion": max_rep,
                "menor_vistas": min_vistas,
                "mas_vieja": vieja,
                "mas_actual": actual
            }
        ),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500