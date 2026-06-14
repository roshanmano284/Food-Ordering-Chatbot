import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("🍔  Food Ordering Chatbot")

menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Sandwich": 100,
    "Coke": 50
}

st.subheader("Menu")

for item, price in menu.items():
    st.write(f"{item} - ₹{price}")

user_input = st.text_input("Ask something or place an order")

if st.button("Send"):

    prompt = f"""
    You are a Food Ordering Assistant.

    Menu:
    Pizza - ₹250
    Burger - ₹120
    Pasta - ₹180
    Sandwich - ₹100
    Coke - ₹50

    User: {user_input}

    Reply as a food ordering chatbot.
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile"
    )

    answer = response.choices[0].message.content

    st.success(answer)