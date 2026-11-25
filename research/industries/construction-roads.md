# Construction, Roads, and Winter Maintenance (incl. Water/Wastewater)

> **Key takeaway:** Maine spends about $155 million a year clearing winter roads and spreads about 493,000 tons of salt [S150]. Fifteen percent of its bridges are in poor condition, the 4th-highest share in the U.S. [S155][S156]. Plow crews run about 20% below planned staffing [S152]. The best physical AI bets are **sensor-guided salt spreading on plows** (CR-2) and **drone + AI bridge inspection** (CR-1). Both have independent evidence from other DOTs [S166][S161], and Waterville's own Ticonic Bridge is already a federal drone case study [S161]. Road scanning for small towns (CR-3) and AI sewer-video coding (CR-4) are cheaper starter projects.

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Each has a one-line reason.

**Scope note: water/wastewater folded in.** The candidate addition "water/wastewater and public works" is included here as CR-4. Reason: the same town public works crews run roads and sewers, and the evidence is solid: $1.7B in municipal wastewater needs in Maine [S186], 53% of Maine wastewater operators over 50 (2020) [S188], and a 19-million-gallon sewer spill in Waterville in 2019 [S190]. **Lead service lines were dropped:** EPA modeled ~18,000 in Maine, but the state had confirmed only about a dozen by May 2024, likely because a 1926 plumbing code banned them [S189]. That is not a robot-sized problem in Maine.

---

## 1. Overview

**Takeaway:** Maine has a big road and bridge network per person, harsh winters, old bridges, and a thin workforce to maintain them.

| Measure | Value | Source |
|---|---|---|
| Public roadway in Maine | 45,586 miles (most per person in New England) | [S151] |
| Road salt used, 2019–20 | ~493,000 tons (787 lb per resident; ~11 tons per lane mile per year) | [S150] |
| Statewide winter road clearing cost | ~$155 million/yr ($114 per resident); excludes corrosion, environment, wells | [S150] |
| MaineDOT winter costs | ~$30M (FY2016) → ~$46M (FY2020) (podcast transcript; check original) | [S151] |
| MaineDOT plow fleet and crew (Dec 2022) | ~400 trucks, ~500 plow workers, 20% below plan; ~8,300 lane miles | [S152] |
| Maine bridges in poor condition (NBI, June 2025) | 392 of 2,542 (15.4%); U.S. 6.7% | [S155] |
| Rank by share of structurally deficient bridges | 4th worst; 1.04M daily crossings on them; $497M est. repair for 413 bridges | [S156] |
| Maine bridges built 1969 or earlier | 59% (5th-highest share) | [S157] |
| Major roads in poor condition | 19% statewide (Bangor 18%, Lewiston-Auburn 14%) | [S157] |
| Cost of rough roads to Maine drivers | $609 per driver/yr; $637M statewide in extra vehicle costs | [S157] |
| Construction jobs in Maine (payroll) | 35.0k (Oct 2026), up from 27.3k (Oct 2016) | [S178] |
| Maine work deaths 2024 | 19 total; construction sector had the most (6) | [S176] |
| Maine clean water (wastewater) needs, 2022 survey | ~$3.1B total; $1.7B municipal wastewater (U.S. total $630.1B) | [S186][S187] |

**Local picture (Waterville / Kennebec)**

| Asset | Fact | Source |
|---|---|---|
| Ticonic Bridge (US-201, Waterville–Winslow, over the Kennebec) | Built 1936. ~9,000 vehicles/day. Drone inspection took 1 day vs at least 2 days before. MaineDOT decided future inspections would use drones. | [S161] |
| Kennebec Sanitary Treatment District (Waterville) | 2019 force main break spilled ~19.2M gallons of sewage into the Kennebec. The pipe was laid inside a storm drain in the early 1970s. | [S190] |

- Note: the FHWA TechBrief says the bridge connects "Wilson and Waterville" [S161]. This looks like a typo for Winslow; the same page places the bridge in Winslow, ME.

---

## 2. Bottlenecks

**Takeaway:** Winter work is expensive, salty, and short-staffed. Bridges and pavement are wearing out faster than crews can inspect and fix them.

