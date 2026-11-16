"""v7 Services (one engagement ladder) and CIRTEC AI Academy pages."""
from layout import icon, PHONE, PHONE_TEL


def _stage(id_, n, title, sub, desc, items, foot, feature=False):
    lis = "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items)
    f = " feature" if feature else ""
    return f'''
<div class="svc{f} reveal" id="{id_}">
  <span class="eyebrow">{n} · {sub}</span>
  <h3 style="margin-top:0">{title}</h3>
  <p class="muted">{desc}</p>
  <ul>{lis}</ul>
  <p style="margin-top:auto;padding-top:18px;font-family:var(--head);font-weight:700;color:var(--forest)">{foot}</p>
</div>'''


def services():
    return f'''
<section class="page-hero mint-bg">
  <div class="wrap">
    <div class="crumbs"><a class="back" href="/">← Home</a><span>Services</span></div>
    <span class="eyebrow">Services · one engagement path</span>
    <h1>Audit. Advise. Implement. Run.</h1>
    <p class="lead">Everything we do follows the same four steps, so a target or a legal requirement becomes a clear plan with costs and savings you can see. Buy a product, or just our people's time.</p>
    <div class="btn-row"><a class="btn btn-primary" href="#enquire">Book an audit {icon("arrow")}</a><a class="btn btn-ghost" href="/energy-infrastructure/#eui-check">Free energy check</a></div>
  </div>
</section>

<section class="section tight" style="padding-top:0">
  <div class="wrap">
    <div class="grid-2">
      {_stage("audit", "1", "Audit", "Entry point",
              "Certified engineers check your energy and water use, onsite or remote, and show you where the savings are. The easiest place to start.",
              ["Electrical, chilled-water, compressed-air, boiler, water and pumping", "How much of your equipment you really use, your backup plans and your sustainability gaps", "Registered engineers for Singapore's mandatory energy-improvement filings", "Customers usually cut energy costs by 15–35% within 12–18 months of acting on the audit"],
              "Fixed fee, USD 5k–25k", feature=True)}
      <div id="consulting" style="display:contents"></div>
      {_stage("advise", "2", "Advise", "Consulting &amp; advisory",
              "Clear plans with the numbers attached: what it costs to buy, what it costs to run, and what you get back.",
              ["Step-by-step plans to reach net-zero and energy certification", "Help to earn green building ratings", "Plans for sensors and upgrades in existing buildings", "<b>Market-entry advisory</b> for manufacturers setting up in a new country: work permits, site visits and regulatory coordination"],
              "USD 200/hr or retainer")}
      {_stage("implement", "3", "Implement", "Delivery",
              "Non-intrusive installation over the infrastructure you already run.",
              ["Setting up our AI apps, including on your own servers", "Connecting sensors and building controls", "Upgrading data centres and air-con", "Installing air-quality sensors, backup power and batteries, and checking the savings are real"],
              "Fixed price or hourly")}
      {_stage("run", "4", "Run · Cirtec Care", "Managed services",
              "We stay with you after go-live, so the savings last.",
              ["Day-to-day technical support, and staff when you need them", "Longer warranties and contracts that guarantee results", "Paperwork for green building ratings", "Annual sustainability-report authoring"],
              "Yearly fee or subscription")}
    </div>
  </div>
</section>

<section class="section mint">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Engineering audits we run</span><h2>What we measure.</h2></div>
    <div class="table-wrap reveal"><table class="table">
      <thead><tr><th>Audit</th><th>What we measure</th></tr></thead>
      <tbody>
        <tr><td>Electrical</td><td>When and where you use power, power quality, motor efficiency and heat-camera checks for faults</td></tr>
        <tr><td>Chiller &amp; HVAC</td><td>How efficiently your chillers and cooling towers turn power into cooling</td></tr>
        <tr><td>Compressed air</td><td>How much air you really need, where it leaks and how much energy it uses</td></tr>
        <tr><td>Boiler &amp; steam</td><td>How much fuel your boilers waste and where steam leaks</td></tr>
        <tr><td>Water &amp; pumping</td><td>Pump efficiency, leaks and where your water goes</td></tr>
      </tbody>
    </table></div>
  </div>
</section>

<section class="section" id="enquire">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Enquire</span>
        <h2>Tell us what you need.</h2>
        <p class="lead" style="margin-top:16px">We come back with a scoped proposal within five working days. Or call <a href="tel:{PHONE_TEL}" class="accent">{PHONE}</a>.</p>
      </div>
      <div class="form-card reveal">
        <form data-lead-form data-endpoint="">
          <div class="form-grid">
            <div class="field"><label for="s-name">Name</label><input id="s-name" required></div>
            <div class="field"><label for="s-co">Company</label><input id="s-co" required></div>
            <div class="field"><label for="s-email">Work email</label><input id="s-email" type="email" required></div>
            <div class="field"><label for="s-country">Country</label><select id="s-country"><option>Singapore</option><option>Malaysia</option><option>Philippines</option><option>India</option><option>Middle East</option><option>Other</option></select></div>
            <div class="field full"><label for="s-svc">Service</label><select id="s-svc"><option>Energy or water audit</option><option>Engineering audit</option><option>Consulting &amp; advisory</option><option>Market-entry advisory</option><option>Implementation</option><option>Cirtec Care managed services</option></select></div>
            <div class="field full"><label for="s-msg">What should we know?</label><textarea id="s-msg" rows="3"></textarea></div>
          </div>
          <button class="btn btn-primary" type="submit" style="margin-top:16px">Send enquiry {icon("arrow")}</button>
        </form>
        <div class="form-success"><div class="tick">{icon("check")}</div><h4>Thank you</h4><p class="small muted">We will reply within five working days.</p></div>
      </div>
    </div>
  </div>
</section>
'''


