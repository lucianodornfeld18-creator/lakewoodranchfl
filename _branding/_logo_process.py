from PIL import Image
src = Image.open("images/logo-lwr.png").convert("RGBA")
px = src.load()
w,h = src.size

# 1) transparent bg: near-white -> alpha 0
trans = src.copy(); tp = trans.load()
for y in range(h):
    for x in range(w):
        r,g,b,a = px[x,y]
        if r>234 and g>234 and b>234:
            tp[x,y]=(r,g,b,0)
# autocrop to content
bbox = trans.getbbox()
if bbox: trans = trans.crop(bbox)
trans.save("images/logo-lwr-transparent.png")

# 2) dark-bg version: white->transparent, dark(text)->cream, keep gold
light = Image.open("images/logo-lwr.png").convert("RGBA"); lp = light.load()
CREAM=(245,240,230)
for y in range(h):
    for x in range(w):
        r,g,b,a = px[x,y]
        if r>234 and g>234 and b>234:
            lp[x,y]=(r,g,b,0)
        elif r<95 and g<95 and b<95:        # dark text -> cream
            lp[x,y]=(CREAM[0],CREAM[1],CREAM[2],255)
        # else keep (gold W + dashes)
if bbox: light = light.crop(bbox)
light.save("images/logo-lwr-light.png")
print("size", w, h, "-> cropped", trans.size)
print("wrote images/logo-lwr-transparent.png + images/logo-lwr-light.png")
