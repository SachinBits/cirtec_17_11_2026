"""Homepage: the live cirtec.ai homepage (same design, same copy, same assets),
with the Message House v7 sections woven in between.

Live sections (kept):  hero video + cards + ticker, partner logos, "Energy Aware"
technology stack, Why Us + Loop cards, Accelerating Circular Transformation banner,
IBP, Loop feature blocks, Success Stories, Blog, "Ready to Transform" CTA.
CMS content (hero cards, ticker, stories, blog) is a snapshot of the WordPress API
taken 16 Nov 2026; in Astro keep fetching it from WordPress as the live site does.
"""
from layout import icon, LIVE
from apps import DOMAINS
from pages_main import ladder, ENERGY_LADDER, AI_LADDER, both_band

IMG = "/assets/img/home"
A = icon("arrow")

HERO_CARDS = [
    ("card-70.jpg", "70%", "Up to 70% grant availability for HVAC and Energy Management"),
    ("card-15.jpg", "", "Save 15% of your energy bill with our IR Blaster and EMS Technology"),
    ("card-factory.jpg", "", "Our AI Factory now includes AI Vision and AI Concierge"),
]
STORIES = [
    ("With CIRTEC AI, we’ve achieved energy savings across our company operations in Singapore &amp; Malaysia", "Stacey Su", "Business Operations Manager"),
    ("We’re tracking our emissions in real-time, and the dashboards allow us to identify energy costs down to the use/day!", "Alina Evans", "Manager, Engineering Team"),
    ("Seeing is Believing, and the CIRTEC AI platform gives us incredible insight and historic data references.", "James Tan", "VP, Investor Risk"),
]
WP = "https://cirtec.ai/wordpress"
POSTS = [
    ("Jul 20, 2026", "Comparing Traditional and Green Data Centers: Energy and Environmental Impact", f"{WP}/comparing-traditional-and-green-data-centers-energy-and-environmental-impact/", f"{WP}/wp-content/uploads/2026/07/Thumbnail.png"),
    ("Jun 4, 2026", "Integrating Renewable Energy into Data Centers Using AI", f"{WP}/integrating-renewable-energy-into-data-centers-using-ai/", ""),
    ("May 21, 2026", "How Cirtec.AI Supports the Future of Green Infrastructure?", f"{WP}/cirtec-ai-green-infrastructure-solutions/", f"{WP}/wp-content/uploads/2026/05/How-Cirtec.AI-Supports-the-Future-of-Green-Infrastructure.jpeg"),
    ("May 6, 2026", "From Carbon Zeroed to CIRTEC.AI: Our Journey and What We’re Building", f"{WP}/from-carbon-zeroed-to-cirtec-ai-our-journey-and-what-were-building/", f"{WP}/wp-content/uploads/2026/05/From-Carbon-Zeroed-to-CIRTEC.AI-Our-Journey-and-What-Were-Building.jpeg"),
    ("Apr 10, 2026", "Too Many Resumes, Too Little Time? Let AI Do the First Round for You", f"{WP}/too-many-resumes-too-little-time-let-ai-do-the-first-round-for-you/", f"{WP}/wp-content/uploads/2026/04/too-many-resumes-too-little-time.jpeg"),
    ("Mar 26, 2026", "The Financial Benefits of Carbon Management for Modern Businesses", f"{WP}/financial-benefits-carbon-management/", f"{WP}/wp-content/uploads/2026/04/The-Financial-Benefits-of-Carbon-Management-for-Modern-Businesses.jpeg"),
    ("Feb 27, 2026", "Smart Buildings and Carbon Reduction: The Integration of IoT", f"{WP}/smart-buildings-iot-carbon-reduction/", f"{WP}/wp-content/uploads/2026/02/Smart-Buildings-and-Carbon-Reductions-Integration-of-IOT.jpeg"),
]
UNSPLASH = "https://images.unsplash.com/photo-{}?auto=format&fit=crop&q=80&w=1200&h=900"


