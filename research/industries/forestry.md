# Forestry, Logging, Sawmills, Paper and Wood Products

> **Key takeaway:** Maine's forest economy is big ($8.3B output [S1]) but is losing workers [S1][S2][S5]. The best near-term physical AI bet is **drone + AI forest inventory**: research is already underway at UMaine with Colby as a partner [S12][S13][S14], and the hardware is cheap. The highest-impact but hardest bet is **remote-operated logging machines**, which Sweden is already testing [S18][S19].

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Each has a one-line reason.

---

## 1. Overview

**Takeaway:** The sector is shrinking in jobs and paper, but growing in wood products. That means more output from fewer people.

| Measure | Value | Source |
|---|---|---|
| Total output, 2024 (incl. multiplier effects) | $8.3 billion | [S1] |
| Total jobs supported, 2024 (incl. multipliers) | 29,000+ | [S1] |
| Labor income, 2024 (incl. multipliers) | $2.1 billion | [S1] |
| Direct sector jobs, 2024 | 13,669 (1.8% of Maine jobs) | [S2] |
| Share of state GDP | 3.45% | [S3] |
| Sector employment change, 2019→2024 | −7% | [S1] |
| Paper manufacturing sales, 2019→2024 | −41% | [S1] |
| Wood product manufacturing sales, 2019→2024 | +45% | [S1] |
| Logging + log trucking output (2017, incl. multipliers) | $619 million; ~9,000 jobs | [S11] |

**Major employers near Colby**

| Employer | Location | What it makes | Size | Source |
|---|---|---|---|---|
| Sappi North America, Somerset Mill | Skowhegan (≈20 mi from Colby) | Coated paper, packaging board | 780 employees; $500M machine upgrade | [S8] |
| Huhtamaki | Waterville | Paper plates / molded fiber packaging | 485 employees (2019; may be outdated) | [S9] |

- Kennebec/Somerset county job counts by NAICS code are **not yet collected**. See "Dig deeper".

---

## 2. Bottlenecks

**Takeaway:** People are the binding constraint, followed by data on the forest itself.

### B1. Loggers and log truckers are aging and hard to replace
- Average Maine logger age is 45 or older [S4].
- A 2019 study for the Professional Logging Contractors of Maine projected the industry needs to hire at least 2,000 people in a decade [S4].
- Logging lost 500+ jobs from 2019 to 2024 [S2]. In 2025, Maine Public reported the logging workforce "is dwindling" [S5].
- A new hire costs a contractor about $100,000 in the first year [S4]. Technical high school logging programs fell from 20 to 5 [S4].
- Log truck drivers earned a median $15.23/hour (2017), among the lowest for heavy truck drivers; thin contractor margins limit raises [S10].

### B2. Logging is the deadliest job in the U.S.
- 2024 fatal injury rate: **110.4 per 100,000 full-time workers**, vs 3.3 for all workers. 51 logging deaths in 2024 [S6].
- Forest, conservation, and logging worker deaths stayed at 42–55 per year, 2020–2024 [S7].

### B3. Forest inventory and forest health data is slow, costly, and short on skilled people
- Under-canopy data like trunk width matters to the timber industry but is "challenging and time-consuming to collect" [S12].
- In a 2024 survey of large Maine forest owners and managers, the barriers to remote sensing were **personnel capacity and lack of knowledge** [S15]. 67% already use LiDAR [S15].
- Spruce budworm is rising in northern Maine [S17]. State monitoring relies on branch sampling and aerial surveys [S17].

