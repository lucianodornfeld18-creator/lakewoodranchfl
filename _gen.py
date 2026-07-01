#!/usr/bin/env python3
"""
Lakewood Ranch Concrete — Shared Page Generator
Bold/Editorial design system: ink black + paper cream + orange accent.
Used by every _build_*.py script.
"""
import json
from _data import BUSINESS, CITIES, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, SMS_LINK, WHY_US_POINTS, PROCESS_STEPS, HERO_TRUST_BADGES, GENERAL_BLOG_POSTS, COST_BLOG_POSTS, clip_desc

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"

# ============================================================================
# OPEN GRAPH IMAGE per category — so social/AI previews differ by service/topic
# instead of every page sharing one og-default.jpg.
# ============================================================================
OG_BY_SERVICE = {
    "concrete-driveways":     "/images/photo-concrete-driveway.jpg",
    "concrete-patios":        "/images/photo-concrete-patio.jpg",
    "concrete-pool-decks":    "/images/photo-pool-deck.jpg",
    "stamped-concrete":       "/images/photo-stamped-concrete.jpg",
    "concrete-slabs":         "/images/photo-concrete-slab.jpg",
    "concrete-resurfacing":   "/images/photo-resurfacing.jpg",
    "paver-driveways":        "/images/photo-paver-driveway.jpg",
    "paver-patios-walkways":  "/images/photo-paver-patio.jpg",
    "pool-deck-pavers":       "/images/photo-pool-deck-pavers.jpg",
    "paver-sealing":          "/images/photo-paver-sealing.jpg",
}
OG_CITY      = "/images/photo-paver-driveway.jpg"
OG_GUIDES    = "/images/photo-stamped-concrete.jpg"
OG_GLOSSARY  = "/images/photo-concrete-patio.jpg"

def og_url(service_slug=None, path=None):
    """Absolute OG image URL for a given service slug (or explicit path)."""
    if path:
        return f"{SITE}{path}"
    return f"{SITE}{OG_BY_SERVICE.get(service_slug, '/images/og-default.jpg')}"