def _hero():
    cards = ""
    for img, big, txt in HERO_CARDS:
        b = f'<div class="big">{big}<img src="{IMG}/polygon.png" alt=""></div>' if big else ""
        cards += f'<div class="h-card"><img src="{IMG}/{img}" alt="" loading="lazy">{b}<p>{txt}</p></div>'
    return f'''
<section class="h-hero">
  <div class="h-hero-shell">
    <video muted autoplay loop playsinline poster="{IMG}/hero-poster.jpg"><source src="{IMG}/hero.mp4" type="video/mp4"></video>
    <div class="h-hero-grid">
      <div style="align-self:center">
        <h1>Circular Tech.<br>Delivered with AI.</h1>
        <div class="bar"></div>
        <p class="sub">We help your buildings use less energy and put ready-made AI to work in your business, using the equipment and systems you already have.</p>
        <a class="h-learn" href="#find-your-page">Learn More <i>↗</i></a>
      </div>
      <div class="h-cards" aria-label="Latest from CIRTEC AI"><div class="h-cards-track">{cards}{cards}</div></div>
    </div>
    <div class="h-ticker"><b>What's happening now?</b><div class="run"><span>AI Vision by CIRTEC is now available on Kaira Global Marketplace.</span></div></div>
  </div>
</section>'''


def _logos():
    one = "".join(f'<a href="#" aria-hidden="true" tabindex="-1"><img src="{IMG}/partner-{n}.png" alt=""><img class="on" src="{IMG}/partner-{n}-on.png" alt=""></a>' for n in (1, 2, 3, 4, 5, 6, 8, 9))
    return f'<div class="h-logos" aria-label="Technology partners"><div class="h-logos-track">{one}{one}</div></div>'


def _find_your_page():
    b = [
        ("/energy-infrastructure/", "hardhat", "Builders &amp; contractors", "Developers · contractors · building-services engineers · system integrators", "Smart building controls for new and refurbished buildings, camera-based site safety, and a digital maintenance record to hand over.", "Energy platforms"),
        ("/infrastructure/#data-centres", "server", "Data-centre owners &amp; operators", "Colocation · telco · enterprise data centres", "Cooling and power for your data halls, with the energy saving written into the contract.", "Power &amp; Cooling"),
        ("/ai-applications/", "building", "Facilities &amp; operations", "Heads of FM · operations directors · hospitality · healthcare", "Ready-made AI apps for guests, safety and maintenance, plus smart air-con control. Live in weeks on the systems you already run.", "AI Applications"),
        ("/it-cloud/", "cloud", "IT &amp; digital leaders", "CIOs · CTOs · heads of infrastructure and data", "Move old databases to the cloud, update legacy software, run AI on your own servers, cut cloud bills, and hire engineers.", "IT &amp; Cloud"),
        ("/ai-applications/carbon-cast/", "leaf", "Sustainability, finance &amp; investor risk", "CSOs · CFOs · boards · lenders · investors", "Carbon reports that meet the new disclosure rules, plus energy audits and advice that turn targets into funded projects.", "Carbon Cast"),
    ]
    cards = "".join(f'<a class="buyer reveal" href="{h}"><div class="ic">{icon(i)}</div><h4>{t}</h4><div class="who">{w}</div><p>{p}</p><span class="link-arrow">{l}</span></a>' for h, i, t, w, p, l in b)
    return f'''
<section class="section" id="find-your-page">
  <div class="wrap">
    <div class="h-roof reveal">
      <span class="eyebrow">Find your page</span>
      <h2>Works with what you already run. <span class="accent">Proves its value before you scale.</span></h2>
      <p>For your buildings, we find where energy is wasted and fix it on the equipment you already have. For your business, we offer ready-made AI apps that run on your own cloud. We also supply power and cooling hardware, and the people to install, support and train.</p>
      <div class="tags"><span>Platforms</span><span>Applications</span><span>Infrastructure</span><span>Services</span></div>
    </div>
    <p class="center muted reveal" style="font-family:var(--head);font-weight:700;color:var(--ink);margin-bottom:22px">Start with the decision you own. Five buyers, five ways in.</p>
    <div class="buyers">{cards}</div>
  </div>
</section>'''


