"""
Reusable UI components for The Hero's Quest.
"""
import streamlit as st
import urllib.parse
import base64
import os
from state import get_hero


@st.cache_data
def load_image_base64(image_path: str) -> str | None:
    """Load an image and convert to base64 for embedding."""
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_hud() -> None:
    """
    Render the Heads-Up Display showing hero stats.
    Shows: Name, Gold, XP bar, Inventory
    """
    hero = get_hero()
    xp_percent = (hero.xp / hero.xp_max) * 100

    hud_html = f'''
    <div class="hud-container">
        <div class="hud-name">⚔️ {hero.name} ⚔️</div>
        <div class="hud-stats">
            <div class="hud-stat">
                <div class="hud-stat-value">💰 {hero.gold}</div>
                <div class="hud-stat-label">Gold</div>
            </div>
            <div class="hud-stat">
                <div class="hud-stat-value">⭐ {hero.xp}</div>
                <div class="hud-stat-label">Experience</div>
            </div>
        </div>
        <div class="xp-bar-container">
            <div class="xp-bar-fill" style="width: {xp_percent}%;"></div>
        </div>
        <div class="xp-bar-text">XP: {hero.xp} / {hero.xp_max}</div>
        <div class="inventory-row">
            {"".join(hero.inventory)}
        </div>
    </div>
    '''
    st.html(hud_html)


def render_quest_card(
    icon: str,
    title: str,
    subtitle: str,
    description: str,
    image_path: str | None = None,
    address: str | None = None
) -> None:
    """
    Render a glassmorphism quest card.

    Args:
        icon: Emoji icon to display at top
        title: Main title text
        subtitle: Smaller subtitle text
        description: Body text (can contain HTML)
        image_path: Optional path to image file
        address: Optional address (makes it clickable for maps)
    """
    html_parts = ['<div class="quest-card">']

    # Icon
    html_parts.append(f'<div class="icon-header">{icon}</div>')

    # Title and subtitle
    html_parts.append(f'<h1>{title}</h1>')
    html_parts.append(f'<h3>{subtitle}</h3>')

    # Image (if provided)
    if image_path:
        img_b64 = load_image_base64(image_path)
        if img_b64:
            html_parts.append(
                f'<img src="data:image/webp;base64,{img_b64}" class="quest-image" alt="{title}">'
            )

    # Divider
    html_parts.append('<hr>')

    # Description
    html_parts.append(f'<p>{description}</p>')

    # Address with map link (if provided)
    if address:
        encoded = urllib.parse.quote(address)
        maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded}"
        html_parts.append(f'''
        <a href="{maps_url}" target="_blank" style="text-decoration: none;">
            <div class="address-box">
                📍 {address}<br>
                <span>(Tap to Open Map)</span>
            </div>
        </a>
        ''')

    html_parts.append('</div>')

    st.html("".join(html_parts))


def navigation_buttons(
    back_label: str | None = None,
    back_screen=None,
    next_label: str | None = None,
    next_screen=None
) -> None:
    """
    Render navigation buttons.

    Args:
        back_label: Text for back button (None to hide)
        back_screen: GameScreen to navigate to on back
        next_label: Text for next button (None to hide)
        next_screen: GameScreen to navigate to on next
    """
    from state import navigate_to

    col1, col2 = st.columns(2)

    with col1:
        if back_label and back_screen:
            if st.button(f"⬅️ {back_label}", use_container_width=True):
                navigate_to(back_screen)

    with col2:
        if next_label and next_screen:
            if st.button(f"{next_label} ➡️", use_container_width=True):
                navigate_to(next_screen)
