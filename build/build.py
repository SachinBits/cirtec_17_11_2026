"""Generate the CIRTEC AI new pages into ../site.

Run:  python3 build/build.py
Serve: python3 -m http.server 4321 --directory site
"""
import os
from layout import page
from apps import DOMAINS, ALL_APPS
import pages_main as M
import pages_ai as A
import pages_infra as I
import pages_svc as S
import pages_home as H

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")


def write(path, html):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return out


PAGES = [
    ("/", "CIRTEC AI | Works with what you already run", "Energy platforms for your buildings, ready-made AI apps on your own cloud, the power and cooling underneath, and the services that run it all.", "home", H.home()),
    ("/energy-infrastructure/", "Energy savings for your buildings | CIRTEC AI", "Guaranteed savings today, AI-ready operations for life, no rip-and-replace. EnergyLoop, PointLoop, ChillerLoop and a free EUI self-check.", "energy", M.energy()),
    ("/ai-applications/", "AI Apps | CIRTEC AI", "Ready-made AI apps across six business domains, deployable on your own cloud and data platform. See any of them live.", "ai", A.hub()),
    ("/infrastructure/", "Power & Cooling Infrastructure | CIRTEC AI", "UPS, BESS and PDUs, Smart Active Tiles, racks, IR Blaster and AI-in-a-Box, with AI DCEM and the PUE reduction written into the contract.", "infra", I.infrastructure()),
    ("/it-cloud/", "IT & Cloud | Database moves, cloud costs, engineers | CIRTEC AI", "Fix the plumbing first: GenAI-accelerated database migration, application modernisation, FinOps and engineering resourcing.", "infra", I.it_cloud()),
    ("/ai-academy/", "CIRTEC AI Academy | Practical AI Training", "Practical AI training for working professionals, delivered with SGTech as an Enterprise AI Practitioner programme. Singapore first, then Malaysia and the Philippines.", "services", S.academy()),
    ("/services/", "Services | Audit, Advise, Implement, Run | CIRTEC AI", "One engagement path around everything we sell: certified audits, consulting and market-entry advisory, implementation and Cirtec Care managed services.", "services", S.services()),
    ("/sitemap-plan/", "Sitemap plan (internal) | CIRTEC AI", "Internal review page mapping Message House v7 onto cirtec.ai.", "", A.sitemap_plan()),
]
for a in ALL_APPS:
    PAGES.append((f'/ai-applications/{a["slug"]}/', f'{a["name"]} | {a["cat"]} | CIRTEC AI',
                  f'{a["name"]}: {a["short"]} Part of the CIRTEC AI Enterprise AI Application Suite.', "ai", A.app_page(a)))

for path, title, desc, active, body in PAGES:
    css = '\n<link rel="stylesheet" href="/assets/css/home.css">' if path == "/" else ""
    write(path, page(title, desc, active, body, DOMAINS, path, css))
print(f"Built {len(PAGES)} pages into {os.path.normpath(ROOT)}")
