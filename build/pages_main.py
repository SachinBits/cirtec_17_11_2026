"""Home, Energy & Infrastructure, Services and AI Bootcamp pages."""
from layout import icon, LIVE, PHONE, PHONE_TEL, EMAIL
from apps import DOMAINS

SHARED = [
    ("ai-vision", "AI Vision", "Turns the cameras you already have into a 24/7 security guard."),
    ("safewatch", "SafeWatch", "Spots missing hard hats and people in no-go zones, on your own site."),
    ("carbon-cast", "Carbon Cast", "Turns utility bills into carbon reports your auditors accept."),
    ("ecolensai", "EcoLensAI", "Point a phone camera at a room and get an energy audit."),
]

ENERGY_LADDER = [
    ("01", "Free energy check", "Two numbers from your bills. See how much energy your building uses per square metre."),
    ("02", "Energy or water audit", "Certified engineers find exactly where energy is wasted."),
    ("03", "90-day pilot", "We prove the saving on one system first, against figures we both sign."),
    ("04", "Deployment", "Our software runs on the equipment you already have."),
    ("05", "Subscription", "We keep tracking and protecting the savings."),
    ("06", "Add AI", "Add AI once the savings are in."),
]

AI_LADDER = [
    ("01", "Choose your apps", "Pick the results you need first."),
    ("02", "Live demo", "We show it working on your own example."),
    ("03", "Deploy on your cloud", "It runs on your systems, so your data stays with you."),
    ("04", "Expand", "Add more apps when you are ready."),
]


def ladder(rungs, cls):
    out = []
    for i, (n, h, p) in enumerate(rungs):
        first = " first" if i == 0 else ""
        out.append(f'<div class="rung{first}"><span class="n">{n}</span><h4>{h}</h4><p>{p}</p></div>')
    return f'<div class="ladder {cls}">{"".join(out)}</div>'


def both_band(context):
    apps = "".join(f'<a href="/ai-applications/{s}/"><strong>{n}</strong><span>{d}</span></a>' for s, n, d in SHARED)
    lead = {
        "energy": "These four AI apps help your buildings and your wider business. Start with whichever matters most.",
        "ai": "These four apps also help cut energy use in your buildings. Many customers start with one and add the other.",
        "home": "AI Vision, SafeWatch, Carbon Cast and EcoLensAI work for your buildings and for your wider business. Start with one, add the other later.",
    }[context]
    return f'''
<section class="section tight"><div class="wrap">
  <div class="both-band reveal">
    <div>
      <span class="eyebrow violet">Four apps, two uses</span>
      <h2>Four AI apps that help your buildings and your business.</h2>
      <p class="lead" style="margin-top:14px">{lead}</p>
      <div class="two-doors">
        <div class="g"><b>For your buildings</b>Added once the energy audit shows where to act.</div>
        <div class="v"><b>For your business</b>Often the first app, after a live demo.</div>
      </div>
    </div>
    <div class="both-apps">{apps}</div>
  </div>
</div></section>'''


def cta(title, text, primary, secondary=None, violet=False):
    v = " violet" if violet else ""
    sec = f'<a class="btn btn-ghost-light" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ""
    return f'''
<section class="section tight"><div class="wrap">
  <div class="cta-band{v} reveal">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btn-row"><a class="btn btn-primary" href="{primary[1]}">{primary[0]} {icon("arrow")}</a>{sec}</div>
  </div>
</div></section>'''


# ---------------------------------------------------------------- ENERGY
def product(name, desc, tag=None, logo=None, href=None):
    t = f'<span class="tag {tag[0]}">{tag[1]}</span>' if tag else ""
    title = f'<a href="{href}">{name}</a>' if href else name
    if logo:
        head = f'<img class="logo-img" src="/assets/img/{logo}" alt="{name}" loading="lazy"><div style="margin-bottom:6px">{t}</div>'
    else:
        head = f'<h4>{title} {t}</h4>'
    return f'<div class="product">{head}<p>{desc}</p></div>'


