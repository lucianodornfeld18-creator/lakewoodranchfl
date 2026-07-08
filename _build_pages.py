#!/usr/bin/env python3
"""Generate /about, /contact, /faq, /financing, /warranty, /thanks, /404.html,
/privacy-policy and /terms for Lakewood Ranch Concrete (concrete & paver contractor).

NEW business: NO invented reviews, ratings, stats, or founding-year claims.
NEVER mention any license — "Fully Insured" / "Free Estimates" only.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *

YEAR = 2026  # current year, used only where a copyright year is needed


# ============================================================================
# ABOUT
# ============================================================================
def build_about():
    URL = f"{SITE}/about/"
    TITLE = f"About {BUSINESS['name']} · Concrete & Paver Crew"
    DESC = clip_desc(
        f"Meet {BUSINESS['name']} — an owner-operated concrete & paver crew based in "
        f"east Bradenton, serving Lakewood Ranch, Manatee & Sarasota. Fully insured, "
        f"free estimates, a written workmanship warranty, and our 42-point install standard."
    )

    schemas = [
        schema_webpage(URL, f"About {BUSINESS['name']}", DESC),
        schema_organization(),
        schema_breadcrumb([("Home", SITE+"/"), ("About", URL)]),
    ]

    bc = breadcrumbs([("Home","/"),("About",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">About · Crew Profile</span>
    <h1>An owner-operated <em>concrete &amp; paver</em> crew,<br>built around the work in front of us.</h1>
    <p class="page-hero-sub">{BUSINESS['name']} is a deliberately small, owner-operated hardscape company in east Bradenton, bordering Lakewood Ranch. The partner answers every call, we measure our own jobs, and the same crew that walks your property for the estimate is the same crew that pours the slab or lays the pavers.</p>
    <div class="page-hero-trust">
      <span>Fully Insured</span>
      <span>Free Estimates</span>
      <span>{CHECKLIST["points"]}-Point Install Standard</span>
      <span>Written Workmanship Warranty</span>
    </div>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">
      <p class="post-lede">{BUSINESS['name']} is an owner-operated concrete and paver crew working out of east Bradenton, in the 34212 ZIP just south of SR-64 and bordering Lakewood Ranch. We pour driveways, patios, pool decks, slabs, and stamped &amp; decorative concrete, and we install paver driveways, patios, walkways, and pool decks &mdash; the kind of hardscape that has to stand up to Florida heat, sandy soil, and afternoon storms for decades.</p>

      <p>There&rsquo;s no call center and no commissioned sales team here. When you call, you reach the partner who runs the crew. When you book a job, the people who measured it are the people who build it &mdash; same crew, start to finish. That is the whole point of staying small on purpose.</p>

      <h2>What we install</h2>

      <p>On the concrete side we pour <strong>driveways</strong>, <strong>patios</strong>, <strong>pool decks</strong>, <strong>slabs &amp; pads</strong> (sheds, AC units, walkways, equipment), and <strong>stamped &amp; decorative concrete</strong> &mdash; and we handle <strong>concrete resurfacing &amp; repair</strong> when an existing surface is sound enough to save. On the paver side we install <strong>paver driveways</strong>, <strong>paver patios &amp; walkways</strong>, and <strong>pool deck pavers &amp; travertine</strong>, plus <strong>paver sealing &amp; restoration</strong> to bring tired hardscape back to life.</p>

      <h2>Why base prep is the whole job</h2>

      <p>Most failed Florida concrete and settled pavers trace back to one thing: a base that was rushed. Sandy and organic soils don&rsquo;t support a slab on their own. We excavate to depth, cut out soft or muck soil, bring in compactable limerock or road base, and compact it in lifts before anything is poured or laid. The prep that prevents the crack is the prep nobody ever sees &mdash; and it&rsquo;s exactly where we refuse to cut corners.</p>

      <h2>Where we work</h2>

      <p>Our service area runs across Lakewood Ranch, Manatee &amp; Sarasota and out along the Suncoast: <a href="/lakewood-ranch/">Lakewood Ranch</a>, <a href="/bradenton/">Bradenton</a>, <a href="/parrish/">Parrish</a>, <a href="/palmetto/">Palmetto</a>, <a href="/ellenton/">Ellenton</a>, <a href="/sarasota/">Sarasota</a>, <a href="/venice/">Venice</a>, and the surrounding communities within roughly a 60-mile radius of our Bradenton 34212 base. We keep the radius tight on purpose &mdash; we&rsquo;d rather be close enough to be on site fast than spread too thin to do the work right.</p>

      <h2>HOA &amp; ARC-ready hardscape</h2>

      <p>Lakewood Ranch and the master-planned communities around it have architectural review rules on driveway materials, paver colors, and finishes. We build to what passes, document the spec, and can prepare the ARC submittal package so your project clears review the first time &mdash; not on the third revision.</p>

      <div class="post-key-takeaway">
        <strong>Our Promise — In Plain English</strong>
        We&rsquo;ll measure your project on site, check the soil and the drainage, review any HOA / ARC rules, talk through finishes, and email you a written, line-itemized quote within 24 hours of the visit. If we get the job, the same crew that measured will be the crew that builds it. The surface passes our {CHECKLIST["points"]}-point install standard before we ask you to sign off, and the workmanship warranty is in writing.
      </div>

      <h2>Fully insured &mdash; and accountable</h2>

      <p>We carry insurance on every job, and we&rsquo;re happy to provide a certificate to your HOA or association before we start. We don&rsquo;t invent credentials or stats we don&rsquo;t have &mdash; what we offer is a fully insured crew, a clear written scope, our {CHECKLIST["points"]}-point standard, and a written workmanship warranty you keep on file along with your job photos.</p>

      <h2>How to get a quote</h2>

      <p>Three ways: <a href="{TEL_LINK}">call or text {BUSINESS["phone_display"]}</a>, <a href="mailto:{BUSINESS["email"]}">email us at {BUSINESS["email"]}</a>, or <a href="/contact/#quote">fill out the form on our contact page</a>. We respond to every inquiry, and we&rsquo;ll schedule a free on-site measure as quickly as the calendar allows &mdash; often same week.</p>
    </article>
  </div>
</section>

{final_cta(headline="Meet the crew. See the work.", sub="Free on-site measure. Written quote within 24 hours. No high-pressure sales, no obligation.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas, og_type="article")
    body = hero + body_content
    write_page("about/index.html", head_html, header(active="about"), body, breadcrumbs_html=bc)
    print("Wrote /about/index.html")


# ============================================================================
# CONTACT
# ============================================================================
def build_contact():
    URL = f"{SITE}/contact/"
    TITLE = f"Contact {BUSINESS['name']} · Free Estimate · {BUSINESS['city']} FL"
    DESC = clip_desc(
        f"Get a free, written concrete or paver estimate within 24 hours. Call "
        f"{BUSINESS['phone_display']}, email {BUSINESS['email']}, or send your project "
        f"details below. Serving Lakewood Ranch, Manatee & Sarasota. Fully insured."
    )

    schemas = [
        schema_webpage(URL, f"Contact {BUSINESS['name']}", DESC),
        schema_local_business(URL, f"Contact {BUSINESS['name']}"),
        schema_breadcrumb([("Home", SITE+"/"), ("Contact", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("Contact",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Contact · Free Estimate · Fully Insured</span>
    <h1>Call us<span class="stop">.</span> Text us<span class="stop">.</span><br>Or send a <em>note</em>.</h1>
    <p class="page-hero-sub">Free estimates on concrete and paver projects across Lakewood Ranch, Manatee &amp; Sarasota. We respond to every inquiry, and we&rsquo;ll get a written, line-itemized quote back to you within 24 hours of the on-site measure.</p>
  </div>
</section>'''

    hours_rows = ''.join(
        f"<tr style='border-bottom:1px solid var(--rule)'><td style='padding:9px 0;font-weight:600'>{d}</td>"
        f"<td style='padding:9px 0;text-align:right;color:var(--gray)'>"
        f"{('Closed' if o=='Closed' else o + '&ndash;' + c)}</td></tr>"
        for d, o, c in BUSINESS["hours"]
    )

    city_options = ''.join(f'<option value="{c["name"]}">{c["name"]}</option>' for c in CITIES.values())
    service_options = ''.join(f'<option value="{s["name"]}">{s["name"]}</option>' for s in SERVICES.values())

    contact_grid = f'''<section>
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start">

      <div>
        <span class="mono-label">Direct Lines</span>
        <h2 style="font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.1;letter-spacing:-.02em;margin:.6rem 0 1.6rem">The fastest way is to <em>just call</em>.</h2>

        <div style="display:flex;flex-direction:column;gap:20px;margin-bottom:2rem">
          <a href="{TEL_LINK}" style="text-decoration:none;color:var(--ink);display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid var(--rule)">
            <span style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);font-weight:600">Phone / Text</span>
            <span style="font-family:var(--font-display);font-size:clamp(1.6rem,3vw,2rem);color:var(--ink);letter-spacing:-.02em;flex-grow:1;text-align:right">{BUSINESS["phone_display"]}</span>
          </a>
          <a href="mailto:{BUSINESS["email"]}" style="text-decoration:none;color:var(--ink);display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid var(--rule)">
            <span style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);font-weight:600">Email</span>
            <span style="font-family:var(--font-editorial);font-size:clamp(1.1rem,2vw,1.4rem);color:var(--ink);font-style:italic;flex-grow:1;text-align:right">{BUSINESS["email"]}</span>
          </a>
          <a href="{WA_LINK}" target="_blank" rel="noopener" style="text-decoration:none;color:var(--ink);display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid var(--rule)">
            <span style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--orange);font-weight:600">WhatsApp</span>
            <span style="font-family:var(--font-mono);font-size:1rem;color:var(--ink);flex-grow:1;text-align:right">{BUSINESS["phone_display"]}</span>
          </a>
        </div>

        <span class="mono-label">Service Area</span>
        <p style="margin:.6rem 0 1.6rem;font-size:1.05rem;line-height:1.6">Based in east {BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]} &mdash; just south of SR-64, bordering Lakewood Ranch. We serve Lakewood Ranch, Manatee &amp; Sarasota and the surrounding Suncoast within roughly a 60-mile radius, and travel further by quote. As a service-area business we come to you &mdash; there&rsquo;s no storefront to visit.</p>

        <span class="mono-label">Hours</span>
        <table style="margin-top:.8rem;width:100%;font-family:var(--font-mono);font-size:.85rem;border-collapse:collapse">
          {hours_rows}
        </table>
      </div>

      <div id="quote">
        <span class="mono-label">Free Estimate Request</span>
        <h2 style="font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.1;letter-spacing:-.02em;margin:.6rem 0 1.6rem">Or send us the <em>details</em>.</h2>
        <p style="font-size:1rem;color:var(--gray);margin-bottom:1.4rem">Tell us about the project &mdash; the surface, the rough square footage, and your timeline. The more detail, the better the first response. We&rsquo;ll reply by phone or email.</p>

        <form class="form-wrap" action="https://api.web3forms.com/submit" method="POST">
          <input type="hidden" name="access_key" value="74487312-c3a2-4317-b586-9a41224cad9a">
          <input type="hidden" name="subject" value="New Free-Estimate Request — {BUSINESS['domain']}">
          <input type="hidden" name="from_name" value="{BUSINESS['name']} Website">
          <input type="hidden" name="redirect" value="{SITE}/thanks/">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-grid">
            <label>Name<input type="text" name="name" required></label>
            <label>Phone<input type="tel" name="phone" required></label>
            <label class="full">Email<input type="email" name="email" required></label>
            <label>City<select name="city" required>
              <option value="">Select…</option>
              {city_options}
              <option value="Other">Other / Not Listed</option>
            </select></label>
            <label>Approx. Size<select name="size">
              <option value="">Select…</option>
              <option>Under 300 sq ft</option>
              <option>300 – 600 sq ft</option>
              <option>600 – 1,000 sq ft</option>
              <option>1,000 – 2,000 sq ft</option>
              <option>2,000+ sq ft</option>
              <option>Driveway only</option>
              <option>Repair / resurfacing only</option>
            </select></label>
            <label class="full">Service Interest<select name="service">
              <option value="">Select…</option>
              {service_options}
              <option>Not sure yet</option>
            </select></label>
            <label class="full">Tell us about the project<textarea name="message" placeholder="Surface, square footage, current condition, finish you have in mind, timeline, and anything else worth mentioning."></textarea></label>
            <button type="submit" class="btn btn-orange form-submit">Send Request <span class="btn-arrow"></span></button>
          </div>
        </form>
      </div>

    </div>
  </div>
</section>

{contact_banner("Prefer to talk it through?", "Call or text — same number, same crew picks up.")}

{final_cta(headline="Free estimate on your concrete or paver project.", sub="On-site measure, transparent pricing, written quote within 24 hours. Fully insured.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("contact/index.html", head_html, header(active="contact"), hero + contact_grid, breadcrumbs_html=bc)
    print("Wrote /contact/index.html")


# ============================================================================
# FAQ — site-wide FAQ
# ============================================================================
def build_faq():
    URL = f"{SITE}/faq/"
    TITLE = f"Concrete & Paver FAQ · Lakewood Ranch · {BUSINESS['name']}"
    DESC = clip_desc(
        f"Answers to the questions Lakewood Ranch, Manatee & Sarasota homeowners ask most: "
        f"concrete vs. pavers, cost, timelines, cracking, sealing, HOA / ARC rules, and how "
        f"Florida sun and soil affect your project."
    )

    site_faqs = [
        ("Do you provide free estimates?", "Yes — every estimate is free, on-site, and no-obligation. We measure the project, check the soil and drainage, review any HOA / ARC requirements, talk through finishes and materials, and email you a written, line-itemized quote within 24 hours of the visit."),
        ("Are you insured?", f"Yes &mdash; we&rsquo;re fully insured, and we&rsquo;re happy to provide a certificate of insurance to your HOA or association before we start. We focus on what we can stand behind: a fully insured crew, a clear written scope, our {CHECKLIST['points']}-point install standard, and a written workmanship warranty."),
        ("Should I choose poured concrete or pavers?", "Both are excellent in Florida when installed right — the choice comes down to look, budget, repairability, and HOA / ARC rules. Poured concrete (including stamped and decorative finishes) is typically lower cost and seamless; pavers cost more up front but are easy to lift and reset for repairs and offer more color and pattern options. We&rsquo;ll show you both at the estimate and tell you honestly which fits your home and community. Our <a href='/blog/pavers-vs-concrete-driveway-florida/'>pavers vs. concrete guide</a> breaks down the trade-offs."),
        ("Why does Florida concrete crack, and can you prevent it?", "Sandy soil, heat, and skipped control joints are the usual culprits. Concrete moves with temperature, so we plan control and expansion joints at engineered spacing and place fiber mesh, wire, or rebar to spec — so the slab cracks where we tell it to, in the joint, instead of across your new driveway. Solid base prep does the rest. Our <a href='/blog/why-florida-concrete-cracks-and-how-to-prevent-it/'>cracking guide</a> explains it in detail."),
        ("How long does a project take?", "Rough rule of thumb: a typical driveway or patio pour is 1–3 working days of on-site work, plus cure time before you drive or place furniture on it. Paver projects of similar size run 2–4 days. Stamped and decorative concrete adds a day or two for coloring and sealing. We give you a real timeline in the written quote, including the cure window before the surface can take traffic."),
        ("How long before I can use a new concrete surface?", "Concrete continues to cure for weeks, but you can usually walk on a slab within 24–48 hours and drive a passenger vehicle on a new driveway after about 7 days, depending on weather and mix. Pavers are walkable almost immediately and drivable within a day or two once joints are sanded and compacted. We give you the exact cure and care window for your project at walkthrough."),
        ("Do you handle HOA and ARC approvals in Lakewood Ranch?", "Yes. Lakewood Ranch and the master-planned communities around it have architectural review rules on driveway materials, paver colors, and finishes. We build to what passes, document the spec, and can prepare the ARC submittal package so your project clears review the first time."),
        ("How often do pavers need sealing and re-sanding in Florida?", "In the Florida sun and rain, most paver surfaces benefit from re-sanding and sealing every 2–4 years — sooner for driveways and pool decks that see heavy use. Sealing locks the joint sand, resists weeds and ants, deepens the color, and makes the surface easier to clean. See our <a href='/blog/paver-sealing-resanding-florida-guide/'>paver sealing guide</a> for the full breakdown."),
        ("Do you remove and haul away the old driveway or slab?", "Yes — demo and haul-away of an existing driveway, patio, slab, or paver field is included in the estimate and itemized on the quote. We protect your landscaping and adjacent surfaces during demo and haul the debris to the appropriate facility."),
        ("What finishes can you do on stamped or decorative concrete?", "We offer broom, smooth-trowel, exposed-aggregate, and a wide range of stamped patterns and color combinations — slate, stone, brick, wood-plank, and more — finished with the right sealer for Florida UV. We bring samples to the estimate and apply the approved color and release on a test area so there are no surprises."),
        ("Do you offer a warranty?", "Yes. Every pour and every paver install carries a written workmanship warranty on our labor. You keep a copy of the warranty and the job photos, and we honor it. Material warranties (concrete admixtures, pavers, sealers) are covered by the manufacturer, and we&rsquo;ll explain what applies to your project."),
        ("How far do you travel?", "We&rsquo;re based in east Bradenton (34212) bordering Lakewood Ranch and serve a roughly 60-mile radius across Manatee and Sarasota and out along the Suncoast. If you&rsquo;re near the edge of that radius, call and we&rsquo;ll let you know."),
    ]

    schemas = [
        schema_faqpage(site_faqs),
        schema_breadcrumb([("Home", SITE+"/"), ("FAQ", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("FAQ",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Frequently Asked · Concrete &amp; Pavers</span>
    <h1>Real questions<span class="stop">.</span><br><em>Real answers</em>, in writing.</h1>
    <p class="page-hero-sub">The questions we hear most from Lakewood Ranch, Manatee &amp; Sarasota homeowners about concrete and paver projects — cost, timelines, cracking, sealing, finishes, HOA / ARC rules, and process.</p>
  </div>
</section>'''

    faq_html = faq_section(site_faqs, headline="Everything we get asked, weekly.", label="Site-Wide FAQ")
    faq_html = faq_html.replace('<div class="section-head-num">07</div>', '<div class="section-head-num">01</div>')

    body = hero + faq_html + f'<div class="container">{contact_banner("Question we didn&rsquo;t answer?", "Call or text — driveways, patios, pool decks &amp; pavers.")}</div>' + final_cta(headline="Free estimate on your concrete or paver project.", sub="On-site measure, transparent pricing, written quote within 24 hours. Fully insured.")
    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("faq/index.html", head_html, header(active=""), body, breadcrumbs_html=bc)
    print("Wrote /faq/index.html")


# ============================================================================
# FINANCING
# ============================================================================
def build_financing():
    URL = f"{SITE}/financing/"
    TITLE = f"Concrete & Paver Financing · {BUSINESS['name']}"
    DESC = clip_desc(
        f"Financing options for concrete and paver projects across Lakewood Ranch, Manatee "
        f"& Sarasota. 0% promotional periods and fixed-payment plans through trusted "
        f"third-party lenders. No in-house pressure."
    )
    schemas = [
        schema_webpage(URL, "Concrete & Paver Financing", DESC),
        schema_breadcrumb([("Home", SITE+"/"), ("Financing", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("Financing",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Financing · Independent Third-Party Lenders</span>
    <h1>Pay over time<span class="stop">.</span><br>No <em>in-house pressure</em>.</h1>
    <p class="page-hero-sub">We don&rsquo;t run financing in-house — we don&rsquo;t want to. We work with reputable home-improvement lenders that offer 0% promotional periods and fixed-payment plans on larger concrete and paver projects.</p>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">
      <p class="post-lede">A good concrete contractor shouldn&rsquo;t also be your bank. We pour and pave &mdash; we don&rsquo;t process loan applications. Instead, we point you to established home-improvement lenders, and we&rsquo;ll walk you through the options on the day of your free estimate.</p>

      <h2>Why we don&rsquo;t do in-house financing</h2>
      <p>Plenty of contractors that &ldquo;offer financing&rdquo; have a commissioned salesperson steering you toward a bigger contract to maximize the loan. We don&rsquo;t. Our crew is paid to build, not to sell, and the financing decision is yours to make with the lender directly &mdash; not with us in the middle.</p>

      <h2>How third-party financing typically works</h2>
      <p>Most home-improvement lenders offer two kinds of plans: 0% APR promotional periods (commonly 6, 12, 18, or 24 months) for qualified borrowers on projects over a few thousand dollars, and fixed-payment installment loans over longer terms at a fixed APR. Promotional plans are best when you can pay the balance off inside the promo window; fixed-payment loans are better when you want a predictable monthly payment over a longer horizon. Applications are online and decisions are usually quick.</p>

      <div class="post-key-takeaway">
        <strong>How to Apply</strong>
        Tell us at the estimate that you&rsquo;re interested in financing. We&rsquo;ll point you to the lender&rsquo;s application the same day. You apply directly with the lender — we don&rsquo;t collect or transmit your financial information. Once approved, the lender pays us for the work, and you pay the lender according to your plan&rsquo;s terms.
      </div>

      <h2>Cash, check, and card</h2>
      <p>We also accept the usual payment forms: cash, business or personal check, and major credit cards. If a card payment carries a processor surcharge, it&rsquo;s itemized in the quote &mdash; that&rsquo;s the card processor&rsquo;s fee, not a markup.</p>

      <h2>Insurance &amp; storm-damage work</h2>
      <p>Some of our repair and replacement work is insurance-driven &mdash; storm damage, root or settlement heave, and similar. We document what an adjuster needs (scope, dated photos, and pre-loss condition where determinable) in the format carriers expect. You handle the claim with your carrier; our paperwork supports it.</p>

      <h2>A note on promotional financing</h2>
      <p>If you take a 0% promotional plan, <strong>pay off the balance before the promo period ends</strong>. Many promotional plans are deferred-interest, which means any remaining balance at the end of the promo can trigger interest retroactively from day one. Set a calendar reminder and pay it off in time. The math only works if you do.</p>
    </article>
  </div>
</section>

{final_cta(headline="Numbers work? Let&rsquo;s schedule the measure.", sub="Free estimate first. Financing conversation after, only if you want one.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("financing/index.html", head_html, header(active=""), hero + body_content, breadcrumbs_html=bc)
    print("Wrote /financing/index.html")


# ============================================================================
# WARRANTY
# ============================================================================
def build_warranty():
    URL = f"{SITE}/warranty/"
    TITLE = f"Workmanship Warranty · {BUSINESS['name']}"
    DESC = clip_desc(
        f"Our written workmanship warranty on every concrete pour and paver install across "
        f"Lakewood Ranch, Manatee & Sarasota. What&rsquo;s covered, what isn&rsquo;t, and how to "
        f"make a claim. Fully insured."
    )
    schemas = [
        schema_webpage(URL, "Workmanship Warranty", DESC),
        schema_breadcrumb([("Home", SITE+"/"), ("Warranty", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("Warranty",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Workmanship Warranty · In Writing</span>
    <h1>If we pour it or lay it,<br><em>we stand behind it</em>.</h1>
    <p class="page-hero-sub">Every concrete pour and every paver install carries a written workmanship warranty on our labor. Here&rsquo;s exactly what&rsquo;s covered, what isn&rsquo;t, and how to make a claim.</p>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">

      <p class="post-lede">Every {BUSINESS['name']} project carries a written workmanship warranty on our labor, effective from the date of substantial completion (the final walkthrough). The warranty is yours as the homeowner, and it&rsquo;s honored by us, in person, by the same crew that did the work.</p>

      <h2>What&rsquo;s covered</h2>

      <p>Anything attributable to the quality of our installation:</p>
      <ul>
        <li>Surface failures that trace back to base prep we performed &mdash; settling or sinking from inadequate compaction.</li>
        <li>Cracking outside the engineered control and expansion joints that is attributable to our forming, jointing, or reinforcement.</li>
        <li>Paver field movement, dipping, or rutting attributable to base or edge-restraint work we installed.</li>
        <li>Joint sand failure or edge-restraint detachment on paver installs within the warranty period.</li>
        <li>Finish defects (delamination, flaking, or peeling of stamped color or sealer) attributable to our application.</li>
        <li>Drainage that doesn&rsquo;t perform as designed because of slope we set incorrectly.</li>
        <li>Any other workmanship-related failure that traces back to our crew.</li>
      </ul>

      <h2>What isn&rsquo;t covered</h2>

      <p>Three categories, all of which we&rsquo;ll talk through on the estimate:</p>
      <ul>
        <li><strong>Hairline and shrinkage cracking.</strong> Concrete is a material that cracks &mdash; that&rsquo;s why we install control joints. Fine hairline cracks and minor shrinkage cracking are normal and are not a workmanship defect. We design the joints to control where the larger cracks go.</li>
        <li><strong>Damage from misuse or abuse.</strong> Driving heavy equipment, trucks, or dumpsters onto a residential-rated slab or paver field; chemical spills; dragging heavy objects; or improper pressure-washing &mdash; none of those are workmanship issues.</li>
        <li><strong>Acts of nature and ground movement.</strong> Hurricane and flood damage, sinkhole or major settlement events, root heave from trees, lightning, and structural movement of the home &mdash; the surface isn&rsquo;t designed to withstand those, and the warranty doesn&rsquo;t pretend to either.</li>
      </ul>

      <div class="post-key-takeaway">
        <strong>The Honest Take</strong>
        Most workmanship issues, if they appear at all, show up in the first season as the surface goes through its first full heat-and-rain cycle. That&rsquo;s exactly what base prep, engineered joints, and proper curing are designed to prevent — and it&rsquo;s why we won&rsquo;t shortcut any of them.
      </div>

      <h2>How to make a claim</h2>

      <p>Call or email us. That&rsquo;s it. We&rsquo;ll come out, inspect the issue, and if it&rsquo;s a workmanship problem we make it right &mdash; no run-around. If we determine it&rsquo;s not a workmanship issue (normal hairline cracking, a material issue, misuse, or an act-of-nature event), we&rsquo;ll tell you so clearly, explain why in writing, and quote any repair work separately.</p>

      <h2>What stays in your job file</h2>

      <p>Every job we complete leaves the homeowner with documentation that is your warranty trigger:</p>
      <ul>
        <li>The signed agreement showing scope and pricing.</li>
        <li>Photos of the base prep, forming, and reinforcement before the pour or paver install.</li>
        <li>Pre- and post-project photos of the work area.</li>
        <li>The mix / material and finish spec used.</li>
        <li>The signed final walkthrough form.</li>
        <li>The written workmanship warranty with the start date and term.</li>
      </ul>

      <p>Keep the file. If anything comes up within the warranty period, that&rsquo;s your proof.</p>

      <h2>Fully insured</h2>

      <p>Beyond the workmanship warranty, we carry insurance on every job and can provide a certificate to your HOA or association on request before work begins.</p>

    </article>
  </div>
</section>

{final_cta(headline="Warranty work you&rsquo;ll never need.", sub="The best warranty claim is the one that never gets filed. That&rsquo;s the install we&rsquo;re trying to do.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("warranty/index.html", head_html, header(active=""), hero + body_content, breadcrumbs_html=bc)
    print("Wrote /warranty/index.html")


# ============================================================================
# PRIVACY POLICY
# ============================================================================
def build_privacy():
    URL = f"{SITE}/privacy-policy/"
    TITLE = f"Privacy Policy · {BUSINESS['name']}"
    DESC = clip_desc(
        f"How {BUSINESS['name']} collects, uses, and protects the information you share "
        f"through our website and estimate form. We never sell your data."
    )
    schemas = [
        schema_webpage(URL, "Privacy Policy", DESC),
        schema_breadcrumb([("Home", SITE+"/"), ("Privacy Policy", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("Privacy Policy",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Legal · Privacy</span>
    <h1>Privacy <em>Policy</em>.</h1>
    <p class="page-hero-sub">{BUSINESS['name']} respects your privacy. This policy explains what information we collect through this website, how we use it, and the choices you have. Last updated {YEAR}.</p>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">

      <p class="post-lede">{BUSINESS['name']} (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;) operates the website at {BUSINESS['domain']}. We are a concrete and paver contractor serving Lakewood Ranch, Manatee &amp; Sarasota and the surrounding Suncoast. This Privacy Policy describes how we handle information collected through this website.</p>

      <h2>Information we collect</h2>
      <p>We collect two kinds of information:</p>
      <ul>
        <li><strong>Information you give us.</strong> When you submit our estimate / contact form, we collect the details you provide &mdash; typically your name, phone number, email address, city, project type, approximate size, and any message you include. We use this only to respond to your inquiry and provide an estimate.</li>
        <li><strong>Information collected automatically.</strong> Like most websites, we use analytics to understand how visitors use the site. This includes data such as pages viewed, approximate location, device and browser type, and referring source, collected through cookies and similar technologies.</li>
      </ul>

      <h2>Cookies and analytics</h2>
      <p>This website uses Google Analytics 4 (GA4) to measure traffic and improve the site. GA4 sets cookies that help us understand aggregate visitor behavior &mdash; for example, which pages are most useful and where visitors come from. This data is used in aggregate and is not used to personally identify you. You can disable cookies in your browser settings or opt out of Google Analytics using Google&rsquo;s opt-out tools; the site will still work.</p>

      <h2>How we use your information</h2>
      <ul>
        <li>To respond to estimate requests and contact-form submissions.</li>
        <li>To schedule and perform the work you ask us to quote or complete.</li>
        <li>To follow up about your project and provide customer service.</li>
        <li>To improve our website and understand how it is used.</li>
        <li>To comply with applicable law.</li>
      </ul>

      <h2>We do not sell your data</h2>
      <p>We do not sell, rent, or trade your personal information to anyone. We share information only with service providers that help us operate &mdash; for example, our form-delivery provider and our analytics provider &mdash; and only to the extent needed to provide their service. We may also disclose information if required by law.</p>

      <h2>Data retention and security</h2>
      <p>We keep estimate and contact information only as long as needed to serve you and to maintain ordinary business records. We use reasonable safeguards to protect the information you share, though no method of transmission over the internet is completely secure.</p>

      <h2>Third-party links</h2>
      <p>Our website may link to third-party sites (for example, a review profile or a lender&rsquo;s application). We are not responsible for the privacy practices of those sites; review their policies separately.</p>

      <h2>Children&rsquo;s privacy</h2>
      <p>This website is intended for adults seeking home-improvement services and is not directed to children under 13. We do not knowingly collect information from children.</p>

      <h2>Your choices</h2>
      <p>You can ask us what information we hold about you, request that we correct or delete it, or ask us not to contact you further. To make a request, contact us using the details below.</p>

      <h2>Changes to this policy</h2>
      <p>We may update this Privacy Policy from time to time. The &ldquo;last updated&rdquo; date above reflects the most recent revision.</p>

      <h2>Contact us</h2>
      <p>Questions about this policy or your information? <a href="{TEL_LINK}">Call or text {BUSINESS["phone_display"]}</a> or <a href="mailto:{BUSINESS["email"]}">email {BUSINESS["email"]}</a>.</p>

    </article>
  </div>
</section>

{final_cta(headline="Ready for a free estimate?", sub="On-site measure, transparent pricing, written quote within 24 hours. Fully insured.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("privacy-policy/index.html", head_html, header(active=""), hero + body_content, breadcrumbs_html=bc)
    print("Wrote /privacy-policy/index.html")


# ============================================================================
# TERMS OF SERVICE
# ============================================================================
def build_terms():
    URL = f"{SITE}/terms/"
    TITLE = f"Terms of Service · {BUSINESS['name']}"
    DESC = clip_desc(
        f"The terms that govern your use of the {BUSINESS['name']} website and the estimates "
        f"and information provided here. Serving Lakewood Ranch, Manatee & Sarasota."
    )
    schemas = [
        schema_webpage(URL, "Terms of Service", DESC),
        schema_breadcrumb([("Home", SITE+"/"), ("Terms of Service", URL)]),
    ]
    bc = breadcrumbs([("Home","/"),("Terms of Service",None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Legal · Terms</span>
    <h1>Terms of <em>Service</em>.</h1>
    <p class="page-hero-sub">These terms govern your use of the {BUSINESS['name']} website and the information and estimates provided through it. Last updated {YEAR}.</p>
  </div>
</section>'''

    body_content = f'''<section>
  <div class="container">
    <article class="page-article">

      <p class="post-lede">By using the website at {BUSINESS['domain']} (the &ldquo;Site&rdquo;), operated by {BUSINESS['name']} (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;), you agree to these Terms of Service. If you do not agree, please do not use the Site.</p>

      <h2>About our services</h2>
      <p>We are a concrete and paver contractor serving Lakewood Ranch, Manatee &amp; Sarasota and the surrounding Suncoast. The Site provides information about our services and lets you request a free estimate. Using the Site or requesting an estimate does not create a contract for work; any project is governed by a separate written agreement we provide and you sign.</p>

      <h2>Estimates and pricing information</h2>
      <p>Pricing, ranges, and timelines shown on the Site are general information to help you plan and are not a binding quote. Your actual price depends on an on-site measure of your specific project, site conditions, material selections, and scope. Only a written, signed estimate is binding.</p>

      <h2>Use of the Site</h2>
      <ul>
        <li>You may use the Site for lawful, personal purposes related to seeking our services.</li>
        <li>You agree not to misuse the Site, attempt to disrupt it, or submit false, abusive, or automated form submissions.</li>
        <li>The content on the Site &mdash; text, images, and design &mdash; is owned by us or our licensors and may not be copied or reused without permission.</li>
      </ul>

      <h2>Form submissions</h2>
      <p>When you submit a form, you confirm the information is accurate and that you are the owner of the contact details provided or are authorized to use them. We use that information to respond to you as described in our <a href="/privacy-policy/">Privacy Policy</a>.</p>

      <h2>No warranties on the Site</h2>
      <p>The Site is provided &ldquo;as is.&rdquo; While we work to keep information accurate and current, we make no warranty that the Site will be error-free, uninterrupted, or complete. This does not affect the written workmanship warranty we provide on completed projects, which is described on our <a href="/warranty/">warranty page</a>.</p>

      <h2>Limitation of liability</h2>
      <p>To the fullest extent permitted by law, we are not liable for any indirect, incidental, or consequential damages arising from your use of the Site. Nothing in these terms limits liability that cannot be limited under applicable law.</p>

      <h2>Third-party links</h2>
      <p>The Site may link to third-party websites for your convenience. We do not control and are not responsible for the content or practices of those sites.</p>

      <h2>Governing law</h2>
      <p>These terms are governed by the laws of the State of Florida, without regard to its conflict-of-laws rules. Any dispute relating to the Site will be handled in the courts located in {BUSINESS['county']}, Florida.</p>

      <h2>Changes to these terms</h2>
      <p>We may update these terms from time to time. The &ldquo;last updated&rdquo; date above reflects the most recent revision, and continued use of the Site means you accept the current terms.</p>

      <h2>Contact us</h2>
      <p>Questions about these terms? <a href="{TEL_LINK}">Call or text {BUSINESS["phone_display"]}</a> or <a href="mailto:{BUSINESS["email"]}">email {BUSINESS["email"]}</a>.</p>

    </article>
  </div>
</section>

{final_cta(headline="Ready for a free estimate?", sub="On-site measure, transparent pricing, written quote within 24 hours. Fully insured.")}'''

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("terms/index.html", head_html, header(active=""), hero + body_content, breadcrumbs_html=bc)
    print("Wrote /terms/index.html")


# ============================================================================
# THANKS (form submission landing)
# ============================================================================
def build_thanks():
    URL = f"{SITE}/thanks/"
    TITLE = f"Thanks · {BUSINESS['name']}"
    DESC = f"Thanks for reaching out to {BUSINESS['name']}. We've received your request and will respond as quickly as we can."
    schemas = [schema_breadcrumb([("Home", SITE+"/"), ("Thanks", URL)])]
    bc = breadcrumbs([("Home","/"),("Thanks",None)])

    body = f'''<section class="page-hero">
  <div class="page-hero-inner" style="text-align:center;max-width:760px;margin:0 auto">
    <span class="mono-label" style="justify-content:center">● Message Received</span>
    <h1>Got it<span class="stop">.</span> <em>Talk soon</em>.</h1>
    <p class="page-hero-sub" style="margin-left:auto;margin-right:auto">We&rsquo;ve received your request. Expect a response from the crew &mdash; not a call center &mdash; as quickly as we can get back to you, and we&rsquo;ll work toward a written estimate within 24 hours of the on-site measure.</p>
    <div style="margin-top:2rem;display:flex;justify-content:center;gap:14px;flex-wrap:wrap">
      <a href="/" class="btn btn-outline-light">Back to Home</a>
      <a href="/blog/" class="btn btn-outline-light">Read the Journal</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <span class="mono-label" style="justify-content:center">In a hurry?</span>
      <h2 style="font-family:var(--font-editorial);font-weight:500;font-size:clamp(1.6rem,3vw,2.4rem);line-height:1.1;letter-spacing:-.02em;margin:.8rem 0 1.2rem">Just call instead.</h2>
      <a href="{TEL_LINK}" style="font-family:var(--font-display);font-size:clamp(2rem,5vw,3rem);color:var(--orange-deep);letter-spacing:-.02em;text-decoration:underline;text-underline-offset:8px;text-decoration-thickness:3px">{BUSINESS["phone_display"]}</a>
    </div>
  </div>
</section>'''

    head_html = head(TITLE, DESC, URL, indexable=False, json_ld=schemas)
    write_page("thanks/index.html", head_html, header(active=""), body, breadcrumbs_html=bc)
    print("Wrote /thanks/index.html")


# ============================================================================
# 404
# ============================================================================
def build_404():
    body = f'''<section class="page-hero">
  <div class="page-hero-inner" style="text-align:center;max-width:760px;margin:0 auto">
    <span class="mono-label" style="justify-content:center">Error 404 · Page Not Found</span>
    <h1>That&rsquo;s a <em>dead-end</em>.</h1>
    <p class="page-hero-sub" style="margin-left:auto;margin-right:auto">The page you&rsquo;re looking for doesn&rsquo;t exist, has moved, or was never there to begin with. Try one of the links below — or just call.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:920px;margin:0 auto;display:grid;grid-template-columns:repeat(2,1fr);gap:14px">
      {''.join(f'<a href="/{s}/" class="neighborhood-pill">{SERVICES[s]["name"]}</a>' for s in SERVICE_ORDER)}
    </div>
    <div style="text-align:center;margin-top:3rem"><a href="/" class="btn btn-orange">Back to Home <span class="btn-arrow"></span></a></div>
  </div>
</section>'''

    head_html = head(f"404 · Page Not Found · {BUSINESS['name']}", "Page not found. Try a service link or call.", f"{SITE}/404.html", indexable=False)
    out = "404.html"
    html = wrap_page(head_html, header(active=""), body)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {out}")


if __name__ == "__main__":
    build_about()
    build_contact()
    build_faq()
    build_financing()
    build_warranty()
    build_privacy()
    build_terms()
    build_thanks()
    build_404()
