#!/usr/bin/env python3
"""Marketing deliverable (NOT a public site page):
FACEBOOK + INSTAGRAM feed content — 12 weeks / 36 posts (Mon/Wed/Fri), keyword-rich
captions (service+city) with hashtags and a link to the specific site page, 4 branded
1080x1080 image templates, photo rotation that never repeats a photo within 2 weeks.
Outputs:
  images/social-fbig/*.jpg      (public — pushed so Make can fetch them)
  _branding/fbig-records.json   (Make data-store records, channel = fbig_lwr)
  _branding/fbig-records.csv    (human backup)
  _branding/SOCIAL-FBIG.html    (open in browser — calendar + thumbnails)
NOTE: NEVER mention 'license/licensed' — only Insured / Free Estimates.
"""
import os, sys, csv, json, html, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import SERVICES, CITIES, BUSINESS
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG  = os.path.join(ROOT, "images"); PROJ = os.path.join(IMG, "projects")
OUT  = os.path.join(IMG, "social-fbig"); os.makedirs(OUT, exist_ok=True)
FD   = os.path.join(ROOT, "_branding", "fonts")
PHONE = BUSINESS["phone_display"]; TEL = BUSINESS["phone"]; DOMAIN = BUSINESS["domain"]
HANDLE = "@lakewoodranchconcrete"

INK=(24,22,16); INK2=(18,17,12); GOLD=(190,154,74); GOLD_LT=(217,190,126)
CREAM=(245,240,230); SAND=(236,228,212)

def OF(w, sz): return ImageFont.truetype(os.path.join(FD, f"Outfit-{w}.ttf"), sz)
logoL = Image.open(os.path.join(IMG, "logo-lwr-light.png")).convert("RGBA")

def fit(d, text, maxw, start, weight=800, floor=34):
    sz = start
    while sz > floor and d.textlength(text, font=OF(weight, sz)) > maxw: sz -= 3
    return OF(weight, sz)

def wrap(d, text, font, maxw):
    words = text.split(); lines=[]; cur=""
    for w in words:
        t = (cur+" "+w).strip()
        if d.textlength(t, font=font) <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def grad_bottom(W, H, top=0.34, amax=238):
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(ov)
    for y in range(H):
        a = int(amax * max(0.0, (y - H*top) / (H*(1-top))))
        d.line([(0,y),(W,y)], fill=(10,9,7,a))
    d.rectangle((0,0,W,int(H*0.22)), fill=(10,9,7,105)); return ov

def cta_bar(im, W, H):
    d = ImageDraw.Draw(im); d.rectangle((0,H-100,W,H), fill=GOLD)
    d.text((W/2, H-62), f"CALL OR TEXT   {PHONE}", font=OF(800,40), fill=INK2, anchor="mm")
    d.text((W/2, H-28), DOMAIN, font=OF(600,25), fill=(54,43,18), anchor="mm")

def load_photo(fn, box):
    im = ImageOps.exif_transpose(Image.open(os.path.join(PROJ, fn))).convert("RGB")
    return ImageOps.fit(im, box, Image.LANCZOS).convert("RGBA")

# ---------------------------------------------------------------- templates
W = H = 1080

def t1_bottom(photo, svc_label, city, out):     # photo + bottom gradient
    bg = load_photo(photo, (W,H)); bg = Image.alpha_composite(bg, grad_bottom(W,H))
    l = logoL.copy(); l.thumbnail((300,300)); bg.alpha_composite(l,(46,44))
    d = ImageDraw.Draw(bg)
    lines = wrap(d, svc_label.upper(), OF(800,74), W-104)
    y = H-330 - (len(lines)-1)*74
    for ln in lines:
        f = fit(d, ln, W-104, 74); d.text((52,y), ln, font=f, fill=CREAM); y += 78
    d.text((54, H-210), f"{city.upper()}, FL", font=OF(800,40), fill=GOLD_LT)
    d.text((54, H-160), "FULLY INSURED  ·  FREE ESTIMATES", font=OF(600,30), fill=CREAM)
    cta_bar(bg, W, H); bg.convert("RGB").save(os.path.join(OUT,out),"JPEG",quality=90)

