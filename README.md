# love-you-animation
Pygame heart animation with 'Love You' text particles

## Features
- ❤️ Beautiful heart-shaped particle animation
- 💬 "Love You" floating text particles with glow effects
- 🎨 Blue color scheme with smooth transitions
- 🎵 Background music support
- 📱 QR Code animation generator

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Run the Main Animation
```bash
python main.py
```
Displays a stunning heart animation with cascading "Love You" text particles on a black background.

### Generate Animated QR Code
```bash
python qr_animation.py
```
Creates `love_qr_animation.gif` - an animated QR code that links to this repository with pulsing heart colors.

## Technical Details
- **Heart Shape**: Mathematical parametric equation for perfect heart curve
- **Particles**: Outline and fill particles with staggered animation timing
- **Glow Effects**: Multi-layer rendering with scaled text for glow illusion
- **QR Animation**: 60-frame smooth color animation embedded in QR code

## Files
- `main.py` - Main pygame animation
- `qr_animation.py` - Animated QR code generator
- `requirements.txt` - Python dependencies

## Output
- `main.py` → Animated window display
- `qr_animation.py` → `love_qr_animation.gif` (animated QR code)
