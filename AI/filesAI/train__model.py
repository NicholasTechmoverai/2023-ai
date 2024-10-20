import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from data import data as dataVal
# Sample dataset creation
print(dataVal)
data = {
    'symptom1': [
        'fever', 'cough', 'headache', 'fever', 'cough', 'nausea', 'shortness of breath', 'sore throat', 
        'fatigue', 'muscle pain', 'chest pain', 'dizziness', 'runny nose', 'sneezing', 'chills', 
        'stomach pain', 'diarrhea', 'vomiting', 'joint pain', 'itchy skin', 'swelling', 'rash', 
        'loss of appetite', 'weight loss', 'night sweats', 'abdominal pain', 'dry cough', 'shortness of breath', 
        'persistent cough', 'drowsiness', 'confusion', 'blurry vision', 'sweating', 'dry skin', 
        'joint stiffness', 'hearing loss', 'nosebleeds', 'hair loss', 'muscle weakness', 'sore muscles', 
        'difficulty swallowing', 'painful urination', 'frequent urination', 'heavy bleeding', 'irregular periods',
        'itchy eyes', 'nasal congestion', 'chest tightness', 'wheezing', 'back pain'
    ],
    'symptom2': [
        'cough', 'sore throat', 'nausea', 'headache', 'shortness of breath', 'shortness of breath', 
        'cough', 'fatigue', 'muscle pain', 'chest pain', 'dizziness', 'runny nose', 'sneezing', 
        'chills', 'stomach pain', 'diarrhea', 'vomiting', 'joint pain', 'itchy skin', 'swelling', 
        'rash', 'loss of appetite', 'weight loss', 'night sweats', 'nausea', 'persistent cough', 
        'drowsiness', 'confusion', 'blurry vision', 'sweating', 'dry skin', 'joint stiffness', 
        'hearing loss', 'nosebleeds', 'hair loss', 'muscle weakness', 'painful urination', 'frequent urination', 
        'heavy bleeding', 'irregular periods', 'abdominal bloating', 'sore throat', 'headache', 
        'runny nose', 'shortness of breath', 'back pain', 'drowsiness', 'fever', 'sweating','NONE'
    ],
    'disease': [
        'flu', 'cold', 'migraine', 'flu', 'asthma', 'asthma', 'flu', 'cold', 'flu', 'arthritis',
        'heart disease', 'vertigo', 'allergy', 'allergy', 'flu', 'gastroenteritis', 'gastroenteritis', 
        'gastroenteritis', 'arthritis', 'eczema', 'heart disease', 'psoriasis', 'anorexia', 'cancer', 
        'tuberculosis', 'bronchitis', 'pneumonia', 'chronic fatigue syndrome', 'diabetes', 'hypertension', 
        'glaucoma', 'osteoporosis', 'hearing loss', 'lupus', 'eczema', 'cystitis', 'kidney infection', 
        'endometriosis', 'fibroids', 'prostatitis', 'peptic ulcer', 'menstrual irregularities', 
        'allergy', 'sinusitis', 'muscle strain', 'asthma', 'flu', 'chronic bronchitis', 'insomnia', 
        'sinusitis'
    ],
    'cause': [
        'virus', 'bacteria', 'stress', 'virus', 'allergy', 'allergy', 'virus', 'bacteria', 'virus', 
        'autoimmune', 'heart condition', 'inner ear issue', 'allergen', 'allergen', 'virus', 
        'virus', 'virus', 'virus', 'autoimmune', 'allergen', 'heart condition', 'autoimmune', 
        'malnutrition', 'cancer', 'bacteria', 'virus', 'bacteria', 'autoimmune', 'metabolic', 
        'genetic', 'age-related', 'infection', 'autoimmune', 'infection', 'bacterial', 'infection', 
        'hormonal', 'genetic', 'infection', 'hormonal', 'bacterial', 'hormonal', 'bacterial', 
        'allergen', 'bacterial', 'viral', 'stress', 'allergy', 'bacterial', 'autoimmune'
    ],
    'prevention': [
        'rest and fluids', 'rest and hydration', 'stress management', 'rest and fluids', 'avoid allergens',
        'avoid allergens', 'rest and hydration', 'rest and fluids', 'rest and fluids', 'manage stress',
        'monitor heart health', 'balance diet', 'avoid allergens', 'avoid allergens', 'rest and fluids',
        'stay hydrated', 'avoid contaminated food', 'avoid contaminated food', 'manage joint health',
        'avoid allergens', 'monitor heart health', 'moisturize skin', 'eat balanced diet', 'get regular check-ups',
        'avoid smoking', 'get vaccinated', 'avoid stress', 'control blood sugar', 'monitor blood pressure',
        'regular eye exams', 'bone density tests', 'hearing tests', 'avoid allergens', 'avoid irritants',
        'increase hydration', 'practice good hygiene', 'manage menstrual health', 'reduce stress', 'consult a doctor',
        'allergy medication', 'nasal irrigation', 'exercise regularly', 'avoid cold environments', 'pain relief', 
        'allergy testing', 'avoid spicy food', 'avoid excessive caffeine', 'take breaks', 'eat balanced meals',
        'regular check-ups'
    ]
}
df = pd.DataFrame(dataVal)

# Aggregate cause and prevention fields if there are duplicate diseases
df_agg = df.groupby('disease').agg({
    'cause': lambda x: ', '.join(set(x)),  # Combine all causes into a comma-separated string
    'prevention': lambda x: ', '.join(set(x))  # Combine all preventions into a comma-separated string
}).reset_index()

# Prepare the features and labels
X = df[['symptom1', 'symptom2']]
y_disease = df['disease']

# Vectorize the symptoms
vectorizer = CountVectorizer()
X_transformed = vectorizer.fit_transform(X['symptom1'] + ' ' + X['symptom2'])

# Encode labels
label_encoder_disease = LabelEncoder()
y_disease_encoded = label_encoder_disease.fit_transform(y_disease)

# Create mapping from disease to cause and prevention
disease_to_info = df_agg.set_index('disease').to_dict(orient='index')

# Save disease information mapping
joblib.dump(disease_to_info, 'disease_to_info.pkl')

# Split the data
X_train, X_test, y_disease_train, y_disease_test = train_test_split(
    X_transformed, y_disease_encoded, test_size=0.2, random_state=42
)

# Convert to TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((X_train.toarray(), y_disease_train))
test_dataset = tf.data.Dataset.from_tensor_slices((X_test.toarray(), y_disease_test))

# Define the model
def create_model(input_shape, num_classes):
    input_layer = tf.keras.layers.Input(shape=(input_shape,))
    
    x = tf.keras.layers.Dense(128, activation='relu')(input_layer)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    
    disease_output = tf.keras.layers.Dense(num_classes, activation='softmax')(x)
    
    model = tf.keras.models.Model(inputs=input_layer, outputs=disease_output)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

model = create_model(X_transformed.shape[1], len(label_encoder_disease.classes_))

# Train the model
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
history = model.fit(
    train_dataset.batch(32),
    epochs=20,
    validation_data=test_dataset.batch(32),
    callbacks=[early_stopping]
)

# Save the model and vectorizers
model.save('symptoms_disease_model.keras')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(label_encoder_disease, 'label_encoder_disease.pkl')

print("Model and vectorizers saved successfully.")
