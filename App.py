import streamlit as st
import time

st.set_page_config(page_title="XMAS_TRIP.exe", page_icon="🎄", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'JetBrains Mono', monospace !important;
    background-color: #0d0d0d !important;
    color: #00ff88 !important;
}

.stApp { background-color: #0d0d0d; }

h1, h2, h3 { color: #00ff88 !important; font-family: 'JetBrains Mono', monospace !important; }

.terminal-box {
    background: #0d0d0d;
    border: 1px solid #00ff88;
    border-radius: 4px;
    padding: 20px 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    line-height: 1.8;
    color: #00ff88;
    margin-bottom: 16px;
    white-space: pre-wrap;
}

.terminal-box .dim { color: #2a7a4a; }
.terminal-box .gold { color: #d4a84b; }
.terminal-box .white { color: #f0eee8; }
.terminal-box .red { color: #ff4466; }
.terminal-box .cyan { color: #44ddff; }

.stRadio > div { gap: 8px; }
.stRadio label {
    font-family: 'JetBrains Mono', monospace !important;
    color: #00ff88 !important;
    font-size: 14px !important;
    cursor: pointer;
}
.stRadio > div > label:hover { color: #d4a84b !important; }

div[data-testid="stRadio"] > div { flex-direction: column; gap: 6px; }

.stButton > button {
    background: transparent !important;
    border: 1px solid #00ff88 !important;
    color: #00ff88 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 14px !important;
    border-radius: 2px !important;
    padding: 8px 24px !important;
    transition: all 0.2s;
}
.stButton > button:hover {
    background: #00ff8815 !important;
    border-color: #d4a84b !important;
    color: #d4a84b !important;
}

.stSelectbox > div > div {
    background: #0d0d0d !important;
    border: 1px solid #2a7a4a !important;
    color: #00ff88 !important;
    font-family: 'JetBrains Mono', monospace !important;
    border-radius: 2px !important;
}

.stSlider > div > div > div { background: #00ff88 !important; }

hr { border-color: #1a3a2a !important; }

.result-card {
    background: #0a1a10;
    border: 1px solid #d4a84b;
    border-radius: 4px;
    padding: 24px;
    margin-top: 16px;
    font-family: 'JetBrains Mono', monospace;
}

/* hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; max-width: 740px; }
</style>
""", unsafe_allow_html=True)

# ── State ──
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

def box(content):
    st.markdown(f'<div class="terminal-box">{content}</div>', unsafe_allow_html=True)

def advance():
    st.session_state.step += 1

# ── City data ──
CITIES = {
    "New York": {
        "emoji": "🗽",
        "tags": ["food", "nightlife", "culture", "walkable"],
        "weather": "cold",
        "vibe": "city",
        "desc": "Holiday windows on 5th Ave, Bryant Park ice rink, best food scene in the country.",
        "temp": "32–45°F",
        "flight": "~3h from Houston",
        "highlight": "You'll walk more in 3 days than you do in a month. Worth it.",
        "budget": "$$$$",
    },
    "Denver": {
        "emoji": "🏔️",
        "tags": ["outdoors", "food", "scenic", "skiing"],
        "weather": "cold",
        "vibe": "adventure",
        "desc": "Snow-capped Rockies backdrop, Christmas markets in LoDo, day-trip skiing in the mountains.",
        "temp": "20–45°F",
        "flight": "~2.5h from Houston",
        "highlight": "Wake up to actual snow on Christmas. Rare experience from Houston.",
        "budget": "$$$",
    },
    "Nashville": {
        "emoji": "🎸",
        "tags": ["nightlife", "food", "music", "walkable"],
        "weather": "mild",
        "vibe": "city",
        "desc": "Broadway neon at Christmas, live music every night, hot chicken, and a surprisingly great food scene.",
        "temp": "35–50°F",
        "flight": "~1.5h from Houston",
        "highlight": "Easiest logistics. Most fun per dollar.",
        "budget": "$$",
    },
    "Chicago": {
        "emoji": "🏙️",
        "tags": ["food", "culture", "nightlife", "architecture"],
        "weather": "cold",
        "vibe": "city",
        "desc": "Christkindlmarket (authentic German Christmas market), Magnificent Mile lights, world-class food.",
        "temp": "20–38°F",
        "flight": "~2.5h from Houston",
        "highlight": "The Christkindlmarket alone is worth the trip. Feels like Europe in December.",
        "budget": "$$$",
    },
    "Atlanta": {
        "emoji": "🍑",
        "tags": ["food", "culture", "nightlife", "easy"],
        "weather": "mild",
        "vibe": "city",
        "desc": "Centennial Park holiday lights, incredible restaurant scene, easy direct flight from Houston.",
        "temp": "38–55°F",
        "flight": "~2h from Houston",
        "highlight": "Underrated for food. Short flight. Good energy year-round.",
        "budget": "$$",
    },
    "New Orleans": {
        "emoji": "🎷",
        "tags": ["food", "nightlife", "culture", "music"],
        "weather": "mild",
        "vibe": "unique",
        "desc": "French Quarter decorated for Christmas, jazz clubs, the best eating city in America, period.",
        "temp": "48–62°F",
        "flight": "~1h from Houston",
        "highlight": "Closest trip that feels like you actually went somewhere. The food is unreal.",
        "budget": "$$",
    },
}

STEP = st.session_state.step
A = st.session_state.answers

# ══════════════════════════════
# STEP 0 — Boot screen
# ══════════════════════════════
if STEP == 0:
    box("""<span class="dim">──────────────────────────────────────────</span>
<span class="gold">  XMAS_TRIP.exe</span>  <span class="dim">v1.0.0 — by Marco</span>
<span class="dim">──────────────────────────────────────────</span>

  Initializing Christmas trip finder...
  <span class="dim">Loading cities.............. ✓</span>
  <span class="dim">Loading vibes............... ✓</span>
  <span class="dim">Loading your preferences.... ✓</span>

  Hey <span class="white">Angel</span> 👋
  Answer a few questions and I'll find
  the best city for us this Christmas.

<span class="dim">──────────────────────────────────────────</span>""")
    st.button(">> RUN PROGRAM", on_click=advance)

# ══════════════════════════════
# STEP 1 — Weather pref
# ══════════════════════════════
elif STEP == 1:
    box("""<span class="dim">[QUERY 1/4]</span> <span class="white">WEATHER PREFERENCE</span>

  It's December. You're leaving Houston.
  What are we working with?""")
    choice = st.radio("", [
        "❄️  Cold — I want actual winter",
        "🧥  Mild — cool but not freezing",
        "☀️  Warm — I don't do cold",
    ], label_visibility="collapsed")
    st.button(">> NEXT", on_click=lambda: (A.update({"weather": choice}), advance()))

# ══════════════════════════════
# STEP 2 — Top priority
# ══════════════════════════════
elif STEP == 2:
    box("""<span class="dim">[QUERY 2/4]</span> <span class="white">TOP PRIORITY</span>

  When you think about a great trip,
  what matters most?""")
    choice = st.radio("", [
        "🍽️  Food — we eat our way through every city",
        "🌙  Nightlife — we're going out",
        "🏔️  Outdoors — hiking, scenery, nature",
        "🎭  Culture — museums, architecture, history",
        "🎵  Music / Live entertainment",
    ], label_visibility="collapsed")
    st.button(">> NEXT", on_click=lambda: (A.update({"priority": choice}), advance()))

# ══════════════════════════════
# STEP 3 — Trip vibe
# ══════════════════════════════
elif STEP == 3:
    box("""<span class="dim">[QUERY 3/4]</span> <span class="white">TRIP ENERGY</span>

  What kind of trip are we going on?""")
    choice = st.radio("", [
        "🔥  Full send — packed itinerary, we sleep when we're home",
        "😌  Balanced — some plans, some wandering",
        "🛋️  Chill — good food, good vibes, no schedule",
    ], label_visibility="collapsed")
    st.button(">> NEXT", on_click=lambda: (A.update({"energy": choice}), advance()))

# ══════════════════════════════
# STEP 4 — NYC budget check
# ══════════════════════════════
elif STEP == 4:
    box("""<span class="dim">[QUERY 4/4]</span> <span class="white">THE NEW YORK QUESTION</span>

  I know you want New York.
  Be honest — are we doing it?""")
    choice = st.radio("", [
        "💸  Yes — we'll figure out the budget",
        "😭  I want to but... probably not this time",
        "🙅  No, let's find somewhere better",
    ], label_visibility="collapsed")
    st.button(">> COMPUTE RESULTS", on_click=lambda: (A.update({"nyc": choice}), advance()))

# ══════════════════════════════
# STEP 5 — Computing animation
# ══════════════════════════════
elif STEP == 5:
    box("""<span class="dim">Running algorithm...</span>
<span class="dim">Cross-referencing 6 cities...</span>
<span class="dim">Checking flights from Houston...</span>
<span class="dim">Calibrating vibe score...</span>""")
    time.sleep(0.5)
    st.session_state.step = 6
    st.rerun()

# ══════════════════════════════
# STEP 6 — Results
# ══════════════════════════════
elif STEP == 6:
    weather_pref = A.get("weather", "")
    priority = A.get("priority", "")
    energy = A.get("energy", "")
    nyc_ans = A.get("nyc", "")

    # Score cities
    scores = {city: 0 for city in CITIES}

    # Weather scoring
    if "Cold" in weather_pref:
        for c in ["New York", "Denver", "Chicago"]: scores[c] += 3
    elif "Mild" in weather_pref:
        for c in ["Nashville", "Atlanta", "New Orleans"]: scores[c] += 3
    elif "Warm" in weather_pref:
        for c in ["New Orleans", "Atlanta"]: scores[c] += 4
        scores["Nashville"] += 2

    # Priority scoring
    if "Food" in priority:
        for c, v in [("New Orleans",4),("Nashville",3),("Chicago",3),("Atlanta",3),("New York",2)]: scores[c] += v
    elif "Nightlife" in priority:
        for c, v in [("New Orleans",4),("Nashville",4),("New York",3),("Atlanta",2)]: scores[c] += v
    elif "Outdoors" in priority:
        scores["Denver"] += 5
    elif "Culture" in priority:
        for c, v in [("New York",4),("Chicago",3),("New Orleans",3)]: scores[c] += v
    elif "Music" in priority:
        for c, v in [("Nashville",5),("New Orleans",4),("Atlanta",2)]: scores[c] += v

    # Energy scoring
    if "Full send" in energy:
        for c in ["New York","Nashville","New Orleans"]: scores[c] += 2
    elif "Chill" in energy:
        for c in ["New Orleans","Denver","Atlanta"]: scores[c] += 2

    # NYC answer
    if "Yes" in nyc_ans:
        scores["New York"] += 6
    elif "probably not" in nyc_ans:
        scores["New York"] -= 2
    elif "No" in nyc_ans:
        scores["New York"] -= 10

    # Sort
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top = ranked[0][0]
    runner_up = ranked[1][0]
    third = ranked[2][0]

    top_data = CITIES[top]
    runner_data = CITIES[runner_up]

    box(f"""<span class="dim">────────────────────────────────────────</span>
<span class="gold">  RESULTS COMPUTED</span>
<span class="dim">────────────────────────────────────────</span>

  Processing complete. Based on your
  inputs, here's where we're going:""")

    st.markdown(f"""
<div class="result-card">
<div style="font-family:'JetBrains Mono',monospace; color:#d4a84b; font-size:11px; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:12px;">── #1 MATCH ──────────────────────────</div>
<div style="font-family:'JetBrains Mono',monospace; font-size:28px; color:#f0eee8; font-weight:700; margin-bottom:4px;">{top_data['emoji']} {top}</div>
<div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#2a7a4a; margin-bottom:14px;">{top_data['flight']} &nbsp;·&nbsp; {top_data['temp']} &nbsp;·&nbsp; {top_data['budget']}</div>
<div style="font-family:'JetBrains Mono',monospace; font-size:13px; color:#a0c8b0; line-height:1.7; margin-bottom:12px;">{top_data['desc']}</div>
<div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#d4a84b; border-top:1px solid #2a3a28; padding-top:10px;">💡 {top_data['highlight']}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div style="background:#0d0d0d; border:1px solid #1a3a2a; border-radius:4px; padding:16px 20px; margin-top:10px; font-family:'JetBrains Mono',monospace;">
<div style="color:#2a7a4a; font-size:11px; letter-spacing:0.1em; margin-bottom:10px;">── RUNNER UP ──</div>
<div style="color:#f0eee8; font-size:16px; font-weight:700; margin-bottom:4px;">{runner_data['emoji']} {runner_up}</div>
<div style="color:#2a7a4a; font-size:12px;">{runner_data['desc']}</div>
</div>
""", unsafe_allow_html=True)

    box(f"""<span class="dim">────────────────────────────────────────</span>
  Full ranking:
  <span class="gold">  1. {ranked[0][0]}</span>  <span class="dim">(score: {ranked[0][1]})</span>
  <span class="white">  2. {ranked[1][0]}</span>  <span class="dim">(score: {ranked[1][1]})</span>
  <span class="white">  3. {ranked[2][0]}</span>  <span class="dim">(score: {ranked[2][1]})</span>
  <span class="dim">  4. {ranked[3][0]}</span>  <span class="dim">(score: {ranked[3][1]})</span>
  <span class="dim">  5. {ranked[4][0]}</span>  <span class="dim">(score: {ranked[4][1]})</span>
  <span class="dim">  6. {ranked[5][0]}</span>  <span class="dim">(score: {ranked[5][1]})</span>
<span class="dim">────────────────────────────────────────</span>
  <span class="white">Program complete.</span> <span class="gold">Marco handles the rest. 🎄</span>
<span class="dim">────────────────────────────────────────</span>""")

    if st.button(">> RUN AGAIN"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()
