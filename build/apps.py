"""The 17 apps of the Enterprise AI Application Suite.

Source: CIRTEC_AI_Application_Suite_Brochure.pdf (Oct 2026) and Message House v6.
Outcome percentages from the brochure (55%, 62%, <3 hrs, 70%, 85%) are NOT used:
the message house says to quote outcome figures only once the deployment behind
each one is named and cleared.
"""

# ---------- illustrative mock visuals (CSS only) ----------

M_AIVISION = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>AI Vision · Gate 3 · Cam 07</b><span class="live">LIVE</span></div>
<div class="cam"><div class="box" style="left:12%;top:30%;width:18%;height:52%"><b>Zone breach</b></div>
<div class="box g" style="left:55%;top:26%;width:15%;height:56%"><b>Authorised</b></div>
<div class="box g" style="left:76%;top:40%;width:12%;height:40%"><b>Vehicle</b></div></div>
<div class="row" style="margin-top:12px"><span class="pill alert">● Zone breach detected</span><span class="pill">Alert sent in under 2 s</span></div>
<div class="list" style="margin-top:12px"><div class="li">Forensic clip attached <em>00:14 · 3 frames</em></div></div></div>'''

M_SAFEWATCH = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>SafeWatch · Plant floor</b><span class="live">EDGE</span></div>
<div class="row"><div class="panel"><div class="lbl">Feeds online</div><div class="big">100+</div></div><div class="panel"><div class="lbl">Inference</div><div class="big" style="font-size:1.1rem;margin-top:8px">On-premise</div></div></div>
<div class="panel" style="margin-top:10px"><div class="lbl">PPE violations by shift</div><div class="bars"><span style="height:70%"></span><span style="height:45%"></span><span style="height:30%"></span><span style="height:22%"></span><span style="height:16%"></span><span style="height:12%"></span></div></div>
<div class="row" style="margin-top:10px"><span class="pill alert">No hard hat · Hoist 2</span><span class="pill ok">Forklift lane clear</span></div></div>'''

M_CARBON = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Carbon Cast · Emissions inventory</b></div>
<div class="row"><div class="panel"><div class="lbl">Scope 1</div><div class="meter"><i style="width:22%"></i></div></div><div class="panel"><div class="lbl">Scope 2</div><div class="meter"><i style="width:48%"></i></div></div><div class="panel"><div class="lbl">Scope 3</div><div class="meter"><i style="width:86%"></i></div></div></div>
<div class="panel" style="margin-top:10px"><div class="lbl">Net-zero pathway to 2050</div><div class="bars"><span style="height:95%"></span><span style="height:84%"></span><span style="height:70%"></span><span style="height:55%"></span><span style="height:38%"></span><span style="height:20%"></span><span style="height:8%"></span></div></div>
<div class="row" style="margin-top:10px"><span class="pill ok">Utility bill parsed</span><span class="pill v">GHG Protocol · GRI</span></div></div>'''

M_ECOLENS = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>EcoLensAI · Walk-through audit</b><span class="live">LIVE</span></div>
<div class="row"><div class="cam" style="aspect-ratio:3/4"><div class="box g" style="left:10%;top:12%;width:70%;height:22%"><b>Split AC · filter due</b></div><div class="box g" style="left:18%;top:55%;width:55%;height:30%"><b>Display · standby</b></div></div>
<div><div class="panel"><div class="lbl">Compliance score</div><div class="big">86</div></div><div class="list" style="margin-top:10px"><div class="li">3 appliances <em>found</em></div><div class="li">1 issue <em>logged</em></div><div class="li">Actions <em>75% closed</em></div></div></div></div></div>'''

