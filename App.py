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

.prog-wrap { display: flex; gap: 6px; margin-bottom: 32px; }
.prog-seg { height: 3px; flex: 1; border-radius: 2px; background: #2a2a2a; transition: background 0.4s; }
.prog-seg.done { background: #e8c14e; }
.prog-seg.active { background: #e8c14e; opacity: 0.5; }

.q-num { font-size: 11px; font-weight: 600; letter-spacing: 0.15em; color: #e8c14e; text-transform: uppercase; margin-bottom: 10px; }
.q-text { font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 4vw, 2rem); font-weight: 700; color: #f5f0e8; line-height: 1.25; margin-bottom: 6px; }
.q-sub { font-size: 13px; color: #666; margin-bottom: 28px; line-height: 1.6; }

div[data-testid="stRadio"] > div { gap: 8px !important; }
div[data-testid="stRadio"] label {
    background: #1a1a1a !important; border: 1px solid #2a2a2a !important;
    border-radius: 8px !important; padding: 14px 18px !important;
    font-size: 14px !important; color: #c8c0b0 !important;
    cursor: pointer !important; transition: all 0.2s !important;
    display: block !important; width: 100% !important;
}
div[data-testid="stRadio"] label:hover { border-color: #e8c14e !important; color: #f5f0e8 !important; }

.stButton > button {
    background: #e8c14e !important; border: none !important;
    color: #0f0f0f !important; font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important; font-weight: 600 !important;
    border-radius: 6px !important; padding: 12px 28px !important;
    width: 100% !important; margin-top: 16px !important; transition: all 0.2s !important;
}
.stButton > button:hover { background: #f0ce6a !important; transform: translateY(-1px) !important; }

.reveal-label { font-size: 11px; font-weight: 600; letter-spacing: 0.15em; color: #e8c14e; text-transform: uppercase; text-align: center; margin-bottom: 12px; }
.city-hero { position: relative; border-radius: 16px; overflow: hidden; margin-bottom: 0; }
.city-hero img { width: 100%; height: 280px; object-fit: cover; display: block; filter: brightness(0.75); }
.city-hero-overlay {
    position: absolute; bottom: 0; left: 0; right: 0; padding: 32px 28px 24px;
    background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%);
}
.city-hero-name { font-family: 'Playfair Display', serif; font-size: 2.4rem; font-weight: 900; color: #fff; line-height: 1; margin-bottom: 6px; }
.city-hero-meta { font-size: 12px; color: rgba(255,255,255,0.6); letter-spacing: 0.04em; }

.city-body { background: #1a1a1a; border-radius: 0 0 16px 16px; padding: 22px 24px 24px; margin-bottom: 24px; }
.city-desc { font-size: 15px; color: #c8c0b0; line-height: 1.75; margin-bottom: 18px; }
.city-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }
.pill { background: #252525; border: 1px solid #333; border-radius: 20px; padding: 5px 14px; font-size: 12px; color: #999; }
.why-box { background: #111; border-left: 3px solid #e8c14e; padding: 14px 16px; border-radius: 0 6px 6px 0; font-size: 13px; color: #b8a878; line-height: 1.6; }

.section-label { font-size: 11px; font-weight: 600; letter-spacing: 0.15em; color: #555; text-transform: uppercase; margin: 28px 0 14px; }

/* Final choice cards */
.choice-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 28px; }
.choice-card { border-radius: 12px; overflow: hidden; cursor: pointer; border: 2px solid transparent; transition: all 0.2s; }
.choice-card:hover { border-color: #e8c14e; transform: translateY(-2px); }
.choice-card img { width: 100%; height: 140px; object-fit: cover; display: block; filter: brightness(0.7); }
.choice-card-label { background: #1a1a1a; padding: 12px 14px; }
.choice-card-name { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: #f5f0e8; margin-bottom: 2px; }
.choice-card-sub { font-size: 11px; color: #555; }

.runner { display: flex; align-items: center; gap: 16px; background: #151515; border-radius: 10px; padding: 14px 16px; margin-bottom: 10px; border: 1px solid #222; }
.runner img { width: 64px; height: 64px; border-radius: 8px; object-fit: cover; flex-shrink: 0; }
.runner-name { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: #f5f0e8; margin-bottom: 3px; }
.runner-sub { font-size: 12px; color: #555; line-height: 1.5; }

.footer-note { text-align: center; padding: 32px 0 48px; font-size: 14px; color: #555; line-height: 1.7; }
.footer-note span { color: #e8c14e; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

CITIES = {
    "New York": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/1280px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg/400px-Southwest_corner_of_Central_Park%2C_looking_east%2C_NYC.jpg",
        "meta": "~3h · 32–45°F · $$$$",
        "desc": "Bryant Park ice rink Friday night, 5th Ave windows Saturday, diner breakfast before the flight home. three days in NYC at christmas just hits.",
        "pills": ["🗽 Iconic", "❄️ Real winter", "🍕 Best food scene", "🎭 Culture overload"],
        "why": "you said you wanted the real christmas energy — nyc is the only city where that's actually true fr",
    },
    "Denver": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Denver_skyline_from_City_Park_2.jpg/1280px-Denver_skyline_from_City_Park_2.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Denver_skyline_from_City_Park_2.jpg/400px-Denver_skyline_from_City_Park_2.jpg",
        "meta": "~2.5h · 20–45°F · $$$",
        "desc": "fly in, check into a spot in lodo, wake up to snow with the rockies right there. the backdrop alone makes it worth it tbh",
        "pills": ["🏔️ Mountains", "❄️ Actual snow", "⛷️ Ski day trips", "🍺 Great bars"],
        "why": "you want scenery and a real winter — denver's genuinely the move. waking up to snow and mountains hits different",
    },
    "Nashville": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg/1280px-Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg/400px-Nashville_Skyline_from_Bicentennial_Capitol_Mall_State_Park.jpg",
        "meta": "~1.5h · 35–50°F · $$",
        "desc": "broadway friday night, hot chicken saturday, rooftop before the flight home. short flight, easy weekend, your money actually goes somewhere",
        "pills": ["🎵 Live music", "🍗 Hot chicken", "🕺 Nightlife", "🌙 Never sleeps"],
        "why": "live music, late nights, great food — and it's like half the price of nyc. nashville fits your energy",
    },
    "Chicago": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Chicago_wideangle_from_john_hancock.jpg/1280px-Chicago_wideangle_from_john_hancock.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Chicago_wideangle_from_john_hancock.jpg/400px-Chicago_wideangle_from_john_hancock.jpg",
        "meta": "~2.5h · 20–38°F · $$$",
        "desc": "actual german christmas market in millennium park, magnificent mile covered in lights, deep dish, architecture everywhere. feels like christmas more than anywhere else on this list",
        "pills": ["🎄 Christkindlmarket", "🏛️ Architecture", "🍕 Deep dish", "❄️ Feels like xmas"],
        "why": "real christmas market, stunning city, great food — chicago lowkey goes crazy at the holidays and nobody talks about it",
    },
    "Atlanta": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlanta_from_Buckhead_2018.jpg/1280px-Atlanta_from_Buckhead_2018.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlanta_from_Buckhead_2018.jpg/400px-Atlanta_from_Buckhead_2018.jpg",
        "meta": "~2h · 38–55°F · $$",
        "desc": "direct flight, great food, easy to get around. no chaos, no overcrowding. just a solid weekend trip with good food and good vibes",
        "pills": ["🍑 Southern food", "🌆 Great neighborhoods", "✈️ Easy direct", "😌 Low-key"],
        "why": "easy flight, great food, no stress. atlanta is the underrated pick — good trip without all the chaos",
    },
    "New Orleans": {
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/New_Orleans_French_Quarter.jpg/1280px-New_Orleans_French_Quarter.jpg",
        "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/New_Orleans_French_Quarter.jpg/400px-New_Orleans_French_Quarter.jpg",
        "meta": "~1h · 48–62°F · $$",
        "desc": "one hour from houston, french quarter decorated for christmas, best food in america. three days in nola and you'll eat and drink better than anywhere else on this list",
        "pills": ["🎷 Jazz everywhere", "🦞 Best food in America", "🎉 Always a party", "🌶️ The vibe"],
        "why": "the food, the jazz, the french quarter at christmas — nola is unmatched for vibes tbh",
    },
}

QUESTIONS = [
    {
        "num": "01",
        "text": "what kind of weather do you want in december",
        "sub": "we're escaping houston either way — question is how cold",
        "options": [
            ("❄️  cold cold — snow, a real coat, the whole thing", "cold"),
            ("🧥  crisp — feels like the holidays but not freezing", "mild"),
            ("☀️  mild — i run cold, 50s is fine, no frost please", "warm"),
        ]
    },
    {
        "num": "02",
        "text": "the trip was perfect. what made it",
        "sub": "pick the one thing you'd be most upset about missing",
        "options": [
            ("🍽️  the food — we ate our way through every neighborhood", "food"),
            ("🌙  the nights out — we closed down more than one spot", "nightlife"),
            ("🏔️  the scenery — views, fresh air, actually being outside", "outdoors"),
            ("🎭  the culture — museums, history, architecture", "culture"),
            ("🎵  the music — live sets, jazz clubs, honky tonks", "music"),
        ]
    },
    {
        "num": "03",
        "text": "how packed is your ideal itinerary",
        "sub": None,
        "options": [
            ("🔥  max — new spot every few hours, sleep when we're home", "packed"),
            ("😌  balanced — a couple things a day, no rushing", "balanced"),
            ("🛋️  easy — good food, slow mornings, no real schedule", "relaxed"),
        ]
    },
    {
        "num": "04",
        "text": "pick your travel personality",
        "sub": None,
        "options": [
            ("📸  i want photos that make people ask where we went", "scenic"),
            ("🍜  i will find the most hyped restaurant and we're going", "foodie"),
            ("🎉  i want a story to tell when we get back", "social"),
            ("🌿  i want to actually come back rested", "chill"),
        ]
    },
    {
        "num": "05",
        "text": "new york is on the list. be honest",
        "sub": "it's the best christmas city. it's also the most expensive",
        "options": [
            ("💸  i want it — we'll figure out the budget", "nyc_yes"),
            ("😅  lowkey yes but... probably not this time", "nyc_maybe"),
            ("🙅  skip it, i want somewhere different", "nyc_no"),
        ]
    },
    {
        "num": "06",
        "text": "last one — pick the vibe",
        "sub": None,
        "options": [
            ("🏙️  big city, tall buildings, always something happening", "bigcity"),
            ("🎶  somewhere with a music scene that actually goes", "music_scene"),
            ("🌄  somewhere with a backdrop — scenery, views, nature", "nature"),
            ("🥘  somewhere i'll be thinking about the food for months", "food_obsessed"),
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
        for c in ["Denver", "Chicago"]: scores[c] += 5
        scores["New York"] += 3
        for c in ["Nashville", "Atlanta", "New Orleans"]: scores[c] -= 2
    elif weather == "mild":
        for c in ["Nashville", "Atlanta"]: scores[c] += 4
        scores["New Orleans"] += 2; scores["Denver"] += 1
    elif weather == "warm":
        scores["New Orleans"] += 5; scores["Atlanta"] += 4; scores["Nashville"] += 3
        for c in ["New York", "Denver", "Chicago"]: scores[c] -= 3

    # Priority
    if priority == "food":
        scores["New Orleans"] += 3; scores["Nashville"] += 3
        scores["Chicago"] += 4; scores["Atlanta"] += 3; scores["New York"] += 2
    elif priority == "nightlife":
        scores["Nashville"] += 5; scores["New Orleans"] += 3
        scores["New York"] += 3; scores["Atlanta"] += 2; scores["Chicago"] += 2
    elif priority == "outdoors":
        scores["Denver"] += 8
        for c in ["Nashville","New York","Chicago","Atlanta","New Orleans"]: scores[c] -= 1
    elif priority == "culture":
        scores["Chicago"] += 6; scores["New York"] += 5
        scores["New Orleans"] += 3; scores["Atlanta"] += 2
    elif priority == "music":
        scores["Nashville"] += 7; scores["New Orleans"] += 4
        scores["Chicago"] += 2; scores["Atlanta"] += 2

    # Energy
    if energy == "packed":
        for c in ["New York", "Nashville", "New Orleans"]: scores[c] += 2
    elif energy == "balanced":
        for c in ["Chicago", "Denver"]: scores[c] += 3
        scores["Atlanta"] += 2
    elif energy == "relaxed":
        scores["Denver"] += 4; scores["Atlanta"] += 3
        for c in ["New York", "Nashville"]: scores[c] -= 2

    # Style
    if style == "scenic":
        scores["Denver"] += 5; scores["Chicago"] += 3; scores["New York"] += 2
    elif style == "foodie":
        scores["New Orleans"] += 3; scores["Nashville"] += 3
        scores["Chicago"] += 4; scores["Atlanta"] += 2; scores["New York"] += 2
    elif style == "social":
        scores["Nashville"] += 4; scores["New Orleans"] += 3
        scores["New York"] += 3; scores["Chicago"] += 3
    elif style == "chill":
        scores["Denver"] += 4; scores["Atlanta"] += 3
        for c in ["New York", "Nashville"]: scores[c] -= 2

    # NYC
    if nyc == "nyc_yes":
        scores["New York"] += 10
    elif nyc == "nyc_maybe":
        scores["New York"] -= 5
        scores["Chicago"] += 3; scores["Denver"] += 2
    elif nyc == "nyc_no":
        scores["New York"] -= 15
        scores["Denver"] += 4; scores["Chicago"] += 3

    # Vibe
    if vibe == "bigcity":
        scores["Chicago"] += 4; scores["New York"] += 3; scores["Atlanta"] += 2
    elif vibe == "music_scene":
        scores["Nashville"] += 5; scores["New Orleans"] += 4; scores["Chicago"] += 2
    elif vibe == "nature":
        scores["Denver"] += 7
    elif vibe == "food_obsessed":
        scores["New Orleans"] += 4; scores["Nashville"] += 3
        scores["Chicago"] += 4; scores["Atlanta"] += 2; scores["New York"] += 2

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # ── RIG: Denver and Chicago always top 2 (in whichever order they earned) ──
    dc = [(n, s) for n, s in ranked if n in ("Denver", "Chicago")]
    rest = [(n, s) for n, s in ranked if n not in ("Denver", "Chicago")]
    return dc + rest

# ── State ──
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "final_pick" not in st.session_state:
    st.session_state.final_pick = None

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
        <div style="font-size:11px; font-weight:600; letter-spacing:0.15em; color:#e8c14e; text-transform:uppercase; margin-bottom:16px;">from marco</div>
        <div style="font-family:'Playfair Display',serif; font-size:clamp(2rem,6vw,2.8rem); font-weight:900; color:#f5f0e8; line-height:1.15; margin-bottom:18px;">
            where should we go<br>for christmas
        </div>
        <div style="font-size:14px; color:#666; max-width: 380px; margin: 0 auto 40px; line-height:1.7;">
            6 questions. real answers. wherever you pick — i already got it handled 🎁
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.button("let's go →", on_click=lambda: setattr(st.session_state, 'step', 1))

# ══════════════════════════════
# QUESTIONS
# ══════════════════════════════
elif 1 <= STEP <= TOTAL:
    q = QUESTIONS[STEP - 1]

    segs = ""
    for i in range(TOTAL):
        cls = "done" if i < STEP - 1 else ("active" if i == STEP - 1 else "")
        segs += f'<div class="prog-seg {cls}"></div>'
    st.markdown(f'<div class="prog-wrap">{segs}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="q-num">{q["num"]} / {TOTAL:02d}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="q-text">{q["text"]}</div>', unsafe_allow_html=True)
    if q["sub"]:
        st.markdown(f'<div class="q-sub">{q["sub"]}</div>', unsafe_allow_html=True)

    key = f"q{STEP-1}"
    choice = st.radio("", [o[0] for o in q["options"]], label_visibility="collapsed", key=f"radio_{STEP}")
    val = next(v for label, v in q["options"] if label == choice)
    label = "see the results 🎄" if STEP == TOTAL else "next →"
    st.button(label, on_click=lambda k=key, v=val: advance(k, v))

# ══════════════════════════════
# CALCULATING
# ══════════════════════════════
elif STEP == TOTAL + 1:
    st.markdown("""
    <div style="text-align:center; padding: 80px 20px;">
        <div style="font-size:32px; margin-bottom:20px;">✨</div>
        <div style="font-family:'Playfair Display',serif; font-size:1.3rem; color:#666; font-style:italic;">figuring it out...</div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1.5)
    st.session_state.step += 1
    st.rerun()

# ══════════════════════════════
# RESULTS — pick between the two
# ══════════════════════════════
elif STEP == TOTAL + 2 and st.session_state.final_pick is None:
    ranked = score_cities(st.session_state.answers)
    first_name, _ = ranked[0]
    second_name, _ = ranked[1]
    first = CITIES[first_name]
    second = CITIES[second_name]

    st.markdown("""
    <div style="text-align:center; margin-bottom: 28px;">
        <div style="font-size:11px; font-weight:600; letter-spacing:0.15em; color:#e8c14e; text-transform:uppercase; margin-bottom:10px;">it came down to these two</div>
        <div style="font-family:'Playfair Display',serif; font-size:1.8rem; font-weight:900; color:#f5f0e8; line-height:1.2;">which one</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="choice-card">
            <img src="{first['photo']}" alt="{first_name}"/>
            <div class="choice-card-label">
                <div class="choice-card-name">{first_name}</div>
                <div class="choice-card-sub">{first['meta']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"→ {first_name}", key="pick_first",
                  on_click=lambda n=first_name: setattr(st.session_state, 'final_pick', n))

    with col2:
        st.markdown(f"""
        <div class="choice-card">
            <img src="{second['photo']}" alt="{second_name}"/>
            <div class="choice-card-label">
                <div class="choice-card-name">{second_name}</div>
                <div class="choice-card-sub">{second['meta']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"→ {second_name}", key="pick_second",
                  on_click=lambda n=second_name: setattr(st.session_state, 'final_pick', n))

# ══════════════════════════════
# FINAL REVEAL
# ══════════════════════════════
elif st.session_state.final_pick is not None:
    pick = st.session_state.final_pick
    city = CITIES[pick]

    st.markdown(f'<div class="reveal-label">✈️ you picked</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="city-hero">
        <img src="{city['photo']}" alt="{pick}"/>
        <div class="city-hero-overlay">
            <div class="city-hero-name">{pick}</div>
            <div class="city-hero-meta">{city['meta']}</div>
        </div>
    </div>
    <div class="city-body">
        <div class="city-desc">{city['desc']}</div>
        <div class="city-pills">{''.join(f'<span class="pill">{p}</span>' for p in city['pills'])}</div>
        <div class="why-box">💬 {city['why']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="footer-note">
        <span>{pick} it is</span> — i got it from here 🎁
    </div>
    """, unsafe_allow_html=True)

    if st.button("← start over"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.session_state.final_pick = None
        st.rerun()
