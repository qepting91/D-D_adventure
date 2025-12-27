"""
State management for The Hero's Quest.
Handles hero state, location tracking, and game progression.
"""
import streamlit as st
from dataclasses import dataclass, field
from enum import Enum
from typing import List


class GameScreen(Enum):
    """All possible screens/locations in the game."""
    WELCOME = "welcome"
    TAVERN = "tavern"
    CITADEL = "citadel"
    MAP = "map"
    LOCATION_DETAIL = "location_detail"
    VICTORY = "victory"


@dataclass
class HeroState:
    """Tracks all hero attributes and quest progress."""
    name: str = "Brave Adventurer"
    xp: int = 0
    xp_max: int = 100
    gold: int = 50
    inventory: List[str] = field(default_factory=lambda: ["🗡️", "🛡️"])

    # Quest completion flags
    tavern_rated: bool = False
    citadel_solved: bool = False


def init_state() -> None:
    """Initialize all session state variables. Call once at app start."""
    if "hero" not in st.session_state:
        st.session_state.hero = HeroState()

    if "current_screen" not in st.session_state:
        st.session_state.current_screen = GameScreen.WELCOME

    if "selected_map_location" not in st.session_state:
        st.session_state.selected_map_location = None

    # Navigation flag to prevent double-triggers
    if "nav_pending" not in st.session_state:
        st.session_state.nav_pending = None


def get_hero() -> HeroState:
    """Get the current hero state."""
    return st.session_state.hero


def get_current_screen() -> GameScreen:
    """Get the current screen."""
    return st.session_state.current_screen


def navigate_to(screen: GameScreen) -> None:
    """
    Navigate to a new screen.
    Uses a pending navigation pattern to avoid rerun loops.
    """
    if st.session_state.current_screen != screen:
        st.session_state.current_screen = screen
        st.rerun()


def set_hero_name(name: str) -> None:
    """Set the hero's name."""
    if name and name != st.session_state.hero.name:
        st.session_state.hero.name = name


def add_xp(amount: int) -> None:
    """Add XP to the hero, capped at max."""
    hero = st.session_state.hero
    hero.xp = min(hero.xp + amount, hero.xp_max)


def add_gold(amount: int) -> None:
    """Add or subtract gold (cannot go below 0)."""
    hero = st.session_state.hero
    hero.gold = max(0, hero.gold + amount)


def add_inventory_item(item: str) -> None:
    """Add an item to inventory if not already present."""
    hero = st.session_state.hero
    if item not in hero.inventory:
        hero.inventory.append(item)


def complete_tavern_quest() -> None:
    """Mark tavern quest as complete and grant rewards."""
    hero = st.session_state.hero
    if not hero.tavern_rated:
        hero.tavern_rated = True
        add_xp(10)
        add_gold(-10)
        add_inventory_item("🧀")


def complete_citadel_quest() -> None:
    """Mark citadel quest as complete and grant rewards."""
    hero = st.session_state.hero
    if not hero.citadel_solved:
        hero.citadel_solved = True
        add_gold(20)
        add_inventory_item("💎")


def set_selected_location(location: dict) -> None:
    """Set the currently selected map location."""
    st.session_state.selected_map_location = location


def get_selected_location() -> dict | None:
    """Get the currently selected map location."""
    return st.session_state.selected_map_location
