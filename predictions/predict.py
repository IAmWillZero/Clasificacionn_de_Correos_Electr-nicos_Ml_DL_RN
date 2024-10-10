import tensorflow as tf

def predict(email_text):
    model = tf.keras.models.load_model('spam_classifier_model.h5')
    # Preprocesar email_text aquí...
    prediction = model.predict([email_text])
    return "Spam" if prediction[0] > 0.5 else "No Spam"

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Predict if an email is spam or not.')
    parser.add_argument('--email', type=str, required=True)
    args = parser.parse_args()
    
    result = predict(args.email)
    print(f'The email is classified as: {result}')