M_CONCIERGE = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>AI Concierge · Lobby kiosk</b><span class="live">LIVE</span></div>
<div class="row"><div class="avatar"></div><div style="display:grid;gap:8px;align-content:center">
<div class="bubble me">Can I move my booking to Friday and add a spa slot?</div>
<div class="bubble ai">Done. Friday, 2 nights, and a 4pm spa slot. Shall I send it to WhatsApp?</div></div></div>
<div class="row" style="margin-top:12px"><span class="pill v">Kiosk</span><span class="pill v">Web</span><span class="pill v">WhatsApp</span><span class="pill v">Mobile</span></div></div>'''

M_CHEF = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Digital Twin AI Chef · Food-court screen</b><span class="live">LIVE</span></div>
<div class="avatar" style="aspect-ratio:16/8"></div>
<div class="bubble ai" style="margin-top:12px">Tonight I recommend the laksa. Shall I show you what is in it?</div>
<div class="list" style="margin-top:10px"><div class="li">Laksa <em>Allergens: shellfish</em></div><div class="li">Chicken rice <em>Recommended</em></div></div></div>'''

M_PROMO = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>PromoIQ · Campaign studio</b></div>
<div class="row"><div class="panel"><div class="lbl">Segments</div><div class="list" style="margin-top:6px"><div class="li">High value</div><div class="li">Rising</div><div class="li">At risk</div><div class="li">New</div></div></div>
<div><div class="panel" style="background:var(--violet);color:#fff;border:0"><div class="lbl" style="color:#d9d3ff">Tonight only</div><div class="big" style="color:#fff">2× points</div><div style="font-size:.72rem;opacity:.85">Written for this member · delivered in real time</div></div>
<div class="panel" style="margin-top:8px"><div class="lbl">A/B test</div><div class="row" style="margin-top:6px"><span class="pill">A</span><span class="pill ok">B wins</span></div></div></div></div></div>'''

M_INTERVIEW = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Interview IQ · Senior Analyst · Round 1</b><span class="live">REC</span></div>
<div class="row"><div class="avatar" style="aspect-ratio:1"></div><div class="panel"><div class="lbl">Rubric score</div>
<div style="font-size:.74rem;margin-top:8px">Communication<div class="meter"><i style="width:82%"></i></div></div>
<div style="font-size:.74rem;margin-top:6px">Problem solving<div class="meter"><i style="width:74%"></i></div></div>
<div style="font-size:.74rem;margin-top:6px">Role knowledge<div class="meter"><i style="width:88%"></i></div></div></div></div>
<div class="row" style="margin-top:12px"><span class="pill v">Proctored</span><span class="pill">Question 3 of 8</span><span class="pill ok">Strong match for the role</span></div></div>'''

M_SKILL = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>SkillIQ · challenge_07.sql</b><span class="live">24:10</span></div>
<div class="code"><span class="k">SELECT</span> store, SUM(qty)<br><span class="k">FROM</span> sales <span class="k">GROUP BY</span> store<br><span class="k">HAVING</span> SUM(qty) &gt; 100;</div>
<div class="row" style="margin-top:10px"><span class="pill ok">Auto-graded · 9 of 10 tests pass</span><span class="pill v">P92</span></div>
<div class="panel" style="margin-top:10px"><div class="lbl">Skills map · SQL · Python · Spark · ML</div><div class="heat" style="margin-top:8px">
<i style="background:#6b57e3"></i><i style="background:#8f80ef"></i><i style="background:#b9aff7"></i><i style="background:#ddd8fb"></i><i style="background:#8f80ef"></i>
<i style="background:#b9aff7"></i><i style="background:#6b57e3"></i><i style="background:#ddd8fb"></i><i style="background:#8f80ef"></i><i style="background:#b9aff7"></i></div></div></div>'''

M_RESONANCE = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Resonance · Practice: quarterly update to the board</b></div>
<div class="row"><div class="panel"><div class="lbl">Pace</div><div class="big">142<small style="font-size:.7rem"> wpm</small></div></div><div class="panel"><div class="lbl">Fillers</div><div class="big">3</div></div><div class="panel"><div class="lbl">Clarity</div><div class="big">84</div></div></div>
<div class="panel" style="margin-top:10px"><div class="lbl">Executive presence · week 1 → week 5</div><div class="bars"><span style="height:40%"></span><span style="height:52%"></span><span style="height:61%"></span><span style="height:70%"></span><span style="height:78%"></span></div></div></div>'''

