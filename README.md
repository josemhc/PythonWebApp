# NOTA: Se debe tener instalado mysql

# Ejecutar la aplicacion web en windows

$env:FLASK_APP="run.py"
$env:FLASK_ENV="development"
python -m flask run --host=0.0.0.0

# Ejecutar la aplicacion web en linux:

export FLASK_APP=run.py
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0