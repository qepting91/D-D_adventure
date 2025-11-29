import streamlit as st
import urllib.parse
import base64
import os

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Date Night Quest",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- PERFORMANCE: CACHED ASSET LOADING ---


@st.cache_data
def get_base64_image(image_path):
    """Converts a local image file to a base64 string so it can be embedded in HTML."""
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- CSS STYLING ---


@st.cache_data
def get_css():
    return """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Lato:wght@400;700&display=swap');

        /* 1. Global Reset */
        .stApp {
            background-color: #000000;
        }
        
        /* 2. The Card Container */
        .quest-card {
            background-color: #fdf6e3; 
            border: 2px solid #b58900; 
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 1rem;
            box-shadow: 0 0 15px rgba(181, 137, 0, 0.2);
            color: #002b36; 
        }

        /* 3. Typography within the Card */
        .quest-card h1 {
            font-family: 'Cinzel', serif;
            color: #8b0000;
            text-align: center;
            font-size: 28px;
            margin-bottom: 5px;
            margin-top: 0;
        }
        
        .quest-card h3 {
            font-family: 'Lato', sans-serif;
            color: #586e75;
            text-align: center;
            font-size: 16px;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 0;
            margin-bottom: 20px;
        }

        .quest-card p {
            font-family: 'Lato', sans-serif;
            font-size: 18px;
            line-height: 1.6;
            color: #073642; 
            margin-bottom: 15px;
        }

        /* 4. Address Box */
        .address-box {
            background-color: #eee8d5;
            border: 1px dashed #93a1a1;
            padding: 12px;
            text-align: center;
            font-family: monospace;
            font-weight: bold;
            color: #000;
            border-radius: 8px;
            margin-top: 20px;
        }

        /* 5. Icon Header */
        .icon-header {
            text-align: center;
            font-size: 40px;
            margin-bottom: 10px;
        }
        
        /* 6. Image Styling within Card */
        .quest-image {
            width: 100%;
            border-radius: 10px;
            border: 2px solid #b58900;
            margin-bottom: 20px;
            display: block;
        }

        /* 7. Button Styling */
        div[data-testid="column"] button, .stButton button {
            width: 100%;
            border-radius: 8px;
            height: auto;
            min-height: 3.5rem;
            font-weight: bold;
            font-family: 'Cinzel', serif;
            font-size: 1.1rem;
            white-space: normal;
            padding: 10px;
        }
        
        .stButton > button {
             border: 2px solid #b58900;
             color: white;
             background-color: #8b0000;
        }
        
        .stButton > button:active {
            transform: scale(0.98);
        }

        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        </style>
    """


st.markdown(get_css(), unsafe_allow_html=True)

# --- DATA STRUCTURES ---
QUEST_DATA = {
    "intro": {
        "title": "The Kids-Free Campaign",
        "subtitle": "A Quest for Food, Loot, and Leisure",
        "text": """Greetings, Adventurers.<br><br>
        You have been granted a rare boon: The Grand Guardians have accepted custody of the chaotic goblin-kin that inhabit your keep, buying you a temporary reprieve from your duties as Wardens of the House.<br><br>
        A scroll of 'Free Time' has been activated, but its magic is fleeting—lasting only from High Noon until the Fifth Bell (12:00 PM – 5:00 PM).<br><br>
        Be warned: The winds outside bite with the Frost of November, and the Lady takes <strong>Double Damage from Cold</strong>. Therefore, your path must cleave to the warm sanctuaries of the Stone-Halls.<br><br>
        Your mission is threefold:<br>
        • Restore your Mana.<br>
        • Acquire legendary loot.<br>
        • Feast without having to cut up anyone else's food.<br><br>
        Your quest begins now. Do not squander it.""",
        "button": "Begin Adventure"
    },
    "tavern": {
        "title": "The Bulldog Tavern",
        "realName": "The British Bulldog Pub",
        "type": "Tavern",
        "desc": "Start your journey here. A dark, wooden sanctuary serving heavy comforts from the old world. Feast on Fish & Chips or Bangers & Mash to bolster your constitution.",
        "address": "1220 Bower Pkwy E-10, Columbia, SC 29212",
        "nextBtn": "To The Armory"
    },
    "armory": {
        "title": "The Firefly Armory",
        "realName": "Firefly Toys & Games",
        "type": "Loot Shop",
        "desc": "The finest purveyor of dice, miniatures, and tomes in the realm. Here you shall equip yourselves. Browse the wall of math rocks and perhaps acquire a new manual for your next campaign.",
        "address": "736 St Andrews Rd C, Columbia, SC 29210",
        "nextBtn": "To The Map"
    }
}

