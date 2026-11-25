# Healthcare and Elder Care

> **Key takeaway:** Maine is the oldest state in the U.S. [S36][S37], and care is running short. Home care goes unstaffed for 23,500 approved hours a week, with Kennebec and Somerset among the hardest-hit counties [S38]. Waterville lost its hospital in 2025 [S39]. The best physical AI bets are **sensors that catch falls fast**, in homes (HC-1) and in nursing homes (HC-2). They stretch a small care workforce, and they target a fall death rate nearly double the U.S. rate [S43].

Ratings and cost ranges below are **the author's judgment**, not sourced figures. Each has a one-line reason.

---

## 1. Overview

**Takeaway:** There are more older people, fewer caregivers, and fewer local facilities.

| Measure | Value | Source |
|---|---|---|
| Maine median age, 2024 | 44.8 (oldest state; Utah youngest at 32.4) | [S36] |
| Share of Mainers age 65+, 2024 | 23.5% (highest in U.S.; U.S. 18.0%) | [S37] |
| Mainers 65+, projected 2030 | more than 425,000 | [S41] |
| Approved home care hours for older adults not staffed | 23,500 hours/week | [S38] |
| Extra full-time care workers needed | 2,300 | [S38] |
| Projected nurse shortage, 2030 | more than 2,800 nurses | [S41] |
| Maine nursing homes closed, past 30 years | 51 (~40%); 9 in the 4 years before Jan 2024 | [S51] |
| Maine adults 65+ who fell in past year, 2023 | 31.3% (U.S. 27.8%) | [S42] |
| Fall death rate age 65+, 2020 | 114.4 per 100,000 in Maine vs 65.6 U.S. (336 deaths) | [S43] |

**Local picture (Waterville / Kennebec)**

| Organization | What changed | Source |
|---|---|---|
| Northern Light Inland Hospital, Waterville | 48-bed hospital stopped patient care May 27, 2025. Was losing ~$1.5M/month. 309 full-time staff affected. | [S39] |
| Northern Light Lakewood, Waterville | 105-bed long-term care facility; stayed open. | [S39] |
| MaineGeneral Health (Augusta + Waterville Thayer campus) | Took on Inland's patients. Primary care waitlist ~4,200; out-of-city ambulance trips from Waterville tripled. | [S40] (partial read) |
| Spectrum Generations | Central Maine Area Agency on Aging; centers in Waterville and Hallowell. | [S50] |

- MaineGeneral's total headcount is **unverified**. Public figures disagree (1,800 to 4,600), so it is left out.

---

## 2. Bottlenecks

**Takeaway:** The core problem is too few hands for a fast-growing older population. Falls are where that shortage turns deadly.

### B1. Home care goes unstaffed
- 23,500 hours a week of approved home care for older adults are not delivered [S38].
- In one MaineCare home care program, the share of people only "partially staffed" rose from 47% to 62% in about a year (Nov 2022 → Dec 2023) [S38].
- Somerset and Kennebec are among the five counties with the greatest need relative to population [S38].

### B2. Falls are common and deadly
- 31.3% of Mainers 65+ fell in the past year, vs 27.8% nationally [S42].
- Maine's fall death rate for ages 65+ was 114.4 per 100,000 in 2020, about 1.7× the U.S. rate of 65.6 [S43].

### B3. Nursing homes are closing, and their aides get hurt
- 51 Maine nursing homes, nearly 40%, have closed over three decades. Low reimbursement and hard-to-keep staff drive it [S51].
- Nursing assistants nationally had 96,480 days-away-from-work injuries in 2020. Patients were the source of 18,060 of them, and lifting/lowering overexertion caused 3,530 [S44].

### B4. Hospital access shrank around Waterville
- Inland Hospital closed in 2025 [S39]. Waterville's out-of-city ambulance transports tripled, and MaineGeneral has a primary care waitlist of about 4,200 [S40].
- Maine expects a shortage of more than 2,800 nurses by 2030 [S41].

---

## 3. Opportunities

### HC-1 · Privacy-preserving in-home fall detection and check-ins
**Bottlenecks:** B1, B2

**In plain language:** A small radar sensor on the wall notices if someone falls or hasn't moved, with no camera. It alerts family or a care agency. Scarce aides can then go where they are needed most, and nobody lies on the floor for hours.

