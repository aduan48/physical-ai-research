# Fisheries, Lobstering, and Aquaculture

> **Key takeaway:** Lobster is still Maine's biggest fishery, but it is shrinking. Landings fell to 78.8 million lb in 2025 [S301], and young lobsters are settling at low rates in the southern Gulf of Maine [S303]. Right whale rules are pushing toward rope-free "on-demand" traps, but nobody can yet see where those traps sit on the bottom [S309][S311]. Aquaculture, mostly small oyster and seaweed farms, is growing [S320][S322]. The best physical AI bets are **low-cost ways to find traps underwater** (FISH-1), **deck safety for lobstermen who fish alone** (FISH-2), and **camera counting for small oyster farms** (FISH-3).

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Each has a one-line reason.

Geography note: Waterville and Kennebec County are inland. This sector is coastal and statewide. The nearest research partner is the UMaine Darling Marine Center in Walpole [S325][S326]. Seafood **processing-plant** robots are covered in Manufacturing as MFG-3 [S62]; this page covers work on the water.

---

## 1. Overview

**Takeaway:** Lobster still brings in most of the money, but it is landing less, with fewer harvesters, in warming water. Aquaculture is small but growing fast.

| Measure | Value | Source |
|---|---|---|
| Lobster landings, 2025 | 78.8 million lb, $461.4M, $5.85/lb | [S301] |
| Lobster landings, 2024 | 86 million lb (lowest since 2009), $6.14/lb | [S300] |
| Lobster fishing trips, 2025 vs 2024 | over 21,000 fewer (~10% less effort) | [S301] |
| All Maine commercial fisheries value, 2025 | $619.1M (2024: ~$710M) | [S301][S300] |
| Licensed commercial lobstermen | ~7,100 (1997) → under 5,200 (2024), −27% | [S302] |
| Active lobster harvesters | 4,506 (2016) → 3,667 (most recent year), −18% | [S302] |
| Gulf of Maine surface warming | 0.84°F per decade (1982–2025), nearly 3× the global ocean (0.31°F) | [S304] |
| Maine aquaculture sales | $105.9M (2023), up 44% from $73.4M (2014) | [S320] |
| Farmed and wild oysters, value 2025 | $16.2M, Maine's 4th most valuable fishery | [S301] |
| Aquaculture sites (early 2025) | 149 standard/experimental leases, 671 small limited-purpose licenses | [S321] |
| North Atlantic right whales, 2024 | 384 (16 entanglements, 5 observed deaths that year) | [S305] |
| Fishing and hunting worker death rate, 2024 | 88.8 per 100,000 full-time workers (all workers: 3.3) | [S6] |

- Atlantic salmon is the other big farmed species, but its value is not public. It is left out as **unverified**.

---

## 2. Bottlenecks

**Takeaway:** Lobstermen face fewer lobsters, whale rules that need new gear, lost traps, and dangerous solo work. Small farms are short on workers and data.

### B1. Lobster is declining, and whale rules demand new gear nobody can track yet
- Landings dropped from 86M lb (2024) to 78.8M lb (2025) [S300][S301]. DMR blamed inflation, tariffs, and a late molt [S301].
- Southern Gulf of Maine settlement of baby lobsters stays low. Warming cuts the larvae's main food, *Calanus* copepods [S303]. A recent rebound along coastal Maine may not last [S303].
- Only 384 right whales remain [S305]. Maine DMR got $5.1M to test rope-free "on-demand" gear and holds 85 on-demand units in its gear library [S310]. New federal rules are on pause through 2028 [S308].
- On-demand gear is expensive. Some units cost about $10,000 to start, while a normal trap costs $150–$200 [S308]. MITRE puts current units at $1,200–$7,000 each [S311].
- **Finding the gear is the unsolved part.** In Maine, gear location is "currently limited" and marking is mostly manual [S309]. More than 12 makers each use their own acoustic signal [S311]. NOAA says it still needs "an effective and affordable system for locating the gear" [S307].

### B2. Traps get lost and keep fishing
- Lobstermen lose about 10% of their gear each year (rough estimate) [S314]. One diver group estimates up to 80 traps per fisherman per year [S313].
- Nobody knows how much is on the bottom. Maine does not track it [S314]. Divers have pulled about 13,000 traps so far, and about 20% were still usable [S313].
- Boat sonar can already show traps on the seafloor: "There's one every ten feet it looks like on the sonar" [S313].

