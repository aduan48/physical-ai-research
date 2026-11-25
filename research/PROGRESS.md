# Progress Log

## Status
| # | Industry | Status |
|---|---|---|
| 1 | Forestry, logging, sawmills, paper | ✅ Done 2026-11-24 |
| 2 | Healthcare and elder care | ✅ Done 2026-11-24 |
| 3 | Manufacturing and food processing | ✅ Done 2026-11-24 |
| 4 | Agriculture | ⏭ Next |
| 5 | Construction, roads, winter maintenance | ⬜ |
| 6 | Energy | ⬜ |
| 7 | Logistics, warehousing, trucking | ⬜ |
| 8 | Fisheries, lobstering, aquaculture | ⬜ |
| 9 | Colby College and local institutions | ⬜ |

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

## Next
- Agriculture: potatoes, dairy, blueberries (farm side), greenhouses. Avoid repeating MFG-2 (packing-line sorting).
- Human to-dos: optionally get a Census API key.
