# Forestry, Logging, Sawmills, Paper and Wood Products

> **Key takeaway:** Maine's forest economy is big ($8.3B output [S1]) but is losing workers [S1][S5][S34]. The best near-term physical AI bet is **drone + AI forest inventory**: research is already underway at UMaine with Colby as a partner [S12][S13][S14], and the hardware is cheap. The highest-impact but hardest bet is **remote-operated logging machines**, which Sweden is already testing [S18][S19].
>
> **Biggest competitor gap:** small mills and woodlot owners. Scanner makers sell full grading lines to large mills [S22][S407], and drone-inventory startups serve large timber firms [S404]. Low-cost, Maine-trained log-yard vision and inventory is open (author analysis; see section 4).

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Each has a one-line reason.

---

## 1. Overview

**Takeaway:** The sector is shrinking in jobs and paper, but growing in wood products. That means more output from fewer people.

| Measure | Value | Source |
|---|---|---|
| Total output, 2024 (incl. multiplier effects) | $8.32 billion | [S1] |
| Total jobs supported, 2024 (incl. multipliers) | 29,637 | [S1] |
| Labor income, 2024 (incl. multipliers) | $2.08 billion | [S1] |
| Direct sector jobs, 2024 | 11,888 | [S1] |
| **Kennebec County** direct jobs, 2024 | 790 (6.6% of sector) | [S1] |
| **Somerset County** direct jobs, 2024 (next county north of Waterville) | 1,743 (14.7% of sector; 2nd-highest county) | [S1] |
| Share of state GDP | 3.45% | [S1][S3] |
| Sector employment change, 2019→2024 | −7% | [S1] |
| Direct GDP per worker, 2019→2024 (inflation-adjusted) | $467,767 → $411,461 (−12%) | [S1] |
| Projected sector job change, 2022→2032 | −3% (−655 jobs) | [S34] |
| Paper manufacturing sales, 2019→2024 | −41% | [S1] |
| Wood product manufacturing sales, 2019→2024 | +45% | [S1] |
| Logging + log trucking output (2017, incl. multipliers) | $619 million; ~9,000 jobs | [S11] |

**Major employers near Colby**

| Employer | Location | What it makes | Size | Source |
|---|---|---|---|---|
| Sappi North America, Somerset Mill | Skowhegan (≈20 mi from Colby) | Coated paper, packaging board | 780 employees; $500M machine upgrade | [S8] |
| Huhtamaki | Waterville | Paper plates / molded fiber packaging | 485 employees (2019; may be outdated) | [S9] |

- The 2023 closure of the Androscoggin paper mill in Jay is named as a cause of job losses [S1].
- Sub-sector (logging vs sawmill vs paper) job counts per county are **not yet collected**. See "Dig deeper".

---

## 2. Bottlenecks

**Takeaway:** People are the binding constraint, followed by data on the forest itself.

### B1. Loggers and log truckers are aging and hard to replace
- Average Maine logger age is 45 or older [S4].
- A 2019 study for the Professional Logging Contractors of Maine projected the industry needs to hire at least 2,000 people in a decade [S4].
- Maine had 1,463 logging equipment operators in 2022. 32% are near retirement. The occupation is projected to shrink 23% by 2032, yet still needs ~211 new hires a year [S34].
- 36% of heavy truck drivers and 39% of millwrights are near retirement [S34].
- Pulp and paper caused most of the 2019–2024 job decline, but logging also lost jobs [S1]. In 2025, Maine Public reported the logging workforce "is dwindling" [S5].
- A new hire costs a contractor about $100,000 in the first year [S4]. Technical high school logging programs fell from 20 to 5 [S4].
- Log truck drivers earned a median $15.23/hour (2017), among the lowest for heavy truck drivers; thin contractor margins limit raises [S10].

### B2. Logging is the deadliest job in the U.S.
- 2024 fatal injury rate: **110.4 per 100,000 full-time workers**, vs 3.3 for all workers. 51 logging deaths in 2024 [S6].
- Forest, conservation, and logging worker deaths stayed at 42–55 per year, 2020–2024 [S7].

