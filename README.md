# Prueba técnica Desarrollador Backend

Pablo Ruz Donoso - marzo 2022 
([Más proyectos](https://gitlab.com/PabloRzDn))

---
*Índice:*

- Preámbulo
- Instalación
- Glosario
- Código de status
- Ingresar Usuario
- Buscar Usuario
- Editar Usuario
- Eliminar Usuario


---
### Preámbulo

La **API REST** almacenada en este repositorio fue diseñada con el objeto de registrar, actualizar, consultar y eliminar usuarios. La estructura de los usuarios corresponde a un id autogenerado a partir de UUID, el nombre, apellido, email y fecha de nacimiento de los usuarios.

Para su utilización se deben utilizar los UUID de cada usuario, u otros datos alternativos, dependiendo de la acción a realizar.

Como nota, se destaca que la aplicación está diseñada para montarse en un servidor local, en este sentido, el endpoint es `127.0.0.1:5000/api`



### Instalación

La aplicación fue desarrollada utilizando el framework Flask de Python y tiene la siguiente estructura:

```
/prueba_tecnica
./app
..__init__.py
..models.py
..views.py
models.log
test_models.py
requirements.txt
run.py

```

Se sugiere crear un entorno virtual para la ejecución de este programa. Para esto, a nivel del directorio principal, ejecutar:

```bash
$ virtualenv venv --python=python3.9
```

Una vez creado el entorno virtual, se debe activar:

GNU/Linux
```bash
$ source venv/bin/activate
```

Windows (Git Bash)
```bash
$ source venv/Scripts/activate
```
Para instalar los requerimientos, se debe ejecutar recursivamente el gestor de instalación pip:

```bash
$ pip install -r requirements.txt

```

Luego, y con propósitos de desarrollo, se asignan las siguientes variables globales:
```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development

```

Finalmente, para correr la aplicación:

```bash
$ flask run
```

```bash
 * Serving Flask app 'run.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Debugger is active!
 * Debugger PIN: 374-775-618
```

#### Opcional: Dockerfile

La aplicación puede montarse también en una imagen Docker. Para esto, situarse en el directorio principal:

**Montar imagen**
```bash
$ docker build -t prueba-tecnica .
```
**Correr Imagen**
```bash
$ docker run -p 5000:5000 prueba-tecnica
```

**Entrar a la aplicación**

Puede entrar a la aplicación en el host y puerto configurado en la imagen.


### Glosario

Los conceptos utilizados y el tipo de datos que recibe la API REST son:

- `uuid`: identificador del usuario. Se genera automáticamente al crear un usuario, y sirve como criterio de búsqueda del mismo. 
- `nombre`: corresponde al primer nombre del usuario. Se debe ingresas con la primera letra en mayúsculas. Si bien la API soporta el ingreso entre mayúsculas y minúsculas, esto se considera una mala práctica.
- `apellido`: corresponde al primer apellido del usuario. Cumple los mismos criterios que el nombre.
- `email`: corresponde al correo electrónico del usuario. La API valida el ingreso del usuario a partir de la existencia de carácteres al lado izquierdo del *@*, y dominios con caractéres al lado izquierdo y derecho del punto.
- `fecha_nacimiento`: es la fecha de nacimiento del usuario. El formato es *YYYY-MM-DD*.

### Código de status

Los códigos de status son los siguientes:

- `200` Se ha encontrado el recurso o la insersión de datos ha sido satisfactoria.
- `400` El recurso ha sido consultado de forma incorrecta.
- `404` No existe el recurso consultado.

### Ingresar usuario

`/api/registro`

Este recurso permite ingresar un usuario, generando un uuid.

**Ejemplo de Consultas**

Request

```
POST: 127.0.0.1:5000/api/registro
```

```json
{
        "nombre": "Raul",
        "apellido": "Zurita",
        "email": "zuriuta@gmail.com",
        "fecha_nacimiento": "1940-12-21"  
    }
```


Respuesta

```
Status 200 OK
```

```json
{
    "apellido": "Zurita",
    "email": "zuriuta@gmail.com",
    "fecha_nacimiento": "1940-12-21",
    "nombre": "Raul",
    "uuid": "34cce5fc-de76-4b7a-83e2-674d3a142027"
}
```

Request

```
POST: 127.0.0.1:5000/api/registro
```

```json
{
        "nombre": "Raul",
        "apellido": "Zurita",
        "email": "zuriuta@gmail.com",
        "fecha_nacimiento": "190-12-21" *fecha incorrecta  
    }
```

Respuesta

```
Status 400 BAD REQUEST
```

```json
{
    
    "mensaje": "Fecha nacimiento incorrecta. intente: YYYY-MM-DD",
    "status": "failed"
}
```

Request

```
POST: 127.0.0.1:5000/api/registro
```

```json
{
        "nombre": "Raul",
        "apellido": "Zurita",
        "email": "zuriuta@gmail.com",
        * faltan datos
    }
```

Respuesta

```
Status 400 BAD REQUEST
```

```
POST: 127.0.0.1:5000/api/registro
```

```json
{
        "nombre": "Raul",
        "apellido": "Zurita",
        "email": "zuriuta@gmail.com", *El mail existe
        "fecha_nacimiento": "1940-12-21"   
    }
```

Respuesta

```
Status 400 BAD REQUEST
```

```json
{
    "mensaje": "usuario ya existe",
    "status": "failed"
}
```
### Buscar Usuario


`/api/buscar`

Este recurso permite buscar un usuario a través de un uuid. Asimismo, también permite la búsqueda a partir de otros criterios. 

Request

`
POST: 127.0.0.1:5000/api/buscar
`


```json
{
    "uuid": "f3660117-164c-4c4a-9056-655cc1fef55f"
}
```


Respuesta

```
Status 200 OK
```

```json
{
    "apellido": "Zurita",
    "email": "zuriuta@gmail.com",
    "fecha_nacimiento": "1940-11-13",
    "nombre": "Raul",
    "uuid": "f3660117-164c-4c4a-9056-655cc1fef55f"
}

```

Request

```
POST: 127.0.0.1:5000/api/buscar
```

```json
{
    "uuid": "incorrecto" *no existe uuid
}
```

Respuesta

```
Status 404 NOT FOUND
```

```json
{
    "mensaje": "No existen datos del usuario",
    "status": "failed"
}
```

### Editar Usuario

Request

```
127.0.0.1:5000/api/editar
```

```
{
    "uuid":"b6b62c5b-0ad7-481b-9fac-6b1a88b69043",
    "usuario":{
        "nombre":"raul",
        "apellido":"zurita",
        "email":"raul@gmail.cl",
        "fecha_nacimiento":"1999-08-30"

    }

}
```

Respuesta

```
Status 200 OK
```

```json
 {
        "apellido": "zurita",
        "email": "raul@gmail.cl",
        "fecha_nacimiento": "1999-08-30",
        "nombre": "raul",
        "uuid": "b6b62c5b-0ad7-481b-9fac-6b1a88b69043"
    }
```

### Eliminar Usuario
`/api/eliminar`

```json
 {
        "apellido": "zurita",
        "email": "raul@gmail.cl",
        "fecha_nacimiento": "1999-08-30",
        "nombre": "raul",
        "uuid": "b6b62c5b-0ad7-481b-9fac-6b1a88b69043"
    }
```

Respuesta

```
Status 200 OK
```