LOCATIONS = [
    {
        "id": 'target',
        "fantasyName": "The Red Bullseye Market",
        "realName": "Target (Harbison)",
        "desc": "A sprawling temple of the merchant gods, marked by the Sigil of the Red Eye. It is a place of dangerous enchantment known as the 'Target Effect'—where an adventurer enters seeking a single potion of cleansing, yet departs with a cart full of garments, strange artifacts, and snacks, their gold purse mysteriously lightened. Requires a high Will Save to resist.",
        "address": "200 Harbison Blvd, Columbia, SC 29212",
        "type": "General Goods",
        "icon": "🛍️"
    },
    {
        "id": 'worldmarket',
        "fantasyName": "The Bazaar of Many Worlds",
        "realName": "World Market",
        "desc": "A trading post gathering wares from the Seven Seas. Here, you shall find furniture carved from exotic acacia, wines from Elven vineyards, and strange confections from the Far East. It is a sensory delight for the weary traveler looking to stock their larder with rare ingredients.",
        "address": "278 Harbison Blvd, Columbia, SC 29212",
        "type": "Exotic Goods",
        "icon": "🗺️"
    },
    {
        "id": '2ndcharles',
        "fantasyName": "The Archives of Charles",
        "realName": "2nd & Charles",
        "desc": "A massive, labyrinthine repository of forgotten lore. Adventurers travel here to trade their old scrolls for credit. From the Bardic Vinyls of the 1980s to the Manga Chronicles of the East, it is a dungeon where hours vanish like smoke. Beware the 'Bin of Clearance'—it is a trap for time.",
        "address": "275-1 Harbison Blvd, Columbia, SC 29212",
        "type": "Tomes & Relics",
        "icon": "📖"
    },
    {
        "id": 'barnes',
        "fantasyName": "The Grand Athenaeum",
        "realName": "Barnes & Noble",
        "desc": "A sanctuary of silence and the aroma of roasted beans. Rows upon rows of pristine, unread parchment await the scholar. It is said the Starbucks Oracle resides within, dispensing hot elixirs of caffeine that grant +2 to Intelligence checks for one hour.",
        "address": "3400 Forest Dr, Columbia, SC 29204",
        "type": "Library",
        "icon": "📜"
    },
    {
        "id": 'heroes',
        "fantasyName": "The Hall of Heroes & Wyrms",
        "realName": "Heroes & Dragons",
        "desc": "A time-capsule dungeon filled with the relics of your childhood. Behold the Plastic Golems (Action Figures) and the Graphic Sagas of the Super-Men. It is a place of heavy nostalgia, where one might reclaim the treasures once lost to the mimic known as 'The Garage Sale'.",
        "address": "1807 Bush River Rd Suite E, Columbia, SC 29210",
        "type": "Vintage Loot",
        "icon": "🛡️"
    },
    {
        "id": 'hobby',
        "fantasyName": "The Guildhall of Artificers",
        "realName": "Hobby Lobby",
        "desc": "Do you seek to forge your own decorations? Here lie the raw materials: glues, pigments, and the fabled 'Live Laugh Love' runes. The Seasonal Wing is currently possessed by the Spirit of Yule—enter only if you have room in your inventory for 1,000 ornaments.",
        "address": "254 Harbison Blvd, Columbia, SC 29212",
        "type": "Crafting Mats",
        "icon": "✨"
    },
    {
        "id": 'antique',
        "fantasyName": "The Ruins of the Old Mill",
        "realName": "Old Mill Antique Mall",
        "desc": "A sprawling labyrinth of the Ancients located across the river. Scavenge through booths of forgotten heirlooms, cursed mirrors, and furniture of solid oak. It is a place for the patient hunter; true treasure lies beneath layers of dust and history.",
        "address": "310 State St A, West Columbia, SC 29169",
        "type": "Ancient Artifacts",
        "icon": "👻"
    },
    {
        "id": 'kirkland',
        "fantasyName": "The Sanctuary of Scents",
        "realName": "Kirkland's Home",
        "desc": "Before you even cross the threshold, the aroma of Cinnamon Brooms strikes you for 1d4 olfactory damage. This is the domain of the High Matrons, filled with soft textiles, warm light, and oversized clocks to ensure your keep feels like a fortress of comfort.",
        "address": "242 Harbison Blvd, Columbia, SC 29212",
        "type": "Keep Decor",
        "icon": "❤️"
    },
    {
        "id": 'wine',
        "fantasyName": "The Alchemist's Vast Cellar",
        "realName": "Total Wine & More",
        "desc": "A dungeon lined not with monsters, but with bottles. Here you will find the Water of Life, the Elven Meads, and the Dwarven Stouts. Stock your party's inventory for the long winter nights ahead. (Warning: Consuming potions may result in -2 Dexterity).",
        "address": "276-1 Harbison Blvd, Columbia, SC 29212",
        "type": "Potions",
        "icon": "🍷"
    },
    {
        "id": 'nifty',
        "fantasyName": "The Village Trading Post",
        "realName": "The Nifty Gifty",
        "desc": "A charming establishment run by the locals of Chapin. It holds unique trinkets and handcrafted boons not found in the Big City markets. The perfect final stop to spend your remaining gold before returning to your own castle.",
        "address": "104 Andrew Corley Rd, Lexington, SC 29072",
        "type": "Local Wares",
        "icon": "👑"
    }
]

