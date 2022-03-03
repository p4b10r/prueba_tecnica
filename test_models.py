import unittest
from app.models import Usuarios

from app import app

class TestUsuarios(unittest.TestCase):
    def setUp(self):
        self.usuarios=[dict({
            "nombre":"Nombre",
            "apellido":"Apellido",
            "email":"email@email.com",
            "fecha_nacimiento":"1111-11-11",
            "uuid":"891edb58-3a56-4362-a2bb-e5a9fad22d56"
        })]

        self.ingreso=dict({
            "uuid":"891edb58-3a56-4362-a2bb-e5a9fad22d56"
        })
        self.respuesta={
            "nombre":"Nombre",
            "apellido":"Apellido",
            "email":"email@email.com",
            "fecha_nacimiento":"1111-11-11",
            "uuid":"891edb58-3a56-4362-a2bb-e5a9fad22d56"
        }

        self.ok=200
        self.bad_request=400
        self.not_found=404

    def test_buscar_usuario(self):
        with app.app_context():

            self.respuesta_notfound={"status":"failed","mensaje":"No existen datos del usuario"}
            self.status=404


            usuario=Usuarios()
            self.dato, self.status=usuario.buscar_usuario(self.ingreso,self.usuarios)
            self.assertEqual(self.dato,self.respuesta)
            self.assertEqual(self.status,self.ok)
   
    def test_no_encuentra_usuario(self):
        with app.app_context():
            self.ingreso=dict({
           "uuid":"891edb58-3a56-4362-a2bb-e5a9fad22d55"
            })
            usuario=Usuarios()
            self.dato, self.status=usuario.buscar_usuario(self.ingreso,self.usuarios)
            self.respuesta={"status":"failed","mensaje":"No existen datos del usuario"}
            self.assertEqual(self.dato,self.respuesta)
            self.assertEqual(self.status,self.not_found)
    def test_no_existe_criterio(self):
        with app.app_context():
            self.ingreso=dict({
           "uui":"891edb58-3a56-4362-a2bb-e5a9fad22d55"
            })
            usuario=Usuarios()
            self.dato, self.status=usuario.buscar_usuario(self.ingreso,self.usuarios)
            self.respuesta={"status":"failed","mensaje":"No existe criterio"}
            self.assertEqual(self.dato,self.respuesta)
            self.assertEqual(self.status,self.not_found)