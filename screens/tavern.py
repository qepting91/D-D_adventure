"""
Tavern Screen - The British Bulldog Pub.
Quest: Rate the feast to earn XP.
"""
import streamlit as st
from config import QUEST_DATA
from components import render_quest_card, render_hud, navigation_buttons
from state import (
    GameScreen,
    navigate_to,
    get_hero,
    complete_tavern_quest,
)


def render_tavern_screen() -> None:
    """Render the tavern screen with rating quest."""
    # Show HUD
    render_hud()

    data = QUEST_DATA["tavern"]
    hero = get_hero()

    # Render the quest card
    render_quest_card(
        icon="🍺",
        title=data["title"],
        subtitle=f"{data['realName']} | {data['type']}",
        description=data["desc"],
        image_path="images/optimized/tavern.webp",
        address=data["address"],
    )

    st.write("")  # Spacer

    # --- Quest: Rate the Feast ---
    if not hero.tavern_rated:
        st.markdown("### 🍕 Quest: Rate the Feast!")
        st.write("How many stars does the **Potion of Mac 'n Cheese** deserve?")

        rating = st.feedback("stars", key="tavern_food_rating")

        if rating is not None:
            complete_tavern_quest()
            st.balloons()
            st.success(f"You rated it {rating + 1} stars! +10 XP earned!")
            st.info("The Cheese Blessing 🧀 has been added to your inventory!")
            st.rerun()  # Rerun to update HUD
    else:
        st.success("✅ Quest Complete! You enjoyed the feast!")
        st.write("You earned **+10 XP** and received the **Cheese Blessing** 🧀")

    st.write("")  # Spacer
    st.write("")  # Extra spacer

    # --- Navigation ---
    st.markdown("### Where to next?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Back to Start", use_container_width=True, key="tavern_back"):
            navigate_to(GameScreen.WELCOME)

    with col2:
        if st.button("To The Citadel ➡️", use_container_width=True, key="tavern_next"):
            navigate_to(GameScreen.CITADEL)