M_RETAIL = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>RetailIQ · Store operations</b></div>
<div class="bubble me">How many units of SKU 4471 in Jurong East?</div>
<div class="code" style="margin-top:10px"><span class="k">SELECT</span> store, qty <span class="k">FROM</span> stock<br><span class="k">WHERE</span> sku = 4471 <span class="k">AND</span> area = 'Jurong East'</div>
<div class="bubble ai" style="margin-top:10px">128 units across 3 stores. Jurong East Mall 64 · Westgate 41 · IMM 23.</div>
<div class="row" style="margin-top:10px"><span class="pill v">Looked up in your stock system</span><span class="pill">Policy answers from your documents</span></div></div>'''

M_QUOTE = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Quote Generator · Q-1042 · valid 30 days</b></div>
<div class="bubble me">12 access points with mounts for Level 3</div>
<div class="list" style="margin-top:10px"><div class="li">Wi-Fi 6 access point <em>× 12</em></div><div class="li">Ceiling mount kit <em>× 12</em></div><div class="li">PoE switch, 24 port <em>× 1</em></div><div class="li">Installation <em>× 1</em></div></div>
<div class="row" style="margin-top:10px"><span class="pill ok">From live inventory</span><span class="pill v">+ Suggested bundle</span><span class="pill">PDF</span></div></div>'''

M_DRLOOPS = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Dr.Loops · Patient education</b><span class="live">0:42</span></div>
<div class="avatar" style="aspect-ratio:16/8"></div>
<div class="panel" style="margin-top:10px;font-family:var(--body);font-size:.85rem">“Keep the dressing dry for 48 hours.”</div>
<div class="row" style="margin-top:10px"><span class="pill v">English</span><span class="pill v">Mandarin</span><span class="pill v">Malay</span><span class="pill v">Tamil</span></div></div>'''

M_AIDE = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>aiDE · Semantic workspace</b></div>
<div class="bubble me">Build a daily sales pipeline with quality checks</div>
<div class="row" style="margin-top:10px"><span class="pill">Microsoft Fabric</span><span class="pill">Snowflake</span><span class="pill">Databricks</span></div>
<div class="list" style="margin-top:10px"><div class="li">Pipeline built <em>by agent</em></div><div class="li">Schemas mapped <em>3 platforms</em></div><div class="li">12 data-quality rules <em>pass</em></div><div class="li">Data tools <em>3 connected</em></div></div></div>'''

M_OPS = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Ops Reporting Portal · Daily remittance summary</b></div>
<div class="row"><div class="panel" style="flex:.6"><div class="lbl">Fields</div><div class="list" style="margin-top:6px"><div class="li">Corridor</div><div class="li">Currency</div><div class="li">Amount</div><div class="li">Status</div></div></div>
<div class="panel"><div class="lbl">Volume by corridor</div><div class="bars"><span style="height:80%"></span><span style="height:60%"></span><span style="height:45%"></span><span style="height:30%"></span></div></div></div>
<div class="row" style="margin-top:10px"><span class="pill">PDF</span><span class="pill">Excel</span><span class="pill alert">Raise incident</span><span class="pill">2 comments</span></div></div>'''

M_INTELLI = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Intelliframe · Sales dashboard v1</b></div>
<div class="row" style="gap:8px"><div class="wf" style="height:46px"></div><div class="wf" style="height:46px"></div><div class="wf" style="height:46px"></div></div>
<div class="row" style="gap:8px;margin-top:8px"><div class="wf" style="height:110px;flex:2"></div><div class="wf" style="height:110px"></div></div>
<div class="row" style="margin-top:10px"><span class="pill v">Schema-aware</span><span class="pill v">Design-system aware</span><span class="pill">PNG · PDF · JSON</span></div></div>'''

