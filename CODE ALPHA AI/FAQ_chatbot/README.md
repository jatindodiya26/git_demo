# FAQ Chatbot using NLP

## 📌 Project Overview

This project is an AI-based FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.
The chatbot answers user questions by comparing them with a predefined set of Frequently Asked Questions (FAQs) and returning the most relevant answer.

The system uses Natural Language Processing (NLP) techniques to understand user input and find the closest matching question.

## 🚀 Features

* Accepts user questions through a simple interface
* Uses NLP techniques for text processing
* Finds the most similar question using cosine similarity
* Returns the most relevant answer
* Simple and interactive web interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* NLTK

## ⚙️ How It Works

1. A list of FAQ questions and answers is stored in the dataset.
2. The questions are converted into numerical vectors using TF-IDF.
3. When a user asks a question, the system compares it with existing questions.
4. Cosine similarity is used to find the most similar question.
5. The chatbot returns the corresponding answer.

## 📂 Project Structure

CodeAlpha_FAQChatbot
│
├── app_chatbot.py
├── chatbot.py
├── faq_data.py
├── requirements.txt
└── README.md

## ▶️ How to Run the Project

1. Install required libraries

pip install streamlit nltk scikit-learn

2. Run the chatbot application

streamlit run app_chatbot.py

3. Open the browser and interact with the chatbot.

## 📊 Example

User Input:
What is AI?

Bot Response:
Artificial Intelligence is the simulation of human intelligence in machines.

## 🎯 Internship Task

This project is developed for **Task 2: FAQ Chatbot** under the CodeAlpha Artificial Intelligence Internship Program.

## 👨‍💻 Author

Jatin
Computer Science Engineering Student
Artificial Intelligence & Machine Learning
