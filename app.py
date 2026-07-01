import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Food Ordering Assistant",
    page_icon="🍔",
    layout="wide"
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
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
        "Tomato Rice": 80,
        "Veg Meals": 150,
        "Chapathi": 40
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
        "Maggie": 80
    },

    "Non-Veg Foods": {
        "Chicken Biryani": 220,
        "Mutton Biryani": 280,
        "Chicken Fried Rice": 180,
        "Chicken Noodles": 180,
        "Chicken 65": 200,
        "Chicken Tikka": 250,
        "Tandoori Chicken": 500,
        "Chicken BBQ": 280,
        "Chicken Kebab": 190,
        "Chicken Shawarma": 120,
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
        "Grape Juice": 70,
        "ABC Juice": 120,
        "Carrot Juice": 60
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
        "Red Velvet Cake": 160,
        "Honey Cake": 80,
        "White Forest Cake": 150
    }
}

# KPI CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🍽 Menu Categories", len(food_menu))

with col2:
    st.metric("⭐ Rating", "4.9")

with col3:
    st.metric("🚚 Delivery", "30 Min")

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Food Ordering Assistant",
    page_icon="🍔",
    layout="wide"
)

st.markdown("""
<style>

/* ---------------- BACKGROUND ---------------- */

.stApp{
    background: linear-gradient(135deg,#1a0000,#3b0000,#660000,#8B0000);
    color:white;
}

/* Hide Streamlit Header */
header{
    visibility:hidden;
}

/* ---------------- HERO ---------------- */

.hero{
    text-align:center;
    padding:40px;
}

.hero h1{
    font-size:58px;
    font-weight:800;
    color:white;
}

.hero p{
    font-size:22px;
    color:#FFE5E5;
}

/* ---------------- SIDEBAR ---------------- */

[data-testid="stSidebar"]{
    background:#1a0000;
    border-right:2px solid #ff4d4d;
}

/* ---------------- METRIC CARDS ---------------- */

[data-testid="metric-container"]{
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:18px;
    padding:18px;
    backdrop-filter:blur(12px);
    box-shadow:0px 8px 20px rgba(0,0,0,.35);
}

/* ---------------- SELECT BOX ---------------- */

.stSelectbox > div > div{
    background:#2b0000;
    color:white;
    border-radius:12px;
    border:1px solid #ff4d4d;
}

/* ---------------- FOOD CARDS ---------------- */

.food-card{

    background:rgba(255,255,255,0.08);

    border-radius:18px;

    padding:18px;

    margin-bottom:18px;

    border:1px solid rgba(255,255,255,.1);

    box-shadow:0 8px 25px rgba(0,0,0,.35);

    transition:0.3s;

}

.food-card:hover{

    transform:translateY(-5px);

    border:1px solid #ff4d4d;

    box-shadow:0 0 20px rgba(255,77,77,.5);

}

/* ---------------- BUTTONS ---------------- */

.stButton>button{

    background:linear-gradient(90deg,#ff1a1a,#cc0000);

    color:white;

    border:none;

    border-radius:12px;

    font-weight:bold;

    height:45px;

    transition:0.3s;

}

.stButton>button:hover{

    background:linear-gradient(90deg,#ff3333,#990000);

    transform:scale(1.04);

}

/* ---------------- CHAT ---------------- */

[data-testid="stChatMessage"]{

    background:rgba(255,255,255,.08);

    border-radius:16px;

    border:1px solid rgba(255,255,255,.1);

    padding:15px;

}

/* ---------------- CHAT INPUT ---------------- */

[data-testid="stChatInput"]{

    background:#2b0000;

    border-radius:15px;

}

/* ---------------- TEXT ---------------- */

h1,h2,h3,h4,h5,h6{
    color:white;
}

p,label,span{
    color:#FFE5E5;
}

/* ---------------- SUCCESS ---------------- */

.stSuccess{
    background:#14532d;
    color:white;
    border-radius:10px;
}

/* ---------------- INFO ---------------- */

.stInfo{
    background:#450a0a;
    color:white;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero">
<h1>🍔 AI Food Ordering Assistant</h1>
<p>Order Food • Get Recommendations • Chat Naturally</p>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# SIDEBAR CART
# -----------------------------
with st.sidebar:

    st.title("🛒 My Cart")

    total = 0

    if len(st.session_state.cart) == 0:
        st.info("Cart Empty")

    for item in st.session_state.cart:

        st.write("✅", item)

        for category in food_menu:
            if item in food_menu[category]:
                total += food_menu[category][item]

    st.markdown("---")
    st.subheader(f"💰 Total: ₹{total}")

    if st.button("Place Order"):
        st.success("🎉 Order Placed Successfully!")

 # -----------------------------
# MENU CATEGORIES
# -----------------------------
st.markdown("## 🍽 Browse Menu")

selected_category = st.selectbox(
    "Choose Food Category",
    list(food_menu.keys())
)       

st.subheader(f"🍴 {selected_category}")

for item, price in food_menu[selected_category].items():

    col1, col2, col3 = st.columns([4,1,1])

    with col1:
        st.write(item)

    with col2:
        st.write(f"₹{price}")

    with col3:
        if st.button("➕", key=item):
            st.session_state.cart.append(item)


# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# CHATBOT
# -----------------------------
user_prompt = st.chat_input(
    "Ask for food, prices, recommendations, or place an order..."
)

if user_prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # -----------------------------
    # HANDLE ORDER CONFIRMATION
    # -----------------------------
    order_keywords = [
        "place order",
        "order now",
        "confirm order",
        "checkout",
        "my order is placed",
        "order placed"
    ]

    if any(word in user_prompt.lower() for word in order_keywords):

        if len(st.session_state.cart) == 0:

            answer = """
❌ Your cart is empty.

Please add some food before placing your order.
"""

        else:

            total = 0

            order_list = ""

            for item in st.session_state.cart:

                order_list += f"✅ {item}\n"

                for category in food_menu:
                    if item in food_menu[category]:
                        total += food_menu[category][item]

            answer = f"""
# 🎉 Order Confirmed

Your order has been placed successfully!

## 🛒 Ordered Items

{order_list}

### 💰 Total Amount: ₹{total}

🚚 Estimated Delivery: **30 Minutes**

Thank you for choosing **AI Food Ordering Assistant** ❤️
"""

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.stop()

    # -----------------------------
    # CURRENT CART
    # -----------------------------
    if len(st.session_state.cart) == 0:
        cart_text = "Cart is empty."
    else:
        cart_text = ", ".join(st.session_state.cart)

    # -----------------------------
    # SYSTEM PROMPT
    # -----------------------------
    system_prompt = f"""
You are an intelligent Food Ordering Assistant.

Available Menu:

{food_menu}

Current Cart:

{cart_text}

Rules:

- Recommend foods.
- Tell prices.
- Suggest combos.
- If the user asks about their cart, use the Current Cart.
- Never say the cart is empty if Current Cart has items.
- If user asks food recommendations, answer naturally.
- Use emojis occasionally.
"""

    groq_messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    for msg in st.session_state.messages:
        groq_messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

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

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(f"Error: {e}")
