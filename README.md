# fusa-tokyo
Notebooks Jupyter para clasificación automática de audios

## Instalación
Crear un entorno virtual y activarlo:
```
virtualenv fusa-tokyo
source fusa-tokyo/bin/activate
```

Luego, instalar las librerías requeridas:
```
pip install -r requirements.txt
```

Agregar kernel de entorno virtual a jupyter notebook
```
python -m ipykernel install --user --name fusa-tokyo --display-name fusa-tokyo
```

## Ejecución
```
jupyter notebook utilities/Testing torch-serve FuSA.ipynb
```
