#!/usr/bin/env python3
"""Marketing deliverable (NOT a public site page):
3 months of Google/Facebook/Instagram posts (3x/week = 36) + 5 branded image
templates + a HighLevel-ready CSV (dates, content, public image URLs).
Outputs: images/posts/*.jpg (public), _branding/POSTS-3-MESES.html,
_branding/posts-highlevel.csv.
"""
import os, sys, csv, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import SERVICES, SERVICE_ORDER, CITIES, BUSINESS
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "images")
POSTS = os.path.join(IMG, "posts")
FD = os.path.join(ROOT, "_branding", "fonts")
os.makedirs(POSTS, exist_ok=True)
PHONE = BUSINESS["phone_display"]; TEL = BUSINESS["phone"]; DOMAIN = BUSINESS["domain"]
INK=(21,20,15); GOLD=(190,154,74); GOLD_LT=(217,190,126); CREAM=(245,240,230)

def OF(w, sz): return ImageFont.truetype(os.path.join(FD, f"Outfit-{w}.ttf"), sz)
logo = Image.open(os.path.join(IMG, "logo-lwr-light.png")).convert("RGBA")

def _grad(W, H):
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(ov)
    for y in range(H):
        a = int(235 * max(0.0, (y - H*0.32) / (H*0.68)))
        d.line([(0,y),(W,y)], fill=(12,11,9,a))
    d.rectangle((0,0,W,int(H*0.28)), fill=(12,11,9,110))
    return ov

def _cta(im, W, H):
    d = ImageDraw.Draw(im)
    d.rectangle((0,H-92,W,H), fill=GOLD)
    d.text((54, H-46), f"CALL {PHONE}", font=OF(800,44), fill=INK, anchor="lm")
    d.text((W-54, H-46), DOMAIN, font=OF(600,30), fill=(40,32,16), anchor="rm")

def make_photo(photo, headline, out):
    W,H=1200,900
    bg = ImageOps.exif_transpose(Image.open(os.path.join(IMG,"projects",photo))).convert("RGB")
    bg = ImageOps.fit(bg,(W,H),Image.LANCZOS).convert("RGBA")
    bg = Image.alpha_composite(bg, _grad(W,H))
    l = logo.copy(); l.thumbnail((360,360)); bg.alpha_composite(l,(50,46))
    d = ImageDraw.Draw(bg)
    d.text((56, H-286), headline, font=OF(800,70), fill=CREAM)
    d.text((58, H-196), "FREE ESTIMATE  ·  FULLY INSURED", font=OF(600,34), fill=GOLD_LT)
    _cta(bg, W, H)
    bg.convert("RGB").save(os.path.join(POSTS,out),"JPEG",quality=88)

