from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faq_data import faq

questions = list(faq.keys())
answers = list(faq.values())

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(questions)

def get_response(user_question):
    
    user_vec = vectorizer.transform([user_question])
    
    similarity = cosine_similarity(user_vec, X)
    
    index = similarity.argmax()
    
    return answers[index]