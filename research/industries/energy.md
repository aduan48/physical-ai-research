# Energy: Hydro, Wind, Solar, Grid

> **Key takeaway:** Maine's grid fails more often than almost anywhere in the U.S. In 2024 Maine had the **most outages per customer of any state** and the **second-longest total outage time** (1,748.6 minutes, about 29 hours, vs 611.3 minutes U.S.) [S200]. Trees are the main cause [S202][S203]. The best physical AI bet is **AI vegetation-risk mapping plus drone line patrol** for Maine utilities (EN-1). Two smaller, cheaper bets sit right next to Colby: **AI fish counting at Kennebec fishways** (EN-2), where the four dams near Waterville are being sold for eventual removal [S220][S221], and **thermal-drone and snow-loss checks for Maine's ~1.7 GW of solar** (EN-3) [S201].

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Each has a one-line reason.

---

## 1. Overview

**Takeaway:** Maine's power is clean and local, but its wooded, rural lines go down often. Big money already goes to storms and trees.

| Measure | Value | Source |
|---|---|---|
| Outage minutes per customer (SAIDI, all events), 2024 | Maine 1,748.6; U.S. 611.3. Maine 2nd-highest of 50 states + DC (author's ranking of EIA table) | [S200] |
| Outages per customer (SAIFI, all events), 2024 | Maine 3.636; U.S. 1.521. Highest of 50 states + DC (author's ranking) | [S200] |
| SAIDI, all events, 2025 | Maine 363.4 min; U.S. 262.6. Highest in New England | [S200] |
| SAIDI without major event days, 2025 | Maine 191.7 min; U.S. 120.8 (day-to-day reliability, not just big storms) | [S200] |
| Maine SAIDI, all events, 2013–2024 | Over 1,700 min in 2017, 2020, 2023, 2024 (peak 2,492.6 in 2017) | [S201] |
| CMP storm restoration cost | $161.7M (2023), $119M (2022), $24.5M (2024, 3 storms) | [S204] |
| Maine outages, past 20 years | "more than tripled" (Southern Maine Planning and Development Commission report) | [S203] |
| In-state capacity, 2024 | 5,586 MW total: gas 1,584; wind 1,030; petroleum 845; hydro 726; utility solar 829; wood 450 | [S201] |
| In-state generation, 2024 | 14.66 million MWh: gas ~44%, hydro ~19%, wind ~17%, wood ~11%, utility solar ~6% (author's shares from EIA table) | [S201] |
| Solar capacity | 829 MW utility-scale + 849 MW small-scale = ~1,680 MW in 2024, up from ~66 MW in 2019 | [S201] |
| Community solar | 694 W per person at end of 2025, 1st in U.S.; new large projects now barred from net energy billing | [S216] |
| Heat pumps | 100,000 goal met ~2 years early (2023); new target 175,000 more by 2027 | [S234] |
| Electric utilities | 11 in Maine: CMP and Versant plus 9 small co-ops and municipal/island utilities | [S210] |

**Local picture (Waterville / Kennebec)**

| Asset | What is happening | Source |
|---|---|---|
| Lockwood, Hydro-Kennebec, Shawmut, Weston dams (four lowest Kennebec dams; the river there flows past Waterville and Skowhegan) | The Nature Conservancy agreed (Sept 2025) to buy all four from Brookfield. A new nonprofit, the Kennebec River Restoration Trust, will own them; Brookfield keeps operating. No changes "for at least the next few years." | [S220][S221][S222] |
| Lockwood fish lift | Lowest dam. 47 adult salmon reached it in 2025 and were trapped and trucked upstream [S223]. 2026 counts: 87 multi-sea-winter salmon, 17 grilse, 145,253 river herring. Counts provided by Brookfield. | [S223][S225] |
| Benton Falls fishway (Sebasticook) | 4,075,670 river herring counted in 2026, counted by Maine DMR [S225]. More than 6 million in 2024 [S226]. | [S225][S226] |
| Shawmut Dam | Supplies water to Sappi's Somerset mill. TNC says it will find a solution for the mill first. | [S220][S221] |
| KVCC Electrical Lineworker Technology (Fairfield) | One-year certificate. Partners include CMP, Cianbro, IBEW 104. | [S236] |
| Dec 2023 windstorm | Gusts over 90 mph, Kennebec flooding. CMP and Versant called it "the largest restoration event" in their histories. | [S206] |

- Maine-specific line worker shortage figures: **unverified**. Nationally, BLS projects 10% job growth for line installers (2025–35), with ~10,900 openings a year [S235].
- Maine onshore wind is 1,030 MW of capacity [S201]. Wind farm locations and owners were not checked.

---

## 2. Bottlenecks

**Takeaway:** The big, costly problem is trees falling on lines. The smaller local problems are counting fish at dams under federal rules, and keeping a fast-built solar fleet producing through Maine winters.

### B1. Trees take down Maine's lines, often and expensively
- Maine had the highest outage frequency of any state in 2024 (3.6 per customer) [S200]. Even without major storms, Maine's outage time in 2025 was about 1.6× the U.S. (191.7 vs 120.8 min) [S200].
- EIA says frequent outages in Maine and Vermont are "often" due to storm-related tree damage [S202]. A 2026 regional report names trees and limbs as the main cause, and vegetation management as its top fix [S203].
- Winter Storm Elliott (Dec 2022) cut power to about 380,000 CMP customers, over 40% of its customers [S203]. In Oct 2024, wind knocked trees onto lines and cut ~85,000 customers [S205].
- CMP restoration costs: $161.7M in 2023 alone [S204]. In 2015, CMP spent about $20M a year on trimming along nearly 24,000 miles of roadside lines, on a 5-year cycle [S207]. Current CMP and Versant trim budgets: **unverified** (cmpco.com would not load).
- Trimming works: a UConn study estimated 16–65% fewer storm outages with vegetation management [S208].

### B2. Fish passage at Kennebec dams depends on counting fish
- NOAA requires the four Brookfield dams to meet "benchmark commitments for safe and effective fish passage," under "an extensive monitoring program" [S224]. Salmon are endangered [S224].
- Counts are done at fishways from May to early November [S225]. Benton Falls alone counted over 4 million river herring in 2026 [S225].
- Manual fish counting from video often has 30–40% error, from sampling and interpolation; humans "cannot count fish 24/7" [S229]. Manual video review is "labor-intensive and time-consuming" [S227].
- The dams are entering a multi-year transition to removal [S221][S223]. Owners, regulators, and restoration groups will all want trusted before-and-after fish data (author analysis).

### B3. A fast-built solar fleet must keep producing in snow
- Maine solar grew from ~66 MW (2019) to ~1,680 MW (2024) [S201]. New large community solar has now stalled under a 2025 law [S216].
- So output from **existing** farms matters more. Snow cuts PV output 1–12% a year, with monthly losses up to 100%. Snow also puts "excessive and uneven stress" on modules [S217].
- Rural Maine solar farms are spread out. Sending a crew to walk each site after storms is slow (author analysis).

---

## 3. Opportunities

### EN-1 · AI vegetation-risk mapping and drone line patrol
**Bottleneck:** B1

**In plain language:** Use satellite and drone images plus AI to find the specific trees most likely to hit a line. Crews trim those first, instead of trimming everything on a fixed 5-year loop [S207]. After a storm, drones fly the lines to find damage faster than trucks.

**Already being done**
- UConn's Outage Prediction Model combines weather forecasts with tree height, density, and leaf-on/leaf-off data. It gives a 3-day storm outlook for Eversource and United Illuminating (3.6M customers) [S209]. No Maine utility is named.
- Overstory (satellite + AI) reports a 48% year-over-year drop in vegetation outages at Hydro Ottawa, and 94% fewer pre-storm inspections at OG&E [S212]. These are vendor figures.
- AiDash uses very-high-resolution satellite images 1–12 times a year to flag tree encroachment, and dispatches drones to flagged spans [S211].
- Skydio sells docked autonomous drones for line inspection. It quotes AEP as avoiding ~30 million customer minutes of interruption over 2.5 years [S214] (vendor-quoted).

| Rating | Score | Why |
|---|---|---|
| Impact | 5/5 | Maine has the most frequent outages in the U.S. [S200], trees are the main cause [S202][S203], and one bad year cost CMP $161.7M [S204]. |
| Feasibility | 3/5 | Tools exist [S211][S212], but utilities must share line maps and outage data, and drone BVLOS flights need FAA waivers [S214][S31]. |
| Time to first pilot | 9 months | A desk study on public data is fast; a field pilot needs a utility partner. |
| Rough cost | $20k–$150k | Satellite/LiDAR data, a drone, and student time for one service area; author's estimate. |

### EN-2 · AI fish counting at Kennebec fishways
**Bottleneck:** B2

**In plain language:** An underwater camera at a fish ladder records every fish. AI counts and sorts them by species, all day and night. Staff check a sample instead of watching hours of video.

**Already being done**
- MIT Sea Grant, Woodwell, and MIT CSAIL built an end-to-end camera + AI system on three Massachusetts rivers. Season counts matched traditional estimates [S227].
- Innovasea HydroAI counts fish at hydro fishways, with error ~5% or less at many sites and up to 20% at hard sites. Side-view cameras are needed for species ID [S229]. Partners named are in Atlantic Canada [S228].
- Vaki Riverwatcher uses infrared scanner plates plus a camera, runs on 12 V, and suits remote sites with solar and batteries [S230].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Supports endangered salmon recovery and a federal monitoring program [S224], but it is a narrow market of a few fishways. |
| Feasibility | 4/5 | Proven nearby in Massachusetts [S227]; fishways already exist at Lockwood and Benton Falls [S225]. |
| Time to first pilot | 6 months | One camera at one fishway for one spring run, if DMR or the dam operator agrees. |
| Rough cost | $5k–$40k | Underwater camera, edge computer, solar power, labeling time; author's estimate. |

### EN-3 · Thermal-drone inspection and snow-loss tracking for community solar
**Bottleneck:** B3

**In plain language:** A drone with a heat camera flies over a solar farm. Hot spots show broken panels or wiring. After snowstorms, cameras or drones show which rows are still covered and how much power is lost, so owners know when clearing is worth it.

**Already being done**
- Raptor Maps sells solar O&M software and "Raptor Solar Sentry" autonomous drones for scheduled or alert-triggered inspections. Its app works offline with no cell signal [S218].
- Zeitview (formerly DroneBase) collects solar data by drone, fixed-wing aircraft, or robotic crawler, including thermal [S219].
- Percepto sells drone-in-a-box systems for solar and utilities; one customer cites avoiding staff trips in −21°F weather [S215].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Snow can cut output 1–12% a year [S217] across ~1.7 GW [S201], but losses per farm are modest. |
| Feasibility | 4/5 | Thermal drones are standard [S218][S219]; Part 107 visual-line-of-sight flights are enough for one farm [S31]. |
| Time to first pilot | 6 months | One winter at one community solar farm. |
| Rough cost | $5k–$50k | Thermal drone, software, student analysis; author's estimate. |

**Considered and not ranked**
- **Wind blade inspection robots/drones:** SkySpecs says it monitors 75%+ of North American blades each year [S237]; Aerones has serviced 25,000 turbines [S238]. The market is already well served.
- **Underwater ROV dam inspection:** ROVs like Deep Trekker's are off the shelf and list hydro as a market [S239]. The four nearest dams are headed for removal [S221], so the local need is short-lived (author analysis).
- **Offshore wind:** UMaine's ASCC launched the first grid-connected floating turbine in the Americas in 2013 [S232] and a quarter-scale base in 2025 [S233]. The commercial research array is paused [S233]. Too early for a student physical-AI pilot.
- **Robotic snow clearing on solar:** No Maine evidence found; left as an open question.

---

## 4. Competitors and our edge

**Takeaway:** Incumbents sell to the largest utilities and solar fleets. Their gaps in Maine are scale (small utilities), local training data (Maine trees, Kennebec fish, snow), and evidence that is mostly vendor-reported.

### EN-1 Vegetation risk and line patrol

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| AiDash | Satellite + AI vegetation management; drones sent to flagged spans; 200+ customers | No New England utility named; no public pricing; built around wildfire and large networks (author analysis) | [S211] |
| Overstory | Satellite AI hazard-tree mapping for utilities | Customers named are large (Exelon, PG&E, OG&E) and none in Maine; results are vendor case studies | [S212] |
| Sharper Shape | Helicopter/drone LiDAR + AI, "living digital twin" for T&D | Aimed at "tier 1 utilities"; no named New England customer | [S213] |
| Skydio | Docked autonomous drones for line and substation inspection | Remote flights need BVLOS waivers and cell coverage for live video, which rural Maine may lack | [S214] |
| UConn Eversource Energy Center | Storm outage prediction using tree and weather data | Serves Eversource and UI in CT/MA/NH; no Maine utility named | [S209] |

**Our edge**
- **Too small for incumbents:** Maine has 9 small utilities beyond CMP and Versant, such as Madison Electric Works [S210]. A low-cost tool built on public satellite and LiDAR data could serve them (author analysis).
- **Maine-tuned models:** Storm winds now come more from the south, where trees are less hardened [S203]. A model trained on Maine species, winds, and leaf-off winter storms fills a gap that CT-trained tools may miss (author analysis).
- **Public outcome data:** EIA publishes state SAIDI/SAIFI every year [S200][S201], so a Colby project can check its claims against independent numbers, not vendor ones.
- **Local workforce link:** KVCC's lineworker program in Fairfield partners with CMP [S236]. Drone patrol training could fit there (author analysis).

### EN-2 Fish counting

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| Innovasea HydroAI | Camera + AI fish counts and species ID at hydro fishways | Up to 20% error at hard sites; species ID needs a second camera; partners named are in Atlantic Canada; no price listed | [S228][S229] |
| Vaki Riverwatcher | Infrared scanner plates + camera counter | Fish must pass between scanner plates [S230]; whether it keeps up with millions of river herring a season, as at Benton Falls [S225], is untested here (author analysis) | [S230][S225] |
| MIT Sea Grant / Woodwell system | Open research system for river herring counting | Trained on Massachusetts rivers, not Kennebec species mix or flows | [S227] |
| Manual counts / video review | Staff counts at fishways | 30–40% error; cannot run 24/7 | [S229] |

**Our edge**
- **Kennebec training data:** The Kennebec has salmon, shad, river herring, striped bass, and lamprey at the same fishways [S225]. A labeled local dataset is something no vendor has published (author analysis).
- **Before-and-after baseline:** The dams will change ownership and later be removed [S221][S223]. Independent, continuous counts now give a baseline for the whole restoration (author analysis).
- **Close partners:** DMR runs Benton Falls counts and Brookfield supplies Lockwood counts [S225]. Both fishways are in the Kennebec watershed near Colby (author analysis).

### EN-3 Solar inspection and snow

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| Raptor Maps | Solar O&M software + autonomous drones | Sold to "leading IPPs, O&Ms, and EPCs"; no snow features shown; no price | [S218] |
| Zeitview (ex-DroneBase/Heliolytics) | Drone and aircraft thermal inspection | No small-site offer or pricing shown | [S219] |
| Percepto | Drone-in-a-box for solar and utilities | Fixed station per site; customers are large (NRG, Chevron); no price | [S215] |
| Snow-loss research (Sandia) | Studies snow losses and module damage | Long-term snow damage still "virtually unknown"; not a product | [S217] |

**Our edge**
- **Maine community solar is dense and stuck:** Maine leads the U.S. in community solar per person, and new projects are stalled [S216]. Owners now need to squeeze more from existing farms (author analysis).
- **Snow is local data:** No vendor page read showed snow features [S218][S219]. Measured winter losses from Maine farms would be new data (author analysis).
- **Cheap per-visit service:** A student-run drone service under Part 107 [S31] could suit small farms that will not buy a docked system (author analysis).

---

## 5. What's needed

| | EN-1 Vegetation risk | EN-2 Fish counting | EN-3 Solar inspection |
|---|---|---|---|
| **Hardware** | Drone with RGB + LiDAR (optional) | Underwater camera, edge computer, solar + battery (12 V like [S230]) | Thermal drone; fixed snow camera |
| **Software/models** | Tree detection, change detection, risk scoring | Fish detection, tracking, species classifier | Hot-spot detection, snow-cover segmentation |
| **Data** | Satellite/LiDAR, line maps, outage logs, EIA reliability [S200] | Labeled fishway video; DMR counts to check against [S225] | Production data from farm owner; weather |
| **Skills** | Remote sensing, ML, GIS | Computer vision, field electronics | CV, PV basics, drone flying |
| **Partners** | CMP, Versant, small utilities [S210]; UConn center [S209] | Maine DMR, Brookfield, TNC/KRRT [S220][S225] | Community solar owners; ReVision Energy, MREA [S216] |
| **Funding** | Utility pilot budgets, MTI, DOE | NOAA, restoration funds, NSF | Owner budgets, MTI |
| **Regulations** | FAA Part 107; BVLOS waiver for long patrols [S31][S214]; utility data agreements | Permission to mount gear at fishway; ESA species rules [S224] | FAA Part 107 [S31]; site safety near energized gear |

---

## 6. Start small (student projects)

- **EN-1 (best first project):** Pick one Kennebec County town. Map tree cover near roads from free imagery. Compare it with outage history (start with EIA state data [S200]; ask a utility for circuit data). Test whether tall trees near lines predict outages.
- **EN-2:** Ask DMR to share fishway video from Benton Falls. Hand-label 2,000 fish by species. Fine-tune an open detector and compare with official counts [S225].
- **EN-3:** Fly a thermal drone over one community solar farm in winter. After each snowstorm, photograph rows, estimate snow cover, and compare with the farm's production.

---

## 7. Who to contact (organizations and public roles only)

- **Utilities:** Central Maine Power (Augusta); Versant Power (Bangor); Madison Electric Works (Madison) and other consumer-owned utilities [S210].
- **Regional research:** Southern Maine Planning and Development Commission (outage report) [S203]; UConn Eversource Energy Center [S208][S209].
- **Fisheries and dams:** Maine DMR Bureau of Sea-Run Fisheries and Habitat [S225][S226]; Brookfield Renewable (Lockwood counts) [S225]; The Nature Conservancy in Maine / Kennebec River Restoration Trust [S220][S221]; Trout Unlimited, Maine Rivers / Kennebec Coalition [S223][S231]; NOAA Fisheries [S224].
- **Fish-counting research:** MIT Sea Grant and Woodwell Climate Research Center [S227].
- **Solar:** Maine Renewable Energy Association; ReVision Energy [S216].
- **Wind and training:** UMaine Advanced Structures and Composites Center [S232][S233]; KVCC Electrical Lineworker Technology program [S236]; Colby Davis Institute for AI [S27].

---

## 8. Risks and open questions

- **Data access:** EN-1 needs line maps and outage logs that utilities may treat as confidential (author analysis).
- **Evidence quality:** Most results are vendor-reported: Overstory [S212], Skydio/AEP [S214], Innovasea [S229]. The UConn trimming study is the main independent result [S208].
- **Drone rules and coverage:** Long patrols need BVLOS waivers and cell coverage [S214].
- **Dam future:** The four Kennebec dams may be removed over about a decade [S223]. Fish counting at Lockwood may move or end (author analysis).
- **Solar policy:** New community solar is stalled [S216], which may shrink O&M budgets.
- **Unknown:** Current CMP and Versant vegetation budgets; share of outages caused by trees today; Maine line worker shortage size; whether DMR already uses AI for counts.

---

## 9. Sources
New sources S200–S239 are listed in `raw/energy/sources-rows.md` (to be merged into [`../sources.md`](../sources.md)). This file also reuses S27 and S31.

## 10. Dig deeper
- Read CMP's Climate Change Resilience Plan (cmpco.com would not load for this research).
- Read the Southern Maine Planning and Development Commission outage report behind [S203].
- Download EIA Form 861 reliability data by utility to compare CMP, Versant, and small utilities.
- Ask DMR how Benton Falls counts are made today (video? manual?) [S225].
- Find the FERC license-amendment dockets for the four dams and read their fish passage monitoring terms (not yet opened).