### B1. Winter maintenance: high cost, heavy salt, too few drivers
- Maine spreads ~493,000 tons of salt a year, about 11 tons per lane mile [S150].
- The salt has side effects. Maine DEP lists 20 streams as chloride-impaired. In 15 towns, at least one well tested above the chloride limit (2011–20). MaineDOT has spent ~$5.3M since 2006 settling private well claims [S150]. (A podcast transcript says $53M [S151]; the written release [S150] is used here.)
- Town practice is basic. About 28% of municipalities anti-ice, and about 71% never pre-wet their salt [S151].
- Drivers are scarce. MaineDOT ran 20% below planned plow staffing in 2022. A spokesman warned a multi-day storm could force reduced service [S152]. In 2017, MaineDOT had 92 open plow-driver jobs, and new drivers often left soon after getting their license [S153].
- Towns are short too. Portland had 17 unfilled driver jobs in 2023, and getting a CDL takes "six to 12 months" [S154].
- About 67% of Maine lane-departure crashes (2010–19) happened in winter [S150].

### B2. Bridges: many in poor condition, and each needs regular inspection
- 392 of 2,542 bridges are poor (15.4%), more than twice the U.S. rate of 6.7% [S155].
- Federal rules require a routine inspection at least every 24 months. Bridges with serious-or-worse ratings need one every 12 months [S160]. If every Maine bridge were on a 24-month cycle, that would be about 1,270 inspections a year (author arithmetic from [S155][S160]).
- Traditional access needs snooper trucks, lane closures, and climbing. Drones cut those, but processing 3D models can erase the time saved (one MnDOT bridge: 11 h traditional vs 17+ h with drone + processing) [S161].

### B3. Pavement: poor roads, frost heaves, slow manual surveys
- 19% of major roads are poor, which costs each driver $609 a year [S157]. In 2022, 20% of rural roads were poor, ranking Maine in the bottom 10 [S158].
- Frost heaves need frost-susceptible soil, moisture, and freezing, and "Maine has all three." MaineDOT puts out thousands of temporary frost-heave signs each spring [S159].
- How small towns survey their roads today is **unverified**; no published Maine town AI survey was found.

### B4. Water/wastewater: aging pipes and retiring operators
- Maine reported ~$3.1B in clean water needs, $1.7B of it municipal wastewater (treatment, conveyance, overflows) [S186].
- 53% of Maine wastewater operators were over 50 in 2020 [S188]. DEP notes "many of Maine's current water and wastewater managers at or near retirement age" [S186].
- Pipe failures are real locally: Waterville's 19.2M-gallon spill in 2019 [S190].

### Context (not a chosen bottleneck): construction labor and safety
- 92% of U.S. contractors reported hiring difficulty in 2025 [S180]. In Maine, 81% of firms in a small 2018 sample (16 firms) had trouble filling craft jobs [S179]. Maine has launched a 50+ member construction workforce partnership [S181] and AGC Maine's 20-day Maine Construction Academy [S182].
- Construction and extraction workers had 1,032 U.S. deaths in 2024; 370 were falls, slips, and trips [S175]. Construction accounted for 47.8% of all fatal falls in 2023 [S177].

---

## 3. Opportunities

### CR-1 · Drone + AI defect detection for bridge inspection
**Bottleneck:** B2

**In plain language:** A drone flies under and around a bridge and takes close-up photos. AI flags cracks, spalling, and rust for the inspector to check. Fewer lane closures, less climbing, faster reports.

**Already being done**
- **Maine:** FHWA names Maine, Minnesota, and Utah as leading states. At the Ticonic Bridge, a drone reached arches that a snooper truck can't. The inspection took 1 day instead of at least 2 [S161]. VHB runs drone inspections for MaineDOT and found hidden backwall spalling on an inaccessible bridge [S162].
- **Minnesota:** 60+ bridges inspected by drone since 2015 [S163]. A Skydio/Collins Engineers story claims ~30% lower inspection cost and ~50% less field time for MnDOT (vendor figures) [S164].
- **Utah:** drone sign inspections did 16 signs a day vs 3–4, saving ~$100K, $80K of it in traffic control [S161].

| Rating | Score | Why |
|---|---|---|
| Impact | 4/5 | Maine has the 4th-worst bridge share [S156], and a local bridge already shows a halved inspection time [S161]. |
| Feasibility | 4/5 | MaineDOT already uses drones [S161][S162]; the gap is AI on the images, which is well-studied. |
| Time to first pilot | 9 months | Needs a consultant or MaineDOT partner and a Part 107 pilot [S31]. |
| Rough cost | $20k–$80k | One U.S.-compliant drone, software, student time; author's estimate. |

