# The Hero's Quest

A magical, interactive adventure application built with **Streamlit 1.52+** for young heroes and their guides. This parent-led experience transforms a real-world outing into an epic D&D-themed quest, complete with XP, gold, inventory, and puzzles.

---

## Features

### Core Mechanics
- **Hero State System** — Track your hero's name, XP (0-100), gold, and inventory
- **HUD Fragment** — Optimized heads-up display using `@st.fragment` for smooth updates
- **Quest Progression** — Complete challenges at each location to earn rewards

### Modern Streamlit 1.52+ Widgets
| Widget | Usage |
|--------|-------|
| `st.pills` | Tactile navigation and hero name selection |
| `st.feedback("stars")` | Rate the tavern feast (1-5 stars) |
| `st.segmented_control` | Solve the rune puzzle at the Citadel |
| `st.audio_input` | Speak your hero name (pretend transcription) |
| `st.html` | Glassmorphism theme injection (no deprecated `st.markdown`) |

### Visual Design
- **Glassmorphism Theme** — Frosted glass cards with backdrop blur
- **Dark Fantasy Palette** — Deep blues and purples with golden accents
- **Responsive Layout** — Optimized for tablet and mobile use
- **Cinzel Typography** — Epic fantasy headers

---

## Screenshots

| Welcome Screen | HUD & Tavern | Citadel Puzzle |
|----------------|--------------|----------------|
| Choose your hero name with pills or voice | Rate the feast with stars | Solve the rune combination |

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Streamlit 1.52+ |
| Language | Python 3.10 - 3.14 |
| Styling | Native `st.html` CSS injection |
| State | `st.session_state` with dataclasses |
| Images | WebP format, base64 embedded |

---

## Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/D-D_adventure.git
cd D-D_adventure

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Requirements

```
streamlit>=1.52.0
```

For image optimization (optional):
```
Pillow>=10.0.0
```

---

## Usage Guide

### Starting the Adventure

1. **Welcome Screen**
   - Choose a hero name using the pill selector
   - Or record your voice to become the "Legendary Champion"
   - Click "Begin Adventure" to start

2. **The Tavern of the Hungry Hound**
   - Read about the British Bulldog Pub
   - Rate the "Potion of Mac 'n Cheese" (1-5 stars)
   - Earn +10 XP and the Cheese Blessing item
   - Spend 10 gold on the feast

3. **The Citadel of Silicon**
   - Solve the Rune Puzzle: Select **Lightning (⚡)** and **Memory (💾)**
   - Earn +20 gold and a Crystal Gem
   - Use the Map Spell button to navigate in real life

4. **The Scroll of Destiny (Map)**
   - Browse 8 additional locations
   - Each location includes a fantasy description and real address
   - Tap addresses to open Google Maps

### Game Mechanics

| Mechanic | Details |
|----------|---------|
| **XP** | Starts at 0/100. Earn by completing quests. |
| **Gold** | Starts at 50. Spend at tavern, earn at citadel. |
| **Inventory** | Starts with Sword and Shield. Collect Cheese and Gems. |

---

## Project Structure

```
D-D_adventure/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── optimize_images.py     # Image optimization utility
├── README.md              # This file
├── claude.md              # AI assistant instructions
├── gemini.md              # AI assistant instructions
└── images/
    ├── adventure.png      # Original images
    ├── armory.png
    ├── map.png
    ├── tavern.png
    └── optimized/         # WebP versions (800px width)
        ├── adventure.webp
        ├── armory.webp
        ├── map.webp
        └── tavern.webp
```

---

## Code Architecture

### State Management

```python
@dataclass
class HeroState:
    name: str = "Brave Adventurer"
    xp: int = 0
    xp_max: int = 100
    gold: int = 50
    inventory: List[str] = field(default_factory=lambda: ["🗡️", "🛡️"])
    location: GameLocation = GameLocation.WELCOME
    tavern_rated: bool = False
    citadel_solved: bool = False
```

### Location Routing

```python
class GameLocation(Enum):
    WELCOME = "welcome"
    TAVERN = "tavern"
    CITADEL = "citadel"
    MAP = "map"
    LOCATION_DETAIL = "location_detail"
```

