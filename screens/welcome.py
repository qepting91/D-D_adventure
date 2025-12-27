"""
Welcome Screen - Hero name selection and adventure start.
"""
import streamlit as st
from config import QUEST_DATA, HERO_NAMES
from components import render_quest_card
from state import (
    GameScreen,
    navigate_to,
    set_hero_name,
    get_hero,
)


def render_welcome_screen() -> None:
    """Render the welcome/intro screen."""
    data = QUEST_DATA["welcome"]

    # Render the quest card
    render_quest_card(
        icon="👑",
        title=data["title"],
        subtitle=data["subtitle"],
        description=data["text"],
        image_path="images/optimized/adventure.webp",
    )

    st.write("")  # Spacer

    # --- Hero Name Selection ---
    st.markdown("### Choose Your Hero Name")

    # Use pills for name selection
    selected_name = st.pills(
        "Select a name:",
        options=HERO_NAMES,
        selection_mode="single",
        key="hero_name_selection",
    )

    # Update hero name when selection changes
    if selected_name:
        set_hero_name(selected_name)
        st.success(f"You shall be known as **{selected_name}**!")

    st.write("")  # Spacer

    # --- Audio Input (Pretend Mode) ---
    st.markdown("##### ...or speak your name:")
    audio_data = st.audio_input(
        "Record your heroic name!",
        key="hero_audio_input",
    )

    if audio_data:
        # Pretend transcription
        set_hero_name("Legendary Champion")
        st.success("The winds whisper... **Legendary Champion** has arrived!")
        st.balloons()

    st.write("")  # Spacer
    st.write("")  # Extra spacer

    # --- Begin Adventure Button ---
    # Show current hero name
    hero = get_hero()
    st.info(f"Current hero: **{hero.name}**")

    if st.button(
        f"⚔️ {data['button']} ⚔️",
        use_container_width=True,
        type="primary",
        key="begin_adventure_btn",
    ):
        navigate_to(GameScreen.TAVERN)