### CR-2 · Road-weather sensors on plows + data-driven salt control
**Bottleneck:** B1

**In plain language:** A sensor on the plow reads road temperature and grip in real time. Software tells the driver, or the spreader directly, how much salt to drop. Less salt, same safety, and less guesswork for new drivers.

**Already being done**
- **Illinois DOT (independent, 2026):** 12 mobile sensors from three makers over three winters. Across 36 paired comparisons, plows with sensors used on average **26% less salt per mile driven**. By contrast, a forecasting decision-support system (MDSS) gave only a 3% cut and did not pay off per route ($521 saved vs $905 cost) [S166].
- **West Des Moines, Iowa:** the city says sensors on plows cut its salt output by over 30% (vendor case study) [S167].
- FHWA case studies find positive benefit-cost for decision support and vehicle tracking in several states [S168].

| Rating | Score | Why |
|---|---|---|
| Impact | 5/5 | Hits cost ($155M/yr [S150]), water pollution [S150], and inexperienced drivers [S152][S153] at once. |
| Feasibility | 4/5 | Sensors are commercial and tested independently [S166]; payback depends on salt per truck [S166]. |
| Time to first pilot | 12 months | Must wait for a winter season; needs a town or MaineDOT garage. |
| Rough cost | $15k–$60k | 2–4 truck sensors plus data logging for one season; author's estimate. |

### CR-3 · Low-cost vehicle-camera road scanning for small towns (potholes, cracks, frost heaves)
**Bottleneck:** B3

**In plain language:** A phone on the dashboard of a town truck records the road. AI marks potholes and cracks on a map, so the road commissioner can plan paving with data instead of memory.

**Already being done**
- **San José, CA:** a 2023–24 city pilot found potholes with 97% accuracy; phase two runs on a $260,000 grant [S169].
- **vialytics** photographs the road every 10 feet and says 1,000+ communities use it [S170]. **Xweather RoadAI** (Vaisala) uses a windshield phone [S171].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Rough roads cost drivers $609/yr [S157], but scanning only plans repairs; it doesn't fix them. |
| Feasibility | 4/5 | Mature tech [S169][S170]; frost-heave detection is new and unproven (author analysis). |
| Time to first pilot | 6 months | One town truck, one spring thaw season. |
| Rough cost | $2k–$20k | Phone mount, cloud or laptop processing; author's estimate. |

### CR-4 · AI first-pass coding of sewer CCTV video for small utilities
**Bottleneck:** B4

**In plain language:** Crews already push camera crawlers down sewer pipes. Watching and coding every defect by hand is slow. AI does a first pass and an operator checks it, so retiring experts' time goes further.

**Already being done**
- NASSCO, the U.S. standards body, endorses "AI algorithm ... as first inspection followed by manual operator checks." But no AI is certified for every code yet [S191].
- SewerAI coded ~75,000 ft for Schaumburg, IL, and found far more severe defects per mile than the manual coding (22.89 vs 3.24), validated by the village's engineer [S192]. A gap that big means humans and AI disagree a lot. That needs checking.

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Real needs [S186] and retiring operators [S188], but small towns inspect few miles a year (author analysis). |
| Feasibility | 3/5 | Software exists [S192], but PACP coding needs a NASSCO license [S191] and labeled Maine video. |
| Time to first pilot | 12 months | Needs a utility to share old video. |
| Rough cost | $10k–$50k | Software, labeling time; uses existing crawlers; author's estimate. |

### Evaluated and not chosen
- **Autonomous or assisted plowing:** no verified U.S. public-road driverless plow pilot was found. Minnesota tested a plow driver-assist system for low visibility starting in 2012 [S195]. Too early and too risky for a student pilot (author analysis).
- **Construction-site robots (rebar tying, layout):** TyBOT is sold as a subcontract and lists no New England states [S185]. Dusty Robotics targets large data center, healthcare, and multifamily jobs [S184]. Maine's construction gap is mainly people and training [S181][S182], not tasks these robots do (author analysis).

---

## 4. Competitors and our edge

**Takeaway:** Incumbents are built for big DOTs and cities. The gap is cheap, cold-tested, Maine-trained tools for MaineDOT crews and the many small towns.