def academy():
    ck = icon("check")
    amber = "background:#fff3dc;color:#b86b00"
    return f'''
<section class="page-hero" style="background:radial-gradient(1100px 520px at 85% -10%, #fff0d6 0%, rgba(255,240,214,0) 60%), linear-gradient(180deg,#fffcf6,#fff)">
  <div class="wrap grid">
    <div>
      <div class="crumbs"><a class="back" href="/">← Home</a><a href="/services/">Services</a><span>/</span><span>CIRTEC AI Academy</span></div>
      <span class="eyebrow" style="color:#b86b00">CIRTEC AI Academy · Launching November 2026</span>
      <h1>Who runs this after we leave? <span style="color:#d98a12">Your team.</span></h1>
      <p class="lead">Hands-on AI training for working professionals: how to plan, build, test and launch AI tools at work. Run with SGTech.</p>
      <div class="btn-row"><a class="btn btn-primary" href="#register">Register interest {icon("arrow")}</a><a class="btn btn-ghost" href="#ways-in">Training for a team</a></div>
    </div>
    <div class="card" style="padding:32px">
      <span class="eyebrow">What you will be able to do</span>
      <div class="svc" style="padding:0;border:0;box-shadow:none"><ul>
        <li>{ck} <span><b>Design</b> an AI solution around a real business problem</span></li>
        <li>{ck} <span><b>Build</b> it with modern models and tooling</span></li>
        <li>{ck} <span><b>Evaluate</b> whether it actually works, with evidence</span></li>
        <li>{ck} <span><b>Deploy</b> it into a governed enterprise environment</span></li>
      </ul></div>
      <p class="small muted" style="margin-top:18px">Packaged by CIRTEC and hosted on CIRTEC's Azure environment.</p>
    </div>
  </div>
</section>

<section class="section mint" id="ways-in">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow">Who it is for</span><h2>Three ways in.</h2></div>
    <div class="grid-3">
      <div class="card top-line a reveal"><div class="ic" style="{amber}">{icon("user")}</div><h3>For yourself</h3><p>Software, data, IT and digital-transformation professionals. A global digital subscription you can start on your own.</p></div>
      <div class="card top-line a reveal"><div class="ic" style="{amber}">{icon("users")}</div><h3>For your team</h3><p>L&amp;D and HR leaders buying for a team. A listed programme that can be funded through training vouchers where your market offers them.</p></div>
      <div class="card top-line a reveal"><div class="ic" style="{amber}">{icon("building")}</div><h3>For your enterprise</h3><p>An enterprise bundle alongside AI hardware, available through our distribution partners.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Why it matters</span>
        <h2>Train the team that will run it.</h2>
        <p class="lead" style="margin-top:16px">Every new system raises the same question: who looks after it once the project team has gone? The Academy trains your own people to do it, and to judge any AI they buy, including ours.</p>
        <div class="btn-row"><a class="btn btn-violet" href="/ai-applications/">See the AI apps {icon("arrow")}</a></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Rolling out</span>
        <div class="ladder three">
          <div class="rung first"><span class="n">First</span><h4>Singapore</h4><p>Launching November 2026.</p></div>
          <div class="rung"><span class="n">Next</span><h4>Malaysia</h4><p>After the Singapore cohorts.</p></div>
          <div class="rung"><span class="n">Then</span><h4>Philippines</h4><p>After Malaysia.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section mint" id="register">
  <div class="wrap">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Register interest</span>
        <h2>Be first into the next cohort.</h2>
        <p class="lead" style="margin-top:16px">Tell us whether you are joining on your own or bringing a team, and we will send dates, format and funding options for your market.</p>
      </div>
      <div class="form-card reveal">
        <form data-lead-form data-endpoint="">
          <div class="form-grid">
            <div class="field"><label for="b-name">Name</label><input id="b-name" required></div>
            <div class="field"><label for="b-email">Email</label><input id="b-email" type="email" required></div>
            <div class="field"><label for="b-country">Country</label><select id="b-country"><option>Singapore</option><option>Malaysia</option><option>Philippines</option><option>Other</option></select></div>
            <div class="field"><label for="b-type">Joining as</label><select id="b-type"><option>An individual</option><option>A team (L&amp;D / HR)</option><option>An enterprise</option></select></div>
            <div class="field full"><label for="b-role">Role</label><input id="b-role" placeholder="e.g. Data engineer, L&amp;D manager"></div>
          </div>
          <button class="btn btn-primary" type="submit" style="margin-top:16px">Register interest {icon("arrow")}</button>
        </form>
        <div class="form-success"><div class="tick">{icon("check")}</div><h4>You are on the list</h4><p class="small muted">We will send cohort dates for your market.</p></div>
      </div>
    </div>
  </div>
</section>
'''
