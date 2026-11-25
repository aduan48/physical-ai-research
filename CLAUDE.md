# CLAUDE.md — Physical AI Opportunities Near Colby

## What this project is
A research project by a Math + CS student at Colby College (Waterville, Maine).
Question: where could physical AI (robotics, drones, computer vision, autonomous machines, smart sensors, embodied AI) solve real bottlenecks in industries near Colby? How would it be built, and what would it take?

Geography priority: Waterville / Kennebec County → central Maine → statewide.

## Start every session here
1. Read `research/PROGRESS.md` to see what is done and what is next.
2. Continue with the next industry. Work **one industry at a time**.
3. After each industry: update `opportunities.csv`, `sources.md`, `dig-deeper.md`, `README.md` (re-rank top 5), `PROGRESS.md`. Then commit (`research: <industry>`) and push to `origin/main`. Then give a 3-line summary and **wait for the user to say "continue"**.

## Industry order
1. Forestry, logging, sawmills, paper and wood products (`forestry`)
2. Healthcare and elder care (`healthcare`)
3. Manufacturing and food processing (`manufacturing`)
4. Agriculture: potatoes, dairy, blueberries, greenhouses (`agriculture`)
5. Construction, roads, winter maintenance (`construction-roads`)
6. Energy: hydro, wind, solar, grid (`energy`)
7. Logistics, warehousing, trucking (`logistics`)
8. Fisheries, lobstering, aquaculture (`fisheries`)
9. Colby College and local institutions (`colby-institutions`)

Candidate additions (add only with evidence, and explain why to the user): water/wastewater and public works; environmental monitoring and conservation; public safety and search and rescue.

## Files
- `research/README.md` — 1-page exec summary: top 5 opportunities ranked, one-line reason each, how to navigate.
- `research/PROGRESS.md` — dated log: done, in progress, next.
- `research/industries/<slug>.md` — one per industry, fixed template below.
- `research/opportunities.csv` — columns: `id,industry,bottleneck,solution,impact,feasibility,months_to_pilot,cost_range,file`. `id` like `FOR-1`. `file` relative to `research/`, e.g. `industries/forestry.md`.
- `research/sources.md` — every source, globally numbered `S1, S2, …`: title, URL, organization, date, claims it supports. Never renumber existing sources; append only.
- `research/dig-deeper.md` — reports, organizations, events, grants, courses, datasets, open questions.
- `research/raw/<slug>/` — raw notes and scraped data. Each file starts with `Source URL:` and `Accessed: YYYY-MM-DD`.
- `research/scripts/` — small Python scrapers for public data only. `check.py` validates citations and the CSV.
- `research/site/index.html` — self-contained dashboard. No build step, no external libraries. Loads `../opportunities.csv`.

## Industry file template (same headings every time)
1. **Overview** — key takeaway first; footprint table with numbers, units, `[S#]` citations.
2. **Bottlenecks** — 2–4, each with evidence (report, dataset, article, quote) and citation.
3. **Opportunities** — one card per bottleneck: solution in plain language; existing examples anywhere in the world; ratings table (Impact 1–5, Feasibility 1–5, Time to first pilot in months, Rough cost range) with a one-sentence reason each.
4. **What's needed** — hardware, software/models, data, skills, partners, funding (MTI, NSF, USDA, etc.), regulations/permits.
5. **Start small** — a realistic first student project per opportunity.
6. **Who to contact** — organizations, companies, Colby programs, Maine research centers. Organizations and public roles only. **No personal contact info.**
7. **Risks and open questions**
8. **Sources** — list of `[S#]` used in the file.
9. **Dig deeper**

## Research rules
- Every factual claim needs a source `[S#]`. If unsourced, label it "unverified" or leave it out.
- **Never invent statistics, companies, or quotes.**
- Prefer primary sources: government data, company sites, peer-reviewed papers. Then reputable news. Blogs last.
- Ratings are the author's judgment. Say so, and give a one-sentence reason.
- Scraping: public pages and datasets only. Check robots.txt. Rate-limit (≥1 s between requests). Generic User-Agent, no personal details in it. No LinkedIn, nothing behind a login, no personal data. Prefer official APIs and CSV downloads.

## Writing style
Short sentences. Plain English. Bullets for lists, tables for comparisons. Numbers with units and sources. Lead every section with the key takeaway.