### B3. Lobstering is dangerous, and many fish alone
- Lobster had 36 of 288 East Coast fishing deaths in 2000–2019 (13%) [S315].
- Falls overboard killed 18 East Coast lobstermen in 2000–2016. About 21% of all falls came from getting tangled in gear. Most falls were not witnessed. A man-overboard alarm was used in only one case [S316].
- In a NIOSH survey of 103 lobstermen, about 73% had been caught in trap line, and 44% in the past 5 years. Most of these happened while setting gear [S317]. NIOSH's fix relies on a sternman to cut the engine, or a manual kill-switch cable [S317].
- The fleet is shrinking and aging. A young harvester says "the older they get the more it's a toll on their body" [S302].

### B4. Small farms grow fast, but lack hands and data
- The industry is "largely owner-operator-scale shellfish and marine algae farms". Finding skilled workers is "a year-after-year challenge" [S322].
- Oyster bags weigh 60–70 lb and are flipped about 11 times a year, by hand, from kayaks [S323].
- A Brunswick oyster farm found that measuring oysters by hand was the main labor cost of tracking growth. Two of its first three sensor buoys sank [S324].

---

## 3. Opportunities

### FISH-1 · Low-cost gear finder: acoustic ranging plus sonar AI for on-demand and lost traps
**Bottlenecks:** B1, B2

**In plain language:** The boat sends a sound ping and measures how far away its traps are. It then puts every trap on one shared chart, whoever made the gear. The same boat's sonar runs an AI model that spots traps on the seafloor, so lost traps can be found and pulled.

**Already being done**
- NOAA's experimental on-demand fishery off Massachusetts and Rhode Island logged 947 hauls in 2025 [S306]. Reliability rose from 63% (2020) to 91% (2024) [S309].
- MITRE's report for NOAA found that ranging by the boat that set the gear is enough to locate traps in high-conflict areas. It recommends a universal cloud database [S311].
- Blue Ocean Gear's Smart Buoy shows gear on existing plotters (vendor claims) [S336].

| Rating | Score | Why |
|---|---|---|
| Impact | 4/5 | Gear location is the missing piece before on-demand gear can scale [S309][S311], and lost gear costs every lobsterman [S314]. |
| Feasibility | 3/5 | Uses existing sonar and acoustic parts, but underwater acoustics and multi-vendor data are hard. |
| Time to first pilot | 12 months | Can plug into DMR's existing gear library trials [S310]. |
| Rough cost | $20k–$150k | Acoustic modem kit, sonar logger, software, boat time; author's estimate. |

### FISH-2 · Deck safety for lobstermen who fish alone: auto-stop on entanglement or man overboard
**Bottleneck:** B3

**In plain language:** A rugged camera watches the hauler and stern. If the lobsterman is pulled toward the stern by a line, or goes over the side, it stops the hauler and engine and sounds an alarm. A wrist tag backs up the camera.

**Already being done**
- Wireless kill switches like OLAS Guardian cut the engine within 2 seconds of a man overboard [S318]. They do nothing for entanglement on deck (author analysis based on [S318]).
- Zelim's ZOE camera system detected 97% of man-overboard events in a certified trial, with about one false alarm a day [S319]. It is aimed at larger ships (author analysis).
- Onboard catch cameras on low-power Raspberry Pi hardware already measure crabs and lobsters in the UK [S338]. The same deck camera could log catch data later.

| Rating | Score | Why |
|---|---|---|
| Impact | 4/5 | Targets the lobster fishery's main killers, falls overboard and line entanglement [S316][S317]. |
| Feasibility | 3/5 | Vision on a wet, rolling deck is hard, and false stops while hauling are costly. |
| Time to first pilot | 12 months | Dockside tests first, then one boat with a willing owner. |
| Rough cost | $10k–$75k | Marine cameras, edge computer, relay to hauler/engine, testing; author's estimate. |

### FISH-3 · Camera counting and sizing for small oyster farms, linked to low-cost water sensors
**Bottleneck:** B4

**In plain language:** When oysters run across the sorting table, a camera counts them, sizes them, and flags dead shells. The farm gets growth and mortality numbers without hand-measuring. It then lines them up with temperature and chlorophyll data from a cheap buoy.

**Already being done**
- A 2025 study sized oysters from photos, but with 12.2 mm average length error and missed oysters in 2 of 10 count images [S327].
- MIT's Oystamaran robot flips oyster bags by remote control; it is a prototype [S323].
- MAIC and UMaine built a farm buoy for just over $2,000 [S326]. The NSF Seafood Engine is putting more than 12 low-cost sensors on Maine oyster, scallop, and kelp farms [S325].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Saves labor on hundreds of small farms [S321][S322], but each farm's gain is modest. |
| Feasibility | 4/5 | Dry, controlled, on-land imaging; cheap cameras; growers already sort on tables. |
| Time to first pilot | 6 months | One farm, one season of sorting. |
| Rough cost | $5k–$40k | Camera, lighting, small computer, labeling time; author's estimate. |

