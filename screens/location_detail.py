"""
Location Detail Screen - Shows details of a selected map location.
"""
import streamlit as st
from components import render_quest_card, render_hud
from state import (
    GameScreen,
    navigate_to,
    get_selected_location,
)


def render_location_detail_screen() -> None:
    """Render the details of a selected location."""
    # Show HUD
    render_hud()

    location = get_selected_location()

    # Safety check - go back to map if no location selected
    if not location:
        navigate_to(GameScreen.MAP)
        return

    # Render the quest card with location details
    render_quest_card(
        icon=location["icon"],
        title=location["fantasyName"],
        subtitle=f"{location['realName']} | {location['type']}",
        description=location["desc"],
        address=location["address"],
    )

    st.write("")  # Spacer
    st.write("")  # Extra spacer

    # Return to map button
    if st.button(
        "⬅️ Return to the Map",
        use_container_width=True,
        type="primary",
        key="location_back",
    ):
        navigate_to(GameScreen.MAP)