def t2_panel(photo, svc_label, city, out):       # left ink panel + right photo
    px = 430
    im = Image.new("RGBA",(W,H),INK+(255,))
    ph = load_photo(photo, (W-px, H)); im.alpha_composite(ph,(px,0))
    d = ImageDraw.Draw(im)
    d.rectangle((px-8,0,px,H), fill=GOLD)
    l = logoL.copy(); l.thumbnail((300,300)); im.alpha_composite(l,(46,54))
    lines = wrap(d, svc_label, OF(800,60), px-86)
    y = 300
    for ln in lines:
        f = fit(d, ln, px-86, 60); d.text((48,y), ln, font=f, fill=CREAM); y += 64
    d.rectangle((50,y+8,110,y+14), fill=GOLD)
    d.text((48,y+34), f"{city}, FL", font=OF(600,38), fill=GOLD_LT)
    d.text((48,H-268), "Fully Insured", font=OF(600,30), fill=SAND)
    d.text((48,H-230), "Free Written Estimates", font=OF(600,30), fill=SAND)
    d.text((48,H-192), "Same Crew · HOA/ARC-Ready", font=OF(600,30), fill=SAND)
    d.text((48,H-144), HANDLE, font=OF(800,32), fill=GOLD_LT)
    cta_bar(im, W, H); im.convert("RGB").save(os.path.join(OUT,out),"JPEG",quality=90)

def t3_frame(photo, svc_label, city, out):       # cream frame around photo
    im = Image.new("RGBA",(W,H),CREAM+(255,)); d = ImageDraw.Draw(im)
    d.rectangle((0,0,W,12), fill=GOLD)
    ph = load_photo(photo, (W-120, H-330)); im.alpha_composite(ph,(60,150))
    l = logoL.copy()
    d.rectangle((60,44,60+150,44+150), fill=INK)
    l.thumbnail((132,132)); im.alpha_composite(l,(69,53))
    f = fit(d, svc_label, W-260, 58, weight=800); d.text((240,70), svc_label, font=f, fill=INK)
    d.text((242,132), f"{city}, FL  ·  Fully Insured", font=OF(600,32), fill=(120,96,40))
    d.text((60,H-142), f"Free estimate: {PHONE}", font=OF(800,40), fill=INK)
    d.text((60,H-92), DOMAIN, font=OF(600,30), fill=(120,96,40))
    d.rectangle((W-232,H-150,W-60,H-146), fill=GOLD)
    d.text((W-60,H-118), HANDLE, font=OF(600,28), fill=(120,96,40), anchor="rm")
    im.convert("RGB").save(os.path.join(OUT,out),"JPEG",quality=90)

