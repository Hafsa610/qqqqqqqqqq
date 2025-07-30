import streamlit as st
import random

st.set_page_config(page_title="Infinity Cool Urdu Poetry", page_icon="🌈", layout="centered")

bg_images = [
    "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1200&q=80"
]

quotes = [
    "محبت میں شاعری خود بخود دل سے نکلتی ہے۔",
    "خوابوں کی دنیا میں شاعری ایک روشنی ہے۔",
    "شاعری دل کی زبان ہے، جو ہر حال میں مسکراہٹ دے جاتی ہے۔",
    "غم ہو یا خوشی، شاعری ہمیشہ ساتھ رہتی ہے۔"
]

moods = {
    "Happy": {
        "subjects": ["Muskurahat", "Umeed", "Khushi", "Roshan Din", "Aasman"],
        "verbs": ["chamakta hai", "muskurata hai", "roshni deta hai", "gungunata hai", "mehka deta hai"],
        "objects": ["zindagi mein", "dil mein", "khayalon mein", "yaadon ke saath", "umeedon ke saaye"]
    },
    "Sad": {
        "subjects": ["Aansu", "Tanhaai", "Dil", "Raat", "Yaad"],
        "verbs": ["chup rehta hai", "dhadakta hai", "bikharta hai", "gum ho jata hai", "sannata deta hai"],
        "objects": ["khamoshi mein", "yaadon mein", "tanhaai mein", "ishq ke safar mein", "dil ki gehraaiyon mein"]
    },
    "Romantic": {
        "subjects": ["Chand", "Khushbu", "Nazuk Lamhe", "Ishq", "Phool"],
        "verbs": ["mehka deta hai", "muskurata hai", "chup rehta hai", "dhadakta hai", "roshni deta hai"],
        "objects": ["ishq mein", "khayalon mein", "yaadon ke saath", "tanhaai mein", "umeedon ke saaye"]
    },
    "Motivational": {
        "subjects": ["Manzil", "Hausla", "Safar", "Taqdeer", "Aasman"],
        "verbs": ["buland hota hai", "chalta hai", "roshni deta hai", "muskurata hai", "mehka deta hai"],
        "objects": ["zindagi mein", "umeedon ke saaye", "khushiyon mein", "dil mein", "khayalon mein"]
    }
}

emojis = ["🌙", "✨", "💖", "🌸", "🌠", "🌹", "🕊️", "⭐", "😊", "😢", "😍", "🔥", "🎉", "🌈", "⚡"]

rainbow_colors = [
    "#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"
]

if "bg_img" not in st.session_state:
    st.session_state.bg_img = random.choice(bg_images)

def change_bg():
    st.session_state.bg_img = random.choice(bg_images)

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('{st.session_state.bg_img}');
    background-size: cover;
}}
.poetry-line {{
    font-size: 1.6em;
    color: #fff;
    background: rgba(0,0,0,0.6);
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 14px;
    border-left: 8px solid #FFD700;
    box-shadow: 2px 2px 12px #222;
    animation: fadeIn 1.2s;
    transition: background 0.5s;
}}
@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(30px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.footer {{
    text-align: center;
    color: #fff;
    margin-top: 40px;
    font-size: 1.2em;
    background: rgba(0,0,0,0.4);
    padding: 10px;
    border-radius: 10px;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌈 Infinity Cool Urdu Poetry Website 🌈")
st.write("Har mood, har lamha, har sher infinity cool!")

col1, col2 = st.columns([2,1])
with col1:
    name = st.text_input("Apna naam likhein (optional):")
    mood = st.selectbox("Apna mood select karein:", list(moods.keys()))
    count = st.slider("Kitne sher chahiye?", min_value=1, max_value=10, value=5)
with col2:
    if st.button("Surprise Me!"):
        name = random.choice(["Ali", "Sara", "Zain", "Ayesha", "Hamza", "Noor", ""])
        mood = random.choice(list(moods.keys()))
        count = random.randint(1, 10)
        change_bg()
        st.success(f"Naam: {name or 'Anonymous'} | Mood: {mood} | Sher: {count}")

def generate_poetry(name=None, mood="Happy"):
    subject = random.choice(moods[mood]["subjects"])
    verb = random.choice(moods[mood]["verbs"])
    obj = random.choice(moods[mood]["objects"])
    emoji = random.choice(emojis)
    color = random.choice(rainbow_colors)
    if name:
        sher = f"<span style='color:{color};'>{emoji} {name} ka {subject} {verb} {obj}.</span>"
    else:
        sher = f"<span style='color:{color};'>{emoji} {subject} {verb} {obj}.</span>"
    return sher

if st.button("Naya Sher Banayein") or st.session_state.get("bg_img_changed", False):
    poetry_list = []
    for _ in range(count):
        poetry_list.append(generate_poetry(name, mood))
    for sher in poetry_list:
        st.markdown(f"<div class='poetry-line'>{sher}</div>", unsafe_allow_html=True)
        st.code(sher, language='')
    change_bg()
    st.session_state.bg_img_changed = False

st.markdown(f"<div class='footer'>{random.choice(quotes)}</div>", unsafe_allow_html=True)