def _stack():
    feat = [("sparkle", "AI Advisory Layer"), ("layout", "Unified Across Systems"), ("chart", "Real-time Intelligence")]
    li = "".join(f'<li><i>{icon(a)}</i>{b}</li>' for a, b in feat)
    return f'''
<section class="h-stack">
  <div class="wrap h-stack-grid">
    <div class="reveal">
      <span class="eyebrow">Our Technology Stack</span>
      <h2>“Energy Aware” Technology Stack</h2>
      <p class="lead">Our platforms connect your IT systems, building equipment and sensors, and add AI on top, so you can see and control everything in one place</p>
      <ul class="h-feat">{li}</ul>
      <a class="btn btn-primary" href="/energy-infrastructure/">Explore Platform {A}</a>
      <div class="h-secure">{icon("shield")} Secure. Scalable. Sustainable.</div>
    </div>
    <div class="orbit reveal">
      <div class="orbit-mark"><img src="{IMG}/cirtec-mark.png" alt=""></div>
      <a class="o-card c1" href="/ai-applications/"><h4>AI Led Operations</h4><p>AI on the front line for people and operations</p><img src="{IMG}/stack-aiops.png" alt="" loading="lazy"><span class="km">Know more →</span></a>
      <a class="o-card c2" href="/energy-infrastructure/#measure"><h4>Monitor &amp; Manage</h4><p>Measurement, emissions, and automated upkeep</p><img src="{IMG}/stack-monitor.png" alt="" loading="lazy"><span class="km">Know more →</span></a>
      <a class="o-card c3" href="/infrastructure/"><h4>Power &amp; Cooling</h4><p>Intelligent power and cooling at the source</p><img src="{IMG}/stack-power.png" alt="" loading="lazy"><span class="km">Know more →</span></a>
    </div>
  </div>
</section>'''


def _houses():
    return f'''
<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Platforms · Applications · Infrastructure · Services</span>
      <h2>What we do.</h2>
      <p class="lead">Two main offers: lower energy use in your buildings, and ready-made AI for your business. Plus the hardware and services behind them.</p>
    </div>
    <div class="grid-2">
      <div class="line-card green reveal">
        <span class="num">For your buildings</span>
        <h3>Energy &amp; Infrastructure</h3>
        <p class="promise">Guaranteed energy savings, without replacing what you have.</p>
        <p>We measure where energy goes, improve how your equipment runs, then add AI.</p>
        <ul><li>Measure: see where your energy goes</li><li>Improve: tune air-con, chillers and controls</li><li>Add AI: cameras, carbon reports, maintenance</li></ul>
        <a class="btn btn-dark" href="/energy-infrastructure/">Explore Energy {A}</a>
      </div>
      <div class="line-card violet reveal">
        <span class="num">For your business</span>
        <h3>Enterprise AI Applications</h3>
        <p class="promise">AI apps that are already built, run on your own systems, and are proven before you buy.</p>
        <p>Ready-made AI apps for six areas of your business, set up and supported by CIRTEC.</p>
        <ul><li>Security &amp; Safety · Sustainability &amp; ESG</li><li>Hospitality &amp; Gaming · People: HR &amp; Learning</li><li>Retail, Sales &amp; Content · Data, Reporting &amp; Design</li></ul>
        <a class="btn btn-violet" href="/ai-applications/">See all AI apps {A}</a>
      </div>
    </div>
    <div class="roof-strip">
      <a class="card top-line reveal" href="/infrastructure/"><div class="ic">{icon("battery")}</div><h3>Infrastructure</h3><p>Backup power, batteries, cooling tiles, server racks and private AI servers.</p></a>
      <a class="card top-line v reveal" href="/it-cloud/"><div class="ic v">{icon("cloud")}</div><h3>IT &amp; Cloud</h3><p>Get your data and systems ready for AI, and cut cloud bills.</p></a>
      <a class="card top-line reveal" href="/services/"><div class="ic">{icon("wrench")}</div><h3>Services</h3><p>We audit, advise, install and support. The same four steps for everything.</p></a>
      <a class="card top-line a reveal" href="/ai-academy/"><div class="ic" style="background:#fff3dc;color:#b86b00">{icon("grad")}</div><h3>CIRTEC AI Academy</h3><p>Practical AI training, so your own team can run the tools.</p></a>
    </div>
  </div>
</section>'''


