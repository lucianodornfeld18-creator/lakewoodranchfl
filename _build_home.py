#!/usr/bin/env python3
"""Homepage for Lakewood Ranch Concrete — concrete & paver contractor.
Ticker before hero, factual trust strip (no invented reviews/stats),
services grid from SERVICE_ORDER, areas grid from CITIES, why-us, process,
42-point standard, reviews CTA (empty-safe), blog teasers, strong CTAs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *

OUT = "index.html"
TITLE = "Concrete & Paver Contractor · Lakewood Ranch & East Manatee FL"
DESC = clip_desc(
    "Concrete driveways, patios, pool decks, stamped concrete & pavers across "
    "Lakewood Ranch, Bradenton & the Suncoast. Fully insured, free estimates, "
    "60-mile radius from Bradenton 34212.")
CANONICAL = f"{SITE}/"
SCHEMAS = [schema_website(), schema_organization(),
           schema_breadcrumb([("Home", SITE + "/")])]

# ──────────────────────────────────────────────────────────────────
# 1) TICKER — goes BEFORE hero so it's visible above the fold
# ──────────────────────────────────────────────────────────────────
ticker = ticker_bar()   # already built in _gen.py

# ──────────────────────────────────────────────────────────────────
# 2) HERO — single static photo, no carousel, no review card
# ──────────────────────────────────────────────────────────────────
hero = f'''<section class="hero">
  <img class="hero-bg-img"
       src="/images/real-stamped-concrete-patio.webp"
       alt="Stamped concrete patio and paver driveway installed by {BUSINESS['name']} in Lakewood Ranch"
       loading="eager" fetchpriority="high">
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-label">Lakewood Ranch · Bradenton · East Manatee</div>
      <h1 class="hero-h1">Concrete &amp; Pavers in<br><em>Lakewood Ranch</em> &amp; East Manatee<span class="stop">.</span></h1>
      <p class="hero-sub"><strong style="color:#FFC84A">Poured right. Built to last.</strong> Driveways, patios, pool decks, stamped &amp; decorative concrete, and paver hardscape &mdash; installed by the same crew that measured your home. Fully insured, free estimates, serving a 60-mile radius from Bradenton 34212.</p>
      <div class="hero-cta">
        <a href="/contact/#quote" class="btn btn-orange">Free Estimate <span class="btn-arrow"></span></a>
        <a href="{TEL_LINK}" class="btn btn-outline-light">{BUSINESS["phone_display"]}</a>
      </div>
      <div class="hero-meta">
        <div><strong>Insured</strong><span>Fully Insured</span></div>
        <div><strong>Free</strong><span>Free Estimates</span></div>
        <div><strong>42-Pt</strong><span>Install Standard</span></div>
        <div><strong>24h</strong><span>Written Estimate</span></div>
        <div><strong>Warranty</strong><span>Workmanship, In Writing</span></div>
      </div>
    </div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 2b) TRUST STRIP — factual items only (NO invented review numbers/ratings)
# ──────────────────────────────────────────────────────────────────
TRUST_ITEMS = [
    "Fully Insured",
    "Free Estimates",
    "42-Point Install Standard",
    "Written Workmanship Warranty",
    "Same Crew, Start to Finish",
    "HOA &amp; ARC-Ready Hardscape",
]
trust_strip = f'''<section class="proof-strip">
  <div class="proof-grid">
    {''.join(f'<div class="proof-item"><div class="proof-num" style="font-size:clamp(1.05rem,2vw,1.35rem)">{t}</div></div>' for t in TRUST_ITEMS)}
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 3) SERVICES — from SERVICE_ORDER
# ──────────────────────────────────────────────────────────────────
svc_cards = "".join(f'''<a href="/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} — {s["short"]}</div>
  <h3>{s["h1_phrase"]}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">View work</span>
</a>''' for slug, s in [(sl, SERVICES[sl]) for sl in SERVICE_ORDER])

services = f'''<section class="home-services">
  <div class="container-wide">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:2rem;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="mono-label">Concrete &amp; Pavers · {len(SERVICE_ORDER)} Services</span>
        <h2 style="margin-top:.5rem;font-size:clamp(1.4rem,3vw,2rem)">Every surface we pour &amp; pave — <em style="font-style:normal;color:var(--orange-dark)">done right.</em></h2>
      </div>
      <a href="/contact/#quote" class="btn btn-orange" style="flex-shrink:0">Get Free Estimate <span class="btn-arrow"></span></a>
    </div>
    <div class="services-grid">{svc_cards}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 4) WHY US
# ──────────────────────────────────────────────────────────────────
why_items = "".join(f'''<div class="why-item">
  <div class="why-num">{w["num"]}</div>
  <div><h3>{w["title"]}</h3><p>{w["body"]}</p></div>
</div>''' for w in WHY_US_POINTS)

why = f'''<section class="why-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">Why {BUSINESS['name']} · {len(WHY_US_POINTS)} Reasons</span>
        <h2>What makes us different — <em>in plain English.</em></h2>
      </div>
    </div>
    <div class="why-grid">{why_items}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 5) AREAS — from CITIES
# ──────────────────────────────────────────────────────────────────
area_cards = "".join(f'''<a href="/{slug}/" class="area-card">
  <div class="area-card-name">{c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">Details →</span>
</a>''' for slug, c in CITIES.items())

areas = f'''<section class="areas-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label on-dark">{len(CITIES)} Cities · Lakewood Ranch, Manatee &amp; Sarasota</span>
        <h2 style="color:var(--white)">{len(CITIES)} cities. <em style="color:var(--orange);font-style:normal">One crew.</em></h2>
      </div>
    </div>
    <div class="areas-grid">{area_cards}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 6) PROCESS
# ──────────────────────────────────────────────────────────────────
process_steps = "".join(
    f'<div class="process-step" data-num="{p["num"]}"><div class="process-num">{p["num"]}</div><h3>{p["title"]}</h3><p>{p["body"]}</p></div>'
    for p in PROCESS_STEPS)

process = f'''<section class="process-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label">How It Works · {len(PROCESS_STEPS)} Steps</span>
        <h2>Estimate to finished surface — <em>no surprises.</em></h2>
      </div>
    </div>
    <div class="process-grid">{process_steps}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 7) 42-POINT STANDARD
# ──────────────────────────────────────────────────────────────────
checklist_html = f'''<section class="checklist-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label">The {BUSINESS['name']} Standard</span>
        <h2>Our {CHECKLIST["points"]}-Point Install Standard</h2>
        <div class="section-head-text"><p>Every driveway, patio, pool deck, slab, and paver field passes all {CHECKLIST["points"]} points before we hand it over. You get the written warranty and the job photos at walkthrough.</p></div>
      </div>
    </div>
    <div class="checklist-grid">{"".join(f"""<article class="checklist-card">
  <header class="checklist-card-head">
    <span class="ck-num">{c["icon"]}</span>
    <strong>{c["title"]}</strong>
    <span class="ck-count">{len(c["items"])} pts</span>
  </header>
  <ol>{"".join(f"<li>{it}</li>" for it in c["items"])}</ol>
