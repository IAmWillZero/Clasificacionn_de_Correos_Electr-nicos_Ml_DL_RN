import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Implementar limpieza y tokenización aquí...
    return data['cleaned_text'], data['label']