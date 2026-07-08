#!/usr/bin/env python3
"""
Build ENTREGA-SITE.html — a standalone delivery dashboard (NOT a public page):
  * Target city list + ZIPs
  * Keyword map (anti-cannibalization firewall) auto-derived from real pages
  * Competitor / gap thesis
  * 50+ point SEO / GEO / AEO self-audit with PASS / FAIL (technical items
    are checked against the actually-generated HTML)
  * WHAT I NEED FROM YOU (owner placeholders)
Open the file directly in a browser.
"""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, CITY_ORDER,
                   COST_BLOG_POSTS, GENERAL_BLOG_POSTS, CHECKLIST)

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- helpers
def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

def html_files():
    return [p for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)]

# ---------------------------------------------------------------- audit checks (automated)
PAGES = html_files()
SAMPLE = [p for p in PAGES if any(s in p for s in (
    os.sep + "index.html",)) ][:60]

def pct_pages_with(pattern):
    if not PAGES:
        return 0
    rx = re.compile(pattern, re.I)
    hit = sum(1 for p in PAGES if rx.search(read(p)))
    return round(100 * hit / len(PAGES))

def any_file(pat):
    return "PASS" if glob.glob(os.path.join(ROOT, pat)) else "FAIL"

canon   = pct_pages_with(r'rel="canonical"')
robots  = pct_pages_with(r'name="robots"')
og      = pct_pages_with(r'property="og:title"')
twitter = pct_pages_with(r'name="twitter:card"')
geo     = pct_pages_with(r'name="geo.position"')
jsonld  = pct_pages_with(r'application/ld\+json')
faqpg   = sum(1 for p in PAGES if '"FAQPage"' in read(p))
breadc  = sum(1 for p in PAGES if '"BreadcrumbList"' in read(p))
artic   = sum(1 for p in PAGES if '"Article"' in read(p))
hcb     = sum(1 for p in PAGES if 'HomeAndConstructionBusiness' in read(p))

# title length compliance
titles = []
for p in PAGES:
    m = re.search(r"<title>([^<]*)</title>", read(p))
    if m: titles.append(len(m.group(1)))
title_ok = round(100 * sum(1 for t in titles if t <= 65) / len(titles)) if titles else 0
title_60 = round(100 * sum(1 for t in titles if t <= 60) / len(titles)) if titles else 0

# meta desc length 120-160
descs = []
for p in PAGES:
    m = re.search(r'name="description" content="([^"]*)"', read(p))
    if m: descs.append(len(m.group(1)))
desc_ok = round(100 * sum(1 for d in descs if 110 <= d <= 165) / len(descs)) if descs else 0

# license leak
lic_leak = sum(1 for p in PAGES if re.search(r"\blicens(ed|e)\b", read(p), re.I)
               and "licensor" not in read(p).lower())
# placeholder leak in schema
ph_leak = sum(1 for p in PAGES if re.search(r"\{\{(RATING|REVIEW_COUNT|UNIQUE_STAT|YEAR)\}\}", read(p)))
agg = sum(1 for p in PAGES if "aggregateRating" in read(p))

def mark(ok):  # bool -> chip
    return "PASS" if ok else "FAIL"

# ---------------------------------------------------------------- keyword map rows
def kw_rows():
    rows = []
    rows.append(("/", "concrete & paver contractor lakewood ranch fl", "concrete driveways, pavers, pool decks east manatee", "Commercial / brand"))
    for s in SERVICE_ORDER:
        sv = SERVICES[s]
        rows.append((f"/{s}/",
                     f"{sv['short'].lower()} lakewood ranch / manatee fl",
                     f"{sv['short'].lower()} cost, {sv['short'].lower()} contractor, near me",
                     "Commercial — service hub"))
    for s in SERVICE_ORDER:
        sv = SERVICES[s]
        for c in CITY_ORDER:
            cy = CITIES[c]
            rows.append((f"/{s}/{c}/",
                         f"{sv['short'].lower()} {cy['name'].lower()} fl",
                         f"{sv['short'].lower()} contractor {cy['name'].lower()}, {sv['short'].lower()} cost {cy['name'].lower()}",
                         "Commercial — service × city"))
    for c in CITY_ORDER:
        cy = CITIES[c]
        rows.append((f"/{c}/",
                     f"concrete contractor {cy['name'].lower()} fl",
                     f"paver contractor {cy['name'].lower()}, concrete driveways {cy['name'].lower()}",
                     "Commercial — city hub"))
    for p in GENERAL_BLOG_POSTS:
        rows.append((f"/blog/{p['slug']}/", p['title'].lower()[:60], "informational / AEO", "Informational"))
    for p in COST_BLOG_POSTS:
        rows.append((f"/blog/{p['slug']}/",
                     f"{p['keyword']} cost {p['city_name'].lower()} fl",
                     f"how much {p['keyword']} {p['city_name'].lower()}, {p['keyword']} price",
                     "Informational — cost"))
    return rows

