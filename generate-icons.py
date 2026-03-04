from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("icons", exist_ok=True)
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0,0,size-1,size-1], radius=size//5, fill=(99,102,241,255))
    font_size = int(size * 0.52)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    draw.text((size//2, size//2), "₹", fill=(255,255,255,255), font=font, anchor="mm")
    img.save(f"icons/icon-{size}.png")
    print(f"✓ icon-{size}.png")

print("All icons generated!")
