# CIRTEC AI — new pages (Message House v7)

Static HTML build of the new site pages, styled to match cirtec.ai (Montserrat/Lato, green pills, mint sections).
Routes use clean URLs so they map straight onto the Astro site.

## Pages (25)
| Route | Page |
|---|---|
| `/` | Home: the live cirtec.ai homepage (same design, copy, video and images) with the Message House v7 sections woven in. Built by `build/pages_home.py`, styled by `site/assets/css/home.css` |
| `/energy-infrastructure/` | House 01: Measure / Act / Transform, 6-step ladder, free EUI self-check |
| `/ai-applications/` | House 02 hub: 17 apps, domain filter + search, demo request |
| `/ai-applications/<app>/` | 17 app pages (use cases, how it fits, related apps, demo form) |
| `/infrastructure/` | Power & Cooling: AI DCEM PUE guarantee, UPS/BESS/PDUs, Smart Active Tiles, racks & IR Blaster, AI-in-a-Box |
| `/it-cloud/` | IT & Cloud: DBShift, modernisation, FinOps, resourcing |
| `/services/` | One engagement path: Audit, Advise, Implement, Run (Cirtec Care) |
| `/ai-academy/` | CIRTEC AI Academy (formerly AI Bootcamp), with SGTech |
| `/sitemap-plan/` | Internal review page: new / update / keep / redirect map. Do not publish. |

## Edit and rebuild
Content lives in `build/` (`apps.py` = the 17 apps, `pages_main.py` (home, energy), `pages_ai.py` (suite, apps, sitemap plan), `pages_infra.py`, `pages_svc.py`, `layout.py` = nav/footer).

```bash
python3 build/build.py
```

Output goes to `site/`. Styles: `site/assets/css/site.css`. Behaviour: `site/assets/js/site.js`.

## For the developer
- Forms show a success state only. Wire each `form[data-lead-form]` to the CRM/form endpoint (`data-endpoint`).
- Links to existing pages (About, Contact, legal) point to https://www.cirtec.ai/... — make them relative when merging.
- Suggested 301s: `/platforms/cx-operations` → `/ai-applications/`, `/solutions/ai-vision` → `/ai-applications/ai-vision/`,
  `/solutions/ai-concierge` → `/ai-applications/ai-concierge/`, `/solutions/ai-interviewer` → `/ai-applications/interview-iq/`,
  `/platforms/power-cooling` → `/infrastructure/`, `/solutions/ir-blaster` → `/infrastructure/#racks`, `/platforms/monitor-manage` → `/energy-infrastructure/#measure`.
- Indicative "from" prices (from Message House v7 and the Q4 brochure) appear on Energy, Infrastructure and IT & Cloud. Remove them in `build/` if pricing should stay off the site.
- App visuals are CSS mock-ups (labelled "Illustrative"). Swap in real screenshots or demo clips when available.
- Homepage hero cards, ticker, success stories and blog list are a snapshot (16 Nov 2026) of the WordPress API the live site uses
  (`/wordpress/wp-json/wp/v2/home-cards`, `whats-now`, `success-stories`, `posts`). In Astro, keep fetching them from WordPress.
- Homepage videos (`assets/img/home/hero.mp4`, `cta-bg.mp4`) and partner logos are copied from the live site.