def make_solid(headline, out):
    W,H=1200,900
    im = Image.new("RGBA",(W,H),INK+(255,)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,14),fill=GOLD)
    l = logo.copy(); l.thumbnail((520,520)); im.alpha_composite(l,((W-l.width)//2,120))
    d.text((W/2, 560), headline, font=OF(800,78), fill=GOLD_LT, anchor="mm")
    d.text((W/2, 650), "FREE ESTIMATE  ·  FULLY INSURED  ·  SAME CREW", font=OF(600,32), fill=CREAM, anchor="mm")
    _cta(im, W, H)
    im.convert("RGB").save(os.path.join(POSTS,out),"JPEG",quality=88)

make_photo("paver-driveway-tan-lakewood-ranch-fl.jpg","PAVER DRIVEWAYS","post-1-paver-driveways.jpg")
make_photo("spaced-paver-patio-gravel-joints-bradenton-fl.jpg","PAVER PATIOS","post-2-paver-patios.jpg")
make_photo("travertine-patio-pergola-lakewood-ranch-fl.jpg","TRAVERTINE POOL DECKS","post-3-pool-decks.jpg")
make_solid("CONCRETE & PAVERS","post-4-concrete-pavers.jpg")
make_photo("paver-walkway-banded-lakewood-ranch-fl.jpg","WALKWAYS & PATIOS","post-5-walkways.jpg")

IMG_MAP = {
    "concrete-driveways":"post-4-concrete-pavers.jpg","concrete-patios":"post-4-concrete-pavers.jpg",
    "concrete-pool-decks":"post-3-pool-decks.jpg","stamped-concrete":"post-4-concrete-pavers.jpg",
    "concrete-slabs":"post-4-concrete-pavers.jpg","concrete-resurfacing":"post-3-pool-decks.jpg",
    "paver-driveways":"post-1-paver-driveways.jpg","paver-patios-walkways":"post-2-paver-patios.jpg",
    "pool-deck-pavers":"post-3-pool-decks.jpg","paver-sealing":"post-2-paver-patios.jpg",
}
BENEFIT = {
    "concrete-driveways":"a poured concrete driveway engineered for Florida heat and shifting soil",
    "concrete-patios":"a broom, smooth or stamped patio built for Gulf Coast sun and drainage",
    "concrete-pool-decks":"a cool-finish, slip-aware pool deck that beats the Florida heat",
    "stamped-concrete":"stamped concrete that reads like stone and clears HOA/ARC review",
    "concrete-slabs":"a solid slab or pad on a properly compacted base",
    "concrete-resurfacing":"resurfacing that renews worn concrete without a full tear-out",
    "paver-driveways":"a paver driveway on a compacted base with polymeric joint sand",
    "paver-patios-walkways":"a paver patio or walkway that won't settle or wash out",
    "pool-deck-pavers":"a travertine or paver pool deck, cool underfoot and sealed",
    "paver-sealing":"paver sealing and re-sanding that locks the joints and boosts color",
}
TYPES = ["Service Spotlight","Free-Estimate Offer","Tip / Educational","Recent Work","Pavers vs Concrete"]
POST_CITY_SLUGS = ["lakewood-ranch","bradenton","sarasota","parrish","palmetto","venice",
                   "ellenton","north-port","riverview","sun-city-center","tampa","brandon"]

def post_text(t, slug, cslug):
    sv = SERVICES[slug]; name = sv["name"]; low = sv["short"].lower(); cname = CITIES[cslug]["name"]
    b = BENEFIT[slug]; link = f"https://{DOMAIN}/{slug}/{cslug}/"
    if t == 0:
        return (f"{name} in {cname}, FL. We install {b} — by the same crew from start to finish. "
                f"Fully insured, free written estimates across Manatee & Sarasota. Call or text {PHONE}.",
                "Learn more", link)
    if t == 1:
        return (f"Get a FREE, written estimate on your {low} in {cname} within 24 hours. No pressure, "
                f"fully insured, and the same crew builds exactly what they quote. Call or text {PHONE}.",
                "Call now", f"tel:{TEL}")
    if t == 2:
        return (f"{cname} homeowners: most cracked concrete and settled pavers trace back to a rushed base. "
                f"Our {low} in {cname} start with excavation, clean fill and a compacted base — the prep that "
                f"prevents the crack. Free estimate: {PHONE}.",
                "Learn more", link)
    if t == 3:
        return (f"Just finished a {low} in {cname}, FL. {b[0].upper()+b[1:]} — done right the first time. "
                f"Want yours next? Free estimates, fully insured. {PHONE}.",
                "Learn more", link)
    return (f"Thinking about a {low} for your {cname} home? We install both concrete and pavers and help you "
            f"pick what fits your budget, HOA and style. Free estimate in {cname}: {PHONE}.",
            "Learn more", link)

today = datetime.date.today()
start = today + datetime.timedelta(days=((0 - today.weekday()) % 7) or 7)
DAY_OFFSET = [0, 2, 4]; DAY_NAME = ["Monday","Wednesday","Friday"]; POST_TIME = "09:00"

rows_html = ""; csv_rows = []
for wk in range(12):
    week_html = ""
    for di in range(3):
        i = wk*3 + di
        slug = SERVICE_ORDER[i % len(SERVICE_ORDER)]
        cslug = POST_CITY_SLUGS[i % len(POST_CITY_SLUGS)]
        t = i % 5
        text, blabel, blink = post_text(t, slug, cslug)
        img = IMG_MAP[slug]
        url = f"https://{DOMAIN}/images/posts/{img}"
        date = (start + datetime.timedelta(days=wk*7 + DAY_OFFSET[di])).isoformat()
        csv_rows.append([date, POST_TIME, "Google Business Profile; Facebook; Instagram", text, url, blabel, blink])
        week_html += f'''<tr>
  <td style="white-space:nowrap"><b>{DAY_NAME[di]}</b><br><span class="dt">{date}</span><br><span class="ty">{TYPES[t]}</span></td>
  <td><img src="../images/posts/{img}" alt="" style="width:150px;border-radius:8px;display:block"></td>
  <td><div class="txt">{text}</div>
      <div class="btn">Button: <b>{blabel}</b> &rarr; <span class="lnk">{blink}</span></div></td>
</tr>'''
    rows_html += f'<tr class="wk"><td colspan="3">WEEK {wk+1}</td></tr>{week_html}'

with open(os.path.join(ROOT, "_branding", "posts-highlevel.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Date","Time","Platforms","Content","Image URL","Button","Button Link"])
    w.writerows(csv_rows)

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Google Posts — 3 meses (36 posts)</title>
<style>
  body{{font-family:Inter,Segoe UI,Arial,sans-serif;color:#241f12;background:#efe9dc;line-height:1.55;margin:0}}
  header{{background:#15140f;color:#f5f0e6;padding:38px 24px;border-bottom:5px solid #BE9A4A}}
  header h1{{font-size:1.6rem}}header p{{color:#c9bfa6;margin-top:.5rem;max-width:820px}}
  .wrap{{max-width:1000px;margin:0 auto;padding:24px 18px 70px}}
  .card{{background:#fff;border-radius:14px;padding:22px;margin:18px 0;box-shadow:0 3px 14px rgba(40,32,16,.07)}}
  h2{{border-bottom:3px solid #BE9A4A;padding-bottom:.4rem;color:#15140f;font-size:1.2rem}}
  table{{width:100%;border-collapse:collapse;font-size:.9rem}}
  td{{padding:11px 10px;border-bottom:1px solid #e3d9c5;vertical-align:top}}
  tr.wk td{{background:#15140f;color:#BE9A4A;font-weight:800;letter-spacing:.1em;font-size:.8rem;padding:8px 10px}}
  .ty{{font-size:.72rem;color:#9A7C32;font-weight:700}} .dt{{font-family:monospace;font-size:.72rem;color:#6b6453}}
  .txt{{background:#faf5ea;border-left:3px solid #BE9A4A;padding:10px 12px;border-radius:0 6px 6px 0}}
  .btn{{font-size:.78rem;color:#6b6453;margin-top:6px}} .lnk{{font-family:monospace;font-size:.75rem;color:#9A7C32}}
  .thumbs{{display:flex;gap:10px;flex-wrap:wrap}} .thumbs img{{width:180px;border-radius:8px}}
  .note{{background:#fff8ec;border:1px solid #f0e2c0;border-radius:8px;padding:12px 15px;font-size:.9rem;margin:.6rem 0}}
  ol li{{margin:.35rem 0}} code{{background:#efe9dc;padding:1px 6px;border-radius:4px}}
</style></head><body>
<header><h1>Google / Facebook / Instagram Posts — 3 meses (36 posts &middot; 3x/semana)</h1>
<p>Agende no HighLevel Social Planner. CSV pronto: <code>_branding/posts-highlevel.csv</code>. Imagens p&uacute;blicas em <code>images/posts/</code>.</p></header>
<div class="wrap">

<div class="card"><h2>Automatizar no HighLevel (voc&ecirc; j&aacute; tem GBP + FB + IG conectados)</h2>
<ol>
<li><b>Publique o site</b> (git push) para as imagens ficarem p&uacute;blicas em <code>https://{DOMAIN}/images/posts/post-1-paver-driveways.jpg</code>.</li>
<li>HighLevel &rarr; <b>Marketing &rarr; Social Planner</b>.</li>
<li>Clique em <b>&ldquo;+ New Post&rdquo;</b> e procure a op&ccedil;&atilde;o <b>CSV / Bulk import</b>. <b>Baixe o template CSV do HighLevel</b>.</li>
<li>Abra <code>posts-highlevel.csv</code> e cole as colunas <b>Date, Time, Content, Image URL</b> no template do HL; marque as contas <b>Google Business Profile + Facebook + Instagram</b>.</li>
<li>Confirme fuso e hor&aacute;rio (09:00) e <b>agende</b>. Pronto: 36 posts, 3 meses, no piloto autom&aacute;tico.</li>
</ol>
<div class="note"><b>Se o seu plano n&atilde;o tiver import CSV:</b> use o manual &mdash; &ldquo;+ New Post&rdquo;, cole o texto, suba a imagem, marque GBP+FB+IG, escolha a data e use <b>&ldquo;Duplicate&rdquo;</b> pra acelerar. O calend&aacute;rio abaixo tem tudo pronto pra copiar.</div>
</div>

<div class="card"><h2>As 5 imagens (1200&times;900)</h2>
<div class="thumbs">
<img src="../images/posts/post-1-paver-driveways.jpg"><img src="../images/posts/post-2-paver-patios.jpg">
<img src="../images/posts/post-3-pool-decks.jpg"><img src="../images/posts/post-4-concrete-pavers.jpg">
<img src="../images/posts/post-5-walkways.jpg"></div></div>

<div class="card"><h2>Calend&aacute;rio &mdash; 36 posts (a partir de {start.isoformat()})</h2>
<table>{rows_html}</table></div>

</div></body></html>'''

with open(os.path.join(ROOT, "_branding", "POSTS-3-MESES.html"), "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Wrote images/posts/*.jpg (5), POSTS-3-MESES.html, posts-highlevel.csv (36 rows from {start.isoformat()})")
