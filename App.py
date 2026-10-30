import streamlit as st
import time

st.set_page_config(page_title="Our Christmas Trip ✈️", page_icon="🎄", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #faf7f2 !important;
    color: #1a1614 !important;
}
.stApp { background-color: #faf7f2; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 3rem; max-width: 680px; }

.gift-header {
    text-align: center;
    padding: 40px 24px 32px;
}
.gift-tag {
    display: inline-block;
    background: #c8392b;
    color: white;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 2px;
    margin-bottom: 20px;
}
.gift-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 6vw, 3rem);
    font-weight: 900;
    color: #1a1614;
    line-height: 1.15;
    margin-bottom: 14px;
}
.gift-title em { color: #c8392b; font-style: italic; }
.gift-sub {
    font-size: 15px;
    color: #6b6460;
    line-height: 1.6;
    max-width: 420px;
    margin: 0 auto;
}

.question-label {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #1a1614;
    margin-bottom: 6px;
}
.question-sub {
    font-size: 13px;
    color: #8a7f7a;
    margin-bottom: 20px;
    line-height: 1.5;
}

div[data-testid="stRadio"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    color: #2a2220 !important;
    padding: 2px 0 !important;
}

.stButton > button {
    background: #1a1614 !important;
    border: none !important;
    color: #faf7f2 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    border-radius: 4px !important;
    padding: 12px 32px !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: #c8392b !important;
    transform: translateY(-1px) !important;
}

.divider {
    border: none;
    border-top: 1px solid #e8e2da;
    margin: 28px 0;
}

/* City result card */
.city-card {
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 16px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.10);
}
.city-img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}
.city-card-body {
    background: white;
    padding: 20px 22px 22px;
}
.city-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 900;
    color: #1a1614;
    margin-bottom: 4px;
}
.city-meta {
    font-size: 12px;
    color: #8a7f7a;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
}
.city-desc {
    font-size: 14px;
    color: #3a3230;
    line-height: 1.65;
    margin-bottom: 14px;
}
.city-highlight {
    background: #fdf3f2;
    border-left: 3px solid #c8392b;
    padding: 10px 14px;
    font-size: 13px;
    color: #6b2020;
    line-height: 1.5;
    border-radius: 0 4px 4px 0;
}

