"""Shared layout pieces for the CIRTEC AI new pages.

Pages are written as static HTML with clean URLs (folder/index.html) so the
structure maps 1:1 onto the Astro routes of the live site.
"""

LIVE = "https://www.cirtec.ai"
PHONE = "+65 9787 1732"
PHONE_TEL = "+6597871732"
EMAIL = "sales@cirtec.ai"

# Lucide-style stroke icons (24x24)
_P = {
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "gauge": '<path d="M12 14l4-4"/><path d="M3.3 19a9 9 0 1 1 17.4 0"/>',
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "sliders": '<path d="M4 21v-7"/><path d="M4 10V3"/><path d="M12 21v-9"/><path d="M12 8V3"/><path d="M20 21v-5"/><path d="M20 12V3"/><path d="M1 14h6"/><path d="M9 8h6"/><path d="M17 16h6"/>',
    "sparkle": '<path d="M12 3l1.9 5.6L19.5 10l-5.6 1.9L12 17.5l-1.9-5.6L4.5 10l5.6-1.4z"/><path d="M19 17l.8 2.2L22 20l-2.2.8L19 23l-.8-2.2L16 20l2.2-.8z"/>',
    "cam": '<path d="M2 8h13l5-3v14l-5-3H2z"/><circle cx="8" cy="12" r="2.5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>',
    "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="3"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
    "chef": '<path d="M6 13.9A4 4 0 0 1 7.4 6a5 5 0 0 1 9.2 0A4 4 0 0 1 18 13.9V21H6z"/><path d="M6 17h12"/>',
    "tag": '<path d="M12.6 2.6A2 2 0 0 0 11.2 2H4a2 2 0 0 0-2 2v7.2a2 2 0 0 0 .6 1.4l8.7 8.7a2.4 2.4 0 0 0 3.4 0l6.6-6.6a2.4 2.4 0 0 0 0-3.4z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "code": '<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>',
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10a7 7 0 0 1-14 0"/><path d="M12 17v5"/>',
    "cart": '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2 2h3l2.7 12.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
    "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8"/><path d="M8 17h5"/>',
    "video": '<rect x="2" y="5" width="14" height="14" rx="2"/><path d="m16 10 6-3v10l-6-3"/>',
    "db": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5"/><path d="M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 16v-5"/><path d="M12 16V8"/><path d="M17 16v-9"/>',
    "layout": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/>',
    "orbit": '<circle cx="12" cy="12" r="3"/><path d="M3 12a9 4 0 1 0 18 0 9 4 0 1 0-18 0"/>',
    "ticket": '<path d="M2 9a3 3 0 0 1 0 6v2a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-2a3 3 0 0 1 0-6V7a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"/><path d="M13 5v2"/><path d="M13 17v2"/><path d="M13 11v2"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.7-9h1.8a4.5 4.5 0 1 1 0 9z"/>',
    "plug": '<path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "grad": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "menu": '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    "thermo": '<path d="M14 4v10.5a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0z"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
    "msg": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M8 10h.01M16 10h.01M12 10h.01M8 14h.01M16 14h.01M12 14h.01"/>',
    "server": '<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><path d="M6 6h.01"/><path d="M6 18h.01"/>',
    "battery": '<rect x="2" y="7" width="16" height="10" rx="2"/><path d="M22 11v2"/><path d="M6 11v2"/><path d="M10 11v2"/>',
    "fan": '<path d="M10.8 9.9C9.3 6 10 2 13 2c2.5 0 3 2.5 1.2 6"/><path d="M14.1 10.8C18 9.3 22 10 22 13c0 2.5-2.5 3-6 1.2"/><path d="M13.2 14.1C14.7 18 14 22 11 22c-2.5 0-3-2.5-1.2-6"/><path d="M9.9 13.2C6 14.7 2 14 2 11c0-2.5 2.5-3 6-1.2"/><circle cx="12" cy="12" r="2"/>',
    "cpu": '<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
    "migrate": '<path d="M3 7h13l-3-3"/><path d="M21 17H8l3 3"/>',
    "hardhat": '<path d="M2 18h20"/><path d="M4 18v-3a8 8 0 0 1 16 0v3"/><path d="M10 7V5h4v2"/>',
    "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.1 10.4A6 6 0 1 1 10.3 18"/><path d="M7 6h1v4"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')


WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.7 11.7 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg>')


def nav(active, apps_by_domain):
    def li(key, inner):
        cls = ' class="active"' if key == active else ""
        return f'<li{cls}>{inner}</li>'

    energy_dd = '''
      <div class="dropdown wide">
        <div class="dd-label">Energy · Platforms</div>
        <a href="/energy-infrastructure/#measure"><strong>Measure</strong><span>See where your energy goes</span></a>
        <a href="/energy-infrastructure/#act"><strong>Improve</strong><span>Fix it on the equipment you have</span></a>
        <a href="/energy-infrastructure/#transform"><strong>Add AI</strong><span>Add AI once the savings are in</span></a>
        <a href="/energy-infrastructure/#eui-check"><strong>Free energy check</strong><span>Two numbers from your bills, one minute</span></a>
        <div class="dd-foot"><a href="/energy-infrastructure/"><strong>Energy overview →</strong></a></div>
      </div>'''

    cols = []
    for d in apps_by_domain:
        names = " · ".join(a["name"] for a in d["apps"])
        cols.append(f'<a href="/ai-applications/#{d["slug"]}"><strong>{d["name"]}</strong><span>{names}</span></a>')
    ai_dd = f'''
      <div class="dropdown wide">
        <div class="dd-label">AI Apps</div>
        {"".join(cols)}
        <div class="dd-foot"><a href="/ai-applications/"><strong>See all AI apps →</strong></a></div>
      </div>'''

    infra_dd = '''
      <div class="dropdown">
        <a href="/infrastructure/#data-centres"><strong>Data-centre cooling</strong><span>Guaranteed energy savings for data halls</span></a>
        <a href="/infrastructure/#power"><strong>Backup power &amp; batteries</strong><span>Secure power, 650 VA to 400 kVA</span></a>
        <a href="/infrastructure/#tiles"><strong>Smart Active Tiles</strong><span>Air where the heat actually is</span></a>
        <a href="/infrastructure/#ai-in-a-box"><strong>AI Factory / AI-in-a-Box</strong><span>Private AI in one rack</span></a>
        <a href="/it-cloud/"><strong>IT &amp; Cloud</strong><span>Database moves, cloud costs, engineers</span></a>
      </div>'''

    svc_dd = '''
      <div class="dropdown">
        <a href="/services/#audit"><strong>Audit</strong><span>Certified energy, water and engineering audits</span></a>
        <a href="/services/#advise"><strong>Advise</strong><span>Consulting, net-zero roadmaps, market entry</span></a>
        <a href="/services/#implement"><strong>Implement</strong><span>We install and connect it</span></a>
        <a href="/services/#run"><strong>Run · Cirtec Care</strong><span>Support after go-live</span></a>
        <a href="/ai-academy/"><strong>CIRTEC AI Academy</strong><span>Practical AI training for professionals</span></a>
      </div>'''

    chev = icon("chev", "chev")
    items = [
        li("energy", f'<button type="button">Energy {chev}</button>{energy_dd}'),
        li("ai", f'<button type="button">AI Applications {chev}</button>{ai_dd}'),
        li("infra", f'<button type="button">Infrastructure {chev}</button>{infra_dd}'),
        li("services", f'<button type="button">Services {chev}</button>{svc_dd}'),
        li("about", f'<a href="{LIVE}/about-us">About Us</a>'),
    ]

    mobile = [
        '<a href="/">Home</a>',
        '<a href="/energy-infrastructure/">Energy</a>',
        '<a class="sub" href="/energy-infrastructure/#measure">Measure</a>',
        '<a class="sub" href="/energy-infrastructure/#act">Improve</a>',
        '<a class="sub" href="/energy-infrastructure/#transform">Add AI</a>',
        '<a class="sub" href="/energy-infrastructure/#eui-check">Free energy check</a>',
        '<a href="/ai-applications/">AI Applications</a>',
    ] + [f'<a class="sub" href="/ai-applications/#{d["slug"]}">{d["name"]}</a>' for d in apps_by_domain] + [
        '<a href="/infrastructure/">Infrastructure</a>',
        '<a class="sub" href="/it-cloud/">IT &amp; Cloud</a>',
        '<a href="/services/">Services</a>',
        '<a class="sub" href="/ai-academy/">CIRTEC AI Academy</a>',
        f'<a href="{LIVE}/about-us">About Us</a>',
        f'<a href="{LIVE}/contact-us">Get in Touch</a>',
    ]

    return f'''
<header class="site-header">
  <nav class="nav" aria-label="Main">
    <a class="nav-logo" href="/" aria-label="CIRTEC AI home"><img src="/assets/img/cirtec-logo.png" alt="CIRTEC AI" width="129" height="30"></a>
    <ul class="nav-links">{"".join(items)}</ul>
    <div class="nav-cta">
      <a class="btn btn-ghost" href="/ai-applications/#demo">Live demo</a>
      <a class="btn btn-primary" href="{LIVE}/contact-us">Get in Touch {icon("arrow")}</a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false">{icon("menu")}</button>
    </div>
  </nav>
  <div class="mobile-menu">{"".join(mobile)}</div>
</header>'''


def footer(apps_by_domain):
    ai_links = "".join(f'<li><a href="/ai-applications/#{d["slug"]}">{d["name"]}</a></li>' for d in apps_by_domain)
    return f'''
<section class="story" aria-label="The one-line story">
  <div class="wrap">
    <p><b>The one-line story</b>CIRTEC helps you get more from what you already have. We cut the energy your buildings use, paid for from the savings. We give your business ready-made AI apps that you see working before you buy. And we train your team to run them.</p>
    <div class="vision"><em>Our vision</em><strong>CIRCULARITY FOR LIFE®</strong></div>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="/assets/img/cirtec-logo.png" alt="CIRTEC AI" width="146" height="34">
        <p class="about">Circular Technology. Delivered with AI. Lower energy bills for your buildings, ready-made AI for your business, and the training to run both.</p>
      </div>
      <div><h5>Energy &amp; Infrastructure</h5><ul>
        <li><a href="/energy-infrastructure/">Energy savings</a></li>
        <li><a href="/energy-infrastructure/#eui-check">Free energy check</a></li>
        <li><a href="/infrastructure/">Power &amp; Cooling</a></li>
        <li><a href="/infrastructure/#ai-in-a-box">AI-in-a-Box</a></li>
        <li><a href="/it-cloud/">IT &amp; Cloud</a></li>
      </ul></div>
      <div><h5>AI Applications</h5><ul>{ai_links}</ul></div>
      <div><h5>Services</h5><ul>
        <li><a href="/services/#audit">Audit</a></li>
        <li><a href="/services/#advise">Advise</a></li>
        <li><a href="/services/#implement">Implement</a></li>
        <li><a href="/services/#run">Run · Cirtec Care</a></li>
        <li><a href="/ai-academy/">CIRTEC AI Academy</a></li>
      </ul></div>
      <div><h5>Contact</h5><ul>
        <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>#24-01 CapitaGreen, 138 Market Street, Singapore 048946</li>
        <li>Also in Kuala Lumpur, Metro Manila and Chennai</li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>©2026 CIRTEC AI Pte. Ltd. All rights reserved.</span>
      <nav><a href="{LIVE}/ai-transparency">AI Transparency</a><a href="{LIVE}/privacy-policy">Privacy Policy</a><a href="{LIVE}/terms-of-service">Terms of Service</a></nav>
    </div>
  </div>
</footer>
<a class="wa" href="https://wa.me/{PHONE_TEL}" aria-label="Chat on WhatsApp">{WA_SVG}</a>'''


def page(title, description, active, body, apps_by_domain, path="/", extra_css=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{LIVE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="icon" href="{LIVE}/fevicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">{extra_css}
</head>
<body>
{nav(active, apps_by_domain)}
<main>
{body}
</main>
{footer(apps_by_domain)}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''
