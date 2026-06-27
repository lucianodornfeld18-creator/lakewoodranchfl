#!/usr/bin/env python3
"""
Lakewood Ranch Concrete — Master Data Module
Concrete & paver contractor · Service-Area Business · Bradenton/Lakewood Ranch FL.
Service entries live in _svc_part1..4.py; city entries in _cities_part1..2.py.
Used by every _build_*.py script.

CRITICAL CONSTRAINTS (per build brief):
  * NEW business — NEVER invent reviews, ratings, stats, years, or testimonials.
    Unknowns are clearly-labeled {{PLACEHOLDERS}} listed in WHAT-I-NEED-FROM-YOU.
  * NEVER mention any license / license number. "Insured" / "Fully Insured" only.
"""


# ============================================================================
# META-DESCRIPTION HELPER — trim at a word boundary, never mid-word.
# ============================================================================
def clip_desc(s, n=155):
    s = " ".join(str(s).split())
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(" ,·-") + "…"


# ============================================================================
# BUSINESS IDENTITY  — placeholders for everything the owner must supply.
# ============================================================================
BUSINESS = {
    "name": "Lakewood Ranch Concrete",
    "legal_name": "Lakewood Ranch Concrete LLC",
    "domain": "lakewoodranchconcretefl.com",
    # ---- PLACEHOLDERS (owner-supplied) ----
    "phone": "+19413524308",
    "phone_display": "(941) 352-4308",
    "phone_tel": "+19413524308",
    "email": "lakewoodranchconcrete@gmail.com",
    "year_founded": "{{YEAR}}",
    "rating": "{{RATING}}",
    "review_count": "{{REVIEW_COUNT}}",
    "unique_stat_number": "{{UNIQUE_STAT}}",
    "unique_stat_full": "{{UNIQUE_STAT}}",
    # ---- Fixed / safe to publish ----
    "street": "",                      # SAB — address HIDDEN, never printed
    "city": "Bradenton",
    "city_slug": "bradenton",
    "state": "FL",
    "state_long": "Florida",
    "zip": "34212",
    "county": "Manatee County",
    "country": "US",
    "lat": "27.4806",
    "lng": "-82.4569",
    "tagline": "Poured right. Built to last.",
    "tagline_long": "East Manatee&rsquo;s concrete &amp; paver crew — driveways, patios, pool decks, and hardscape installed to last in the Florida sun, from Lakewood Ranch to the coast.",
    "checklist_name": "Lakewood Ranch Concrete 42-Point Install Standard",
    "checklist_points": 42,
    "guarantee": "Written workmanship warranty on every pour and every paver install.",
    "response_time": "Free estimate within 24 hours, often same-day.",
    # ---- Profiles (fill when live) ----
    "google_profile": "{{GOOGLE_PROFILE_URL}}",
    "google_review_url": "{{GOOGLE_REVIEW_URL}}",
    "facebook": "https://www.facebook.com/profile.php?id=61591647230902",
    "instagram": "https://www.instagram.com/lakewoodranchconcrete/",
    "yelp": "",
    "thumbtack": "",
    "angi": "",
    "houzz": "",
    "pinterest": "",
    "bbb": "",
    "hours": [
        ("Monday", "07:00", "18:00"),
        ("Tuesday", "07:00", "18:00"),
        ("Wednesday", "07:00", "18:00"),
        ("Thursday", "07:00", "18:00"),
        ("Friday", "07:00", "18:00"),
        ("Saturday", "08:00", "15:00"),
        ("Sunday", "Closed", "Closed"),
    ],
    # Toggles for the engine — NEW business has no reviews/ratings yet.
    "has_reviews": False,
}

WA_LINK = f"https://wa.me/{BUSINESS['phone'].lstrip('+')}?text=Hi%20Lakewood%20Ranch%20Concrete%2C%20I%27d%20like%20a%20free%20estimate."
SMS_LINK = f"sms:{BUSINESS['phone']}?body=Hi%20Lakewood%20Ranch%20Concrete%2C%20I%27d%20like%20a%20free%20estimate."
TEL_LINK = f"tel:{BUSINESS['phone']}"