# ============================================================================
# CSS — Bold/Editorial design system
# ============================================================================
CSS = r"""
:root{
  /* Warm Travertine palette — ink + brass/gold + cream/sand */
  --orange:#BE9A4A;          /* gold accent (kept var name for compatibility) */
  --orange-dark:#9A7C32;     /* deep gold — links, hovers, eyebrows */
  --orange-light:#F4ECD9;    /* soft cream-gold tint */
  --gold-lt:#D9BE7E;
  --dark:#1C1813;            /* warm near-black ink */
  --white:#FBF7EF;           /* warm cream base / cards / text-on-dark */
  --card:#FFFFFF;
  --gray-bg:#ECE4D4;         /* sand — alternating sections */
  --gray-border:#E3D9C5;
  --text:#2B2820;
  --text-light:#6B6453;
  --shadow-sm:0 2px 8px rgba(40,32,16,.07);
  --shadow:0 6px 22px rgba(40,32,16,.10);
  --shadow-lg:0 16px 44px rgba(40,32,16,.16);
  --radius:12px;
  --radius-lg:18px;
  --font-head:'Outfit','Inter',sans-serif;
  --font-body:'Inter','Helvetica Neue',Arial,sans-serif;
  --container:1200px;
  --container-wide:1380px;
  /* compat aliases */
  --ink:#1C1813; --ink-soft:#2A241B; --paper:#FBF7EF; --paper-deep:#ECE4D4;
  --orange-deep:#9A7C32; --rule:#E3D9C5; --gray:#6B6453; --muted:#9A958A;
  --font-display:'Outfit','Inter',sans-serif; --font-editorial:'Georgia',serif;
  --font-mono:'Courier New',monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;scroll-padding-top:80px}
body{font-family:var(--font-body);font-size:16px;line-height:1.65;color:var(--text);background:var(--white);overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--dark);text-decoration:none;transition:color .2s}
a:hover{color:var(--orange-dark)}
h1,h2,h3,h4,h5{font-family:var(--font-head);font-weight:700;line-height:1.15;letter-spacing:-.02em;color:var(--dark)}
h1{font-size:clamp(2rem,5vw,3.2rem)}
h2{font-size:clamp(1.6rem,3.5vw,2.4rem)}
h3{font-size:clamp(1.15rem,2vw,1.45rem)}
p{margin:0 0 1rem}
ul,ol{margin:0;padding:0}
.container{max-width:var(--container);margin:0 auto;padding:0 24px}
.container-wide{max-width:var(--container-wide);margin:0 auto;padding:0 24px}

/* MONO LABEL */
.mono-label{display:inline-flex;align-items:center;gap:8px;font-size:.78rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--orange-dark);font-family:var(--font-body)}
.mono-label::before{content:"";width:22px;height:2px;background:var(--orange);display:inline-block;flex-shrink:0}
.mono-label.no-bar::before{display:none}
.mono-label.on-dark{color:rgba(255,248,236,.85)}
.mono-label.on-dark::before{background:var(--orange)}

/* SECTION NUMBERS */
.section-num{font-family:var(--font-head);font-size:clamp(2rem,6vw,3.8rem);color:var(--orange);line-height:1;letter-spacing:-.03em;display:inline-block}
.section-head{margin-bottom:3rem;display:grid;grid-template-columns:auto 1fr;gap:0 40px;align-items:start;border-bottom:3px solid var(--gray-border);padding-bottom:1.6rem}
.section-head-num{font-family:var(--font-head);font-size:clamp(2.8rem,7vw,4.5rem);color:var(--orange);line-height:1;letter-spacing:-.04em;padding-right:10px}
.section-head-meta{display:flex;flex-direction:column;gap:8px}
.section-head h2{font-size:clamp(1.6rem,3.5vw,2.4rem)}
.section-head h2 em{font-style:normal;color:var(--orange-dark)}
.section-head-text p{font-size:1rem;color:var(--text-light);margin:0}
.kicker{display:flex;align-items:baseline;gap:14px;margin-bottom:1.4rem;padding-bottom:.8rem;border-bottom:2px solid var(--orange)}
.kicker-num{font-family:var(--font-head);font-size:1.8rem;color:var(--orange);line-height:1;font-weight:800}
.kicker-label{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--dark)}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:9px;padding:14px 28px;font-family:var(--font-head);font-weight:700;font-size:.95rem;letter-spacing:.01em;text-decoration:none;cursor:pointer;border:2px solid transparent;border-radius:40px;transition:all .22s ease;white-space:nowrap;position:relative}
.btn-ink,.btn-ink:hover{background:var(--dark);color:var(--white);border-color:var(--dark)}
.btn-ink:hover{background:var(--orange);border-color:var(--orange);color:var(--dark);transform:translateY(-2px);box-shadow:var(--shadow)}
.btn-orange{background:var(--orange);color:var(--dark);border-color:var(--orange);font-weight:700}
.btn-orange:hover{background:var(--orange-dark);border-color:var(--orange-dark);color:var(--white);transform:translateY(-2px);box-shadow:0 6px 20px rgba(190,154,74,.4)}
.btn-outline{background:transparent;color:var(--dark);border-color:var(--dark)}
.btn-outline:hover{background:var(--dark);color:var(--white)}
.btn-outline-light{background:transparent;color:var(--white);border-color:rgba(255,255,255,.7)}
.btn-outline-light:hover{background:var(--white);color:var(--dark);border-color:var(--white)}
.btn-arrow::after{content:"→";font-size:1rem;margin-left:2px;transition:transform .2s}
.btn:hover .btn-arrow::after,.btn-arrow:hover::after{transform:translateX(4px)}

/* TOP BANNER */
.top-bar{background:var(--dark);color:rgba(255,255,255,.85);padding:9px 0;font-size:.78rem;letter-spacing:.06em}
.top-bar-inner{max-width:var(--container-wide);margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}
.top-bar a{color:rgba(255,255,255,.85)}
.top-bar a:hover{color:var(--orange)}
.top-bar-edition{color:rgba(255,255,255,.4);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase}

/* HEADER */
.site-header{position:sticky;top:0;z-index:100;background:var(--white);border-bottom:1px solid var(--gray-border);box-shadow:var(--shadow-sm)}
.nav-bar{display:flex;align-items:center;justify-content:space-between;padding:10px 24px;max-width:var(--container-wide);margin:0 auto;gap:1.2rem}
.brand{display:flex;align-items:center;gap:4px;text-decoration:none;flex-shrink:0}
.brand img{height:72px;width:auto}
.brand{display:flex;align-items:center;gap:4px;text-decoration:none;flex-shrink:0}
.brand img{height:52px;width:auto}
.brand-mark{width:44px;height:44px;background:var(--orange);display:grid;place-items:center;border-radius:6px;flex-shrink:0}
.brand-mark span{color:var(--dark);font-family:var(--font-head);font-size:1.3rem;font-weight:800;line-height:1}
.brand-text{display:flex;flex-direction:column;line-height:1;margin-left:4px}
.brand-name{font-family:var(--font-head);font-weight:800;font-size:1.25rem;color:var(--dark);letter-spacing:-.02em}
.brand-tag{font-size:.65rem;letter-spacing:.14em;color:var(--orange-dark);text-transform:uppercase;margin-top:3px;font-weight:600}
.nav-menu{display:flex;align-items:center;gap:1.6rem;list-style:none}
.nav-menu li{position:relative}
.nav-menu>li>a{font-family:var(--font-head);font-weight:600;color:var(--text);font-size:.92rem;padding:8px 2px;position:relative;white-space:nowrap}
.nav-menu>li>a::after{content:"";position:absolute;bottom:2px;left:0;width:0;height:2px;background:var(--orange);transition:width .22s}
.nav-menu>li:hover>a::after,.nav-menu>li.active>a::after{width:100%}
.nav-menu>li:hover>a,.nav-menu>li.active>a{color:var(--dark)}
.dropdown{position:absolute;top:calc(100% + 10px);left:0;background:var(--white);min-width:240px;border-radius:var(--radius);box-shadow:var(--shadow-lg);padding:8px 0;opacity:0;visibility:hidden;transform:translateY(-6px);transition:all .22s;z-index:99;border:1px solid var(--gray-border)}
.nav-menu li:hover .dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.dropdown a{display:block;padding:10px 20px;font-size:.9rem;color:var(--text);font-weight:500;transition:all .15s}
.dropdown a:hover{background:var(--orange-light);color:var(--orange-dark)}
.dropdown a .dot{color:var(--orange);margin-right:8px;font-size:.7rem}
.nav-cta{display:flex;align-items:center;gap:14px;flex-shrink:0}
.nav-phone{display:flex;align-items:center;gap:7px;color:var(--dark);font-weight:700;font-size:.9rem;white-space:nowrap;font-family:var(--font-head)}
.nav-phone:hover{color:var(--orange-dark)}
.nav-phone svg{width:16px;height:16px;color:var(--orange);flex-shrink:0}
.menu-toggle{display:none;background:none;border:none;cursor:pointer;padding:6px;color:var(--dark)}
.menu-toggle svg{width:26px;height:26px}

/* BREADCRUMBS */
.breadcrumbs{background:var(--gray-bg);padding:14px 0;border-bottom:1px solid var(--gray-border)}
.breadcrumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:6px;font-size:.82rem;color:var(--text-light)}
.breadcrumbs li{display:flex;align-items:center;gap:6px}
.breadcrumbs li::after{content:"/";color:var(--gray-border)}
.breadcrumbs li:last-child::after{display:none}
.breadcrumbs a{color:var(--orange-dark);font-weight:500}
.breadcrumbs a:hover{color:var(--dark)}
.breadcrumbs li:last-child{color:var(--dark);font-weight:600}

/* HERO — full photo background */
.hero{position:relative;min-height:600px;display:flex;align-items:center;overflow:hidden;background:#111}
.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(105deg,rgba(10,10,10,.82) 0%,rgba(10,10,10,.55) 55%,rgba(10,10,10,.25) 100%);z-index:1}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.hero-inner{max-width:var(--container-wide);margin:0 auto;padding:100px 24px 80px;display:grid;grid-template-columns:1.1fr .9fr;gap:50px;align-items:center;position:relative;z-index:2;width:100%}
.hero-label{display:flex;align-items:center;gap:12px;font-size:.78rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);margin-bottom:22px}
.hero-label::before{content:"";width:28px;height:2px;background:var(--orange);flex-shrink:0}
.hero-h1{font-family:var(--font-head);font-weight:800;font-size:clamp(2.4rem,5.5vw,4rem);line-height:1.08;letter-spacing:-.03em;color:var(--white);margin-bottom:1.4rem}
.hero-h1 em{font-style:normal;color:var(--orange)}
.hero-h1 .stop{color:var(--orange)}
.hero-sub{font-size:1.1rem;line-height:1.6;color:rgba(255,255,255,.85);margin-bottom:2rem;max-width:540px}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:2.4rem}
.hero-meta{display:flex;flex-wrap:wrap;gap:24px 36px;border-top:1px solid rgba(255,255,255,.2);padding-top:1.6rem}
.hero-meta div{display:flex;flex-direction:column;gap:3px}
.hero-meta strong{font-family:var(--font-head);font-size:1.6rem;color:var(--white);font-weight:800;letter-spacing:-.02em;line-height:1}
.hero-meta span{font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.6)}
/* Right side: photo grid */
.hero-art{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;height:440px}
.hero-photo{overflow:hidden;border-radius:8px}
.hero-photo img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
.hero-photo:hover img{transform:scale(1.04)}
.hero-photo:first-child{grid-row:span 2;border-radius:12px}
.hero-art-tag{display:none}
.hero-art-caption{display:none}

/* PAGE HERO */
.page-hero{background:linear-gradient(135deg,var(--dark) 0%,#2a2a2a 100%);color:var(--white);padding:70px 0;position:relative;overflow:hidden}
.page-hero::after{content:"";position:absolute;right:-60px;top:-60px;width:300px;height:300px;background:radial-gradient(circle,rgba(190,154,74,.15),transparent 70%);pointer-events:none}
.page-hero-inner{max-width:var(--container);margin:0 auto;padding:0 24px;position:relative;z-index:1}
.page-hero .mono-label{color:var(--orange);margin-bottom:12px}
.page-hero .mono-label::before{background:var(--orange)}
.page-hero h1{color:var(--white);margin:0 0 1.2rem;font-size:clamp(2rem,5vw,3.4rem)}
.page-hero h1 em{font-style:normal;color:var(--orange)}
.page-hero h1 .stop{color:var(--orange)}
.page-hero-sub{font-size:1.05rem;line-height:1.6;color:rgba(255,255,255,.8);max-width:740px;margin-bottom:2rem}
.page-hero-trust{display:flex;flex-wrap:wrap;gap:16px 32px;border-top:1px solid rgba(255,255,255,.15);padding-top:1.4rem}
.page-hero-trust span{font-size:.82rem;color:rgba(255,255,255,.75);letter-spacing:.04em;display:flex;align-items:center;gap:6px}
.page-hero-trust span::before{content:"✓";color:var(--orange);font-weight:700}

/* TICKER */
.ticker{background:var(--orange);color:var(--dark);overflow:hidden;border-top:1px solid var(--orange-dark);border-bottom:1px solid var(--orange-dark)}
.ticker-inner{display:flex;animation:tickerScroll 50s linear infinite;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:12px 0;white-space:nowrap}
.ticker-inner span{padding:0 28px;flex-shrink:0}
.ticker-inner span::after{content:"●";margin-left:28px;font-size:.5rem;vertical-align:middle;opacity:.6}
@keyframes tickerScroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* SECTIONS */
section{padding:80px 0}
section.tight{padding:48px 0}

/* PROOF STRIP */
.proof-strip{background:var(--white);padding:32px 0;border-bottom:1px solid var(--gray-border);border-top:4px solid var(--orange)}
.proof-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:24px;max-width:var(--container-wide);margin:0 auto;padding:0 24px}
.proof-item{display:flex;flex-direction:column;gap:4px;padding-left:16px;border-left:3px solid var(--orange)}
.proof-num{font-family:var(--font-head);font-size:clamp(1.5rem,3vw,2.2rem);color:var(--dark);font-weight:800;line-height:1}
.proof-label{font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-light);font-weight:500}

/* SERVICES GRID */
.services-section{background:var(--gray-bg)}
.services-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:.5rem}
.service-card{background:var(--white);border-radius:var(--radius-lg);padding:32px 26px;text-decoration:none;color:var(--text);transition:all .25s ease;display:flex;flex-direction:column;min-height:290px;box-shadow:var(--shadow-sm);border:1px solid var(--gray-border)}
.service-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);border-color:var(--orange)}
.service-card-num{font-size:.76rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange);margin-bottom:14px;font-family:var(--font-head)}
.service-card h3{font-family:var(--font-head);font-weight:700;font-size:1.55rem;line-height:1.1;color:var(--dark);margin:0 0 .8rem}
.service-card-desc{font-size:.94rem;color:var(--text-light);line-height:1.55;flex-grow:1;margin-bottom:1.2rem}
.service-card-cta{font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--orange-dark);display:flex;align-items:center;gap:8px}
.service-card-cta::after{content:"→";font-size:1rem;transition:transform .22s}
.service-card:hover .service-card-cta::after{transform:translateX(5px)}

/* PHOTO GALLERY (homepage portfolio section) */
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.gallery-item{overflow:hidden;border-radius:var(--radius);aspect-ratio:1/1;position:relative}
.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .4s ease}
.gallery-item:hover img{transform:scale(1.06)}
.gallery-item:first-child{grid-column:span 1;aspect-ratio:1/1}
.gallery-caption{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(0deg,rgba(0,0,0,.7),transparent);color:#fff;padding:14px 16px 12px;font-size:.82rem;font-weight:600;letter-spacing:.04em;opacity:0;transition:opacity .3s}
.gallery-item:hover .gallery-caption{opacity:1}

/* WHY US */
.why-section{background:var(--white)}
.why-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:0}
.why-item{padding:32px 24px;border-bottom:1px solid var(--gray-border);display:grid;grid-template-columns:70px 1fr;gap:20px;align-items:start}
.why-item:nth-child(odd){border-right:1px solid var(--gray-border)}
.why-num{font-family:var(--font-head);font-size:2.4rem;color:var(--orange);font-weight:800;line-height:1}
.why-item h3{font-size:1.2rem;margin-bottom:.6rem;font-weight:700;line-height:1.2}
.why-item p{font-size:.94rem;color:var(--text-light);line-height:1.6;margin:0}

/* AREAS */
.areas-section{background:var(--dark)}
.areas-section h2{color:var(--white)}
.areas-section h2 em{color:var(--orange)}
.areas-section .section-head{border-bottom-color:rgba(255,255,255,.15)}
.areas-section .section-head-text p{color:rgba(255,255,255,.65)}
.areas-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:.5rem}
.area-card{padding:22px 20px;border-radius:var(--radius);background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);text-decoration:none;color:var(--white);transition:all .22s;display:flex;flex-direction:column;gap:6px}
.area-card:hover{background:var(--orange);border-color:var(--orange);transform:translateY(-2px)}
.area-card:hover .area-card-name,.area-card:hover .area-card-meta,.area-card:hover .area-card-arrow{color:var(--dark)}
.area-card-name{font-family:var(--font-head);font-weight:700;font-size:1.2rem;color:var(--white)}
.area-card-meta{font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.5)}
.area-card-arrow{margin-top:auto;font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--orange);display:flex;align-items:center;gap:6px}

/* PROCESS */
.process-section{background:var(--gray-bg)}
.process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:.5rem}
.process-step{background:var(--white);border-radius:var(--radius-lg);padding:32px 24px;box-shadow:var(--shadow-sm);border:1px solid var(--gray-border);position:relative}
.process-step::before{content:attr(data-num);position:absolute;top:-12px;left:24px;background:var(--orange);color:var(--dark);font-family:var(--font-head);font-weight:800;font-size:.82rem;padding:4px 12px;border-radius:20px;letter-spacing:.06em}
.process-num{font-family:var(--font-head);font-size:2.6rem;color:var(--orange);font-weight:800;line-height:1;margin-bottom:1rem}
.process-step h3{font-size:1.18rem;margin-bottom:.6rem;font-weight:700}
.process-step p{font-size:.9rem;color:var(--text-light);line-height:1.55;margin:0}

/* REVIEWS */
.reviews-section{background:var(--white)}
.reviews-rating-bar{display:flex;align-items:center;gap:12px;padding:16px 20px;background:var(--orange-light);border:1px solid rgba(190,154,74,.3);border-radius:var(--radius);margin-bottom:2.4rem;flex-wrap:wrap}
.reviews-rating-bar strong{font-family:var(--font-head);color:var(--dark);font-size:1.5rem;font-weight:800}
.reviews-rating-bar .stars{color:var(--orange);font-size:1.1rem;letter-spacing:2px}
.reviews-rating-bar span{font-size:.85rem;color:var(--text-light)}
.reviews-rating-bar a{color:var(--orange-dark);font-weight:600;font-size:.85rem;margin-left:auto}
.reviews-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.review-card{background:var(--white);border-radius:var(--radius-lg);padding:28px;box-shadow:var(--shadow-sm);border:1px solid var(--gray-border);display:flex;flex-direction:column;gap:.9rem;position:relative}
.review-quote-mark{font-family:Georgia,serif;font-size:4.5rem;line-height:.65;color:var(--orange);position:absolute;top:18px;right:20px;opacity:.2;font-weight:700}
.review-stars{color:var(--orange);font-size:.95rem;letter-spacing:2px}
.review-text{font-size:.98rem;line-height:1.62;color:var(--text);flex-grow:1;margin:0}
.review-meta{border-top:1px solid var(--gray-border);padding-top:1rem;display:flex;flex-direction:column;gap:3px;margin-top:auto}
.review-author{font-weight:700;font-size:.9rem;color:var(--dark)}
.review-where{font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--text-light)}
.review-verified{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--success);font-weight:600;display:inline-flex;align-items:center;gap:5px}

/* CHECKLIST */
.checklist-section{background:var(--gray-bg)}
.checklist-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:.5rem}
.checklist-card{background:var(--white);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);border:1px solid var(--gray-border)}
.checklist-card-head{background:var(--dark);color:var(--white);padding:16px 20px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.checklist-card-head strong{font-family:var(--font-head);font-weight:600;font-size:1rem}
.checklist-card-head .ck-num{color:var(--orange);font-weight:800;font-size:1rem}
.checklist-card-head .ck-count{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.5);margin-left:auto}
.checklist-card ol{padding:16px 20px 20px 38px;list-style:decimal;font-size:.88rem;line-height:1.55;color:var(--text)}
.checklist-card ol li{margin-bottom:.45rem}
.checklist-card ol li::marker{color:var(--orange);font-weight:700}

/* NEIGHBORHOODS */
.neighborhoods-section{background:var(--white)}
.neighborhood-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:9px;margin:1rem 0 1.6rem}
.neighborhood-pill{padding:11px 16px;background:var(--white);border:1.5px solid var(--gray-border);color:var(--text);font-weight:500;font-size:.9rem;border-radius:var(--radius);display:flex;align-items:center;gap:9px;transition:all .2s;cursor:default}
.neighborhood-pill::before{content:"";width:6px;height:6px;background:var(--orange);border-radius:50%;flex-shrink:0}
.neighborhood-pill:hover{border-color:var(--orange);background:var(--orange-light);color:var(--dark)}
.zips-bar{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-top:1.6rem;padding-top:1.4rem;border-top:1px solid var(--gray-border)}
.zips-bar-label{font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--text-light);font-weight:600;margin-right:8px}
.zip-tag{padding:5px 10px;background:var(--dark);color:var(--white);font-size:.8rem;font-weight:600;border-radius:5px}

/* PRICING TABLE */
.pricing-section{background:var(--gray-bg)}
.pricing-wrap{background:var(--white);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--gray-border)}
.pricing-head-bar{background:var(--dark);color:var(--white);padding:18px 24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem}
.pricing-head-bar h3{font-family:var(--font-head);font-weight:700;color:var(--white);font-size:1.35rem;margin:0}
.pricing-head-bar h3 em{color:var(--orange);font-style:normal}
.pricing-head-meta{font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.6)}
table.pricing-table{width:100%;border-collapse:collapse}
.pricing-table thead{background:var(--gray-bg);border-bottom:2px solid var(--gray-border)}
.pricing-table th{padding:13px 20px;text-align:left;font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--dark)}
.pricing-table th:last-child,.pricing-table td:last-child{text-align:right}
.pricing-table td{padding:14px 20px;border-bottom:1px solid var(--gray-border);color:var(--text);vertical-align:top}
.pricing-table td:first-child{font-weight:600;color:var(--dark)}
.pricing-table .price{font-family:var(--font-head);font-weight:800;color:var(--orange-dark);white-space:nowrap;font-size:.95rem}
.pricing-table tr:last-child td{border-bottom:none}
.pricing-table tr:hover td{background:var(--orange-light)}
.pricing-note{padding:12px 20px;background:var(--gray-bg);font-size:.8rem;color:var(--text-light);border-top:1px solid var(--gray-border)}
.pricing-note a{color:var(--orange-dark);font-weight:600}

/* STAT BADGE */
.stat-badge{margin:2rem 0;padding:20px 24px;background:var(--orange-light);border-left:5px solid var(--orange);border-radius:0 var(--radius) var(--radius) 0;display:flex;align-items:center;gap:20px}
.stat-badge-num{font-family:var(--font-head);font-size:2.4rem;color:var(--orange-dark);font-weight:800;line-height:1;flex-shrink:0}
.stat-badge-body strong{font-family:var(--font-head);font-weight:700;font-size:1.1rem;color:var(--dark);display:block;margin-bottom:3px}
.stat-badge-body small{font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--text-light)}

/* PULL QUOTE */
.pull-quote{max-width:780px;margin:2.8rem auto;padding:2rem;text-align:center;border-top:3px solid var(--orange);border-bottom:3px solid var(--orange)}
.pull-quote p{font-family:Georgia,serif;font-style:italic;font-size:clamp(1.3rem,2.5vw,1.8rem);line-height:1.3;color:var(--dark);margin:0}
.pull-quote p::before{content:"\201C";color:var(--orange);font-weight:700;margin-right:4px}
.pull-quote p::after{content:"\201D";color:var(--orange);font-weight:700;margin-left:4px}
.pull-quote cite{display:block;margin-top:.9rem;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-style:normal;color:var(--text-light)}

/* FEATURES / MISTAKES LIST */
.features-list{display:flex;flex-direction:column;max-width:880px;margin:0 auto;border-top:1px solid var(--gray-border)}
.feature-row{padding:26px 0;border-bottom:1px solid var(--gray-border);display:grid;grid-template-columns:70px 1fr;gap:24px;align-items:start}
.feature-num{font-family:var(--font-head);font-size:2.2rem;color:var(--orange);font-weight:800;line-height:1}
.feature-body h3{font-size:1.22rem;margin-bottom:.6rem;font-weight:700;line-height:1.2}
.feature-body p{font-size:.96rem;color:var(--text-light);line-height:1.6;margin:0}

/* FAQ */
.faq-section{background:var(--white)}
.faq-list{max-width:840px;margin:0 auto;border-top:1px solid var(--gray-border)}
.faq-list details{border-bottom:1px solid var(--gray-border)}
.faq-list summary{padding:22px 0;cursor:pointer;list-style:none;display:flex;align-items:center;gap:16px;font-weight:700;font-size:1.05rem;line-height:1.3;color:var(--dark)}
.faq-list summary::-webkit-details-marker{display:none}
.faq-list summary::before{content:"+";color:var(--orange);font-size:1.4rem;font-weight:400;flex-shrink:0;width:24px;font-family:var(--font-head)}
.faq-list details[open] summary::before{content:"−"}
.faq-list details[open] summary{color:var(--orange-dark)}
.faq-list .faq-body{padding:0 0 22px 40px;font-size:.97rem;line-height:1.65;color:var(--text-light)}
.faq-list .faq-body p{margin-bottom:.9rem}

/* RELATED BOX */
.related-box{background:var(--dark);color:var(--white);padding:28px 28px;border-radius:var(--radius-lg)}
.related-box-label{font-size:.74rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange);margin-bottom:10px}
.related-box h3{font-family:var(--font-head);color:var(--white);font-size:1.3rem;margin-bottom:1.4rem;font-weight:700}
.related-box ul{list-style:none}
.related-box li{border-bottom:1px solid rgba(255,255,255,.1)}
.related-box li a{display:block;padding:9px 0;color:rgba(255,255,255,.8);font-size:.92rem;transition:all .18s}
.related-box li a:hover{color:var(--orange);padding-left:6px}

/* CONTACT BANNER */
.contact-banner{background:var(--dark);color:var(--white);padding:24px 28px;border-radius:var(--radius-lg);margin:2.4rem 0;display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center;border-left:5px solid var(--orange)}
.contact-banner-text strong{font-family:var(--font-head);font-size:1.3rem;color:var(--white);display:block;margin-bottom:3px;font-weight:700}
.contact-banner-text span{font-size:.82rem;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.6)}
.contact-banner-cta{display:flex;gap:10px;flex-wrap:wrap}

/* FINAL CTA */
.final-cta{background:var(--orange);padding:80px 0;text-align:center;border-top:1px solid var(--orange-dark)}
.final-cta .mono-label{color:var(--dark);justify-content:center}
.final-cta .mono-label::before{background:var(--dark)}
.final-cta h2{color:var(--dark);margin:1rem auto 1.2rem;max-width:720px;font-size:clamp(1.8rem,4vw,3rem)}
.final-cta h2 em{font-style:normal;color:rgba(0,0,0,.55)}
.final-cta-sub{font-size:1.05rem;color:rgba(0,0,0,.7);max-width:540px;margin:0 auto 1.8rem}
.final-cta-phone{font-family:var(--font-head);font-size:clamp(1.8rem,4vw,2.6rem);color:var(--dark);font-weight:800;display:inline-block;margin-bottom:1.4rem;text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:6px}
.final-cta-phone:hover{color:var(--white)}
.final-cta-buttons{display:flex;justify-content:center;gap:12px;flex-wrap:wrap}

/* FOOTER */
footer{background:var(--dark);color:rgba(255,255,255,.75);padding:70px 0 0}
.footer-grid{max-width:var(--container-wide);margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:44px;margin-bottom:3rem}
.footer-col .ftitle{font-family:var(--font-head);color:var(--orange);font-size:.76rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;margin-bottom:1rem}
.footer-brand-bar{display:flex;align-items:center;gap:12px;margin-bottom:1.1rem}
.footer-brand-mark{width:42px;height:42px;background:var(--orange);display:grid;place-items:center;border-radius:7px}
.footer-brand-mark span{color:var(--dark);font-family:var(--font-head);font-size:1.2rem;font-weight:800}
.footer-brand strong{font-family:var(--font-head);font-weight:800;font-size:1.35rem;color:var(--white)}
.footer-col p{color:rgba(255,255,255,.55);line-height:1.65;font-size:.92rem;margin-bottom:.75rem}
.footer-col ul{list-style:none}
.footer-col li{margin-bottom:.5rem}
.footer-col a{color:rgba(255,255,255,.65);font-size:.9rem;transition:color .18s}
.footer-col a:hover{color:var(--orange)}
.footer-contact-item{display:flex;gap:10px;margin-bottom:.6rem;font-size:.9rem;color:rgba(255,255,255,.65);align-items:flex-start}
.footer-contact-item svg{width:15px;height:15px;color:var(--orange);flex-shrink:0;margin-top:3px}
.footer-hours{font-size:.8rem;color:rgba(255,255,255,.5);line-height:1.75;margin-top:.9rem}
.footer-bottom{border-top:1px solid rgba(255,255,255,.1);padding:1.4rem 24px;max-width:var(--container-wide);margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.8rem;font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.4)}
.footer-bottom a{color:rgba(255,255,255,.45)}
.footer-bottom a:hover{color:var(--orange)}
.footer-bigtype{padding:1.6rem 24px 1.2rem;text-align:center;border-top:1px solid rgba(255,255,255,.08);max-width:var(--container-wide);margin:0 auto}
.footer-bigtype span{font-family:var(--font-head);font-size:clamp(2rem,7vw,4.5rem);color:rgba(190,154,74,.25);font-weight:800;letter-spacing:-.03em;display:block}

/* CONTACT FLOAT */
.contact-float{position:fixed;bottom:22px;right:22px;z-index:9999;display:flex;flex-direction:column;gap:10px;align-items:flex-end}
.contact-float-btn{display:inline-flex;align-items:center;gap:8px;background:var(--dark);color:var(--white);padding:12px 18px;font-weight:700;font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;border-radius:var(--radius);box-shadow:var(--shadow-lg);transition:all .22s}
.contact-float-btn:hover{background:var(--orange);color:var(--dark);transform:translateY(-2px)}
.contact-float-btn svg{width:16px;height:16px}
.contact-float-btn.wa{background:var(--whatsapp);color:var(--white)}
.contact-float-btn.wa:hover{background:#1da851;color:var(--white)}

/* CONTACT FORM */
.form-wrap{background:var(--white);border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:32px;box-shadow:var(--shadow-sm)}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.form-grid label{grid-column:span 1;display:flex;flex-direction:column;gap:6px;font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--dark)}
.form-grid label.full{grid-column:span 2}
.form-grid input,.form-grid select,.form-grid textarea{font-family:var(--font-body);font-size:.96rem;color:var(--text);background:var(--gray-bg);border:1.5px solid var(--gray-border);border-radius:var(--radius);padding:12px 14px;transition:all .2s}
.form-grid input:focus,.form-grid select:focus,.form-grid textarea:focus{outline:none;border-color:var(--orange);background:var(--white);box-shadow:0 0 0 3px rgba(190,154,74,.15)}
.form-grid textarea{min-height:130px;resize:vertical}
.form-submit{grid-column:span 2;justify-self:start}

/* BLOG */
.blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.blog-card{background:var(--white);border-radius:var(--radius-lg);padding:28px;text-decoration:none;color:var(--text);transition:all .22s;display:flex;flex-direction:column;min-height:240px;box-shadow:var(--shadow-sm);border:1px solid var(--gray-border)}
.blog-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg);border-color:var(--orange)}
.blog-card-meta{font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--orange);margin-bottom:.9rem;display:flex;justify-content:space-between;gap:1rem}
.blog-card h3{font-family:var(--font-head);font-weight:700;font-size:1.18rem;line-height:1.2;color:var(--dark);margin:0 0 .8rem;flex-grow:1}
.blog-card-cta{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--orange-dark);margin-top:auto;display:flex;align-items:center;gap:6px}
.blog-card-cta::after{content:"→";display:inline-block;transition:transform .22s}
.blog-card:hover .blog-card-cta::after{transform:translateX(4px)}

/* BLOG POST */
.post-article{max-width:760px;margin:0 auto;padding:56px 0}
.post-meta-bar{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-light);display:flex;flex-wrap:wrap;gap:20px;margin-bottom:1.4rem}
.post-meta-bar .cat{color:var(--orange-dark);font-weight:700}
.post-article h1{font-family:var(--font-head);font-weight:800;font-size:clamp(1.9rem,4vw,3rem);line-height:1.1;margin-bottom:1.3rem}
.post-lede{font-size:1.2rem;line-height:1.5;color:var(--text-light);font-style:italic;margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid var(--gray-border)}
.post-article h2{font-family:var(--font-head);font-weight:700;font-size:clamp(1.4rem,2.8vw,1.9rem);margin:2.4rem 0 1rem;border-top:2px solid var(--gray-border);padding-top:2rem}
.post-article h3{font-family:var(--font-head);font-weight:700;font-size:1.25rem;margin:1.6rem 0 .8rem}
.post-article p{font-size:1.05rem;line-height:1.72;margin-bottom:1.1rem}
.post-article ul,.post-article ol{padding-left:1.4rem;margin-bottom:1.3rem}
.post-article li{margin-bottom:.55rem;font-size:1.02rem;line-height:1.65}
.post-article li::marker{color:var(--orange);font-weight:700}
.post-article blockquote{border-left:4px solid var(--orange);padding:.5rem 0 .5rem 1.4rem;font-size:1.15rem;line-height:1.45;color:var(--text-light);margin:1.8rem 0;font-style:italic}
.post-article .post-table{width:100%;border-collapse:collapse;margin:2rem 0;font-size:.92rem;border:1px solid var(--gray-border);border-radius:var(--radius);overflow:hidden}
.post-article .post-table th{background:var(--dark);color:var(--white);padding:11px 16px;text-align:left;font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700}
.post-article .post-table td{padding:11px 16px;border-bottom:1px solid var(--gray-border);color:var(--text)}
.post-article .post-table tr:nth-child(even) td{background:var(--gray-bg)}
.post-article .post-key-takeaway{background:var(--orange-light);border-left:4px solid var(--orange);padding:1.2rem 1.4rem;margin:1.8rem 0;border-radius:0 var(--radius) var(--radius) 0}
.post-article .post-key-takeaway strong{font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--orange-dark);display:block;margin-bottom:.5rem;font-weight:700}
.post-author{margin:2.5rem 0 0;padding:1.8rem 0;border-top:2px solid var(--gray-border);display:flex;align-items:center;gap:16px}
.post-author-avatar{width:52px;height:52px;background:var(--orange);border-radius:50%;display:grid;place-items:center;color:var(--dark);font-family:var(--font-head);font-size:1.3rem;font-weight:800;flex-shrink:0}
.post-author-info strong{display:block;font-family:var(--font-head);font-weight:700;font-size:1rem;color:var(--dark);margin-bottom:2px}
.post-author-info span{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-light)}

/* PAGE ARTICLE */
.page-article{max-width:800px;margin:0 auto;padding:50px 0}
.page-article p{font-size:1.05rem;line-height:1.7;margin-bottom:1rem}
.page-article h2{font-family:var(--font-head);font-weight:700;font-size:clamp(1.5rem,3vw,2rem);margin:2.2rem 0 1rem;border-top:2px solid var(--gray-border);padding-top:1.8rem}
.page-article h3{font-family:var(--font-head);font-weight:700;font-size:1.25rem;margin:1.5rem 0 .7rem}
.page-article ul,.page-article ol{padding-left:1.4rem;margin-bottom:1.3rem}
.page-article li{margin-bottom:.5rem;font-size:1.02rem;line-height:1.65}
.page-article li::marker{color:var(--orange);font-weight:700}
.post-lede{font-size:1.2rem;line-height:1.5;color:var(--text-light);font-style:italic;margin-bottom:1.8rem;padding-bottom:1.8rem;border-bottom:1px solid var(--gray-border)}
.post-key-takeaway{background:var(--orange-light);border-left:4px solid var(--orange);padding:1.1rem 1.4rem;margin:1.6rem 0;border-radius:0 var(--radius) var(--radius) 0}
.post-key-takeaway strong{font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--orange-dark);display:block;margin-bottom:.5rem;font-weight:700}

/* INTRO PROSE */
.intro-prose{max-width:800px;margin:0 auto;font-size:1.05rem;line-height:1.72;color:var(--text)}
.intro-prose p:first-child::first-letter{font-family:var(--font-head);font-size:4rem;float:left;line-height:.9;padding:5px 12px 0 0;color:var(--orange);font-weight:800}
.intro-prose p{margin-bottom:1.1rem}
.intro-prose strong{font-weight:700;color:var(--dark)}

/* RESPONSIVE */
@media(max-width:1100px){
  .hero-inner{grid-template-columns:1fr;gap:36px}
  .hero-art{height:300px}
  .section-head{grid-template-columns:80px 1fr;gap:0 24px}
  .services-grid{grid-template-columns:repeat(2,1fr)}
  .areas-grid{grid-template-columns:repeat(2,1fr)}
  .process-grid{grid-template-columns:repeat(2,1fr)}
  .reviews-grid{grid-template-columns:repeat(2,1fr)}
  .blog-grid{grid-template-columns:repeat(2,1fr)}
  .checklist-grid{grid-template-columns:repeat(2,1fr)}
  .footer-grid{grid-template-columns:1fr 1fr;gap:32px}
  .why-grid{grid-template-columns:1fr}
  .why-item:nth-child(odd){border-right:none}
}
@media(max-width:768px){
  .top-bar-inner{justify-content:center;gap:12px}
  .top-bar-edition{display:none}
  .nav-menu{display:none;position:absolute;top:100%;left:0;right:0;flex-direction:column;background:var(--white);border-top:1px solid var(--gray-border);border-bottom:1px solid var(--gray-border);align-items:stretch;gap:0;box-shadow:var(--shadow-lg);z-index:200;max-height:calc(100vh - 92px);overflow-y:auto;-webkit-overflow-scrolling:touch}
  .nav-menu.open{display:flex}
  .nav-menu>li{border-bottom:1px solid var(--gray-border);position:relative}
  .nav-menu>li>a{display:block;padding:16px 24px;font-size:1rem}
  /* dropdowns collapsed by default on mobile */
  .nav-menu .dropdown{position:static;opacity:0;visibility:hidden;transform:none;box-shadow:none;background:var(--gray-bg);border:none;border-radius:0;max-height:0;overflow:hidden;padding:0;transition:max-height .25s ease,opacity .15s ease}
  .nav-menu>li.mobile-open>.dropdown{opacity:1;visibility:visible;max-height:80vh;padding:6px 0}
  .nav-menu .dropdown a{padding:11px 40px;font-size:.92rem;display:block}
  /* arrow indicator on parents with dropdowns */
  .nav-menu>li.has-dropdown>a::before{content:"+";float:right;color:var(--orange);font-weight:400;font-size:1.2rem;line-height:1;margin-left:8px;transition:transform .25s}
  .nav-menu>li.has-dropdown.mobile-open>a::before{content:"−"}
  .nav-menu>li.has-dropdown>a::after{display:none}
  .menu-toggle{display:block}
  .nav-phone span{display:none}
  .brand-tag{display:none}
  .hero{min-height:auto;padding:20px 0}
  .hero-inner{padding:60px 18px 50px}
  .page-hero{padding:48px 0 50px}
  section{padding:52px 0}
  .proof-grid{grid-template-columns:repeat(2,1fr);gap:16px}
  .proof-item:nth-child(5){display:none}
  .services-grid,.areas-grid,.process-grid,.reviews-grid,.blog-grid,.checklist-grid{grid-template-columns:1fr}
  .gallery-grid{grid-template-columns:1fr 1fr}
  .gallery-item:first-child{grid-column:span 1}
  .footer-grid{grid-template-columns:1fr;gap:28px}
  .related-box ul{grid-template-columns:1fr}
  .form-grid{grid-template-columns:1fr}
  .form-grid label.full,.form-submit{grid-column:span 1}
  .contact-banner{grid-template-columns:1fr}
  .feature-row{grid-template-columns:55px 1fr;gap:16px}
  .why-item{grid-template-columns:55px 1fr;gap:14px;padding:22px 0}
  .hero-art{display:none}
}
@media(max-width:520px){
  .container,.container-wide{padding:0 16px}
  .nav-bar{padding:12px 16px}
  .proof-grid{grid-template-columns:1fr 1fr}
  .stat-badge{flex-direction:column;gap:8px}
  .pricing-table{display:block;overflow-x:auto}
  .pricing-table table{min-width:480px}
  .form-wrap{padding:22px 16px}
  .hero-inner{padding:50px 16px 40px}
}
"""