def t4_solid(svc_label, city, out):              # typographic card (concrete, no photo)
    im = Image.new("RGBA",(W,H),INK2+(255,)); d = ImageDraw.Draw(im)
    d.rectangle((0,0,W,14), fill=GOLD)
    l = logoL.copy(); l.thumbnail((470,470)); im.alpha_composite(l,((W-l.width)//2,110))
    lines = wrap(d, svc_label.upper(), OF(800,72), W-150); y = 560 - (len(lines)-1)*40
    for ln in lines:
        f = fit(d, ln, W-150, 72); d.text((W/2,y), ln, font=f, fill=GOLD_LT, anchor="mm"); y += 80
    d.text((W/2, y+18), f"{city.upper()}, FL", font=OF(800,42), fill=CREAM, anchor="mm")
    d.text((W/2, y+78), "FULLY INSURED · FREE ESTIMATES · SAME CREW", font=OF(600,28), fill=SAND, anchor="mm")
    cta_bar(im, W, H); im.convert("RGB").save(os.path.join(OUT,out),"JPEG",quality=90)

# ---------------------------------------------------------------- content data
PHOTO_SEQ = [
 ("paver-driveway-tan-lakewood-ranch-fl.jpg","paver-driveways",["lakewood-ranch","bradenton","sarasota"]),
 ("paver-driveway-charcoal-border-bradenton-fl.jpg","paver-driveways",["bradenton","parrish","palmetto"]),
 ("paver-driveway-cobble-parrish-fl.jpg","paver-driveways",["parrish","ellenton","lakewood-ranch"]),
 ("paver-driveway-brick-bradenton-fl.jpg","paver-driveways",["bradenton","sarasota","venice"]),
 ("paver-walkway-driveway-lakewood-ranch-fl.jpg","paver-driveways",["lakewood-ranch","bradenton","parrish"]),
 ("spaced-paver-patio-gravel-joints-bradenton-fl.jpg","paver-patios-walkways",["bradenton","lakewood-ranch","parrish"]),
 ("spaced-paver-patio-lakewood-ranch-fl.jpg","paver-patios-walkways",["lakewood-ranch","sarasota","bradenton"]),
 ("paver-patio-gray-backyard-bradenton-fl.jpg","paver-patios-walkways",["bradenton","palmetto","ellenton"]),
 ("paver-patio-gray-parrish-fl.jpg","paver-patios-walkways",["parrish","bradenton","lakewood-ranch"]),
 ("paver-walkway-banded-lakewood-ranch-fl.jpg","paver-patios-walkways",["lakewood-ranch","sarasota","venice"]),
 ("concrete-stone-entry-steps-lakewood-ranch-fl.jpg","paver-patios-walkways",["lakewood-ranch","bradenton","parrish"]),
 ("paver-pool-deck-patio-lakewood-ranch-fl.jpg","pool-deck-pavers",["lakewood-ranch","bradenton","sarasota"]),
 ("travertine-patio-pergola-lakewood-ranch-fl.jpg","pool-deck-pavers",["lakewood-ranch","sarasota","venice"]),
]
SOLID_SEQ = [
 ("concrete-driveways",["lakewood-ranch","bradenton","parrish"]),
 ("concrete-patios",["bradenton","sarasota","palmetto"]),
 ("stamped-concrete",["lakewood-ranch","sarasota","bradenton"]),
 ("concrete-pool-decks",["bradenton","lakewood-ranch","venice"]),
 ("concrete-slabs",["parrish","palmetto","ellenton"]),
 ("concrete-resurfacing",["bradenton","sarasota","lakewood-ranch"]),
 ("paver-sealing",["lakewood-ranch","bradenton","sarasota"]),
]
NEAR = {
 "lakewood-ranch":"Bradenton, Sarasota & Parrish","bradenton":"Lakewood Ranch, Palmetto & Ellenton",
 "sarasota":"Lakewood Ranch, Osprey & Venice","parrish":"Ellenton, Palmetto & Bradenton",
 "palmetto":"Ellenton, Bradenton & Parrish","ellenton":"Palmetto, Parrish & Bradenton",
 "venice":"Nokomis, Osprey & North Port",
}
BENEFIT = {
 "concrete-driveways":"a poured concrete driveway engineered for Florida heat and shifting soil",
 "concrete-patios":"a broom, smooth or stamped concrete patio built for Gulf Coast sun and drainage",
 "concrete-pool-decks":"a cool-finish, slip-aware concrete pool deck that beats the Florida heat",
 "stamped-concrete":"stamped concrete that reads like natural stone and clears HOA/ARC review",
 "concrete-slabs":"a solid concrete slab or pad on a properly compacted base",
 "concrete-resurfacing":"concrete resurfacing that renews a worn, cracked surface without a full tear-out",
 "paver-driveways":"a paver driveway set on a fully compacted base with polymeric joint sand",
 "paver-patios-walkways":"a paver patio or walkway that won't settle, shift or wash out",
 "pool-deck-pavers":"a travertine or paver pool deck, cool underfoot and sealed to last",
 "paver-sealing":"paver sealing and re-sanding that locks the joints and brings the color back",
}
TIP = {
 "concrete-driveways":"a driveway is only as good as its base and control joints",
 "concrete-patios":"a patio needs slope and control joints or it puddles and cracks",
 "concrete-pool-decks":"pool decks need a slip-aware finish and the right slope away from the pool",
 "stamped-concrete":"stamped concrete lives or dies on the sealer and release color",
 "concrete-slabs":"a slab is only as strong as the compaction and thickness under it",
 "concrete-resurfacing":"resurfacing only lasts if the old surface is sound and properly prepped",
 "paver-driveways":"most sunken pavers trace back to a rushed, under-compacted base",
 "paver-patios-walkways":"polymeric sand and edge restraint are what keep pavers from spreading",
 "pool-deck-pavers":"travertine stays cooler than concrete and pavers flex instead of cracking",
 "paver-sealing":"sealing every 2-3 years is what keeps pavers from fading and weeds from setting in",
}
RELATED = "concrete & paver driveways, patios, pool decks, travertine, stamped concrete, walkways & sealing"

def kebab(s): return " ".join(s.replace("&"," ").split()).replace(" ","-").lower()

def hashtags(short, cname):
    st = "".join(w.capitalize() for w in short.replace("&"," ").split())
    ct = cname.replace(" ","").replace(".","")
    base = f"#{st} #{ct} #{ct}FL #Concrete #Pavers #ConcreteContractor #Hardscape #Hardscaping"
    region = "#LakewoodRanch #Bradenton #Sarasota #ManateeCounty #FloridaHomes #CurbAppeal #OutdoorLiving #SWFL"
    seen=set(); out=[]
    for t in (base+" "+region).split():
        if t.lower() not in seen: seen.add(t.lower()); out.append(t)
    return " ".join(out)

def caption(ct, slug, cslug):
    sv = SERVICES[slug]; name = html.unescape(sv["name"]); short = html.unescape(sv["short"]); low = short.lower()
    cname = CITIES[cslug]["name"]; b = BENEFIT[slug]; near = NEAR[cslug]; tip = TIP[slug]
    link = f"https://{DOMAIN}/{slug}/{cslug}/"; tg = hashtags(short, cname)
    if ct == 0:
        body = (f"{name} in {cname}, FL done right. Lakewood Ranch Concrete installs {b}. "
                f"We install {RELATED} across {cname}, {near} and all of Manatee & Sarasota County. "
                f"Fully insured. Free written estimates.")
    elif ct == 1:
        body = (f"Free {low} estimate in {cname}, FL. {name} — {b}. Serving {cname}, {near} and the Suncoast. "
                f"No pressure, fully insured, same crew from start to finish.")
    elif ct == 2:
        body = (f"{cname} homeowners: {tip}. Our {low} start with real base prep and engineered joints — "
                f"not shortcuts. {name} plus {RELATED} across {cname}, {near}. Fully insured, free estimates.")
    else:
        body = (f"Another {low} finished in {cname}, FL — {b}. Your {cname} project could be next. "
                f"We install {RELATED} across {cname}, {near}. Fully insured, free written estimates, HOA/ARC-ready.")
    return f"{body}\n\n\U0001F4DE Free estimate: {PHONE}\n\U0001F517 {link}\n\n{tg}", link

# ---------------------------------------------------------------- build calendar
today = datetime.date.today()
start = today + datetime.timedelta(days=((0 - today.weekday()) % 7) or 7)  # next Monday
DAY_OFFSET=[0,2,4]; DAY_NAME=["Monday","Wednesday","Friday"]; POST_TIME="11:30"
TYPE_LABEL=["Service Spotlight","Free-Estimate Offer","Tip / Educational","Recent Work"]

records=[]; csv_rows=[]; rows_html=""; cp=cs=0
for i in range(36):
    wk, di = divmod(i, 3)
    is_solid = (i % 4 == 3)
    if is_solid:
        svc, cities = SOLID_SEQ[cs % len(SOLID_SEQ)]; city = cities[(cs//len(SOLID_SEQ)) % 3]
        photo=None; tmpl="T4-Solid"; cs+=1
    else:
        photo, svc, cities = PHOTO_SEQ[cp % len(PHOTO_SEQ)]; city = cities[(cp//len(PHOTO_SEQ)) % 3]
        tmpl = ["T1-Photo","T2-Panel","T3-Frame"][cp % 3]; cp+=1
    ct = i % 4
    sv = SERVICES[svc]; short = html.unescape(sv["short"]); cname = CITIES[city]["name"]
    fn_out = f"fbig-{i+1:02d}-{kebab(short)}-{city}-fl.jpg"
    if is_solid:                      t4_solid(html.unescape(sv["name"]), cname, fn_out)
    elif tmpl=="T1-Photo":            t1_bottom(photo, short, cname, fn_out)
    elif tmpl=="T2-Panel":            t2_panel(photo, html.unescape(sv["name"]), cname, fn_out)
    else:                             t3_frame(photo, html.unescape(sv["name"]), cname, fn_out)
    cap, link = caption(ct, svc, city)
    url = f"https://{DOMAIN}/images/social-fbig/{fn_out}"
    date = (start + datetime.timedelta(days=wk*7 + DAY_OFFSET[di]))
    key = f"lwr-fbig-{date.isoformat()}-{kebab(short)}-{city}"
    records.append({"key": key, "data": {
        "date": date.isoformat()+"T11:30:00", "channel": "fbig_lwr", "service": short, "city": cname,
        "image_url": url, "caption": cap, "link": link, "status": "approved", "permalink": ""}})
    csv_rows.append([date.isoformat(), POST_TIME, cap, url, link, ""])
    if i%3==0: rows_html += f'<tr class="wk"><td colspan="3">WEEK {i//3+1}</td></tr>'
    rows_html += f'''<tr>
  <td style="white-space:nowrap"><b>{DAY_NAME[di]}</b><br><span class="dt">{date.isoformat()}</span><br><span class="ty">{TYPE_LABEL[ct]}</span><br><span class="tm">{tmpl}</span></td>
  <td><img src="../images/social-fbig/{fn_out}" alt="" style="width:170px;border-radius:10px;display:block"></td>
  <td><div class="txt">{html.escape(cap)}</div></td>
</tr>'''

with open(os.path.join(ROOT,"_branding","fbig-records.json"),"w",encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=1)
with open(os.path.join(ROOT,"_branding","fbig-records.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["Date","Time","Caption","Image URL","Link","Status"]); w.writerows(csv_rows)

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Facebook + Instagram — 3 meses</title>
<style>
 body{{font-family:Inter,Segoe UI,Arial,sans-serif;color:#241f12;background:#efe9dc;line-height:1.55;margin:0}}
 header{{background:#15140f;color:#f5f0e6;padding:38px 24px;border-bottom:5px solid #BE9A4A}}
 header h1{{font-size:1.55rem}}header p{{color:#c9bfa6;margin-top:.5rem;max-width:860px}}
 .wrap{{max-width:1040px;margin:0 auto;padding:24px 18px 70px}}
 .card{{background:#fff;border-radius:14px;padding:22px;margin:18px 0;box-shadow:0 3px 14px rgba(40,32,16,.07)}}
 h2{{border-bottom:3px solid #BE9A4A;padding-bottom:.4rem;color:#15140f;font-size:1.2rem}}
 table{{width:100%;border-collapse:collapse;font-size:.86rem}}
 td{{padding:11px 10px;border-bottom:1px solid #e3d9c5;vertical-align:top}}
 tr.wk td{{background:#15140f;color:#BE9A4A;font-weight:800;letter-spacing:.1em;font-size:.8rem;padding:8px 10px}}
 .ty{{font-size:.72rem;color:#9A7C32;font-weight:700}} .tm{{font-size:.68rem;color:#8a8272;font-family:monospace}}
 .dt{{font-family:monospace;font-size:.72rem;color:#6b6453}}
 .txt{{background:#faf5ea;border-left:3px solid #BE9A4A;padding:10px 12px;border-radius:0 6px 6px 0;font-size:.83rem;white-space:pre-wrap}}
 .thumbs{{display:flex;gap:10px;flex-wrap:wrap}} .thumbs img{{width:150px;border-radius:10px}}
 .note{{background:#fff8ec;border:1px solid #f0e2c0;border-radius:8px;padding:12px 15px;font-size:.9rem;margin:.6rem 0}}
 ol li{{margin:.35rem 0}} code{{background:#efe9dc;padding:1px 6px;border-radius:4px}}
 .kpi{{display:flex;gap:14px;flex-wrap:wrap;margin:.5rem 0}}
 .kpi div{{background:#15140f;color:#f0e6d2;border-radius:10px;padding:12px 16px;min-width:120px}}
 .kpi b{{color:#D9BE7E;font-size:1.35rem;display:block}}
</style></head><body>
<header><h1>Facebook + Instagram &mdash; 3 meses (36 posts &middot; Seg/Qua/Sex)</h1>
<p>Publica automaticamente no <b>Facebook</b> e no <b>Instagram</b> ao mesmo tempo. Legendas ricas em keywords
(servi&ccedil;o+cidade), hashtags e <b>link da p&aacute;gina espec&iacute;fica</b> de cada post. Foto nunca repete
dentro de 2 semanas. Depois de ~90 dias o pr&oacute;prio cen&aacute;rio <b>recicla</b> os posts. Automa&ccedil;&atilde;o via <b>Make</b>.</p></header>
<div class="wrap">
<div class="card"><h2>Resumo</h2>
<div class="kpi">
 <div><b>36</b>posts prontos</div><div><b>2</b>redes (FB+IG)</div><div><b>4</b>templates de arte</div>
 <div><b>13</b>fotos em rod&iacute;zio</div><div><b>3x</b>por semana</div><div><b>+90d</b>reciclagem autom&aacute;tica</div>
</div>
<div class="note"><b>Como funciona:</b> o Make l&ecirc; a fila (data store, channel <code>fbig_lwr</code>) &rarr; baixa a imagem &rarr;
publica a <b>foto no Facebook</b> (message = legenda) &rarr; publica a <b>foto no Instagram</b> (mesma legenda) &rarr;
reagenda o mesmo post para daqui 90 dias. Roda Seg/Qua/Sex entre 11:30 e 12:30.</div></div>

<div class="card"><h2>4 templates de arte (1080&times;1080)</h2>
<div class="thumbs">
<img src="../images/social-fbig/fbig-01-paver-driveways-lakewood-ranch-fl.jpg">
<img src="../images/social-fbig/fbig-02-paver-driveways-bradenton-fl.jpg">
<img src="../images/social-fbig/fbig-03-paver-driveways-parrish-fl.jpg">
<img src="../images/social-fbig/fbig-04-concrete-driveways-lakewood-ranch-fl.jpg">
</div>
<p style="font-size:.85rem;color:#6b6453;margin-top:.6rem">T1 Foto+degrad&ecirc; &middot; T2 Painel lateral &middot; T3 Moldura creme &middot; T4 Card tipogr&aacute;fico (concreto)</p></div>

<div class="card"><h2>Calend&aacute;rio &mdash; 36 posts (a partir de {start.isoformat()})</h2>
<table>{rows_html}</table></div>
</div></body></html>'''
with open(os.path.join(ROOT,"_branding","SOCIAL-FBIG.html"),"w",encoding="utf-8") as f: f.write(HTML)
print(f"Wrote 36 social images + fbig-records.json + fbig-records.csv + SOCIAL-FBIG.html (from {start.isoformat()})")
print(f"Photo-posts: {cp}, Solid-posts: {cs}")