### B3. Forest inventory and forest health data is slow, costly, and short on skilled people
- Under-canopy data like trunk width matters to the timber industry but is "challenging and time-consuming to collect" [S12].
- In a 2024 survey of large Maine forest owners and managers, the barriers to remote sensing were **personnel capacity and lack of knowledge** [S15]. 67% already use LiDAR [S15].
- Spruce budworm is rising in northern Maine [S17]. State monitoring relies on branch sampling and aerial surveys [S17].

### B4. Mills must produce more with fewer workers, but output per worker is falling
- Sector jobs fell 7% while wood product sales rose 45% (2019–2024) [S1].
- Direct GDP per worker fell from $467,767 to $411,461 (2019→2024, inflation-adjusted) [S1].
- Paper sales fell 41% [S1]. Paper mills compete on cost, so unplanned downtime hurts. (The downtime link is the author's inference, not a sourced figure.)

---

## 3. Opportunities

### FOR-1 · Remote-operated and assisted logging machines
**Bottlenecks:** B1, B2

**In plain language:** An operator runs a forwarder or harvester from a safe cab or office, with cameras and sensors, instead of sitting in the machine in the woods. Later, software automates repeat tasks like crane loading.

**Already being done**
- Sweden, 2024: a forwarder near Västerås was driven by an operator ~90 km away in Skogforsk's Uppsala lab. A drone carried a portable 5G base station to fill a coverage gap [S18]. Partners: SCA, Skogforsk, Ericsson, Telia, Volvo CE, Mid Sweden University [S18].
- Skogforsk found VR remote crane control performed "comparable to" in-cab control. But latency above ~200 ms made the crane impossible to control normally [S19].
- Swedish simulation of 1,100 harvest sites: one teleoperator running several forwarders cut extraction cost by 7%, and up to 15% on long hauls over 500 m [S20].

| Rating | Score | Why |
|---|---|---|
| Impact | 4/5 | Removes people from the deadliest job [S6] and makes the job appealing to new workers. |
| Feasibility | 2/5 | Maine woods have weak cell coverage, and Sweden's test needed a custom drone network [S18]. |
| Time to first pilot | 24 months | Needs an OEM partner, a willing contractor, and connectivity work. |
| Rough cost | $250k–$2M | One retrofitted machine plus a remote station and network; author's estimate. |

### FOR-2 · Drone + AI forest inventory and pest detection
**Bottleneck:** B3

**In plain language:** Fly drones above and below the canopy. AI counts trees, measures trunk width, spots species and damage. Landowners get cheaper, more frequent inventories.

**Already being done**
- UMaine (NSF Maine-FOREST): AI drones that fly under the canopy, detect trees, and plan paths. Goal: trunk width, species, disease. Early stage [S12].
- UMaine + Colby: airborne and ground LiDAR for forest measurement [S13]. Colby's role, ~$1M, is AI to process forest data for landowners [S14].
- UMaine Wheatland Geospatial Lab builds LiDAR-based "Enhanced Forest Inventories" [S30].
- Under-canopy drone autonomy research at UPenn's GRASP Lab [S29] and in a 2025 preprint on photogrammetric inventory [S28].

| Rating | Score | Why |
|---|---|---|
| Impact | 4/5 | Fills a documented skills and capacity gap [S15] across Maine's large forest land base. |
| Feasibility | 4/5 | Off-the-shelf drones work above canopy today; under-canopy is research-grade [S12]. |
| Time to first pilot | 6 months | Colby already has a partnership and data pipeline [S13][S14]. |
| Rough cost | $5k–$50k | Consumer/prosumer drone + GPU time; LiDAR payloads push the top end; author's estimate. |

### FOR-3 · Computer vision for log scaling and lumber grading at small and mid-size mills
**Bottleneck:** B4 (also B1, through log truck turnaround)

**In plain language:** Cameras at the log yard measure each truckload. Cameras on the line grade boards. Fewer people needed for repetitive measuring, and better yield.

**Already being done**
- MiCROTEC's AI strength-grading scanner at Södra's Värö sawmill (Sweden): 240 boards/minute, four-sided [S21].
- MiCROTEC's Lucidyne scanner grades boards with deep learning at up to 4,500 ft/minute [S22]. Hampton Lumber runs it at three Oregon sawmills [S35].
- Vendors sell camera-based log scaling from truck cameras or a phone photo [S23] (vendor claims; no accuracy data published there).

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Helps mills grow output with fewer workers [S1], but large mills already own scanners. |
| Feasibility | 4/5 | Commercial products exist [S21][S22]; small mills are the gap. |
| Time to first pilot | 6 months | A camera at one log yard is a small, low-risk install. |
| Rough cost | $10k–$150k | Cameras + edge computer for scaling; full grading lines cost far more; author's estimate. |

### FOR-4 · Predictive maintenance sensors for paper and packaging mills
**Bottleneck:** B4

**In plain language:** Wireless vibration and temperature sensors on motors, rolls, and bearings. ML flags a failing part weeks before it breaks.

**Already being done**
- A paper mill using Emerson online vibration monitoring caught a misinstalled roller bearing, avoiding ~$40,000 in downtime [S24] (vendor case study).

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Protects two large local employers [S8][S9] but gains per mill are incremental. |
| Feasibility | 3/5 | Mature tech, but mills are cautious and already use vendor systems. |
| Time to first pilot | 9 months | Needs plant access, safety training, and IT approval. |
| Rough cost | $20k–$200k | Sensor kit plus software for one machine line; author's estimate. |

---

## 4. Competitors and our edge

**Takeaway:** Big equipment makers already sell most of these tools, but to big buyers. Machine makers sell in-cab assist, not remote operation. Scanner makers sell full grading lines to large mills. The clearest opening is **low-cost, Maine-trained vision and inventory for small mills and woodlot owners** (FOR-2, FOR-3). FOR-4 is the most crowded.

### FOR-1 · Remote-operated and assisted logging machines

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| Ponsse | Harvester Active Crane: the operator steers the harvester head, not each crane joint. Needs the Opti 5G control system. | Driver assist in the cab, not remote operation. "Currently available in the Scorpion product range's harvesters in certain market areas." | [S402] |
| Komatsu Forest | Smart Crane on forwarders: grapple run with three joystick movements; boom extension automated. | Still an operator in the cab; no remote mode described. Comes with a new machine, so it does not help older fleets (author analysis). | [S400] |
| John Deere | Intelligent Boom Control: the operator moves the head and the system guides the boom (first on the 1270G, CH7 boom). | Same: assist only, and only on certain new models and booms. | [S401] |
| Skogforsk lab + SCA, Ericsson, Telia, Volvo CE, Mid Sweden University | Drove a forwarder from ~90 km away over 5G; VR remote crane tests. | Needed a drone-carried 5G base station to fill a coverage gap [S18]. Latency over ~200 ms broke crane control [S19]. Maine woods have no such private networks (author analysis). | [S18][S19] |
| SLU (Sweden) | Model: one teleoperator running several forwarders cuts extraction cost 7–15%. | Simulation of Swedish harvest sites, not Maine stands or contractors. | [S20] |

**Our edge:**
- No major maker offers true remote operation yet. Their products are in-cab assist [S400][S401][S402]. A low-cost assist or teleop retrofit for machines Maine contractors already own is open (author analysis).
- Maine contractors run on thin margins [S10], so a $250k+ remote system is a hard sell. A cheap, staged path (cameras and assist first, remote later) fits them better (author analysis).
- The key research question, how much latency and bandwidth an operator can tolerate [S19], can be studied on a small scale model at Colby before any field work.
- Honest limit: this is the weakest edge in the file. Real progress needs an OEM or dealer partner.

### FOR-2 · Drone + AI forest inventory and pest detection

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| DJI Enterprise | Matrice 400 drone with Zenmuse L3 LiDAR; DJI Terra builds point clouds. Rated to −20 °C. | Sells hardware and generic point clouds. Forest analysis is left to "third-party software". No species identification is mentioned. | [S406] |
| Treeswift (UPenn GRASP Lab spin-out, Philadelphia) | Under-canopy LiDAR drones (SwiftCruise) for timber and carbon inventory. $4.8M seed round (2022). | Customers named are large industrial timber firms (Weyerhaeuser, Molpus, Superior Pine) [S404]. No Maine deployment found (author analysis). | [S403][S404] |
| Pix4D | Photogrammetry software. A Quebec study used it to outline tree crowns and tell conifer from deciduous. | One 2018 study, two classes only [S405]. Needs a skilled operator, and Maine owners name staff capacity and knowledge as the main barriers [S15]. | [S405][S15] |
| UMaine Maine-FOREST and Wheatland Geospatial Lab | Under-canopy AI drones; LiDAR-based Enhanced Forest Inventories. | Under-canopy work is still "preliminary" research [S12]. A partner more than a competitor. | [S12][S30] |

**Our edge:**
- The gap is not drones but **people and analysis**. Maine forest owners already use LiDAR (67%) but lack staff and know-how [S15]. A turnkey "fly, count, report" service fills that gap (author analysis).
- Colby is already funded to build AI for forest data with UMaine [S13][S14]. That gives access to Maine ground-truth plots no outside vendor has.
- Treeswift serves large timber companies [S404]. Smaller Maine owners are likely below its focus (author analysis).
- Models tuned to Maine species (spruce, fir, northern hardwoods) and to spruce budworm damage [S17] would beat generic tools (author analysis).

### FOR-3 · Computer vision for log scaling and lumber grading

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| MiCROTEC (Lucidyne) | Deep-learning lumber grading at up to 4,500 ft/min; AI strength grading at 240 boards/min. | Built for high-speed lines at large mills (Hampton Lumber, Oregon; Södra, Sweden) [S21][S35]. Too big for small Maine mills (author analysis). | [S21][S22][S35] |
| USNR | Automated grading (BioVision, Transverse and Lineal High Graders) with deep-learning defect detection. | Full-line mill systems; no price published. Reference mill is in North Carolina. | [S407] |
| BID Group (Comact brand) | ResawExpert: AI resaw optimizer that grades all four board faces, incl. NHLA hardwood grades. | Brand new; first install at one Quebec flooring maker. Resaw-line equipment, not a cheap add-on. | [S408] |
| Roboflow (DIY vision platform) | Camera-based log scaling from truck cameras or a phone. | No accuracy data published. The mill must build and label its own model (author analysis). | [S23] |

**Our edge:**
- Incumbents sell full grading lines to big mills [S22][S35][S407]. **Log-yard scaling for small and mid-size mills** is the open niche: one camera, one edge computer (author analysis).
- No vendor publishes accuracy for camera log scaling [S23]. A student project that measures accuracy against scale tickets would itself be useful.
- A labeled image set of Maine logs (species, bark, snow and ice on logs in winter) is something no national vendor has (author analysis).

### FOR-4 · Predictive maintenance sensors for paper and packaging mills

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| Emerson | Online vibration monitoring; caught a bad roller bearing, ~$40k downtime avoided. | Vendor case study only. | [S24] |
| SKF | Enlight Collect IMx-1 wireless vibration and temperature sensor; mesh network; 4-year battery. Data can go to SKF's cloud analysis centers. | Tied to SKF's own service model. Evidence is vendor-written. | [S409] |
| Augury | Full-stack machine health for pulp and paper (named customer: Essity). Claims 3–10× first-year ROI and >99% accuracy. | All figures are vendor claims. | [S410] |
| Analog Devices (OtoSense Smart Motor Sensor) | Turnkey motor sensor with app and web dashboard; 0–10 health score. | Vendor-only evidence; cloud dashboard means mill IT approval (author analysis). | [S411] |

**Our edge:**
- This market is crowded with large, credible vendors [S24][S409][S410][S411]. A new product is unlikely to win (author analysis).
- The realistic role is **independent testing**: comparing a cheap sensor to a vendor system on one line, since all published results are vendor-written [S24][S410].
- Sappi Somerset and Huhtamaki are near Colby [S8][S9], which helps access, but they likely already use vendor systems (author analysis).

---

## 5. What's needed

| | FOR-1 Remote logging | FOR-2 Drone inventory | FOR-3 Mill vision | FOR-4 Mill sensors |
|---|---|---|---|---|
| **Hardware** | Retrofit kit, cameras, LiDAR, remote cab, private LTE/5G or mesh | Drone, RGB/multispectral camera, optional LiDAR | Industrial cameras, lighting, edge GPU | Vibration/temp sensors, gateway |
| **Software/models** | ROS, low-latency video, teleop UI [S19] | Tree detection/segmentation, SLAM, photogrammetry | Object detection, segmentation, measurement | Anomaly detection, time series |
| **Data** | Machine logs, operator video | Ground-truth plots, LiDAR [S13][S30] | Labeled log/board images | Run-to-failure history |
| **Skills** | Robotics, networking, controls | CV, GIS, forestry | CV, embedded | Signal processing, ML |
| **Partners** | PLC, machine dealers, a logging contractor | UMaine Maine-FOREST, Wheatland Lab, CFRU | A Maine sawmill | Sappi Somerset, Huhtamaki |
| **Funding** | MTI [S26], EDA Tech Hub [S25], NSF | NSF EPSCoR [S32], USDA, MTI | MTI | MTI, company funds |
| **Regulations/permits** | OSHA logging rules; FCC for radios | FAA Part 107 [S31]; landowner permission | Plant safety | Plant safety, IT security |

---

## 6. Start small (student projects)

- **FOR-2 (best first project):** Fly a consumer drone over a stand in the Colby woods (with permission and a Part 107 pilot [S31]). Train a tree-crown detection model. Compare counts to a hand-measured plot. Deliverable: accuracy table and a map.
- **FOR-3:** Photograph log ends on 50 truckloads at a local yard (with permission). Build a log-end counter and diameter estimator. Compare to the mill's scale tickets.
- **FOR-1:** Build a 1:10 scale teleoperated crane with a ROS arm. Measure task time vs added latency (0–600 ms) to reproduce Skogforsk's finding [S19].
- **FOR-4:** Put a $50 accelerometer + microcontroller on a campus fan or pump. Train an anomaly detector. Hand facilities a dashboard.

---

## 7. Who to contact (organizations and public roles only)

- **Colby:** Davis Institute for Artificial Intelligence [S27]; the Colby faculty member on the UMaine–Colby forest LiDAR project, Environmental Studies [S13]; Colby Computer Science.
- **UMaine:** Maine-FOREST project (NSF EPSCoR) [S12][S32]; Wheatland Geospatial Lab [S13][S30]; Center for Research on Sustainable Forests (CRSF) and its Cooperative Forestry Research Unit (CFRU) [S16]; School of Forest Resources.
- **Industry groups:** Professional Logging Contractors of Maine [S4]; Maine Forest Products Council [S1]; FOR/Maine [S25].
- **Companies:** Sappi Somerset Mill (Skowhegan) [S8]; Huhtamaki (Waterville) [S9].
- **Funders:** Maine Technology Institute [S25][S26]; NSF EPSCoR [S32].
- **State:** Maine Forest Service (spruce budworm program) [S17].

---

## 8. Risks and open questions

- **Connectivity:** Can teleoperation work in Maine woods without a custom network? Latency above ~200 ms breaks control [S19].
- **Cost vs margins:** Logging contractors have thin margins [S10]. Who pays for a $250k+ retrofit?
- **Jobs:** Automation could be framed as cutting jobs. In a shortage it may instead keep operations running. Needs local interviews.
- **Under-canopy drones** are still "preliminary" research [S12].
- **Data quality:** Many sources here are search summaries only (🔎), because several sites block automated readers. The key economic figures now come from the full reports [S1][S34].
- **Unknown:** Kennebec and Somerset job counts split by logging (NAICS 113), sawmills (321), and paper (322).

---

## 9. Sources
All in [`../sources.md`](../sources.md). This file uses S1, S3–S35, S400–S411. (S2 was withdrawn.)

## 10. Dig deeper
- Read the FOR/Maine workforce report [S34] for training programs and wage data by occupation.
- Visit UMaine's Advanced Manufacturing Center "B.O.T. Loft" robotics training space [S1].
- Get county data: Maine DOL Center for Workforce Research (QCEW by county) or a free Census API key for County Business Patterns.
- Read the full Maine Policy Review spruce budworm paper [S15].
- Ask the Maine-FOREST team what data they need labeled. A student could help.
- Look for the 2025 Maine Public story on training the next generation of loggers [S5] for current training programs.