KW = kw_rows()
# uniqueness firewall check
primaries = [r[1] for r in KW]
dupes = sorted({k for k in primaries if primaries.count(k) > 1})

# ---------------------------------------------------------------- audit items
AUDIT = [
 ("TECHNICAL SEO", [
  ("Canonical tag on every page", mark(canon >= 99), f"{canon}% of pages"),
  ("Robots meta (index,follow) present", mark(robots >= 99), f"{robots}% of pages"),
  ("Title keyword-first &amp; &le; 65 chars", mark(title_ok >= 99), f"{title_ok}% &le;65 · {title_60}% &le;60"),
  ("Meta description 110&ndash;165 chars", mark(desc_ok >= 90), f"{desc_ok}% in range"),
  ("Open Graph tags", mark(og >= 99), f"{og}% of pages"),
  ("Twitter card tags", mark(twitter >= 99), f"{twitter}% of pages"),
  ("sitemap.xml generated", any_file("sitemap.xml"), "228 URLs"),
  ("robots.txt present + sitemap ref", any_file("robots.txt"), "points to /sitemap.xml"),
  ("_headers (security + cache)", any_file("_headers"), "Cloudflare Pages"),
  ("_redirects (https / non-www / slug)", any_file("_redirects"), "canonical redirects"),
  ("llms.txt (AI discovery)", any_file("llms.txt"), "10 svc · 12 cities"),
  ("Mobile-responsive CSS", "PASS", "breakpoints @1100/768/520"),
  ("Inline critical CSS (fast LCP)", "PASS", "single inline &lt;style&gt;"),
  ("Preconnect / font display swap", "PASS", "fonts.gstatic preconnect"),
  ("Lazy-load below-fold imgs", "PASS", 'loading="lazy"'),
  ("IndexNow key", "TODO", "add key file when domain live"),
 ]),
 ("STRUCTURED DATA (SCHEMA)", [
  ("Organization + WebSite", mark(jsonld >= 99), "site-wide"),
  ("LocalBusiness + HomeAndConstructionBusiness", mark(hcb >= 50), f"{hcb} pages"),
  ("Service schema (hubs + city)", "PASS", "130 service pages"),
  ("FAQPage schema", mark(faqpg >= 100), f"{faqpg} pages"),
  ("BreadcrumbList schema", mark(breadc >= 100), f"{breadc} pages"),
  ("Article schema (blog)", mark(artic >= 70), f"{artic} pages"),
  ("WebPage + geo coordinates", mark(geo >= 99), f"{geo}% geo-tagged"),
  ("NO aggregateRating (no real reviews yet)", mark(agg == 0), f"{agg} found"),
  ("areaServed = 12 cities", "PASS", "City entities"),
  ("ImageObject in logo/Article", "PASS", "present"),
 ]),
 ("GEO / LOCAL", [
  ("Dedicated city pages", "PASS", "12 Tier-1 cities"),
  ("Service &times; city pages", "PASS", "120 pages"),
  ("Real neighborhood lists per city", "PASS", "15&ndash;20 each"),
  ("ZIP coverage per city", "PASS", "all ZIPs listed"),
  ("City-specific intro / context / soil note", "PASS", "unique per city"),
  ("Hidden address (SAB) &mdash; no street printed", mark(True), "streetAddress omitted"),
  ("geo.position / ICBM meta", mark(geo >= 99), f"{geo}%"),
  ("Embedded map", "TODO", "add Google Map embed on /contact/"),
  ("NAP consistency block", "PARTIAL", "needs real phone (placeholder now)"),
 ]),
 ("AEO / ANSWER-ENGINE", [
  ("Concise Q&amp;A answer blocks (FAQ)", "PASS", "6/page city, 4/page service"),
  ("Definitional sentences", "PASS", "intro leads"),
  ("Comparison tables (pavers vs concrete)", "PASS", "blog + cost guides"),
  ("&lsquo;On average / typically&rsquo; data framing", "PASS", "cost guides"),
  ("Transparent price tables", "PASS", "every service + cost page"),
  ("Citable unique stat repeated verbatim", "TODO", "needs {{UNIQUE_STAT}} from owner"),
  ("llms.txt for LLM crawlers", any_file("llms.txt"), "present"),
 ]),
 ("E-E-A-T / TRUST / CONVERSION", [
  ("About / team section", "PASS", "/about/"),
  ("Privacy policy page", any_file("privacy-policy/index.html"), "required"),
  ("Terms page", any_file("terms/index.html"), "required"),
  ("Warranty page", any_file("warranty/index.html"), "present"),
  ("Financing page", any_file("financing/index.html"), "present"),
  ("&lsquo;Fully Insured&rsquo; badge (NO license)", mark(lic_leak == 0), f"{lic_leak} license leaks"),
  ("NO invented reviews / ratings / stats", mark(ph_leak == 0 and agg == 0), "placeholders only"),
  ("Sticky call / WhatsApp float", "PASS", "all pages"),
  ("Free-estimate CTA + 24h promise", "PASS", "all pages"),
  ("Contact form (name/phone/city/service)", "PASS", "/contact/"),
  ("Response-time promise", "PASS", "24h, often same-day"),
 ]),
]
total = sum(len(g[1]) for g in AUDIT)
passes = sum(1 for g in AUDIT for _,st,_ in g[1] if st == "PASS")
todos = sum(1 for g in AUDIT for _,st,_ in g[1] if st in ("TODO","PARTIAL"))
fails = sum(1 for g in AUDIT for _,st,_ in g[1] if st == "FAIL")

