"""AI Applications hub, the 17 app detail pages, and the sitemap plan page."""
from layout import icon, LIVE
from apps import DOMAINS, ALL_APPS
from pages_main import ladder, AI_LADDER, both_band, cta


def demo_form(preselect=None):
    boxes = []
    for a in ALL_APPS:
        chk = " checked" if a["slug"] == preselect else ""
        boxes.append(f'<label><input type="checkbox" name="apps" value="{a["slug"]}"{chk}> {a["name"]}</label>')
    return f'''
<div class="form-card reveal">
  <form data-lead-form data-endpoint="">
    <div class="form-grid">
      <div class="field"><label for="d-name">Name</label><input id="d-name" required></div>
      <div class="field"><label for="d-co">Company</label><input id="d-co" required></div>
      <div class="field"><label for="d-email">Work email</label><input id="d-email" type="email" required></div>
      <div class="field"><label for="d-country">Country</label><select id="d-country"><option>Singapore</option><option>Malaysia</option><option>Philippines</option><option>India</option><option>Middle East</option><option>Other</option></select></div>
      <div class="field full"><label>Which apps do you want to see?</label><div class="check-grid">{"".join(boxes)}</div></div>
      <div class="field full"><label for="d-use">What do you want it to do?</label><textarea id="d-use" rows="3" placeholder="e.g. spot people without hard hats at our site gate"></textarea></div>
    </div>
    <button class="btn btn-violet" type="submit" style="margin-top:16px">Request a live demo {icon("arrow")}</button>
  </form>
  <div class="form-success"><div class="tick">{icon("check")}</div><h4>Demo requested</h4><p class="small muted">We will set it up for your example and come back within five working days.</p></div>
</div>'''


def app_card(a):
    search = " ".join([a["name"], a["cat"], a["short"], a["domain"]["name"]]).lower()
    both = '<span class="tag both">Also for buildings</span>' if a.get("both") else ""
    return f'''
<a class="app-card" href="/ai-applications/{a["slug"]}/" data-search="{search}">
  <div class="top"><div class="app-mark">{icon(a["icon"])}</div><div><span class="cat">{a["cat"]}</span><h4>{a["name"]}</h4></div></div>
  <p>{a["short"]}</p>
  <div class="foot"><span class="link-arrow">View app</span>{both}</div>
</a>'''