.runner-up {
    background: white;
    border-radius: 10px;
    padding: 16px 20px;
    display: flex;
    gap: 16px;
    align-items: center;
    margin-bottom: 10px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.runner-up-img {
    width: 72px;
    height: 72px;
    border-radius: 8px;
    object-fit: cover;
    flex-shrink: 0;
}
.runner-up-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #1a1614;
    margin-bottom: 3px;
}
.runner-up-desc { font-size: 12px; color: #8a7f7a; line-height: 1.5; }

.final-note {
    text-align: center;
    padding: 28px 20px 40px;
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-style: italic;
    color: #6b6460;
}
.final-note strong { color: #c8392b; font-style: normal; }
</style>
""", unsafe_allow_html=True)

# ── City data with real Unsplash photos ──
CITIES = {
    "New York": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/1280px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/400px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
        "tags": ["food", "nightlife", "culture"],
        "weather": ["cold"],
        "desc": "Holiday windows on 5th Ave, Bryant Park ice rink, the best food scene in the country. Christmas in New York is a whole thing.",
        "highlight": "✈️ ~3h from Houston · ❄️ 32–45°F · 💸 $$$$",
        "score_base": 0,
    },
    "Denver": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Denver_skyline_from_City_Park_2.jpg/1280px-Denver_skyline_from_City_Park_2.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Denver_skyline_from_City_Park_2.jpg/400px-Denver_skyline_from_City_Park_2.jpg",
        "tags": ["outdoors", "food", "scenery"],
        "weather": ["cold"],
        "desc": "Waking up to actual snow on Christmas with the Rockies out the window. Holiday markets in LoDo, day trips to ski resorts, cozy mountain bars.",
        "highlight": "✈️ ~2.5h from Houston · ❄️ 20–45°F · 💸 $$$",
        "score_base": 0,
    },
    "Nashville": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg/1280px-Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg/400px-Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg",
        "tags": ["nightlife", "food", "music"],
        "weather": ["mild"],
        "desc": "Broadway lit up for Christmas, live music literally everywhere, hot chicken, and a food scene that surprises everyone. Most fun per dollar of any city on this list.",
        "highlight": "✈️ ~1.5h from Houston · 🌤 35–50°F · 💸 $$",
        "score_base": 0,
    },
    "Chicago": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Chicago_wideangle_from_john_hancock.jpg/1280px-Chicago_wideangle_from_john_hancock.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Chicago_wideangle_from_john_hancock.jpg/400px-Chicago_wideangle_from_john_hancock.jpg",
        "tags": ["food", "culture", "architecture"],
        "weather": ["cold"],
        "desc": "The Christkindlmarket is a real German Christmas market in Millennium Park. Magnificent Mile covered in lights. World-class deep dish. Stunning architecture.",
        "highlight": "✈️ ~2.5h from Houston · ❄️ 20–38°F · 💸 $$$",
        "score_base": 0,
    },
    "Atlanta": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlanta_from_Buckhead_2018.jpg/1280px-Atlanta_from_Buckhead_2018.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlanta_from_Buckhead_2018.jpg/400px-Atlanta_from_Buckhead_2018.jpg",
        "tags": ["food", "culture", "nightlife"],
        "weather": ["mild"],
        "desc": "Centennial Park lit up for the holidays, one of the best restaurant scenes in the South, easy direct flight from Houston. Underrated for a winter trip.",
        "highlight": "✈️ ~2h from Houston · 🌤 38–55°F · 💸 $$",
        "score_base": 0,
    },
    "New Orleans": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/New_Orleans_French_Quarter.jpg/1280px-New_Orleans_French_Quarter.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/New_Orleans_French_Quarter.jpg/400px-New_Orleans_French_Quarter.jpg",
        "tags": ["food", "nightlife", "music", "culture"],
        "weather": ["mild", "warm"],
        "desc": "The French Quarter decorated for Christmas is something else. Best eating city in America — not debatable. Jazz clubs, cocktail bars, and a vibe you can't find anywhere else.",
        "highlight": "✈️ ~1h from Houston · 🌤 48–62°F · 💸 $$",
        "score_base": 0,
    },
}

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

def advance():
    st.session_state.step += 1

STEP = st.session_state.step
A = st.session_state.answers

# ══════════════════════════════
# STEP 0 — Intro
# ══════════════════════════════
if STEP == 0:
    st.markdown("""
    <div class="gift-header">
        <div class="gift-tag">🎄 A gift from Marco</div>
        <div class="gift-title">Where should we go<br>for <em>Christmas?</em></div>
        <div class="gift-sub">Answer a few questions and I'll find the perfect city for us. Whatever you pick — I've got it handled. 🎁</div>
    </div>
    """, unsafe_allow_html=True)
    st.button("Let's find our city →", on_click=advance)

# ══════════════════════════════
# STEP 1 — Weather
# ══════════════════════════════
elif STEP == 1:
    st.markdown('<div class="question-label">What\'s your vibe for December weather?</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-sub">We\'re leaving Houston either way — question is how cold we\'re going.</div>', unsafe_allow_html=True)
    choice = st.radio("", [
        "❄️  Cold — I want actual winter, snow, the whole thing",
        "🧥  Mild — cool and comfortable, not freezing",
        "☀️  Warm — I run cold, keep it above 50°F",
    ], label_visibility="collapsed")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.button("Next →", on_click=lambda: (A.update({"weather": choice}), advance()))

# ══════════════════════════════
# STEP 2 — Priority
# ══════════════════════════════
elif STEP == 2:
    st.markdown('<div class="question-label">What makes a trip great for you?</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-sub">Pick the one thing you\'d be most upset about missing.</div>', unsafe_allow_html=True)
    choice = st.radio("", [
        "🍽️  Food — we eat our way through every city",
        "🌙  Nightlife — we\'re going out every night",
        "🏔️  Outdoors — scenery, nature, fresh air",
        "🎭  Culture — museums, architecture, history",
        "🎵  Live music and entertainment",
    ], label_visibility="collapsed")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.button("Next →", on_click=lambda: (A.update({"priority": choice}), advance()))

# ══════════════════════════════
# STEP 3 — Energy
# ══════════════════════════════
elif STEP == 3:
    st.markdown('<div class="question-label">How do you want to spend the days?</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-sub">No wrong answer — just honest.</div>', unsafe_allow_html=True)
    choice = st.radio("", [
        "🔥  Packed — new spot every few hours, sleep when we\'re home",
        "😌  Balanced — a couple things a day, no rushing",
        "🛋️  Relaxed — good food, walks, no real schedule",
    ], label_visibility="collapsed")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.button("Next →", on_click=lambda: (A.update({"energy": choice}), advance()))

# ══════════════════════════════
# STEP 4 — NYC check
# ══════════════════════════════
elif STEP == 4:
    st.markdown('<div class="question-label">Last question — be honest.</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-sub">New York at Christmas is incredible. It\'s also expensive. Where\'s your head at?</div>', unsafe_allow_html=True)
    choice = st.radio("", [
        "💸  NYC or bust — we\'ll make it work",
        "😅  I want it but realistically... probably not",
        "🙅  Skip it, I want somewhere different",
    ], label_visibility="collapsed")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.button("Find our city 🎄", on_click=lambda: (A.update({"nyc": choice}), advance()))

# ══════════════════════════════
# STEP 5 — Computing
# ══════════════════════════════
elif STEP == 5:
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px; font-family:'Playfair Display',serif; font-size:1.2rem; color:#6b6460; font-style:italic;">
        Finding your city...
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1.2)
    st.session_state.step = 6
    st.rerun()

# ══════════════════════════════
# STEP 6 — Results
# ══════════════════════════════
elif STEP == 6:
    weather = A.get("weather", "")
    priority = A.get("priority", "")
    energy = A.get("energy", "")
    nyc = A.get("nyc", "")

    scores = {c: 0 for c in CITIES}

    # Weather
    if "Cold" in weather:
        for c in ["New York","Denver","Chicago"]: scores[c] += 3
    elif "Mild" in weather:
        for c in ["Nashville","Atlanta","New Orleans"]: scores[c] += 3
    elif "Warm" in weather:
        scores["New Orleans"] += 4; scores["Atlanta"] += 3; scores["Nashville"] += 2

    # Priority
    if "Food" in priority:
        for c,v in [("New Orleans",5),("Nashville",4),("Chicago",3),("Atlanta",3),("New York",2)]: scores[c] += v
    elif "Nightlife" in priority:
        for c,v in [("New Orleans",5),("Nashville",4),("New York",3),("Atlanta",2),("Chicago",2)]: scores[c] += v
    elif "Outdoors" in priority:
        scores["Denver"] += 6; scores["New York"] += 1
    elif "Culture" in priority:
        for c,v in [("New York",5),("Chicago",4),("New Orleans",3)]: scores[c] += v
    elif "Music" in priority:
        scores["Nashville"] += 6; scores["New Orleans"] += 5; scores["Atlanta"] += 2

    # Energy
    if "Packed" in energy:
        for c in ["New York","Nashville","New Orleans"]: scores[c] += 2
    elif "Relaxed" in energy:
        for c in ["New Orleans","Denver","Atlanta"]: scores[c] += 2

    # NYC
    if "NYC or bust" in nyc:
        scores["New York"] += 8
    elif "probably not" in nyc:
        scores["New York"] -= 3
    elif "Skip" in nyc:
        scores["New York"] -= 12

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_name = ranked[0][0]
    top = CITIES[top_name]
    second_name = ranked[1][0]
    second = CITIES[second_name]
    third_name = ranked[2][0]
    third = CITIES[third_name]

    st.markdown(f"""
    <div style="text-align:center; margin-bottom:28px;">
        <div style="font-size:11px; font-weight:600; letter-spacing:0.14em; text-transform:uppercase; color:#c8392b; margin-bottom:10px;">✈️ Your city is</div>
        <div style="font-family:'Playfair Display',serif; font-size:2.4rem; font-weight:900; color:#1a1614; line-height:1.1;">{top_name}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="city-card">
        <img class="city-img" src="{top['photo']}" alt="{top_name}"/>
        <div class="city-card-body">
            <div class="city-name">{top_name}</div>
            <div class="city-meta">{top['highlight']}</div>
            <div class="city-desc">{top['desc']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:12px; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; color:#8a7f7a; margin: 24px 0 12px;">
        Also worth considering
    </div>
    """, unsafe_allow_html=True)

    for name, data in [(second_name, second), (third_name, third)]:
        st.markdown(f"""
        <div class="runner-up">
            <img class="runner-up-img" src="{data['photo']}" alt="{name}"/>
            <div>
                <div class="runner-up-name">{name}</div>
                <div class="runner-up-desc">{data['desc'][:90]}...</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="final-note">
        Whatever you pick — <strong>Marco's got it handled.</strong> 🎄
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Start over"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()