**Already being done**
- UNSW Sydney is piloting millimetre-wave radar fall prediction in aged care facilities. "No cameras or personal identifiers are used" [S47].
- New York State gave older adults 800+ ElliQ AI companion devices. It reported a 95% drop in self-reported loneliness, but with no control group [S46]. This shows a state agency will fund in-home AI devices.

| Rating | Score | Why |
|---|---|---|
| Impact | 5/5 | Targets a measured gap (23,500 unstaffed hours/week [S38]) in the oldest state, with fall deaths at 1.7× the U.S. rate [S43]. |
| Feasibility | 3/5 | Sensors are cheap, but false alarms, consent, and who responds still need solving. |
| Time to first pilot | 9 months | Needs an agency partner (e.g. Spectrum Generations) and IRB-style consent. |
| Rough cost | $10k–$100k | 10–50 homes of off-the-shelf radar sensors plus software; author's estimate. |

### HC-2 · AI video fall detection in nursing homes and memory care
**Bottlenecks:** B2, B3

**In plain language:** Cameras in residents' rooms (with family consent) run AI that spots a fall within seconds and alerts staff. Staff then review the clip to see how the fall happened.

**Already being done**
- Peer-reviewed study in 6 California memory care facilities (66 residents, 436 falls). With real-time AI alerts, time on the ground after a fall dropped by 29.6 minutes. Falls with over an hour on the ground went from 31% to zero [S45]. Note: some authors work for the vendor, SafelyYou.

| Rating | Score | Why |
|---|---|---|
| Impact | 4/5 | Speeds help for the most fall-prone residents while staff are stretched thin [S45][S51]. |
| Feasibility | 4/5 | Commercial products exist, and there is published evidence [S45]. |
| Time to first pilot | 6 months | One unit in one facility, using an existing product. |
| Rough cost | $5k–$50k | Per-facility subscription and cameras; author's estimate. |

### HC-3 · Robotic and sensor-assisted patient lifting
**Bottleneck:** B3

**In plain language:** A robot or smart lift moves a patient from bed to wheelchair, so aides don't strain their backs.

**Already being done**
- RIKEN's RIBA-II robot (Japan, 2011) lifts patients up to 80 kg from floor bedding into a wheelchair. Care staff do this lift about 40 times a day [S48]. It was a research prototype, and field testing was still planned.

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Lifting injuries are real [S44], but ordinary mechanical lifts already help. |
| Feasibility | 2/5 | Robot lifters are still not commercial after 15 years [S48]; safety bar is very high. |
| Time to first pilot | 36 months | Needs medical-device-level safety work. |
| Rough cost | $50k–$250k | Research prototype; author's estimate. |

### HC-4 · Autonomous hospital delivery robots
**Bottleneck:** B4

**In plain language:** A robot carries medications, lab samples, and supplies around the hospital, so nurses stay with patients.

**Already being done**
- Diligent Robotics' Moxi runs in 25 U.S. hospitals. The company reports 1.3M+ deliveries and 600,000+ staff hours returned [S52] (company figures, not independent).

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Saves nurse time where the shortage is growing [S41], but at one hospital system locally. |
| Feasibility | 3/5 | Commercial product [S52], but needs hospital IT, elevator, and security integration. |
| Time to first pilot | 12 months | Hospital procurement is slow. |
| Rough cost | $100k–$500k | Robot lease plus integration; author's estimate. |

### HC-5 · Drone delivery of lab samples and medications
**Bottleneck:** B4

**In plain language:** Drones fly lab samples and urgent medicines between clinics, labs, and the hospital in Augusta, instead of a courier or a patient driving.

**Already being done**
- North Dakota, 2025: an 80-mile drone flight carried medical supplies between two rural towns in about 35 minutes. Federally funded (EDA) [S49].

| Rating | Score | Why |
|---|---|---|
| Impact | 3/5 | Helps Waterville-area access after Inland closed [S39][S40], but only for small items. |
| Feasibility | 3/5 | Proven in rural trials [S49]; Maine winters and FAA beyond-line-of-sight approval are hurdles. |
| Time to first pilot | 18 months | Needs FAA waivers and a health system partner. |
| Rough cost | $50k–$300k | Drone service contract for a trial route; author's estimate. |