def _why():
    loops = [
        ("ic-pointloop.png", "Point", "brand-g", "Centralized Building Management", "Cloud building controls that bring air-con, lighting, pumps, chillers and meters onto one screen, so you can see and control them live."),
        ("ic-energyloop.png", "Energy", "brand-o", "Energy Intelligence", "Enterprise-grade energy management with granular consumption analytics and demand forecasting across every meter and site."),
        ("ic-chillerloop.png", "Chiller", "brand-v", "HVAC Optimization", "Intelligent HVAC energy optimization that integrates with your existing BMS to cut energy consumption by 15–20%."),
    ]
    cards = "".join(f'<div class="loop-card reveal"><div class="lr"><img src="{IMG}/{i}" alt=""><span class="brand">{n}<span class="{c}">Loop</span></span></div><h3>{h}</h3><p>{p}</p></div>' for i, n, c, h, p in loops)
    return f'''
<section class="h-why">
  <div class="wrap">
    <h2 class="reveal">Why Us?</h2>
    <p class="reveal">CIRTEC AI has pre-defined, outcome-driven AI solutions designed to help businesses achieve measurable results in a short timeframe — without the complexity, cost, or risk typically associated with large-scale AI projects.</p>
    <p class="reveal">Under the MSFT-IMDA GenAIxDigital Leaders Programme, CIRTEC AI enables digitally ready SMEs to adopt secure, enterprise-grade AI solutions that are quick to plan, fast to set up, and aligned with real operational needs.</p>
    <div class="loop-cards">{cards}</div>
  </div>
</section>'''


def _energy_ladder():
    return f'''
<section class="section">
  <div class="wrap">
    <div class="grid-2" style="align-items:center;gap:56px">
      <div class="reveal">
        <span class="eyebrow">For your buildings · step by step</span>
        <h2>We measure before we change anything.</h2>
        <p class="lead" style="margin-top:16px">You can't fix what you can't see. So we start by measuring. The first step is free, and there's no upfront cost: you pay from the money you save.</p>
        <div class="btn-row"><a class="btn btn-primary" href="/energy-infrastructure/#eui-check">Free energy check {A}</a><a class="btn btn-ghost" href="/services/#audit">Book an energy audit</a></div>
      </div>
      <div class="reveal">{ladder(ENERGY_LADDER, "six-compact")}</div>
    </div>
  </div>
</section>'''


def _accelerating():
    pts = [("Optimize Energy", "Reduce consumption and costs"), ("Reduce Carbon", "Track, manage and reduce emissions"), ("Future Ready", "AI-driven insights for smarter decisions")]
    li = "".join(f'<li>{icon("bolt")}<span><b>{a}</b>{b}</span></li>' for a, b in pts)
    return f'''
<section class="section tight"><div class="wrap">
  <div class="v-banner reveal">
    <video muted autoplay loop playsinline preload="metadata" poster="{IMG}/cta-poster.jpg"><source src="{IMG}/cta-bg.mp4" type="video/mp4"></video>
    <div class="v-inner">
      <span class="v-badge">🍃 AI-Powered. Sustainable. Scalable.</span>
      <h2><small>Accelerating</small>Circular Transformation<br><small>with <span class="accent">CIRTEC AI</span></small></h2>
      <p>Intelligent solutions that optimize energy, reduce carbon footprint, and future-proof your operations.</p>
      <div class="v-btns"><a class="btn btn-dark" href="{LIVE}/contact-us">Schedule Demo <i>↗</i></a><a class="link-arrow" href="/energy-infrastructure/">Explore Solutions</a></div>
      <ul class="v-points">{li}</ul>
    </div>
  </div>
</div></section>'''