### CR-1 · Bridge drones

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| VHB (consultant) | Drone bridge inspections for MaineDOT, incl. Ticonic Bridge | Contract service; the page describes imaging, not automated AI defect detection | [S162][S161] |
| Skydio + Collins Engineers | Autonomous drones and 3D digital twins for MnDOT | Savings are vendor-reported; no public pricing | [S164] |
| DJI and other foreign drones | Widely used low-cost drones | New foreign models can't get FCC approval since Dec 22, 2025; existing models still OK | [S165] |
| MnDOT drone program | 60+ bridges since 2015 | Minnesota staff and bridges; shows the method, not a Maine service | [S163] |
| 3D-model workflows generally | Structure-from-motion models of whole bridges | Processing time can wipe out the field time saved (11 h vs 17+ h) | [S161] |

**Our edge:**
- **Speed up the slow step.** FHWA says post-processing is the bottleneck [S161]. A student can build defect detection that flags only the frames an inspector must review (author analysis).
- **Maine training data.** Old steel and concrete bridges built before 1970 (59% of the stock [S157]), photographed in Maine light and snow. Generic models are not trained on them (author analysis).
- **Local anchor.** The Ticonic Bridge is next to Colby and already on a drone inspection plan [S161].

### CR-2 · Plow sensors and salt control

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| Vaisala MD30 | Mobile road-surface sensor on plows | In Illinois it broke even only at ~191 tons of salt per plow per year and had more connection issues | [S166][S167] |
| Lufft MARWIS, Teconer RCM511 | Mobile road-surface sensors | Teconer had the best payback (1.47 yr) in Illinois; all need pre-season calibration and training | [S166] |
| MDSS (forecast-based decision support) | Treatment recommendations from forecasts | Illinois saw only a 3% salt cut and no payback per route | [S166] |
| Status quo at Maine towns | Manual rates; ~71% never pre-wet | No data-driven control | [S151] |

**Our edge:**
- **Serve small fleets.** Payback rises with salt per truck [S166]. A cheaper sensor plus spreader logging could pay off for a town with 3–5 trucks (author analysis; needs testing).
- **Cold, coastal-inland Maine testing.** Illinois results may not carry over to Maine freeze-thaw and nor'easters (author analysis).
- **Policy fit.** UMaine's salt report calls for more chloride monitoring and town training through the Maine Municipal Association [S150].

### CR-3 · Road scanning

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| vialytics | Photos every 10 ft, AI distress mapping; 1,000+ communities | U.S. examples are NJ, CT, NY, GA, IN; no Maine town listed; pricing not public | [S170] |
| Xweather RoadAI (Vaisala) | Windshield-phone AI for cracks and potholes | Frost heaves are not listed among detected defects | [S171] |
| Cyclomedia | Street-level imagery + LiDAR, AI pavement detection | Heavy capture system aimed at larger agencies (author analysis) | [S172] |
| Michelin (RoadBotics) | Phone-based AI road rating, 250+ communities | Michelin is discontinuing its Better Roads product by end of 2025; small-town market proved fragile | [S173][S174] |
| San José pilot | City-run AI hazard detection on city vehicles | Grant-funded big-city program | [S169] |

**Our edge:**
- **Frost-heave season focus.** Measure heave height and timing each spring, something listed tools don't advertise (author analysis, based on [S171][S159]).
- **Shared county dataset.** One dataset for several Kennebec towns gives each a cheap baseline (author analysis).

### CR-4 · Sewer video AI

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| RedZone Robotics | Inspection robots, cloud software; 100M+ ft inspected | Customer logos are large utilities; quote-only pricing | [S193] |
| Envirosight | ROVVER crawlers and WinCan software | Home page mentions no AI coding | [S194] |
| SewerAI | AutoCode AI defect coding | Vendor case study; huge disagreement with manual coding needs QC | [S192] |
| NASSCO (standard) | PACP coding standard | No AI certified for all codes; license needed to use PACP codes | [S191] |

**Our edge:**
- **Human-in-the-loop for small districts.** NASSCO's recommended workflow (AI first, operator checks) [S191] fits a utility with a few aging experts [S188] (author analysis).
- **Legacy video.** Maine utilities may hold years of unreviewed video; NASSCO lists "quick coding of legacy inspection video" as a use [S191].

---

## 5. What's needed

