"""
Citadel Screen - The Citadel of Silicon.
Quest: Solve the rune puzzle to unlock the vault.
"""
import streamlit as st
from config import QUEST_DATA, CITADEL_PUZZLE_SOLUTION, CITADEL_PUZZLE_OPTIONS
from components import render_quest_card, render_hud
from state import (
    GameScreen,
    navigate_to,
    get_hero,
    complete_citadel_quest,
)


def render_citadel_screen() -> None:
    """Render the citadel screen with puzzle quest."""
    # Show HUD
    render_hud()

    data = QUEST_DATA["citadel"]
    hero = get_hero()

    # Render the quest card
    render_quest_card(
        icon="💻",
        title=data["title"],
        subtitle=f"{data['realName']} | {data['type']}",
        description=data["desc"],
        image_path="images/optimized/armory.webp",
        address=data["address"],
    )

    st.write("")  # Spacer

    # --- Quest: Solve the Rune Puzzle ---
    if not hero.citadel_solved:
        st.markdown("### 🔐 Quest: Unlock the Vault!")
        st.write("Select the **Power Runes** to open the treasure vault.")
        st.write("*Hint: You need Lightning and Memory...*")

        st.write("")  # Spacer

        # Use segmented control for puzzle
        selected_runes = st.segmented_control(
            "Choose the runes:",
            options=CITADEL_PUZZLE_OPTIONS,
            selection_mode="multi",
            key="citadel_rune_puzzle",
        )

        st.write("")  # Spacer

        # Check solution button
        if st.button("🔓 Try Combination", use_container_width=True, key="try_puzzle"):
            if selected_runes and set(selected_runes) == CITADEL_PUZZLE_SOLUTION:
                complete_citadel_quest()
                st.snow()
                st.success("🎉 THE VAULT OPENS!")
                st.info("You found **+20 Gold** and a **Crystal Gem** 💎!")
                st.rerun()  # Rerun to update HUD
            elif selected_runes:
                st.warning("The runes glow... but the combination is wrong. Try again!")
            else:
                st.error("Select some runes first!")
    else:
        st.success("✅ Quest Complete! The vault has been opened!")
        st.write("You found **+20 Gold** and received a **Crystal Gem** 💎")

    st.write("")  # Spacer
    st.write("")  # Extra spacer

    # --- Navigation ---
    st.markdown("### Where to next?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Back to Tavern", use_container_width=True, key="citadel_back"):
            navigate_to(GameScreen.TAVERN)

    with col2:
        if st.button("To The Map ➡️", use_container_width=True, key="citadel_next"):
            navigate_to(GameScreen.MAP)
