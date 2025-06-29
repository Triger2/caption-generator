import streamlit as st
import random

st.markdown("### 🪙 Sponsored: Earn Crypto")
st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <iframe data-aa='2400660' src='//ad.a-ads.com/2400660?size=300x250' style='width:300px; height:250px; border:0px; padding:0; overflow:hidden; background-color: transparent;'></iframe>
</div>
""", unsafe_allow_html=True)


# --- Caption Vault ---
mood_captions = {
    "Romantic": [
        "You + Me = ❤️", "I fell for you like gravity 💫", "Love is my favorite caption.",
        "Every love story is beautiful, but ours is my favorite 💕", "You stole my heart, but I’ll let you keep it 😘",
        "With you, every moment is magic ✨", "Hold my hand and my heart forever 🫶", "Kisses are the words when words can't express love 💋"
    ],
    "Savage": [
        "Too glam to give a damn 😎", "Born to express, not to impress 🔥", "Proof I do selfies better than you.",
        "Mirror: you look amazing. Me: I know 😏", "I’m not mean, I’m just brutally honest 🧠",
        "I don’t chase, I attract 💅", "Wanna be me? Keep dreaming 💀", "Silence is the best reply to a fool 🧊"
    ],
    "Funny": [
        "Followed my heart… it led to the fridge 🧀", "Sassy, classy, and smart-assy 😏", "404: Caption not found.",
        "I'm not lazy, I’m on energy-saving mode 🛋️", "If Monday had a face, I’d punch it 💢",
        "Why fall in love when you can fall asleep? 😴", "I speak fluent sarcasm 💬", "Running on coffee and dry humor ☕"
    ],
    "Anime": [
        "Vibin’ like Luffy on a meat break 🍖", "Eyes sharper than Levi’s blade ⚔️", "I’m the main character ✨",
        "Senpai noticed me and life is complete 💞", "My power level? Off the charts 💥", "Nani?! I look this good?? 😳",
        "I protect those I love — like a true shonen hero 🛡️", "Just waiting for my arc to peak 📈"
    ],
    "Sad Boi": [
        "I’m fine — just tired of everything. 🖤", "Crying in silence hits different.", "Even shadows leave me in the dark.",
        "Smiling, but shattered inside.", "Heart heavy, soul tired.", "Sometimes silence screams the loudest.",
        "Not okay, just pretending.", "Rain hides my tears better than people do 🌧️"
    ],
    "Boss Mode": [
        "Built myself from scratch 💪", "Money talks, I don't interrupt 💸", "Focus: Me, myself, and millions 🧠",
        "No breaks. Just breakthroughs.", "Success looks good on me 😤", "Not lucky, just relentless 😎",
        "Rise. Grind. Repeat.", "Zero excuses, only executions."
    ],
    "Nerdy": [
        "function love(you): return forever 💻", "404: Emotions not found.", "Fueled by caffeine and code ☕",
        "I turn coffee into logic ☕➡️🧠", "Binary love: 1 for you, 0 for everyone else 💕", "Talk nerdy to me 😏",
        "Error: Too intelligent for small talk 🧠", "You had me at 'import numpy as np'"
    ],
    "Flirty": [
        "Are you Cu-Te? Because you're blowing my circuits 😘", "Hey cutie, got a map? I’m lost in your eyes 💋",
        "I must be WiFi ‘cause I'm feeling a strong connection 😏", "Do you believe in love at first swipe? 😍",
        "Flirt mode: activated 🔥", "I like you more than free WiFi 📶", "You bring the fire, I’ll bring the spark 💫",
        "Warning: I bite 😈"
    ],
    "Aesthetic": [
        "Moonlit thoughts & cold coffee nights ☕🌙", "Pastel skies and pixel hearts ✨", "Caught between dreams and reality 🌌",
        "Wanderer with a vintage soul 🌸", "Silhouettes under starlight ✨", "Peaceful chaos in motion 🌊",
        "Muted tones, loud thoughts 🎧", "Soft souls need harder armor 🧷"
    ]
}

# --- Topic-based Generator ---
def generate_topic_caption(topic):
    lines = [
        f"{topic.capitalize()} is not just a word, it’s a whole vibe 💫",
        f"Feeling the {topic} energy today 🔥",
        f"Keep calm and love {topic} 😎",
        f"If life had a soundtrack, it’d be called {topic} 🎵",
        f"I don’t chase, I attract — even {topic} comes to me 💋"
    ]
    return random.choice(lines)

# --- Streamlit UI ---
st.set_page_config(page_title="Insta Caption Generator", layout="centered")

# 🔥 Title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🔥 Insta Caption Generator 🔥</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'>Get the perfect caption for every mood or moment!</div>", unsafe_allow_html=True)
st.markdown(" ")

# 🎭 Mood Section
st.markdown("### 🎭 Pick a Mood")
mood = st.selectbox("Choose a mood:", list(mood_captions.keys()))
if st.button("🎉 Generate Mood Caption"):
    mood_caption = random.choice(mood_captions[mood])
    st.success(mood_caption)
    st.code(mood_caption)
    try:
        st.button("📋 Copy", on_click=st.experimental_copy, args=(mood_caption,))
    except:
        st.warning("Update Streamlit to latest version to use the copy feature 💻")

st.markdown(" ")

# 💡 Topic Section
st.markdown("### 💡 Or Enter a Topic")
topic = st.text_input("Write a topic (e.g., gym, anime, love, money):")
if st.button("✨ Generate Topic Caption"):
    if topic.strip():
        topic_caption = generate_topic_caption(topic)
        st.success(topic_caption)
        st.code(topic_caption)
        try:
            st.button("📋 Copy", on_click=st.experimental_copy, args=(topic_caption,))
        except:
            st.warning("Update Streamlit to latest version to use the copy feature 💻")
    else:
        st.warning("Please type something, babe 🫶")

# 💸 Tip Jar
# 💸 Tip Me in Crypto Section
st.markdown("---")
st.markdown("### 💸 Love this tool? Tip me in crypto!")

st.info(
    "**BTC Wallet:** `bc1q08dss8tfkvl2mx3qgz44danzet4a707f5aj3xs"
    "**ETH Wallet:** `0xE3356ad20DC404C514C6dAadd6c062C1F22431Df"
)

st.markdown(
    """
    <div style='text-align:center; font-size:13px; color:gray;'>
    Loved the captions? Drop me a coffee in crypto ☕❤️<br>
    Every satoshi helps me keep this tool free and spicy 🔥
    </div>
    """,
    unsafe_allow_html=True
)