def energy():
    both = ("both", "Also in AI suite")
    partner = lambda n: ("partner", n)
    return f'''
<section class="page-hero mint-bg">
  <div class="wrap grid">
    <div>
      <div class="crumbs"><a class="back" href="/">← Home</a><a href="/">Solutions</a><span>/</span><span>Energy &amp; Infrastructure</span></div>
      <span class="eyebrow">Energy savings for your buildings</span>
      <h1>Cut your energy bills, <span class="accent">without replacing what you have.</span></h1>
      <p class="lead">We measure where your energy goes, make your existing equipment run better, then add AI. There's no upfront cost: you pay from the money you save.</p>
      <div class="btn-row"><a class="btn btn-primary" href="#eui-check">Free energy check {icon("arrow")}</a><a class="btn btn-ghost" href="/services/#audit">Book an energy audit</a></div>
    </div>
    <div class="hero-figure"><img src="/assets/img/smart-campus.jpg" alt="Isometric smart campus with buildings, solar and plant" width="1261" height="903"></div>
  </div>
</section>

<section class="section tight"><div class="wrap">
  <div class="callout reveal">
    <span class="q">“</span>
    <p>Is this building using more than last month, and do you know why?<small>If you're not sure, measuring is where we start.</small></p>
    <a class="btn btn-primary" href="#eui-check">Find out {icon("arrow")}</a>
  </div>
</div></section>

<section class="section mint" id="measure">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Measure · Improve · Add AI</span>
      <h2>Three steps, in this order.</h2>
      <p class="lead">Each step pays for the next. We always start by measuring.</p>
    </div>
    <div class="pillars">
      <div class="pillar reveal">
        <span class="step"><b>1</b> Measure</span>
        <p class="intro">You can't fix what you can't see. The easiest place to start.</p>
        {product("EnergyLoop", "Tracks electricity, water, gas and indoor air quality across all your sites, and spots waste. Works even without a building management system. From S$750/yr + setup.", ("green", "CIRTEC platform"), "energyloop.png")}
        {product("AI DCEM", "A live 3D map of heat and power in your data hall that shows exactly where to adjust cooling. The energy saving is written into the contract.", partner("Powered by EkkoSense"), "ai-dcem.png")}
        {product("Energy &amp; Water Audits", "A certified engineer checks each piece of equipment, onsite or remote, and tells you what to fix. Fixed fee from USD 5k.", ("green", "Service"), href="/services/#audit")}
        <p class="kicker">Ask yourself: is this building using more energy than last month, and do you know why?</p>
      </div>
      <div class="pillar reveal" id="act">
        <span class="step"><b>2</b> Improve</span>
        <p class="intro">Make your existing equipment run better.</p>
        {product("PointLoop", "Controls your whole building from one screen, using the controllers you already have.", ("green", "CIRTEC platform"), "pointloop.png")}
        {product("ChillerLoop", "Makes your chillers, pumps and air-con run more efficiently, without new equipment. S$10k licence or subscription.", ("green", "CIRTEC platform"), "chillerloop.png")}
        {product("Backup power &amp; batteries", "Backup power, battery storage and smart power strips for any size of site. From USD 1,600.", partner("BPE"), href="/infrastructure/#power")}
        {product("Smart Active Tiles", "Floor tiles with fans that send cold air to the hottest racks. From USD 100 per tile pilot.", partner("BPE"), href="/infrastructure/#tiles")}
        <p class="kicker">No upfront cost. You pay from the money you save.</p>
      </div>
      <div class="pillar reveal" id="transform">
        <span class="step"><b>3</b> Add AI</span>
        <p class="intro">Add AI once the savings are in.</p>
        {product("AI Vision", "Turns the cameras you already have into a 24/7 security guard.", both, href="/ai-applications/ai-vision/")}
        {product("SafeWatch", "Spots missing hard hats and people in no-go zones, on your own site.", both, href="/ai-applications/safewatch/")}
        {product("Carbon Cast", "Turns utility bills into carbon reports your auditors accept.", both, href="/ai-applications/carbon-cast/")}
        {product("EcoLensAI", "Point a phone camera at a room and get an energy audit.", both, href="/ai-applications/ecolensai/")}
        {product("AI Asset Manager", "Maintenance software for all your buildings: planned servicing, work orders, early warnings and an AI that learns from every repair. From USD 550/yr + setup.", ("both", "Discover all AI apps"), href="/ai-applications/")}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Step by step</span>
      <h2>Start small. Grow when it pays.</h2>
      <p class="lead">Six steps from a free check to AI across all your buildings. Most customers start at step one or two.</p>
    </div>
    <div class="reveal">{ladder(ENERGY_LADDER, "six")}</div>
  </div>
</section>

<section class="section mint">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:start">
      <div class="reveal">
        <span class="eyebrow">Sound familiar?</span>
        <h2>The problems we are called in for.</h2>
        <p class="lead" style="margin-top:16px">For the people who run buildings, plants and data centres, and the people who report on their energy.</p>
        <div class="chips" style="margin-top:22px"><span class="chip">Facilities &amp; Energy Managers</span><span class="chip">Building Operators</span><span class="chip">Plant &amp; Ops Heads</span><span class="chip">Data-centre Ops</span><span class="chip">Chief Engineers</span><span class="chip">Sustainability Leads</span></div>
      </div>
      <div class="pain-list reveal">
        <div class="pain"><span class="x">!</span><p>Energy bills keep rising and nobody knows why.</p></div>
        <div class="pain"><span class="x">!</span><p>An old building control system that nobody wants to touch.</p></div>
        <div class="pain"><span class="x">!</span><p>Worry that equipment or data halls will go down.</p></div>
        <div class="pain"><span class="x">!</span><p>Quotes that start with replacing all your equipment.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Results</span><h2>Savings, guaranteed.</h2></div>
    <div class="proof">
      <div class="card reveal"><strong>~15%</strong><h4>Guaranteed air-con savings</h4><p>Backed by a $1M insurance policy.</p></div>
      <div class="card reveal"><strong>20+</strong><h4>Data centres on our AI DCEM platform</h4><p>Including CBRE, BT, Visa and Telefónica.</p></div>
      <div class="card reveal"><strong>&gt;12%</strong><h4>Annual saving, chillers 9% more efficient</h4><p>At a 603,200 sq ft hospital in Bangkok.</p></div>
      <div class="card reveal"><strong>12%</strong><h4>Cut, no machine replaced</h4><p>At a dairy plant in Tamil Nadu.</p></div>
      <div class="card reveal"><strong>15 MW</strong><h4>Saved across client projects</h4><p>Plus 250 sustainability audits completed.</p></div>
    </div>
  </div>
</section>

<section class="section mint" id="eui-check">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Step 01 · Free</span>
        <h2>Free energy check.</h2>
        <p class="lead" style="margin-top:16px">The first number we look at is how much energy your building uses for every square metre of floor (called EUI). Two inputs from your last twelve months of bills. One minute.</p>
        <div class="svc" style="background:none;border:0;box-shadow:none;padding:0;margin-top:10px"><ul>
          <li>{icon("check")} Your building's energy use per square metre, instantly</li>
          <li>{icon("check")} An engineer's view of how it compares with similar buildings</li>
          <li>{icon("check")} A recommendation on whether an audit is worth it</li>
        </ul></div>
      </div>
      <div class="form-card reveal">
        <form data-eui>
          <div class="form-grid">
            <div class="field full"><label for="kwh">Electricity used, last 12 months (kWh)</label><input id="kwh" name="kwh" inputmode="decimal" placeholder="e.g. 1,850,000" required></div>
            <div class="field"><label for="area">Gross floor area</label><input id="area" name="area" inputmode="decimal" placeholder="e.g. 9,500" required></div>
            <div class="field"><label for="unit">Unit</label><select id="unit" name="unit"><option value="m2">m²</option><option value="sqft">sq ft</option></select></div>
          </div>
          <button class="btn btn-primary" type="submit" style="margin-top:18px;width:100%;justify-content:center">Check my building {icon("arrow")}</button>
        </form>
        <div class="eui-result" data-eui-result>
          <div class="lbl small muted">Your building's energy use</div>
          <strong data-eui-value>0</strong> <span class="muted">kWh/m²/yr</span>
          <p class="small muted" style="margin-top:6px">Across <span data-eui-area>0</span> m². What counts as good depends on the building type, climate and opening hours, so send it to our engineers for a free comparison.</p>
          <form data-lead-form style="margin-top:14px">
            <div class="form-grid">
              <div class="field"><label for="eui-name">Name</label><input id="eui-name" required></div>
              <div class="field"><label for="eui-email">Work email</label><input id="eui-email" type="email" required></div>
              <div class="field full"><label for="eui-type">Building type</label><select id="eui-type"><option>Office</option><option>Retail / mall</option><option>Hotel</option><option>Hospital</option><option>Data centre</option><option>Industrial / plant</option><option>Education</option><option>Other</option></select></div>
            </div>
            <button class="btn btn-dark" type="submit" style="margin-top:14px">Send to an engineer</button>
          </form>
          <div class="form-success"><div class="tick">{icon("check")}</div><h4>Sent to our auditors</h4><p class="small muted">We will reply within five working days.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

{both_band("energy")}

{cta("Measure first. Then decide.", "Start with the free energy check, or book a certified energy and water audit, onsite or remote.", ("Book an energy audit", "/services/#audit"), ("See Power &amp; Cooling", "/infrastructure/"))}
'''