def _ibp():
    layers = [("layout", "Unified Experience", "Web · Mobile · Voice"), ("sparkle", "AI Decisions", "Predicts · understands · sees"), ("db", "Digital Twin Core", "Live 3D building model")]
    ls = "".join(f'<div class="l"><i>{icon(a)}</i><div><b>{b}</b><span>{c}</span></div></div>' for a, b, c in layers)
    cards = [
        ("layout", "Unified User Experience", "One interface for the entire building — web dashboard, mobile, AR/VR, and voice — so every team works the way they already do."),
        ("sparkle", "AI Orchestration &amp; Decision Layer", "AI that predicts problems, understands requests and reads camera feeds, and makes decisions across every system as things happen."),
        ("db", "Digital Twin Core", "Every asset, sensor, and system is anchored to a live 3D model of your building, kept in sync in real time."),
        ("plug", "Integration Fabric (API + IoT)", "Connects your existing hardware and software — BACnet, Modbus, OPC-UA, MQTT, REST, GraphQL — without ripping anything out."),
        ("cpu", "Edge &amp; Field Layer", "Sensors, actuators, controllers, and gateways form the physical layer where every decision is actually carried out."),
    ]
    cs = "".join(f'<div class="ibp-card reveal"><div class="ic">{icon(a)}</div><h4>{b}</h4><p>{c}</p></div>' for a, b, c in cards)
    return f'''
<section class="h-ibp">
  <div class="wrap">
    <div class="h-ibp-head reveal"><h2>IBP From CIRTEC AI</h2><span>INTEGRATED BUILDING PLATFORM</span></div>
    <div class="h-ibp-grid">
      <div class="ibp-visual reveal">
        <img src="{IMG}/ibp-visual.jpg" alt="CIRTEC AI's Integrated Building Platform: five unified layers" loading="lazy">
        <div class="ibp-tele t1">Impact Telemetry<b>25–40%</b><small>Lower energy use</small></div>
        <div class="ibp-tele t2">Autonomous AI Loop<b>70%+</b><small>Alarms auto-resolved</small></div>
      </div>
      <div class="ibp-copy reveal">
        <p>Five separate systems (maintenance, building model, automation, energy and building management) joined into one AI platform that learns how your building behaves and keeps improving it.</p>
        <div class="ibp-stats"><div><b>25–40%</b><span>Lower energy use</span></div><div><b>50%</b><span>Faster repairs</span></div><div><b>70%+</b><span>Alarms auto-resolved</span></div></div>
        <div class="ibp-layers">{ls}<div class="cu">CONNECTS &amp; UNIFIES</div><div class="chips chips-row"><span class="chip">CMMS</span> <span class="chip">BAS</span> <span class="chip">EMS</span> <span class="chip">BMS</span></div></div>
      </div>
    </div>
    <div class="ibp-cards">{cs}</div>
  </div>
</section>'''


def _features():
    blocks = [
        (False, "users", "Cloud building controls", '<span>Point<span class="brand-g">Loop</span></span> : Niagara Native Cloud-Based <span class="g">Building Management System</span>',
         ["PointLoop is a Niagara Native Cloud-Based Building Management System (BMS) that connects, monitors, and controls building systems — from HVAC and lighting to pumps, chillers, and meters — through a single centralized platform.",
          "Built on the open, scalable Niagara Framework, PointLoop eliminates the need for multiple disconnected control systems, giving facility teams real-time visibility, remote control, and automation across every connected building."],
         [("sliders", "Niagara Native"), ("building", "Centralized Control"), ("bell", "Real-Time Alarms")], "1486406146926-c627a92ad1ab", "Glass office towers"),
        (True, "users", "AI Energy Analytics", '<span>Energy<span class="brand-o">Loop</span></span> : AI-Powered <span class="g">Energy Intelligence Platform</span>',
         ["EnergyLoop is an AI-powered cloud analytics and energy management platform that provides real-time visibility into buildings, equipment, and utilities from a single centralized dashboard.",
          "By connecting sensors, meters, HVAC systems, and electrical panels, EnergyLoop continuously monitors performance, detects anomalies, and delivers actionable insights that reduce operational costs and support smarter, data-driven decisions."],
         [("chart", "Real-Time Monitoring"), ("sparkle", "AI-Powered Analytics"), ("globe", "Multi-Site Visibility")], "1473341304170-971dccb5ac1e", "Power pylons at sunset"),
        (False, "users", "AI HVAC Optimization", '<span>Chiller<span class="brand-v">Loop</span></span> : Intelligent HVAC Energy Optimization',
         ["ChillerLoop is an AI-powered HVAC optimization platform that continuously tunes chillers, air handlers, and cooling plants for peak efficiency — without ripping out the Building Management System you already run.",
          "By learning how your building actually behaves, ChillerLoop automatically adjusts setpoints and sequencing in real time, cutting energy consumption by 15–20% while protecting occupant comfort and equipment health."],
         [("fan", "Chiller Plant Optimization"), ("plug", "Works with your building controls"), ("bolt", "15–20% Energy Savings")], "1621905251918-48416bd8575a", "Engineer working on an electrical panel"),
    ]
    out = ""
    for rev, ic, tag, title, paras, chips, img, alt in blocks:
        ps = "".join(f"<p>{p}</p>" for p in paras)
        ch = "".join(f'<span><i>{icon(a)}</i>{b}</span>' for a, b in chips)
        out += f'''
    <div class="feat-block{' rev' if rev else ''} reveal">
      <div class="feat-copy"><span class="pill-tag">{icon(ic)} {tag}</span><h3>{title}</h3><div class="uline"></div>{ps}<div class="feat-chips">{ch}</div></div>
      <div class="feat-img"><img src="{UNSPLASH.format(img)}" alt="{alt}" loading="lazy"></div>
    </div>'''
    return f'<section class="section" style="padding-bottom:40px"><div class="wrap">{out}</div></section>'