# ============================================================================
# CITIES — Tier 1 (merged from city part files)
# ============================================================================
from _cities_part1 import CITIES as _c1
from _cities_part2 import CITIES as _c2
from _cities_part3 import CITIES as _c3
from _cities_part4 import CITIES as _c4
CITIES = {**_c1, **_c2, **_c3, **_c4}

CITY_ORDER = [
    # Tier 1 — core Manatee / Sarasota / Charlotte + south Hillsborough
    "lakewood-ranch", "bradenton", "parrish", "palmetto", "ellenton", "sarasota",
    "venice", "north-port", "port-charlotte", "punta-gorda", "riverview", "sun-city-center",
    # Tier 2 — extended reach (Tampa Bay, coastal islands, DeSoto, east Manatee)
    "tampa", "st-petersburg", "brandon", "ruskin", "wimauma", "apollo-beach",
    "osprey", "nokomis", "arcadia", "anna-maria", "longboat-key", "myakka-city",
]
CITIES = {k: CITIES[k] for k in CITY_ORDER if k in CITIES}


# ============================================================================
# SERVICES — 10 core hubs (merged from service part files)
# ============================================================================
from _svc_part1 import SERVICES as _s1
from _svc_part2 import SERVICES as _s2
from _svc_part3 import SERVICES as _s3
from _svc_part4 import SERVICES as _s4
SERVICES = {**_s1, **_s2, **_s3, **_s4}

SERVICE_ORDER = [
    "concrete-driveways", "concrete-patios", "concrete-pool-decks",
    "stamped-concrete", "concrete-slabs", "concrete-resurfacing",
    "paver-driveways", "paver-patios-walkways", "pool-deck-pavers", "paver-sealing",
]
SERVICES = {k: SERVICES[k] for k in SERVICE_ORDER if k in SERVICES}

SERVICE_GROUPS = [
    ("Concrete", ["concrete-driveways", "concrete-patios", "concrete-pool-decks",
                  "stamped-concrete", "concrete-slabs", "concrete-resurfacing"]),
    ("Pavers &amp; Hardscape", ["paver-driveways", "paver-patios-walkways",
                                "pool-deck-pavers", "paver-sealing"]),
]