---

## 4. Competitors and our edge

**Takeaway:** Big players build gear, ROVs, and pen cameras for large salmon farms, offshore fleets, and navies. Few build cheap, cross-vendor tools for a Maine owner-operator or a 2-acre oyster farm.

### FISH-1 Gear finder

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| EdgeTech (5112 system, Trap Tracker app) | On-demand release and gear app | Proprietary acoustics; >12 makers don't talk to each other [S311]. Unit costs $1.2k–$7k vs $150–200 trap [S311][S308]. | [S335] |
| Ashored, Sub Sea Sonics, Desert Star, FioBuoy, SMELTS, Ropeless Systems | Competing on-demand systems | Same: each closed; battery and rope-stowage problems in Maine tests [S310]. | [S307][S310][S334] |
| Blue Ocean Gear Smart Buoy | Gear tracking on plotters | Evidence is vendor-written [S336]; adoption funding came from Canadian programs [S336]. | [S336] |
| NOAA NEFSC gear library and MITRE interoperability work | Lends gear; designing a universal database | Policy and enforcement focus; still lacks an affordable locator [S307][S311]. | [S307][S311] |
| Ghost gear coalition (Center for Coastal Studies, GOMLF, OceansWide) | Finds and removes lost traps | Relies on divers; ~13,000 traps removed against an unknown total [S313][S314]. No automated trap detection found (author analysis). | [S313][S314] |

**Our edge**
- **Vendor-neutral software layer.** MITRE says scale is "intractable" without interoperability and recommends a shared database [S311]. A student team can build the open chart and data format without building new acoustic hardware (author analysis).
- **Sonar AI for ghost traps.** Traps already show on boat sonar [S313]. Labeling Maine sonar images to auto-detect traps is a clear, data-driven student project (author analysis).
- **Local trial channel.** DMR's gear library already lends gear for free and collects data through at least 2027 [S310].

### FISH-2 Deck safety

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| ACR / Exposure Marine OLAS Guardian | Wearable wireless kill switch | Overboard only; does not detect being dragged by line on deck (author analysis); U.S. law doesn't require it on commercial boats [S318]. | [S318] |
| Zelim ZOE | Thermal + visible camera MOB detection | Built and certified for larger ships; ~1 false alarm/day [S319]; price not public. | [S319] |
| NIOSH engineering controls | Line bins, fairleads, gagline kill switch, sternman | Manual; a gagline must be grabbed; a solo fisherman has no sternman [S317]. | [S317] |
| Bangor Univ. / Ystumtec catch camera | Onboard crab/lobster measurement | Research system for UK data; not a safety product [S338]. | [S338] |

**Our edge**
- **Entanglement, not just overboard.** Line entanglement causes about 21% of falls [S316], and most happen while setting gear [S317]. No product found watches for it (author analysis; only products in [S318][S319] checked).
- **Cheap edge hardware works at sea.** A Raspberry Pi in a waterproof housing already runs catch vision on fishing boats [S338].
- **Built for one-person boats.** The kill-switch market targets solo boaters [S318]. Adding a hauler stop is a small, testable retrofit (author analysis).

### FISH-3 Oyster farm vision

| Competitor / existing player | What they do | Where they fall short for central Maine | Source |
|---|---|---|---|
| Aquabyte | Salmon pen cameras: lice, biomass, feeding | Built for salmon net pens in Norway; not shellfish [S330]. | [S330] |
| Blueye, Deep Trekker | Inspection ROVs for fish pens | Inspection video only, no counting; quote-based or no public price [S331][S332]. | [S331][S332] |
| Academic oyster vision (Mexico, 2025) | Photo-based oyster sizing | 12.2 mm error, small dataset, standard conditions only [S327]. | [S327] |
| MIT Oystamaran | Bag-flipping robot | Prototype; remote-controlled; Cape Cod [S323]. | [S323] |
| UMaine DMC / MAIC / Bluesonde / NSF Seafood Engine | Low-cost water sensors for farms | Measures water, not oysters; early buoys sank on one Maine farm [S324][S325]. | [S325][S326] |

**Our edge**
- **Maine oyster data.** The published model has a tiny dataset under fixed conditions [S327]. Labeled images from Maine farms would be new (author analysis).
- **Pairs with sensors already coming.** The Seafood Engine is putting sensors on farms and wants students to help deploy them [S325]. Oyster counts are the missing "output" side of that data.
- **Fits small farms.** Most Maine farms are owner-operator size [S322], too small for salmon-scale systems [S330] (author analysis).

