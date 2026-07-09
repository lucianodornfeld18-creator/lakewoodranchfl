#!/usr/bin/env python3
"""Marketing deliverable (NOT a public site page):
3 months of GOOGLE BUSINESS PROFILE posts (3x/week = 36), keyword-heavy captions,
12 branded image templates, and a Make-ready CSV (Google Sheet source).
Outputs: images/posts/*.jpg (public), _branding/POSTS-3-MESES.html,
_branding/posts-gbp.csv.
"""
import os, sys, csv, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import SERVICES, SERVICE_ORDER, CITIES, BUSINESS
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "images"); POSTS = os.path.join(IMG, "posts")
FD = os.path.join(ROOT, "_branding", "fonts"); os.makedirs(POSTS, exist_ok=True)
PHONE = BUSINESS["phone_display"]; TEL = BUSINESS["phone"]; DOMAIN = BUSINESS["domain"]
INK=(21,20,15); GOLD=(190,154,74); GOLD_LT=(217,190,126); CREAM=(245,240,230)

def OF(w, sz): return ImageFont.truetype(os.path.join(FD, f"Outfit-{w}.ttf"), sz)
logo = Image.open(os.path.join(IMG, "logo-lwr-light.png")).convert("RGBA")

def _fit(d, text, maxw, start, weight=800, floor=42):
    sz = start
    while sz > floor and d.textlength(text, font=OF(weight,sz)) > maxw: sz -= 4
    return OF(weight, sz)
def _grad(W, H):
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(ov)
    for y in range(H):
        a = int(235 * max(0.0, (y - H*0.32) / (H*0.68)))
        d.line([(0,y),(W,y)], fill=(12,11,9,a))
    d.rectangle((0,0,W,int(H*0.28)), fill=(12,11,9,110)); return ov
def _cta(im, W, H):
    d = ImageDraw.Draw(im); d.rectangle((0,H-92,W,H), fill=GOLD)
    d.text((54, H-46), f"CALL {PHONE}", font=OF(800,44), fill=INK, anchor="lm")
    d.text((W-54, H-46), DOMAIN, font=OF(600,30), fill=(40,32,16), anchor="rm")
def make_photo(photo, headline, out):
    W,H=1200,900
    bg = ImageOps.exif_transpose(Image.open(os.path.join(IMG,"projects",photo))).convert("RGB")
    bg = ImageOps.fit(bg,(W,H),Image.LANCZOS).convert("RGBA")
    bg = Image.alpha_composite(bg, _grad(W,H))
    l = logo.copy(); l.thumbnail((360,360)); bg.alpha_composite(l,(50,46))
    d = ImageDraw.Draw(bg)
    d.text((56, H-286), headline, font=_fit(d,headline,W-110,70), fill=CREAM)
    d.text((58, H-196), "FREE ESTIMATE  ·  FULLY INSURED", font=OF(600,34), fill=GOLD_LT)
    _cta(bg, W, H); bg.convert("RGB").save(os.path.join(POSTS,out),"JPEG",quality=88)