# ============================================================================
# 42-POINT INSTALL STANDARD — concrete & paver workflow (6 × 7 = 42)
# ============================================================================
CHECKLIST = {
    "name": "Lakewood Ranch Concrete 42-Point Install Standard",
    "points": 42,
    "categories": [
        {
            "title": "Site Survey &amp; Layout",
            "icon": "01",
            "items": [
                "On-site measure of the full pour or paver footprint",
                "Soil and subgrade condition assessed for sand, muck, or fill",
                "Drainage and slope direction mapped away from the home",
                "Existing slab, driveway, or deck inspected for tie-in points",
                "Utility, irrigation, and sprinkler lines located and flagged",
                "HOA / ARC color, paver, and finish restrictions reviewed",
                "Access path for trucks, mixers, and equipment confirmed",
            ],
        },
        {
            "title": "Excavation &amp; Base Prep",
            "icon": "02",
            "items": [
                "Existing surface demoed and hauled off as scoped",
                "Subgrade excavated to design depth for slab or paver base",
                "Soft or organic soil cut out and replaced with clean fill",
                "Compactable base (crushed limerock / road base) brought in",
                "Base compacted in lifts with a plate compactor to spec",
                "Final grade and slope re-checked for positive drainage",
                "Edge lines, depth, and pad dimensions verified before forming",
            ],
        },
        {
            "title": "Forming, Steel &amp; Reinforcement",
            "icon": "03",
            "items": [
                "Forms set, staked, and leveled to the planned slope",
                "Fiber mesh and / or rebar / wire reinforcement placed",
                "Rebar chaired up off the base so it sits inside the slab",
                "Control-joint and expansion-joint layout planned",
                "Thickened edges formed where load demands it",
                "Vapor barrier installed under interior-adjacent slabs",
                "Forms and reinforcement photographed before the pour",
            ],
        },
        {
            "title": "Pour, Finish &amp; Pavers",
            "icon": "04",
            "items": [
                "Concrete mix and PSI confirmed for the application",
                "Pour placed, screeded, and floated to grade",
                "Specified finish applied — broom, stamp, or smooth",
                "Color, release, or stain applied per the approved sample",
                "Pavers laid to pattern on a screeded sand setting bed",
                "Edge restraints installed to lock the paver field",
                "Soldier course / borders set straight and consistent",
            ],
        },
        {
            "title": "Joints, Curing &amp; Sand",
            "icon": "05",
            "items": [
                "Control joints cut or tooled at engineered spacing",
                "Expansion joints set against the house and fixed structures",
                "Curing compound or wet-cure applied to the fresh slab",
                "Pavers compacted into the bed with a plate compactor",
                "Polymeric joint sand swept in, compacted, and activated",
                "Slab and paver edges cleaned of slurry and excess sand",
                "Cure / set time communicated before foot or vehicle traffic",
            ],
        },
        {
            "title": "Cleanup, Seal &amp; Walkthrough",
            "icon": "06",
            "items": [
                "Site cleaned, forms pulled, and debris hauled away",
                "Surface pressure-washed and inspected when sealing is scoped",
                "Sealer applied evenly at the correct cure window",
                "Final slope and drainage confirmed with a hose test",
                "Walkthrough with the homeowner — full surface inspected",
                "Care, curing, and maintenance guidance handed over",
                "Written workmanship warranty issued and job photos sent",
            ],
        },
    ],
}
_total = sum(len(c["items"]) for c in CHECKLIST["categories"])
assert _total == 42, f"Checklist totals to {_total}, not 42 — fix the lists in _data.py"


# ============================================================================
# REVIEWS — NEW business: NONE invented. Empty until the owner supplies real
# Google reviews. The engine renders a "be the first" CTA instead of cards.
# ============================================================================
REVIEWS = []


# ============================================================================
# BLOG — general posts (concrete/paver topics) + per-city cost guides.
# ============================================================================
GENERAL_BLOG_POSTS = [
    {
        "slug": "pavers-vs-concrete-driveway-florida",
        "title": "Pavers vs. Concrete Driveway in Florida: The Honest 2026 Breakdown",
        "meta_desc": "Pavers or poured concrete for a Florida driveway? Real cost, lifespan, repair, resale, and HOA factors compared for Lakewood Ranch and Manatee/Sarasota homes.",
        "category": "Compare",
        "primary_city": "Lakewood Ranch",
        "primary_service": "paver-driveways",
        "word_target": 2300,
        "topic": "pavers_vs_concrete",
        "date_published": "2026-05-12",
        "date_modified": "2026-05-12",
    },
    {
        "slug": "why-florida-concrete-cracks-and-how-to-prevent-it",
        "title": "Why Florida Concrete Cracks — and How a Good Pour Prevents It",
        "meta_desc": "Sandy soil, heat, and skipped joints crack Gulf Coast concrete. What actually causes driveway and slab cracks in Manatee County, and the prep that stops them.",
        "category": "How It Works",
        "primary_city": "Bradenton",
        "primary_service": "concrete-driveways",
        "word_target": 2100,
        "topic": "cracking_guide",
        "date_published": "2026-04-18",
        "date_modified": "2026-04-18",
    },
    {
        "slug": "best-pool-deck-surface-florida-heat",
        "title": "The Coolest Pool Deck Surfaces for Florida Heat (2026 Guide)",
        "meta_desc": "Travertine, pavers, or Kool-Deck resurfacing — which pool deck stays coolest underfoot in the Florida sun? Slip, heat, and cost compared for Suncoast homes.",
        "category": "Buyer&rsquo;s Guide",
        "primary_city": "Sarasota",
        "primary_service": "pool-deck-pavers",
        "word_target": 2200,
        "topic": "pool_deck_guide",
        "date_published": "2026-03-22",
        "date_modified": "2026-03-22",
    },
    {
        "slug": "stamped-concrete-patio-ideas-lakewood-ranch",
        "title": "Stamped Concrete Patio Ideas That Pass HOA Review in Lakewood Ranch",
        "meta_desc": "Stamped concrete patterns, colors, and finishes that look high-end and clear ARC approval in Lakewood Ranch and East Manatee master-planned communities.",
        "category": "Design",
        "primary_city": "Lakewood Ranch",
        "primary_service": "stamped-concrete",
        "word_target": 2050,
        "topic": "stamped_ideas",
        "date_published": "2026-02-20",
        "date_modified": "2026-02-20",
    },
    {
        "slug": "paver-sealing-resanding-florida-guide",
        "title": "Paver Sealing &amp; Re-Sanding in Florida: When, Why, and What It Costs",
        "meta_desc": "How often to seal pavers in Florida, why joints wash out, and what polymeric re-sanding and sealing actually cost on the Suncoast. An installer&rsquo;s straight answer.",
        "category": "Maintenance",
        "primary_city": "Bradenton",
        "primary_service": "paver-sealing",
        "word_target": 2050,
        "topic": "sealing_guide",
        "date_published": "2026-01-24",
        "date_modified": "2026-01-24",
    },
]