</article>""" for c in CHECKLIST["categories"])}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 8) REVIEWS — NEW business, REVIEWS=[]: render an honest CTA, never
#    invented cards/ratings. Be-the-first-to-review framing.
# ──────────────────────────────────────────────────────────────────
if REVIEWS:
    cards = ""
    for r in REVIEWS[:6]:
        stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
        cards += f'''<article class="review-card">
  <div class="review-quote-mark">&ldquo;</div>
  <div class="review-stars" aria-label="{r["rating"]} out of 5 stars">{stars}</div>
  <p class="review-text">{r["text"]}</p>
  <div class="review-meta">
    <span class="review-author">{r["name"]}</span>
    <span class="review-where">{r["city"]}, FL · {r["service"]}</span>
  </div>
</article>'''
    reviews_block = f'<div class="reviews-grid">{cards}</div>'
else:
    reviews_block = f'''<div style="background:var(--gray-bg);border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:40px 32px;text-align:center;max-width:760px;margin:0 auto">
      <p style="font-size:1.1rem;line-height:1.6;color:var(--text);margin-bottom:1.4rem">We&rsquo;re a local, owner-operated concrete &amp; paver crew building a reputation one driveway, patio, and pool deck at a time across Lakewood Ranch and East Manatee. Hire us for your project and you&rsquo;ll get the same crew start to finish, our {CHECKLIST["points"]}-point install standard, and a written workmanship warranty.</p>
      <a href="/contact/#quote" class="btn btn-orange">Get Your Free Estimate <span class="btn-arrow"></span></a>
    </div>'''

reviews_section_html = f'''<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">05</div>
      <div class="section-head-meta">
        <span class="mono-label">Local · Owner-Operated · Fully Insured</span>
        <h2>Built on workmanship — <em style="font-style:normal;color:var(--orange-dark)">not hype.</em></h2>
      </div>
    </div>
    {reviews_block}
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# 9) BLOG TEASERS — from GENERAL_BLOG_POSTS
# ──────────────────────────────────────────────────────────────────
blog_cards = "".join(f'''<a href="/blog/{p["slug"]}/" class="blog-card">
  <div class="blog-card-meta"><span>{p["category"]}</span><span>{p["primary_city"]}</span></div>
  <h3>{p["title"]}</h3>
  <span class="blog-card-cta">Read guide</span>
</a>''' for p in GENERAL_BLOG_POSTS[:3])

blog = f'''<section>
  <div class="container-wide">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:2rem;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="mono-label">From the Journal · Concrete &amp; Pavers</span>
        <h2 style="margin-top:.5rem;font-size:clamp(1.4rem,3vw,2rem)">Straight answers before you <em style="font-style:normal;color:var(--orange-dark)">spend a dollar.</em></h2>
      </div>
      <a href="/blog/" class="btn btn-outline" style="flex-shrink:0">All Articles <span class="btn-arrow"></span></a>
    </div>
    <div class="blog-grid">{blog_cards}</div>
  </div>
</section>'''

# ──────────────────────────────────────────────────────────────────
# EXTRA CSS
# ──────────────────────────────────────────────────────────────────
EXTRA_CSS = """
/* ── HERO: static single photo ── */
.hero{
  position:relative;
  height:calc(100vh - 92px - 46px);
  min-height:480px;
  max-height:900px;
  display:flex;
  align-items:center;
  overflow:hidden;
  background:#ddd;
}
.hero-bg-img{
  position:absolute;inset:0;
  width:100%;height:100%;
  object-fit:cover;
  object-position:center 60%;
}
.hero::after{
  content:"";position:absolute;inset:0;
  background:linear-gradient(95deg,rgba(0,0,0,.78) 0%,rgba(0,0,0,.62) 25%,rgba(0,0,0,.40) 50%,rgba(0,0,0,.15) 75%,rgba(0,0,0,0) 100%);
  z-index:1;pointer-events:none;
}
.hero-inner{
  position:relative;z-index:2;
  max-width:var(--container);
  margin:0 auto;padding:0 28px;
  width:100%;
}
.hero-left{
  display:flex;flex-direction:column;
  max-width:640px;
}
.hero-label{
  display:flex;align-items:center;gap:10px;
  font-size:.76rem;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;color:#FFC84A;
  margin-bottom:16px;
  text-shadow:0 1px 8px rgba(0,0,0,.95);
}
.hero-label::before{content:"";width:22px;height:2px;background:#FFC84A;flex-shrink:0;box-shadow:0 0 8px rgba(0,0,0,.9)}
.hero-h1{
  font-family:var(--font-head);font-weight:800;
  font-size:clamp(2.1rem,4.4vw,3.4rem);
  line-height:1.08;letter-spacing:-.03em;
  color:#FFFFFF;margin-bottom:1rem;
  text-shadow:0 2px 18px rgba(0,0,0,.95),0 1px 4px rgba(0,0,0,.8);
}
.hero-h1 em{font-style:normal;color:#FFC84A;text-shadow:0 2px 18px rgba(0,0,0,.95),0 0 12px rgba(0,0,0,.5)}
.hero-sub{
  font-size:1.02rem;line-height:1.65;
  color:#FFFFFF;margin-bottom:1.6rem;
  text-shadow:0 1px 12px rgba(0,0,0,.95),0 1px 4px rgba(0,0,0,.8);
  max-width:560px;font-weight:500;
}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:1.8rem}
.hero-meta{
  display:flex;flex-wrap:wrap;gap:16px 28px;
  border-top:1px solid rgba(255,255,255,.35);
  padding-top:1.3rem;
}
.hero-meta div{display:flex;flex-direction:column;gap:3px}
.hero-meta strong{
  font-family:var(--font-head);font-size:1.35rem;
  color:#FFFFFF;font-weight:800;line-height:1;
  text-shadow:0 1px 10px rgba(0,0,0,.95);
}
.hero-meta span{
  font-size:.7rem;letter-spacing:.1em;
  text-transform:uppercase;color:rgba(255,255,255,.92);
  text-shadow:0 1px 8px rgba(0,0,0,.95);font-weight:600;
}

/* ── TICKER redesigned (compact, more elegant) ── */
.ticker{
  background:linear-gradient(180deg,#1A1A1A 0%,#0F0F0F 100%);
  color:#fff;
  border-top:2px solid var(--orange);
  border-bottom:1px solid rgba(255,255,255,.08);
  overflow:hidden;
}
.ticker-inner{
  display:flex;
  animation:tickerScroll 55s linear infinite;
  font-size:.72rem;font-weight:600;letter-spacing:.14em;
  text-transform:uppercase;padding:14px 0;white-space:nowrap;
  color:rgba(255,255,255,.85);
}
.ticker-inner span{padding:0 22px;flex-shrink:0;display:inline-flex;align-items:center;gap:8px}
.ticker-inner span::before{content:"●";color:var(--orange);font-size:.5rem;margin-right:8px}
.ticker-inner span::after{display:none}

/* ── SERVICES compact ── */
.home-services{padding:60px 0;background:var(--gray-bg)}
.home-services .services-grid{grid-template-columns:repeat(3,1fr);gap:14px}
.home-services .service-card{min-height:210px;padding:22px 18px}
.home-services .service-card h3{font-size:1.15rem}

/* ── PROOF / TRUST STRIP ── */
.proof-strip .proof-grid{grid-template-columns:repeat(6,1fr)}
.proof-strip .proof-num{font-weight:800;letter-spacing:-.01em}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .hero{height:calc(100vh - 80px - 44px);min-height:440px}
  .hero::after{background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.70) 100%)}
  .hero-h1{font-size:clamp(1.85rem,6vw,2.7rem)}
  .proof-strip .proof-grid{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:520px){
  .hero{height:calc(100vh - 72px - 44px);min-height:400px}
  .hero-inner{padding:0 18px}
  .proof-strip .proof-grid{grid-template-columns:1fr 1fr}
}
"""

# ──────────────────────────────────────────────────────────────────
# ASSEMBLE — ticker BEFORE hero (visually after, per layout)
# ──────────────────────────────────────────────────────────────────
final_cta_html = final_cta(
    "Free estimate on your concrete or paver project.",
    "On-site measure, transparent pricing, written quote within 24 hours. Fully insured.")

body = "\n".join([
    hero,
    ticker,
    trust_strip,
    services,
    why,
    areas,
    process,
    checklist_html,
    reviews_section_html,
    blog,
    f'<div class="container">{contact_banner("Free, no-pressure estimate within 24 hours.", "Call, text, or email — driveways, patios, pool decks &amp; pavers.")}</div>',
    final_cta_html,
])

extra = (f'<style>{EXTRA_CSS}</style>'
         '<link rel="preload" href="/images/real-stamped-concrete-patio.webp" as="image">')

head_html = head(TITLE, DESC, CANONICAL, og_image=og_url(path="/images/og-default.jpg"), json_ld=SCHEMAS, extra_meta=extra)
write_page(OUT, head_html, header(active="home"), body)
print(f"Wrote /{OUT} - {open(OUT, encoding='utf-8').read().count(chr(10))} lines")
