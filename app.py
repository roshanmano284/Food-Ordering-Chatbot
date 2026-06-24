
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Food Ordering Chatbot",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 AI Food Ordering Chatbot")
st.caption("Order food, ask for recommendations, and chat naturally.")

# -----------------------------
# Food Menu
# -----------------------------
food_menu = {

    "Tamil Foods": {
        "Idli": 40,
        "Dosa": 60,
        "Masala Dosa": 80,
        "Ghee Roast": 100,
        "Pongal": 70,
        "Vada": 20,
        "Poori": 60,
        "Appam": 50,
        "Paniyaram": 70,
        "Kothu Parotta": 120,
        "Wheat Parotta": 50,
        "Parotta": 40,
        "Sambar Rice": 90,
        "Curd Rice": 80,
        "Lemon Rice": 80,
        "Tamarind Rice": 80,
        "Tomato Rice": 80,
        "Veg Meals": 150,
        "Chappathi": 40
    },

    "Veg Foods": {
        "Veg Fried Rice": 140,
        "Veg Biryani": 160,
        "Paneer Butter Masala": 180,
        "Paneer Tikka": 200,
        "Mushroom Masala": 170,
        "Veg Noodles": 130,
        "Chilli Paneer": 180,
        "Gobi Manchurian": 150,
        "Aloo Paratha": 90,
        "Veg Burger": 120,
        "Veg Pizza": 220,
        "Veg Sandwich": 100,
        "Maggie" : 80
    },

    "Non-Veg Foods": {
        "Chicken Biryani": 220,
        "Mutton Biryani": 280,
        "Chicken Fried Rice": 180,
        "Chicken Noodles": 180,
        "Chicken 65": 200,
        "Chicken Tikka": 250,
        "Tandoori chicken" : 500,
        "Chicken BBQ" : 280,
        "Chicken kebab" : 190,
        "Chicken shawarma" : 120,
        "Spicy chicken" : 170,
        "Butter Chicken": 260,
        "Pepper Chicken": 240,
        "Mutton Curry": 280,
        "Mutton Chukka": 300,
        "Egg Fried Rice": 140,
        "Egg Curry": 120
    },

    "Sea Foods": {
        "Fish Fry": 220,
        "Fish Curry": 240,
        "Prawn Fry": 280,
        "Prawn Curry": 300,
        "Prawn Biryani": 320,
        "Crab Masala": 350,
        "Crab Soup": 180,
        "Squid Fry": 320,
        "Lobster Masala": 550
    },

    "Beverages": {
        "Fresh Lime Juice": 50,
        "Orange Juice": 80,
        "Mango Juice": 90,
        "Watermelon Juice": 70,
        "Pineapple Juice": 80,
        "Apple Juice": 100,
        "Milk Shake": 120,
        "Chocolate Shake": 140,
        "Strawberry Shake": 130,
        "Badam Milk": 90,
        "Elaneer Payasam Cold" : 50,
        "Grape Juice" : 70,
        "Musk Melon Juice":70,
        "ABC Juice" :120,
        "Carrot juice" : 60,

    },

    "Desserts": {
        "Gulab Jamun": 40,
        "Rasgulla": 40,
        "Jalebi": 50,
        "Kesari": 50,
        "Payasam": 60,
        "Brownie": 100,
        "Chocolate Cake": 120,
        "Black Forest Cake": 140,
        "Red velvet cake" : 160,
        "Honey cake" : 80,
        "White forest cake" : 150
    }
}

# -----------------------------
# Sidebar Menu
# -----------------------------
with st.sidebar:
    st.header("🍽 Menu")

    for category, items in food_menu.items():
        with st.expander(category):
            for item, price in items.items():
                st.write(f"{item} - ₹{price}")

# -----------------------------
# Chat Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_prompt = st.chat_input(
    "Ask for food, prices, recommendations, or place an order..."
)

if user_prompt:

    # Show user message
    st.chat_message("user").markdown(user_prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # System Prompt
    system_prompt = f"""
You are an intelligent Food Ordering Assistant.

Available Menu:
{food_menu}

Your responsibilities:
- Help customers order food.
- Recommend dishes.
- Suggest combos.
- Mention prices when asked.
- Be friendly and professional.
- Remember previous messages in the conversation.
- Respond naturally like ChatGPT.
- Use emojis occasionally.
- If food is not available, politely say it is unavailable.
"""

    # Prepare messages for Groq
    groq_messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    for msg in st.session_state.messages:
        groq_messages.append(
            {
                "role": msg["role"],
                "content": msg["content"]
            }
        )

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_messages,
            temperature=0.7,
            max_tokens=1024
        )

        answer = response.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        st.error(f"Error: {e}")