# ---------------------------------------------------------------- HUB
def hub():
    filters = ['<button type="button" data-domain="all" aria-pressed="true">All apps</button>'] + [
        f'<button type="button" data-domain="{d["slug"]}" aria-pressed="false">{d["name"]}</button>' for d in DOMAINS]
    blocks = []
    for d in DOMAINS:
        cards = "".join(app_card(dict(a, domain=d)) for a in d["apps"])
        blocks.append(f'''
<div class="domain-block" id="{d["slug"]}" data-domain="{d["slug"]}">
  <div class="domain-head"><h3>{d["name"]} <span class="muted small" style="font-weight:600">· {len(d["apps"])} apps</span></h3><p>{d["line"]}</p></div>
  <div class="apps-grid">{cards}</div>
</div>''')

    return f'''
<section class="page-hero violet-bg">
  <div class="wrap grid">
    <div>
      <div class="crumbs"><a class="back" href="/">← Home</a><a href="/">Solutions</a><span>/</span><span>Enterprise AI Applications</span></div>
      <span class="eyebrow violet">AI apps for your business</span>
      <h1>AI apps that are <span class="accent-v">already built</span> and run on your own systems.</h1>
      <p class="lead">Ready-made AI apps that watch camera feeds, answer questions, write reports and more. Each one does one clear job. We set them up and support them.</p>
      <div class="btn-row"><a class="btn btn-violet" href="#demo">Request a live demo {icon("arrow")}</a><a class="btn btn-ghost" href="#apps">Browse the apps</a></div>
      <div class="stats three">
                <div class="stat v"><strong>6</strong><span>areas of your business</span></div>
        <div class="stat v"><strong>4</strong><span>kinds of AI: assistants, cameras, chat, reports</span></div>
        <div class="stat v"><strong>1</strong><span>rule: it runs on your systems, your data stays yours</span></div>
      </div>
    </div>
    <div>{ALL_APPS[0]["mock"]}<p class="caption-note">Illustrative product visual · AI Vision</p></div>
  </div>
</section>

<section class="section" id="apps" style="padding-top:40px">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow violet">All AI apps</span><h2>Six areas. One simple setup.</h2></div>
    <div class="filter-bar" data-filter-bar>
      {"".join(filters)}
      <label class="search">{icon("search")}<input type="search" placeholder="Search apps" aria-label="Search apps"></label>
    </div>
    {"".join(blocks)}
    <p class="center muted" data-empty hidden>No apps match that search.</p>
  </div>
</section>

<section class="section violet">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow violet">Why the suite</span><h2>Why businesses choose it.</h2></div>
    <div class="claims">
      <div class="claim reveal"><span class="n">01</span><h4>Built and ready</h4><p>Set up and go. No long build from scratch.</p></div>
      <div class="claim reveal"><span class="n">02</span><h4>Your cloud, your data</h4><p>Runs on your own cloud, so your data stays with you.</p></div>
      <div class="claim reveal"><span class="n">03</span><h4>Fits what you run</h4><p>Works with your cameras, hiring and helpdesk systems, Microsoft Teams and data tools.</p></div>
      <div class="claim reveal"><span class="n">04</span><h4>Measured by outcomes</h4><p>Each app has one clear result: faster responses, quicker turnaround, fewer hours of manual work.</p></div>
    </div>
    <div class="works-with reveal"><span>Existing CCTV</span><span>Your hiring system</span><span>Helpdesk tools</span><span>Microsoft Teams</span><span>Microsoft Fabric</span><span>Snowflake</span><span>Databricks</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow violet">How it works</span><h2>See it working before you buy.</h2></div>
    <div class="reveal">{ladder(AI_LADDER, "four v")}</div>
    <p class="center muted" style="margin-top:28px">Also inside the suite: <b>AI Asset Manager</b>, <b>ShiftX</b> and <b>Application Performance Management</b>, set up the same way.</p>
  </div>
</section>

{both_band("ai")}

<section class="section violet" id="demo">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow violet">Request a live demo</span>
        <h2>See them working on your own example.</h2>
        <p class="lead" style="margin-top:16px">Tell us which apps interest you and what you want to see. We show them working live on your example, before you commit to anything.</p>
        <div class="ladder" style="grid-template-columns:1fr;margin-top:24px;gap:10px">
          <div class="rung first"><span class="n">01</span><h4>Choose your apps</h4><p>Pick the ones that match the outcomes you need first.</p></div>
          <div class="rung"><span class="n">02</span><h4>See them live</h4><p>Test each app against your own use case.</p></div>
          <div class="rung"><span class="n">03</span><h4>Deploy in your environment</h4><p>Roll out on your own cloud and data platform.</p></div>
        </div>
      </div>
      {demo_form()}
    </div>
  </div>
</section>
'''


