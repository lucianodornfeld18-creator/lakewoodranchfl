#!/usr/bin/env python3
"""Generate /guides/ hub + long-form decision guides + /glossary/.
Guide topics are intentionally distinct from the cost blog and the 5 general
posts, and avoid generic competitor angles. Metadata lives in _data.GUIDES;
glossary terms in _data.GLOSSARY. Bodies live here."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _gen import *
from _data import GUIDES, GLOSSARY

GUIDES_BY_SLUG = {g["slug"]: g for g in GUIDES}


def term_id(term):
    return "t-" + re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")


# ============================================================================
# Guide page shell
# ============================================================================
def guide_shell(guide, lede, sections_html, faqs=None, related=None):
    URL = f"{SITE}/guides/{guide['slug']}/"
    TITLE = guide["title"][:60]
    DESC = clip_desc(guide["meta_desc"])
    cat = guide.get("category", "Guide")
    date_pretty = guide["date_published"][:10]

    schemas = [
        schema_article(guide, URL),
        schema_breadcrumb([
            ("Home", SITE + "/"),
            ("Guides", f"{SITE}/guides/"),
            (guide["title"], URL),
        ]),
    ]
    if faqs:
        schemas.append(schema_faqpage(faqs))

    bc = breadcrumbs([
        ("Home", "/"),
        ("Guides", "/guides/"),
        (guide["title"][:48] + ("…" if len(guide["title"]) > 48 else ""), None),
    ])

    article_hero = f'''<section class="page-hero" style="padding:60px 0 50px">
  <div class="page-hero-inner">
    <div class="post-meta-bar" style="color:rgba(245,242,236,.6)">
      <span class="cat" style="color:var(--orange)">● Guide · {cat}</span>
      <span>Updated {date_pretty}</span>
      <span>By Napa&rsquo;s Crew</span>
    </div>
    <h1 style="margin-top:14px">{guide["title"]}</h1>
    <p class="page-hero-sub" style="font-style:italic">{guide["meta_desc"]}</p>
  </div>
</section>'''

    related_block = ""
    if related:
        items = "".join(f'<li><a href="{url}">{label}</a></li>' for url, label in related)
        related_block = f'''<div class="related-box">
  <div class="related-box-label">Read Next · Related</div>
  <h3>Keep going.</h3>
  <ul>{items}</ul>
</div>'''

    author_block = f'''<div class="post-author">
  <div class="post-author-avatar">N</div>
  <div class="post-author-info">
    <strong>The Napa&rsquo;s Crew</strong>
    <span>{BUSINESS["city"]}, FL · Est. {BUSINESS["year_founded"]} · {BUSINESS["unique_stat_full"]}</span>
  </div>
</div>'''

    faq_html = ""
    if faqs:
        faq_html = faq_section(faqs, headline="Questions this raises.", label="FAQ · Quick Answers")

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

<div class="container">{contact_banner()}</div>

{final_cta(headline="Got a project this guide applies to?", sub="Free in-home measure. Written, line-itemized quote within 24 hours.")}'''

    head_html = head(TITLE, DESC, URL, og_image=og_url(path=OG_GUIDES), json_ld=schemas, og_type="article")
    write_page(f"guides/{guide['slug']}/index.html", head_html, header(active="guides"), body, breadcrumbs_html=bc)
    print(f"Wrote /guides/{guide['slug']}/")


# ============================================================================
# GUIDE BODIES
# ============================================================================
def build_guides():
    # ---- 1. Herringbone worth it ----
    g = GUIDES_BY_SLUG["is-herringbone-worth-it"]
    lede = ("A herringbone or chevron floor is the single most-photographed thing we install — "
            "and the single most-misjudged on budget. The material barely costs more than straight "
            "plank. The labor is where it lands, and that number surprises people. Here's the honest "
            "math on whether the pattern earns its premium in a Tampa Bay home.")
    sections = '''
<h2>Herringbone vs. chevron — they aren't the same floor</h2>
<p><strong>Herringbone</strong> uses square-cut rectangular planks laid at a 90-degree angle in a staggered, broken zigzag. <strong>Chevron</strong> uses planks cut at an angle so the ends meet point-to-point in a continuous V. Chevron is the cleaner, more formal look; it's also the more expensive of the two because every board is mitre-cut and the cut angles have to be dead-consistent across the whole field.</p>

<h2>Where the premium actually comes from</h2>
<p>The plank itself runs you a few dollars a foot more, sometimes nothing if you're using a product that ships in standard sizes. The cost is the install. A straight-plank floor racks fast — rows go down, joints stagger, you move. A herringbone floor is laid one piece at a time off a snapped centerline, every board angle-checked, every intersection tight, with far more offcut waste. Plan on roughly <strong>50–90% more labor than the same square footage of straight plank</strong>, and add a 10–15% material waste factor on top.</p>

<table class="post-table">
<thead><tr><th>Layout</th><th>Labor vs. straight plank</th><th>Best in</th></tr></thead>
<tbody>
<tr><td>Straight plank</td><td><strong>Baseline</strong></td><td>Whole-home, anywhere</td></tr>
<tr><td>Diagonal straight</td><td><strong>+15–25%</strong></td><td>Small rooms that need to feel bigger</td></tr>
<tr><td>Herringbone</td><td><strong>+50–70%</strong></td><td>Foyers, dining, studies, accent areas</td></tr>
<tr><td>Chevron</td><td><strong>+70–90%</strong></td><td>Statement foyers, formal spaces</td></tr>
</tbody>
</table>

<h2>When it's worth it</h2>
<ul>
<li><strong>As an accent, not the whole house.</strong> The pattern reads strongest in a defined space — a foyer, a dining room, a study — that then transitions to straight plank everywhere else. We've done exactly this in Esplanade and Country Club East homes and it photographs like a custom build at a fraction of doing the whole floor in pattern.</li>
<li><strong>In a home where flooring affects resale.</strong> In the upper brackets of Lakewood Ranch, downtown Sarasota, and South Tampa, a herringbone foyer signals a level of finish buyers notice. In a starter home it's money the appraisal won't return.</li>
<li><strong>When you're already committed to premium wood.</strong> If you're installing European white oak anyway, the pattern upgrade is a smaller relative jump than it looks.</li>
</ul>

<h2>When it isn't</h2>
<ul>
<li><strong>Over a slab that hasn't been flattened.</strong> Pattern work is brutally honest about a wavy subfloor — every intersection shows it. Herringbone over an unprepped slab looks worse than straight plank would. We self-level first, every time, which adds to the number.</li>
<li><strong>In a budget whole-home install.</strong> Patterning 1,800 square feet can add five figures in labor alone. That money usually buys more home value as a better-grade plank laid straight.</li>
<li><strong>In a rental.</strong> Guests don't pay more for herringbone; the floor just costs you more to install and repair.</li>
</ul>

<div class="post-key-takeaway">
<strong>The Honest Call</strong>
Herringbone and chevron are worth the premium as a defined accent in a home where finish level matters — a foyer or dining room that transitions to straight plank elsewhere. As a whole-home layout on a budget, the labor premium almost never returns more than spending the same dollars on better material laid straight. We'll quote both ways and let you see the difference on paper.
</div>
'''
    faqs = [
        ("Can you do herringbone in vinyl plank, or only real wood?",
         "Both. Plenty of premium LVP and SPC lines now ship in herringbone-ready sizes, and the pattern labor premium applies the same way it does for wood. It's a great way to get the look in a kitchen or rental where you want waterproof material — you carry the design statement without the maintenance of real wood."),
        ("Does herringbone make a small room look bigger or smaller?",
         "It draws the eye along its direction, so running the pattern's long axis toward the room's far wall makes a narrow space read longer. In a genuinely small room a tight herringbone can feel busy, though — sometimes a simple diagonal straight lay gives you the space-expanding effect at a fraction of the labor."),
    ]
    related = [
        ("/hardwood-flooring/", "Hardwood Flooring · Service Page"),
        ("/guides/wide-plank-vs-standard-width/", "Wide-Plank vs. Standard Width"),
        ("/blog/engineered-hardwood-vs-spc-lakewood-ranch/", "Engineered Hardwood vs. SPC: Field Test"),
    ]
    guide_shell(g, lede, sections, faqs=faqs, related=related)

    # ---- 2. Porcelain vs LVP kitchen ----
    g = GUIDES_BY_SLUG["porcelain-vs-lvp-florida-kitchen"]
    lede = ("In most rooms the flooring choice is obvious. The kitchen is the exception — it's the one "
            "space where porcelain tile and luxury vinyl plank genuinely compete, each with a real case. "
            "Here's how we actually decide between them in Tampa Bay kitchens, and why the answer changes "
            "with the house.")
    sections = '''
<h2>Why the kitchen is the hard call</h2>
<p>Everywhere else, the decision tends to make itself: living areas lean toward wood or wood-look plank, full baths and laundry rooms lean toward tile. The kitchen sits in the middle. It takes water like a bathroom, traffic like a living room, dropped pans like nowhere else, and it's usually open to the rooms on either side — so the floor has to make sense next to whatever's out there too.</p>

<h2>The case for porcelain</h2>
<ul>
<li><strong>It does not care about water, heat, or sand.</strong> A porcelain floor in a Florida kitchen will outlive the cabinets above it. Spills, dishwasher leaks, dropped glassware — none of it touches the tile.</li>
<li><strong>It's the premium look in an upper-bracket home.</strong> Large-format porcelain or a marble-look slab reads as a finished, high-end kitchen in a way vinyl can't quite match up close.</li>
<li><strong>It's effectively permanent.</strong> No wear layer to grind through, no refinishing, no replacement on any normal timeline.</li>
</ul>
<p>The costs: it's harder underfoot (tougher on dropped dishes and on your knees over a long cooking session), it's cooler in winter unless you add radiant heat, and the substrate has to be properly flat — which on a Florida slab usually means self-leveling first.</p>

<h2>The case for LVP</h2>
<ul>
<li><strong>It's warmer, softer, and quieter underfoot.</strong> For a kitchen you stand in for hours, that matters more than people expect.</li>
<li><strong>It flows seamlessly into the rest of the house.</strong> If your living areas are already a wood-look plank, running the same product through the kitchen makes an open floor plan read as one continuous space with no transition strip.</li>
<li><strong>It's waterproof through the core</strong> and far more forgiving of a dropped pan than tile.</li>
</ul>
<p>The costs: even a premium 22-mil plank has a wear layer that's finite, a heavy appliance dragged across it can gouge it, and in a true luxury kitchen it reads a notch below porcelain or stone up close.</p>

<table class="post-table">
<thead><tr><th>Factor</th><th>Porcelain Tile</th><th>Premium LVP</th></tr></thead>
<tbody>
<tr><td>Waterproof</td><td><strong>Completely</strong></td><td><strong>Through the core</strong></td></tr>
<tr><td>Underfoot comfort</td><td>Hard, cool</td><td><strong>Warm, softer, quiet</strong></td></tr>
<tr><td>Dropped-dish survival</td><td>The dish loses</td><td><strong>More forgiving</strong></td></tr>
<tr><td>Flows into open-plan wood-look</td><td>Needs a transition</td><td><strong>Seamless</strong></td></tr>
<tr><td>Lifespan</td><td><strong>Effectively permanent</strong></td><td>15–25 years</td></tr>
<tr><td>Installed cost (2026)</td><td>$7.50–$16/sq ft</td><td><strong>$4.25–$9.50/sq ft</strong></td></tr>
</tbody>
</table>

<h2>How we actually decide</h2>
<p>We ask three questions at the kitchen table. <strong>Is the rest of the open floor already a wood-look plank?</strong> If yes, LVP usually wins on flow alone. <strong>Is this an upper-bracket home where the kitchen is a selling feature?</strong> If yes, porcelain or slab earns its premium. <strong>Do you stand and cook for hours, with knees or a back that notice a hard floor?</strong> If yes, that tips it toward LVP regardless of the rest.</p>

<div class="post-key-takeaway">
<strong>The Short Version</strong>
For an open-plan Tampa Bay home where the kitchen flows into wood-look living areas, premium LVP usually wins on continuity and comfort. For a closed-off or upper-bracket kitchen where the floor is a design statement and water is a constant, porcelain earns its premium and never looks back. There's no universally right answer — there's a right answer for your house, and that's what the estimate is for.
</div>
'''
    faqs = [
        ("Can I run the same vinyl plank from my living room straight through the kitchen?",
         "Yes, and it's one of the most popular things we do — a continuous waterproof SPC plank across living areas and kitchen with no transition strip makes an open floor plan feel twice as large. The only caution is heavy appliances: we use protective sliders on install and recommend felt under anything you'll move."),
        ("Is tile too cold for a Florida kitchen?",
         "Most of the year it's a feature, not a bug — a cool porcelain floor is welcome eight months out of twelve here. If you're someone who feels the January mornings, a radiant heat mat under the tile (about $4–$6 per square foot added) turns it into the most comfortable floor in the house."),
    ]
    related = [
        ("/tile-installation/", "Tile Installation · Service Page"),
        ("/vinyl-plank-flooring/", "Vinyl Plank Flooring · Service Page"),
        ("/blog/best-flooring-gulf-coast-humidity/", "Gulf Coast Humidity Guide"),
    ]
    guide_shell(g, lede, sections, faqs=faqs, related=related)

    # ---- 3. How to read a flooring quote ----
    g = GUIDES_BY_SLUG["how-to-read-a-flooring-quote"]
    lede = ("A flooring quote is where contractors hide things. A one-number bid tells you nothing; a "
            "properly line-itemized quote tells you everything. Here's exactly what every line should "
            "say, where the padding usually lives, and the questions that turn a vague estimate into a "
            "real one.")
    sections = '''
<h2>The one-number quote is the red flag</h2>
<p>If a contractor hands you a single number — "$11,400, all in" — you can't evaluate it, you can't compare it, and you can't tell what happens when the scope shifts. A real quote breaks the job into its parts so you can see what you're buying and what you're not. If you can't get a line-itemized version, that's your answer about the contractor.</p>

<h2>The lines that should be on every quote</h2>
<ul>
<li><strong>Material</strong> — the actual product, with brand, line, thickness, and wear layer or species. "LVP" is not a spec; "6.5mm SPC, 22-mil wear layer, [brand/line]" is.</li>
<li><strong>Material waste factor</strong> — a real install orders 7–10% over (more for diagonal or pattern work). It should be stated, not buried.</li>
<li><strong>Labor</strong> — install labor, separate from material, ideally per square foot.</li>
<li><strong>Demo &amp; haul-away</strong> — removing and disposing of the old floor, per square foot.</li>
<li><strong>Subfloor prep</strong> — self-leveling, patching, vapor barrier, moisture testing. This is the line that "surprise change orders" come from when it's missing.</li>
<li><strong>Transitions &amp; trim</strong> — thresholds, reducers, quarter-round, baseboard reset. Count the doorways; each one is a transition.</li>
<li><strong>Furniture / appliance / toilet handling</strong> — what they move and what they don't.</li>
<li><strong>Timeline &amp; payment schedule</strong> — start date, working days, and when each payment is due.</li>
</ul>

<h2>Where the padding hides</h2>
<table class="post-table">
<thead><tr><th>Tactic</th><th>What it looks like</th><th>What to ask</th></tr></thead>
<tbody>
<tr><td>The missing prep line</td><td>No subfloor/moisture line at all</td><td>"What happens if the slab isn't flat or reads wet?"</td></tr>
<tr><td>Vague material</td><td>"Premium LVP" with no brand/spec</td><td>"What's the exact product, thickness, and wear layer?"</td></tr>
<tr><td>The lowball start</td><td>Far below every other bid</td><td>"Is demo, prep, and trim included, or billed later?"</td></tr>
<tr><td>Cash-only / no contract</td><td>No written scope, no warranty</td><td>"Can I get this in writing with a workmanship warranty?"</td></tr>
<tr><td>The fat waste factor</td><td>20%+ material overage</td><td>"Why is the waste factor this high for a straight lay?"</td></tr>
</tbody>
</table>

<h2>The three questions that expose a lowball</h2>
<ol>
<li><strong>"Is subfloor prep included, and what's your plan if the slab tests wet or uneven?"</strong> A real installer has already taken a moisture reading and has an answer. A lowballer says "we'll deal with it if it comes up" — which is where the change order is born.</li>
<li><strong>"Who, exactly, installs it?"</strong> The price gap between bids is almost always labor. Subcontracted day-labor is cheaper and inconsistent. Ask whether the people who measured are the people who install.</li>
<li><strong>"What's the workmanship warranty, in writing?"</strong> No written warranty means no accountability after the check clears.</li>
</ol>

<div class="post-key-takeaway">
<strong>The Rule of Thumb</strong>
The cheapest bid and the most expensive bid are both usually telling you something. The cheapest one is often missing a line — prep, demo, trim — that becomes a change order later. The honest quote is the one that itemizes everything, names the actual product, includes the prep, and puts the warranty in writing. That's the one you can hold someone to. It's also exactly how we write ours.
</div>
'''
    faqs = [
        ("Should I just take the lowest bid?",
         "Only after you've confirmed all three bids cover the same scope. The lowest number frequently leaves out demo, subfloor prep, or trim, so it's not actually the lowest job — it's the most incomplete quote. Normalize the scope across bids first, then the real comparison appears, and it's often not the bid you'd have guessed."),
        ("Is a deposit normal before work starts?",
         "Yes — a deposit to lock the start date and order materials is standard, typically around 10%, with the balance tied to delivery, mid-install, and a final payment after you've walked the finished floor. What isn't normal is a large up-front payment with no written scope or schedule attached to it."),
    ]
    related = [
        ("/financing/", "Financing Options"),
        ("/warranty/", "12-Month Workmanship Warranty"),
        ("/contact/#quote", "Get a Line-Itemized Quote"),
    ]
    guide_shell(g, lede, sections, faqs=faqs, related=related)

    # ---- 4. Wide-plank vs standard width ----
    g = GUIDES_BY_SLUG["wide-plank-vs-standard-width"]
    lede = ("Plank width looks like a styling choice. It's actually an engineering one. Going from a "
            "3-inch board to a 7-inch board changes how the floor moves, how it's installed, how flat "
            "the subfloor has to be, and what it costs. Here's what actually shifts when the plank "
            "gets wider — and why it matters more in Florida than up north.")
    sections = '''
<h2>What "wide plank" even means</h2>
<p>There's no legal line, but in practice the trade calls anything 5 inches and up "wide plank," with 7–9 inch boards being the modern premium look and 10-inch-plus boards being genuinely wide. Traditional strip flooring — the 2¼ and 3¼ inch oak in pre-war homes — is "standard" or "narrow." The wider the board, the more contemporary and the more material you see per plank.</p>

<h2>Wider boards move more</h2>
<p>Wood expands and contracts across its width, not its length. A 7-inch board has more than double the across-grain dimension of a 3-inch board, so it moves more than double the absolute distance with the same humidity swing. In Florida — where the indoor-to-outdoor moisture swing is real — that's the whole reason wide-plank <em>solid</em> hardwood is risky on a slab, and why almost all wide-plank flooring sold here is <strong>engineered</strong>: the cross-ply core holds the width stable in a way solid wood can't.</p>

<h2>Wider boards demand a flatter subfloor</h2>
<p>A narrow board flexes slightly and forgives a minor dip. A wide, rigid plank bridges the dip instead — so it telegraphs every low spot as a hollow, deflecting feel underfoot, and on glue-down it can lead to bonding gaps. The flatter the floor has to be, the more self-leveling we do up front. Budget for prep when you go wide.</p>

<table class="post-table">
<thead><tr><th>Factor</th><th>Standard (2¼–4″)</th><th>Wide Plank (7–9″)</th></tr></thead>
<tbody>
<tr><td>Look</td><td>Traditional, busier grain</td><td><strong>Contemporary, calmer</strong></td></tr>
<tr><td>Movement with humidity</td><td><strong>Less per board</strong></td><td>More per board</td></tr>
<tr><td>Solid hardwood on slab</td><td>Risky</td><td><strong>Don't — go engineered</strong></td></tr>
<tr><td>Subfloor flatness needed</td><td>Forgiving</td><td><strong>Strict — often self-level</strong></td></tr>
<tr><td>Seams / joints per room</td><td>Many</td><td><strong>Far fewer</strong></td></tr>
<tr><td>Installed cost</td><td>Lower</td><td>Higher (material + prep)</td></tr>
</tbody>
</table>

<h2>So which should you pick?</h2>
<ul>
<li><strong>Wide plank, engineered</strong> is the right call for most modern Tampa Bay homes that want the current look — open floor plans especially, where fewer seams make the space read calmer and larger. Just price in the subfloor prep.</li>
<li><strong>Standard width</strong> is right for restoring a period home (matching original 2¼ oak in a 1920s bungalow), for tighter budgets, and anywhere the subfloor is genuinely uneven and self-leveling the whole floor isn't in the cards.</li>
</ul>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
Wide plank is a look most people want and a fully sound choice in Florida — as long as it's engineered, not solid, and as long as you accept that a wider board needs a flatter subfloor and a bit more prep. Narrow strip flooring still wins for period restorations and tight budgets. The width changes the engineering, not just the style, and a good installer prices it that way.
</div>
'''
    faqs = [
        ("Why is almost all wide-plank flooring engineered, not solid?",
         "Because width is where wood moves, and a wide solid board on a Florida slab moves enough to cup or gap within a few seasons. Engineered wide plank puts a real-wood wear layer over a cross-ply core that holds the width dimensionally stable, so you get the wide-plank look without the wide-plank failure mode. It's the right answer here nearly every time."),
        ("Does wide plank really need more subfloor prep?",
         "Usually yes. A rigid wide board won't follow a dip the way a narrow board flexes to — it bridges the low spot and feels hollow, or on glue-down it bonds unevenly. We straightedge the floor and self-level where needed before wide plank goes down, and that prep belongs in the quote, not in a surprise change order later."),
    ]
    related = [
        ("/hardwood-flooring/", "Hardwood Flooring · Service Page"),
        ("/guides/slab-moisture-explained/", "Slab Moisture, Explained"),
        ("/guides/is-herringbone-worth-it/", "Is Herringbone Worth the Premium?"),
    ]
    guide_shell(g, lede, sections, faqs=faqs, related=related)

    # ---- 5. Slab moisture explained ----
    g = GUIDES_BY_SLUG["slab-moisture-explained"]
    lede = ("Most Gulf Coast floor failures don't start in the floor. They start in the slab underneath "
            "it. Concrete wicks moisture up from the soil, and if the floor going down on top can't "
            "handle it, the failure is just a matter of time. Here's what the moisture numbers mean, "
            "how we read them, and why a reading can change your whole install.")
    sections = '''
<h2>Why a Florida slab is never really "dry"</h2>
<p>A concrete slab sits on soil, and soil holds water. Concrete is porous, so it pulls that moisture upward and releases it as vapor at the surface — continuously, for the life of the slab. In Florida's water table and humidity, that vapor emission is higher and more persistent than in most of the country. The slab looks bone dry. It isn't. A floor that traps that vapor against itself — or an adhesive that can't tolerate it — fails from below, where you can't see it coming.</p>

<h2>The two readings we take</h2>
<h3>Calcium chloride test (MVER)</h3>
<p>A small dish of calcium chloride is sealed to the slab for a set window; the weight it gains tells us the Moisture Vapor Emission Rate — pounds of water per 1,000 square feet per 24 hours. It's a surface-emission snapshot. Most glue-down products want to see roughly <strong>3 lbs or below</strong>; borderline numbers mean a moisture-mitigation step before adhesive.</p>
<h3>In-situ relative humidity (RH) probe</h3>
<p>A probe set into a drilled hole reads the humidity <em>inside</em> the slab at depth — a truer picture of how much moisture is actually in the concrete and will eventually reach the surface. Most flooring systems target an in-slab RH at or under <strong>75–80%</strong> depending on the product. We use the probe on anything we're gluing down where the stakes are high.</p>

<table class="post-table">
<thead><tr><th>Reading</th><th>What it means</th><th>What we do</th></tr></thead>
<tbody>
<tr><td>Calcium chloride ≤ 3 lbs</td><td>Low surface emission</td><td><strong>Glue-down is clear</strong></td></tr>
<tr><td>Calcium chloride 3–5 lbs</td><td>Borderline</td><td>Vapor barrier or membrane first</td></tr>
<tr><td>Calcium chloride 5+ lbs</td><td>High emission</td><td><strong>Mitigation required — no exceptions</strong></td></tr>
<tr><td>RH probe ≤ 75%</td><td>Slab interior acceptable</td><td>Proceed per product spec</td></tr>
<tr><td>RH probe 80%+</td><td>Wet slab interior</td><td><strong>Membrane or rethink the product</strong></td></tr>
</tbody>
</table>

<h2>How a reading changes the install</h2>
<ul>
<li><strong>It picks the product.</strong> A wet slab rules out laminate and makes solid hardwood a non-starter; SPC vinyl plank and properly-isolated tile handle slab moisture far better.</li>
<li><strong>It adds (or removes) a mitigation step.</strong> Borderline numbers mean a 6-mil vapor barrier, a poured liquid membrane, or a moisture-mitigating adhesive — real line items that a quote skipping the test will "discover" later.</li>
<li><strong>It protects the warranty.</strong> Manufacturers void warranties for installs over out-of-spec slabs. A documented reading is what keeps your product warranty intact.</li>
</ul>

<div class="post-key-takeaway">
<strong>The One Thing to Remember</strong>
A slab can look perfectly dry and still emit enough vapor to destroy the floor you put on it. The only way to know is to test, and the test costs a fraction of a redo. Any quote for a glue-down floor over concrete that doesn't mention a moisture reading is quoting a gamble. We test every slab, log the number, and build the mitigation into the plan before anything goes down.
</div>
'''
    faqs = [
        ("Can't you just feel or look at whether a slab is dry?",
         "No — and anyone who says they can is guessing. A slab that's been sealed under old flooring for decades can read bone-dry to the touch and still emit well over the limit when you actually test it. The dish and the probe exist precisely because the eye and the hand can't see vapor. We don't skip the reading on glue-down work."),
        ("What does moisture mitigation actually cost?",
         "It depends on the reading and the area, but it's modest against a failed floor — a vapor-barrier underlayment runs roughly $0.55–$1.10 per square foot, and a poured liquid membrane for a genuinely wet slab is more. The point is that it's a known, quotable step when you test first, instead of a torn-out floor and a redo when you don't."),
    ]
    related = [
        ("/floor-repair/", "Floor Repair · Service Page"),
        ("/guides/wide-plank-vs-standard-width/", "Wide-Plank vs. Standard Width"),
        ("/glossary/", "Flooring Glossary"),
    ]
    guide_shell(g, lede, sections, faqs=faqs, related=related)

    # ---- 6. HOA condo flooring rules ----
    g = GUIDES_BY_SLUG["hoa-condo-flooring-rules"]
    lede = ("If your floor sits over someone else's ceiling, the rules change. Second-floor condos and "
            "many HOA communities across Tampa Bay carry sound-rating requirements, underlayment specs, "
            "and approval steps that have to be handled before install day — not discovered on it. "
            "Here's what to sort out first so your project doesn't get stopped halfway.")
    sections = '''
<h2>The thing most people miss: sound ratings</h2>
<p>In a multi-story building, your floor is your downstairs neighbor's ceiling. To keep footstep noise from traveling, condo associations almost always require a minimum sound rating on any hard-surface floor — quoted as <strong>IIC</strong> (Impact Insulation Class, footstep/impact noise) and sometimes <strong>STC</strong> (Sound Transmission Class, airborne noise). Common requirements land around <strong>IIC 50–55</strong>, and they're usually met with a rated acoustic underlayment under the floor.</p>

<h2>What that changes about your install</h2>
<ul>
<li><strong>Underlayment becomes mandatory, and specific.</strong> Not just any foam — a documented, rated acoustic underlayment (cork or a engineered acoustic mat) that meets the building's IIC number. That's a real line in the quote.</li>
<li><strong>It can steer the product.</strong> Some thin glue-down assemblies can't hit the rating without help; a floating floor over a rated mat often gets there more easily. We match the system to the rule.</li>
<li><strong>It affects height.</strong> The acoustic layer adds a few millimeters, which ripples into door clearance and transitions — worth knowing before, not after.</li>
</ul>

<h2>The approval steps to handle before install day</h2>
<ol>
<li><strong>Get the flooring rules in writing</strong> from the HOA or condo board — sound rating, approved hours, and whether a specific underlayment is named.</li>
<li><strong>Submit for architectural / board approval</strong> if required. Many associations want the product and underlayment spec approved before work starts; this can take days to weeks, so start early.</li>
<li><strong>Provide a certificate of insurance (COI).</strong> Most buildings require the installer's COI naming the association before anyone's allowed in. We provide ours on request.</li>
<li><strong>Confirm the logistics:</strong> elevator reservations and padding, allowed work hours and quiet hours, dumpster or debris-removal rules, and gate or fob access.</li>
</ol>

<table class="post-table">
<thead><tr><th>Requirement</th><th>Typical condo rule</th><th>Handle by</th></tr></thead>
<tbody>
<tr><td>Impact sound rating</td><td>IIC 50–55 minimum</td><td>Rated acoustic underlayment</td></tr>
<tr><td>Board / architectural approval</td><td>Product + underlayment pre-approved</td><td>Submit early — allow weeks</td></tr>
<tr><td>Installer COI</td><td>Naming the association</td><td>We provide on request</td></tr>
<tr><td>Work hours</td><td>Weekday daytime, quiet hours</td><td>Schedule around them</td></tr>
<tr><td>Access &amp; debris</td><td>Elevator padding, dumpster rules</td><td>Confirm before day one</td></tr>
</tbody>
</table>

<h2>Where this comes up most in our area</h2>
<p>It's a near-constant on the keys and waterfront towers — Siesta, Lido, Longboat, the downtown Sarasota and St. Pete high-rises, the Riviera Dunes condos in Palmetto — and in the second-floor stacks of master-planned communities across Lakewood Ranch and Wellen Park. We've worked most of them and we know the drill; we'll handle the association communication if you want us to.</p>

<div class="post-key-takeaway">
<strong>The Bottom Line</strong>
The floor itself is the easy part. In a condo or HOA community, the sound rating, the underlayment spec, the board approval, and the COI are what decide whether install day actually happens. Sort those out first — get the rules in writing, submit early, and confirm access — and the install goes exactly as planned. Walk in cold and the building can stop you at the door.
</div>
'''
    faqs = [
        ("What's IIC and why does my condo care about it?",
         "IIC — Impact Insulation Class — measures how well a floor blocks footstep and impact noise from reaching the unit below. Because your floor is your neighbor's ceiling, associations set a minimum (often IIC 50–55) to keep the peace between units. You meet it with a rated acoustic underlayment, which we spec to the building's exact requirement."),
        ("Will you deal with the HOA for me?",
         "Yes, if you'd like us to. We can pull the flooring rules, provide the product and underlayment specs the board needs to approve, supply our certificate of insurance, and schedule around the building's work-hour and access rules. Most of our condo clients hand us the gate code and the board contact and let us run it."),
    ]
    related = [
        ("/vinyl-plank-flooring/", "Vinyl Plank Flooring · Service Page"),
        ("/blog/short-term-rental-flooring-tampa-bay/", "Short-Term Rental Flooring Playbook"),
        ("/contact/#quote", "Start a Condo Flooring Quote"),
    ]
    guide_shell(g, lede, sections, faqs=faqs, related=related)


# ============================================================================
# GUIDES INDEX (hub)
# ============================================================================
def build_guides_index():
    URL = f"{SITE}/guides/"
    # NOTE: guide bodies in this file are legacy flooring content from another
    # project — rewrite for concrete/pavers BEFORE ever populating GUIDES.
    TITLE = f"Concrete & Paver Guides · Lakewood Ranch · {BUSINESS['name']}"
    DESC = clip_desc(
        "Plain-English concrete and paver decision guides from a working Lakewood Ranch crew — "
        "driveways, patios, pool decks, sealing, HOA/ARC approvals, and more."
    )
    schemas = [
        schema_breadcrumb([("Home", SITE + "/"), ("Guides", URL)]),
        schema_webpage(URL, TITLE, DESC),
        schema_local_business(URL, f"{BUSINESS['name']} Guides"),
    ]
    bc = breadcrumbs([("Home", "/"), ("Guides", None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Guides · Decisions, Not Sales Pitches</span>
    <h1>The calls that <em>cost the most to get wrong</em>.</h1>
    <p class="page-hero-sub">Short, honest guides to the flooring decisions where the money and the regret live &mdash; written by the crew that installs the floors, for {len(CITIES)} Tampa Bay cities. No fluff, no upsell.</p>
  </div>
</section>'''

    cards = ""
    for g in GUIDES:
        cards += f'''<a href="/guides/{g["slug"]}/" class="blog-card">
  <div class="blog-card-meta">
    <span>● {g["category"]}</span>
    <span>{g["date_published"][:7]}</span>
  </div>
  <h3>{g["title"]}</h3>
  <span class="blog-card-cta">Read the Guide</span>
</a>'''

    grid = f'''<section class="services-section">
  <div class="container-wide">
    <div class="section-head">
      <div class="section-head-num">01</div>
      <div class="section-head-meta">
        <span class="mono-label">{len(GUIDES)} Guides</span>
        <h2>Read before you <em>commit</em>.</h2>
        <div class="section-head-text"><p>Each guide takes one real decision apart &mdash; the trade-offs, the numbers, and the honest call. For pricing by city, see the <a href="/blog/">cost journal</a>; for terms, the <a href="/glossary/">glossary</a>.</p></div>
      </div>
    </div>
    <div class="blog-grid">{cards}</div>
  </div>
</section>'''

    body = "\n".join([hero, grid, f'<div class="container">{contact_banner()}</div>', final_cta()])
    head_html = head(TITLE, DESC, URL, og_image=og_url(path=OG_GUIDES), json_ld=schemas)
    write_page("guides/index.html", head_html, header(active="guides"), body, breadcrumbs_html=bc)
    print("Wrote /guides/index.html")


# ============================================================================
# GLOSSARY
# ============================================================================
def build_glossary():
    URL = f"{SITE}/glossary/"
    TITLE = "Flooring Glossary · Plain English · Napa's Flooring"  # 52
    DESC = clip_desc(
        f"{len(GLOSSARY)} flooring terms explained in plain English by Tampa Bay installers — "
        "acclimation, calcium chloride, lippage, SPC, wear layer, and the rest of the jargon, decoded."
    )

    defined_terms = {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "@id": URL + "#glossary",
        "name": "Napa's Flooring Glossary",
        "url": URL,
        "hasDefinedTerm": [
            {
                "@type": "DefinedTerm",
                "@id": f"{URL}#{term_id(t)}",
                "name": t,
                "description": d,
                "inDefinedTermSet": URL + "#glossary",
            }
            for t, d in GLOSSARY
        ],
    }
    schemas = [
        schema_breadcrumb([("Home", SITE + "/"), ("Glossary", URL)]),
        schema_webpage(URL, TITLE, DESC),
        defined_terms,
    ]
    bc = breadcrumbs([("Home", "/"), ("Glossary", None)])

    hero = f'''<section class="page-hero">
  <div class="page-hero-inner">
    <span class="mono-label">Glossary · {len(GLOSSARY)} Terms</span>
    <h1>Flooring jargon, <em>decoded</em>.</h1>
    <p class="page-hero-sub">Every term a Tampa Bay homeowner runs into on an estimate or a product spec sheet &mdash; in plain English, from the people who use the words on the jobsite.</p>
  </div>
</section>'''

    # A-Z quick jump
    letters = sorted({t[0].upper() for t, _ in GLOSSARY})
    jump = " · ".join(f'<a href="#{term_id(t)}" style="color:var(--orange-dark);font-weight:600">{t}</a>'
                      for t, _ in sorted(GLOSSARY, key=lambda x: x[0].lower()))

    rows = ""
    for t, d in sorted(GLOSSARY, key=lambda x: x[0].lower()):
        rows += f'''<div id="{term_id(t)}" style="padding:22px 0;border-bottom:1px solid var(--gray-border);scroll-margin-top:90px">
  <h3 style="font-size:1.2rem;margin-bottom:.5rem;color:var(--dark)">{t}</h3>
  <p style="margin:0;color:var(--text-light);line-height:1.65">{d}</p>
</div>'''

    body = f'''{hero}
<section>
  <div class="container">
    <article class="page-article" style="max-width:880px">
      <p class="post-lede">Flooring has its own vocabulary, and a lot of it shows up for the first time on your estimate &mdash; right when a wrong assumption gets expensive. This is every term we use with clients, defined the way we'd explain it standing in your living room. Jump to a term: {jump}.</p>
      <div>{rows}</div>
    </article>
  </div>
</section>

<div class="container">{contact_banner()}</div>

{final_cta()}'''

    head_html = head(TITLE, DESC, URL, og_image=og_url(path=OG_GLOSSARY), json_ld=schemas)
    write_page("glossary/index.html", head_html, header(active="guides"), body, breadcrumbs_html=bc)
    print("Wrote /glossary/index.html")


if __name__ == "__main__":
    print(f"Building {len(GUIDES)} guides…")
    build_guides()
    build_guides_index()
    build_glossary()
    print("Done: guides + glossary.")
