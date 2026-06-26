#!/usr/bin/env python3
"""Generate /[service]/ hub pages + /[service]/[city]/ pages — Lakewood Ranch Concrete."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *

REGION = "Lakewood Ranch, Manatee &amp; Sarasota"
REGION_PLAIN = "Lakewood Ranch, Manatee & Sarasota"

# Real project photos mapped ONLY to services they honestly depict (no stock/AI).
SERVICE_PHOTOS = {
    "paver-driveways": [
        ("paver-driveway-tan-lakewood-ranch-fl.jpg", "Paver driveway"),
        ("paver-driveway-charcoal-border-bradenton-fl.jpg", "Paver driveway with charcoal border"),
        ("paver-driveway-cobble-parrish-fl.jpg", "Cobblestone paver driveway"),
        ("paver-walkway-driveway-lakewood-ranch-fl.jpg", "Paver driveway and walkway"),
        ("paver-driveway-brick-bradenton-fl.jpg", "Brick paver driveway"),
    ],
    "paver-patios-walkways": [
        ("spaced-paver-patio-gravel-joints-bradenton-fl.jpg", "Spaced paver patio with gravel joints"),
        ("paver-walkway-banded-lakewood-ranch-fl.jpg", "Banded paver walkway"),
        ("spaced-paver-patio-lakewood-ranch-fl.jpg", "Spaced paver patio"),
        ("paver-patio-gray-backyard-bradenton-fl.jpg", "Gray paver patio"),
    ],
    "pool-deck-pavers": [
        ("paver-pool-deck-patio-lakewood-ranch-fl.jpg", "Paver pool deck and patio"),
        ("travertine-patio-pergola-lakewood-ranch-fl.jpg", "Travertine patio under a pergola"),
    ],
}

def project_photos_html(service_slug, city_slug=None):
    photos = SERVICE_PHOTOS.get(service_slug)
    if not photos:
        return ""
    if city_slug:
        cname = CITIES.get(city_slug, {}).get("name", "")
        keys = list(CITIES.keys())
        idx = keys.index(city_slug) if city_slug in keys else 0
        fn, label = photos[idx % len(photos)]
        return f'''<section style="background:var(--paper)">
  <div class="container">
    <figure style="margin:0;border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow)">
      <img src="/images/projects/{fn}" alt="{label} by {BUSINESS['name']}, serving {cname}, FL" loading="lazy" style="width:100%;height:auto;display:block">
      <figcaption style="background:var(--dark);color:var(--white);font-size:.82rem;letter-spacing:.04em;padding:12px 18px">Recent work · {label} · serving {cname} &amp; {REGION_PLAIN}</figcaption>
    </figure>
  </div>
</section>'''
    items = "".join(
        f'''<figure class="gallery-item"><img src="/images/projects/{fn}" alt="{label} by {BUSINESS['name']} in {REGION_PLAIN}" loading="lazy"><figcaption class="gallery-caption">{label}</figcaption></figure>'''
        for fn, label in photos[:3]
    )
    return f'''<section style="background:var(--paper)">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">★</div>
      <div class="section-head-meta">
        <span class="mono-label">Our Work · Real Projects</span>
        <h2>Recent {SERVICES[service_slug]["short"].lower()} we&rsquo;ve <em>actually built</em>.</h2>
      </div>
    </div>
    <div class="gallery-grid">{items}</div>
  </div>
</section>'''


def lead_snippet(text, n=90):
    """Clip an intro_lead for use mid-sentence in a meta description without
    leaving a dangling em-dash or a doubled ellipsis."""
    s = clip_desc(text, n)
    s = s.rstrip("…").rstrip()
    if s.endswith("&mdash;"):
        s = s[:-len("&mdash;")].rstrip(" ,-")
    return s.rstrip(" ,;:-") + "."


def clip_title(s, n=65):
    """Trim a title to <= n chars at a word boundary, never mid-word."""
    s = " ".join(str(s).split())
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(" ,·-|&")


def local_business_no_rating(*args, **kwargs):
    """schema_local_business but with the invented aggregateRating stripped and
    flooring-era 'Tampa Bay' copy rewritten for this concrete brand. NEW
    business has no real reviews, so we never emit rating/review-count."""
    s = schema_local_business(*args, **kwargs)
    s.pop("aggregateRating", None)
    if isinstance(s.get("description"), str):
        s["description"] = (s["description"]
            .replace("services across Tampa Bay and Sarasota",
                     f"services across {REGION_PLAIN}")
            .replace("Flooring contractor", "Concrete & paver contractor")
            .replace("Tampa Bay", "the Suncoast"))
    return s


# ============================================================================
# 5 COMMON MISTAKES — one set per service (unique wording, used across cities)
# All concrete/paver — surrounding template copy only; per-service prose is in
# SERVICES[...] (already concrete-correct).
# ============================================================================
MISTAKES_BY_SERVICE = {
    "concrete-driveways": [
        ("Pouring on an un-compacted sandy base.",
         "Our Gulf Coast subgrade is sand and fill that swells and shrinks with the wet season. A driveway placed on a base that was never excavated to depth and mechanically compacted will settle unevenly and telegraph that movement straight up as cracks by its second summer. The slab is rarely the problem &mdash; the base under it is. We proofroll and compact in lifts before a single yard of concrete is ordered, because the prep that prevents the crack is the prep nobody sees."),
        ("Skipping &mdash; or mis-spacing &mdash; control joints.",
         "Concrete shrinks as it cures and moves with Florida heat. Without saw-cut control joints at roughly ten-foot spacing, that stress relieves itself wherever it wants &mdash; a random web across your apron. We have walked Lakewood Ranch driveways that cracked in a grid because nobody cut a relief joint. Proper joint layout tells the slab exactly where to crack: in a straight, intended line you barely notice."),
        ("Pouring the slab too thin for the load.",
         "Four inches of fiber-reinforced concrete over a compacted base handles standard cars and light trucks. Park an RV, a boat trailer, or a loaded work truck on that same slab and the edges spall and crack. The honest fix is to step the slab to five or six inches and adjust the base where the heavy load actually sits &mdash; which is why we ask about your heaviest vehicle at the estimate, not after the pour."),
        ("Ignoring HOA / ARC color and finish rules.",
         "Lakewood Ranch and the gated golf villages govern driveway color, finish, and even joint pattern through architectural review. A beautiful pour that does not match the approved submittal can get flagged after the fact &mdash; and a flagged driveway is an expensive thing to redo. We pull the approved palette, document the color and finish, and handle the ARC submittal so the install clears review the first time."),
        ("Buying the lowest bid and skipping the sealer.",
         "The lowest driveway bid almost always means thinned base work, wider joint spacing, and no penetrating sealer. In full Florida sun and summer rain, an unsealed slab stains, fades, and scales years sooner. A penetrating sealer is a small line item against the cost of a premature resurface. Pay for the base prep and the sealer up front; it is far cheaper than the redo."),
    ],
    "concrete-patios": [
        ("Pouring a dead-flat patio with no drainage.",
         "A patio with no deliberate slope becomes a standing-water complaint by the first storm season, and water pooling against the slab edge undermines the sandy subgrade beneath it. Every patio we pour falls away from the house and the pool cage at an engineered grade, then gets hose-tested before we sign off. Drainage is decided before the pour, not patched after."),
        ("Choosing a dark, dense surface for full sun.",
         "A dark, smooth slab in full Lakewood Ranch sun gets brutal underfoot &mdash; the kind of hot you can&rsquo;t cross barefoot in July. We steer homeowners toward lighter integral colors and textured finishes that stay walkable. The prettiest patio you never use because it cooks your feet is not a win."),
        ("Tying the patio rigidly to the house slab.",
         "The house slab and a new patio move independently. Pour them locked together with no expansion-joint isolation and the differential movement cracks one or both. We isolate every patio from the house and footers with a proper expansion joint so each slab can move without dragging the other along with it."),
        ("Stamping or staining without sealing it for UV.",
         "Stamped and stained concrete looks incredible the week it&rsquo;s poured &mdash; and fades, chalks, and wears blotchy fast if it&rsquo;s left unsealed under relentless Gulf Coast UV. Decorative work needs a UV-stable sealer and periodic reseals to hold its color. Skipping the seal isn&rsquo;t a saving; it&rsquo;s a countdown to a dull, patchy patio."),
        ("Building it too small to actually live on.",
         "The most common patio regret isn&rsquo;t the finish &mdash; it&rsquo;s the size. A slab sized to the budget instead of to a table, chairs, a grill, and walking room becomes the patio you outgrow in a season. We&rsquo;d rather lay out the real footprint once, with financing if needed, than pour a too-small slab you tear out in three years."),
    ],
    "concrete-pool-decks": [
        ("Letting water drain back toward the pool and cage.",
         "A pool deck has to shed water away from the coping and the screen cage, or rainwater and splash-out pool chemicals pool at the edge and attack both the slab and the cage footers. We pour pool decks to a deliberate slope away from the water and toward the deck drains, and hose-test it before handover. Get the drainage wrong and you fight algae, staining, and standing water for the life of the deck."),
        ("Picking a hot, slick surface around water.",
         "Bare gray concrete in Florida sun is too hot for bare feet and too slick when wet &mdash; the worst combination right where people walk dripping and barefoot. We finish pool decks with textured, lighter-colored, slip-resistant surfaces &mdash; broom, knock-down, or cool-deck textures &mdash; that stay cooler underfoot and grippier when splashed."),
        ("Pouring tight to the coping with no expansion joint.",
         "The pool shell, the deck, and the cage all move at different rates. A deck poured rigidly against the coping with no expansion joint cracks at the bond beam and can transfer stress into the pool structure itself. We isolate the deck from the coping and the cage with proper expansion joints so each element moves on its own."),
        ("Resurfacing over a deck with a base problem.",
         "A cool-deck or overlay over a slab that has already settled or cracked just buys a year &mdash; the underlying movement telegraphs straight back through the new surface. We read the deck before quoting: a sound slab is a great candidate for resurfacing, but a deck that has heaved or cracked at the joints needs the base addressed, not a pretty coat over the problem."),
        ("Skipping the sealer on a chlorinated, salt-air deck.",
         "Pool decks live in the harshest spot on the property &mdash; UV, chlorine or salt water, and constant wet-dry cycling. An unsealed decorative deck stains and scales years sooner. A UV- and chemical-stable sealer, reapplied on schedule, is what keeps the color and surface intact. It&rsquo;s a small line item against resurfacing the whole deck early."),
    ],
    "stamped-concrete": [
        ("Stamping without integral color and a release.",
         "Stamped concrete that&rsquo;s only surface-colored looks convincing the first year, then wears thin at the high-traffic lines and shows gray underneath. We build color in two layers &mdash; integral color through the slab plus a contrasting release in the texture &mdash; so even as the surface wears, the color goes all the way down and the pattern keeps its depth."),
        ("Choosing a pattern that fights the space.",
         "An oversized ashlar-slate stamp on a small entry, or a tight brick running-bond on a sweeping driveway, reads as obviously fake. The pattern and joint scale have to suit the size of the slab and the look of the home. We mock up the pattern, color, and grout line on your actual project so you see it at scale before we commit the whole pour."),
        ("Stamping over a slab that isn&rsquo;t poured for it.",
         "Stamped concrete is only as sound as the slab under it. Stamp a thin, under-jointed, poorly based pour and the texture just decorates a slab that&rsquo;s going to crack. We pour the slab to the same 42-point standard as any structural flatwork &mdash; compacted base, fiber reinforcement, engineered joints &mdash; then stamp. Pretty texture over bad prep is still bad prep."),
        ("Ignoring HOA / ARC review on the pattern and color.",
         "In Lakewood Ranch and the gated villages, the architectural committee often reviews decorative finishes &mdash; pattern, color, and border banding included. A stamped patio or driveway that doesn&rsquo;t match the approved palette can be flagged after it&rsquo;s cured. We document the pattern and color and handle the ARC submittal so the decorative work clears review the first time."),
        ("Never resealing it.",
         "Stamped concrete depends on its sealer for both color depth and protection. Under Gulf Coast UV and rain, that sealer wears, and a stamped surface left to go dull and chalky is the giveaway of a neglected job. A reseal every couple of years restores the wet-look depth and protects the color. Budget for it &mdash; it&rsquo;s a fraction of the original install and it&rsquo;s what keeps the finish looking new."),
    ],
    "concrete-slabs": [
        ("Skipping the base on a slab you&rsquo;ll build or park on.",
         "A shed slab, an RV or boat pad, an AC or generator pad, a paver-base slab &mdash; all of them carry concentrated load, and all of them fail the same way if the base is skipped. We excavate to depth, cut out soft or organic soil, bring in compactable base, and compact it in lifts before forming. The flatwork is only as good as what&rsquo;s under it."),
        ("Forgetting the vapor barrier under interior-adjacent slabs.",
         "A slab that abuts conditioned or enclosed space &mdash; a garage extension, a slab a structure will sit on &mdash; needs a vapor barrier under it, or Florida ground moisture wicks up through the concrete and into whatever sits on top. We install the barrier where the application calls for it; skipping it invites moisture, efflorescence, and damaged finishes down the line."),
        ("Under-reinforcing for the actual load.",
         "Fiber mesh is right for many flatwork slabs; a pad that&rsquo;ll carry a boat trailer, a shed, or equipment often needs rebar or wire on chairs, sized and placed to the load. We match the reinforcement to the use &mdash; and we chair the steel up off the base so it actually sits inside the slab, where it does its job, instead of lying uselessly at the bottom."),
        ("Pouring with no plan for where it&rsquo;ll crack.",
         "Every slab moves as it cures. Without engineered control joints, it cracks where it wants. We plan the joint layout to the slab&rsquo;s shape and use so the inevitable shrinkage relieves itself in a clean line &mdash; not a random web across a pad you just paid for."),
        ("Confirming the mix and PSI after the truck arrives.",
         "The right concrete mix and PSI depend on the application &mdash; a light walkway pad and a heavy equipment slab are not the same pour. We confirm the mix design and strength for the specific job before the order goes in, not on the fly when the truck is already on site. The wrong mix is a problem you can&rsquo;t fix after it&rsquo;s placed."),
    ],
    "concrete-resurfacing": [
        ("Resurfacing a slab that&rsquo;s failing at the base.",
         "An overlay is a surface solution. Bonded over a slab that has settled, heaved, or cracked from a base problem, it just telegraphs the same movement back through within a year. We read the slab honestly before quoting: surface wear, discoloration, and minor spalling are great resurfacing candidates; a slab with structural or base movement needs that addressed first, or the money&rsquo;s wasted."),
        ("Skipping proper surface prep before the overlay.",
         "An overlay only lasts if it bonds, and it only bonds to a clean, profiled, sound surface. Skip the pressure-wash, the grinding or etching, and the crack treatment, and the new coat delaminates and peels at the edges. We prep the substrate to the system&rsquo;s spec before any material goes down &mdash; the bond is the whole job."),
        ("Treating cracks by coating straight over them.",
         "A crack coated over without being chased out and treated comes straight back through the new surface &mdash; often within a season. We address moving and non-moving cracks appropriately before resurfacing, so the finished overlay reads as one clean surface instead of a map of the old damage."),
        ("Using the wrong overlay system for the exposure.",
         "A thin micro-topping made for a covered entry won&rsquo;t survive on a sun-and-rain pool deck or a vehicle-load driveway. The overlay system has to match the traffic, the UV, and the wet exposure. We spec the system to where it lives &mdash; spray-down texture, stampable overlay, or polymer-modified topping &mdash; not whatever&rsquo;s cheapest by the bucket."),
        ("Never sealing the finished surface.",
         "A resurfaced slab depends on its sealer to protect the new color and texture from UV, stains, and wear. Left unsealed, decorative resurfacing dulls and stains fast in the Florida climate. A proper seal at the right cure window &mdash; and reseals on schedule &mdash; is what makes the resurface last instead of looking tired in a year."),
    ],
    "paver-driveways": [
        ("Laying pavers on a base that was never compacted.",
         "Settled, dipping, rutted pavers almost always trace back to a base that was rushed. A paver driveway needs an excavated, properly compacted crushed-base and bedding layer &mdash; compacted in lifts &mdash; before a single paver is set. Skip that and the field settles into ruts where the tires track. The pavers don&rsquo;t fail; the base under them does."),
        ("Leaving out the edge restraints.",
         "Pavers are held in place at the perimeter by edge restraints. Without them, the outer rows creep and spread under vehicle load, the joints open, and the whole field starts to migrate. We install proper edge restraints to lock the paver field before joint sand ever goes in &mdash; it&rsquo;s the detail that keeps the driveway tight for decades."),
        ("Using regular sand instead of polymeric in the joints.",
         "Plain joint sand washes out in the first hard Florida rain, the joints empty, weeds and ants move in, and pavers start to rock. Polymeric joint sand is swept in, compacted, and activated so it locks the field and resists washout. It&rsquo;s the difference between a driveway that stays tight and one that needs constant re-sanding."),
        ("Skipping the soldier course and pattern layout.",
         "A paver driveway with no soldier-course border and a pattern that wanders looks unfinished and reads as a budget job. The border courses and a consistent, properly set pattern are what make a paver driveway look custom. We set the borders straight, plan the pattern to the space, and keep the field consistent edge to edge."),
        ("Ignoring HOA / ARC paver color and pattern rules.",
         "Most Lakewood Ranch villages review paver color, style, and pattern through architectural review. A driveway laid in a color the committee didn&rsquo;t approve can be flagged after install. We match the approved paver and pattern, document it, and handle the ARC submittal so the driveway clears review the first time."),
    ],
    "paver-patios-walkways": [
        ("Rushing the base on a patio or walkway.",
         "Sunken, wobbly, tripping-hazard pavers come from a skipped base. Even a walkway needs an excavated, compacted base and a screeded bedding layer before pavers are set. We compact in lifts and screed the bed flat so the finished surface is even and stays that way &mdash; not a patchwork of high and low pavers a season later."),
        ("Forgetting the slope away from the house.",
         "A paver patio still has to shed water away from the home and the lanai. Laid dead-flat or sloped the wrong way, it sends rainwater toward the foundation. We set the bedding and field to a deliberate fall away from the structure so water runs off where it should, not back against the house."),
        ("Leaving out edge restraints on the open sides.",
         "Patios and walkways spread at any unrestrained edge &mdash; the open sides creep, joints open, and the border pavers wander. We install edge restraints along every open edge to lock the field, so the clean lines you paid for stay clean."),
        ("Using plain sand that washes out of the joints.",
         "Joint sand that isn&rsquo;t polymeric washes out in Florida downpours, and then come the weeds, the ants, and the rocking pavers. We sweep in polymeric joint sand, compact it, and activate it so the joints stay locked and the surface stays solid and low-maintenance."),
        ("Treating the layout as an afterthought.",
         "A walkway that doesn&rsquo;t line up with the door, or a patio pattern that fights the shape of the space, reads as cheap no matter how good the pavers are. We plan the pattern, borders, and transitions to the home and the layout so the finished hardscape looks designed, not just installed."),
    ],
    "pool-deck-pavers": [
        ("Skipping the compacted base around the pool.",
         "A paver pool deck on a rushed base settles unevenly right where people walk barefoot and dripping &mdash; the worst place for a tripping lip. We excavate and compact a proper base and bedding layer in lifts before setting pavers, so the deck stays flat and even around the entire pool for the long haul."),
        ("Draining water back toward the pool and cage.",
         "A pool deck has to fall away from the coping and toward the deck drains, or splash-out and rain pool at the water&rsquo;s edge and attack the coping and cage footers. We set the paver field to a deliberate slope away from the pool and hose-test it before handover."),
        ("Choosing a paver that bakes in the sun.",
         "Some pavers hold heat and cook bare feet around a pool. Travertine and lighter-colored pavers stay markedly cooler underfoot &mdash; a real difference on a July afternoon. We steer pool-deck clients toward cooler, slip-resistant materials made for wet, barefoot traffic."),
        ("Leaving the joints with plain, washout-prone sand.",
         "Around a pool, joint sand faces constant splash-out and rain. Plain sand washes out fast, the joints empty, and pavers loosen. Polymeric joint sand &mdash; compacted and activated &mdash; holds the field together against all that water and keeps the deck tight and weed-free."),
        ("Setting pavers tight to the coping with no isolation.",
         "The pool shell, deck, and cage all move at different rates. Pavers crowded against the coping with no allowance for that movement loosen and lift at the bond beam. We detail the deck-to-coping transition properly so the field moves with the structure instead of fighting it."),
    ],
    "paver-sealing": [
        ("Sealing pavers before re-sanding the joints.",
         "Sealing over washed-out, half-empty joints locks in a weak, gappy surface and traps the problem under the finish. Joints get re-sanded with polymeric sand first &mdash; swept in, compacted, activated &mdash; and only then sealed. Seal-first is doing the steps in the wrong order, and it shows within a year."),
        ("Pressure-washing too aggressively before sealing.",
         "Too much pressure blasts the joint sand out, etches the paver faces, and can scar the surface &mdash; leaving more damage to seal over than you started with. We clean at the right pressure and technique for the paver type, lift the stains, and leave the surface sound and ready to re-sand and seal."),
        ("Using the wrong sealer &mdash; or putting it on too thick.",
         "The wrong sealer, or one laid on too heavy, hazes white, gets slick when wet, or peels in sheets under Florida UV. Pool-deck and driveway pavers each want the right product and finish &mdash; matte or wet-look &mdash; applied at the correct rate. We match the sealer to the surface and apply it evenly at the right coverage so it cures clear and grippy."),
        ("Sealing in the wrong weather or cure window.",
         "Seal pavers with rain coming, on a damp base, or in punishing midday heat and the sealer clouds, blisters, or won&rsquo;t cure. Florida&rsquo;s afternoon storms make timing everything. We schedule sealing around the weather and apply within the correct moisture and temperature window so it cures right the first time."),
        ("Treating sealing as one-and-done.",
         "Paver sealer wears under UV, traffic, and rain &mdash; it&rsquo;s a maintenance cycle, not a permanent coat. Driveways and pool decks need re-sanding and resealing every couple of years to keep the joints locked and the color rich. We&rsquo;ll tell you honestly when a surface is due, instead of pretending one seal lasts forever."),
    ],
}

# ============================================================================
# Pricing table builder
# ============================================================================
def pricing_table_html(svc, city_name=None):
    rows = ""
    for label, price, note in svc["pricing_rows"]:
        rows += f'<tr><td>{label}</td><td>{note}</td><td class="price">{price}</td></tr>'
    city_note = f" for {city_name} homes" if city_name else ""
    head_h3 = f'2026 {svc["name"]} pricing<em>{city_note}</em>.'
    return f'''<section class="pricing-section">
  <div class="container">
    <div class="pricing-wrap">
      <header class="pricing-head-bar">
        <h3>{head_h3}</h3>
        <span class="pricing-head-meta">Updated for 2026 · {REGION} rates</span>
      </header>
      <table class="pricing-table">
        <thead><tr><th>Option</th><th>What it&rsquo;s best for</th><th>Installed cost</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <div class="pricing-note">Prices include labor, base prep, and standard finishing. Old-surface demo &amp; haul-away quoted per job. Financing available on larger projects. <a href="/contact/#quote">Free written estimate within 24 hrs →</a></div>
    </div>
  </div>
</section>'''

# ============================================================================
# Scope items list
# ============================================================================
def scope_section(svc):
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">03</div>
      <div class="section-head-meta">
        <span class="mono-label">Scope of Work · What&rsquo;s Included</span>
        <h2>What every <em>{svc["name"].lower()}</em> project includes.</h2>
        <div class="section-head-text"><p>Itemized in your estimate, executed on the job, signed off at the final walkthrough. No surprise change orders mid-pour.</p></div>
      </div>
    </div>
    <ul style="list-style:none;display:grid;grid-template-columns:repeat(2,1fr);gap:14px 30px;max-width:1080px;margin:0 auto;padding:0;font-size:1rem;line-height:1.5">
      {"".join(f'<li style="display:flex;gap:14px;align-items:flex-start;padding-bottom:14px;border-bottom:1px solid var(--rule)"><span style="font-family:var(--font-display);color:var(--orange);font-size:1.1rem;line-height:1;flex-shrink:0">●</span><span>{x}</span></li>' for x in svc["scope_items"])}
    </ul>
  </div>
</section>'''

# ============================================================================
# 5 MISTAKES section
# ============================================================================
def mistakes_section(service_slug, svc, city_name=None):
    items = MISTAKES_BY_SERVICE.get(service_slug, [])
    rows = ""
    for i, (h, body) in enumerate(items, 1):
        rows += f'''<div class="feature-row">
  <div class="feature-num">{i:02d}</div>
  <div class="feature-body">
    <h3>{h}</h3>
    <p>{body}</p>
  </div>
</div>'''
    title_city = f" in {city_name}" if city_name else ""
    return f'''<section style="background:var(--paper)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label">Hard-Won Lessons · {svc["short"]}</span>
        <h2>Five expensive {svc["short"].lower()} mistakes to avoid<em>{title_city}</em>.</h2>
        <div class="section-head-text"><p>Every one of these has cost a Florida homeowner real money on a redo. None of them are obvious in advance. All of them are avoidable.</p></div>
      </div>
    </div>
    <div class="features-list">{rows}</div>
  </div>
</section>'''

# ============================================================================
# REVIEWS — NEW business: no invented reviews/ratings. Render a "be the first"
# CTA when there are no real reviews yet; never print rating placeholders.
# ============================================================================
def reviews_or_cta(svc, city_name=None, section_num="07"):
    real = [r for r in REVIEWS if isinstance(r, dict)] if REVIEWS else []
    where = f" in {city_name}" if city_name else f" across {REGION}"
    label_where = city_name if city_name else REGION
    if BUSINESS.get("has_reviews") and real:
        # (Reserved for when the owner supplies real Google reviews.)
        return reviews_section(limit=6, headline=f"What {svc['short'].lower()} clients say.")
    return f'''<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">{section_num}</div>
      <div class="section-head-meta">
        <span class="mono-label">Reviews · {label_where}</span>
        <h2>Be our first <em>{svc["short"].lower()}</em> review{where}.</h2>
        <div class="section-head-text"><p>{BUSINESS["name"]} is a local, owner-run concrete &amp; paver crew building a name the honest way &mdash; one driveway, patio, and pool deck at a time. We&rsquo;d rather earn a review than borrow one, so you won&rsquo;t find invented star ratings here. Hire us for your {svc["short"].lower()} project and tell the next homeowner the truth.</p></div>
      </div>
    </div>
    <aside class="contact-banner" style="margin-top:0">
      <div class="contact-banner-text">
        <strong>Fully Insured · written workmanship warranty on every job.</strong>
        <span>Free estimate within 24 hours, often same-day — call, text, or email.</span>
      </div>
      <div class="contact-banner-cta">
        <a href="{TEL_LINK}" class="btn btn-orange">Call {BUSINESS["phone_display"]}</a>
        <a href="/contact/#quote" class="btn btn-outline-light">Get a Free Estimate</a>
      </div>
    </aside>
  </div>
</section>'''

# ============================================================================
# CHECKLIST — wrap _gen helper, rewrite "47" → "42" copy for this engine.
# ============================================================================
def checklist_42(city_name=None, service_name=None, section_num="04"):
    html = checklist_section(city_name=city_name, service_name=service_name)
    html = html.replace("all 47 points", "all 42 points")
    html = html.replace("47-Point", "42-Point")
    html = html.replace("The Napa&rsquo;s Standard", "The Lakewood Ranch Concrete Standard")
    if section_num != "04":
        html = html.replace('<div class="section-head-num">04</div>', f'<div class="section-head-num">{section_num}</div>')
    return html

# ============================================================================
# SERVICE-CITY page builder
# ============================================================================
def build_service_city(service_slug, city_slug):
    svc = SERVICES[service_slug]
    city = CITIES[city_slug]
    URL = f"{SITE}/{service_slug}/{city_slug}/"

    short = svc["short"]
    city_name = city["name"]

    # SEO — keyword-first ("concrete driveways bradenton"), city-specific.
    TITLE = clip_title(f"{short} {city_name} FL · {BUSINESS['name']}")
    DESC = clip_desc(
        f"{short} in {city_name}, FL — {lead_snippet(svc['intro_lead'], 80)} "
        f"Local crew, {len(city['neighborhoods'])}+ {city_name} neighborhoods. "
        f"Fully Insured · free estimate."
    )

    schemas = [
        local_business_no_rating(URL, f"{svc['name']} in {city_name}, FL", city=city_name, service=svc["name"]),
        schema_service(svc, city=city_name, canonical=URL),
        schema_faqpage(svc["faqs"]),
        schema_breadcrumb([
            ("Home", SITE+"/"),
            (svc["name"], f"{SITE}/{service_slug}/"),
            (city_name, URL),
        ]),
    ]
    bc = breadcrumbs([
        ("Home","/"),
        (svc["name"], f"/{service_slug}/"),
        (city_name, None),
    ])

    # HERO — city-specific H1: "{service} in {city}" (distinct from hub).
    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">{city["county"]} · {svc["name"]} · {len(city["neighborhoods"])}+ neighborhoods</span>
    <h1>{svc["h1_phrase"]}<br>in <em>{city_name}<span class="stop">,</span></em> FL.</h1>
    <p class="page-hero-sub">{svc["intro_lead"]}</p>
    <div class="page-hero-trust">
      <span>{len(city["neighborhoods"])}+ {city_name} neighborhoods</span>
      <span>Fully Insured</span>
      <span>42-point install standard</span>
      <span>Written workmanship warranty</span>
    </div>
  </div>
</section>'''

    # CITY-SPECIFIC LEAD (01) — woven from city context fields.
    lead = f'''<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">{svc["name"]} · {city_name} Service Profile</span>
        <h2>{svc["short"]} in {city_name}, done <em>the right way</em>.</h2>
      </div>
    </div>
    <div class="intro-prose">
      <p><strong>{svc["name"]} in {city_name}, Florida</strong> is one of our most-requested services across {city["county"]}. {city["context_short"]} The {svc["name"].lower()} market in {city_name} is shaped by three things: {city["primary_market"].lower()}, the sandy soil and year-round humidity we share across {REGION}, and the volume of new construction (and aging concrete) in the neighborhoods we work here.</p>

      <p>{svc["intro_long_p1"]}</p>

      <p>{svc["intro_long_p2"]}</p>

      <p><strong>The local angle for {city_name}:</strong> {city["humidity_note"]} For {svc["name"].lower()} specifically, that means we excavate and compact the base to depth, plan control and expansion joints for how this ground moves, and confirm drainage before anything is poured or laid. Most {city_name} projects we take on are in {city["neighborhoods"][0]}, {city["neighborhoods"][1]}, or one of the surrounding subdivisions &mdash; we&rsquo;ve worked all of them, we know the HOA / ARC rules, and we know what {city["county"]} permitting actually looks for when a permit is involved.</p>
    </div>
  </div>
</section>'''

    # SCOPE (03)
    scope_html = scope_section(svc)

    # CHECKLIST (04)
    checklist_html = checklist_42(city_name=city_name, service_name=svc["name"], section_num="04")

    # NEIGHBORHOODS (05)
    neigh_html = neighborhoods_section(city)

    # MISTAKES (06)
    mistakes_html = mistakes_section(service_slug, svc, city_name=city_name)

    # PRICING TABLE
    pricing_html = pricing_table_html(svc, city_name=city_name)

    # REVIEWS / CTA (07)
    reviews_html = reviews_or_cta(svc, city_name=city_name, section_num="07")

    # FAQ (08)
    faq_html = faq_section(svc["faqs"], headline=f"{svc['short']} in {city_name} &mdash; the real questions.", label=f"FAQ · {svc['name']} · {city_name}")

    # RELATED — other services in this city + same service in other cities
    other_svcs = [s for s in SERVICE_ORDER if s != service_slug]
    other_svcs_links = "".join(
        f'<li><a href="/{s}/{city_slug}/">{SERVICES[s]["short"]} in {city_name}</a></li>'
        for s in other_svcs
    )
    other_cities = [c for c in CITIES if c != city_slug]
    other_cities_links = "".join(
        f'<li><a href="/{service_slug}/{c}/">{svc["short"]} in {CITIES[c]["name"]}</a></li>'
        for c in other_cities
    )
    related_html = f'''<section style="background:var(--paper)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px">
      <div class="related-box">
        <div class="related-box-label">Read Next · Other {city_name} Services</div>
        <h3>{city_name} homeowners also book.</h3>
        <ul>{other_svcs_links}<li><a href="/{city_slug}/">All services in {city_name} →</a></li></ul>
      </div>
      <div class="related-box">
        <div class="related-box-label">Read Next · {svc["short"]} in Other Cities</div>
        <h3>{svc["short"]} across the Suncoast.</h3>
        <ul>{other_cities_links}<li><a href="/{service_slug}/">{svc["short"]} service overview →</a></li></ul>
      </div>
    </div>
  </div>
</section>'''

    # FINAL CTA
    final_html = final_cta(
        headline=f"Ready for a real estimate on {svc['short'].lower()} in {city_name}?",
        sub=f"Free on-site measure. Written estimate within 24 hours. {svc['short']} for {city_name} homes, built to the {BUSINESS['checklist_points']}-point {BUSINESS['name']} standard &mdash; Fully Insured."
    )

    body = "\n".join([hero, lead, project_photos_html(service_slug, city_slug=city_slug), scope_html, checklist_html, neigh_html, mistakes_html, pricing_html, reviews_html, faq_html, related_html, f'<div class="container">{contact_banner(message="Free, no-pressure estimate within 24 hours.", subtitle="Call, text, or email — your project, your call.")}</div>', final_html])

    head_html = head(TITLE, DESC, URL, og_image=og_url(service_slug), json_ld=schemas)
    out = f"{service_slug}/{city_slug}/index.html"
    write_page(out, head_html, header(active="services"), body, breadcrumbs_html=bc)


# ============================================================================
# SERVICE HUB page builder
# ============================================================================
def build_service_hub(service_slug):
    svc = SERVICES[service_slug]
    URL = f"{SITE}/{service_slug}/"
    n_cities = len(CITIES)

    # SEO — keyword-first, region-level (distinct from city pages).
    TITLE = clip_title(f"{svc['h1_phrase']} in Lakewood Ranch & Manatee FL")
    DESC = clip_desc(
        f"{svc['name']} across {REGION_PLAIN}. {lead_snippet(svc['intro_lead'], 60)} "
        f"Fully Insured · free estimate."
    )

    schemas = [
        local_business_no_rating(URL, f"{svc['name']} contractor", service=svc["name"]),
        schema_service(svc, canonical=URL),
        schema_faqpage(svc["faqs"]),
        schema_breadcrumb([
            ("Home", SITE+"/"),
            (svc["name"], URL),
        ]),
    ]
    bc = breadcrumbs([("Home","/"), (svc["name"], None)])

    # HERO — region-level H1: "{service} · Lakewood Ranch & Manatee" (distinct).
    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Service · {svc["name"]} · {n_cities} Suncoast Cities</span>
    <h1>{svc["h1_phrase"]}.<br>Lakewood Ranch &amp; <em>Manatee</em>.</h1>
    <p class="page-hero-sub">{svc["intro_lead"]}</p>
    <div class="page-hero-trust">
      <span>{n_cities} cities served</span>
      <span>Fully Insured</span>
      <span>Free estimate in 24 hours</span>
      <span>42-point install standard</span>
    </div>
  </div>
</section>'''

    # INTRO (01)
    lead = f'''<section style="background:var(--paper-deep)">
  <div class="container">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">Service · Overview</span>
        <h2>{svc["name"]}, the <em>right way</em>.</h2>
      </div>
    </div>
    <div class="intro-prose">
      <p>{svc["intro_long_p1"]}</p>
      <p>{svc["intro_long_p2"]}</p>
      <p>This service is available in all {n_cities} cities we cover across {REGION} &mdash; pick the city closest to you below for {svc["short"].lower()}-specific pricing, FAQ, and a local-context page tailored to that market.</p>
    </div>
  </div>
</section>'''

    # SCOPE (02)
    scope_html = scope_section(svc)
    scope_html = scope_html.replace('<div class="section-head-num">03</div>', '<div class="section-head-num">02</div>')

    # CHECKLIST (03)
    checklist_html = checklist_42(service_name=svc["name"], section_num="03")

    # MISTAKES (04)
    mistakes_html = mistakes_section(service_slug, svc)
    mistakes_html = mistakes_html.replace('<div class="section-head-num">06</div>', '<div class="section-head-num">04</div>')

    # PRICING (05)
    pricing_html = pricing_table_html(svc)

    # CITIES GRID (06)
    city_cards = ""
    for cslug, c in CITIES.items():
        city_cards += f'''<a href="/{service_slug}/{cslug}/" class="area-card">
  <div class="area-card-name">{svc["short"]} · {c["name"]}, FL</div>
  <div class="area-card-meta">{c["county"]} · {len(c["zips"])} ZIPs</div>
  <span class="area-card-arrow">See {c["name"]} →</span>
</a>'''
    cities_html = f'''<section class="areas-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">06</div>
      <div class="section-head-meta">
        <span class="mono-label on-dark">Cities Served · {svc["short"]}</span>
        <h2>{svc["short"]} across <em>{n_cities} Suncoast cities</em>.</h2>
        <div class="section-head-text"><p>Each city has its own page with local pricing, neighborhoods, and a {svc["short"].lower()} FAQ tailored to that market.</p></div>
      </div>
    </div>
    <div class="areas-grid">{city_cards}</div>
  </div>
</section>'''

    # REVIEWS / CTA (07)
    reviews_html = reviews_or_cta(svc, city_name=None, section_num="07")

    # FAQ (08)
    faq_html = faq_section(svc["faqs"], headline=f"{svc['short']} questions, honestly answered.", label=f"FAQ · {svc['name']}")

    final_html = final_cta(
        headline=f"Get a real {svc['short'].lower()} estimate.",
        sub=f"Free on-site measure. Written, line-itemized estimate within 24 hours. {svc['short']} built to the {BUSINESS['checklist_points']}-point {BUSINESS['name']} standard &mdash; Fully Insured."
    )

    body = "\n".join([hero, lead, project_photos_html(service_slug), scope_html, checklist_html, mistakes_html, pricing_html, cities_html, reviews_html, faq_html, f'<div class="container">{contact_banner(message="Free, no-pressure estimate within 24 hours.", subtitle="Call, text, or email — your project, your call.")}</div>', final_html])

    head_html = head(TITLE, DESC, URL, og_image=og_url(service_slug), json_ld=schemas)
    out = f"{service_slug}/index.html"
    write_page(out, head_html, header(active="services"), body, breadcrumbs_html=bc)


if __name__ == "__main__":
    print(f"Building {len(SERVICE_ORDER)} service hub pages...")
    for s in SERVICE_ORDER:
        build_service_hub(s)
        print(f"  [ok] /{s}/")
    print(f"\nBuilding {len(SERVICE_ORDER)*len(CITIES)} service-city pages...")
    count = 0
    for s in SERVICE_ORDER:
        for c in CITIES:
            build_service_city(s, c)
            count += 1
    print(f"  [ok] Built {count} service-city pages.")
    print(f"\nTotal pages written: {len(SERVICE_ORDER) + count}")
