"""
CSS styles for The Hero's Quest.
Glassmorphism theme with dark fantasy aesthetics.
"""
import streamlit as st


def get_css() -> str:
    """Returns the complete CSS for the application."""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Lato:wght@400;700&display=swap');

    /* === GLOBAL STYLES === */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
    }

    div.block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    /* === QUEST CARD (Glassmorphism) === */
    .quest-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        color: #ffffff;
    }

    .quest-card h1 {
        font-family: 'Cinzel', serif;
        color: #ffd700;
        text-align: center;
        font-size: 26px;
        margin-bottom: 5px;
        margin-top: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    .quest-card h3 {
        font-family: 'Lato', sans-serif;
        color: #a0d2eb;
        text-align: center;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 0;
        margin-bottom: 15px;
    }

    .quest-card p {
        font-family: 'Lato', sans-serif;
        font-size: 15px;
        line-height: 1.6;
        color: #e0e0e0;
        margin-bottom: 15px;
    }

    .quest-card hr {
        border: none;
        border-top: 1px solid rgba(255, 215, 0, 0.3);
        margin: 15px 0;
    }

    /* === ICON HEADER === */
    .icon-header {
        text-align: center;
        font-size: 50px;
        margin-bottom: 10px;
        filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.5));
    }

    /* === QUEST IMAGE === */
    .quest-image {
        width: 100%;
        border-radius: 15px;
        border: 2px solid rgba(255, 215, 0, 0.3);
        margin-bottom: 15px;
        display: block;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* === ADDRESS BOX === */
    .address-box {
        background: rgba(255, 215, 0, 0.15);
        border: 1px solid rgba(255, 215, 0, 0.4);
        padding: 12px;
        text-align: center;
        font-family: monospace;
        font-weight: bold;
        color: #ffd700;
        border-radius: 10px;
        margin-top: 15px;
        transition: all 0.3s ease;
    }

    .address-box:hover {
        background: rgba(255, 215, 0, 0.25);
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
    }

    .address-box span {
        font-size: 11px;
        color: #a0d2eb;
    }

    /* === HUD (Heads-Up Display) === */
    .hud-container {
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 215, 0, 0.3);
    }

    .hud-name {
        font-family: 'Cinzel', serif;
        color: #ffd700;
        text-align: center;
        font-size: 20px;
        margin: 0 0 10px 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    .hud-stats {
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
    }

    .hud-stat {
        text-align: center;
        color: #e0e0e0;
        font-family: 'Lato', sans-serif;
    }

    .hud-stat-value {
        font-size: 22px;
        font-weight: bold;
        color: #ffd700;
    }

    .hud-stat-label {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #a0d2eb;
    }

    /* === XP BAR === */
    .xp-bar-container {
        width: 100%;
        background: rgba(0, 0, 0, 0.4);
        border-radius: 10px;
        height: 18px;
        overflow: hidden;
        margin-top: 10px;
        border: 1px solid rgba(255, 215, 0, 0.3);
    }

    .xp-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #4CAF50, #8BC34A);
        border-radius: 10px;
        transition: width 0.5s ease;
        box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
    }

    .xp-bar-text {
        text-align: center;
        font-size: 10px;
        color: #a0d2eb;
        margin-top: 5px;
        font-family: 'Lato', sans-serif;
    }

    /* === INVENTORY ROW === */
    .inventory-row {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 10px;
        font-size: 22px;
    }

    /* === GLOBAL TEXT COLOR FIX === */
    /* Make all text white on the dark background */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp div {
        color: #ffffff;
    }

    /* Markdown text */
    .stMarkdown, .stMarkdown p, .stMarkdown span {
        color: #ffffff !important;
    }

    /* Headers outside cards */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #ffd700 !important;
    }

    /* Info/Success/Warning boxes - ensure readable */
    [data-testid="stAlert"] {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
    }

    [data-testid="stAlert"] p {
        color: #ffffff !important;
    }

    /* Caption and small text */
    .stCaption, small {
        color: #a0d2eb !important;
    }

    /* === HIDE STREAMLIT ELEMENTS === */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* === BUTTON STYLING === */
    .stButton > button {
        font-family: 'Cinzel', serif !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        border: 2px solid rgba(255, 215, 0, 0.5) !important;
        background: rgba(139, 0, 0, 0.8) !important;
        color: #ffd700 !important;
    }

    .stButton > button:hover {
        background: rgba(139, 0, 0, 1) !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4) !important;
    }

    /* === PILLS STYLING === */
    [data-testid="stPills"] > div {
        gap: 8px;
    }

    [data-testid="stPills"] button {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        color: #e0e0e0 !important;
        border-radius: 20px !important;
        font-family: 'Lato', sans-serif !important;
    }

    [data-testid="stPills"] button[aria-pressed="true"] {
        background: rgba(255, 215, 0, 0.3) !important;
        border: 2px solid #ffd700 !important;
        color: #ffd700 !important;
    }

    /* === SEGMENTED CONTROL === */
    [data-testid="stSegmentedControl"] button {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        color: #e0e0e0 !important;
    }

    [data-testid="stSegmentedControl"] button[aria-pressed="true"] {
        background: rgba(255, 215, 0, 0.4) !important;
        border: 2px solid #ffd700 !important;
        color: #ffd700 !important;
    }

    /* === FEEDBACK STARS === */
    [data-testid="stFeedback"] {
        justify-content: center;
    }

    /* === AUDIO INPUT === */
    [data-testid="stAudioInput"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 10px;
    }

    /* === LINK BUTTON === */
    .stLinkButton > a {
        background: linear-gradient(135deg, #ffd700 0%, #ff8c00 100%) !important;
        color: #1a1a2e !important;
        font-weight: bold !important;
        border-radius: 12px !important;
    }

    /* === SUCCESS/WARNING MESSAGES === */
    .stSuccess, .stWarning {
        border-radius: 10px !important;
    }
    </style>
    """


def inject_css() -> None:
    """Inject the CSS into the Streamlit app."""
    st.html(get_css())
