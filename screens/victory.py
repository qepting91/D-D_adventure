"""
Victory Screen - Quest Completion Celebration!
"""
import streamlit as st
from components import render_quest_card, render_hud
from state import (
    GameScreen,
    navigate_to,
    get_hero,
)


def render_victory_screen() -> None:
    """Render the victory/conclusion screen."""
    # Show final HUD
    render_hud()

    hero = get_hero()

    # Calculate achievements
    quests_completed = sum([
        hero.tavern_rated,
        hero.citadel_solved,
    ])

    # Victory message based on completion
    if quests_completed == 2:
        title = "LEGENDARY HERO!"
        subtitle = "All Quests Completed"
        desc = f"""Hail, <strong>{hero.name}</strong>!<br><br>
        You have proven yourself a true champion of the realm!
        The bards shall sing of your exploits for generations to come.<br><br>
        You conquered the Tavern's feast and unlocked the Citadel's vault.
        Your inventory overflows with treasures, and your name echoes through the land!<br><br>
        <strong>Final Stats:</strong><br>
        ⭐ Experience: {hero.xp} XP<br>
        💰 Gold: {hero.gold} coins<br>
        🎒 Items: {' '.join(hero.inventory)}<br><br>
        <em>The quest is complete. Until the next adventure...</em>"""
    elif quests_completed == 1:
        title = "BRAVE ADVENTURER!"
        subtitle = "Quest Survived"
        desc = f"""Well done, <strong>{hero.name}</strong>!<br><br>
        You have ventured forth and returned with tales to tell!
        Though some challenges remain unconquered, your courage is undeniable.<br><br>
        <strong>Final Stats:</strong><br>
        ⭐ Experience: {hero.xp} XP<br>
        💰 Gold: {hero.gold} coins<br>
        🎒 Items: {' '.join(hero.inventory)}<br><br>
        <em>Perhaps next time, you shall claim all the treasures...</em>"""
    else:
        title = "QUEST SURVIVED!"
        subtitle = "The Journey Continues"
        desc = f"""Greetings, <strong>{hero.name}</strong>!<br><br>
        You have explored the realm and lived to tell the tale!
        The path of adventure stretches ever onward.<br><br>
        <strong>Final Stats:</strong><br>
        ⭐ Experience: {hero.xp} XP<br>
        💰 Gold: {hero.gold} coins<br>
        🎒 Items: {' '.join(hero.inventory)}<br><br>
        <em>Every journey begins with a single step...</em>"""

    # Render victory card
    render_quest_card(
        icon="🏆",
        title=title,
        subtitle=subtitle,
        description=desc,
        image_path="images/optimized/adventure.webp",
    )

    # Celebration effects
    if quests_completed == 2:
        st.balloons()
        st.snow()

    st.write("")
    st.write("")

    # Thank you message
    st.markdown("### Thank You For Playing!")
    st.write("This adventure was crafted with magic and code.")

    st.write("")
    st.write("")

    # Play again button
    if st.button(
        "🔄 Start a New Adventure",
        use_container_width=True,
        type="primary",
        key="play_again_btn",
    ):
        # Reset the hero state for a new game
        st.session_state.clear()
        st.rerun()
