"""
Configuration and data constants for The Hero's Quest.
"""

# Hero name options for the welcome screen
HERO_NAMES = ["Brave Knight", "Mighty Wizard", "Swift Ranger", "Cunning Rogue"]

# Main quest locations data
QUEST_DATA = {
    "welcome": {
        "title": "The Hero's Quest",
        "subtitle": "An Adventure Awaits!",
        "text": """Greetings, young hero!<br><br>
        A magical adventure awaits you today. You shall journey to enchanted lands,
        discover hidden treasures, and perhaps... find the legendary Artifact of Power!<br><br>
        Choose your hero name and begin your quest!""",
        "button": "Begin Adventure"
    },
    "tavern": {
        "title": "The Tavern of the Hungry Hound",
        "realName": "The British Bulldog Pub",
        "type": "Tavern",
        "desc": "Welcome to the warm hearth of the Hungry Hound! Here, weary travelers restore their strength with legendary potions and enchanted feasts. The Potion of Mac 'n Cheese is said to grant +10 to Happiness!",
        "address": "1220 Bower Pkwy E-10, Columbia, SC 29212",
    },
    "citadel": {
        "title": "The Citadel of Silicon",
        "realName": "The Tech Sanctuary",
        "type": "Artifact Repository",
        "desc": "Behold the Citadel of Silicon! Ancient tech relics hum with power within these walls. Cables of lightning, discs of memory, and devices of wonder await those who can solve the Rune Puzzle!",
        "address": "275 Harbison Blvd p, Columbia, SC 29212",
    }
}

# Additional map locations
MAP_LOCATIONS = [
    {
        "id": "target",
        "fantasyName": "The Red Bullseye Market",
        "realName": "Target (Harbison)",
        "desc": "A sprawling temple of the merchant gods, marked by the Sigil of the Red Eye. Beware the 'Target Effect'—where adventurers enter for one thing and leave with a cart full of treasures!",
        "address": "200 Harbison Blvd, Columbia, SC 29212",
        "type": "General Goods",
        "icon": "🎯"
    },
    {
        "id": "worldmarket",
        "fantasyName": "The Bazaar of Many Worlds",
        "realName": "World Market",
        "desc": "A trading post gathering wares from the Seven Seas. Find exotic treasures, strange confections, and furniture carved from enchanted wood!",
        "address": "278 Harbison Blvd, Columbia, SC 29212",
        "type": "Exotic Goods",
        "icon": "🗺️"
    },
    {
        "id": "2ndcharles",
        "fantasyName": "The Archives of Charles",
        "realName": "2nd & Charles",
        "desc": "A massive labyrinth of forgotten lore. Books, games, and treasures of old await the patient explorer. Beware—hours vanish like smoke within!",
        "address": "275-1 Harbison Blvd, Columbia, SC 29212",
        "type": "Tomes & Relics",
        "icon": "📖"
    },
    {
        "id": "barnes",
        "fantasyName": "The Grand Athenaeum",
        "realName": "Barnes & Noble",
        "desc": "A sanctuary of silence and the aroma of magical elixirs. The Coffee Oracle within grants +2 to Wisdom for one hour!",
        "address": "3400 Forest Dr, Columbia, SC 29204",
        "type": "Library",
        "icon": "📜"
    },
    {
        "id": "heroes",
        "fantasyName": "The Hall of Heroes & Wyrms",
        "realName": "Heroes & Dragons",
        "desc": "A legendary dungeon filled with action figures, gaming relics, and treasures of childhood. Nostalgia damage: 1d20!",
        "address": "1807 Bush River Rd Suite E, Columbia, SC 29210",
        "type": "Vintage Loot",
        "icon": "🐉"
    },
    {
        "id": "hobby",
        "fantasyName": "The Guildhall of Artificers",
        "realName": "Hobby Lobby",
        "desc": "Forge your own decorations! Here lie glues, pigments, and crafting materials. Currently possessed by the Spirit of Yule!",
        "address": "254 Harbison Blvd, Columbia, SC 29212",
        "type": "Crafting Mats",
        "icon": "✨"
    },
    {
        "id": "antique",
        "fantasyName": "The Ruins of the Old Mill",
        "realName": "Old Mill Antique Mall",
        "desc": "A sprawling labyrinth of ancient artifacts. Scavenge through booths of forgotten heirlooms and furniture of solid oak!",
        "address": "310 State St A, West Columbia, SC 29169",
        "type": "Ancient Artifacts",
        "icon": "👻"
    },
    {
        "id": "wine",
        "fantasyName": "The Alchemist's Vast Cellar",
        "realName": "Total Wine & More",
        "desc": "A dungeon lined with bottles of the Water of Life and Dwarven Stouts. Stock your inventory for the long winter!",
        "address": "276-1 Harbison Blvd, Columbia, SC 29212",
        "type": "Potions",
        "icon": "🍷"
    }
]

# Puzzle solution for the Citadel
CITADEL_PUZZLE_SOLUTION = {"⚡", "💾"}
CITADEL_PUZZLE_OPTIONS = ["⚡", "🔋", "💾", "🎮"]