---

## 4. What's needed

| | HC-1 Home sensors | HC-2 Facility fall AI | HC-3 Lifting | HC-4 Hospital robots | HC-5 Drones |
|---|---|---|---|---|---|
| **Hardware** | mmWave radar, Wi-Fi/LTE hub | Room cameras, edge box | Robot arm/lift, force sensors | Mobile manipulator robot | Delivery drone, landing pads |
| **Software/models** | Fall/inactivity detection, alert app | Pose estimation, fall classifier | Motion planning, force control | Navigation, elevator API | Route planning, detect-and-avoid |
| **Data** | Labeled falls (staged + real) | Labeled video [S45] | Transfer trials | Hospital maps, task logs | Flight logs, weather |
| **Skills** | Signal processing, ML, UX | CV, privacy engineering | Robotics, biomechanics | Robotics, systems integration | Aviation, embedded |
| **Partners** | Spectrum Generations [S50], home care agencies | Nursing homes, Northern Light Lakewood [S39] | Nursing homes, UMaine | MaineGeneral | MaineGeneral, FAA |
| **Funding** | NIH/NIA SBIR, MTI, state aging funds (NY model [S46]) | Facility budgets, CMS quality funds | NSF, NIH | Hospital capital | EDA (ND model [S49]), USDOT |
| **Regulations** | HIPAA if clinical; consent | Consent, HIPAA, state rules on cameras in rooms | FDA medical device | Hospital safety, HIPAA | FAA Part 107 + BVLOS waiver [S31] |

---

## 5. Start small (student projects)

- **HC-1 (best first project):** Buy a low-cost mmWave radar development board. Stage 200 falls and 200 "sit-downs" on a mat (with a crash pad). Train a classifier and report false-alarm rate. This directly tests the main weakness.
- **HC-2:** Train a pose-estimation fall detector on a public fall dataset. Measure detection delay in seconds.
- **HC-3:** Build a force-sensing mat or bed sensor that warns when a patient is about to get up alone.
- **HC-4:** Simulate a robot delivery route on a Colby building floor plan in ROS 2. Estimate the walking time a nurse would save.
- **HC-5:** Map candidate drone routes between Waterville and Augusta health sites. Check FAA airspace, distance, and winter weather days.

---

## 6. Who to contact (organizations and public roles only)

- **Aging services:** Spectrum Generations, Central Maine Area Agency on Aging (Waterville and Hallowell centers) [S50]; Maine Council on Aging [S54].
- **Care providers:** MaineGeneral Health (Augusta; Thayer campus, Waterville) [S40]; Northern Light Lakewood long-term care, Waterville [S39]; Maine Health Care Association (nursing home trade group) [S51].
- **Research:** UMaine Center on Aging, incl. its Maine Older Adult Research Registry [S53]; Colby Davis Institute for AI [S27].
- **Policy/data:** Maine Center for Economic Policy (home care data) [S38]; Maine Nursing Action Coalition [S41].
- **Model programs elsewhere:** New York State Office for the Aging [S46]; UNSW aged-care radar team [S47].

---

## 7. Risks and open questions

- **Privacy and dignity:** Cameras in bedrooms are sensitive. Radar avoids images, but still collects personal data.
- **Who responds?** An alert is useless if no one can come. Pair any sensor pilot with a response plan.
- **Evidence quality:** The fall-detection study had vendor co-authors [S45]. The ElliQ results are self-reported with no control group [S46]. Hospital robot figures come from the company [S52].
- **Replacing people:** These tools should extend caregivers, not justify fewer of them. Worker groups may push back.
- **Unknown:** MaineGeneral headcount and its plans; how many Waterville-area older adults live alone.

---

## 8. Sources
All in [`../sources.md`](../sources.md). This file uses S27, S31, S36–S54.

## 9. Dig deeper
- Read the full MECEP direct care report behind [S38], including its county tables.
- Read the full Maine Nursing Action Coalition forecast behind [S41].
- Ask Spectrum Generations whether clients would accept a radar sensor pilot.
- Check whether Maine DHHS has funded in-home technology like New York's ElliQ program [S46].
- Look for the outcome of the controlled trial of SafelyYou (ClinicalTrials.gov NCT03685240; status unknown).