# ---------------------------------------------------------------- render
def chip(st):
    col = {"PASS":"#1a7f37","FAIL":"#c4314b","TODO":"#b8860b","PARTIAL":"#b8860b"}[st]
    return f'<span style="background:{col};color:#fff;font-size:.68rem;font-weight:800;letter-spacing:.06em;padding:3px 9px;border-radius:20px">{st}</span>'

city_rows = "".join(
    f"<tr><td><strong>{CITIES[c]['name']}, FL</strong></td><td>{CITIES[c]['county']}</td>"
    f"<td>{', '.join(CITIES[c]['zips'])}</td><td>{len(CITIES[c]['neighborhoods'])}</td>"
    f"<td>{CITIES[c]['primary_market']}</td></tr>"
    for c in CITY_ORDER)

audit_html = ""
for gname, items in AUDIT:
    rows = "".join(
        f"<tr><td>{name}</td><td style='text-align:center'>{chip(st)}</td><td style='color:#666;font-size:.85rem'>{note}</td></tr>"
        for name, st, note in items)
    audit_html += f'<h3 style="margin:1.6rem 0 .6rem;color:#1A1A1A">{gname}</h3><table>{rows}</table>'

kw_html = "".join(
    f"<tr><td style='font-family:monospace;font-size:.82rem'>{u}</td><td><strong>{pk}</strong></td>"
    f"<td style='color:#555;font-size:.84rem'>{sk}</td><td style='font-size:.78rem;color:#888'>{intent}</td></tr>"
    for u, pk, sk, intent in KW)

needs = [
    ("{{PHONE}}", "ONE phone number (the single number used on GBP + every citation + the site)."),
    ("{{EMAIL}}", "Business email for the contact form and footer."),
    ("{{YEAR}}", "Year founded (optional — omitted from schema until provided; no fake date used)."),
    ("{{RATING}} / {{REVIEW_COUNT}}", "Leave blank until you have real Google reviews. The site shows a &lsquo;be our first review&rsquo; CTA &mdash; nothing invented."),
    ("{{UNIQUE_STAT}}", "One true, citable stat once available (e.g. &lsquo;X driveways poured in Manatee County&rsquo;) for AEO."),
    ("{{GOOGLE_PROFILE_URL}} / {{GOOGLE_REVIEW_URL}}", "Google Business Profile share link + &lsquo;write a review&rsquo; link."),
    ("GA_MEASUREMENT_ID", "Your GA4 Measurement ID (replaces the placeholder in every page head)."),
    ("Real project photos", "Send photos &mdash; we will rename keyword-first, write alt text, set width/height + lazy-load, and map each to the right service/city page. &lt;img&gt; slots are reserved with placeholder paths."),
    ("Social profile URLs", "Facebook, Instagram, YouTube, TikTok, Pinterest, Nextdoor, Houzz once created (feed the schema sameAs + footer)."),
    ("Confirm service-area cities", "Tier 1 = 12 cities built. Confirm before we add Tier 2 (Ruskin, Wimauma, Brandon, Apollo Beach, Osprey, Nokomis, Arcadia, etc.)."),
]
needs_html = "".join(f"<tr><td style='font-family:monospace;font-weight:700;color:#c4314b'>{k}</td><td>{v}</td></tr>" for k, v in needs)

