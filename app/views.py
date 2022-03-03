from crypt import methods
from flask import jsonify
from werkzeug.exceptions import BadRequestKeyError
import logging


from app import app, request
from app.models import Usuarios

logging.basicConfig(filename="models.log",
                    level=logging.DEBUG,
                    format="%(asctime)s - funcion: %(funcName)s - %(message)s"
                    )


lista_usuarios=[]
@app.route("/", methods=["GET"])
@app.route("/api/", methods=["GET"])
def Index():
    """ Ruta index: muestra la lista completa de usuarios existentes."""    
    if lista_usuarios==[]:
        respuesta={"mensaje":"no existen datos"}
        status=200
        return jsonify(respuesta), status
    else:
        return jsonify(lista_usuarios) 

@app.route("/api/registro", methods=["POST"])
def Registro():
    try:
        if request.method=="POST":

            data={
                "nombre":request.json["nombre"],
                "apellido":request.json["apellido"],
                "email":request.json["email"],
                "fecha_nacimiento":request.json["fecha_nacimiento"]
                }   
            usuario=Usuarios()
            respuesta, status=usuario.crear_usuario(data,lista_usuarios)

            return jsonify(respuesta), status
    except (BadRequestKeyError, KeyError) as error:
        logging.debug(f"Excepción: {error}")
        respuesta={"status":"Error","mensaje":"Formato Incorrecto"}
        status=400
        return jsonify(respuesta), status    


@app.route("/api/buscar", methods=["POST"])
def Buscar():
    try:
        data=request.json
        usuario=Usuarios()
        respuesta, status=usuario.buscar_usuario(data,lista_usuarios)
        return jsonify(respuesta), status
    except (BadRequestKeyError, KeyError) as error:
        logging.debug(f"Excepción: {error}")
        respuesta={"status":"Error","mensaje":"Formato Incorrecto"}
        status=400
        return jsonify(respuesta), status  
        
@app.route("/api/editar", methods=["POST"])
def Editar():
    try:
        uuid={"uuid": request.json["uuid"]}
        data=request.json["usuario"]
        usuarios=Usuarios()
        consulta, status=usuarios.buscar_usuario(uuid,lista_usuarios)
        editado=usuarios.editar_usuario(consulta,data)
        return jsonify(editado), status
    except (BadRequestKeyError, KeyError) as error:
        logging.debug(f"Excepción: {error}")
        respuesta={"status":"Error","mensaje":"Formato Incorrecto"}
        status=400
        return jsonify(respuesta), status  
    

@app.route("/api/eliminar", methods=["POST"])
def Eliminar():
    try:
        uuid={"uuid": request.json["uuid"]}
        usuarios=Usuarios()
        eliminado, status=usuarios.eliminar_usuario(uuid,lista_usuarios)
        return jsonify(eliminado), status
    except (BadRequestKeyError, KeyError) as error:
        logging.debug(f"Excepción: {error}")
        respuesta={"status":"Error","mensaje":"Formato Incorrecto"}
        status=400
        return jsonify(respuesta), status  
