"""
The Hero's Quest - Main Application Entry Point
================================================
A magical D&D-themed adventure app for young heroes.

Built with Streamlit 1.52+
"""
import streamlit as st

# --- PAGE CONFIGURATION (must be first Streamlit command) ---
st.set_page_config(
    page_title="The Hero's Quest",
    page_icon="⚔️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- IMPORTS (after page config) ---
from styles import inject_css
from state import init_state, get_current_screen, GameScreen
from screens import (
    render_welcome_screen,
    render_tavern_screen,
    render_citadel_screen,
    render_map_screen,
    render_location_detail_screen,
    render_victory_screen,
)


def main() -> None:
    """Main application entry point."""
    # Initialize state
    init_state()

    # Inject CSS styles
    inject_css()

    # Get current screen
    current_screen = get_current_screen()

    # Route to appropriate screen
    if current_screen == GameScreen.WELCOME:
        render_welcome_screen()

    elif current_screen == GameScreen.TAVERN:
        render_tavern_screen()

    elif current_screen == GameScreen.CITADEL:
        render_citadel_screen()

    elif current_screen == GameScreen.MAP:
        render_map_screen()

    elif current_screen == GameScreen.LOCATION_DETAIL:
        render_location_detail_screen()

    elif current_screen == GameScreen.VICTORY:
        render_victory_screen()

    else:
        # Fallback - should never happen
        st.error("Unknown screen! Returning to welcome...")
        render_welcome_screen()


if __name__ == "__main__":
    main()
