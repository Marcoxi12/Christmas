import streamlit as st
import time

st.set_page_config(page_title="Christmas Trip 🎄", page_icon="🎄", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif !important; }
.stApp { background: #0f0f0f; color: #f5f0e8; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; max-width: 700px; }

/* Progress bar */
.prog-wrap { display: flex; gap: 6px; margin-bottom: 32px; }
.prog-seg {
    height: 3px; flex: 1; border-radius: 2px;
    background: #2a2a2a;
    transition: background 0.4s;
}
.prog-seg.done { background: #e8c14e; }
.prog-seg.active { background: #e8c14e; opacity: 0.5; }

/* Question */
.q-num { font-size: 11px; font-weight: 600; letter-spacing: 0.15em; color: #e8c14e; text-transform: uppercase; margin-bottom: 10px; }
.q-text { font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 4vw, 2rem); font-weight: 700; color: #f5f0e8; line-height: 1.25; margin-bottom: 6px; }
.q-sub { font-size: 13px; color: #666; margin-bottom: 28px; line-height: 1.6; }

/* Radio override */
div[data-testid="stRadio"] > div { gap: 8px !important; }
div[data-testid="stRadio"] label {
    background: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 8px !important;
    padding: 14px 18px !important;
    font-size: 14px !important;
    color: #c8c0b0 !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    display: block !important;
    width: 100% !important;
}
div[data-testid="stRadio"] label:hover { border-color: #e8c14e !important; color: #f5f0e8 !important; }

/* Button */
.stButton > button {
    background: #e8c14e !important; border: none !important;
    color: #0f0f0f !important; font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important; font-weight: 600 !important;
    border-radius: 6px !important; padding: 12px 28px !important;
    width: 100% !important; margin-top: 16px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover { background: #f0ce6a !important; transform: translateY(-1px) !important; }

/* Result */
.reveal-label { font-size: 11px; font-weight: 600; letter-spacing: 0.15em; color: #e8c14e; text-transform: uppercase; text-align: center; margin-bottom: 12px; }
.city-hero { position: relative; border-radius: 16px; overflow: hidden; margin-bottom: 0; }
.city-hero img { width: 100%; height: 280px; object-fit: cover; display: block; filter: brightness(0.75); }
.city-hero-overlay {
    position: absolute; bottom: 0; left: 0; right: 0;
    padding: 32px 28px 24px;
    background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%);
}
.city-hero-name { font-family: 'Playfair Display', serif; font-size: 2.4rem; font-weight: 900; color: #fff; line-height: 1; margin-bottom: 6px; }
.city-hero-meta { font-size: 12px; color: rgba(255,255,255,0.6); letter-spacing: 0.04em; }

.city-body { background: #1a1a1a; border-radius: 0 0 16px 16px; padding: 22px 24px 24px; margin-bottom: 24px; }
.city-desc { font-size: 15px; color: #c8c0b0; line-height: 1.75; margin-bottom: 18px; }
.city-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }
.pill { background: #252525; border: 1px solid #333; border-radius: 20px; padding: 5px 14px; font-size: 12px; color: #999; }
.why-box { background: #111; border-left: 3px solid #e8c14e; padding: 14px 16px; border-radius: 0 6px 6px 0; font-size: 13px; color: #b8a878; line-height: 1.6; }

.others-label { font-size: 11px; font-weight: 600; letter-spacing: 0.15em; color: #555; text-transform: uppercase; margin: 28px 0 14px; }
.runner { display: flex; align-items: center; gap: 16px; background: #151515; border-radius: 10px; padding: 14px 16px; margin-bottom: 10px; border: 1px solid #222; }
.runner img { width: 64px; height: 64px; border-radius: 8px; object-fit: cover; flex-shrink: 0; }
.runner-name { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: #f5f0e8; margin-bottom: 3px; }
.runner-sub { font-size: 12px; color: #555; line-height: 1.5; }

.footer-note { text-align: center; padding: 32px 0 48px; font-family: 'Playfair Display', serif; font-size: 1rem; font-style: italic; color: #555; }
.footer-note span { color: #e8c14e; }
</style>
""", unsafe_allow_html=True)

CITIES = {
    "New York": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/1280px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/400px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
        "meta": "~3h flight · 32–45°F · $$$$ · best 3-day US city",
        "desc": "Bryant Park ice rink Friday night, 5th Ave windows Saturday, a diner breakfast before the flight home. Three days in New York at Christmas goes hard.",
        "pills": ["🗽 Iconic", "❄️ Real winter", "🍕 Best food scene", "🎭 Culture overload"],
        "tags": ["food", "nightlife", "culture", "cold"],
    },
    "Denver": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Denver_skyline_from_City_Park_2.jpg/1280px-Denver_skyline_from_City_Park_2.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Denver_skyline_from_City_Park_2.jpg/400px-Denver_skyline_from_City_Park_2.jpg",
        "meta": "~2.5h flight · 20–45°F · $$$",
        "desc": "Fly in, check into a spot in LoDo, wake up to snow and the Rockies out the window. Three days goes surprisingly far when the scenery is that good.",
        "pills": ["🏔️ Mountains", "❄️ Actual snow", "⛷️ Ski day trips", "🍺 Great bars"],
        "tags": ["outdoors", "scenery", "cold", "relaxed"],
    },
    "Nashville": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg/1280px-Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg/400px-Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg",
        "meta": "~1.5h flight · 35–50°F · $$ · perfect weekend city",
        "desc": "Short flight, easy weekend. Hit Broadway Friday night, hot chicken Saturday, rooftop bar Sunday before the flight home. Nashville is built for a 3-day trip.",
        "pills": ["🎵 Live music", "🍗 Hot chicken", "🕺 Best nightlife $", "🌙 Never sleeps"],
        "tags": ["nightlife", "food", "music", "mild", "packed"],
    },
    "Chicago": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Chicago_wideangle_from_john_hancock.jpg/1280px-Chicago_wideangle_from_john_hancock.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Chicago_wideangle_from_john_hancock.jpg/400px-Chicago_wideangle_from_john_hancock.jpg",
        "meta": "~2.5h flight · 20–38°F · $$$",
        "desc": "Christkindlmarket Friday, Magnificent Mile Saturday, deep dish before the flight home. Chicago is a full weekend without even trying — everything is walkable.",
        "pills": ["🎄 Christkindlmarket", "🏛️ Architecture", "🍕 Deep dish", "❄️ Feels like Christmas"],
        "tags": ["food", "culture", "cold", "packed"],
    },
    "Atlanta": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlanta_from_Buckhead_2018.jpg/1280px-Atlanta_from_Buckhead_2018.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlanta_from_Buckhead_2018.jpg/400px-Atlanta_from_Buckhead_2018.jpg",
        "meta": "~2h flight · 38–55°F · $$",
        "desc": "Direct flight under 2 hours, great food, easy to get around. Atlanta is the low-stress weekend trip — no chaos, just a good time.",
        "pills": ["🍑 Southern food", "🌆 Great neighborhoods", "✈️ Easy direct flight", "😌 No crowds"],
        "tags": ["food", "culture", "mild", "relaxed"],
    },
    "New Orleans": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/New_Orleans_French_Quarter.jpg/1280px-New_Orleans_French_Quarter.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/New_Orleans_French_Quarter.jpg/400px-New_Orleans_French_Quarter.jpg",
        "meta": "~1h flight · 48–62°F · $$ · closest city on the list",
        "desc": "One hour from Houston, French Quarter decorated for the holidays, best food in America. Three days in NOLA and you'll eat and drink better than anywhere else on this list.",
        "pills": ["🎷 Jazz everywhere", "🦞 Best food in America", "🎉 Always a party", "🌶️ The vibe"],
        "tags": ["food", "nightlife", "music", "warm", "packed"],
    },
}

QUESTIONS = [
    {
        "num": "01",
        "text": "What does your ideal December weather look like?",
        "sub": "Be honest — Houston has no winter so literally anything counts as a change.",
        "options": [
            ("❄️  Cold cold — I want snow, a coat, the real thing", "cold"),
            ("🧥  Crisp — cool enough to feel like the holidays", "mild"),
            ("☀️  Mild — I run cold, 50s is fine, please no frost", "warm"),
        ]
    },
    {
        "num": "02",
        "text": "The trip is amazing. What made it?",
        "sub": "Pick the one thing you'd be most upset about missing.",
        "options": [
            ("🍽️  The food — we ate our way through every neighborhood", "food"),
            ("🌙  The nights out — we closed down more than one bar", "nightlife"),
            ("🏔️  The scenery — views, fresh air, being outside", "outdoors"),
            ("🎭  The culture — museums, history, architecture", "culture"),
            ("🎵  The music — live sets, jazz clubs, honky tonks", "music"),
        ]
    },
    {
        "num": "03",
        "text": "How packed is your perfect itinerary?",
        "sub": "No wrong answer.",
        "options": [
            ("🔥  Max — new spot every few hours, no downtime", "packed"),
            ("😌  Balanced — a couple things a day, no rushing", "balanced"),
            ("🛋️  Easy — good food, slow mornings, no real schedule", "relaxed"),
        ]
    },
    {
        "num": "04",
        "text": "Your travel style in one sentence:",
        "sub": None,
        "options": [
            ("📸  I want photos that make people ask where we went", "scenic"),
            ("🍜  I will eat at the most-hyped restaurant in every city", "foodie"),
            ("🎉  I want a story to tell when we get back", "social"),
            ("🌿  I want to come back actually rested", "chill"),
        ]
    },
    {
        "num": "05",
        "text": "New York is on the list. Real talk:",
        "sub": "It's the most magical Christmas city. It's also the most expensive.",
        "options": [
            ("💸  I want it — we'll figure out the budget", "nyc_yes"),
            ("😅  Honestly... probably not this time", "nyc_maybe"),
            ("🙅  Skip it, I want somewhere different anyway", "nyc_no"),
        ]
    },
    {
        "num": "06",
        "text": "Last one. Pick your vibe:",
        "sub": None,
        "options": [
            ("🏙️  Big city energy, tall buildings, always something happening", "bigcity"),
            ("🎶  Somewhere with a music scene that actually slaps", "music_scene"),
            ("🌄  Somewhere with a backdrop — scenery, nature, views", "nature"),
            ("🥘  Somewhere I'll be thinking about the food for months", "food_obsessed"),
        ]
    },
]

def score_cities(answers):
    scores = {c: 0 for c in CITIES}

    weather = answers.get("q0")
    priority = answers.get("q1")
    energy = answers.get("q2")
    style = answers.get("q3")
    nyc = answers.get("q4")
    vibe = answers.get("q5")

    # Weather
    if weather == "cold":
        for c in ["New York", "Denver", "Chicago"]: scores[c] += 4
        for c in ["Nashville", "Atlanta", "New Orleans"]: scores[c] -= 1
    elif weather == "mild":
        for c in ["Nashville", "Atlanta"]: scores[c] += 4
        scores["New Orleans"] += 2
        scores["Denver"] += 1
    elif weather == "warm":
        scores["New Orleans"] += 5
        scores["Atlanta"] += 4
        scores["Nashville"] += 3
        for c in ["New York", "Denver", "Chicago"]: scores[c] -= 2

    # Priority
    if priority == "food":
        scores["New Orleans"] += 4
        scores["Nashville"] += 3
        scores["Chicago"] += 3
        scores["Atlanta"] += 3
        scores["New York"] += 2
        scores["Denver"] += 1
    elif priority == "nightlife":
        scores["Nashville"] += 5
        scores["New Orleans"] += 4
        scores["New York"] += 3
        scores["Atlanta"] += 2
        scores["Chicago"] += 2
        scores["Denver"] += 0
    elif priority == "outdoors":
        scores["Denver"] += 7
        scores["Nashville"] += 1
        scores["New York"] += 1
    elif priority == "culture":
        scores["New York"] += 6
        scores["Chicago"] += 5
        scores["New Orleans"] += 3
        scores["Atlanta"] += 2
    elif priority == "music":
        scores["Nashville"] += 7
        scores["New Orleans"] += 5
        scores["Chicago"] += 1
        scores["Atlanta"] += 2

    # Energy
    if energy == "packed":
        for c in ["New York", "Nashville", "New Orleans"]: scores[c] += 3
        scores["Denver"] -= 1
    elif energy == "balanced":
        for c in ["Chicago", "Atlanta", "Denver"]: scores[c] += 2
    elif energy == "relaxed":
        scores["New Orleans"] += 2
        scores["Denver"] += 3
        scores["Atlanta"] += 3
        for c in ["New York", "Nashville"]: scores[c] -= 1

    # Travel style
    if style == "scenic":
        scores["Denver"] += 4
        scores["New York"] += 2
        scores["Chicago"] += 2
    elif style == "foodie":
        scores["New Orleans"] += 4
        scores["Nashville"] += 3
        scores["Chicago"] += 3
        scores["Atlanta"] += 2
        scores["New York"] += 2
    elif style == "social":
        scores["Nashville"] += 4
        scores["New Orleans"] += 3
        scores["New York"] += 3
        scores["Chicago"] += 2
    elif style == "chill":
        scores["Denver"] += 3
        scores["Atlanta"] += 3
        scores["New Orleans"] += 2
        for c in ["New York", "Nashville"]: scores[c] -= 1

    # NYC question — this is the big one
    if nyc == "nyc_yes":
        scores["New York"] += 10
    elif nyc == "nyc_maybe":
        scores["New York"] -= 4
        for c in ["Nashville", "Chicago", "Atlanta"]: scores[c] += 2
    elif nyc == "nyc_no":
        scores["New York"] -= 15
        for c in ["Denver", "Nashville", "New Orleans"]: scores[c] += 3

    # Final vibe
    if vibe == "bigcity":
        scores["New York"] += 4
        scores["Chicago"] += 3
        scores["Atlanta"] += 2
    elif vibe == "music_scene":
        scores["Nashville"] += 5
        scores["New Orleans"] += 4
        scores["Chicago"] += 1
    elif vibe == "nature":
        scores["Denver"] += 6
        scores["Nashville"] += 1
    elif vibe == "food_obsessed":
        scores["New Orleans"] += 5
        scores["Nashville"] += 3
        scores["Chicago"] += 3
        scores["Atlanta"] += 2
        scores["New York"] += 2

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def why_match(city_name, answers):
    lines = {
        "New York": "You said you want the real Christmas experience — Bryant Park ice rink, 5th Ave windows, holiday energy everywhere. NYC delivers that like nowhere else.",
        "Denver": "The Rockies in December with actual snow hits different. You want scenery and a real winter — Denver's the answer.",
        "Nashville": "Live music, late nights, great food, and your dollar goes twice as far as NYC. Nashville matches your energy perfectly.",
        "Chicago": "A real Christmas market, stunning architecture, deep dish, and a city that feels like the holidays. Chicago's the underrated pick.",
        "Atlanta": "Easy flight, great food, low-key vibe, no crowds. Atlanta gives you a great trip without the chaos.",
        "New Orleans": "The French Quarter at Christmas, the best food in America, and jazz coming out of every door. NOLA fits your vibe.",
    }
    return lines.get(city_name, "")

# ── State ──
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

STEP = st.session_state.step
TOTAL = len(QUESTIONS)

def advance(key, val):
    st.session_state.answers[key] = val
    st.session_state.step += 1

# ══════════════════════════════
# INTRO
# ══════════════════════════════
if STEP == 0:
    st.markdown("""
    <div style="padding: 60px 0 40px; text-align: center;">
        <div style="font-size:48px; margin-bottom: 20px;">🎄</div>
        <div style="font-size:11px; font-weight:600; letter-spacing:0.15em; color:#e8c14e; text-transform:uppercase; margin-bottom:16px;">A gift from Marco</div>
        <div style="font-family:'Playfair Display',serif; font-size:clamp(2rem,6vw,2.8rem); font-weight:900; color:#f5f0e8; line-height:1.15; margin-bottom:18px;">
            Where should we go<br>for Christmas?
        </div>
        <div style="font-size:14px; color:#666; max-width: 380px; margin: 0 auto 40px; line-height:1.7;">
            6 questions. Real answers. Wherever you pick — I've already got it handled.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.button("Let's go →", on_click=lambda: setattr(st.session_state, 'step', 1))

# ══════════════════════════════
# QUESTIONS
# ══════════════════════════════
elif 1 <= STEP <= TOTAL:
    q = QUESTIONS[STEP - 1]

    # Progress bar
    segs = ""
    for i in range(TOTAL):
        cls = "done" if i < STEP - 1 else ("active" if i == STEP - 1 else "")
        segs += f'<div class="prog-seg {cls}"></div>'
    st.markdown(f'<div class="prog-wrap">{segs}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="q-num">Question {q["num"]} of {TOTAL:02d}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="q-text">{q["text"]}</div>', unsafe_allow_html=True)
    if q["sub"]:
        st.markdown(f'<div class="q-sub">{q["sub"]}</div>', unsafe_allow_html=True)

    key = f"q{STEP-1}"
    choice = st.radio("", [o[0] for o in q["options"]], label_visibility="collapsed", key=f"radio_{STEP}")

    val = next(v for label, v in q["options"] if label == choice)
    label = "Find our city 🎄" if STEP == TOTAL else "Next →"
    st.button(label, on_click=lambda k=key, v=val: advance(k, v))

# ══════════════════════════════
# CALCULATING
# ══════════════════════════════
elif STEP == TOTAL + 1:
    st.markdown("""
    <div style="text-align:center; padding: 80px 20px;">
        <div style="font-size:32px; margin-bottom:20px;">✨</div>
        <div style="font-family:'Playfair Display',serif; font-size:1.3rem; color:#666; font-style:italic;">Finding your city...</div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1.5)
    st.session_state.step += 1
    st.rerun()

# ══════════════════════════════
# RESULTS
# ══════════════════════════════
elif STEP == TOTAL + 2:
    ranked = score_cities(st.session_state.answers)
    top_name, _ = ranked[0]
    top = CITIES[top_name]

    st.markdown('<div class="reveal-label">✈️ Your city is</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="city-hero">
        <img src="{top['photo']}" alt="{top_name}"/>
        <div class="city-hero-overlay">
            <div class="city-hero-name">{top_name}</div>
            <div class="city-hero-meta">{top['meta']}</div>
        </div>
    </div>
    <div class="city-body">
        <div class="city-desc">{top['desc']}</div>
        <div class="city-pills">{''.join(f'<span class="pill">{p}</span>' for p in top['pills'])}</div>
        <div class="why-box">💬 {why_match(top_name, st.session_state.answers)}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="others-label">The rest of the list</div>', unsafe_allow_html=True)

    for name, score in ranked[1:4]:
        city = CITIES[name]
        st.markdown(f"""
        <div class="runner">
            <img src="{city['thumb']}" alt="{name}"/>
            <div>
                <div class="runner-name">{name}</div>
                <div class="runner-sub">{city['meta']}<br>{city['desc'][:80]}...</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-note">
        Whatever you pick — <span>Marco's got it handled.</span> 🎁
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Take it again"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()