# Per-(service, city) cost guides — restricted to high-value priority services
# so we publish rich, differentiated pages instead of 120 thin near-duplicates.
COST_PRIORITY_SERVICES = [
    "concrete-driveways", "paver-driveways", "concrete-patios",
    "concrete-pool-decks", "pool-deck-pavers", "stamped-concrete",
]
COST_BLOG_POSTS = []
for svc_slug in COST_PRIORITY_SERVICES:
    svc = SERVICES[svc_slug]
    keyword = svc["short"].lower()
    for city_slug, city in CITIES.items():
        COST_BLOG_POSTS.append({
            "slug": f"{svc_slug}-cost-{city_slug}",
            "service_slug": svc_slug,
            "city_slug": city_slug,
            "service_name": svc["name"],
            "service_short": svc["short"],
            "city_name": city["name"],
            "keyword": keyword,
            "title": f"{svc['short']} Cost in {city['name']}, FL (2026)",
            "meta_desc": clip_desc(
                f"What {keyword} actually costs in {city['name']}, FL in 2026 — "
                f"transparent rates by finish and material, real timelines, and "
                f"{city['name']}-specific factors. Free estimate from a local crew."
            ),
            "category": "Pricing",
            "primary_city": city["name"],
            "primary_service": svc_slug,
            "word_target": 2050,
            "topic": "cost_guide",
            "date_published": "2026-01-15",
            "date_modified": "2026-01-15",
        })


# ============================================================================
# GUIDES + GLOSSARY — reserved for a later content wave (kept empty so the
# engine, sitemap, and content-map run cleanly without thin/irrelevant pages).
# ============================================================================
GUIDES = []
GLOSSARY = []


# ============================================================================
# SHARED COPY — NO invented stats. Badges are factual/process-based only.
# ============================================================================
HERO_TRUST_BADGES = [
    "Fully Insured",
    "Free Estimates",
    "Lakewood Ranch &amp; Manatee / Sarasota",
    "Free estimate in 24 hours",
    "42-Point Install Standard",
]

