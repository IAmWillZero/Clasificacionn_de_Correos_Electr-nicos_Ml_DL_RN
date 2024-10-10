import pandas as pd
from model import create_model

# Cargar y preprocesar datos aquí...
data = pd.read_csv('data/dataset.csv')
# Suponiendo que 'X' y 'y' son las características y etiquetas respectivamente.
X = data['text']
y = data['label']

model = create_model(input_shape=X.shape[1])
model.fit(X, y, epochs=5, batch_size=32)
model.save('spam_classifier_model.h5')