# --- STATE MANAGEMENT ---
if 'step' not in st.session_state:
    st.session_state.step = 'intro'
if 'selected_loc' not in st.session_state:
    st.session_state.selected_loc = None


def set_step(new_step):
    st.session_state.step = new_step
    st.rerun()


def go_to_location(loc):
    st.session_state.selected_loc = loc
    st.session_state.step = 'location_detail'
    st.rerun()

# --- HELPER: RENDER CARD ---


def render_quest_card(icon, title, subtitle, desc, address=None, image_path=None):
    # We build the HTML as a list of strings and join them.
    # This prevents Python's indentation from being included in the HTML string,
    # which fixes the issue where Streamlit thinks it's a code block.

    html_content = [f'<div class="quest-card">']
    html_content.append(f'<div class="icon-header">{icon}</div>')
    html_content.append(f'<h1>{title}</h1>')
    html_content.append(f'<h3>{subtitle}</h3>')

    if image_path:
        img_b64 = get_base64_image(image_path)
        if img_b64:
            html_content.append(
                f'<img src="data:image/png;base64,{img_b64}" class="quest-image">')

    html_content.append(
        '<hr style="border-color: #b58900; opacity: 0.3; margin: 15px 0;">')
    html_content.append(f'<p>{desc}</p>')

    if address:
        encoded_addr = urllib.parse.quote(address)
        waze_url = f"https://waze.com/ul?q={encoded_addr}&navigate=yes"
        html_content.append(
            f'<a href="{waze_url}" target="_blank" style="text-decoration:none;"><div class="address-box">📍 {address}<br><span style="font-size: 12px; color: #8b0000; text-transform: uppercase;">(Tap to Navigate in Waze)</span></div></a>')

    html_content.append('</div>')

    # Join everything into one long string with no indentation
    final_html = "".join(html_content)

    st.markdown(final_html, unsafe_allow_html=True)

# --- HELPER: NAVIGATION BUTTONS ---


def nav_buttons(back_target, next_target, next_label="Next"):
    col1, col2 = st.columns([1, 2])
    with col1:
        if back_target:
            if st.button("⬅ Back"):
                set_step(back_target)
    with col2:
        if next_target:
            if st.button(f"{next_label} ➡"):
                set_step(next_target)

# --- APP FLOW ---


# 1. INTRO
if st.session_state.step == 'intro':
    data = QUEST_DATA['intro']
    render_quest_card(
        icon="👑",
        title=data['title'],
        subtitle=data['subtitle'],
        desc=data['text'],
        image_path="images/optimized/adventure.webp"
    )
    if st.button(data['button'], use_container_width=True):
        set_step('tavern')

# 2. TAVERN
elif st.session_state.step == 'tavern':
    data = QUEST_DATA['tavern']
    render_quest_card(
        icon="🍺",
        title=data['title'],
        subtitle=f"{data['realName']} | {data['type']}",
        desc=data['desc'],
        address=data['address'],
        image_path="images/optimized/tavern.webp"
    )
    nav_buttons(back_target='intro', next_target='armory',
                next_label=data['nextBtn'])

# 3. ARMORY
elif st.session_state.step == 'armory':
    data = QUEST_DATA['armory']
    render_quest_card(
        icon="⚔️",
        title=data['title'],
        subtitle=f"{data['realName']} | {data['type']}",
        desc=data['desc'],
        address=data['address'],
        image_path="images/optimized/armory.webp"
    )
    nav_buttons(back_target='tavern', next_target='map',
                next_label=data['nextBtn'])

# 4. MAP (THE MENU)
elif st.session_state.step == 'map':
    render_quest_card(
        icon="🧭",
        title="Where does the adventure take you now?",
        subtitle="The path is yours to choose",
        desc="Select a destination from the list below to reveal its secrets.",
        image_path="images/optimized/map.webp"
    )

    # Back button to Armory
    if st.button("⬅ Back to Armory"):
        set_step('armory')

    st.write("")  # Spacer

    # Render a button for each location
    for loc in LOCATIONS:
        # We use a unique key for each button to avoid conflicts
        if st.button(f"{loc['icon']}  {loc['fantasyName']}", key=loc['id'], use_container_width=True):
            go_to_location(loc)

# 5. LOCATION DETAIL (THE REVEAL)
elif st.session_state.step == 'location_detail':
    loc = st.session_state.selected_loc

    render_quest_card(
        icon=loc['icon'],
        title=loc['fantasyName'],
        subtitle=loc['realName'],
        desc=loc['desc'],
        address=loc['address']
    )

    if st.button("⬅ Return to the Path", use_container_width=True):
        set_step('map')
