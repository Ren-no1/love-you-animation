import qrcode
from PIL import Image, ImageDraw, ImageFont
import imageio
import os

# Configuration
REPO_URL = "https://github.com/Ren-no1/love-you-animation"
FRAMES = 60  # Number of frames for smooth animation
OUTPUT_FILE = "love_qr_animation.gif"

def generate_qr_with_heart(frame_num, total_frames):
    """
    Generate a QR code with animated colors and heart overlay effect
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(REPO_URL)
    qr.make(fit=True)
    
    # Animate between heart colors (pink shades)
    progress = frame_num / total_frames
    # Create color gradient from light pink to dark pink and back
    if progress < 0.5:
        intensity = progress * 2
    else:
        intensity = 2 - (progress * 2)
    
    r = int(200 + 55 * (intensity - 0.5) * 2)
    g = int(100 + 92 * (intensity - 0.5) * 2)
    b = int(150 + 103 * (intensity - 0.5) * 2)
    
    fill_color = (r, g, b)
    back_color = (255, 255, 255)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img = img.convert('RGB')
    
    # Add decorative heart text at the bottom
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    # Add "Love You" text with pulsing alpha effect
    text = "❤ Love You ❤"
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = (width - text_width) // 2
    text_y = height - text_height - 10
    
    # Add white background for text
    padding = 5
    draw.rectangle(
        [text_x - padding, text_y - padding, 
         text_x + text_width + padding, text_y + text_height + padding],
        fill=(255, 255, 255),
        outline=fill_color,
        width=2
    )
    
    draw.text((text_x, text_y), text, fill=fill_color, font=font)
    
    return img

def generate_animated_qr():
    """
    Generate an animated QR code that links to the repository
    """
    print(f"Generating {FRAMES} frames of animated QR code...")
    
    frames = []
    for i in range(FRAMES):
        print(f"  Frame {i+1}/{FRAMES}", end='\r')
        img = generate_qr_with_heart(i, FRAMES)
        frames.append(img)
    
    print(f"\nSaving animation to {OUTPUT_FILE}...")
    imageio.mimsave(OUTPUT_FILE, frames, duration=0.1, loop=0)
    print(f"✓ Animation created successfully: {OUTPUT_FILE}")
    print(f"✓ QR code links to: {REPO_URL}")

if __name__ == "__main__":
    generate_animated_qr()