def _ai_suite():
    tiles = "".join(
        f'<a class="claim reveal" href="/ai-applications/#{d["slug"]}"><span class="n">{d["name"]}</span><h4 style="font-size:.98rem">{" · ".join(a["name"] for a in d["apps"])}</h4><p>{d["line"]}</p></a>'
        for d in DOMAINS)
    return f'''
<section class="section violet">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow violet">For your business · AI apps</span>
      <h2>AI apps, already built. See them working before you buy.</h2>
      <p class="lead">Ready-made AI for six areas of your business. It runs on your own cloud and works with what you already use: your cameras, hiring and helpdesk systems, Microsoft Teams and data tools.</p>
    </div>
    <div class="claims three">{tiles}</div>
    <div class="reveal" style="margin-top:40px">{ladder(AI_LADDER, "four v")}</div>
    <div class="center" style="margin-top:30px"><a class="btn btn-violet" href="/ai-applications/#demo">Request a live demo {A}</a> <a class="btn btn-ghost" href="/ai-applications/" style="margin-left:8px">See all AI apps</a></div>
  </div>
</section>'''


def _proof():
    items = [("~15%", "Guaranteed air-con savings", "Backed by a $1M insurance policy."),
             ("20+", "Data centres on our AI DCEM platform", "Including CBRE, BT, Visa and Telefónica."),
             ("&gt;12%", "Annual saving, chillers 9% more efficient", "At a 603,200 sq ft hospital in Bangkok."),
             ("12%", "Cut, no machine replaced", "At a dairy plant in Tamil Nadu."),
             ("15 MW", "Saved across client projects", "Plus 250 sustainability audits completed.")]
    cs = "".join(f'<div class="card reveal"><strong>{a}</strong><h4>{b}</h4><p>{c}</p></div>' for a, b, c in items)
    return f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Proof</span><h2>Measured, not marketed.</h2></div>
    <div class="proof">{cs}</div>
  </div>
</section>'''


def _stories():
    cs = "".join(f'<div class="story-card reveal"><img class="q" src="{IMG}/quotes.png" alt=""><p>{q}</p><div class="who"><b>{n}</b><span>{r}</span></div></div>' for q, n, r in STORIES)
    return f'''
<section class="h-stories">
  <div class="wrap">
    <div class="h-center-head reveal"><h2>Success Stories</h2><p>Discover exceptional experiences through testimonials from our satisfied customers</p></div>
    <div class="grid-3">{cs}</div>
  </div>
</section>'''


def _services():
    return f'''
<section class="section mint">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Services</span>
      <h2>Four simple steps, for everything we do.</h2>
      <p class="lead">So a target or a legal requirement becomes a clear plan, with the costs and savings measured.</p>
    </div>
    <div class="grid-4">
      <a class="card top-line reveal" href="/services/#audit"><div class="ic">{icon("gauge")}</div><h3>1 · Audit</h3><p>Certified engineers measure your energy and water use and show where the savings are.</p></a>
      <a class="card top-line reveal" href="/services/#advise"><div class="ic">{icon("target")}</div><h3>2 · Advise</h3><p>Clear plans for net-zero, green building certification and entering new markets.</p></a>
      <a class="card top-line reveal" href="/services/#implement"><div class="ic">{icon("wrench")}</div><h3>3 · Implement</h3><p>We install, connect and set up the systems, and check the savings are real.</p></a>
      <a class="card top-line reveal" href="/services/#run"><div class="ic">{icon("shield")}</div><h3>4 · Run</h3><p>Cirtec Care: support, warranty and yearly reports after go-live.</p></a>
    </div>
    <div class="callout reveal" style="margin-top:36px">
      <span class="q">“</span>
      <p>Who runs this after we leave? Your team.<small>The CIRTEC AI Academy, run with SGTech, trains your people to use and look after the AI. Launching in Singapore this November.</small></p>
      <a class="btn btn-primary" href="/ai-academy/">About the Academy {A}</a>
    </div>
  </div>
