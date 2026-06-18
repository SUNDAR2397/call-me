from PIL import Image, ImageDraw, ImageFont

W, H = 600, 640
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (20, 20, 20)
BLUE = (120, 200, 240)
LW = 9

# ---- face (big round head) ----
fx0, fy0, fx1, fy1 = 70, 30, 530, 470
d.ellipse([fx0, fy0, fx1, fy1], fill="white", outline=BLACK, width=LW)

# ---- eyes (big teary ovals) ----
def eye(cx, cy, w, h):
    d.ellipse([cx-w, cy-h, cx+w, cy+h], fill=BLACK)
    # highlights
    d.ellipse([cx-w*0.45-8, cy-h*0.55, cx-w*0.45+22, cy-h*0.55+30], fill="white")
    d.ellipse([cx-6, cy+h*0.15, cx+14, cy+h*0.15+18], fill="white")

eye(220, 250, 42, 70)
eye(380, 250, 42, 70)

# ---- sad drooping eyebrows ----
d.arc([165, 150, 285, 250], start=200, end=320, fill=BLACK, width=8)
d.arc([320, 150, 440, 250], start=220, end=340, fill=BLACK, width=8)

# ---- small content mouth (gentle u) ----
d.arc([275, 330, 335, 380], start=20, end=160, fill=BLACK, width=7)

# ---- blue tears ----
# left streaming tear
d.polygon([(178, 300), (150, 430), (205, 430)], fill=BLUE)
d.ellipse([150, 415, 205, 455], fill=BLUE)
# right tear (being wiped)
d.ellipse([398, 300, 432, 345], fill=BLUE)
d.polygon([(404, 300), (415, 280), (426, 300)], fill=BLUE)

# ---- hand wiping right eye ----
hx, hy = 455, 300
# palm
d.ellipse([hx-10, hy+20, hx+70, hy+110], fill="white", outline=BLACK, width=7)
# fingers curling toward the eye
for i, off in enumerate([-8, 14, 36, 58]):
    d.line([(hx+off, hy+30), (hx+off-20, hy-10)], fill=BLACK, width=7)
    d.ellipse([hx+off-26, hy-22, hx+off-6, hy-2], fill="white", outline=BLACK, width=6)
# thumb
d.line([(hx-8, hy+70), (hx-40, hy+55)], fill=BLACK, width=7)

# ---- caption text ----
def load(sz):
    return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Black.ttf", sz)

def caption(text, cy, size):
    f = load(size)
    bbox = d.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    x = (W - tw) / 2 - bbox[0]
    # black outline
    for dx in range(-4, 5, 2):
        for dy in range(-4, 5, 2):
            d.text((x+dx, cy+dy), text, font=f, fill=BLACK)
    d.text((x, cy), text, font=f, fill="white")

caption("You make me", 488, 58)
caption("emosenal", 555, 58)

img.save("gifs/emosenal.png")
print("saved gifs/emosenal.png", img.size)
