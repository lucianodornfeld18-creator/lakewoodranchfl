#!/usr/bin/env python3
"""Generate /[city]/ hub pages — one per city in CITIES."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *

# ============================================================================
# City-specific FAQ generator
# ============================================================================
def city_faqs(city):
    """Returns a list of (q, a) tuples — 6 city-specific Q&As (concrete & pavers)."""
    name = city["name"]
    cnty = city["county"]
    neigh_sample = city["neighborhoods"][:3]
    primary = city["primary_market"]
    humid = city["humidity_note"]

    return [
        (f"How much does a concrete or paver project cost in {name}, FL?",
         f"Real 2026 numbers for {name} and the rest of {cnty}: poured concrete driveways and patios with a broom finish run roughly $8&ndash;$14 per square foot; stamped or decorative concrete $12&ndash;$20; concrete pool decks $10&ndash;$16; resurfacing existing slabs $5&ndash;$12; and sealing $1&ndash;$3. Pavers cost more for the upgrade in look and repairability &mdash; paver driveways and patios land around $14&ndash;$26 per square foot, and travertine or paver pool decks $16&ndash;$32. What moves your number in {name} is the base prep (sandy or soft soil that needs extra excavation and compaction adds cost), demo and haul-off of an old slab, drainage and slope work, and the finish or paver you choose. You get a written, line-itemized estimate within 24 hours of the on-site measure &mdash; no &lsquo;starting at&rsquo; pricing, no surprise change orders."),
        (f"How long does a concrete or paver job take in {name}?",
         f"For a typical {name} home: a poured driveway runs about a few working days &mdash; demo and haul-off, base prep, forming, and the pour &mdash; then concrete needs to cure before you drive on it (we&rsquo;ll give you the exact window before anyone parks on it). A paver driveway, patio, or pool deck usually takes 2&ndash;4 days from excavation through base compaction, laying, edge restraints, and polymeric joint sand. Stamped and decorative concrete adds a little time for the stamping, color, and sealing steps. Whole-home hardscape projects in larger homes around {neigh_sample[0]} and {neigh_sample[1]} run longer. The real schedule lives in your written quote, not in this paragraph."),
        (f"Are you actually local to {name}?",
         f"Yes. Our crew is based in east {BUSINESS['city']}, in the 34212 ZIP bordering Lakewood Ranch &mdash; minutes from most of {name}, not driving in from another county. We pour concrete and lay pavers across {cnty} every week, so we know the soil, the drainage, the HOA / ARC rules, and the community access protocols at {neigh_sample[0]}, {neigh_sample[1]}, and {neigh_sample[2]}. The same crew that measures your {name} project is the crew that pours and paves it, start to finish."),
        (f"Why does {name} need specific prep for concrete and pavers?",
         f"{humid} The bigger picture: {primary.lower()}. That dictates how deep we excavate, how much base we bring in and compact, where the control and expansion joints go, and how we slope the surface for drainage. The same square footage in two different {name} neighborhoods can need very different prep &mdash; an older home near {city['neighborhoods'][-2] if len(city['neighborhoods']) > 1 else city['neighborhoods'][0]} may have soft or organic soil that has to be cut out and replaced, while a newer build in {neigh_sample[0]} sits on engineered fill. We assess all of that at the on-site measure, because the base prep nobody sees is what stops the crack you would have seen."),
        (f"Do you handle HOA and ARC-managed communities in {name}?",
         f"Yes. Most of the gated and master-planned communities in {name} (including {neigh_sample[0]}, {neigh_sample[1]}, and {neigh_sample[2]}) run an architectural review committee with rules on driveway material, paver color and pattern, and concrete finish. We build to what passes, document the spec, and can prepare and submit the ARC package so your project clears review the first time. Give us the gate code and the community&rsquo;s guidelines and we&rsquo;ll work within them &mdash; color samples, joint and border details, and all."),
        (f"Can you start a {name} project within the week?",
         f"Sometimes &mdash; it depends on the size of the job and our current schedule. Smaller pours and paver jobs can often start within the week of a signed estimate, especially in the slower, drier stretches of the year. Larger driveways, pool decks, and multi-surface hardscape projects typically book a few weeks out. Florida weather is the other variable: we schedule pours around the rainy-season afternoon storms and protect fresh concrete while it cures. We&rsquo;ll give you a real start date in the quote, not a vague &lsquo;we&rsquo;ll get to it.&rsquo;"),
    ]

# ============================================================================
# City-specific "why this city" content section
# ============================================================================
def city_why_here(city):
    name = city["name"]
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">{city["county"]} · {city["population"]}</span>
        <h2>Why concrete &amp; pavers in <em>{name}</em> aren&rsquo;t the same as anywhere else.</h2>
        <div class="section-head-text"><p>{city["growth"]}. The hardscape market here has its own dynamics.</p></div>
      </div>
    </div>

    <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:50px;align-items:start;max-width:1100px;margin:0 auto">
      <div class="intro-prose" style="margin:0">
        <p>{city["context"]}</p>

        <p><strong>Humidity reality:</strong> {city["humidity_note"]}</p>

        <p><strong>Primary market we serve:</strong> {city["primary_market"]}. Most {name} concrete and paver projects are some version of one of those scenarios &mdash; and the right material, the right base prep, and the right timeline depend on which one your home falls into.</p>

        <p><strong>Permitting &amp; review:</strong> {city["trade_class"]}. We pour and pave in this jurisdiction every week and we know what passes, what flags, and what the inspectors and ARC committees actually look for.</p>
      </div>

      <aside style="background:var(--paper-deep);padding:32px 28px;border-left:6px solid var(--orange)">
        <span class="mono-label">{name} Quick Facts</span>
        <dl style="margin-top:1.2rem;display:flex;flex-direction:column;gap:.8rem;font-family:var(--font-mono);font-size:.85rem">
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">County</dt><dd style="font-weight:600;text-align:right">{city["county"]}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">Population</dt><dd style="font-weight:600;text-align:right">{city["population"]}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">Growth</dt><dd style="font-weight:600;text-align:right">{city["growth"]}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--rule)"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">ZIPs Served</dt><dd style="font-weight:600;text-align:right">{len(city["zips"])}</dd></div>
          <div style="display:flex;justify-content:space-between;gap:1rem"><dt style="color:var(--gray);letter-spacing:.08em;text-transform:uppercase;font-size:.72rem">Coordinates</dt><dd style="font-weight:600;text-align:right;font-size:.78rem">{city["lat"]}, {city["lng"]}</dd></div>
        </dl>
        <p style="margin-top:1.4rem;font-family:var(--font-body);font-size:.92rem;color:var(--gray);line-height:1.55;font-style:normal"><em>Landmarks nearby:</em> {city["landmarks"]}.</p>
      </aside>
    </div>
  </div>
</section>'''

# ============================================================================
# Services grid filtered by city (each links to /service/city/)
# ============================================================================
def city_services_grid(city):
    name = city["name"]
    slug = city["slug"]
    cards = ""
    for sslug in SERVICE_ORDER:
        s = SERVICES[sslug]
        cards += f'''<a href="/{sslug}/{slug}/" class="service-card">
  <div class="service-card-num">{s["icon"]} / {s["short"]}</div>
  <h3>{s["short"]} in {name}</h3>
  <p class="service-card-desc">{s["intro_lead"]}</p>
  <span class="service-card-cta">See {s["short"]} · {name}</span>
</a>'''
    return f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label">Ten services · {name}, FL</span>
        <h2>Every surface we pour &amp; pave,<br><em>in {name}</em>.</h2>
        <div class="section-head-text"><p>Concrete driveways, patios, pool decks, stamped concrete, slabs, resurfacing, paver driveways, patios &amp; walkways, pool-deck pavers, and sealing &mdash; pick what you&rsquo;re after. Each service page has {name}-specific pricing, scope, and FAQ.</p></div>
      </div>
    </div>
    <div class="services-grid">{cards}</div>
  </div>
</section>'''

# ============================================================================
# Reviews — NEW business: NO fabricated reviews, NO ratings. Defer to the
# shared reviews_section() from _gen, which renders a "be our first review"
# CTA when REVIEWS is empty.
# ============================================================================
def city_reviews(city, count=6):
    name = city["name"]
    return reviews_section(limit=count, headline=f"Be the first {name} review.")

# ============================================================================
# Related city links + related posts (cross-link)
# ============================================================================
def city_related_box(city):
    slug = city["slug"]
    name = city["name"]
    # Other cities
    other_links = "".join(
        f'<li><a href="/{s}/">{c["name"]}, FL</a></li>'
        for s, c in CITIES.items() if s != slug
    )
    # Cost blog posts for this city
    cost_posts = [p for p in COST_BLOG_POSTS if p["city_slug"] == slug]
    blog_links = "".join(
        f'<li><a href="/blog/{p["slug"]}/">{p["title"]}</a></li>'
        for p in cost_posts
    )
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px">
      <div class="related-box">
        <div class="related-box-label">Read Next · Other Cities</div>
        <h3>We also work nearby.</h3>
        <ul>{other_links}</ul>
      </div>
      <div class="related-box">
        <div class="related-box-label">Read Next · {name} Cost Guides</div>
        <h3>What it actually costs in {name}.</h3>
        <ul>{blog_links}</ul>
      </div>
    </div>
  </div>
</section>'''

# ============================================================================
# Build one city page
# ============================================================================
def build_city(slug):
    city = CITIES[slug]
    name = city["name"]
    URL = f"{SITE}/{slug}/"

    # SEO
    TITLE_RAW = f"Concrete & Paver Contractor {name} FL · {BUSINESS['name']}"
    if len(TITLE_RAW) > 65:
        TITLE_RAW = f"Concrete Contractor {name} FL · {BUSINESS['name']}"
    TITLE = TITLE_RAW[:65]
    DESC = clip_desc(
        f"Concrete driveways, patios, pool decks, stamped concrete & pavers in "
        f"{name}, FL. {len(city['neighborhoods'])}+ neighborhoods served. "
        f"Fully Insured · 42-Point Standard · free estimate."
    )

    faqs = city_faqs(city)
    schemas = [
        schema_local_business(URL, f"Concrete & Pavers in {name}, FL", city=name),
        schema_faqpage(faqs),
        schema_breadcrumb([("Home", SITE+"/"), (f"{name}, FL", URL)]),
        schema_webpage(URL, TITLE, DESC),
    ]
    bc = breadcrumbs([("Home","/"), (f"{name}, FL", None)])

    # HERO
    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">{city["county"]} · {len(city["zips"])} ZIPs · {len(city["neighborhoods"])}+ neighborhoods</span>
    <h1>Concrete &amp; paver contractor.<br><em>{name}<span class="stop">,</span></em> Florida.</h1>
    <p class="page-hero-sub">Driveways, patios, pool decks, stamped concrete, slabs, resurfacing &amp; pavers &mdash; poured and laid by the same crew, on a base built to last in the Florida sun. {city["context_short"]}</p>
    <div class="page-hero-trust">
      <span>{len(city["neighborhoods"])}+ {name} neighborhoods</span>
      <span>Fully Insured</span>
      <span>42-Point Install Standard</span>
      <span>Free estimate in 24 hrs</span>
    </div>
  </div>
</section>'''

    # INTRO (numbered 01)
    intro = f'''<section style="background:var(--paper-deep)" id="intro">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">{name} · Service Profile</span>
        <h2>Local concrete &amp; paver crew. <em>Real {name} addresses.</em></h2>
      </div>
    </div>
    <div class="intro-prose">
      <p><strong>{BUSINESS["name"]}</strong> pours concrete and lays pavers in {name} &mdash; driveways, patios, pool decks, stamped concrete, slabs, resurfacing, and pavers &mdash; from the gated golf communities around {city["neighborhoods"][0]} and {city["neighborhoods"][1] if len(city["neighborhoods"]) > 1 else city["neighborhoods"][0]}, to the older single-family homes off the main corridors, to the new construction in {city["neighborhoods"][-1]}. We&rsquo;re based in east {BUSINESS["city"]}, in the 34212 ZIP bordering Lakewood Ranch, with a tight service radius across Lakewood Ranch, Manatee &amp; Sarasota that covers every part of {name}, {city["county"]}, and the surrounding corridor.</p>

      <p>Our approach in {name} is the same as everywhere we work: <strong>poured and laid to spec, on a base that&rsquo;s actually excavated and compacted, by the same crew from estimate to walkthrough.</strong> We don&rsquo;t hand the demo to one outfit and the pour to another &mdash; the people who measure your {name} project are the people who prep the base, set the forms, place the steel, and finish the surface. Fully insured, with a written workmanship warranty on every job.</p>

      <p>Every project in {name} passes our <a href="#checklist">42-point install standard</a> &mdash; from soil and drainage survey through base compaction, reinforcement, finish, curing, and the final hose-test walkthrough. {city["humidity_note"]} Those 42 points are how we make sure the surface holds up in the Florida sun instead of cracking or settling a year later.</p>
    </div>
  </div>
</section>'''

    # WHY THIS CITY (02)
    why_here = city_why_here(city)

    # SERVICES GRID (03)
    services_grid_html = city_services_grid(city)

    # CHECKLIST (04)
    checklist_html = checklist_section(city_name=name)

    # NEIGHBORHOODS (05)
    neigh_html = neighborhoods_section(city)

    # REVIEWS (06)
    reviews_html = city_reviews(city, count=6)

    # FAQ (07)
    faq_html = faq_section(faqs, headline=f"Questions {name} homeowners ask, weekly.", label=f"FAQ · {name}, FL")

    # RELATED LINKS
    related_html = city_related_box(city)

    # FINAL CTA
    final_html = final_cta(
        headline=f"Ready for a real estimate, on a real {name} project?",
        sub=f"Free on-site measure within 24&ndash;48 hours. Written, line-itemized quote within 24 hours of the visit. No high-pressure sales, no obligation."
    )

    body = "\n".join([hero, intro, why_here, services_grid_html, checklist_html, neigh_html, reviews_html, faq_html, related_html, f'<div class="container">{contact_banner(subtitle="Call, text, or email — your project, your call.")}</div>', final_html])

    head_html = head(TITLE, DESC, URL, og_image=og_url(path=OG_CITY), json_ld=schemas)
    write_page(f"{slug}/index.html", head_html, header(active="areas"), body, breadcrumbs_html=bc)
    print(f"Wrote /{slug}/index.html")


if __name__ == "__main__":
    for slug in CITIES:
        build_city(slug)
    print(f"\nBuilt {len(CITIES)} city hub pages.")
