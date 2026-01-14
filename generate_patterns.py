import os, random
from PIL import Image, ImageDraw, ImageFilter

OUT_DIR = "_static/global/patterns"
N_BLOCKS = 2
N_STIM = 8

os.makedirs(OUT_DIR, exist_ok=True)

def make_pattern(seed, size=512):
    random.seed(seed)
    img = Image.new("RGB", (size, size), (20, 20, 25))
    d = ImageDraw.Draw(img)

    # viele zufällige Formen + Linien (schlecht verbal zu labeln)
    for _ in range(180):
        x1, y1 = random.randint(0,size), random.randint(0,size)
        x2, y2 = random.randint(0,size), random.randint(0,size)
        col = (random.randint(40,220), random.randint(40,220), random.randint(40,220))
        w = random.randint(1,6)
        d.line((x1,y1,x2,y2), fill=col, width=w)

    for _ in range(60):
        x, y = random.randint(0,size), random.randint(0,size)
        r = random.randint(10,120)
        col = (random.randint(30,240), random.randint(30,240), random.randint(30,240))
        d.ellipse((x-r,y-r,x+r,y+r), outline=col, width=random.randint(2,6))

    img = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    return img

for b in range(1, N_BLOCKS+1):
    for i in range(1, N_STIM+1):
        make_pattern(f"b{b}-t-{i}").save(os.path.join(OUT_DIR, f"block{b}_targets_{i:02d}.png"))
        make_pattern(f"b{b}-f1-{i}").save(os.path.join(OUT_DIR, f"block{b}_foil1_{i:02d}.png"))
        make_pattern(f"b{b}-f2-{i}").save(os.path.join(OUT_DIR, f"block{b}_foil2_{i:02d}.png"))

print("Done. Patterns written to", OUT_DIR)