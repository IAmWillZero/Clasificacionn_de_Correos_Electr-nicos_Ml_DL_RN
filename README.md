# Clasificador de Correos Electrónicos Spam

## Resumen del Proyecto
Este proyecto utiliza una red neuronal LSTM para clasificar correos electrónicos como spam o no spam. Se basa en características del contenido del correo, como la frecuencia de palabras clave y el número de enlaces.

## Objetivo
Desarrollar un modelo que pueda identificar correos electrónicos no deseados con alta precisión, mejorando así la experiencia del usuario en el manejo del correo electrónico.

## Tecnologías Utilizadas
- Python 3.x
- TensorFlow 2.x
- Pandas
- NumPy

## Instalación
1. Clona este repositorio.
2. Navega a la carpeta del proyecto.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

   Uso
4. Para entrenar el modelo:
    ```bash
    python model/train.py

5. Para hacer predicciones:
    ```bash
    python predictions/predict.py --email "Texto del correo aquí"