---

## 5. What's needed

| | FISH-1 Gear finder | FISH-2 Deck safety | FISH-3 Oyster vision |
|---|---|---|---|
| **Hardware** | Acoustic modem/transducer, boat sonar logger | Marine cameras, edge computer, relay to hauler and engine, wrist tag | Camera over sorting table, LED lights, small computer |
| **Software/models** | Ranging/localization, shared gear chart, sonar trap detector | Pose estimation, line-drag and overboard detection | Detection, sizing, dead-shell classifier |
| **Data** | Sonar images of traps, on-demand haul logs [S310] | Staged deck video, real haul video | Labeled oyster images, hand-measured ground truth [S324] |
| **Skills** | Underwater acoustics, signal processing, GIS | Computer vision, embedded, marine electrical | Computer vision, farm operations |
| **Partners** | Maine DMR gear library [S310], NOAA NEFSC [S307], GOMLF/OceansWide [S313] | Lobstermen's groups, NIOSH fishing safety [S317] | MAIC, Darling Marine Center [S326], NSF Seafood Engine [S325] |
| **Funding** | NOAA/NFWF gear funds [S310], NSF | NIOSH, Maine Sea Grant | USDA SARE [S324], NSF Seafood Engine [S325], MTI |
| **Regulations** | Federal EFP / Maine special license for test gear [S310]; gear marking rules [S311] | Boat electrical and engine safety; owner consent for cameras | Lease rules; food safety if handling product |

---

## 6. Start small (student projects)

- **FISH-1 (best first project):** Collect sonar screen recordings from a lobster boat or ghost-gear dive trip. Label traps. Train a detector. Report how many traps it finds vs. divers [S313].
- **FISH-2:** Build a mock hauler and stern on land. Stage 100 "pulled by line" events with a dummy and 100 normal hauls. Measure stop time and false stops.
- **FISH-3:** Spend one sorting day on a small oyster farm. Photograph 2,000 oysters with hand measurements. Train a sizing model and compare error with the 12.2 mm baseline [S327].

---

## 7. Who to contact (organizations and public roles only)

- **State and federal:** Maine DMR Maine Innovative Gear Library [S310]; NOAA NEFSC Gear Research Team [S306][S307].
- **Industry groups:** Maine Lobstermen's Community Alliance [S310]; Maine Lobstermen's Association [S312]; Maine Aquaculture Association [S320].
- **Research:** Gulf of Maine Research Institute (warming data, electronic monitoring) [S304][S328]; UMaine Darling Marine Center [S325]; Maine Aquaculture Innovation Center [S326]; UMaine Lobster Institute / ALSI [S303]; Maine Sea Grant (UMaine is the Sea Grant institution [S325]).
- **Ghost gear:** Gulf of Maine Lobster Foundation (also runs eMOLT sensors with NOAA [S337]); OceansWide; Center for Coastal Studies [S313][S314].
- **Funding networks:** NSF Seafood Engine, led by NERACOOS [S325].
- **Model programs elsewhere:** MIT Sea Grant Oystamaran team [S323]; GMRI–CVision AI electronic monitoring [S328][S329].

---

## 8. Risks and open questions

- **Trust:** Lobstermen fear that joining gear trials will be read as support for mandates [S308]. They also fought GPS tracking in court [S312]. Any camera or data project needs clear data ownership.
- **Policy may move:** New right whale rules are paused until 2028 [S308]. Demand for gear location depends on what comes next.
- **Evidence quality:** Blue Ocean Gear and Zelim figures come from vendors [S336][S319]. Ghost gear counts are rough estimates [S313][S314].
- **Hardware at sea:** Buoys sank on a Maine farm [S324]. Saltwater, ice, and spray will break prototypes.
- **Bigger players drifting away:** Saildrone now focuses on defense and ocean intelligence [S333]. Don't count on big vendors to serve small Maine users.
- **Unknown:** How many Maine lobster boats fish solo; Atlantic salmon value; current lease and acreage counts (the Sea Grant page could not be read).

---

## 9. Sources
All in [`../sources.md`](../sources.md). This file uses S6, S62, S300–S338.

## 10. Dig deeper
- Read the full MITRE interoperability report [S311], especially the cost and localization sections.
- Read the NOAA NEFSC three-year on-demand gear report when it is published (in progress per [S306]).
- Ask Maine DMR for anonymized gear-library haul and failure data [S310].
- Read the Maine Aquaculture Association 2025 economic report summarized in [S320].
- Check whether eMOLT's fishermen-carried sensors [S337] could also carry a deck camera.
- Check NIOSH for lobster-specific fatality data after 2019.
