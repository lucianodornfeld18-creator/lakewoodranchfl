#!/usr/bin/env python3
"""Generate /blog/ index + blog posts (5 general concrete/paver guides + 72 per-(service,city) cost guides)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *

ALL_POSTS = []  # assembled as we go for the index


# ============================================================================
# Local helpers
# ============================================================================
def clip_title(s, n=65):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0].rstrip(" ,·-") + "…"


def _author_initial():
    return BUSINESS["name"].strip()[0].upper() if BUSINESS.get("name") else "L"


# ============================================================================
# Helper: render a post's article body
# ============================================================================
def post_shell(post, lede, sections_html, faqs=None, related_links=None, cta_headline=None):
    """Common wrapper for any blog post."""
    URL = f"{SITE}/blog/{post['slug']}/"
    TITLE = clip_title(post["title"])
    DESC = clip_desc(post["meta_desc"])
    cat = post.get("category", "Concrete")
    date_pretty = post["date_published"][:10]

    schemas = [
        schema_article(post, URL),
        schema_breadcrumb([
            ("Home", SITE + "/"),
            ("Journal", f"{SITE}/blog/"),
            (post["title"], URL),
        ]),
        schema_webpage(URL, post["title"], DESC),
    ]
    if faqs:
        schemas.append(schema_faqpage(faqs))

    bc = breadcrumbs([
        ("Home", "/"),
        ("Journal", "/blog/"),
        (post["title"][:50] + ("…" if len(post["title"]) > 50 else ""), None),
    ])

    article_hero = f'''<section class="page-hero" style="padding:60px 0 50px">
  <div class="page-hero-inner">
    <div class="post-meta-bar" style="color:rgba(245,242,236,.6)">
      <span class="cat" style="color:var(--orange)">● {cat}</span>
      <span>Published {date_pretty}</span>
      <span>By the {BUSINESS["name"]} Crew</span>
    </div>
    <h1 style="margin-top:14px">{post["title"]}</h1>
    <p class="page-hero-sub" style="font-style:italic">{post["meta_desc"]}</p>
  </div>
</section>'''

    related_block = ""
    if related_links:
        items = "".join(f'<li><a href="{url}">{label}</a></li>' for url, label in related_links)
        related_block = f'''<div class="related-box">
  <div class="related-box-label">Read Next · Related Reading</div>
  <h3>If this helped, also read.</h3>
  <ul>{items}</ul>
</div>'''

    faq_html = ""
    if faqs:
        faq_html = faq_section(faqs, headline="Common questions on this topic.", label="FAQ · Quick Answers")

    author_block = f'''<div class="post-author">
  <div class="post-author-avatar">{_author_initial()}</div>
  <div class="post-author-info">
    <strong>The {BUSINESS["name"]} Crew</strong>
    <span>{BUSINESS["city"]}, FL · Concrete &amp; paver contractor · Fully Insured · {BUSINESS["checklist_name"]}</span>
  </div>
</div>'''

    body = f'''{article_hero}
<section>
  <div class="container">
    <article class="post-article">
      <p class="post-lede">{lede}</p>
      {sections_html}
      {author_block}
      {related_block}
    </article>
  </div>
</section>

{faq_html}

{f'<div class="container">{contact_banner()}</div>'}

{final_cta(headline=cta_headline or post.get("cta_headline", "Got a project this guide would help with?"), sub="Free on-site estimate. Written, line-itemized quote within 24 hours.")}'''

    og_slug = post.get("service_slug") or post.get("primary_service")
    head_html = head(TITLE, DESC, URL, og_image=og_url(og_slug), json_ld=schemas, og_type="article")
    out = f"blog/{post['slug']}/index.html"
    write_page(out, head_html, header(active="blog"), body, breadcrumbs_html=bc)
    ALL_POSTS.append(post)


# ============================================================================
# 5 GENERAL POSTS — handcrafted, concrete-expert content, topic dispatch
# ============================================================================
def _post_pavers_vs_concrete(post):
    lede = (
        "It is the single most common question we field on a Lakewood Ranch driveway "
        "estimate: pavers or poured concrete? Both are excellent surfaces and both "
        "are everywhere in Manatee &amp; Sarasota &mdash; but they age, repair, and price "
        "differently in the Florida sun. Here is the honest, installer&rsquo;s breakdown, "
        "with real 2026 Suncoast numbers and the factors that should actually decide it."
    )
    sections = '''
<h2>The short answer</h2>
<p>For most Suncoast homes, the decision comes down to three things: budget, the look you want, and how you feel about maintenance. Poured concrete costs less up front, gives you a clean monolithic surface, and asks almost nothing of you for years. Pavers cost more, give you a richer high-end look and the ability to lift-and-reset a section, but they ask for periodic re-sanding and sealing to stay sharp. Neither is &ldquo;better&rdquo; in the abstract &mdash; they are better at different things.</p>

<blockquote>A poured driveway is one continuous slab with no joints for weeds or ants. A paver driveway is hundreds of individual units that flex with the ground. That single structural difference drives almost every trade-off below.</blockquote>

<h2>Cost: what each actually runs in 2026</h2>
<p>On the Suncoast in 2026, a standard 4-inch broom-finish concrete driveway runs roughly <strong>$8&ndash;$12 per square foot installed</strong>, fiber-reinforced and properly jointed. Step up to stamped or decorative concrete and you are in the <strong>$15&ndash;$24 per square foot</strong> range &mdash; which, notably, overlaps the bottom of the paver range. Concrete and clay pavers land at roughly <strong>$14&ndash;$26 per square foot installed</strong> depending on the paver, the base, and the pattern.</p>

<table class="post-table">
<thead><tr><th>Surface</th><th>Installed Cost / Sq Ft</th><th>Up-Front vs. Pavers</th></tr></thead>
<tbody>
<tr><td>Broom-finish concrete driveway</td><td><strong>$8&ndash;$12</strong></td><td>Lowest cost</td></tr>
<tr><td>Exposed-aggregate concrete</td><td><strong>$13&ndash;$19</strong></td><td>Mid</td></tr>
<tr><td>Stamped / decorative concrete</td><td><strong>$15&ndash;$24</strong></td><td>Overlaps pavers</td></tr>
<tr><td>Concrete / clay paver driveway</td><td><strong>$14&ndash;$26</strong></td><td>Highest up-front</td></tr>
</tbody>
</table>

<p>On a typical 600 sq ft two-car Suncoast driveway, that is roughly $4,800&ndash;$7,200 for broom-finish concrete versus $8,400&ndash;$15,600 for pavers. The gap is real &mdash; but so is the difference in look and resale presence, which is why so many gated-community homeowners pay it.</p>

<h2>Lifespan and what fails first</h2>
<p>A correctly poured, jointed, and reinforced concrete driveway lasts 25&ndash;30+ years in our climate. What fails it is almost never the concrete itself &mdash; it is the base. A slab on un-compacted sandy fill, or one starved of control joints, will crack and settle long before its time. That is exactly what our base prep and engineered joint layout are built to prevent.</p>
<p>A paver driveway can last just as long or longer, because the surface is modular: if the base settles, you lift the affected pavers, regrade, and relay them. The joint sand and sealer are the maintenance items, not the pavers. In our high-water-table soils, edge restraint and a properly compacted base matter just as much for pavers as joint cutting does for concrete.</p>

<h2>Repair: the deciding factor for a lot of people</h2>
<p>This is where pavers genuinely shine. Stain one paver with oil, crack one under a dropped trailer jack, or settle a section over a sprinkler trench &mdash; you pull and replace just those units, and the repair is invisible. Concrete cannot be spot-repaired invisibly: a crack repair or a patch will always read as a repair, even done well. If your driveway takes heavy or unpredictable loads, or sits over utilities you may need to dig up, pavers are forgiving in a way concrete is not.</p>

<h2>Heat, slip, and the Florida-specific stuff</h2>
<p>Both surfaces can be made cool and grippy &mdash; or hot and slick &mdash; depending on color and finish. Lighter pavers and lighter integral-colored concrete both stay more barefoot-friendly than a dark, dense surface baking in the afternoon sun. For pool decks specifically, this matters even more than for driveways; see our pool-deck surface guide for the full heat comparison.</p>

<h2>HOA and ARC reality in Lakewood Ranch</h2>
<p>In Lakewood Ranch and the master-planned communities around it, your choice may be partly made for you. Many villages run an architectural review committee (ARC) that governs driveway materials, paver colors, and even joint and border patterns. Some communities lean paver; some restrict color palettes; some require a banded border. We match the approved spec and can handle the ARC submittal so the install clears review the first time &mdash; whichever surface you choose.</p>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
Choose poured concrete when budget is the priority, you want a clean low-maintenance surface, and you do not anticipate digging up the driveway. Choose pavers when you want the high-end modular look, the ability to repair invisibly, or your community&rsquo;s ARC favors them &mdash; and you accept periodic re-sanding and sealing. On the Suncoast in 2026, that is roughly a $4,800&ndash;$7,200 broom-finish concrete job versus an $8,400&ndash;$15,600 paver job on a typical two-car driveway. We install both and will tell you honestly which fits your home.
</div>
'''
    related = [
        ("/paver-driveways/lakewood-ranch/", "Paver Driveways in Lakewood Ranch · Service Page"),
        ("/concrete-driveways/lakewood-ranch/", "Concrete Driveways in Lakewood Ranch · Service Page"),
        ("/blog/why-florida-concrete-cracks-and-how-to-prevent-it/", "Why Florida Concrete Cracks"),
        ("/blog/best-pool-deck-surface-florida-heat/", "Coolest Pool Deck Surfaces for Florida Heat"),
    ]
    faqs = [
        ("Are pavers or concrete better for resale value in Lakewood Ranch?",
         "In the gated golf villages and higher-end Lakewood Ranch communities, a quality paver driveway typically reads as the more premium surface and tends to show well at resale &mdash; buyers in that bracket expect it. In more value-oriented neighborhoods, a clean, properly jointed broom-finish or lightly decorative concrete driveway presents perfectly well and the resale difference narrows. The bigger resale killer is a cracked, settled, or stained driveway of either type, which is why prep and maintenance matter more than the material choice alone."),
        ("Do paver driveways really need more maintenance than concrete?",
         "Yes, modestly. Pavers rely on joint sand to lock the field together, and in Florida that sand washes out over time from rain and pressure-washing, so plan on polymeric re-sanding and a fresh coat of sealer every few years to keep them tight and sharp. Concrete asks for far less &mdash; an occasional clean and a re-seal on decorative work. Neither is high-maintenance, but if &lsquo;set it and forget it&rsquo; is your priority, concrete edges it."),
        ("Can you put pavers over my existing concrete driveway?",
         "Sometimes, if the existing slab is sound, draining correctly, and at a height that still works with your garage and apron once pavers are added on top. An overlay can save demo cost, but it is not always the right call &mdash; a cracked or settling slab underneath will telegraph problems up through the pavers. We check the slab during the free estimate and tell you honestly whether an overlay or a full tear-out-and-rebuild is the better long-term value."),
        ("Which holds up better to Florida heat and sun underfoot?",
         "Both can be specified to stay walkable. The driver is color and density, not concrete-versus-paver: lighter tones reflect more sun and run cooler, dark dense surfaces of either type get hot. For driveways this rarely matters since you are not walking them barefoot, but for adjacent pool decks and patios we steer toward lighter colors and textured finishes specifically to keep them comfortable in the midday sun."),
    ]
    post_shell(post, lede, sections, faqs=faqs, related_links=related,
               cta_headline="Pavers or concrete? Get a free side-by-side estimate.")


def _post_cracking_guide(post):
    lede = (
        "Every Florida homeowner has seen it: a driveway or patio that spider-cracks "
        "within a couple of summers of being poured. It is the most common concrete "
        "complaint we are called to fix in Manatee County &mdash; and almost all of it is "
        "preventable. Here is what actually causes Gulf Coast concrete to crack, and "
        "the prep that stops it before the truck ever arrives."
    )
    sections = '''
<h2>First, the honest truth about cracks</h2>
<p>Concrete cracks. That is not a defect &mdash; it is physics. Concrete shrinks as it cures and moves as temperature and moisture change, and no contractor can promise a slab that never cracks. What a good contractor controls is <em>where</em> it cracks. Done right, the inevitable movement relieves itself in a straight, intentional control joint instead of a random web across your new driveway. A hairline crack inside a joint is normal and harmless. A grid of cracks across the field, a heaved edge, or a settled low spot is a prep failure &mdash; and that is what this guide is about.</p>

<h2>The four things that actually crack Florida concrete</h2>

<h3>1. Un-compacted sandy subgrade</h3>
<p>Our Gulf Coast soils are sandy and, in many spots, expansive &mdash; they swell with the rainy-season water table and shrink in the dry months. Pour a slab on loose or poorly compacted fill and the ground moves underneath it, settling unevenly and cracking the concrete from below. This is the single most common cause we see. The fix is unglamorous and invisible: excavate to depth, cut out soft or organic soil, bring in compactable base, and compact it in lifts before anything is poured.</p>

<h3>2. Missing or mis-spaced control joints</h3>
<p>Control joints are the saw-cut or tooled grooves that tell a slab where to crack. Skip them, or space them too far apart, and the slab decides for itself &mdash; usually in an ugly diagonal across the field. As a rule we cut control joints at roughly ten-foot spacing and lay them out to complement the slab&rsquo;s shape. The joints have to be cut at the right depth (about a quarter of the slab thickness) and at the right time, before the slab cracks on its own.</p>

<h3>3. A slab poured too thin, or under-reinforced</h3>
<p>Four inches of fiber-reinforced concrete handles standard cars and light trucks. Park an RV, a boat trailer, or a heavy work truck on a thin, unreinforced slab and it cracks under the point load. We spec slab thickness to the heaviest vehicle the surface will carry, add synthetic fiber to the mix, and step up to five or six inches with added reinforcement where the load demands it.</p>

<h3>4. Water pooling and bad drainage</h3>
<p>Water that ponds against a slab edge undermines the base it sits on and, around pool cages, rusts the footers and stains the concrete. Every surface we pour gets a deliberate slope to drain away from the house, the pool shell, and the cage track. In our summer downpours, a flat slab is a standing-water complaint by the first storm season.</p>

<table class="post-table">
<thead><tr><th>Crack Cause</th><th>What You See</th><th>The Prevention</th></tr></thead>
<tbody>
<tr><td>Un-compacted base</td><td>Settling, heaving, grid cracks</td><td>Excavate, cut out soft soil, compact base in lifts</td></tr>
<tr><td>Missing control joints</td><td>Random diagonal field cracks</td><td>Saw-cut joints at ~10 ft spacing, correct depth</td></tr>
<tr><td>Slab too thin / under-reinforced</td><td>Cracks under heavy vehicles</td><td>Spec thickness to load, fiber + rebar as needed</td></tr>
<tr><td>Bad drainage / ponding</td><td>Edge undermining, rust, stains</td><td>Engineered slope away from house and cage</td></tr>
<tr><td>Curing too fast in the heat</td><td>Surface crazing, weak finish</td><td>Cure compound / wet-cure, pour around the rain</td></tr>
</tbody>
</table>

<h2>The Florida-specific curing problem</h2>
<p>Concrete needs to cure slowly to reach full strength. In the Manatee County summer &mdash; mid-90s heat, blazing sun, then an afternoon downpour &mdash; fresh concrete can flash off its surface moisture far too fast, leaving a weak, crazed, dusty top layer. We schedule pours around the rain, place early in the day when we can, and apply a curing compound or wet-cure to hold moisture in while the slab gains strength. Crazing (a fine map of shallow surface cracks) is almost always a curing-and-finishing issue, not a structural one &mdash; but it is avoidable.</p>

<h2>What our 42-point standard gates before the pour</h2>
<p>Most cracking failures are decided before any concrete is mixed. That is why our install standard gates the invisible work: the subgrade compaction, the slab thickness, the reinforcement placement, and the joint layout all get checked and photographed before a truck is called. When a homeowner&rsquo;s budget pushes toward thinning the slab or skipping base work, we would rather walk through options than cut the step that keeps the slab flat &mdash; because we are the ones who get the call two summers later.</p>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
Florida concrete cracks because of what happens underneath and at the edges, not because of the concrete. Compact the base, cut the joints at the right spacing and depth, pour to the right thickness for the load, slope it to drain, and cure it properly &mdash; and a Manatee County driveway or slab stays flat and tight for decades. Skip any one of those, and you are looking at a grid-cracked surface by its second summer. The prep that prevents the crack is the prep nobody sees.
</div>
'''
    related = [
        ("/concrete-driveways/bradenton/", "Concrete Driveways in Bradenton · Service Page"),
        ("/concrete-resurfacing/", "Concrete Resurfacing &amp; Repair · Service Page"),
        ("/blog/pavers-vs-concrete-driveway-florida/", "Pavers vs. Concrete Driveway in Florida"),
    ]
    faqs = [
        ("Is a hairline crack in my new driveway a problem?",
         "Usually not. A fine hairline crack that runs inside a control joint is normal shrinkage relieving itself exactly where it was designed to &mdash; that is the joint doing its job. What is a problem is a crack that runs across the field outside the joints, one that has a vertical lip you can feel with your foot (indicating settlement), or a widening crack that grows season to season. If you are unsure, we will look at it during a free visit and tell you honestly whether it is cosmetic or structural."),
        ("Can a cracked driveway be repaired, or does it need replacing?",
         "It depends on what is failing. Isolated surface cracks, scaling, or staining on an otherwise sound, well-draining slab can often be repaired, resurfaced, and sealed for far less than replacement. But once a driveway has heaved at the joints, cracked in a grid, or settled into puddling low spots, the problem is in the base &mdash; and patching the surface just buys you a year. We read the crack pattern and check for movement at the joints to tell you which camp you are in."),
        ("Why did my driveway crack when my neighbor's didn't?",
         "Almost always a difference in what happened before the pour. Two slabs of identical concrete will behave completely differently if one sits on a properly compacted base with correct joints and the other was poured fast on loose fill with joints spaced too far apart. Soil conditions can also vary lot to lot. The concrete you see is rarely the variable &mdash; the prep underneath it is."),
        ("Does fiber reinforcement stop cracks?",
         "It helps control them, but it is not a magic fix. Synthetic fiber distributed through the mix reduces shrinkage cracking and adds toughness, which is why we use it as standard. But fiber does not replace proper base compaction, correct joint spacing, or adequate slab thickness &mdash; it works alongside them. A fiber-reinforced slab on a bad base will still crack. Reinforcement is one layer of a system, not a substitute for the prep."),
    ]
    post_shell(post, lede, sections, faqs=faqs, related_links=related,
               cta_headline="Cracked driveway or planning a new pour? Get a free assessment.")


def _post_pool_deck_guide(post):
    lede = (
        "On a Sarasota pool deck in July, the surface underfoot is not a detail &mdash; "
        "it is the whole experience. The wrong material is a barefoot branding iron at "
        "two in the afternoon; the right one stays walkable in full sun. Here is the "
        "honest comparison of the coolest, safest pool-deck surfaces for Florida heat, "
        "with slip, temperature, and cost weighed for Suncoast homes."
    )
    sections = '''
<h2>What actually makes a pool deck cool</h2>
<p>Three things drive how hot a deck gets underfoot: color, density, and texture. Light colors reflect sunlight instead of absorbing it. Less-dense, more-porous materials hold less heat and shed it faster. And textured surfaces put less material in direct contact with your foot at once. The hottest possible deck is a dark, dense, smooth slab in full sun; the coolest is a light, porous, textured surface. Every option below sits somewhere on that spectrum.</p>

<blockquote>The same lighter, textured finishes that stay cool underfoot also tend to grip better when wet. Cool and slip-safe usually pull in the same direction &mdash; which is convenient, because both are non-negotiable around a pool.</blockquote>

<h2>The contenders, coolest to warmest</h2>

<h3>Travertine pavers — the cool-deck favorite</h3>
<p>Natural travertine is the gold standard for Suncoast pool decks, and for good reason: it is naturally light-colored and porous, so it stays remarkably cool even in direct afternoon sun, and its surface grips well when wet. It is a premium look that reads high-end the moment you step onto it. The trade-offs are cost and care &mdash; it is one of the pricier options and, being a natural stone, it wants periodic sealing to resist staining from sunscreen, leaves, and pool chemistry.</p>

<h3>Concrete &amp; porcelain pavers — cool, controllable, modular</h3>
<p>Light-colored concrete or porcelain pavers run cool when you choose a pale tone, give you the modular repair advantage of any paver field, and come in a huge range of looks including shellstone and marble-look finishes. They sit just below travertine on coolness and just below it on price, and they are extremely durable around salt and chlorine.</p>

<h3>Cool-deck acrylic resurfacing — the heat specialist</h3>
<p>A sprayed, knock-down acrylic &ldquo;cool deck&rdquo; finish is engineered specifically to reflect heat and stay barefoot-friendly. Its superpower is renewal: if you have a sound but dated or hot existing deck, an acrylic cool-deck finish gives it a new slip-rated, heat-reflective surface for far less than a tear-out. It is the classic Florida answer to the midday-sun problem and one of the most cost-effective routes to a cooler deck.</p>

<h3>Stamped concrete — design-forward, manage the color</h3>
<p>Textured stamped concrete delivers a high-end stone or shell look as one continuous, joint-free, weed-free surface, and the texture grips well when wet. Heat is the variable to manage: choose a lighter integral color and you have a comfortable deck; go dark for drama and you will want shade from the cage or a pergola to keep it walkable. Stamped is the value pick when you want a custom look without paver labor.</p>

<table class="post-table">
<thead><tr><th>Surface</th><th>Coolness</th><th>Slip (wet)</th><th>Installed Cost / Sq Ft</th></tr></thead>
<tbody>
<tr><td>Travertine pavers</td><td>Coolest</td><td>Excellent</td><td><strong>$18&ndash;$30</strong></td></tr>
<tr><td>Light concrete / porcelain pavers</td><td>Very cool</td><td>Very good</td><td><strong>$15&ndash;$26</strong></td></tr>
<tr><td>Cool-deck acrylic resurface</td><td>Very cool</td><td>Very good</td><td><strong>$5&ndash;$9</strong></td></tr>
<tr><td>Stamped concrete (light color)</td><td>Cool&ndash;moderate</td><td>Good</td><td><strong>$15&ndash;$24</strong></td></tr>
<tr><td>Stamped concrete (dark color)</td><td>Warm &mdash; needs shade</td><td>Good</td><td><strong>$15&ndash;$24</strong></td></tr>
</tbody>
</table>

<h2>Slip resistance: the safety floor</h2>
<p>Around water, a smooth troweled surface is a genuine hazard &mdash; we never finish a pool deck that way. Every deck we build or resurface gets a slip-rated texture: the natural texture of travertine, the surface of a textured paver, a broom or stamped finish on concrete, or the knock-down texture of an acrylic cool-deck. If you have small kids or older family members, weight this as heavily as coolness.</p>

<h2>Salt, chlorine, and drainage — the Florida tax</h2>
<p>A pool deck takes constant chlorine, salt-system runoff, and splash-out that would etch and spall unprotected concrete over time. Decorative concrete decks get a UV-stable, slip-rated, chlorine-resistant sealer, and natural-stone pavers get sealed too &mdash; plan to refresh that roughly every two to three years in our climate. Just as important, the deck has to slope decisively away from the coping and the screen-cage track so chemical-laden water drains off instead of pooling against footers and staining the surface.</p>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
For the coolest barefoot deck regardless of budget, travertine or light-colored porcelain/concrete pavers win. For the best value upgrade on a sound existing deck, an acrylic cool-deck resurface delivers a cool, slip-rated surface at a fraction of replacement cost. For a custom look without paver pricing, stamped concrete works beautifully &mdash; just keep the color light or plan for shade. Whatever you choose, slope it to drain and seal it for pool chemistry, and your Suncoast deck stays cool, safe, and good-looking for years.
</div>
'''
    related = [
        ("/pool-deck-pavers/sarasota/", "Pool Deck Pavers in Sarasota · Service Page"),
        ("/concrete-pool-decks/sarasota/", "Concrete Pool Decks in Sarasota · Service Page"),
        ("/blog/paver-sealing-resanding-florida-guide/", "Paver Sealing &amp; Re-Sanding in Florida"),
    ]
    faqs = [
        ("What is the coolest pool deck surface for Florida sun?",
         "Natural travertine is generally the coolest, because it is naturally light-colored and porous, so it reflects sun and sheds heat rather than storing it. Light-colored porcelain and concrete pavers are nearly as cool and offer more color and pattern options. If you are working with a sound existing deck, an acrylic cool-deck resurface is engineered specifically to stay barefoot-friendly and is the most cost-effective way to fix a hot deck without a tear-out."),
        ("Can you resurface my hot, dated pool deck instead of replacing it?",
         "Usually yes, and it is one of the most common pool-deck jobs we do. If the slab underneath is structurally sound, a cool-deck acrylic finish or a stamped overlay gives a stained, dated, or hot deck a brand-new slip-rated, heat-reflective surface for far less than a tear-out. The prerequisite is prep &mdash; we repair cracks and patch spalled areas first, because a resurface over unaddressed damage just telegraphs the same problems back through. If the slab has heaved or settled from a base failure, we will tell you replacement is the right call."),
        ("Are travertine pool decks slippery when wet?",
         "Travertine is actually one of the better natural surfaces for wet slip resistance &mdash; its naturally textured, slightly porous surface gives good grip even with water and splash-out on it. That combination of staying cool and gripping when wet is exactly why it is so popular around Suncoast pools. Sealing it correctly preserves that texture while protecting against staining; we use a sealer that does not turn the surface glassy."),
        ("How do salt-system pools affect the deck material?",
         "Salt-system runoff and splash-out are corrosive to unprotected concrete and to some metals over time, which is why deck choice and sealing matter near saltwater pools. Pavers and properly sealed decorative concrete both stand up well; we use chlorine- and salt-resistant sealers and make sure the deck slopes to drain that water away rather than letting it sit. On the keys and other coastal spots we treat salt exposure as a given and spec accordingly."),
    ]
    post_shell(post, lede, sections, faqs=faqs, related_links=related,
               cta_headline="Planning a cooler pool deck? Get a free on-site estimate.")


def _post_stamped_ideas(post):
    lede = (
        "Stamped concrete can look like brick, slate, flagstone, or wood plank at a "
        "fraction of paver labor &mdash; but in Lakewood Ranch, the prettiest patio in the "
        "world still has to clear architectural review first. Here are stamped patio "
        "ideas that read genuinely high-end <em>and</em> pass ARC in East Manatee&rsquo;s "
        "master-planned communities, from someone who submits the packages."
    )
    sections = '''
<h2>Why stamped concrete is the smart patio play here</h2>
<p>Stamped concrete presses a pattern and texture into a fresh slab, then takes integral or broadcast color and a release agent to produce convincing brick, stone, slate, wood-plank, or flagstone looks. Because it is one continuous slab, there are no joints for weeds or ants to colonize and nothing to settle unevenly like an individual paver can. For a clean, low-maintenance, design-forward patio at a friendlier labor cost than pavers, it is hard to beat &mdash; which is exactly why it is everywhere in Lakewood Ranch backyards.</p>

<h2>The ARC reality in Lakewood Ranch</h2>
<p>Almost every Lakewood Ranch village &mdash; Country Club East, The Lake Club, Esplanade, Polo Run, Indigo, Mallory Park, Lorraine Lakes, Azario, Star Farms and the rest &mdash; runs an architectural review committee. For a patio, the ARC typically cares about color (it should harmonize with your home and roof), finish, location, drainage, and sometimes pattern and border details. The good news: stamped concrete in a tasteful, home-matched palette is approved all the time. The work is in submitting it correctly &mdash; with a color sample, the pattern, and a site plan &mdash; rather than pouring first and asking later.</p>

<blockquote>The patios that get flagged are rarely flagged for being stamped concrete. They get flagged for a color that fights the house, a finish that reads too busy, or work started before the package cleared. All three are avoidable.</blockquote>

<h2>Patterns that read high-end and clear review</h2>

<h3>1. Large-format ashlar slate</h3>
<p>An ashlar slate pattern &mdash; irregular rectangular stones &mdash; in a soft greige or sandstone tone is one of the most reliably ARC-friendly looks in the Ranch. It reads as natural stone, harmonizes with the neutral palettes most communities favor, and the subtle texture stays comfortable underfoot.</p>

<h3>2. Seamless stone / textured skin</h3>
<p>A seamless textured stamp gives an organic, quarried-stone surface with no repeating grid &mdash; understated and modern. In a single light integral color it is about as inoffensive to a review committee as a decorative finish gets, while still looking custom.</p>

<h3>3. Wood-plank stamp</h3>
<p>A wood-plank stamp delivers the warm, on-trend look of a wood deck with none of the rot, splinters, or maintenance &mdash; a real advantage in our humidity. In a muted driftwood or weathered-oak tone it pairs beautifully with transitional and coastal home styles common in newer Ranch villages.</p>

<h3>4. Brick-bordered broom field</h3>
<p>A practical, budget-friendly approach the ARC tends to like: a simple light broom-finish field framed by a stamped brick or stone border band. The border gives it a finished, intentional edge that ties to the home, while the broom field keeps cost down and stays cool and grippy. This banded approach also reads as a deliberate design choice, which reviewers respond well to.</p>

<table class="post-table">
<thead><tr><th>Look</th><th>Best Paired With</th><th>ARC-Friendliness</th></tr></thead>
<tbody>
<tr><td>Ashlar slate, greige/sandstone</td><td>Most home styles, neutral palettes</td><td>Very high</td></tr>
<tr><td>Seamless textured stone</td><td>Modern / transitional homes</td><td>Very high</td></tr>
<tr><td>Wood-plank, driftwood tones</td><td>Coastal / transitional homes</td><td>High</td></tr>
<tr><td>Broom field + stamped border</td><td>Budget-conscious, any style</td><td>Very high</td></tr>
<tr><td>Bold multi-tone Roman slate</td><td>Statement patios w/ shade</td><td>Submit carefully</td></tr>
</tbody>
</table>

<h2>Color: the single biggest approval factor</h2>
<p>If there is one lever that decides ARC approval and long-term satisfaction, it is color. Pull tones from your home&rsquo;s body, trim, and roof rather than chasing a magazine photo. Lighter integral colors not only harmonize better with the neutral palettes most Ranch communities expect &mdash; they also stay noticeably cooler underfoot in full sun, which matters for a patio you actually want to use ten months a year. We mock up the color on a sample board, hold it against your home, and put it in the submittal so the reviewer sees exactly what will be poured.</p>

<h2>How we handle the submittal</h2>
<p>For Lakewood Ranch projects we build to what passes and document the spec: the pattern, the color sample, a site plan showing location and drainage, and the finish. We can assemble and submit the ARC package so your patio clears review the first time, rather than risking a stop-work or a redo after the fact. We do not handle structural or drainage engineering that some submittals require &mdash; flatwork, finish, color matching, and the design package are our lane.</p>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
Stamped concrete is the value-smart way to get a high-end patio look in Lakewood Ranch &mdash; and it clears ARC routinely when you keep the color harmonized with your home, choose a tasteful natural-stone or wood-plank pattern, and submit the package properly before pouring. Ashlar slate, seamless stone, wood plank, and a broom field with a stamped border are the most reliably approved looks. Get the color right and the rest tends to follow.
</div>
'''
    related = [
        ("/stamped-concrete/lakewood-ranch/", "Stamped Concrete in Lakewood Ranch · Service Page"),
        ("/concrete-patios/lakewood-ranch/", "Concrete Patios in Lakewood Ranch · Service Page"),
        ("/blog/pavers-vs-concrete-driveway-florida/", "Pavers vs. Concrete in Florida"),
    ]
    faqs = [
        ("Will a stamped concrete patio pass HOA architectural review in Lakewood Ranch?",
         "Routinely, yes &mdash; provided the color and finish harmonize with your home and the package is submitted correctly. Most Lakewood Ranch villages run an ARC that cares about color, finish, location, and drainage more than the fact that the surface is stamped concrete. We build to the approved spec, mock up the color on a sample, and can assemble the submittal so it clears review the first time rather than risking a stop-work after the pour."),
        ("Does stamped concrete look fake or cheap?",
         "Not when it is done with the right pattern, a home-matched color, and a quality release and seal. The looks that read fake are usually a poorly chosen high-contrast color, a too-repetitive pattern, or a worn-out unsealed surface. A tasteful ashlar slate or seamless stone in a natural tone, properly sealed, genuinely reads as stone to most people standing on it &mdash; at a fraction of natural-stone or paver labor."),
        ("How long does a stamped concrete patio last in Florida?",
         "The concrete itself lasts decades when it is poured on a proper base with correct joints, like any quality slab. The decorative color and finish are the maintenance item: plan to re-seal a stamped patio with a UV-stable sealer every few years in our sun to keep the color rich and protected. Re-sealing is straightforward and far cheaper than any structural concern, and it is what keeps a stamped patio looking new well past the ten-year mark."),
        ("Is stamped concrete hot to walk on?",
         "It can be if you choose a dark color in full sun &mdash; the same physics as any dense surface. The fix is at the design stage: choose a lighter integral color, which reflects more sun and stays cooler underfoot, and pair a deeper accent color with shade from a cage, pergola, or roofline if you want drama. We talk through where the afternoon sun lands on your specific patio during the estimate so the color fits how you will actually use the space."),
    ]
    post_shell(post, lede, sections, faqs=faqs, related_links=related,
               cta_headline="Designing a stamped patio? Get a free estimate and ARC-ready spec.")


def _post_sealing_guide(post):
    lede = (
        "Pavers are sold as low-maintenance, and they nearly are &mdash; but in Florida, "
        "&lsquo;low&rsquo; is not &lsquo;none.&rsquo; Joint sand washes out, weeds and ants move in, "
        "and the color fades under the Suncoast sun. Sealing and re-sanding on the "
        "right schedule is what keeps a paver driveway or pool deck tight, bright, and "
        "weed-free. Here is the straight answer on when, why, and what it costs."
    )
    sections = '''
<h2>Why paver joints fail in Florida specifically</h2>
<p>A paver surface is held together not by the pavers but by the sand packed between them. That joint sand locks the field, distributes load, and keeps weeds and ants out. In Florida, three forces work against it: heavy rain and irrigation that wash loose sand out of the joints, pressure-washing that blasts it out even faster, and the freeze-thaw-free but moisture-heavy climate that lets weeds and ants exploit any gap. Once the joints empty, pavers can shift, edges can lift, and the whole field loosens &mdash; which is why re-sanding is the core maintenance task, not sealing alone.</p>

<h2>Polymeric sand: the upgrade that matters</h2>
<p>Ordinary joint sand washes out and hosts weeds. Polymeric sand contains binders that, once swept in and activated with a light misting of water, harden into a firm, flexible joint that resists wash-out, locks the pavers, and dramatically reduces weeds and ants. When we re-sand a Florida paver surface, we use polymeric sand &mdash; it is the difference between re-sanding every year and re-sanding every several years.</p>

<blockquote>Sealing protects the surface and the color. Re-sanding protects the structure. They are two different jobs that are usually done together &mdash; but if you only do one, re-sanding is the one that keeps your pavers from shifting.</blockquote>

<h2>What sealing actually does</h2>
<p>A quality paver sealer does several things at once: it locks and stabilizes the joint sand, repels oil, rust, leaf tannin, and pool-chemical stains, enriches and protects the color against UV fade, and makes the surface easier to clean. On a Suncoast driveway or pool deck taking full sun and constant use, an unsealed paver field fades and stains noticeably faster than a sealed one. You can choose a natural &ldquo;matte&rdquo; finish that looks like nothing was applied, or a &ldquo;wet-look&rdquo; sealer that deepens the color &mdash; both protect; it is an aesthetic choice.</p>

<h2>How often, in our climate</h2>
<p>The honest answer is that it depends on sun exposure, traffic, and pressure-washing habits, but as a Suncoast rule of thumb:</p>

<table class="post-table">
<thead><tr><th>Task</th><th>Typical Florida Interval</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Re-seal pavers</td><td>Every 2&ndash;4 years</td><td>UV and traffic wear the sealer down</td></tr>
<tr><td>Re-sand joints (top-up)</td><td>As joints show wash-out</td><td>Rain &amp; pressure-washing empty joints</td></tr>
<tr><td>Full polymeric re-sand</td><td>Every 4&ndash;6 years (or as needed)</td><td>Restores a tight, weed-resistant field</td></tr>
<tr><td>Pool-deck sealer refresh</td><td>Every 2&ndash;3 years</td><td>Chlorine, salt, and splash-out are harsh</td></tr>
</tbody>
</table>

<p>Pool decks sit at the short end of every interval because salt-system runoff, chlorine, and constant splash-out are tougher on sealer than a driveway&rsquo;s exposure. Heavily shaded surfaces under oaks may need more frequent attention for organic staining; full-sun surfaces need it for fade.</p>

<h2>What it costs on the Suncoast</h2>
<p>Sealing and re-sanding are typically priced per square foot and usually done together for the best result. As a 2026 Suncoast guide, a clean-and-seal with a polymeric re-sand commonly runs in the range of <strong>$1.50&ndash;$3.50 per square foot</strong>, depending on the surface size, how much sand the joints need, the condition going in, and whether you choose a natural or wet-look sealer. A typical paver driveway or pool deck therefore lands in the few-hundred to low-four-figure range &mdash; far less than the cost of letting joints wash out until pavers shift and need lifting and relaying.</p>

<h2>The right order of operations</h2>
<p>Done properly, a re-seal-and-re-sand is a sequence, not a single spray. We pressure-wash the surface to strip dirt, old failing sealer, and organic growth; let it fully dry; sweep fresh polymeric sand into the joints and compact it in; activate the sand; then apply the sealer at the correct cure window in even coats. Skipping the wash, sanding into wet joints, or sealing over dirty pavers are the shortcuts that make a sealing job fail early &mdash; and they are exactly why a DIY or low-bid seal often does not last.</p>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
In Florida, plan to re-seal pavers every 2&ndash;4 years and do a full polymeric re-sand every 4&ndash;6 years &mdash; sooner on pool decks, where chlorine and salt are harsh. Re-sanding protects the structure; sealing protects the color and stain-resistance; do them together for roughly $1.50&ndash;$3.50 per square foot on the Suncoast. It is modest, predictable maintenance that keeps a paver surface tight, bright, and weed-free &mdash; and prevents the far costlier problem of shifted pavers down the road.
</div>
'''
    related = [
        ("/paver-sealing/bradenton/", "Paver Sealing in Bradenton · Service Page"),
        ("/paver-driveways/", "Paver Driveways · Service Page"),
        ("/blog/best-pool-deck-surface-florida-heat/", "Coolest Pool Deck Surfaces for Florida Heat"),
    ]
    faqs = [
        ("How often do pavers need to be sealed in Florida?",
         "As a Suncoast rule of thumb, re-seal a paver driveway or patio every 2 to 4 years and a paver pool deck every 2 to 3 years, because chlorine, salt, and splash-out are harder on the sealer. The exact interval depends on sun exposure, traffic, and how often you pressure-wash &mdash; full-sun surfaces fade faster, shaded surfaces collect more organic staining. When the color looks dull or water stops beading on the surface, it is time."),
        ("What is the difference between sealing and re-sanding pavers?",
         "They are two different jobs usually done together. Re-sanding refills the joints between the pavers &mdash; ideally with polymeric sand &mdash; which locks the field, prevents shifting, and resists weeds and ants. Sealing applies a protective coat over the whole surface that stabilizes the sand, repels stains, and protects the color from UV fade. Re-sanding protects the structure; sealing protects the look. If you only do one, re-sanding is what keeps the pavers from moving."),
        ("Why do weeds keep growing between my pavers?",
         "Almost always because the joint sand has washed out, leaving gaps where windblown seeds settle and germinate. Florida rain, irrigation, and pressure-washing empty ordinary joint sand over time. The durable fix is a full polymeric re-sand &mdash; the binders harden the joint into a firm surface that dramatically reduces weed and ant intrusion &mdash; followed by a sealer to lock it in. Spraying weeds treats the symptom; re-sanding fixes the cause."),
        ("Can I pressure-wash my own pavers between sealings?",
         "Yes, but gently and with awareness. A too-aggressive pressure-wash blasts the joint sand right out of the joints, which is the very thing you are trying to preserve, and can etch softer pavers. Use a moderate setting, keep the tip moving and not too close, and expect to top up joint sand afterward. If you are about to have the surface professionally sealed, we handle the wash as the first step of the job so it is done at the right pressure and the joints get re-sanded properly afterward."),
    ]
    post_shell(post, lede, sections, faqs=faqs, related_links=related,
               cta_headline="Pavers looking tired? Get a free seal &amp; re-sand estimate.")


_GENERAL_DISPATCH = {
    "pavers_vs_concrete": _post_pavers_vs_concrete,
    "cracking_guide": _post_cracking_guide,
    "pool_deck_guide": _post_pool_deck_guide,
    "stamped_ideas": _post_stamped_ideas,
    "sealing_guide": _post_sealing_guide,
}


def build_general_posts():
    for post in GENERAL_BLOG_POSTS:
        fn = _GENERAL_DISPATCH.get(post["topic"])
        if fn is None:
            raise KeyError(f"No body generator for general topic: {post['topic']!r}")
        fn(post)


# ============================================================================
# 72 COST POSTS — one per (priority service × city) combination
# ============================================================================
# Per-service "what it translates to" cost framing — concrete/paver specific,
# keeps each service's cost posts factually accurate and textually distinct.
COST_TYPICALS = {
    "concrete-driveways": {
        "quote": "for a typical 600 sq ft two-car driveway, a standard broom-finish pour runs <strong>$8&ndash;$12 per square foot installed</strong> &mdash; roughly <strong>$4,800&ndash;$7,200 all-in</strong> for the typical {city} job, with stamped and decorative finishes running higher",
        "take": "A typical 600 sq ft two-car concrete driveway in {city} runs $4,800&ndash;$7,200 all-in at the standard broom-finish tier. Stamped and decorative finishes run higher ($9,000&ndash;$14,400 on the same footprint); a tear-out-and-replace adds demo and haul to the number",
    },
    "paver-driveways": {
        "quote": "for a typical 600 sq ft two-car driveway, concrete or clay pavers run <strong>$14&ndash;$26 per square foot installed</strong> &mdash; roughly <strong>$8,400&ndash;$15,600 all-in</strong> for the typical {city} job depending on paver, base, and pattern",
        "take": "A typical 600 sq ft two-car paver driveway in {city} runs $8,400&ndash;$15,600 all-in, depending on the paver, the base work, and the pattern. Premium clay and intricate patterns run higher; tear-out of an old slab and extra base prep add to the number",
    },
    "concrete-patios": {
        "quote": "for a typical 300&ndash;400 sq ft patio, a broom-finish slab runs <strong>$7&ndash;$11 per square foot installed</strong> &mdash; roughly <strong>$2,100&ndash;$4,400 all-in</strong> for the typical {city} job, with stamped and stained finishes running higher",
        "take": "A typical 300&ndash;400 sq ft concrete patio in {city} runs $2,100&ndash;$4,400 all-in at the broom-finish tier. Stamped and acid-stained finishes run higher ($4,200&ndash;$8,800 on the same footprint); a decorative overlay of a sound existing slab can come in lower",
    },
    "concrete-pool-decks": {
        "quote": "for a typical 700&ndash;900 sq ft deck, a broom-finish or resurfaced pool deck runs <strong>$8&ndash;$12 per square foot installed</strong> for new work and <strong>$5&ndash;$9 per square foot</strong> for an acrylic cool-deck resurface &mdash; roughly <strong>$5,600&ndash;$10,800 all-in</strong> for a typical {city} new deck",
        "take": "A typical 700&ndash;900 sq ft concrete pool deck in {city} runs $5,600&ndash;$10,800 all-in for a new broom-finish pour, or far less for an acrylic cool-deck resurface of a sound existing slab ($3,500&ndash;$8,100). Textured stamped decks run higher",
    },
    "pool-deck-pavers": {
        "quote": "for a typical 700&ndash;900 sq ft deck, travertine and quality pavers run <strong>$15&ndash;$30 per square foot installed</strong> &mdash; roughly <strong>$10,500&ndash;$27,000 all-in</strong> for the typical {city} job depending on the stone, the base, and any demo of the old deck",
        "take": "A typical 700&ndash;900 sq ft paver pool deck in {city} runs $10,500&ndash;$27,000 all-in, depending on the paver or travertine selected, the base work, and demo of the existing deck. Light porcelain and concrete pavers anchor the lower end; premium travertine and shellstone run higher",
    },
    "stamped-concrete": {
        "quote": "stamped concrete runs <strong>$14&ndash;$24 per square foot installed</strong> on the Suncoast &mdash; so a typical 300&ndash;400 sq ft stamped patio lands around <strong>$4,200&ndash;$9,600 all-in</strong> for the typical {city} job, pattern, color, and release included",
        "take": "Stamped concrete in {city} runs $14&ndash;$24 per square foot installed, so a typical 300&ndash;400 sq ft stamped patio lands around $4,200&ndash;$9,600 all-in. A broom field with a stamped border band comes in lower; intricate multi-color stone patterns run higher",
    },
}
COST_TYPICALS_DEFAULT = COST_TYPICALS["concrete-patios"]


def build_cost_posts():
    for post in COST_BLOG_POSTS:
        svc = SERVICES[post["service_slug"]]
        city = CITIES[post["city_slug"]]
        kw = post["keyword"]
        city_name = city["name"]
        svc_name = svc["name"]
        svc_short = svc["short"]
        county = city["county"]
        nbhd = city["neighborhoods"]
        n0 = nbhd[0]
        n1 = nbhd[1] if len(nbhd) > 1 else n0
        n2 = nbhd[2] if len(nbhd) > 2 else n0
        zips = ", ".join(city.get("zips", [])[:4])
        _typ = COST_TYPICALS.get(post["service_slug"], COST_TYPICALS_DEFAULT)
        typ_quote = _typ["quote"].format(city=city_name)
        typ_take = _typ["take"].format(city=city_name)

        lede = (
            f"What does {kw} actually cost in {city_name}, FL in 2026? Here is the honest, "
            f"installer&rsquo;s pricing &mdash; by finish and material, with the {city_name}-specific "
            f"factors (soil, HOA / ARC rules, and the local market) that drive the numbers up "
            f"or down &mdash; from a concrete &amp; paver crew that works {county} every week."
        )

        sections = f'''
<h2>The honest cost ranges for {kw} in {city_name}</h2>

<p>{svc["intro_long_p1"]}</p>

<p><strong>What that translates to in {city_name} dollar terms:</strong> {typ_quote}. The table below has the full range by tier &mdash; budget options run lower, premium finishes run higher.</p>

<table class="post-table">
<thead><tr><th>{svc_short} Option</th><th>Installed Cost</th><th>Notes</th></tr></thead>
<tbody>
{''.join(f"<tr><td>{label}</td><td><strong>{price}</strong></td><td>{note}</td></tr>" for label, price, note in svc["pricing_rows"])}
</tbody>
</table>

<h2>Why pricing varies in {city_name} specifically</h2>

<p>{city["context_short"]} That market profile drives the local cost dynamics in three specific ways:</p>

<ul>
<li><strong>Soil and site prep.</strong> {city["humidity_note"]} For {kw} that means the base work is not optional &mdash; we excavate, cut out soft or organic soil, bring in compactable base, and compact it in lifts before anything is poured or laid. Where the subgrade is poor or fill is required, budget an extra $2&ndash;$5 per square foot of base prep. It is the step that prevents the crack or the settle, and it is the step low bidders skip.</li>

<li><strong>Demo and tie-ins.</strong> {city["primary_market"]}. Replacing an existing driveway, deck, or slab means demo and haul of the old surface, plus tie-ins to your apron, garage, coping, or cage &mdash; all of which add to a number that a bare new pour on open ground would not carry.</li>

<li><strong>Access and HOA / ARC logistics.</strong> Many of {city_name}&rsquo;s communities ({n0}, {n1}, {n2}) run an architectural review committee with rules on driveway materials, paver colors, finishes, and joint or border patterns. We build to what passes and can handle the ARC submittal, but the approved spec &mdash; and any weekday-only or quiet-hours access rules &mdash; affects the schedule and the quote.</li>
</ul>

<h2>What your money buys at each tier (in {city_name})</h2>

<h3>Entry tier ({svc["pricing_rows"][0][1]})</h3>
<p>{svc["pricing_rows"][0][2]}. This is the practical starting point for {city_name} homes &mdash; the workhorse surface that handles everyday Florida use. The quality is real; it is not a stripped-down product. As you move up the table, you are buying look, finish, and longevity, not fixing a deficient base &mdash; we never cut the prep to hit a price.</p>

<h3>Mid tier (the most-installed)</h3>
<p>Most {city_name} homeowners land in the middle of the table. This is where the decorative finishes, richer colors, and premium materials live, and where the value-per-dollar curve hits its sweet spot for a surface you will look at every day for fifteen-plus years.</p>

<h3>Premium tier</h3>
<p>For homeowners who want the best the category offers &mdash; premium materials, top-tier finishes, and the high-end look expected in the gated communities of {county}. Premium {svc_short.lower()} in {city_name} shows up most in neighborhoods like {n0} and {n1}, where the surface is part of the home&rsquo;s presentation.</p>

<h2>What the timeline looks like in {city_name}</h2>

<p>A typical {city_name} {svc_short.lower()} project runs like this:</p>

<ul>
<li><strong>Day 1 &mdash; layout &amp; prep:</strong> On-site measure confirmed, utilities and irrigation flagged, demo of any existing surface, excavation, and base brought in and compacted.</li>
<li><strong>Day 2 &mdash; form, steel &amp; pour (or set):</strong> Forms set to the right slope, reinforcement placed, then the pour, screed, and finish &mdash; or, for pavers, the screeded setting bed, the field laid to pattern, and edge restraints installed.</li>
<li><strong>Day 3+ &mdash; joints, cure, seal &amp; clean:</strong> Control joints cut, the slab cured (or pavers compacted and polymeric sand swept in), decorative work sealed, the site cleaned, drainage hose-tested, and a walkthrough with you.</li>
</ul>

<p>Concrete needs cure time before traffic &mdash; you can usually walk a slab the next day, but keep vehicles off a new driveway for about seven days. Stamped and stained work adds a day or two for coloring and sealing. Larger jobs scale roughly linearly. Our {city["humidity_note"][:1].lower()}{city["humidity_note"][1:]} so we schedule pours around the rain and protect fresh concrete &mdash; that timeline discipline is part of why the finish lasts.</p>

<h2>The {city_name} neighborhoods where we work most</h2>

<p>We pour and pave across {city_name}, but the highest concentration of {svc_short.lower()} work has been in:</p>

<ul>
{''.join(f"<li><strong>{n}</strong></li>" for n in nbhd[:6])}
</ul>

<p>Plus dozens of other neighborhoods and subdivisions across {county} (ZIPs {zips} and beyond). If your community is not on this list, we have almost certainly worked nearby &mdash; we just have not logged it as a top concentration for the year.</p>

<h2>What can change your {city_name} quote &mdash; up or down</h2>

<h3>Drives the price up</h3>
<ul>
<li>Poor subgrade that needs extra excavation, soft-soil removal, and fill &mdash; +$2&ndash;$5 per square foot.</li>
<li>Demo and haul of an existing driveway, deck, or slab &mdash; folded into the tear-out line on the table above.</li>
<li>Decorative upgrades &mdash; stamping, integral or broadcast color, exposed aggregate, or premium pavers and travertine.</li>
<li>Drainage corrections, thickened edges for heavy vehicles, or coping and cage tie-ins on pool decks.</li>
<li>Sealing on a schedule for decorative and paver work &mdash; protects your investment but is a real line item.</li>
</ul>

<h3>Drives the price down</h3>
<ul>
<li>A sound existing slab that can be resurfaced or overlaid instead of torn out &mdash; often a fraction of replacement cost.</li>
<li>Larger or combined projects (driveway plus walkway, or deck plus patio) that share mobilization and earn efficiency in scheduling.</li>
<li>Schedule flexibility during a slower stretch of the year.</li>
<li>A simple, clean footprint on open, well-draining ground with good truck access.</li>
</ul>

<div class="post-key-takeaway">
<strong>The Honest Answer for {city_name}, FL in 2026</strong>
{typ_take}. Most {city_name} homeowners we work with land in the mid range and stay there for fifteen-plus years &mdash; because the surface was built on a properly prepped base, jointed or restrained correctly, and sealed for the Florida sun.
</div>

<h2>How to get a {city_name} quote that&rsquo;s actually useful</h2>

<p>Three things make a {city_name} {kw} quote worth the paper:</p>

<ol>
<li><strong>An on-site measure.</strong> We measure the real footprint, check the soil and the drainage, and look at the tie-in points &mdash; not a guess off a photo.</li>
<li><strong>A line-itemized written quote.</strong> Excavation, base prep, forming, reinforcement, the pour or paver material, finish, sealing, demo, and cleanup &mdash; all itemized. A one-number quote is hiding something.</li>
<li><strong>An honest read on repair vs. replace.</strong> If your existing surface can be resurfaced or repaired for far less, we will tell you &mdash; we would rather earn the next job than oversell this one.</li>
</ol>

<p>We send written, line-itemized quotes within 24 hours of the on-site measure &mdash; often same-day. <a href="/contact/#quote">Request a {city_name} {kw} estimate</a> or call <a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a>. We are based in east {BUSINESS["city"]} and work {city_name} every week, so the turnaround is fast and the crew is local.</p>
'''

        related = [
            (f"/{post['service_slug']}/{post['city_slug']}/", f"{svc_short} in {city_name} · Service Page"),
            (f"/{post['city_slug']}/", f"All Concrete &amp; Paver Services in {city_name}, FL"),
        ]
        other_in_city = [p for p in COST_BLOG_POSTS
                         if p["city_slug"] == post["city_slug"] and p["slug"] != post["slug"]]
        if other_in_city:
            related.append((f"/blog/{other_in_city[0]['slug']}/", other_in_city[0]["title"]))

        # 2 service FAQs + 2 city-specific FAQs
        faqs = list(svc["faqs"][:2]) + [
            (f"Do you do estimates specifically for {city_name}?",
             f"Yes &mdash; every {city_name} project gets an on-site measure, a soil and drainage check, "
             f"and a written, line-itemized quote within 24 hours, often same-day. We are based in east "
             f"{BUSINESS['city']} bordering Lakewood Ranch and work {city_name} every week, so the schedule "
             f"turnaround is fast and we already know the local soil and HOA / ARC requirements."),
            (f"Is {kw} in {city_name} affected by HOA or architectural review rules?",
             f"In many {city_name} communities, yes &mdash; neighborhoods such as {n0} and {n1} run an "
             f"architectural review committee that governs materials, colors, finishes, and sometimes "
             f"joint or border patterns. We build to the approved spec, match the palette, and can assemble "
             f"and submit the ARC package so your project clears review the first time. We are Fully Insured "
             f"and back every job with a written workmanship warranty."),
        ]
        post_shell(post, lede, sections, faqs=faqs, related_links=related,
                   cta_headline=f"Get a free, written {kw} estimate in {city_name}.")


# ============================================================================
# BLOG INDEX
# ============================================================================
def svc_count_label(city_slug):
    name = CITIES[city_slug]["name"]
    n = len([p for p in COST_BLOG_POSTS if p["city_slug"] == city_slug])
    return f"{name} pricing · {n} cost guides."


def build_blog_index():
    URL = f"{SITE}/blog/"
    TITLE = clip_title(f"Lakewood Ranch, Manatee &amp; Sarasota Concrete Journal · {BUSINESS['name']}")
    DESC = clip_desc(
        "Practical concrete &amp; paver guides for the Suncoast: pavers-vs-concrete, why "
        "Florida concrete cracks, the coolest pool-deck surfaces, HOA-approved stamped "
        "patio ideas, paver sealing, and cost-by-city pricing. Written by installers."
    )

    schemas = [
        schema_breadcrumb([("Home", SITE + "/"), ("Journal", URL)]),
        schema_webpage(URL, TITLE, DESC),
        schema_local_business(URL, f"{BUSINESS['name']} Journal"),
    ]
    bc = breadcrumbs([("Home", "/"), ("Journal", None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">The {BUSINESS["name"]} Journal · Updated Monthly</span>
    <h1>Field notes from <em>the form boards</em>.</h1>
    <p class="page-hero-sub">Practical guides for Lakewood Ranch, Manatee &amp; Sarasota homeowners &mdash; written by the crew that pours and paves the Suncoast, not by SEO writers. Cost data, the pavers-vs-concrete math, the honest crack-prevention answers. {len(GENERAL_BLOG_POSTS) + len(COST_BLOG_POSTS)} articles and counting.</p>
  </div>
</section>'''

    intro = f'''<section>
  <div class="container">
    <article class="page-article">
      <p class="post-lede">Most concrete and paver &ldquo;advice&rdquo; online is written by people who have never set a form, compacted a base, or cut a control joint in Florida sand. This journal is the opposite. Every guide here comes out of jobs we actually run across {len(CITIES)} Suncoast cities &mdash; the cracked driveways and settled pavers we are called to fix as much as the new pours and decks we install.</p>

      <p>If you are planning a driveway, patio, or pool deck for a Lakewood Ranch, Manatee, or Sarasota home, a few questions decide almost everything: <strong>pavers or poured concrete</strong>, <strong>what it actually costs installed in your city</strong>, <strong>what makes Florida concrete crack</strong>, and <strong>which surfaces stay cool and safe in the sun</strong>. We have organized the journal around exactly those.</p>

      <h2>Start with the big decisions</h2>
      <p>The five featured guides below cover the choices that cost the most to get wrong &mdash; the pavers-versus-concrete question on nearly every driveway quote, why Gulf Coast concrete cracks and the prep that prevents it, the coolest pool-deck surfaces for Florida heat, stamped-patio ideas that clear HOA architectural review in Lakewood Ranch, and the straight answer on paver sealing and re-sanding. Read those first if you are early in the process.</p>

      <h2>Then price it for your city</h2>
      <p>Below the features sit {len(COST_BLOG_POSTS)} cost guides &mdash; our priority services across each of the {len(CITIES)} cities we serve. Pricing genuinely changes by city: a new-construction paver upgrade in a gated Lakewood Ranch village prices differently than a poured driveway on a 1960s lot in west Bradenton that needs base remediation first, and a coastal Sarasota pool deck carries salt-exposure and sealing work an inland Parrish job does not. The guides give you a real 2026 installed range by finish and material, not a national average that means nothing on the Suncoast.</p>

      <h2>Why trust an installer&rsquo;s numbers</h2>
      <p>Because we publish our pricing on every service page, run every job through the {BUSINESS["checklist_name"]}, slope and cure and seal for the Florida climate, and back the work with a written workmanship warranty &mdash; and we are Fully Insured. The same standard runs through everything we write here. If a guide tells you a surface or a finish is the wrong call for your home, it is because we have seen that exact thing fail in that exact condition &mdash; not because it is the cheaper recommendation.</p>
    </article>
  </div>
</section>'''

    # FEATURED: 5 general posts
    featured_html = ""
    for p in GENERAL_BLOG_POSTS:
        featured_html += f'''<a href="/blog/{p["slug"]}/" class="blog-card">
  <div class="blog-card-meta">
    <span>● {p["category"]}</span>
    <span>{p["date_published"][:7]}</span>
  </div>
  <h3>{p["title"]}</h3>
  <span class="blog-card-cta">Read Field Notes</span>
</a>'''

    featured = f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">Featured Reading</span>
        <h2>Five long-form guides, <em>read-them-first</em>.</h2>
        <div class="section-head-text"><p>The handful of guides that cover the biggest decisions Suncoast concrete and paver buyers face. Start here.</p></div>
      </div>
    </div>
    <div class="blog-grid">{featured_html}</div>
  </div>
</section>'''

    # COST POSTS BY CITY
    by_city_html = ""
    for cslug, c in CITIES.items():
        city_posts = [p for p in COST_BLOG_POSTS if p["city_slug"] == cslug]
        items = "".join(f'<li><a href="/blog/{p["slug"]}/">{p["title"]}</a></li>' for p in city_posts)
        by_city_html += f'''<div class="related-box" style="margin:0">
  <div class="related-box-label">Cost Guides · {c["name"]}, FL</div>
  <h3>{svc_count_label(cslug)}</h3>
  <ul>{items}</ul>
</div>'''

    n_svc = len(set(p["service_slug"] for p in COST_BLOG_POSTS))
    cost_section = f'''<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">02</div>
      <div class="section-head-meta">
        <span class="mono-label">Cost Guides · {len(COST_BLOG_POSTS)} Articles · {n_svc} Services × {len(CITIES)} Cities</span>
        <h2>What it actually costs<em>, by city</em>.</h2>
        <div class="section-head-text"><p>One cost guide per priority service, per city &mdash; with real 2026 Suncoast pricing, the local soil and HOA / ARC factors, and what changes the number up or down.</p></div>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px">{by_city_html}</div>
  </div>
</section>'''

    body = "\n".join([hero, intro, featured, cost_section,
                      f'<div class="container">{contact_banner()}</div>', final_cta()])

    head_html = head(TITLE, DESC, URL, json_ld=schemas)
    write_page("blog/index.html", head_html, header(active="blog"), body, breadcrumbs_html=bc)
    print("Wrote /blog/index.html")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"Building {len(GENERAL_BLOG_POSTS)} general blog posts...")
    build_general_posts()
    print(f"  [ok] Built {len(GENERAL_BLOG_POSTS)} general posts")
    print(f"\nBuilding {len(COST_BLOG_POSTS)} cost posts...")
    build_cost_posts()
    print(f"  [ok] Built {len(COST_BLOG_POSTS)} cost posts")
    print("\nBuilding blog index...")
    build_blog_index()
    print(f"\nTotal blog pages: {len(ALL_POSTS) + 1}")