# ============================================================================
# HEAD — page <head> builder
# ============================================================================
def head(title, desc, canonical, og_image=None, og_type="website", indexable=True, json_ld=None, extra_meta=""):
    """Builds the <head> section with all SEO meta, OG, fonts, CSS, and JSON-LD."""
    og_image = og_image or f"{SITE}/images/og-default.jpg"
    robots = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" if indexable else "noindex, nofollow"
    schemas_html = ""
    if json_ld:
        if isinstance(json_ld, list):
            for s in json_ld:
                schemas_html += f'<script type="application/ld+json">{json.dumps(s, separators=(",",":"))}</script>\n'
        else:
            schemas_html = f'<script type="application/ld+json">{json.dumps(json_ld, separators=(",",":"))}</script>\n'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QH57PV4QRK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-QH57PV4QRK');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="author" content="{BUSINESS["name"]}">
<meta name="geo.region" content="US-{BUSINESS["state"]}">
<meta name="geo.placename" content="{BUSINESS["city"]}, {BUSINESS["state_long"]}">
<meta name="geo.position" content="{BUSINESS["lat"]};{BUSINESS["lng"]}">
<meta name="ICBM" content="{BUSINESS["lat"]}, {BUSINESS["lng"]}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BUSINESS["name"]} — {BUSINESS["tagline"]}">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{BUSINESS["name"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" type="image/png" sizes="96x96" href="/images/favicon.png">
<link rel="icon" type="image/png" sizes="48x48" href="/images/favicon-48.png">
<link rel="shortcut icon" href="/images/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{extra_meta}
<style>{CSS}</style>
{schemas_html}</head>
'''

# ============================================================================
# HEADER — site nav (consistent across all pages)
# ============================================================================
def header(active=""):
    svc_links = "".join(
        f'<a href="/{slug}/"><span class="dot">{SERVICES[slug]["icon"]}</span>{SERVICES[slug]["name"]}</a>'
        for slug in SERVICE_ORDER
    )
    _main_cities = list(CITIES)[:8]
    city_links = "".join(
        f'<a href="/{slug}/"><span class="dot">●</span>{CITIES[slug]["name"]}, FL</a>'
        for slug in _main_cities
    ) + f'<a href="/directories/" style="font-weight:700;color:var(--orange-dark);border-top:1px solid var(--gray-border);margin-top:4px"><span class="dot">+</span>View all {len(CITIES)} service areas &rarr;</a>'
    nav_active = {
        "home":"", "services":"active", "areas":"active",
        "blog":"active", "about":"active", "contact":"active", "":""
    }
    a_serv = nav_active.get("services","") if active in ("services","service","service-city") else ""
    a_area = nav_active.get("areas","") if active in ("areas","city") else ""
    a_blog = nav_active.get("blog","") if active == "blog" else ""
    a_about = nav_active.get("about","") if active == "about" else ""
    a_cont = nav_active.get("contact","") if active == "contact" else ""

    return f'''<header class="site-header">
  <nav class="nav-bar" aria-label="Main">
    <a href="/" class="brand" aria-label="{BUSINESS["name"]} home">
      <img src="/images/logo-lwr-transparent.png" alt="{BUSINESS["name"]} — Concrete &amp; Pavers" width="240" height="121" loading="eager">
    </a>
    <ul class="nav-menu" id="navMenu">
      <li{' class="active"' if active=="home" else ''}><a href="/">Home</a></li>
      <li{' class="' + a_serv + '"' if a_serv else ''}><a href="/concrete-driveways/">Services</a>
        <div class="dropdown">{svc_links}</div>
      </li>
      <li{' class="' + a_area + '"' if a_area else ''}><a href="/lakewood-ranch/">Service Areas</a>
        <div class="dropdown">{city_links}</div>
      </li>
      <li{' class="' + a_blog + '"' if a_blog else ''}><a href="/blog/">Blog</a></li>
      <li{' class="' + a_about + '"' if a_about else ''}><a href="/about/">About</a></li>
      <li{' class="' + a_cont + '"' if a_cont else ''}><a href="/contact/">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a href="{TEL_LINK}" class="nav-phone" aria-label="Call {BUSINESS["name"]}">
        <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        <span>{BUSINESS["phone_display"]}</span>
      </a>
      <a href="/contact/#quote" class="btn btn-orange">Free Quote <span class="btn-arrow"></span></a>
      <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu" aria-expanded="false">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </nav>
</header>'''

# ============================================================================
# BREADCRUMBS
# ============================================================================
def breadcrumbs(items):
    """items: list of (label, href|None). Last item href should be None."""
    lis = ""
    for label, href in items:
        if href:
            lis += f'<li><a href="{href}">{label}</a></li>'
        else:
            lis += f'<li>{label}</li>'
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><div class="container"><ol>{lis}</ol></div></nav>'

# ============================================================================
# FOOTER
# ============================================================================
def footer():
    svc_links = "".join(
        f'<li><a href="/{slug}/">{SERVICES[slug]["name"]}</a></li>'
        for slug in SERVICE_ORDER
    )
    area_links = "".join(
        f'<li><a href="/{slug}/">{CITIES[slug]["name"]}, FL</a></li>'
        for slug in CITIES
    )
    hours_html = "<br>".join(
        f'<span>{day[:3].upper()}</span> &nbsp; {o}–{c}'
        for day, o, c in BUSINESS["hours"]
    )
    return f'''<footer>
  <div class="footer-grid">
    <div class="footer-col footer-brand">
      <div class="footer-brand-bar">
        <a href="/" style="display:inline-block;text-decoration:none">
          <img src="/images/logo-lwr-light.png" alt="Lakewood Ranch Concrete" width="230" height="116" style="height:58px;width:auto" loading="lazy">
        </a>
      </div>
      <p>{BUSINESS["tagline_long"]}</p>
      <p style="font-family:var(--font-mono);font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin-top:1rem">{BUSINESS["checklist_name"]} · Fully Insured</p>
      <div style="display:flex;gap:10px;margin-top:1.2rem">
        <a href="{BUSINESS['facebook']}" target="_blank" rel="noopener" aria-label="Facebook" style="width:40px;height:40px;border:1px solid rgba(255,255,255,.22);border-radius:50%;display:grid;place-items:center;color:var(--orange);transition:all .2s"><svg viewBox="0 0 24 24" fill="currentColor" width="19" height="19"><path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.89v2.25h3.32l-.53 3.49h-2.79V24C19.61 23.1 24 18.1 24 12.07z"/></svg></a>
        <a href="{BUSINESS['instagram']}" target="_blank" rel="noopener" aria-label="Instagram" style="width:40px;height:40px;border:1px solid rgba(255,255,255,.22);border-radius:50%;display:grid;place-items:center;color:var(--orange);transition:all .2s"><svg viewBox="0 0 24 24" fill="currentColor" width="19" height="19"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zm0 3.68a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm7.84-10.4a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0z"/></svg></a>
      </div>
    </div>
    <div class="footer-col">
      <div class="ftitle">Services</div>
      <ul>{svc_links}</ul>
    </div>
    <div class="footer-col">
      <div class="ftitle">Service Areas</div>
      <ul>{area_links}</ul>
    </div>
    <div class="footer-col">
      <div class="ftitle">Contact</div>
      <div class="footer-contact-item">
        <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        <a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a>
      </div>
      <div class="footer-contact-item">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a>
      </div>
      <div class="footer-contact-item">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        <span>{BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]}</span>
      </div>
      <p class="footer-hours">{hours_html}</p>
    </div>
  </div>
  <div class="footer-bigtype"><span>LAKEWOOD RANCH CONCRETE.</span></div>
  <div class="footer-bottom">
    <span>© 2026 {BUSINESS["legal_name"]} · Fully Insured</span>
    <span><a href="/about/">About</a> &nbsp;·&nbsp; <a href="/directories/">Directory</a> &nbsp;·&nbsp; <a href="/warranty/">Warranty</a> &nbsp;·&nbsp; <a href="/financing/">Financing</a> &nbsp;·&nbsp; <a href="/faq/">FAQ</a></span>
  </div>
</footer>'''

# ============================================================================
# WhatsApp / Contact floats
# ============================================================================
FLOAT_CONTACT = f'''<div class="contact-float">
  <a href="{TEL_LINK}" class="contact-float-btn" aria-label="Call {BUSINESS["name"]}">
    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
    Call Now
  </a>
  <a href="{WA_LINK}" target="_blank" rel="noopener" class="contact-float-btn wa" aria-label="Message us on WhatsApp">
    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.157 5.335 5.495 0 12.05 0a11.817 11.817 0 018.413 3.488 11.824 11.824 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.888-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.743-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413z"/></svg>
    WhatsApp
  </a>
</div>'''

# Compact MENU script — toggle hamburger
MENU_JS = '''<script>
(function(){
  var t=document.getElementById("menuToggle"), m=document.getElementById("navMenu");
  if(t&&m){
    t.addEventListener("click", function(){
      var o = m.classList.toggle("open");
      t.setAttribute("aria-expanded", o);
      // close any open dropdowns when menu closes
      if(!o) m.querySelectorAll("li.mobile-open").forEach(function(li){ li.classList.remove("mobile-open"); });
    });

    // Mark parents that have dropdowns + handle tap-to-expand on mobile
    var parents = m.querySelectorAll("li");
    parents.forEach(function(li){
      var dd = li.querySelector(".dropdown");
      if(!dd) return;
      li.classList.add("has-dropdown");
      var link = li.querySelector(":scope > a");
      if(!link) return;
      link.addEventListener("click", function(e){
        // only intercept on mobile
        if(window.innerWidth <= 768){
          e.preventDefault();
          // close siblings
          var siblings = li.parentNode.querySelectorAll("li.mobile-open");
          siblings.forEach(function(s){ if(s !== li) s.classList.remove("mobile-open"); });
          li.classList.toggle("mobile-open");
        }
      });
    });
  }
})();
</script>'''

# Inline contact banner (used in long pages)
def contact_banner(message="Free, no-pressure estimate within 24 hours.", subtitle="Call, text, or email — your pour, your call."):
    return f'''<aside class="contact-banner">
  <div class="contact-banner-text">
    <strong>{message}</strong>
    <span>{subtitle}</span>
  </div>
  <div class="contact-banner-cta">
    <a href="{TEL_LINK}" class="btn btn-orange">Call {BUSINESS["phone_display"]}</a>
    <a href="/contact/" class="btn btn-outline-light">Email Us</a>
  </div>
</aside>'''

# Stat badge (used on service/city pages)
def stat_badge():
    return f'''<div class="stat-badge">
  <div class="stat-badge-num">42</div>
  <div class="stat-badge-body">
    <strong>Point Install Standard — every pour &amp; paver install, start to finish.</strong>
    <small>Fully Insured · Free Estimates · Written workmanship warranty</small>
  </div>
</div>'''

# Final CTA (most pages end with this)
def final_cta(headline=None, sub=None):
    headline = headline or "Get a real estimate from a real concrete &amp; paver crew."
    sub = sub or f"Free, written, line-itemized — within 24 hours. We respond to every inquiry, every day."
    return f'''<section class="final-cta">
  <div class="container">
    <span class="mono-label">Free Estimate · No Pressure</span>
    <h2>{headline}</h2>
    <p class="final-cta-sub">{sub}</p>
    <a href="{TEL_LINK}" class="final-cta-phone">{BUSINESS["phone_display"]}</a>
    <div class="final-cta-buttons">
      <a href="/contact/#quote" class="btn btn-ink btn-arrow">Email Us</a>
      <a href="{SMS_LINK}" class="btn btn-outline">Text Us</a>
    </div>
  </div>
</section>'''

# Ticker scrolling bar (animated, used after hero)
def ticker_bar():
    items = [
        f"{BUSINESS['checklist_name']}",
        f"Fully Insured",
        f"Free estimate in 24 hours",
        f"Written workmanship warranty",
        f"Compacted base · engineered joints",
        f"Same crew, start to finish",
        f"HOA &amp; ARC-ready hardscape",
        f"Concrete &amp; pavers · Lakewood Ranch to the coast",
    ]
    # Repeat for seamless scroll
    items2 = "".join(f"<span>{x}</span>" for x in (items*2))
    return f'<div class="ticker"><div class="ticker-inner">{items2}</div></div>'

# Reviews section (drop in any page)
def reviews_section(limit=6, headline=None):
    headline = headline or "What homeowners actually say."
    # NEW business: no reviews yet. Render a clean "be our first review" CTA —
    # NO fabricated cards, NO star ratings, NO review counts.
    if not REVIEWS:
        gp = BUSINESS.get("google_review_url") or BUSINESS.get("google_profile") or ""
        review_btn = (f'<a href="{gp}" target="_blank" rel="noopener" class="btn btn-orange">Leave a Google review</a>'
                      if gp and not gp.startswith("{{") else "")
        return f'''<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label">Reviews · {BUSINESS["county"]}</span>
        <h2>{headline}</h2>
        <div class="section-head-text"><p>We&rsquo;re a local, owner-run concrete &amp; paver crew building our reputation one project at a time. We don&rsquo;t post made-up testimonials &mdash; so this space is honest and open. Hire us, and your honest review could be the first one here.</p></div>
      </div>
    </div>
    <aside class="contact-banner" style="margin-top:8px">
      <div class="contact-banner-text">
        <strong>Already worked with us?</strong>
        <span>Your feedback helps your neighbors choose with confidence.</span>
      </div>
      <div class="contact-banner-cta">
        {review_btn}
        <a href="/contact/" class="btn btn-outline-light">Get a free estimate</a>
      </div>
    </aside>
  </div>
</section>'''
    cards = ""
    for r in REVIEWS[:limit]:
        stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
        cards += f'''<article class="review-card">
  <div class="review-quote-mark">&ldquo;</div>
  <div class="review-stars" aria-label="{r["rating"]} out of 5 stars">{stars}</div>
  <p class="review-text">{r["text"]}</p>
  <div class="review-meta">
    <span class="review-author">{r["name"]}</span>
    <span class="review-where">{r["city"]}, FL · {r["service"]}</span>
    <span class="review-verified">● Verified Google Review · {r["date"]}</span>
  </div>
</article>'''
    return f'''<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label">Reviews · Lakewood Ranch, Manatee &amp; Sarasota</span>
        <h2>{headline}</h2>
      </div>
    </div>
    <div class="reviews-rating-bar">
      <span>● Google Verified</span>
      <span class="stars">★★★★★</span>
      <strong>{BUSINESS["rating"]}</strong>
      <span>from {BUSINESS["review_count"]} reviews · 100% 5-star</span>
      <a href="{BUSINESS["google_profile"]}" target="_blank" rel="noopener" style="color:var(--orange);text-decoration:underline">View on Google →</a>
    </div>
    <div class="reviews-grid">{cards}</div>
  </div>
</section>'''

# 42-point checklist section (used on every service-city page + service hub)
def checklist_section(city_name=None, service_name=None):
    pts = CHECKLIST["points"]
    title_city = f" for {city_name} Homes" if city_name else ""
    if service_name:
        intro_text = f"Every {service_name.lower()} project passes all {pts} points before we sign off. You get a printed copy at handover."
    else:
        intro_text = f"Every pour and paver install passes all {pts} points before we sign off. You get a printed copy at handover."
    cards = ""
    for c in CHECKLIST["categories"]:
        items_html = "".join(f"<li>{it}</li>" for it in c["items"])
        cards += f'''<article class="checklist-card">
  <header class="checklist-card-head">
    <span class="ck-num">{c["icon"]}</span>
    <strong>{c["title"]}</strong>
    <span class="ck-count">{len(c["items"])} pts</span>
  </header>
  <ol>{items_html}</ol>
</article>'''
    return f'''<section class="checklist-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">04</div>
      <div class="section-head-meta">
        <span class="mono-label">The {BUSINESS["name"]} Standard</span>
        <h2>Our {CHECKLIST["points"]}-Point Install Standard<em>{title_city}</em></h2>
        <div class="section-head-text"><p>{intro_text}</p></div>
      </div>
    </div>
    <div class="checklist-grid">{cards}</div>
  </div>
</section>'''

# Neighborhood + ZIP grid section
def neighborhoods_section(city):
    pills = "".join(f'<div class="neighborhood-pill">{n}</div>' for n in city["neighborhoods"])
    zips = "".join(f'<span class="zip-tag">{z}</span>' for z in city["zips"])
    return f'''<section class="neighborhoods-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">05</div>
      <div class="section-head-meta">
        <span class="mono-label">Local Coverage · {city["county"]}</span>
        <h2>Where we work in <em>{city["name"]}</em>.</h2>
        <div class="section-head-text"><p>We serve every neighborhood, subdivision, and ZIP code in {city["name"]} and the surrounding {city["county"]} corridor. If your community isn&rsquo;t listed below, it just means we haven&rsquo;t worked there yet — call and we&rsquo;ll quote it.</p></div>
      </div>
    </div>
    <div class="neighborhood-grid">{pills}</div>
    <div class="zips-bar">
      <span class="zips-bar-label">ZIPs served</span>
      {zips}
    </div>
  </div>
</section>'''

# FAQ section with details/summary
def faq_section(faqs, headline=None, label="FAQ · Frequently Asked"):
    headline = headline or "Questions homeowners actually ask."
    items = ""
    for q, a in faqs:
        items += f'<details><summary>{q}</summary><div class="faq-body"><p>{a}</p></div></details>'
    return f'''<section class="faq-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">07</div>
      <div class="section-head-meta">
        <span class="mono-label">{label}</span>
        <h2>{headline}</h2>
      </div>
    </div>
    <div class="faq-list">{items}</div>
  </div>
</section>'''

# ============================================================================
# JSON-LD SCHEMA builders
# ============================================================================
def schema_organization():
    same_as = [x for x in [BUSINESS["google_profile"], BUSINESS["facebook"], BUSINESS["instagram"], BUSINESS["yelp"], BUSINESS["thumbtack"], BUSINESS["angi"], BUSINESS["houzz"], BUSINESS["bbb"]] if x and "{{" not in x]
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": BUSINESS["name"],
        "alternateName": BUSINESS["legal_name"],
        "url": SITE,
        "logo": {"@type":"ImageObject","url":f"{SITE}/images/logo.png","width":600,"height":400},
        "image": f"{SITE}/images/og-default.jpg",
        "telephone": BUSINESS["phone"],
        "email": BUSINESS["email"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": BUSINESS["city"],
            "addressRegion": BUSINESS["state"],
            "postalCode": BUSINESS["zip"],
            "addressCountry": BUSINESS["country"],
        },
        "geo": {"@type":"GeoCoordinates","latitude":BUSINESS["lat"],"longitude":BUSINESS["lng"]},
        "areaServed": [{"@type":"City","name":c["name"]} for c in CITIES.values()],
        "sameAs": same_as,
        "openingHoursSpecification": [
            {"@type":"OpeningHoursSpecification","dayOfWeek":d,"opens":o,"closes":c}
            for d,o,c in BUSINESS["hours"]
        ],
        "priceRange": "$$",
        "description": BUSINESS["tagline_long"],
    }
    # Only emit foundingDate once the owner supplies a real year (never a placeholder).
    if "{{" not in str(BUSINESS["year_founded"]):
        org["foundingDate"] = str(BUSINESS["year_founded"])
    return org

def schema_local_business(page_url, page_name, city=None, service=None, image=None):
    image = image or f"{SITE}/images/og-default.jpg"
    desc = page_name
    if service and city:
        desc = f"{service} contractor in {city}, FL. {BUSINESS['tagline_long']}"
    elif service:
        desc = f"{service} across Lakewood Ranch, Manatee &amp; Sarasota. {BUSINESS['tagline_long']}"
    elif city:
        desc = f"Concrete &amp; paver contractor in {city}, FL. {BUSINESS['tagline_long']}"
    schema = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": page_url + "#business",
        "name": BUSINESS["name"],
        "url": page_url,
        "telephone": BUSINESS["phone"],
        "email": BUSINESS["email"],
        "image": image,
        "description": desc,
        "address": {
            "@type":"PostalAddress",
            "addressLocality": BUSINESS["city"],
            "addressRegion": BUSINESS["state"],
            "postalCode": BUSINESS["zip"],
            "addressCountry": BUSINESS["country"],
        },
        "geo": {"@type":"GeoCoordinates","latitude":BUSINESS["lat"],"longitude":BUSINESS["lng"]},
        "areaServed": {"@type":"City","name":city} if city else [{"@type":"City","name":c["name"]} for c in CITIES.values()],
        "priceRange":"$$",
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":d,"opens":o,"closes":c} for d,o,c in BUSINESS["hours"]],
    }
    # NEW business — only emit a rating when real reviews exist (no placeholders).
    if BUSINESS.get("has_reviews") and REVIEWS and not str(BUSINESS["rating"]).startswith("{{"):
        schema["aggregateRating"] = {"@type":"AggregateRating","ratingValue":BUSINESS["rating"],"reviewCount":str(BUSINESS["review_count"]),"bestRating":"5"}
    return schema

def schema_breadcrumb(items):
    """items: list of (name, url). LAST one's url is page url."""
    return {
        "@context":"https://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":i+1,"name":name,"item":url}
            for i,(name,url) in enumerate(items)
        ],
    }

def schema_faqpage(faqs):
    return {
        "@context":"https://schema.org",
        "@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
            for q,a in faqs
        ],
    }

def schema_article(post, canonical):
    return {
        "@context":"https://schema.org",
        "@type":"Article",
        "headline": post["title"],
        "description": post["meta_desc"],
        "image": f"{SITE}/images/og-default.jpg",
        "datePublished": post["date_published"],
        "dateModified": post["date_modified"],
        "author":{"@type":"Organization","name":BUSINESS["name"]},
        "publisher":{
            "@type":"Organization",
            "name":BUSINESS["name"],
            "logo":{"@type":"ImageObject","url":f"{SITE}/images/logo.png"},
        },
        "mainEntityOfPage":{"@type":"WebPage","@id":canonical},
        "articleSection":post.get("category","Concrete &amp; Pavers"),
    }

def schema_webpage(canonical, name, desc):
    return {
        "@context":"https://schema.org",
        "@type":"WebPage",
        "@id":canonical,
        "url":canonical,
        "name":name,
        "description":desc,
        "isPartOf":{"@id":f"{SITE}/#website"},
    }

def schema_website():
    return {
        "@context":"https://schema.org",
        "@type":"WebSite",
        "@id":f"{SITE}/#website",
        "url":SITE,
        "name":BUSINESS["name"],
        "publisher":{"@id":f"{SITE}/#organization"},
        "inLanguage":"en-US",
    }

def schema_service(service, city=None, canonical=None):
    desc = service["intro_lead"]
    name = service["name"]
    if city:
        name = f"{service['name']} in {city}, FL"
    return {
        "@context":"https://schema.org",
        "@type":"Service",
        "serviceType": service["name"],
        "name": name,
        "description": desc,
        "provider":{"@id":f"{SITE}/#organization"},
        "areaServed": {"@type":"City","name":city} if city else [{"@type":"City","name":c["name"]} for c in CITIES.values()],
        "url": canonical or SITE,
    }

# ============================================================================
# WRAPPER — full HTML page (combines everything)
# ============================================================================
def wrap_page(head_html, header_html, body_html, footer_html=None, breadcrumbs_html="", float_html=None):
    footer_html = footer_html if footer_html is not None else footer()
    float_html = float_html if float_html is not None else FLOAT_CONTACT
    return f'''{head_html}<body>
{header_html}
{breadcrumbs_html}
<main>
{body_html}
</main>
{footer_html}
{float_html}
{MENU_JS}
</body>
</html>'''

# Convenience: full page builder for the homepage and most pages
def write_page(filepath, head_html, header_html, body_html, footer_html=None, breadcrumbs_html="", float_html=None):
    import os
    html = wrap_page(head_html, header_html, body_html, footer_html=footer_html, breadcrumbs_html=breadcrumbs_html, float_html=float_html)
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath
