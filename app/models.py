from abc import ABCMeta, abstractmethod
import json
import uuid
import re
import logging
from datetime import datetime



class metaUsuarios(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def crear_usuario(self):
        pass
    @abstractmethod
    def buscar_usuario(self):
        pass
    @abstractmethod
    def editar_usuario(self):
        pass
    
    @abstractmethod
    def eliminar_usuario(self):
        pass
    
    

class Usuarios(metaUsuarios):
    def __init__(self):
        pass


    def crear_usuario(self,datos:dict,lista_usuarios:list):
        
        self.datos=datos
        self.usuarios=lista_usuarios
        #Se genera id en formato UUID
        self.uuid=str(uuid.uuid4())
        self.nombre=str(self.datos["nombre"])
        self.apellido=str(self.datos["apellido"])
        self.email=str(self.datos["email"])
        self.fecha_nacimiento=self.datos["fecha_nacimiento"]

        #valida formato de la fecha
        try: datetime.fromisoformat(self.fecha_nacimiento)
        except ValueError:
            logging.debug(f"Fecha nacimiento'{self.fecha_nacimiento}' incorrecta.")
            self.respuesta={"status":"failed",
                            "mensaje":"Fecha nacimiento incorrecta. intente: YYYY-MM-DD"}
            self.status=400
            return self.respuesta, self.status
            
        #No se pueden crear usuarios con el mismo email
        for user in self.usuarios:
            if self.email == user["email"]:
                logging.debug(f"mail en la lista: '{self.email}', mail ingresado: '{user['email']}'")
                self.nuevo_usuario={"status":"failed","mensaje":"usuario ya existe"}
                self.respuesta=self.nuevo_usuario
                self.status=400
                return self.respuesta, self.status
        #se valida el formato del mail con expresiones regulares
        if re.search("^[a-zA-Z0-9'_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$",self.email):
            self.nuevo_usuario={
                "uuid": self.uuid,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "email":self.email,
                "fecha_nacimiento":self.fecha_nacimiento
            }
           
            self.usuarios.append(self.nuevo_usuario)
            self.respuesta=self.nuevo_usuario
            self.status=200         
            logging.debug(f" mail '{self.email}' válido. Usuario creado: {self.nuevo_usuario}")
        else:
           
            self.respuesta={"status":"failed","mensaje":"Correo no válido"}
            self.status=400
            logging.debug(f" Correo '{self.email}' no válido")
       
        return self.respuesta, self.status

    def buscar_usuario(self,datos:dict,lista_usuarios:list):
        try:
            self.lista_usuarios=lista_usuarios
            self.datos=datos
            self.criterios=["uuid","nombre","apellido","email","fecha_nacimiento"]
            for criterio in self.criterios:
                
                if criterio in self.datos:
                    self.criterio=criterio
                    self.atributo=self.datos[criterio].lower()
                    logging.debug(f"atributo: {self.atributo}. Criterio: {self.criterio}")
                    break
            
            self.usuario_encontrado=[usuario for usuario in self.lista_usuarios if usuario[self.criterio].lower()==self.atributo]
            logging.debug(f" usuario encontrado: {self.usuario_encontrado}")
            if (len(self.usuario_encontrado)>0):
                self.respuesta=self.usuario_encontrado[0]
                self.status=200
            
                return self.respuesta, self.status
            
            self.respuesta={"status":"failed","mensaje":"No existen datos del usuario"}
            self.status=404
            return self.respuesta, self.status
       
        except AttributeError:
            self.respuesta={"status":"failed","mensaje":"No existe criterio"}
            self.status=404
            return self.respuesta, self.status


    def editar_usuario(self,consulta:dict,data:dict):
        try:
            self.data=data
            self.consulta=consulta
            self.criterios=["nombre","apellido","email","fecha_nacimiento"]

            
            logging.debug(f" Consulta: {self.consulta['nombre']} , data: {self.data['nombre']}, crit: {self.criterio}")

            for criterio in self.criterios:
                if self.data[criterio]!=self.consulta[criterio]:
                        self.consulta.update({criterio: self.data[criterio]})
            
            self.respuesta=self.consulta
            self.status=200
                

            return self.respuesta, self.status
    
        except KeyError:
            self.respuesta={"status":"failed","mensaje":"Debe actualizar los campos"}
            self.status=400
            return self.respuesta, self.status


    def eliminar_usuario(self,uuid,lista_usuarios):
        try:
            self.uuid=uuid
            self.lista_usuarios=lista_usuarios
            self.lista_editada=[self.lista_usuarios.remove[dato] for dato in self.lista_usuarios if dato["uuid"]==uuid]
            self.respuesta=self.lista_editada
            self.status=200
            if self.respuesta==[]:
                respuesta={"mensaje":"no existen datos"}
                status=200
                return respuesta, status
            else:
                return self.respuesta, self.status

        
        except KeyError:
            self.respuesta={"status":"failed","mensaje":"Debe actualizar los campos"}
            self.status=400
            return self.respuesta, self.status