| | CR-1 Bridge drones | CR-2 Plow sensors | CR-3 Road scanning | CR-4 Sewer AI |
|---|---|---|---|---|
| **Hardware** | FCC-compliant drone [S165], camera | Mobile road sensor, GPS, spreader controller link | Phone, mount | Existing CCTV crawler |
| **Software/models** | Defect detector (crack, spall, rust) | Salt-rate model, logging dashboard | Pothole/crack/heave detector | PACP defect classifier |
| **Data** | Labeled Maine bridge images | Salt tons per route, road temp, grip | Geotagged road video, spring repeats | Labeled sewer video |
| **Skills** | CV, photogrammetry | Embedded sensors, stats | CV, GIS | CV, PACP coding |
| **Partners** | MaineDOT, VHB [S162] | Waterville/Winslow public works, MaineDOT | Kennebec towns | Kennebec Sanitary Treatment District [S190] |
| **Funding** | MTI [S25]; state research funds (to check) | Town budgets, MTI; DEP chloride programs (to check) | Town budgets | Clean Water SRF (to check) |
| **Regulations** | FAA Part 107 [S31]; 23 CFR 650 [S160] | Vehicle equipment rules (to check) | Privacy of street images | NASSCO license for PACP codes [S191] |

---

## 6. Start small (student projects)

- **CR-2 (best first project):** Put one low-cost infrared road-temperature sensor and a GPS logger on a town plow for one winter. Log salt rate vs road temperature. Compare with a truck without the sensor, the way Illinois did [S166].
- **CR-1:** Build a crack and spall detector on public bridge-defect image sets. Then test it on photos of a Kennebec bridge taken from public land (no flights over traffic).
- **CR-3:** Drive a phone-mounted route in Waterville in March and again in May. Map frost heaves and potholes. Report precision against a hand survey.
- **CR-4:** Ask a utility for 10 hours of old sewer video. Train a model to flag just three defect types. Measure agreement with a certified coder.

---

## 7. Who to contact (organizations and public roles only)

- **State:** MaineDOT Bridge Program and Maintenance & Operations (winter) [S161][S152]; Maine DEP Wastewater program [S186].
- **Local:** City of Waterville and Town of Winslow public works (Ticonic Bridge ends) [S161]; Kennebec Sanitary Treatment District [S190].
- **Industry:** AGC Maine, Augusta [S183]; VHB (MaineDOT drone consultant) [S162].
- **Research and policy:** UMaine Margaret Chase Smith Policy Center (road salt report) [S150]; Maine Municipal Association (town training) [S150]; NEIWPCC (wastewater workforce) [S188]; Colby Davis Institute for AI [S27].
- **Training:** Maine Community College System construction partnership [S181].
- **Model programs elsewhere:** Illinois Center for Transportation (mobile sensor study) [S166]; MnDOT Bridge Office drone program [S163]; City of San José road AI pilot [S169].

---

## 8. Risks and open questions

- **Winter-only testing:** CR-2 can be tested only in winter. Missing one season costs a year.
- **Drone rules:** New foreign drone models are blocked [S165]. Check which U.S.-allowed drones a state contractor may fly.
- **Evidence quality:** Skydio [S164], vialytics [S170], Vaisala [S167], and SewerAI [S192] figures are vendor-reported. Illinois [S166] and FHWA [S161] are the independent anchors.
- **Data conflicts:** MaineDOT lane miles and truck counts vary by year (8,300 lane miles and ~400 trucks in 2022 [S152]; newer MaineDOT pages could not be read). The well-claim cost is $5.3M in [S150] but $53M in a transcript [S151].
- **Safety:** Changing salt rates affects crash risk. Any pilot must keep the town's level of service.
- **Unknown:** How much salt each MaineDOT or town truck spreads per year (sets sensor payback [S166]). How many Kennebec bridges are town-owned. Whether Maine towns already use road-scanning apps.

---

## 9. Sources
All in [`../sources.md`](../sources.md). This file uses S25, S27, S31, S150–S195.

## 10. Dig deeper
- Read the full UMaine "Road Salt in Maine" report behind [S150]: town-level salt and well data.
- Read the full Illinois report [S166], incl. unit prices and per-plow salt use.
- Get the MaineDOT winter readiness figures (lane miles, trucks, salt) from maine.gov directly; the site blocks automated readers.
- Download the FHWA NBI file for Maine and count Kennebec County poor bridges by owner.
- Ask Kennebec Sanitary Treatment District how many miles of sewer video it records per year.
