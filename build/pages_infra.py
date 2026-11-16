"""v7 additions: Infrastructure (Power & Cooling) and IT & Cloud pages."""
from layout import icon, LIVE
from pages_main import cta


def spec_card(id_, ic, eyebrow, title, desc, bullets, price):
    lis = "".join(f"<li>{icon('check')}<span>{b}</span></li>" for b in bullets)
    return f'''
<div class="svc reveal" id="{id_}">
  <div class="ic" style="width:44px;height:44px;border-radius:12px;background:var(--mint-2);color:var(--green-deep);display:grid;place-items:center">{icon(ic)}</div>
  <span class="eyebrow" style="margin-top:16px">{eyebrow}</span>
  <h3 style="margin-top:0">{title}</h3>
  <p class="muted">{desc}</p>
  <ul>{lis}</ul>
  <p style="margin-top:auto;padding-top:18px;font-family:var(--head);font-weight:700;color:var(--forest)">{price}</p>
</div>'''


def infrastructure():
    return f'''
<section class="page-hero mint-bg">
  <div class="wrap grid">
    <div>
      <div class="crumbs"><a class="back" href="/">← Home</a><span>Infrastructure</span><span>/</span><span>Power &amp; Cooling</span></div>
      <span class="eyebrow">Infrastructure · Power &amp; Cooling</span>
      <h1>The physical layer that <span class="accent">keeps it all up.</span></h1>
      <p class="lead">Backup power, cooling, server racks and private AI servers. All of it connects to our software, so you can see and improve how it runs.</p>
      <div class="btn-row"><a class="btn btn-primary" href="#data-centres">For data centres {icon("arrow")}</a><a class="btn btn-ghost" href="#enquire">Ask for a quote</a></div>
    </div>
    <div class="hero-figure"><img src="/assets/img/green-industry.jpg" alt="Green industrial landscape" width="2762" height="1016" style="aspect-ratio:4/3.2"></div>
  </div>
</section>

<section class="section tight" id="data-centres"><div class="wrap">
  <div class="callout reveal">
    <span class="q">“</span>
    <p>We put the energy saving in the contract.<small>AI DCEM puts sensors on every rack and cooling unit, shows a live 3D map of heat in your data hall, and tells your team exactly what to adjust. The efficiency gain is guaranteed every quarter. Running in 20+ data centres, including CBRE, BT, Visa and Telefónica.</small></p>
    <a class="btn btn-primary" href="/energy-infrastructure/#measure">See AI DCEM {icon("arrow")}</a>
  </div>
</div></section>

<section class="section mint">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow">The physical layer</span><h2>What we supply.</h2><p class="lead">Prices are starting points. Every quote is based on your site.</p></div>
    <div class="grid-2">
      {spec_card("power", "battery", "BPE · exclusive Southeast Asia distribution", "Backup power &amp; batteries",
                 "Always-on backup power, lithium battery storage and smart power strips, at 30–50% below the big brands' list prices.",
                 ["Backup power from a single office to a full data hall", "Battery storage, from one rack to shipping-container size", "Smart power strips you can monitor and switch remotely", "Shows up on the same dashboard as your other systems"],
                 "From USD 1,600 (10 kVA)")}
      {spec_card("tiles", "fan", "BPE", "Smart Active Tiles",
                 "A floor tile with built-in fans. It swaps in for a normal tile in minutes and sends cold air to the racks that are running hot.",
                 ["Fans you can replace without switching off", "30-minute backup", "Racks up to 4°C cooler", "About 7% less cooling energy for every 1°C warmer you can run the room"],
                 "From USD 100 per tile pilot")}
      {spec_card("racks", "server", "Racks &amp; comfort cooling", "Racks &amp; IR Blaster",
                 "Strong server racks with smart locks. IR Blaster adds AI scheduling to ordinary wall and ceiling air-cons.",
                 ["Server racks for any size of room", "Smart locks that log who opened each rack", "IR Blaster switches air-con by weather and by who is in the room", "30% average saving on comfort cooling"],
                 "IR Blaster SGD 220 per device")}
      {spec_card("ai-in-a-box", "cpu", "Private AI", "AI Factory / AI-in-a-Box",
                 "Everything you need to run AI on your own premises, in one rack. Installed in four weeks, with a five-year warranty. Built on Dell, Lenovo and NVIDIA.",
                 ["Runs AI Vision or Carbon Cast on-premise", "Your data never leaves your building", "Sizes from one site to a full private cloud", "Deployed in four weeks"],
                 "From USD 25k (Edge XS)")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Why operators pair the layers</span>
        <h2>One partner, one data model.</h2>
        <p class="lead" style="margin-top:16px">AI DCEM finds the hot spots. Smart Active Tiles cool them. Backup power reports to the same screen. Carbon Cast turns the energy figures into the carbon reports your auditors ask for.</p>
      </div>
      <div class="ladder reveal" style="grid-template-columns:1fr 1fr">
        <div class="rung first"><span class="n">Find</span><h4>AI DCEM</h4><p>A live map of heat and power.</p></div>
        <div class="rung"><span class="n">Fix</span><h4>Smart Active Tiles</h4><p>Air where the heat actually is.</p></div>
        <div class="rung"><span class="n">Protect</span><h4>Backup power &amp; batteries</h4><p>Power that never blinks.</p></div>
        <div class="rung"><span class="n">Report</span><h4>Carbon Cast</h4><p>Energy figures into carbon reports.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section mint" id="enquire">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Ask for a quote</span>
        <h2>Tell us what you need to power or cool.</h2>
        <p class="lead" style="margin-top:16px">A list of your racks, your power use or a site drawing is enough to start. We come back within five working days.</p>
      </div>
      <div class="form-card reveal">
        <form data-lead-form data-endpoint="">
          <div class="form-grid">
            <div class="field"><label for="i-name">Name</label><input id="i-name" required></div>
            <div class="field"><label for="i-co">Company</label><input id="i-co" required></div>
            <div class="field"><label for="i-email">Work email</label><input id="i-email" type="email" required></div>
            <div class="field"><label for="i-what">Interested in</label><select id="i-what"><option>AI DCEM (data centre)</option><option>Backup power &amp; batteries</option><option>Smart Active Tiles</option><option>Racks or IR Blaster</option><option>AI Factory / AI-in-a-Box</option></select></div>
            <div class="field full"><label for="i-msg">Site details</label><textarea id="i-msg" rows="3" placeholder="Racks, load, location"></textarea></div>
          </div>
          <button class="btn btn-primary" type="submit" style="margin-top:16px">Request a quote {icon("arrow")}</button>
        </form>
        <div class="form-success"><div class="tick">{icon("check")}</div><h4>Thank you</h4><p class="small muted">We will reply within five working days.</p></div>
      </div>
    </div>
  </div>
</section>
'''


