# Physical AI Opportunities Near Colby College

Where can robots, drones, computer vision, and smart sensors fix real bottlenecks in industries around Waterville, Maine? Who already sells a fix, where do they fall short, and where could a Colby-based effort win? Every claim is sourced.

**Status:** All 9 industries done. 34 opportunities, 324 sources. See [PROGRESS.md](PROGRESS.md).

## Top 5 opportunities
Ranked by Impact × Feasibility, then shortest time to pilot. Ties are broken by how strong our edge over competitors is. All ratings are the author's judgment.

| Rank | ID | Opportunity | Impact | Feas. | Pilot | Why it matters | Our edge |
|---|---|---|---|---|---|---|---|
| 1 | CR-2 | Road-weather sensors on plows + data-driven salt rates | 5 | 4 | 12 mo | Maine spends ~$155M a year clearing winter roads and spreads ~493,000 tons of salt [S150]. Plow-mounted sensors cut salt per mile 26% in an Illinois DOT study [S166]. | Incumbent sensors break even only on heavy-salt routes; a cheap retrofit sized for small Maine town fleets is unserved [S166]. |
| 2 | FOR-2 | Drone + AI forest inventory and pest detection | 4 | 4 | 6 mo | Forest owners lack remote-sensing staff [S15]; UMaine + Colby already run this research [S13][S14]. | Turnkey service trained on Maine species, for owners too small for enterprise vendors. |
| 3 | AG-2 | Drone RGB + thermal maps of wild blueberry fields | 4 | 4 | 6 mo | 2025 drought cut the crop to ~54.9M lb [S111][S112]; growers have had negative margins for 3+ years [S113]. | Maine grows almost all U.S. wild blueberries [S113], and no vendor models this crop. |
| 4 | AG-1 | Low-cost camera alerts for lame or thin cows on small dairies | 4 | 4 | 6 mo | Milk is $42.1M of Kennebec's $64.3M farm sales [S101]; Maine went from 602 to 140 dairies [S105]. | Robot milkers cost ~$250k [S107]; camera systems are proven on 1,000-cow parlour herds [S121]. |
| 5 | LOG-1 | Winter-aware AI dash cams + coaching for small truck fleets | 4 | 4 | 6 mo | Snow, slush or ice was on the road in ~18% of Maine truck crashes [S255]. Video + coaching cut safety events 38–52% [S260]. | ~90% of U.S. carriers run ≤10 trucks and have no safety manager to coach [S262]. |

**Next in line:** HC-2 nursing-home fall detection (4/4, 6 mo; strong evidence [S45] but a mature market), CR-1 drone bridge inspection (4/4, 9 mo; MaineDOT already drone-inspected the Waterville–Winslow Ticonic Bridge [S161]), HC-1 and EN-1 (impact 5, harder).

**Best first step for a Colby student:** COL-3, a campus drone tree inventory (3 months). It feeds straight into FOR-2 and extends the existing UMaine–Colby partnership. See [colby-institutions.md](industries/colby-institutions.md).

Full list: [opportunities.csv](opportunities.csv) or the [dashboard](https://aduan48.github.io/physical-ai-research/research/site/).

## Industries
Each file uses the same template: Overview, Bottlenecks, Opportunities, **Competitors and our edge**, What's needed, Start small, Who to contact, Risks, Sources, Dig deeper.

| Industry | Opportunities | Headline fact |
|---|---|---|
| [Forestry](industries/forestry.md) | FOR-1 to FOR-4 | $8.3B sector; logging is the deadliest U.S. job [S1][S6] |
| [Healthcare and elder care](industries/healthcare.md) | HC-1 to HC-5 | Oldest state; 23,500 unstaffed home-care hours/week [S36][S38] |
| [Manufacturing and food processing](industries/manufacturing.md) | MFG-1 to MFG-3 | 51,300 jobs, down from 59,400 in 2006 [S55] |
| [Agriculture](industries/agriculture.md) | AG-1 to AG-4 | Kennebec is a dairy county; PFAS is concentrated around Fairfield [S101][S109] |
| [Construction, roads, winter](industries/construction-roads.md) | CR-1 to CR-4 | 15.4% of Maine bridges in poor condition vs 6.7% U.S. [S155] |
| [Energy](industries/energy.md) | EN-1 to EN-3 | 1,748.6 outage minutes per customer in 2024 vs 611.3 U.S. [S200] |
| [Logistics](industries/logistics.md) | LOG-1 to LOG-4 | Amazon delivery station approved in Waterville, 2026 [S252] |
| [Fisheries](industries/fisheries.md) | FISH-1 to FISH-3 | Lobster landings 78.8M lb in 2025, down from 86M in 2024 [S301][S300] |
| [Colby and local institutions](industries/colby-institutions.md) | COL-1 to COL-4 | Waterville Public Works under a hiring freeze, 3 jobs vacant 1+ year [S363][S364] |

## How to navigate
- [opportunities.csv](opportunities.csv) — every opportunity, with competitors and our edge.
- [sources.md](sources.md) — numbered sources. ✅ = page read, 🔎 = partial read or search summary only, ❌ = withdrawn. Numbers are grouped in blocks by industry (S100s agriculture, S150s construction, S200s energy, S250s logistics, S300s fisheries, S350s Colby, S400s competitor research), so gaps are expected.
- [dig-deeper.md](dig-deeper.md) — reports, groups, grants, datasets, open questions.
- [Dashboard](https://aduan48.github.io/physical-ai-research/research/site/) — sortable table, Impact vs Feasibility chart, industry cards.
- `raw/` — raw notes with URLs and access dates, plus items left out as unverified. `scripts/check.py` checks citations and the CSV.
