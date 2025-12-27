"""
Screen modules for The Hero's Quest.
Each screen is a separate module for clean separation of concerns.
"""
from screens.welcome import render_welcome_screen
from screens.tavern import render_tavern_screen
from screens.citadel import render_citadel_screen
from screens.map import render_map_screen
from screens.location_detail import render_location_detail_screen
from screens.victory import render_victory_screen

__all__ = [
    "render_welcome_screen",
    "render_tavern_screen",
    "render_citadel_screen",
    "render_map_screen",
    "render_location_detail_screen",
    "render_victory_screen",
]