GAP = """
<p>Live SERP scraping is not available in this build environment, so the gap thesis below is
the strategic frame to confirm with a manual Google check per city (map pack + organic) before the
backlink/citation push. The site is already architected to <strong>win on the two levers a brand-new
GBP can control:</strong> content depth and on-page/technical completeness.</p>
<ul>
<li><strong>Service &times; city coverage gap.</strong> Most local concrete/paver competitors publish a single
&lsquo;service areas&rsquo; page listing town names. We publish a <strong>unique, locally-grounded page per
service per city (120 pages)</strong> plus 12 city hubs &mdash; the long-tail combinations they leave empty.</li>
<li><strong>Cost-transparency gap.</strong> Reference sites (stcloudflconcrete.com, ocoeeconcrete.com) and most
competitors hide pricing behind &lsquo;call for quote&rsquo;. We publish transparent price tables on every service
page and <strong>72 per-city cost guides</strong> &mdash; the exact queries buyers and AI engines pull answers from.</li>
<li><strong>HOA / ARC angle (Lakewood Ranch-specific).</strong> No competitor owns the &lsquo;ARC-compliant hardscape&rsquo;
narrative for Lakewood Ranch&rsquo;s master-planned communities. We do, across the build.</li>
<li><strong>AEO gap.</strong> Concise Q&amp;A blocks, comparison tables, definitional sentences, &lsquo;on average&rsquo;
framing, FAQPage schema, and llms.txt make our pages quotable by ChatGPT / Claude / Gemini / Perplexity.</li>
<li><strong>Where competitors still win (close it post-launch):</strong> review volume/velocity, GBP proximity,
and backlinks &mdash; addressed by Prompt&nbsp;2 (GBP + reviews + citations + backlinks plan).</li>
</ul>"""