def it_cloud():
    return f'''
<section class="page-hero violet-bg">
  <div class="wrap grid">
    <div>
      <div class="crumbs"><a class="back" href="/">← Home</a><span>Infrastructure</span><span>/</span><span>IT &amp; Cloud</span></div>
      <span class="eyebrow violet">IT &amp; Cloud</span>
      <h1>Get your data and systems ready for AI.</h1>
      <p class="lead">Old databases, wasted cloud spend and data that can't leave the building stop most AI projects before they start. We sort that out first, then add AI.</p>
      <div class="btn-row"><a class="btn btn-violet" href="#enquire">Talk to an engineer {icon("arrow")}</a><a class="btn btn-ghost" href="/ai-applications/">See the AI apps</a></div>
    </div>
    <div class="mock">
      <div class="mock-bar"><i></i><i></i><i></i><b>DBShift · migration run</b></div>
      <div class="row"><span class="pill">SQL Server</span><span class="pill">Oracle</span><span class="pill">DB2</span><span class="pill">Teradata</span></div>
      <div class="center" style="margin:10px 0;color:var(--violet)">{icon("migrate")}</div>
      <div class="row"><span class="pill v">Snowflake</span><span class="pill v">PostgreSQL</span><span class="pill v">Azure</span></div>
      <div class="list" style="margin-top:12px"><div class="li">Tables converted <em>25 of 25</em></div><div class="li">Pipelines <em>50 built</em></div><div class="li">Code documented <em>yes</em></div></div>
      <p class="caption-note">Illustrative product visual</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow violet">Four ways in</span><h2>Four ways we help.</h2></div>
    <div class="grid-2">
      <div class="svc reveal" id="dbshift"><span class="eyebrow violet">Cloud migration</span><h3>DBShift</h3>
        <p class="muted">Moves old databases (SQL Server, Oracle, DB2, Teradata) to modern cloud platforms, using AI to do most of the work. Delivered with Systech.</p>
        <ul><li>{icon("check")}<span>Your first working reporting database in four weeks</span></li><li>{icon("check")}<span>Code converted 8× faster</span></li><li>{icon("check")}<span>70% lower cost than manual modernisation</span></li></ul>
        <p style="margin-top:auto;padding-top:18px;font-family:var(--head);font-weight:700;color:var(--violet)">Project-quoted</p></div>
      <div class="svc reveal" id="modernisation"><span class="eyebrow violet">Analog to digital</span><h3>Application modernisation</h3>
        <p class="muted">Paper logbooks, gate passes and inspection forms turned into digital, AI-assisted steps.</p>
        <ul><li>{icon("check")}<span>Old software connected to new tools</span></li><li>{icon("check")}<span>Linked up through our Orbit app</span></li><li>{icon("check")}<span>So the AI suite can reach the systems you already run</span></li></ul></div>
      <div class="svc reveal" id="finops"><span class="eyebrow violet">Cloud cost</span><h3>Cloud cost control</h3>
        <p class="muted">See what you spend on Azure, AWS and Google Cloud, cut what you don't need, and see the energy and carbon behind each system.</p>
        <ul><li>{icon("check")}<span>Cut servers you don't need</span></li><li>{icon("check")}<span>Show each team its own cost and carbon</span></li><li>{icon("check")}<span>Option to pay from the money you save</span></li></ul>
        <p style="margin-top:auto;padding-top:18px;font-family:var(--head);font-weight:700;color:var(--violet)">From USD 400/month</p></div>
      <div class="svc reveal" id="resourcing"><span class="eyebrow violet">People</span><h3>Resourcing &amp; engineering</h3>
        <p class="muted">Building-control engineers, data engineers, software developers and AI product managers.</p>
        <ul><li>{icon("check")}<span>On retainer, on project or embedded in your team</span></li><li>{icon("check")}<span>Across Singapore, Malaysia, the Philippines and India</span></li></ul></div>
    </div>
  </div>
</section>

{cta("Not ready for AI yet? Start here.", "Tell us what is holding the data back, and we will scope the fix before anyone talks about models.", ("Talk to an engineer", f"{LIVE}/contact-us"), ("See AI-in-a-Box", "/infrastructure/#ai-in-a-box"), violet=True).replace('<section class="section tight">', '<section class="section tight" id="enquire">', 1)}
'''
