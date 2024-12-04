# Proyecto desplegado en:

[Despliegue en vivo](URL)

# Ejecucion en entorno de desarrollo

## NOTA: Se debe tener instalado mysql

## Ejecutar la creacion de base de datos y tablas correspondientes a la AppWeb

Navegue al directorio donde esta el archivo init.sql

``````
mysql -u <SuUsuario> -p < init.sql
``````

## Ejecutar la aplicacion web en windows

``````
$env:FLASK_APP="run.py"
$env:FLASK_ENV="development"
python -m flask run --host=0.0.0.0
``````

## Ejecutar la aplicacion web en linux:

``````
export FLASK_APP=run.py
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0
``````