# Manufacturing and Food Processing

> **Key takeaway:** Maine has about 51,300 manufacturing jobs, down from 59,400 in 2006 [S55]. A state-funded study found Maine firms lag on automation [S57]. The proven, ready-now win is **AI optical sorting on food packing lines**: a Maine blueberry packer got 4× the throughput with about half the labor [S60]. **Collaborative robots (cobots)** for small shops are the broadest opportunity near Waterville, and there's already a support network to deliver them (Maine MEP, UMaine, Roux) [S66].

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Paper and packaging mills (Sappi, Huhtamaki) are covered in [forestry.md](forestry.md).

---

## 1. Overview

**Takeaway:** Manufacturing has held steady for a decade at a lower level. Food processing is seasonal and leans on scarce labor.

| Measure | Value | Source |
|---|---|---|
| Maine manufacturing jobs, Oct 2026 | 51,300 | [S55] |
| Maine manufacturing jobs, Oct 2016 / Oct 2006 | 50,700 / 59,400 | [S55] |
| Seasonal labor demand per capita | 9th-highest of all states | [S59] |
| Manufacturers interviewed in Maine Industry 4.0 study | 10 firms, 7 sectors | [S57] |

**Employers near Colby**

| Employer | Location | What it makes | Size | Source |
|---|---|---|---|---|
| New Balance | Skowhegan (≈20 mi from Colby) | Athletic footwear | ~400 workers; $65M, 120,000 sq ft expansion done Sept 2025 | [S56] |
| New Balance (all Maine) | Skowhegan, Norway, Norridgewock (2023) | Footwear | ~780 employees (2023; Norridgewock since merged into Skowhegan) | [S58] (partial read) |
| Brodis Blueberries | Hope (Knox County) | Wild blueberry packing | 35 employees | [S60] |

- Kennebec County manufacturing totals by industry are **not yet collected** (state data sites block scripts; Census API needs a key).

---

## 2. Bottlenecks

**Takeaway:** Small firms haven't adopted automation, and seasonal food lines can't find enough hands.

### B1. Small manufacturers are slow to automate
- Maine has ~8,100 fewer manufacturing jobs than in 2006 [S55].
- A Maine Technology Institute–funded study (2024) says Maine companies face "an urgent need to incorporate automation and real-time data". It found business leaders "lack awareness and understanding of the digital transformation" [S57].

### B2. Seasonal food packing needs scarce, round-the-clock labor
- Maine has the 9th-highest per capita demand for seasonal labor in the U.S. and relies heavily on foreign seasonal workers (H-2A, H-2B) [S59]. Visa caps make that supply uncertain.
- Fresh wild blueberry packing is "highly labour intensive and requires round the clock personnel to operate seasonally during a very short harvesting season" [S61].

### B3. Seafood processing can't recruit, and quality is checked by hand
- Seafood companies "often can't recruit enough workers" for peak orders. Workers judge fish quality by picking it up [S62] (Massachusetts, 2018; no Maine-specific data found).

---

## 3. Opportunities

### MFG-1 · Cobots for small manufacturers
**Bottleneck:** B1

**In plain language:** A small, safe robot arm works next to people. It loads machines, packs boxes, or inspects parts. A small shop can set one up in weeks, not months.

**Already being done**
- Kay Manufacturing (Illinois) bought its first cobot for under $50,000, ran it within 30 days, and saved about $150,000 in packing costs. Three inspectors moved to other jobs [S63].
- NIST publishes a free best-practice guide for adding cobots in small and mid-size shops [S64].
- In Maine, the Roux Institute's Smart Manufacturing Roadmap Program gives vendor-neutral roadmaps and implementation help, with UMaine's Advanced Manufacturing Center and Maine MEP [S66].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Helps many small firms, but each gain is modest. |
| Feasibility | 4/5 | Off-the-shelf hardware [S63], and a Maine support network already exists [S66]. |
| Time to first pilot | 6 months | One cell at one shop, with MEP help. |
| Rough cost | $30k–$100k | One cobot plus tooling and integration; author's estimate based on [S63]. |

### MFG-2 · AI optical sorting for wild blueberry and produce packing
**Bottleneck:** B2

**In plain language:** Cameras look at every berry on a conveyor. Air jets knock out unripe, soft, or damaged berries and debris. Fewer people stand at the sorting line.

**Already being done**
- **Maine:** Brodis Blueberries (Hope) became the first wild blueberry grower in Maine to add an optical sorter. With help from Maine MEP and UMaine's Advanced Manufacturing Center, it invested $125,000+ in equipment. Result: "four times the volume through the machine with about half the labor" [S60].
- **Nova Scotia field trial:** automated sorters cut sorting-line labor by 56.75%. Payback was ~10 years running 12 hours/day, but under 1 year running 24 hours/day [S61].
- **Quebec:** a frozen blueberry processor "doubled our throughput with the same number of workers" with a Key Technology sorter [S65] (company statement).

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Big gains per plant [S60][S61], but blueberries are mostly Downeast, not Kennebec. |
| Feasibility | 5/5 | Already working in Maine [S60] with published trial data [S61]. |
| Time to first pilot | 6 months | Buy and install before one harvest season. |
| Rough cost | $100k–$500k | Brodis spent $125k+ [S60]; bigger lines cost more; author's estimate. |