### B4. Mills must produce more with fewer workers
- Sector jobs fell 7% while wood product sales rose 45% (2019–2024) [S1].
- Paper sales fell 41% [S1]. Paper mills compete on cost, so unplanned downtime hurts. (The downtime link is the author's inference, not a sourced figure.)

---

## 3. Opportunities

### FOR-1 · Remote-operated and assisted logging machines
**Bottlenecks:** B1, B2

**In plain language:** An operator runs a forwarder or harvester from a safe cab or office, with cameras and sensors, instead of sitting in the machine in the woods. Later, software automates repeat tasks like crane loading.

**Already being done**
- Sweden, 2024: a forwarder near Västerås was driven by an operator ~90 km away in Skogforsk's Uppsala lab. A drone carried a portable 5G base station to fill a coverage gap [S18]. Partners: SCA, Skogforsk, Ericsson, Telia, Volvo CE, Mid Sweden University [S18].
- Skogforsk found VR remote crane control performed "comparable to" in-cab control. But latency above ~200 ms made the crane impossible to control normally [S19].
- Swedish research: operators are 35–38% of forwarding cost in northern Sweden; remote work can improve operator conditions [S20].

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
- Lucidyne (Oregon) uses deep learning to grade lumber at up to 4,500 ft/minute [S22].
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

## 4. What's needed

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

## 5. Start small (student projects)

- **FOR-2 (best first project):** Fly a consumer drone over a stand in the Colby woods (with permission and a Part 107 pilot [S31]). Train a tree-crown detection model. Compare counts to a hand-measured plot. Deliverable: accuracy table and a map.
- **FOR-3:** Photograph log ends on 50 truckloads at a local yard (with permission). Build a log-end counter and diameter estimator. Compare to the mill's scale tickets.
- **FOR-1:** Build a 1:10 scale teleoperated crane with a ROS arm. Measure task time vs added latency (0–600 ms) to reproduce Skogforsk's finding [S19].
- **FOR-4:** Put a $50 accelerometer + microcontroller on a campus fan or pump. Train an anomaly detector. Hand facilities a dashboard.

---

## 6. Who to contact (organizations and public roles only)

- **Colby:** Davis Institute for Artificial Intelligence [S27]; the Colby faculty member on the UMaine–Colby forest LiDAR project, Environmental Studies [S13]; Colby Computer Science.
- **UMaine:** Maine-FOREST project (NSF EPSCoR) [S12][S32]; Wheatland Geospatial Lab [S13][S30]; Center for Research on Sustainable Forests (CRSF) and its Cooperative Forestry Research Unit (CFRU) [S16]; School of Forest Resources.
- **Industry groups:** Professional Logging Contractors of Maine [S4]; Maine Forest Products Council [S1]; FOR/Maine [S25].
- **Companies:** Sappi Somerset Mill (Skowhegan) [S8]; Huhtamaki (Waterville) [S9].
- **Funders:** Maine Technology Institute [S25][S26]; NSF EPSCoR [S32].
- **State:** Maine Forest Service (spruce budworm program) [S17].

---

## 7. Risks and open questions

- **Connectivity:** Can teleoperation work in Maine woods without a custom network? Latency above ~200 ms breaks control [S19].
- **Cost vs margins:** Logging contractors have thin margins [S10]. Who pays for a $250k+ retrofit?
- **Jobs:** Automation could be framed as cutting jobs. In a shortage it may instead keep operations running. Needs local interviews.
- **Under-canopy drones** are still "preliminary" research [S12].
- **Data quality:** 21 of 32 sources here are search summaries only (🔎), because several sites block automated readers. The two DECD reports [S1][S2] are the most important to re-check by hand.
- **Unknown:** Kennebec and Somerset county job counts in NAICS 113, 321, 322.

---

## 8. Sources
S1–S32 in [`../sources.md`](../sources.md). This file uses S1–S32.

## 9. Dig deeper
- Download and read the full DECD 2024 report [S1] and summary [S2] by hand (blocked to scripts).
- Get county data: Maine DOL Center for Workforce Research (QCEW by county) or a free Census API key for County Business Patterns.
- Read the full Maine Policy Review spruce budworm paper [S15].
- Ask the Maine-FOREST team what data they need labeled. A student could help.
- Look for the 2025 Maine Public story on training the next generation of loggers [S5] for current training programs.