M_ORBIT = '''
<div class="mock"><div class="mock-bar"><i></i><i></i><i></i><b>Orbit · Service desk in Microsoft Teams</b></div>
<div class="kan"><div><span class="t">New · 4</span><span class="c">INC-2041</span><span class="c">INC-2042</span><span class="c">INC-2043</span></div>
<div><span class="t">In progress · 6</span><span class="c red">INC-2048 · 00:12</span><span class="c">INC-2049</span><span class="c">INC-2050</span></div>
<div><span class="t">Resolved · 12</span><span class="c">INC-2055</span><span class="c">INC-2056</span></div></div>
<div class="row" style="margin-top:10px"><span class="pill alert">SLA breach in 12 min</span><span class="pill">Escalated to duty manager</span></div></div>'''


DOMAINS = [
    {
        "slug": "security-safety", "name": "Security & Safety", "icon": "shield",
        "line": "Computer vision that turns passive cameras into real-time protection for people, sites and assets.",
        "apps": [
            dict(slug="ai-vision", name="AI Vision", cat="Intelligent surveillance", icon="cam", both=True,
                 short="Turns the cameras you already have into a 24/7 security guard.",
                 headline="Every camera becomes an extra set of eyes.",
                 desc="AI Vision turns the CCTV you already own into an active security layer. Several AI models watch every camera at once and flag zone breaches, safety hazards and anomalies, with alerts dispatched in under two seconds. Every alert comes with the video clip, so your team can act straight away.",
                 caps=["Works with existing CCTV", "Several AI models on every feed", "Alerts in under 2 seconds", "Video evidence with every alert"],
                 uses=[("Perimeters and restricted zones", "Flag intrusions at plants, warehouses and data halls the moment a line is crossed."),
                       ("Operational hazard watch", "Spot unsafe conditions and anomalies on production floors before they become incidents."),
                       ("Multi-site command centres", "Give security teams one alert stream across campuses, malls and transport hubs.")],
                 works=["Existing IP cameras and NVRs", "RTSP streams", "Cloud, edge or on-premise"],
                 outcome="Faster incident response, on cameras you already own", mock=M_AIVISION,
                 existing=True),
            dict(slug="safewatch", name="SafeWatch", cat="Worker safety & PPE", icon="shield", both=True,
                 short="Spots missing hard hats and people in no-go zones across 100+ cameras, on your own site.",
                 headline="Safety compliance that never looks away.",
                 desc="SafeWatch detects missing PPE such as hard hats and catches restricted-zone intrusions across more than 100 concurrent camera feeds. The AI runs on your own premises, so alerts are fast and video never leaves the site. Ideal for factories and construction sites.",
                 caps=["PPE detection, including hard hats", "Restricted-zone intrusion alerts", "100+ concurrent camera feeds", "Video stays on your site"],
                 uses=[("Construction sites", "Check hard-hat compliance at gates, hoists and work fronts on every shift."),
                       ("Factories and plants", "Guard machine cells, forklift lanes and other restricted zones in real time."),
                       ("EHS reporting", "Turn detections into shift-level evidence for audits and toolbox talks.")],
                 works=["Existing site CCTV", "On-premise edge servers", "EHS reporting packs"],
                 outcome="Fewer recordable incidents, evidence for every shift", mock=M_SAFEWATCH),
        ],
    },
    {
        "slug": "sustainability-esg", "name": "Sustainability & ESG", "icon": "leaf",
        "line": "From utility bill to board-ready disclosure, with audits that run continuously.",
        "apps": [
            dict(slug="carbon-cast", name="Carbon Cast", cat="ESG & carbon accounting", icon="leaf", both=True, logo="carbon-cast.png",
                 short="Turns utility bills into carbon reports your auditors accept.",
                 headline="Measure, analyse and report. In hours, not weeks.",
                 desc="Carbon Cast reads your utility bills and invoices automatically, works out your carbon emissions (from your own sites, the energy you buy and your suppliers), drafts the written report, and shows what different net-zero plans would deliver. It follows the main international reporting standards.",
                 caps=["Reads utility bills automatically", "Emissions from your sites, energy and suppliers", "Report text drafted for you", "Compares net-zero plans"],
                 uses=[("Annual sustainability reporting", "Produce disclosure-ready narratives for listed companies and their assurers."),
                       ("Multi-site carbon baselines", "Consolidate utility data from buildings, plants and data centres into one inventory."),
                       ("Net-zero planning", "Model reduction pathways and show the board what each scenario delivers.")],
                 works=["Utility bills and invoices", "EnergyLoop and EMS meter data", "ERP via REST"],
                 outcome="Reporting cycles measured in hours, not weeks", mock=M_CARBON),
            dict(slug="ecolensai", name="EcoLensAI", cat="Vision-based auditing", icon="scan", both=True,
                 short="Point a phone camera at a room and get an energy audit.",
                 headline="Point a camera. Get an audit.",
                 desc="EcoLensAI runs audits through the camera of a phone, laptop or VR headset. It recognises appliances in real time, logs issues as the auditor walks the site, recommends corrective actions and scores compliance on a live dashboard.",
                 caps=["Phone, laptop or VR headset", "Recognises equipment as you walk", "Issues and corrective actions logged", "Live compliance scoring"],
                 uses=[("Building energy audits", "Walk a floor once and leave with a logged, scored inventory of what was found."),
                       ("Shops and restaurants", "Run the same audit across every outlet and compare the scores."),
                       ("Certification readiness", "Track corrective actions to closure ahead of green-building assessments.")],
                 works=["Phones and laptops", "VR headsets", "Live compliance dashboard"],
                 outcome="Audits become continuous, not periodic", mock=M_ECOLENS),
        ],
    },
    {
        "slug": "hospitality-gaming", "name": "Hospitality & Gaming", "icon": "bell",
        "line": "Conversational agents and avatars that serve every guest, on every channel, at any hour.",
        "apps": [
            dict(slug="ai-concierge", name="AI Concierge", cat="Hotel booking agent", icon="bell",
                 short="A lifelike booking agent on every guest channel.",
                 headline="The always-on team member who remembers every guest.",
                 desc="AI Concierge is a conversational agent with a lifelike avatar. It handles bookings from start to finish, takes spa and dining reservations and handles guest requests across every channel, from the lobby kiosk to the guest's own phone.",
                 caps=["Lifelike avatar", "Bookings from start to finish", "Amenity and guest requests", "Every guest channel"],
                 uses=[("Reservations desk, 24/7", "Make, change and cancel bookings without a queue at the front desk."),
                       ("Amenity and dining sales", "Offer spa, dining and experiences at the moment guests are deciding."),
                       ("In-stay guest requests", "Take housekeeping, late check-out and service requests on any channel.")],
                 works=["Kiosk, web, WhatsApp and mobile", "Booking and PMS systems", "CRM and helpdesk"],
                 outcome="A lighter front desk and more ancillary revenue", mock=M_CONCIERGE, existing=True),
            dict(slug="digital-twin-ai-chef", name="Digital Twin AI Chef", cat="F&B video avatar", icon="chef",
                 short="A lip-synced AI chef that recommends dishes around the clock.",
                 headline="A chef on every screen, around the clock.",
                 desc="A lip-synced AI presenter that recommends dishes, guides guests through recipes and displays allergen information at any hour of the day.",
                 caps=["Lip-synced AI presenter", "Dish recommendations", "Allergen and dietary display", "Guided recipes in your brand voice"],
                 uses=[("Restaurant and food-court kiosks", "Recommend dishes while guests browse the menu."),
                       ("Allergen and dietary guidance", "Show allergen information clearly before the order is placed."),
                       ("Guided recipes", "Walk guests through a recipe step by step, in the brand's own voice.")],
                 works=["Kiosks and digital menu boards", "Your menu and allergen data", "Web and mobile"],
                 outcome="An always-on guest engagement channel", mock=M_CHEF),
            dict(slug="promoiq", name="PromoIQ", cat="Personalised promotions", icon="tag",
                 short="The right offer for the right member, written and sent in real time.",
                 headline="The right offer for the right player, right now.",
                 desc="PromoIQ groups your members by how much they spend and how likely they are to respond, writes a personal offer for each, sends it instantly on any channel, and tests which offers work best.",
                 caps=["Groups members by value and likely response", "AI-written offer copy", "Real-time multi-channel delivery", "Tests which offers work best"],
                 uses=[("Loyalty programme offers", "Match rewards to each member's value and likelihood to respond."),
                       ("Integrated-resort cross-sell", "Carry offers from the gaming floor to rooms, dining and entertainment."),
                       ("Win-back campaigns", "Test and refine offers for lapsed members before churn sets in.")],
                 works=["Loyalty and CRM platforms", "Email, SMS and app push", "Campaign analytics"],
                 outcome="Higher promotion ROI, lower churn", mock=M_PROMO),
        ],
    },
    {
        "slug": "people-hr-learning", "name": "People: HR & Learning", "icon": "users",
        "line": "Faster, more consistent hiring and measurable skills for every team.",
        "apps": [
            dict(slug="interview-iq", name="Interview IQ", cat="AI candidate screening", icon="user",
                 short="From application to shortlist, without the scheduling.",
                 headline="From application to shortlist, without the scheduling.",
                 desc="Interview IQ runs screening end to end. It matches applicants from your hiring system, runs monitored video interviews led by AI, scores every answer against the same scoring guide and gives hiring managers a clear report on each candidate.",
                 caps=["Matches applicants from your hiring system", "Monitored video interviews led by AI", "Every answer scored the same way", "Structured hiring reports"],
                 uses=[("High-volume hiring", "Screen retail, BPO and contact-centre applicants at any hour."),
                       ("Graduate and campus intakes", "Give every candidate the same interview and the same scoring."),
                       ("Regional shared services", "Run one screening standard across countries and business units.")],
                 works=["Your hiring system", "Video interviews", "Option to run on your own servers"],
                 outcome="Faster hiring, with every candidate scored the same way", mock=M_INTERVIEW, existing=True),
            dict(slug="skilliq", name="SkillIQ", cat="Technical assessment", icon="code",
                 short="Timed, auto-graded challenges that benchmark data talent.",
                 headline="Know what your data talent can really do.",
                 desc="Timed coding tests that mark themselves, a bank of questions by topic, and a clear view of how each person ranks, so you can judge data skills fairly.",
                 caps=["Timed coding challenges", "Auto-grading", "Questions sorted by topic", "Rankings and team skill maps"],
                 uses=[("Data and analytics hiring", "Shortlist on demonstrated skill before the first interview."),
                       ("Workforce skill mapping", "See strengths and gaps across teams on one chart."),
                       ("Partner and vendor benches", "Benchmark outsourced engineers before they join a project.")],
                 works=["SQL, Python and Spark", "Your hiring system", "Team skill maps"],
                 outcome="An objective, data-driven hiring baseline", mock=M_SKILL),
            dict(slug="resonance", name="Resonance", cat="Communication coaching", icon="mic",
                 short="Executive presence, measured and coached.",
                 headline="Executive presence, measured and coached.",
                 desc="Resonance analyses speech and evaluates coherence and executive presence, then builds adaptive practice scenarios and competency maps for individuals and teams.",
                 caps=["Speech analysis", "Coherence and presence scoring", "Adaptive practice scenarios", "Individual and team competency maps"],
                 uses=[("Leadership development", "Give emerging leaders private practice and a measurable baseline."),
                       ("Sales and client teams", "Rehearse pitches and difficult conversations before the meeting."),
                       ("Customer-service onboarding", "Coach new hires towards one consistent standard.")],
                 works=["Browser and mobile", "L&D programmes", "The CIRTEC AI Academy"],
                 outcome="Measurable communication skills at scale", mock=M_RESONANCE),
        ],
    },
    {
        "slug": "retail-sales-content", "name": "Retail, Sales & Content", "icon": "cart",
        "line": "Agents that answer, quote and present, so your teams can spend their time selling.",
        "apps": [
            dict(slug="retailiq", name="RetailIQ", cat="Retail operations chatbot", icon="cart",
                 short="Ask your stores anything in plain language. Get the answer.",
                 headline="Ask your stores anything. Get the answer.",
                 desc="Ask RetailIQ about stock in plain English and it looks up the answer in your database. It also answers product and policy questions from your own documents. When a person is needed, it passes the chat to your staff.",
                 caps=["Stock questions in plain English", "Answers from your own documents", "Seamless hand-off to human agents", "Works with helpdesk tools"],
                 uses=[("Store associate assistant", "Check stock and policies from the shop floor in plain language."),
                       ("Customer-service deflection", "Resolve routine questions and hand the rest to human agents."),
                       ("Head-office operations", "Let merchandising and operations teams query inventory without an analyst.")],
                 works=["Inventory databases", "Policy and catalogue documents", "Helpdesk tools"],
                 outcome="Answers from live data, with a human when it matters", mock=M_RETAIL),
            dict(slug="quote-generator", name="Quote Generator", cat="AI quoting engine", icon="doc",
                 short="Plain-language requests or product photos into polished quotes.",
                 headline="From request to quote in one step.",
                 desc="Quote Generator turns plain-language requests or product photos into structured quotes from live inventory, suggests accessory bundles and outputs a polished PDF.",
                 caps=["Plain-language or photo input", "Quotes from live inventory", "Suggested accessory bundles", "Polished PDF output"],
                 uses=[("Distributor inside sales", "Answer quote requests without searching the catalogue."),
                       ("Field sales", "Photograph the product on site and turn it into a quote."),
                       ("Bundles and attach sales", "Add suggested accessories to every quote.")],
                 works=["Price book and inventory", "CRM", "PDF and email"],
                 outcome="Faster deals, zero catalogue searching", mock=M_QUOTE),
            dict(slug="dr-loops", name="Dr.Loops", cat="Healthcare video", icon="video", logo="dr-loops.png",
                 short="Healthcare scripts into clinician-presented video, in many languages.",
                 headline="Your script in, a clinician-presented video out.",
                 desc="Dr.Loops converts healthcare scripts into videos presented by lifelike clinician avatars, in multiple languages, with presenters you can reuse across every title.",
                 caps=["Script-to-video", "Lifelike clinician avatars", "Multiple languages", "Reusable presenters"],
                 uses=[("Patient education", "Explain procedures and aftercare in the patient's own language."),
                       ("Clinical staff training", "Refresh training content whenever the script changes."),
                       ("Health campaigns", "Keep one familiar presenter across a whole series.")],
                 works=["Your clinical scripts", "Patient portals and screens", "LMS platforms"],
                 outcome="Studio-quality video without the studio", mock=M_DRLOOPS),
        ],
    },
    {
        "slug": "data-reporting-design", "name": "Data, Reporting & Design", "icon": "db",
        "line": "A shorter path from a business question to a governed, well-designed answer.",
        "apps": [
            dict(slug="aide", name="aiDE", cat="AI data engineering", icon="db",
                 short="One interface across Fabric, Snowflake and Databricks.",
                 headline="One interface across Fabric, Snowflake and Databricks.",
                 desc="aiDE is a unified toolkit for data teams working across Microsoft Fabric, Snowflake and Databricks. Data teams describe what they need in plain English and aiDE builds it, finds data across all three platforms and checks its quality automatically.",
                 caps=["Connects to all your data tools", "Builds data pipelines from plain English", "Finds data across platforms", "Checks data quality automatically"],
                 uses=[("Data on several platforms", "Find and use data across platforms without switching tools."),
                       ("Faster pipeline delivery", "Describe what you need in plain English and have it built for you."),
                       ("Data quality at scale", "Automatically check the data that matters most.")],
                 works=["Microsoft Fabric", "Snowflake", "Databricks"],
                 outcome="Less manual data work, in one simple tool", mock=M_AIDE),
            dict(slug="ops-reporting-portal", name="Ops Reporting Portal", cat="Self-service reporting", icon="chart",
                 short="Reports built by operations, without waiting on IT.",
                 headline="Reports built by operations, without waiting on IT.",
                 desc="A drag-and-drop report builder for money-transfer and foreign-exchange teams. Teams assemble their own reports, export them to PDF or Excel, collaborate inline and raise an IT incident in one click when something needs attention.",
                 caps=["Drag-and-drop report builder", "PDF and Excel export", "Inline collaboration", "One-click IT incident raising"],
                 uses=[("FX and remittance operations", "Build day-to-day operational reports without raising a ticket."),
                       ("Audit and compliance packs", "Export consistent report packs to PDF or Excel on demand."),
                       ("Operations and IT hand-offs", "Raise an incident from the report where the issue appears.")],
                 works=["Operational databases", "PDF and Excel", "IT service management"],
                 outcome="Shorter IT request queues", mock=M_OPS),
            dict(slug="intelliframe", name="Intelliframe", cat="AI wireframe generator", icon="layout",
                 short="From written brief to annotated wireframe.",
                 headline="From written brief to annotated wireframe.",
                 desc="Intelliframe generates annotated dashboard and app wireframes from a written brief. It knows your data and your brand style, so the first draft already fits both, and it exports to image, PDF or JSON.",
                 caps=["Wireframes from a written brief", "Fits your data", "Fits your brand style", "Image, PDF or JSON export"],
                 uses=[("BI and dashboard programmes", "Agree layouts with stakeholders before a single report is built."),
                       ("Product and app teams", "Turn requirement documents into screens the team can review."),
                       ("Proposals and pre-sales", "Show clients what they will get alongside the written scope.")],
                 works=["Your data", "Your brand style", "PNG, PDF and JSON"],
                 outcome="Weeks of wireframing reduced to hours", mock=M_INTELLI),
            dict(slug="orbit", name="Orbit", cat="Project & ticket tracking", icon="orbit",
                 short="Every ticket, project and SLA, inside Microsoft Teams.",
                 headline="Every ticket, project and SLA, inside Microsoft Teams.",
                 desc="Orbit brings ticket and project tracking into Microsoft Teams. It assigns each ticket, passes urgent ones up, tracks them to the end, and warns you the moment a deadline is about to be missed.",
                 caps=["Integrated with Microsoft Teams", "Assigns and escalates tickets", "Tracks every ticket to the end", "Warns before deadlines are missed"],
                 uses=[("IT service desks", "Log, assign and resolve tickets where staff already work."),
                       ("Facilities and operations", "Track work orders from request to close-out."),
                       ("Project delivery offices", "See project status and escalations in one view.")],
                 works=["Microsoft Teams", "Email intake", "SLA policies"],
                 outcome="One source of operational truth", mock=M_ORBIT),
        ],
    },
]

ALL_APPS = [dict(a, domain=d) for d in DOMAINS for a in d["apps"]]
assert len(ALL_APPS) == 17, len(ALL_APPS)