### MFG-3 · Cobots and vision for seafood handling and quality checks
**Bottleneck:** B3

**In plain language:** Robots and cameras do the repetitive handling and quality checks on fish and shellfish lines. People keep the skilled cutting and trimming.

**Already being done**
- Northeastern University's FISH project (funded by the national Advanced Robotics for Manufacturing institute) is bringing collaborative robots into seafood plants in New Bedford, Massachusetts. Robots do quality testing and handling; humans trim [S62]. The lead researcher's "double or triple production" figure is a projection, not a result [S62].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Seafood processing matters statewide, but less near Waterville. |
| Feasibility | 2/5 | Wet, cold, irregular, slippery products are hard for robots; still research-stage [S62]. |
| Time to first pilot | 24 months | Needs a research partner and a willing processor. |
| Rough cost | $200k–$1M | Research-grade cell; author's estimate. |

---

## 4. What's needed

| | MFG-1 Cobots | MFG-2 Optical sorting | MFG-3 Seafood robots |
|---|---|---|---|
| **Hardware** | Cobot arm, gripper, safety scanner | Optical sorter, conveyors, air ejectors | Food-safe washdown robot, cameras, lights |
| **Software/models** | Cobot programming, simple vision | Color/shape classifiers (vendor) | Grasp planning, quality classifier |
| **Data** | Cycle times, part images | Labeled berry images, reject rates | Labeled product images, grading standards |
| **Skills** | Robot programming, safety | Equipment setup, food safety | Robotics, food engineering |
| **Partners** | Maine MEP, UMaine AMC, Roux [S66] | Maine MEP, UMaine AMC [S60] | Northeastern robotics [S62], Maine processors |
| **Funding** | MTI [S57], MEP cost-share | USDA, MTI, MEP [S60] | ARM institute [S62], NSF, USDA |
| **Regulations** | Robot safety standards, OSHA | FDA food safety | FDA/USDA food safety, washdown rules |

---

## 5. Start small (student projects)

- **MFG-1 (best first project):** Use a low-cost desktop robot arm and a webcam to sort parts by color or shape. Then visit one Waterville-area shop (via Maine MEP) and time one repetitive task. Estimate the cobot payback.
- **MFG-2:** Photograph good and bad blueberries (or any fruit). Train a small image classifier. Report accuracy and false rejects, the two numbers that matter in [S61].
- **MFG-3:** Build a vision model that grades fish fillet or scallop images by color. Compare with a human grader.

---

## 6. Who to contact (organizations and public roles only)

- **Support network:** Maine Manufacturing Extension Partnership (Maine MEP) [S57][S60]; UMaine Advanced Manufacturing Center, incl. its B.O.T. Loft robotics training space [S1][S60]; Roux Institute Smart Manufacturing Roadmap Program [S66].
- **Companies:** New Balance Skowhegan factory [S56]; Brodis Blueberries (Hope) as a model adopter [S60].
- **Funders:** Maine Technology Institute [S57]; Advanced Robotics for Manufacturing (ARM) Institute [S62].
- **Research:** Northeastern University robotics (seafood handling) [S62]; Colby Davis Institute for AI [S27].

---

## 7. Risks and open questions

- **Payback depends on hours run:** sorters pay back in <1 year at 24 h/day but ~10 years at 12 h/day [S61]. A short harvest season limits use.
- **Leaders, not tools, may be the barrier:** the Industry 4.0 study points to awareness and culture [S57].
- **Jobs:** automation moves workers to other tasks in the examples [S63], but that won't always happen.
- **Evidence:** most results are company or MEP success stories [S60][S63][S65]. The Nova Scotia trial [S61] is the most rigorous.
- **Unknown:** the claim that Maine manufacturers need ~3,000 more skilled workers (could not verify; left out); Kennebec manufacturing totals; whether New Balance Skowhegan uses or wants automation.

---

## 8. Sources
All in [`../sources.md`](../sources.md). This file uses S1, S27, S55–S66.

## 9. Dig deeper
- Read the full Industry 4.0 market study (linked from [S57] on the Maine MEP site).
- Ask Maine MEP for Kennebec/Somerset success stories with cobots or vision.
- Find Maine food-processing job data (Maine DECD's 2025 food processing report; site blocks scripts, so read by hand).
- Ask Maine blueberry processors how many now use optical sorters after [S60].