# ---------------------------------------------------------------- APP DETAIL
def app_page(a):
    d = a["domain"]
    caps = "".join(f'<div class="cap">{icon("check")}{c}</div>' for c in a["caps"])
    uses = "".join(f'<div class="usecase reveal"><span class="n">0{i+1}</span><h4>{h}</h4><p>{p}</p></div>'
                   for i, (h, p) in enumerate(a["uses"]))
    works = "".join(f"<span>{w}</span>" for w in a["works"])
    siblings = [dict(x, domain=d) for x in d["apps"] if x["slug"] != a["slug"]]
    if len(siblings) < 2:
        idx = DOMAINS.index(d)
        nxt = DOMAINS[(idx + 1) % len(DOMAINS)]
        siblings += [dict(x, domain=nxt) for x in nxt["apps"]][: 3 - len(siblings)]
    related = "".join(app_card(s) for s in siblings[:3])
    logo = f'<img src="/assets/img/{a["logo"]}" alt="{a["name"]}" style="height:44px;width:auto;margin-bottom:18px">' if a.get("logo") else ""
    both = ""
    if a.get("both"):
        both = f'''
<section class="section tight"><div class="wrap">
  <div class="both-band reveal" style="grid-template-columns:1fr auto">
    <div><span class="eyebrow">Also for your buildings</span><h3 style="font-size:1.4rem">{a["name"]} also helps cut energy use in your buildings.</h3>
    <p class="muted" style="margin-top:8px">For buildings, we add it once an energy audit shows where to act. For the wider business, it is often the first app customers try.</p></div>
    <a class="btn btn-dark" href="/energy-infrastructure/#transform">See it for buildings {icon("arrow")}</a>
  </div>
</div></section>'''

    return f'''
<section class="page-hero violet-bg">
  <div class="wrap grid">
    <div>
      <div class="crumbs"><a class="back" href="/ai-applications/">← All apps</a><a href="/ai-applications/">AI Applications</a><span>/</span><a href="/ai-applications/#{d["slug"]}">{d["name"]}</a><span>/</span><span>{a["name"]}</span></div>
      {logo}
      <span class="eyebrow violet">{a["name"]} · {a["cat"]}</span>
      <h1>{a["headline"]}</h1>
      <p class="lead">{a["desc"]}</p>
      <div class="cap-grid">{caps}</div>
      <div class="btn-row"><a class="btn btn-violet" href="#demo">See {a["name"]} live {icon("arrow")}</a><a class="btn btn-ghost" href="/ai-applications/">All AI apps</a></div>
    </div>
    <div>{a["mock"]}<p class="caption-note">Illustrative product visual</p></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="tabs"><a class="on" href="#use-cases">Use cases</a><a href="#fit">How it fits</a><a href="#demo">Live demo</a></div>
    <div class="section-head reveal" id="use-cases"><span class="eyebrow violet">How businesses use it</span><h2>Where {a["name"]} earns its place.</h2></div>
    <div class="grid-3">{uses}</div>
  </div>
</section>

<section class="section violet" id="fit">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow violet">How it fits</span>
      <h2>{a["outcome"]}.</h2>
      <p class="lead">It runs on your own cloud and works with the systems you already use.</p>
    </div>
    <div class="works-with reveal">{works}</div>
    <div class="reveal" style="margin-top:48px">{ladder(AI_LADDER, "four v")}</div>
  </div>
</section>

{both}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow violet">Related apps</span><h2>More from the suite.</h2></div>
    <div class="apps-grid">{related}</div>
  </div>
</section>

<section class="section violet" id="demo">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow violet">Live demo</span>
        <h2>See {a["name"]} working on your own example.</h2>
        <p class="lead" style="margin-top:16px">We show the app working on your own example before you commit. Add any other apps you want to see in the same session.</p>
      </div>
      {demo_form(a["slug"])}
    </div>
  </div>
</section>
'''


