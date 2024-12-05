import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import os

class RAGModel:
    def __init__(self):
        genai.configure(api_key='AIzaSyB9KhUP9GySctSAh7Ks4h87PbrSItUgHPU')
        self.model = genai.GenerativeModel('gemini-pro')
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
    
    def get_response(self, query, context):
        prompt = f"Context: {context}\nQuery: {query}\nResponse:"
        response = self.model.generate_content(prompt)
        return response.text