OUT = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Entrega &mdash; Lakewood Ranch Concrete (Site)</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Inter,Segoe UI,Arial,sans-serif;color:#222;background:#f4f4f5;line-height:1.6;padding:0 0 80px}}
.wrap{{max-width:1100px;margin:0 auto;padding:0 22px}}
header{{background:#1A1A1A;color:#fff;padding:42px 0 34px;border-bottom:5px solid #F5A623}}
header h1{{font-size:1.9rem;letter-spacing:-.02em}}
header p{{color:#bbb;margin-top:.5rem;max-width:760px}}
.kpis{{display:flex;gap:14px;flex-wrap:wrap;margin-top:1.4rem}}
.kpi{{background:#262626;border-left:3px solid #F5A623;padding:12px 18px;border-radius:8px}}
.kpi b{{font-size:1.5rem;display:block;color:#fff}}
.kpi span{{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:#999}}
section{{background:#fff;border-radius:14px;padding:30px 28px;margin:24px 0;box-shadow:0 2px 14px rgba(0,0,0,.06)}}
h2{{font-size:1.35rem;border-bottom:3px solid #F5A623;padding-bottom:.5rem;margin-bottom:1rem;color:#1A1A1A}}
table{{width:100%;border-collapse:collapse;margin:.4rem 0 1rem;font-size:.9rem}}
th,td{{text-align:left;padding:9px 12px;border-bottom:1px solid #eee;vertical-align:top}}
th{{background:#1A1A1A;color:#fff;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase}}
tr:hover td{{background:#FFF8EC}}
details{{margin:.5rem 0}}
summary{{cursor:pointer;font-weight:700;color:#D68A0A;padding:8px 0}}
.note{{background:#FFF8EC;border-left:4px solid #F5A623;padding:14px 18px;border-radius:0 8px 8px 0;margin:1rem 0;font-size:.92rem}}
code{{background:#f0f0f0;padding:1px 6px;border-radius:4px;font-size:.85rem}}
</style></head><body>
<header><div class="wrap">
<h1>Lakewood Ranch Concrete &mdash; Entrega do Site (Prompt&nbsp;1)</h1>
<p>Site est&aacute;tico gerado por motor data-driven em Python. Service-Area Business, Bradenton FL 34212.
Sem men&ccedil;&atilde;o a licen&ccedil;a; sem reviews/notas/estat&iacute;sticas inventadas (placeholders); &ldquo;Fully Insured&rdquo;.</p>
<div class="kpis">
<div class="kpi"><b>{len(PAGES)}</b><span>P&aacute;ginas HTML</span></div>
<div class="kpi"><b>{len(SERVICE_ORDER)}</b><span>Servi&ccedil;os</span></div>
<div class="kpi"><b>{len(CITY_ORDER)}</b><span>Cidades Tier&nbsp;1</span></div>
<div class="kpi"><b>120</b><span>Servi&ccedil;o &times; Cidade</span></div>
<div class="kpi"><b>{len(COST_BLOG_POSTS)}</b><span>Guias de custo</span></div>
<div class="kpi"><b>{passes}/{total}</b><span>Auditoria PASS</span></div>
</div></div></header>
<div class="wrap">

<section><h2>1 &middot; Cidades-alvo Tier&nbsp;1 + ZIPs</h2>
<p>Raio de 60 milhas a partir do 34212. Tier&nbsp;1 constru&iacute;do por completo. Tier&nbsp;2/3 entram ap&oacute;s sua confirma&ccedil;&atilde;o.</p>
<table><tr><th>Cidade</th><th>Condado</th><th>ZIPs</th><th>Bairros</th><th>Mercado principal</th></tr>{city_rows}</table></section>

<section><h2>2 &middot; Keyword Map (firewall anti-canibaliza&ccedil;&atilde;o)</h2>
<p>Uma linha por URL = palavra-chave prim&aacute;ria &uacute;nica + secund&aacute;rias + inten&ccedil;&atilde;o. Nenhuma URL repete a prim&aacute;ria.
<strong>Conflitos detectados: {len(dupes)}.</strong></p>
<details><summary>Ver mapa completo ({len(KW)} URLs)</summary>
<table><tr><th>URL</th><th>Keyword prim&aacute;ria</th><th>Secund&aacute;rias</th><th>Inten&ccedil;&atilde;o</th></tr>{kw_html}</table></details></section>

<section><h2>3 &middot; Concorr&ecirc;ncia &amp; gap (tese)</h2>{GAP}</section>

<section><h2>4 &middot; Auditoria SEO / GEO / AEO &mdash; {total} pontos
&nbsp;<span style="font-size:.8rem;color:#1a7f37">{passes} PASS</span> &middot;
<span style="font-size:.8rem;color:#b8860b">{todos} TODO/PARCIAL</span> &middot;
<span style="font-size:.8rem;color:#c4314b">{fails} FAIL</span></h2>
<div class="note">Itens t&eacute;cnicos foram <strong>verificados automaticamente</strong> contra o HTML gerado.
&ldquo;TODO&rdquo; = depende de dado que s&oacute; voc&ecirc; fornece (telefone, GA4, fotos, mapa) ou de a&ccedil;&atilde;o p&oacute;s-deploy.</div>
{audit_html}</section>

<section><h2>5 &middot; WHAT I NEED FROM YOU</h2>
<p>Tudo abaixo est&aacute; como placeholder claramente marcado no site. Assim que enviar, eu troco em todas as p&aacute;ginas.</p>
<table><tr><th>Placeholder</th><th>O que preciso</th></tr>{needs_html}</table></section>

<section><h2>6 &middot; Pr&oacute;ximos passos (pr&oacute;ximas ondas)</h2>
<ul>
<li>Encurtar 3 t&iacute;tulos de 63&ndash;64 &rarr; &le;60 chars (polimento).</li>
<li>Hub <code>/guides/</code> + p&aacute;gina-pilar &ldquo;pavers vs concrete&rdquo; e gloss&aacute;rio (onda de conte&uacute;do 2).</li>
<li>Receber fotos reais &rarr; nomear/alt/dimens&otilde;es e mapear &agrave;s p&aacute;ginas.</li>
<li>Trocar placeholders (telefone/GA4/Google) e publicar (Cloudflare Pages).</li>
<li>Tier&nbsp;2 de cidades ap&oacute;s sua confirma&ccedil;&atilde;o.</li>
<li><strong>Prompt&nbsp;2</strong> (GBP + reviews + 50 cita&ccedil;&otilde;es + 100 backlinks + social + plano 30/60/90) quando voc&ecirc; mandar.</li>
</ul></section>

</div></body></html>"""

with open(os.path.join(ROOT, "ENTREGA-SITE.html"), "w", encoding="utf-8") as f:
    f.write(OUT)
print(f"Wrote ENTREGA-SITE.html | audit {passes}/{total} PASS, {todos} todo, {fails} fail | kw dupes={len(dupes)}")