</section>'''


def _rules():
    r = [("We ask before we present", "We start with your data and your questions, not a slide deck."),
         ("We prove before we propose", "An audit for energy, a live demo for AI. We never quote into a gap nobody has measured."),
         ("We start with what you run", "The equipment you already have, the cameras on your walls, the tools your team already uses."),
         ("We come prepared", "Every senior meeting is prepared a day ahead, so your time is spent on decisions.")]
    cs = "".join(f'<div class="rule-card reveal"><div class="n">{i+1}</div><h4>{a}</h4><p>{b}</p></div>' for i, (a, b) in enumerate(r))
    return f'''
<section class="section">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow">How we work</span><h2>Four rules, on every engagement.</h2></div>
    <div class="rules">{cs}</div>
  </div>
</section>'''


def _blog():
    cs = ""
    for d, t, u, img in POSTS:
        bg = f' style="background-image:url(\'{img}\')"' if img else ""
        cs += f'<a class="blog-card" href="{u}"><div class="thumb"{bg}></div><div class="b"><time>{d}</time><h4>{t}</h4></div></a>'
    return f'''
<section class="section mint" style="padding-top:70px">
  <div class="wrap">
    <div class="h-center-head reveal"><h2>CIRTEC AI's Blog Articles</h2></div>
    <div class="blog-row">{cs}</div>
  </div>
</section>'''


def _offices():
    o = [("Singapore", "Headquarters", "#24-01 CapitaGreen<br>138 Market Street<br>Singapore 048946"),
         ("Malaysia", "Regional office", "C-5-9, Plaza Mont Kiara<br>2 Jalan Kiara<br>50480 Kuala Lumpur"),
         ("Philippines", "Regional office", "Level 24, PSE Tower<br>One Bonifacio High Street<br>Fort BGC, Taguig City"),
         ("India", "Delivery centre", "Level 2, Indiqube Alpine<br>SIDCO Industry Estate<br>Guindy, Chennai")]
    cs = "".join(f'<div class="office reveal"><h4>{a}</h4><div class="role">{b}</div><p>{c}</p></div>' for a, b, c in o)
    return f'''
<section class="section tight">
  <div class="wrap">
    <div class="section-head reveal" style="margin-bottom:28px"><span class="eyebrow">Where we work</span><h2>Headquartered in Singapore. Delivering region-wide.</h2></div>
    <div class="offices">{cs}</div>
  </div>
</section>'''


def _cta():
    return f'''
<section class="section tight" style="padding-bottom:90px"><div class="wrap">
  <div class="v-banner cta reveal">
    <video muted autoplay loop playsinline preload="metadata" poster="{IMG}/cta-poster.jpg"><source src="{IMG}/cta-bg.mp4" type="video/mp4"></video>
    <div class="v-inner">
      <span class="v-badge">Enterprise AI Solutions</span>
      <h2>Ready to Transform Your Operations?</h2>
      <p>Join leading organizations in reducing energy costs, improving efficiency, and achieving sustainability goals with our climate tech solutions.</p>
      <div class="v-btns"><a class="btn btn-dark" href="{LIVE}/contact-us">Schedule Demo <i>↗</i></a><a class="link-arrow" href="/energy-infrastructure/">Explore Solutions</a></div>
      <div class="v-trust"><span>✓ Enterprise Ready</span><span>✓ Microsoft Partner</span><span>✓ Secure &amp; Scalable</span></div>
    </div>
  </div>
</div></section>'''


def home():
    return "".join([
        _hero(),            # live
        _logos(),           # live
        _find_your_page(),  # NEW: roof line + five buyers
        _stack(),           # live
        _houses(),          # NEW: two houses + infrastructure / IT / services / academy
        _why(),             # live
        _energy_ladder(),   # NEW: energy ladder + EUI
        _accelerating(),    # live
        _ibp(),             # live
        _features(),        # live
        _ai_suite(),        # NEW: 17 apps by domain + AI ladder
        both_band("home"),  # NEW: four apps, two doors
        _proof(),           # NEW: v7 proof
        _stories(),         # live
        _services(),        # NEW: services path + academy
        _rules(),           # NEW: how we work
        _blog(),            # live
        _offices(),         # NEW: offices
        _cta(),             # live
    ])
