#!/usr/bin/env python3
"""Generate sitemap.xml, robots.txt, _headers, _redirects for Lakewood Ranch Concrete."""
import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import (
    BUSINESS, CITIES, SERVICES, SERVICE_ORDER, CITY_ORDER,
    GENERAL_BLOG_POSTS, COST_BLOG_POSTS, GUIDES, GLOSSARY,
)

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"
TODAY = date.today().isoformat()

# Static / company pages that always exist in the site.
STATIC_PAGES = [
    "about", "contact", "faq", "financing", "warranty",
    "privacy-policy", "terms",
]


def build_sitemap():
    """Build sitemap.xml covering every published URL on the site."""
    urls = []

    # Homepage — priority 1.0
    urls.append((f"{SITE}/", TODAY, "weekly", "1.0"))

    # Service hubs — priority 0.9
    for s in SERVICE_ORDER:
        urls.append((f"{SITE}/{s}/", TODAY, "weekly", "0.9"))

    # City hubs — priority 0.8
    for c in CITY_ORDER:
        urls.append((f"{SITE}/{c}/", TODAY, "weekly", "0.8"))

    # Service-city pages — priority 0.7
    for s in SERVICE_ORDER:
        for c in CITY_ORDER:
            urls.append((f"{SITE}/{s}/{c}/", TODAY, "monthly", "0.7"))

    # Blog index — priority 0.7
    urls.append((f"{SITE}/blog/", TODAY, "weekly", "0.7"))

    # Blog posts (general + cost guides) — priority 0.6
    for p in GENERAL_BLOG_POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", p.get("date_modified", TODAY), "monthly", "0.6"))
    for p in COST_BLOG_POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", p.get("date_modified", TODAY), "monthly", "0.6"))

    # Guides (reserved content wave — empty until populated) — priority 0.6
    for g in GUIDES:
        urls.append((f"{SITE}/guides/{g['slug']}/", g.get("date_modified", TODAY), "monthly", "0.6"))

    # Glossary (reserved content wave — empty until populated) — priority 0.4
    for g in GLOSSARY:
        urls.append((f"{SITE}/glossary/{g['slug']}/", g.get("date_modified", TODAY), "monthly", "0.4"))

    # Static / company pages — priority 0.5
    for path in STATIC_PAGES:
        urls.append((f"{SITE}/{path}/", TODAY, "monthly", "0.5"))

    # Build XML
    rows = "\n".join(
        f'  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{p}</priority></url>'
        for loc, lm, cf, p in urls
    )
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
'''
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote sitemap.xml ({len(urls)} URLs)")
    return len(urls)


def build_robots():
    # GEO strategy: AI crawlers are explicitly ALLOWED so the business gets cited
    # by ChatGPT, Claude, Gemini, Perplexity and Google AI Overviews.
    txt = f'''User-agent: *
Allow: /
Disallow: /thanks/
Disallow: /404.html

# --- AI / LLM crawlers: explicitly allowed (GEO — we want to be cited) ---
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GoogleOther
Allow: /

User-agent: CCBot
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: meta-externalagent
Allow: /

# Sitemap
Sitemap: {SITE}/sitemap.xml

# LLM-readable site summary
# {SITE}/llms.txt
'''
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote robots.txt")


def build_llms_txt():
    """llms.txt — structured, LLM-readable summary of the business and site.
    Spec: https://llmstxt.org — consumed by ChatGPT, Claude, Perplexity & friends.
    NEW business: NO license, NO invented reviews/ratings/stats."""
    svc_lines = "\n".join(
        f"- [{SERVICES[s]['name']}]({SITE}/{s}/): {SERVICES[s]['intro_lead']}"
        for s in SERVICE_ORDER
    )
    city_lines = "\n".join(
        f"- [{CITIES[slug]['name']}, FL]({SITE}/{slug}/): {CITIES[slug]['context_short']}"
        for slug in CITY_ORDER if slug in CITIES
    )
    cost_lines = "\n".join(
        f"- [{p['title']}]({SITE}/blog/{p['slug']}/)"
        for p in COST_BLOG_POSTS
    )
    guide_lines = "\n".join(
        f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {p['meta_desc']}"
        for p in GENERAL_BLOG_POSTS
    )
    txt = f'''# {BUSINESS["name"]}

> {BUSINESS["tagline_long"]}
> Fully insured concrete &amp; paver contractor — a Service-Area Business based in east
> {BUSINESS["city"]}, {BUSINESS["state_long"]} {BUSINESS["zip"]} (bordering Lakewood Ranch), serving Lakewood Ranch,
> Manatee, Sarasota, Charlotte &amp; south Hillsborough counties within a ~60-mile radius.

