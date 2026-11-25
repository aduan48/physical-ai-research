# Progress Log

## Status
| # | Industry | Status |
|---|---|---|
| 1 | Forestry, logging, sawmills, paper | ✅ Done 2026-11-24 |
| 2 | Healthcare and elder care | ✅ Done 2026-11-24 |
| 3 | Manufacturing and food processing | ✅ Done 2026-11-24 |
| 4 | Agriculture | ✅ Done 2026-11-25 |
| 5 | Construction, roads, winter maintenance | ✅ Done 2026-11-25 |
| 6 | Energy | ✅ Done 2026-11-25 |
| 7 | Logistics, warehousing, trucking | ✅ Done 2026-11-25 |
| 8 | Fisheries, lobstering, aquaculture | ✅ Done 2026-11-25 |
| 9 | Colby College and local institutions | ✅ Done 2026-11-25 |

## Log
### 2026-11-24
- Set up project: CLAUDE.md, folder structure, CSV, sources, dashboard.
- Forestry done: 4 opportunities (FOR-1 to FOR-4), sources S1–S32.
- Access limits found: maine.gov, news.colby.edu, mainebiz.biz, journals.maine.edu block automated readers. data.bls.gov robots.txt disallows all. Census API needs a key. Many facts are "🔎 Snippet" status; see sources.md.

### 2026-11-24 (fix)
- User reported S1 and S2 links were broken. S1 now points to the real report on maineforest.org (full text read and figures checked). S2 withdrawn: claims could not be verified and conflicted with S1.
- Link check of all sources: also replaced S20 (dead), S22 (404), S25 (bot-blocked, figure changed from ~$22M to the verified $20M). Added S33–S35. Added county jobs (Kennebec 790, Somerset 1,743) and FOR/Maine retirement data.
- GitHub Pages enabled by user.
- Remaining 403s (maine.gov, bls.gov, colby.edu) are bot blocks, not dead links; BLS pages were read successfully via the page reader.

### 2026-11-24 (healthcare)
- Healthcare done: 5 opportunities (HC-1 to HC-5), sources S36–S54. Every cited page was opened first (new rule), except S40 (partial read).
- Key local fact: Northern Light Inland Hospital in Waterville closed May 27, 2025.
- Left out as unverified: MaineGeneral headcount; "15 nursing homes closed since 2020"; SafelyYou "80% fewer ER visits".

### 2026-11-24 (manufacturing)
- Manufacturing done: 3 opportunities (MFG-1 to MFG-3), sources S55–S66. Paper mills stay in forestry.
- Left out as unverified: "3,000 skilled manufacturing workers needed" (Mainebiz 403; mame.org is a parked domain); Greenhead Lobster HPP details; DECD food processing job counts.

### 2026-11-25 (all remaining sectors + competitors)
- User asked to finish all sectors and add competitor analysis ("how competitors fall short", "finding an edge").
- Added template section 4 "Competitors and our edge" (CLAUDE.md) and CSV columns `competitors,edge`; dashboard shows the edge column and competitors in tooltips.
- Remaining 6 industries researched in parallel by sub-agents with reserved source blocks (S100–S399); competitor sections for forestry/healthcare/manufacturing added (S400–S433). Lead merged outputs, ran check.py, scanned for personal contact info, and spot-checked README claims against source rows.
- Totals: 34 opportunities, 324 sources. Water/wastewater folded into construction-roads as CR-4.
- Each industry's raw/<slug>/notes.md lists claims left out as unverified.

## Next
- All 9 industries done. Possible next steps: re-check 🔎 sources by hand; pull Kennebec county data (Census API key); talk to the organizations in each "Who to contact" list; pick one top-5 opportunity for a pilot proposal.
