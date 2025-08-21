# POO_with_python
distintos ejercicios para practicar POO en python

## Comandos que te ayudaran en pythoN

#### Entorno virtual 
- Creación de entorno
```
python -m venv nombre_entorno (por convencion se usa venv)
python -m venv venv
```

- Activar entorno (cmd)

``` venv\Scripts\activate```

Con el entorno activado puedes instalar todas las dependencias que se utilizaran unicamente en ese proyecto

- Desactivar entorno

```deactivate```

#### Dependencias
- Guardar dependencias en un archivo

```
pip freeze > nombre_archivo.txt (por convencion el nombre del archivo es requirements
python -m pip freeze > nombre_archivo.txt    (en un entorno)
```

- Instalar dependencias

```
pip install -r requeriments.txt    (desde un archivo)
pip install dependencia==version   (==version) se utiliza solo si se desea instalar una version especifica ej. flask==4.1
python -m pip install dependencia==version  (dentro de un entorno)
```