## Key Facts

- Business name: {BUSINESS["name"]} ({BUSINESS["legal_name"]})
- Type: Concrete &amp; paver / hardscape contractor (Service-Area Business — no walk-in storefront)
- Service area: east {BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]} hub, ~60-mile radius across {BUSINESS["county"]},
  Sarasota County, Charlotte County, and south Hillsborough County
- Insured: Fully Insured
- Estimates: {BUSINESS["response_time"]}
- Warranty: {BUSINESS["guarantee"]}
- Quality standard: {BUSINESS["checklist_name"]} ({BUSINESS["checklist_points"]} verification points on every job)
- Cities served: Lakewood Ranch, Bradenton, Parrish, Palmetto, Ellenton, Sarasota,
  Venice, North Port, Port Charlotte, Punta Gorda, Riverview, and Sun City Center, Florida

## Services

{svc_lines}

## Service Areas

{city_lines}

## Guides

{guide_lines}

## Cost Guides (2026 pricing by city)

{cost_lines}

## Company Pages

- [About {BUSINESS["name"]}]({SITE}/about/): Who we are, our crew, and our 42-Point Install Standard
- [FAQ]({SITE}/faq/): Real questions homeowners ask about concrete &amp; pavers, answered in writing
- [Warranty]({SITE}/warranty/): Written workmanship warranty on every pour and paver install
- [Financing]({SITE}/financing/): Payment options for driveways, patios, and pool decks
- [Contact]({SITE}/contact/): Free estimate within 24 hours, often same-day
'''
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote llms.txt")


def build_headers():
    """Cloudflare Pages _headers file — security + cache rules."""
    txt = '''/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  X-XSS-Protection: 1; mode=block

# HTML files — short cache, must revalidate
/*.html
  Cache-Control: public, max-age=3600, must-revalidate

# Images — long cache (immutable assets)
/images/*
  Cache-Control: public, max-age=31536000, immutable

# Fonts — long cache
*.woff2
  Cache-Control: public, max-age=31536000, immutable

# Sitemap & robots — moderate cache
/sitemap.xml
  Cache-Control: public, max-age=86400

/robots.txt
  Cache-Control: public, max-age=86400
'''
    with open("_headers", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote _headers")


def build_redirects():
    """Cloudflare Pages _redirects file — canonical domain + URL normalizations."""
    txt = f'''# Force HTTPS + non-www canonical (Cloudflare usually handles this, but explicit)
http://{DOMAIN}/* https://{DOMAIN}/:splat 301!
http://www.{DOMAIN}/* https://{DOMAIN}/:splat 301!
https://www.{DOMAIN}/* https://{DOMAIN}/:splat 301!

# Common path variations
/services/* /:splat 301
/service-areas/* /:splat 301
/areas/* /:splat 301

# Service slug variations
/driveways/* /concrete-driveways/:splat 301
/concrete-driveway/* /concrete-driveways/:splat 301
/patios/* /concrete-patios/:splat 301
/concrete-patio/* /concrete-patios/:splat 301
/pool-decks/* /concrete-pool-decks/:splat 301
/pool-deck/* /concrete-pool-decks/:splat 301
/stamped/* /stamped-concrete/:splat 301
/slabs/* /concrete-slabs/:splat 301
/concrete-slab/* /concrete-slabs/:splat 301
/resurfacing/* /concrete-resurfacing/:splat 301
/concrete-overlay/* /concrete-resurfacing/:splat 301
/pavers/* /paver-patios-walkways/:splat 301
/paver-driveway/* /paver-driveways/:splat 301
/paver-patios/* /paver-patios-walkways/:splat 301
/paver-walkways/* /paver-patios-walkways/:splat 301
/walkways/* /paver-patios-walkways/:splat 301
/paver-pool-deck/* /pool-deck-pavers/:splat 301
/travertine/* /pool-deck-pavers/:splat 301
/sealing/* /paver-sealing/:splat 301

# City variations
/lakewoodranch/* /lakewood-ranch/:splat 301
/lwr/* /lakewood-ranch/:splat 301
/portcharlotte/* /port-charlotte/:splat 301
/northport/* /north-port/:splat 301
/puntagorda/* /punta-gorda/:splat 301
/suncitycenter/* /sun-city-center/:splat 301

# 404 fallback
/* /404.html 404
'''
    with open("_redirects", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote _redirects")


if __name__ == "__main__":
    build_sitemap()
    build_robots()
    build_llms_txt()
    build_headers()
    build_redirects()
