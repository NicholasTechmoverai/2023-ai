import pandas as pd

data = pd.DataFrame({
    'symptom1': [
        'fever', 'cough', 'headache', 'fever', 'cough', 'nausea', 'shortness of breath', 
        'sore throat', 'fatigue', 'muscle pain', 'chest pain', 'dizziness', 'runny nose', 
        'sneezing', 'chills', 'stomach pain', 'diarrhea', 'vomiting', 'joint pain', 'itchy skin', 
        'swelling', 'rash', 'loss of appetite', 'weight loss', 'night sweats', 'abdominal pain', 
        'dry cough', 'shortness of breath', 'persistent cough', 'drowsiness', 'confusion', 
        'blurry vision', 'sweating', 'dry skin', 'joint stiffness', 'hearing loss', 'nosebleeds', 
        'hair loss', 'muscle weakness', 'sore muscles', 'difficulty swallowing', 'painful urination', 
        'frequent urination', 'heavy bleeding', 'irregular periods', 'itchy eyes', 'nasal congestion', 
        'chest tightness', 'wheezing', 'back pain'
    ],
    'symptom2': [
        'cough', 'sore throat', 'nausea', 'headache', 'shortness of breath', 'shortness of breath', 
        'cough', 'fatigue', 'muscle pain', 'chest pain', 'dizziness', 'runny nose', 'sneezing', 
        'chills', 'stomach pain', 'diarrhea', 'vomiting', 'joint pain', 'itchy skin', 'swelling', 
        'rash', 'loss of appetite', 'weight loss', 'night sweats', 'nausea', 'persistent cough', 
        'drowsiness', 'confusion', 'blurry vision', 'sweating', 'dry skin', 'joint stiffness', 
        'hearing loss', 'nosebleeds', 'hair loss', 'muscle weakness', 'painful urination', 
        'frequent urination', 'heavy bleeding', 'irregular periods', 'abdominal bloating', 
        'sore throat', 'headache', 'runny nose', 'shortness of breath', 'back pain', 
        'drowsiness', 'fever', 'sweating', 'NONE'
    ],
    'disease': [
        'flu', 'cold', 'migraine', 'flu', 'asthma', 'asthma', 'flu', 'cold', 'flu', 'arthritis',
        'heart disease', 'vertigo', 'allergy', 'allergy', 'flu', 'gastroenteritis', 'gastroenteritis', 
        'gastroenteritis', 'arthritis', 'eczema', 'heart disease', 'psoriasis', 'anorexia', 'cancer', 
        'tuberculosis', 'bronchitis', 'pneumonia', 'chronic fatigue syndrome', 'diabetes', 
        'hypertension', 'glaucoma', 'osteoporosis', 'hearing loss', 'lupus', 'eczema', 'cystitis', 
        'kidney infection', 'endometriosis', 'fibroids', 'prostatitis', 'peptic ulcer', 
        'menstrual irregularities', 'allergy', 'sinusitis', 'muscle strain', 'asthma', 'flu', 
        'chronic bronchitis', 'insomnia', 'sinusitis'
    ],
    'cause': [
        'virus', 'bacteria', 'stress', 'virus', 'allergy', 'allergy', 'virus', 'bacteria', 
        'virus', 'autoimmune', 'heart condition', 'inner ear issue', 'allergen', 'allergen', 
        'virus', 'virus', 'virus', 'virus', 'autoimmune', 'allergen', 'heart condition', 
        'autoimmune', 'malnutrition', 'cancer', 'bacteria', 'virus', 'bacteria', 'autoimmune', 
        'metabolic', 'genetic', 'age-related', 'infection', 'autoimmune', 'infection', 'bacterial', 
        'infection', 'hormonal', 'genetic', 'infection', 'hormonal', 'bacterial', 'hormonal', 
        'bacterial', 'allergen', 'bacterial', 'viral', 'stress', 'allergy', 'bacterial', 
        'autoimmune'
    ],
    'prevention': [
        'rest and fluids', 'rest and hydration', 'stress management', 'rest and fluids', 
        'avoid allergens', 'avoid allergens', 'rest and hydration', 'rest and fluids', 
        'rest and fluids', 'manage stress', 'monitor heart health', 'balance diet', 
        'avoid allergens', 'avoid allergens', 'rest and fluids', 'stay hydrated', 
        'avoid contaminated food', 'avoid contaminated food', 'manage joint health', 
        'avoid allergens', 'monitor heart health', 'moisturize skin', 'eat balanced diet', 
        'get regular check-ups', 'avoid smoking', 'get vaccinated', 'avoid stress', 
        'control blood sugar', 'monitor blood pressure', 'regular eye exams', 'bone density tests', 
        'hearing tests', 'avoid allergens', 'avoid irritants', 'increase hydration', 
        'practice good hygiene', 'manage menstrual health', 'reduce stress', 'consult a doctor', 
        'allergy medication', 'nasal irrigation', 'exercise regularly', 'avoid cold environments', 
        'pain relief', 'allergy testing', 'avoid spicy food', 'avoid excessive caffeine', 
        'take breaks', 'eat balanced meals', 'regular check-ups'
    ]
})

print(data)


matched_data = data[
    (data['symptom1'] == data['symptom2']) &
    (data['symptom2'] == data['disease']) &
    (data['disease'] == data['cause']) &
    (data['cause'] == data['prevention'])
]

# Printing the lengths of the columns
print(len(data['symptom1']))  # Should print 50
print(len(data['symptom2']))  # Should print 50
print(len(data['disease']))  # Should print 50
print(len(data['cause']))  # Should print 50
print(len(data['prevention'])) 