def make_solid(headline, out):
    W,H=1200,900
    im = Image.new("RGBA",(W,H),INK+(255,)); d=ImageDraw.Draw(im); d.rectangle((0,0,W,14),fill=GOLD)
    l = logo.copy(); l.thumbnail((520,520)); im.alpha_composite(l,((W-l.width)//2,120))
    d.text((W/2, 560), headline, font=_fit(d,headline,W-140,78), fill=GOLD_LT, anchor="mm")
    d.text((W/2, 650), "FREE ESTIMATE  ·  FULLY INSURED  ·  SAME CREW", font=OF(600,32), fill=CREAM, anchor="mm")
    _cta(im, W, H); im.convert("RGB").save(os.path.join(POSTS,out),"JPEG",quality=88)

TEMPLATES = [
    ("paver-driveway-tan-lakewood-ranch-fl.jpg","PAVER DRIVEWAYS","post-01.jpg"),
    ("paver-driveway-charcoal-border-bradenton-fl.jpg","PAVER DRIVEWAYS","post-02.jpg"),
    ("paver-driveway-cobble-parrish-fl.jpg","PAVER DRIVEWAYS","post-03.jpg"),
    ("paver-driveway-brick-bradenton-fl.jpg","BRICK PAVER DRIVEWAYS","post-04.jpg"),
    ("spaced-paver-patio-gravel-joints-bradenton-fl.jpg","PAVER PATIOS","post-05.jpg"),
    ("spaced-paver-patio-lakewood-ranch-fl.jpg","SPACED PAVER PATIOS","post-06.jpg"),
    ("paver-patio-gray-backyard-bradenton-fl.jpg","PAVER PATIOS","post-07.jpg"),
    ("travertine-patio-pergola-lakewood-ranch-fl.jpg","TRAVERTINE POOL DECKS","post-08.jpg"),
    ("paver-pool-deck-patio-lakewood-ranch-fl.jpg","PAVER POOL DECKS","post-09.jpg"),
    ("paver-walkway-banded-lakewood-ranch-fl.jpg","PAVER WALKWAYS","post-10.jpg"),
    ("concrete-stone-entry-steps-lakewood-ranch-fl.jpg","STEPS & ENTRIES","post-11.jpg"),
]
for src, hl, out in TEMPLATES: make_photo(src, hl, out)
make_solid("CONCRETE & PAVERS","post-solid.jpg")

IMG_POOL = {
    "concrete-driveways":["post-solid.jpg"], "concrete-patios":["post-solid.jpg"],
    "concrete-pool-decks":["post-solid.jpg"], "stamped-concrete":["post-solid.jpg"],
    "concrete-slabs":["post-11.jpg","post-solid.jpg"], "concrete-resurfacing":["post-solid.jpg"],
    "paver-driveways":["post-01.jpg","post-02.jpg","post-03.jpg","post-04.jpg"],
    "paver-patios-walkways":["post-05.jpg","post-06.jpg","post-07.jpg","post-10.jpg"],
    "pool-deck-pavers":["post-08.jpg","post-09.jpg"], "paver-sealing":["post-07.jpg","post-05.jpg"],
}
BENEFIT = {
    "concrete-driveways":"a poured concrete driveway engineered for Florida heat and shifting soil",
    "concrete-patios":"a broom, smooth or stamped concrete patio built for Gulf Coast sun and drainage",
    "concrete-pool-decks":"a cool-finish, slip-aware concrete pool deck that beats the Florida heat",
    "stamped-concrete":"stamped concrete that reads like stone and clears HOA/ARC review",
    "concrete-slabs":"a solid concrete slab or pad on a properly compacted base",
    "concrete-resurfacing":"concrete resurfacing that renews a worn surface without a full tear-out",
    "paver-driveways":"a paver driveway on a compacted base with polymeric joint sand",
    "paver-patios-walkways":"a paver patio or walkway that won't settle or wash out",
    "pool-deck-pavers":"a travertine or paver pool deck, cool underfoot and sealed",
    "paver-sealing":"paver sealing and re-sanding that locks the joints and boosts color",
}
NEARBY = {
    "lakewood-ranch":"Bradenton, Parrish & Sarasota","bradenton":"Lakewood Ranch, Palmetto & Ellenton",
    "sarasota":"Osprey, Nokomis & Venice","parrish":"Ellenton, Palmetto & Bradenton",
    "palmetto":"Ellenton, Bradenton & Parrish","venice":"Nokomis, Osprey & North Port",
    "ellenton":"Palmetto, Parrish & Bradenton","north-port":"Venice, Port Charlotte & Punta Gorda",
    "riverview":"Brandon, Apollo Beach & Ruskin","sun-city-center":"Ruskin, Wimauma & Apollo Beach",
    "tampa":"Brandon, Riverview & Apollo Beach","brandon":"Riverview, Tampa & Valrico",
}
RELATED = "concrete & paver driveways, patios, pool decks, travertine, stamped concrete, sidewalks & sealing"
TYPES = ["Service Spotlight","Free-Estimate Offer","Tip / Educational","Recent Work","Pavers vs Concrete"]
POST_CITY_SLUGS = list(NEARBY.keys())

def tags(short, cname):
    st = "".join(w.capitalize() for w in short.replace("&"," ").split())
    ct = cname.replace(" ","").replace(".","")
    return f"#{st} #{ct} #ConcreteContractor #Pavers #{ct}FL"

def post_text(t, slug, cslug):
    sv = SERVICES[slug]; name = sv["name"]; short = sv["short"]; low = short.lower()
    cname = CITIES[cslug]["name"]; b = BENEFIT[slug]; near = NEARBY[cslug]
    link = f"https://{DOMAIN}/{slug}/{cslug}/"; h = tags(short, cname)
    if t == 0:
        return (f"{name} in {cname}, FL. Looking for a {low} contractor in {cname}? Lakewood Ranch Concrete "
                f"installs {b}. We also do {RELATED} across {cname}, {near} and all of Manatee & Sarasota County. "
                f"Compacted base, engineered joints, HOA/ARC-ready. Fully insured. Free written estimates. "
                f"Call or text {PHONE}. {h}", "Learn more", link)
    if t == 1:
        return (f"FREE {low} estimate in {cname}, FL within 24 hours. {name} done right — {b}. "
                f"Serving {cname}, {near} & the Suncoast: {RELATED}. No pressure, fully insured, same crew "
                f"start to finish. Call or text {PHONE} for your {low} in {cname}. {h}", "Call now", f"tel:{TEL}")
    if t == 2:
        return (f"{cname} {low}: why base prep is the whole job. Most cracked concrete and settled pavers in "
                f"{cname} trace back to a rushed base. Our {low} start with excavation, clean fill and a compacted "
                f"base. {name} plus {RELATED} in {cname}, {near}. Fully insured, free estimate. {PHONE}. {h}",
                "Learn more", link)
    if t == 3:
        return (f"Just finished a {low} in {cname}, FL. {b[0].upper()+b[1:]} — done right the first time. "
                f"Your {cname} {low} could be next. We install {RELATED} across {cname}, {near}. "
                f"Free estimates, fully insured, HOA/ARC-ready. {PHONE}. {h}", "Learn more", link)
    return (f"Pavers or concrete for your {cname} {low}? We install both. {name} contractor serving {cname}, "
            f"{near} — {RELATED}. Compacted base, engineered joints, fully insured. Free {low} estimate in "
            f"{cname}. Call or text {PHONE}. {h}", "Learn more", link)

today = datetime.date.today()
start = today + datetime.timedelta(days=((0 - today.weekday()) % 7) or 7)
DAY_OFFSET=[0,2,4]; DAY_NAME=["Monday","Wednesday","Friday"]; POST_TIME="09:00"
rows_html=""; csv_rows=[]; occ={}
for wk in range(12):
    week_html=""
    for di in range(3):
        i = wk*3 + di
        slug = SERVICE_ORDER[i % len(SERVICE_ORDER)]; cslug = POST_CITY_SLUGS[i % len(POST_CITY_SLUGS)]; t = i % 5
        text, blabel, blink = post_text(t, slug, cslug)
        pool = IMG_POOL[slug]; k = occ.get(slug,0); occ[slug]=k+1; img = pool[k % len(pool)]
        url = f"https://{DOMAIN}/images/posts/{img}"
        date = (start + datetime.timedelta(days=wk*7 + DAY_OFFSET[di])).isoformat()
        csv_rows.append([date, POST_TIME, text, url, blabel, blink, ""])
        week_html += f'''<tr>
  <td style="white-space:nowrap"><b>{DAY_NAME[di]}</b><br><span class="dt">{date}</span><br><span class="ty">{TYPES[t]}</span></td>
  <td><img src="../images/posts/{img}" alt="" style="width:150px;border-radius:8px;display:block"></td>
  <td><div class="txt">{text}</div><div class="btn">Button: <b>{blabel}</b> &rarr; <span class="lnk">{blink}</span></div></td>
</tr>'''
    rows_html += f'<tr class="wk"><td colspan="3">WEEK {wk+1}</td></tr>{week_html}'

with open(os.path.join(ROOT,"_branding","posts-gbp.csv"),"w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Date","Time","Content","Image URL","CTA","CTA Link","Status"])
    w.writerows(csv_rows)

thumbs = "".join(f'<img src="../images/posts/{o}">' for _,_,o in TEMPLATES)+'<img src="../images/posts/post-solid.jpg">'
HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Google Posts — 3 meses</title>
<style>
  body{{font-family:Inter,Segoe UI,Arial,sans-serif;color:#241f12;background:#efe9dc;line-height:1.55;margin:0}}
  header{{background:#15140f;color:#f5f0e6;padding:38px 24px;border-bottom:5px solid #BE9A4A}}
  header h1{{font-size:1.6rem}}header p{{color:#c9bfa6;margin-top:.5rem;max-width:820px}}
  .wrap{{max-width:1000px;margin:0 auto;padding:24px 18px 70px}}
  .card{{background:#fff;border-radius:14px;padding:22px;margin:18px 0;box-shadow:0 3px 14px rgba(40,32,16,.07)}}
  h2{{border-bottom:3px solid #BE9A4A;padding-bottom:.4rem;color:#15140f;font-size:1.2rem}}
  table{{width:100%;border-collapse:collapse;font-size:.88rem}}
  td{{padding:11px 10px;border-bottom:1px solid #e3d9c5;vertical-align:top}}
  tr.wk td{{background:#15140f;color:#BE9A4A;font-weight:800;letter-spacing:.1em;font-size:.8rem;padding:8px 10px}}
  .ty{{font-size:.72rem;color:#9A7C32;font-weight:700}} .dt{{font-family:monospace;font-size:.72rem;color:#6b6453}}
  .txt{{background:#faf5ea;border-left:3px solid #BE9A4A;padding:10px 12px;border-radius:0 6px 6px 0;font-size:.86rem}}
  .btn{{font-size:.76rem;color:#6b6453;margin-top:6px}} .lnk{{font-family:monospace;font-size:.74rem;color:#9A7C32}}
  .thumbs{{display:flex;gap:10px;flex-wrap:wrap}} .thumbs img{{width:150px;border-radius:8px}}
  .note{{background:#fff8ec;border:1px solid #f0e2c0;border-radius:8px;padding:12px 15px;font-size:.9rem;margin:.6rem 0}}
  ol li{{margin:.35rem 0}} code{{background:#efe9dc;padding:1px 6px;border-radius:4px}}
</style></head><body>
<header><h1>Google Business Profile — 3 meses (36 posts &middot; 3x/semana)</h1>
<p>Somente GBP. Legendas com <b>abuso de keywords</b> (servi&ccedil;o+cidade+vizinhas+servi&ccedil;os+hashtags). Automa&ccedil;&atilde;o via <b>Make</b>. CSV: <code>_branding/posts-gbp.csv</code>.</p></header>
<div class="wrap">

<div class="card"><h2>Automatizar no Make (GBP j&aacute; conectado)</h2>
<ol>
<li><b>Publique o site</b> (git push) &mdash; as imagens ficam p&uacute;blicas em <code>https://{DOMAIN}/images/posts/post-01.jpg</code>&hellip;</li>
<li>Crie um <b>Google Sheet</b> e <b>importe</b> o <code>posts-gbp.csv</code> (colunas Date, Time, Content, Image URL, CTA, CTA Link, Status).</li>
<li>No Make, novo cen&aacute;rio: <b>Schedule</b> (Seg/Qua/Sex 09:00) &rarr; <b>Google Sheets &ldquo;Search Rows&rdquo;</b> (Status vazio, ordenar por Date, limite 1) &rarr; <b>Google My Business &ldquo;Create a Post&rdquo;</b> (Summary = Content, Media/Photo = Image URL, CTA = CTA + CTA Link) &rarr; <b>Google Sheets &ldquo;Update Row&rdquo;</b> (Status = Posted).</li>
<li>Ative o cen&aacute;rio. Pronto: 36 posts, 3x/semana, no piloto autom&aacute;tico &mdash; sem repetir (o Status controla).</li>
</ol>
<div class="note">Alternativa 1-clique: no Make, importe o CSV numa <b>Data Store</b> em vez de Sheet. O fluxo &eacute; o mesmo (Schedule &rarr; pega pr&oacute;ximo &rarr; GMB Create Post &rarr; marca como enviado). Quero montar o cen&aacute;rio pra voc&ecirc;? Tenho acesso ao seu Make &mdash; s&oacute; pedir.</div></div>

<div class="card"><h2>12 templates de imagem (1200&times;900)</h2><div class="thumbs">{thumbs}</div></div>

<div class="card"><h2>Calend&aacute;rio &mdash; 36 posts (a partir de {start.isoformat()})</h2>
<table>{rows_html}</table></div>

</div></body></html>'''
with open(os.path.join(ROOT,"_branding","POSTS-3-MESES.html"),"w",encoding="utf-8") as f: f.write(HTML)
print(f"Wrote {len(TEMPLATES)+1} templates + POSTS-3-MESES.html + posts-gbp.csv (GBP-only, keyword-heavy, from {start.isoformat()})")
