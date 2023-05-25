#Finanacial Advisory Chatbot

import json
import numpy as np
import pandas as pd
import openai

openai.api_key = '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'  # Replace with your OpenAI API key


data_str = '[{ "date": "2021-01-01", "amount": 1000, "category": "income", "description": "salary" }, { "date": "2021-01-02", "amount": -50, "category": "groceries", "description": "milk and eggs" }, { "date": "2021-01-03", "amount": -100, "category": "entertainment", "description": "movie tickets" }, { "date": "2021-01-04", "amount": -20, "category": "transportation", "description": "bus fare" }, { "date": "2021-01-05", "amount": -200, "category": "bills", "description": "electricity bill" }, { "date": "2021-01-06", "amount": -30, "category": "groceries", "description": "bread and cheese" }, { "date": "2021-01-07", "amount": -150, "category": "clothing", "description": "new shoes" }, { "date": "2021-01-08", "amount": -40, "category": "healthcare", "description": "prescription drugs" }, { "date": "2021-01-09", "amount": -80, "category": "education", "description": "online course" }, { "date": "2021-01-10", "amount": -60, "category": "entertainment", "description": "pizza delivery" }, { "date": "2021-01-11", "amount": -25, "category": "transportation", "description": "taxi ride" }, { "date": "2021-01-12", "amount": -300, "category": "bills", "description": "internet bill" }, { "date": "2021-01-13", "amount": -50, "category": "groceries", "description": "fruits and vegetables" }]'

# Replace smart quotes with regular quotes
data_str = data_str.replace("“", "\"").replace("”", "\"")

# Load the data as a Python list
data = json.loads(data_str)


def load_transaction_data(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return pd.DataFrame(data)

file_path = 'financial_data.json'  # Replace with your JSON file path
transactions = load_transaction_data(file_path)

def process_user_query(query, transactions):
    # Define the conversation history as input to ChatGPT
    conversation = [
        {"role": "system", "content": "You are a user seeking financial advice."},
        {"role": "user", "content": query}
    ]

    # Generate a response from ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=2000,
        temperature=0.7,
        n=1,
        stop=None
    )

    return response.choices[0].message.content.strip()

print('Personal Advisory Chatbot')
print('-------------------------')
print('Chatbot is ready. Ask your questions!')

while True:
    # Get user input
    user_input = input('User: ') + 'answer this question based on this data:-[ { “date”: “2021-01-01”, “amount”: 1000, “category”: “income”, “description”: “salary” }, { “date”: “2021-01-02”, “amount”: -50, “category”: “groceries”, “description”: “milk and eggs” }, { “date”: “2021-01-03”, “amount”: -100, “category”: “entertainment”, “description”: “movie tickets” }, { “date”: “2021-01-04”, “amount”: -20, “category”: “transportation”, “description”: “bus fare” }, { “date”: “2021-01-05”, “amount”: -200, “category”: “bills”, “description”: “electricity bill” }, { “date”: “2021-01-06”, “amount”: -30, “category”: “groceries”, “description”: “bread and cheese” }, { “date”: “2021-01-07”, “amount”: -150, “category”: “clothing”, “description”: “new shoes” }, { “date”: “2021-01-08”, “amount”: -40, “category”: “healthcare”, “description”: “prescription drugs” }, { “date”: “2021-01-09”, “amount”: -80, “category”: “education”, “description”: “online course” }, { “date”: “2021-01-10”, “amount”: -60, “category”: “entertainment”, “description”: “pizza delivery” }, {“date”: “2021-01-11”, “amount”: -25, “category”: “transportation”, “description”: “taxi ride” }, { “date”: “2021-01-12”, “amount”: -300, “category”:“bills”, “description”:“internet bill” }, { “date”:“2021-01-13”, “amount”:-50, “category”:“groceries”, “description”:“fruits and vegetables” } ]'

    # Process user input and generate response
    response = process_user_query(user_input, transactions)

    print('Chatbot:', response)
