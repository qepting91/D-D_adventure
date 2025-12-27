"""
Map Screen - The Scroll of Destiny.
Browse and select additional locations.
"""
import streamlit as st
from config import MAP_LOCATIONS
from components import render_quest_card, render_hud
from state import (
    GameScreen,
    navigate_to,
    set_selected_location,
)


def render_map_screen() -> None:
    """Render the map screen with location selection."""
    # Show HUD
    render_hud()

    # Render the quest card
    render_quest_card(
        icon="🧭",
        title="The Scroll of Destiny",
        subtitle="Where does the adventure take you?",
        description="Select a destination from the mystical list below to reveal its secrets...",
        image_path="images/optimized/map.webp",
    )

    # Back navigation
    if st.button("⬅️ Back to Citadel", use_container_width=True, key="map_back"):
        navigate_to(GameScreen.CITADEL)

    st.write("")  # Spacer
    st.markdown("### 📍 Choose Your Destination")
    st.write("")  # Spacer

    # Create a grid of location buttons
    # Use 2 columns for better mobile display
    col1, col2 = st.columns(2)

    for i, location in enumerate(MAP_LOCATIONS):
        # Alternate between columns
        col = col1 if i % 2 == 0 else col2

        with col:
            button_label = f"{location['icon']} {location['fantasyName']}"
            if st.button(
                button_label,
                use_container_width=True,
                key=f"loc_{location['id']}",
            ):
                set_selected_location(location)
                navigate_to(GameScreen.LOCATION_DETAIL)

    # Spacer
    st.write("")
    st.write("")

    # Complete Quest button
    st.markdown("### Ready to end your adventure?")
    if st.button(
        "🏆 Complete the Quest!",
        use_container_width=True,
        type="primary",
        key="complete_quest_btn",
    ):
        navigate_to(GameScreen.VICTORY)
