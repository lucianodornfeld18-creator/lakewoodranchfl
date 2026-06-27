#!/usr/bin/env python3
"""Generate /directories/ — a 'find us across the web' + internal link hub page.
Boosts crawl/indexation (links every service, city, service-city, and blog post)
and consolidates citation/social signals."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *
from _data import LIVE_PROFILES, DIRECTORY_NETWORK, COST_BLOG_POSTS, GENERAL_BLOG_POSTS, CITY_ORDER

URL = f"{SITE}/directories/"
TITLE = "Find Us Online · Lakewood Ranch Concrete Directory"
DESC = clip_desc("Find Lakewood Ranch Concrete across Google, Facebook, Instagram and the web — plus a full index of our concrete & paver services and service areas.")

ICONS = {
    "Facebook": '<svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22"><path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.89v2.25h3.32l-.53 3.49h-2.79V24C19.61 23.1 24 18.1 24 12.07z"/></svg>',
    "Instagram": '<svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zm0 3.68a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm7.84-10.4a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0z"/></svg>',
    "Google Business Profile": '<svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
}

# Live profiles (skip placeholders)
prof_cards = ""
for name, url in LIVE_PROFILES:
    if not url or "{{" in url:
        continue
    icon = ICONS.get(name, "★")
    prof_cards += f'''<a href="{url}" target="_blank" rel="noopener" class="area-card" style="flex-direction:row;align-items:center;gap:14px">
  <span style="color:var(--orange);display:flex">{icon}</span>
  <span class="area-card-name" style="font-size:1.05rem">{name}</span>
</a>'''

# Directory network chips (link the ones that match a live profile, else plain)
live_map = {n: u for n, u in LIVE_PROFILES if u and "{{" not in u}
chips = ""
for d in DIRECTORY_NETWORK:
    if d in live_map:
        chips += f'<a href="{live_map[d]}" target="_blank" rel="noopener" class="neighborhood-pill" style="text-decoration:none">{d}</a>'
    else:
        chips += f'<span class="neighborhood-pill">{d}</span>'

# Internal hub
svc_links = "".join(f'<li><a href="/{s}/">{SERVICES[s]["name"]}</a></li>' for s in SERVICE_ORDER)
city_links = "".join(f'<li><a href="/{c}/">{CITIES[c]["name"]}, FL</a></li>' for c in CITY_ORDER)

svc_city_blocks = ""
for s in SERVICE_ORDER:
    rows = "".join(f'<a href="/{s}/{c}/" class="neighborhood-pill" style="text-decoration:none">{SERVICES[s]["short"]} · {CITIES[c]["name"]}</a>' for c in CITY_ORDER)
    svc_city_blocks += f'<h3 style="margin-top:1.4rem">{SERVICES[s]["name"]} by city</h3><div class="neighborhood-grid">{rows}</div>'

blog_links = "".join(f'<li><a href="/blog/{p["slug"]}/">{p["title"]}</a></li>' for p in GENERAL_BLOG_POSTS)
cost_links = "".join(f'<li><a href="/blog/{p["slug"]}/">{p["title"]}</a></li>' for p in COST_BLOG_POSTS)

bc = breadcrumbs([("Home", "/"), ("Directory", None)])
schemas = [schema_webpage(URL, TITLE, DESC), schema_breadcrumb([("Home", SITE+"/"), ("Directory", URL)])]

hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Directory &amp; Listings</span>
    <h1>Find <em>Lakewood Ranch Concrete</em> across the web<span class="stop">.</span></h1>
    <p class="page-hero-sub">Follow our work, read reviews, and request a free estimate &mdash; on Google, Facebook, Instagram and beyond. Below you&rsquo;ll also find a full index of our concrete &amp; paver services and the cities we serve across Manatee &amp; Sarasota.</p>
    <div class="page-hero-trust"><span>Fully Insured</span><span>Free Estimates</span><span>(941) 352-4308</span></div>
  </div>
</section>'''

body = f'''{hero}
<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head"><div class="section-head-num">01</div><div class="section-head-meta">
      <span class="mono-label">Follow &amp; Review</span><h2>Our official profiles.</h2></div></div>
    <div class="areas-grid" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">{prof_cards}</div>
  </div>
</section>
<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head"><div class="section-head-num">02</div><div class="section-head-meta">
      <span class="mono-label">Citations · Listed Across the Web</span><h2>Where to find us.</h2>
      <div class="section-head-text"><p>Lakewood Ranch Concrete maintains consistent listings across these business directories and map platforms.</p></div></div>
    <div class="neighborhood-grid">{chips}</div>
  </div>
</section>
<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head"><div class="section-head-num">03</div><div class="section-head-meta">
      <span class="mono-label">Site Index · Services &amp; Areas</span><h2>Everything we offer, everywhere we work.</h2></div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">
      <div class="related-box"><div class="related-box-label">Services</div><ul>{svc_links}</ul></div>
      <div class="related-box"><div class="related-box-label">Service Areas</div><ul>{city_links}</ul></div>
    </div>
    <div style="margin-top:2rem">{svc_city_blocks}</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:2rem">
      <div class="related-box"><div class="related-box-label">Guides</div><ul>{blog_links}</ul></div>
      <div class="related-box"><div class="related-box-label">Cost Guides by City</div><ul>{cost_links}</ul></div>
    </div>
  </div>
</section>
{final_cta()}'''

head_html = head(TITLE, DESC, URL, json_ld=schemas)
write_page("directories/index.html", head_html, header(), body, breadcrumbs_html=bc)
print("Wrote /directories/index.html")