WHY_US_POINTS = [
    {
        "num": "01",
        "title": "Local crew, real East Manatee addresses.",
        "body": "We&rsquo;re based in east Bradenton in the 34212 ZIP, bordering Lakewood Ranch &mdash; not driving in from another county. We know the soil, the HOA / ARC rules, and the community access protocols across Manatee and north Sarasota because we pour and pave here every week.",
    },
    {
        "num": "02",
        "title": "Base prep we won&rsquo;t shortcut.",
        "body": "Most failed Florida concrete and settled pavers trace back to a skipped base. We excavate to depth, cut out soft soil, bring in compactable base, and compact it in lifts before anything is poured or laid. The prep that prevents the crack is the prep nobody sees.",
    },
    {
        "num": "03",
        "title": "Engineered joints &amp; reinforcement.",
        "body": "Concrete moves with Florida heat. We plan control and expansion joints at engineered spacing and place fiber mesh, wire, or rebar to spec, so the slab cracks where we tell it to &mdash; in the joint &mdash; instead of across your new driveway.",
    },
    {
        "num": "04",
        "title": "Transparent pricing &mdash; no &lsquo;call for quote&rsquo;.",
        "body": "Our pricing is published on this site by finish and material type. You get a written, line-itemized estimate within 24 hours of the on-site measure. We don&rsquo;t pad, we don&rsquo;t bait-and-switch, and change orders only happen when the scope genuinely changes.",
    },
    {
        "num": "05",
        "title": "HOA &amp; ARC-ready hardscape.",
        "body": "Lakewood Ranch and the master-planned communities around it have architectural review rules on driveway materials, paver colors, and finishes. We build to what passes, document the spec, and can handle the ARC submittal package so your project clears review the first time.",
    },
    {
        "num": "06",
        "title": "Written workmanship warranty &mdash; and Fully Insured.",
        "body": "Every pour and every paver install carries a written workmanship warranty on our labor, and we&rsquo;re fully insured. You keep a copy of the warranty and the job photos, and we honor it.",
    },
]

PROCESS_STEPS = [
    {"num": "01", "title": "Measure &amp; Quote", "body": "We measure on site, check soil and drainage, review any HOA / ARC rules, talk through finishes, and email a written, line-itemized quote within 24 hours."},
    {"num": "02", "title": "Prep &amp; Form", "body": "We excavate, cut out soft soil, bring in and compact the base, set forms to the right slope, and place reinforcement &mdash; the work that decides whether the surface lasts."},
    {"num": "03", "title": "Pour or Pave", "body": "Same crew start to finish. Concrete poured, screeded, and finished to your chosen texture; or pavers laid to pattern with edge restraints and polymeric joint sand. Daily progress photos."},
    {"num": "04", "title": "Cure, Seal &amp; Walkthrough", "body": "We cut joints, cure or seal the surface, clean the site, hose-test the drainage, walk it with you, and hand over the care guide plus your written workmanship warranty."},
]


# ============================================================================
# SOCIAL + DIRECTORY NETWORK (for footer icons + /directories/ page)
# ============================================================================
SOCIAL_LINKS = [
    ("Facebook", BUSINESS["facebook"]),
    ("Instagram", BUSINESS["instagram"]),
]
# Live profile links (only the ones we actually have go on the page as links)
LIVE_PROFILES = [
    ("Facebook", BUSINESS["facebook"]),
    ("Instagram", BUSINESS["instagram"]),
    ("Google Business Profile", BUSINESS["google_profile"]),
]
# Citation/listing network we are (or will be) listed on — builds the hub page
DIRECTORY_NETWORK = [
    "Google Business Profile", "Bing Places", "Apple Maps", "Yelp", "Facebook",
    "Instagram", "Houzz", "Angi", "Thumbtack", "HomeAdvisor", "Porch", "BuildZoom",
    "Nextdoor", "Better Business Bureau", "Manta", "Hotfrog", "Yellow Pages",
    "Foursquare", "MerchantCircle", "Brownbook", "Cylex", "Pinterest", "Trustpilot",
    "Alignable", "ChamberofCommerce.com", "Superpages", "Citysearch", "Local.com",
    "EZlocal", "ShowMeLocal", "iBegin", "2FindLocal", "Bizapedia", "The Blue Book Network",
]