### Fragment Optimization

The HUD uses `@st.fragment` to prevent full page reruns when stats change:

```python
@st.fragment
def render_hud():
    # Only this component rerenders when XP/gold updates
    ...
```

---

## Locations

### Main Quest Locations

| Location | Real Name | Address |
|----------|-----------|---------|
| Tavern of the Hungry Hound | The British Bulldog Pub | 1220 Bower Pkwy E-10, Columbia, SC 29212 |
| Citadel of Silicon | Tech Sanctuary | 275 Harbison Blvd p, Columbia, SC 29212 |

### Optional Destinations

| Fantasy Name | Real Name | Type |
|--------------|-----------|------|
| The Red Bullseye Market | Target (Harbison) | General Goods |
| The Bazaar of Many Worlds | World Market | Exotic Goods |
| The Archives of Charles | 2nd & Charles | Tomes & Relics |
| The Grand Athenaeum | Barnes & Noble | Library |
| The Hall of Heroes & Wyrms | Heroes & Dragons | Vintage Loot |
| The Guildhall of Artificers | Hobby Lobby | Crafting Mats |
| The Ruins of the Old Mill | Old Mill Antique Mall | Ancient Artifacts |
| The Alchemist's Vast Cellar | Total Wine & More | Potions |

---

## Image Optimization

The project includes an image optimization script for faster loading:

```bash
# Requires Pillow
pip install Pillow

# Run optimization
python optimize_images.py
```

This converts PNG images to WebP format at 800px width with 80% quality, typically achieving 95%+ size reduction.

---

## Customization

### Adding New Locations

Edit the `LOCATIONS` list in `app.py`:

```python
{
    "id": 'unique_id',
    "fantasyName": "The Enchanted Grove",
    "realName": "Local Park",
    "desc": "A mystical forest where...",
    "address": "123 Main St, City, ST 12345",
    "type": "Nature Sanctuary",
    "icon": "🌲"
}
```

### Modifying the Theme

Edit the `get_css()` function to customize colors:

```python
# Primary background gradient
background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);

# Accent color (gold)
color: #ffd700;

# Card transparency
background: rgba(255, 255, 255, 0.1);
backdrop-filter: blur(12px);
```

### Adding New Quests

1. Add a quest flag to `HeroState`:
   ```python
   new_quest_completed: bool = False
   ```

2. Create the quest interaction in the screen function:
   ```python
   if not hero.new_quest_completed:
       # Show quest UI
       if quest_condition_met:
           st.session_state.hero.new_quest_completed = True
           add_xp(15)
           st.balloons()
   ```

---

## Browser Support

| Browser | Support |
|---------|---------|
| Chrome | Full |
| Safari | Full |
| Firefox | Full |
| Edge | Full |

**Note:** `backdrop-filter` (glassmorphism blur) requires modern browser versions.

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"

Ensure you've activated your virtual environment and installed dependencies:

```bash
venv\Scripts\activate  # Windows
pip install streamlit
```

### Venv Points to Missing Python

If your venv was created with a Python version that's been uninstalled:

```bash
# Remove old venv and recreate
rmdir /s /q venv  # Windows
rm -rf venv       # macOS/Linux

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Images Not Loading

Ensure the `images/optimized/` folder contains the WebP files:
- `adventure.webp`
- `armory.webp`
- `map.webp`
- `tavern.webp`

Run `python optimize_images.py` to regenerate if needed.

---

## Performance

The application uses several optimization techniques:

1. **`@st.cache_data`** — Caches CSS and base64-encoded images
2. **`@st.fragment`** — HUD updates independently of main content
3. **WebP Images** — 90%+ smaller than PNG originals
4. **Embedded Images** — Base64 encoding eliminates network requests

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-quest`)
3. Commit changes (`git commit -m 'Add new quest location'`)
4. Push to branch (`git push origin feature/new-quest`)
5. Open a Pull Request

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- **Streamlit** — For the magical framework
- **Google Fonts** — Cinzel and Lato typefaces
- **The Young Adventurer** — For inspiring this quest

---

*May your dice roll true and your code compile clean.* ⚔️