# ---------------------------------------------------------------- SITEMAP PLAN
def sitemap_plan():
    def node(path, title, status, note, children=""):
        lab = {"new": "New", "upd": "Update", "keep": "Keep", "redir": "Redirect"}[status]
        ch = f'<div class="tree-children">{children}</div>' if children else ""
        href = path if path.startswith("/") and status == "new" else (LIVE + path if path.startswith("/") else path)
        return f'<div class="tree-node"><a class="path" href="{href}">{path}</a><h4>{title}<span class="status {status}">{lab}</span></h4><p>{note}</p>{ch}</div>'

    apps = "".join(node(f'/ai-applications/{a["slug"]}/', a["name"], "new", f'{a["domain"]["name"]} · {a["cat"]}') for a in ALL_APPS)
    return f'''
<section class="page-hero mint-bg">
  <div class="wrap">
    <span class="eyebrow">Internal · for review</span>
    <h1>Sitemap plan: platforms, applications, infrastructure, services.</h1>
    <p class="lead">How Message House v7 maps onto cirtec.ai. New pages are live in this preview; existing pages link to the current site. Not for publication.</p>
  </div>
</section>

<section class="section tight" style="padding-top:0">
  <div class="wrap">
    <div class="grid-2" style="align-items:start">
      <div class="tree">
        {node("/", "Home: the roof", "upd", "Roof line, five-buyer 'find your page' layer, two houses plus Infrastructure, IT &amp; Cloud, Services and Academy, the shared four apps, both ladders, proof, rules and offices.")}
        {node("/energy-infrastructure/", "House 01 · Energy & Infrastructure", "new", "Measure, Act, Transform. Six-step ladder, zero-CAPEX, cleared proof only, free EUI self-check.",
              node("/platforms/monitor-manage", "Monitor & Manage", "redir", "301 to /energy-infrastructure/#measure."))}
        {node("/infrastructure/", "Infrastructure · Power & Cooling", "new", "AI DCEM PUE guarantee, UPS/BESS/PDUs, Smart Active Tiles, racks &amp; IR Blaster, AI-in-a-Box, quote form.",
              node("/platforms/power-cooling", "Power & Cooling (old)", "redir", "301 to /infrastructure/.") +
              node("/solutions/ir-blaster", "IR Blaster (old)", "redir", "301 to /infrastructure/#racks."))}
        {node("/it-cloud/", "IT & Cloud", "new", "DBShift, application modernisation, FinOps &amp; Cloud Health, resourcing.")}
        {node("/ai-applications/", "House 02 · Enterprise AI Applications", "new", "Hub for all the AI apps: domain filter, four claims, demo ladder, demo request form.", apps)}
      </div>
      <div class="tree">
        {node("/services/", "Services", "new", "One engagement path: Audit, Advise (incl. market-entry advisory), Implement, Run (Cirtec Care). Audit types, enquiry form.")}
        {node("/ai-academy/", "CIRTEC AI Academy", "new", "Renamed from AI Bootcamp. Delivered with SGTech. Three ways in, rollout Singapore → Malaysia → Philippines.")}
        {node("/platforms/cx-operations", "AI Led Operations", "redir", "301 to /ai-applications/. Until then, point its AI Asset Manager tile at /ai-applications/ as the &quot;Discover more&quot; door into all the AI apps.")}
        {node("/solutions/ai-vision", "AI Vision (old)", "redir", "301 to /ai-applications/ai-vision/.")}
        {node("/solutions/ai-concierge", "AI Concierge (old)", "redir", "301 to /ai-applications/ai-concierge/.")}
        {node("/solutions/ai-interviewer", "AI Interviewer (old)", "redir", "301 to /ai-applications/interview-iq/. The product is now called Interview IQ.")}
        {node("/about-us", "About Us", "keep", "Keep. Update the office list to CapitaGreen, Kuala Lumpur, Manila and Chennai.")}
        {node("/contact-us", "Contact Us", "keep", "Keep. Phone is +65 9787 1732.")}
        {node("/industries/*", "Industry pages", "keep", "Keep for SEO. Add links into the relevant house from each.")}
        <div class="card" style="margin-top:6px">
          <h4>Main navigation</h4>
          <p class="small" style="margin-top:8px">Energy ▾ · AI Applications ▾ · Infrastructure ▾ · Services ▾ · About Us · <b>Live demo</b> · <b>Get in Touch</b></p>
          <h4 style="margin-top:18px">Message house rules applied</h4>
          <ul class="small muted" style="padding-left:18px;margin:8px 0 0">
            <li>New energy platform not pre-announced; no product name retired.</li>
            <li>App pages carry no outcome percentages until the deployment behind each is named and cleared.</li>
            <li>Partner hardware labelled “Partner” or by brand (BPE, EkkoSense), not “Resold”.</li>
            <li>Data-centre proof says 20+ (CIRTEC), never 2,000+ (EkkoSense global).</li>
            <li>AI Asset Manager is one product: Smart FM, AI EAM and FixByte are not used.</li>
            <li>Asset Manager, ShiftX and APM shown as part of the suite, not separate products.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
'''
