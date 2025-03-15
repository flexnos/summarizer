from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np

# GIF Parameters
width, height = 500, 200
num_frames = 40  # Total frames in GIF
output_path = "summarize_with_ease.gif"

# Font Settings (Ensure arial.ttf exists or provide another font path)
font_path = "arial.ttf"
font_size = 45
font = ImageFont.truetype(font_path, font_size)

# Create frames
frames = []
for i in range(num_frames):
    img = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(img)

    # Text
    text = "Summarize with Ease"

    # Calculate text position (Centered)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Smooth glowing effect (sin wave for natural pulsing)
    glow_intensity = int(180 + 75 * np.sin(2 * np.pi * i / num_frames))  # Smooth glow variation
    text_color = (glow_intensity, glow_intensity, 255)  # Professional blue glow

    # Draw text with glow effect (adding multiple layers for soft glow)
    for offset in range(3, 0, -1):  
        draw.text((x - offset, y - offset), text, fill=(0, 0, glow_intensity // 2), font=font)
        draw.text((x + offset, y + offset), text, fill=(0, 0, glow_intensity // 2), font=font)

    draw.text((x, y), text, fill=text_color, font=font)  # Main text

    # Append frame
    frames.append(img)

# Save GIF
imageio.mimsave(output_path, frames, duration=0.1)

print(f"GIF saved successfully: {output_path}")
