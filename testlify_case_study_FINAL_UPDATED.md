# TESTLIFY: BUILDING STRUCTURE IN AMBIGUITY
**Product Design at Scale**  
*June 2023 – January 2026 (2.5 years)*

---

## AT A GLANCE

**My Role**  
Product Designer leading end-to-end feature development in a fast-moving B2B SaaS environment. I translated ambiguous business requirements into production-ready systems, owned features from concept through deployment, and maintained platform coherence across 505 UX-tracked tickets.

**Scope & Surfaces**  
• Employer Portal (assessment creation, test management, reporting)  
• Candidate Test Portal (web + Android/iOS apps)  
• AI Interview System (chat, video, audio simulations)  
• Marketing Website (positioning, conversion optimization)  
• White-label & Reseller Systems (enterprise configurations)

**Scale of Work (Jira Metrics)**  
• **505 UX-tracked tickets** delivered (tasks, epics, improvements, bugs)  
• **498 issues reported by me** (proactive bug identification, UX improvements)  
• **130 resolved recently** (active delivery velocity)  
• **122 created recently** (ongoing pipeline management)  
• Validated across **4 environments** (Preview → Staging → Release → Production)  
• Tested across **5 browsers** (Chrome, Safari, Edge, Firefox, mobile browsers)  
• Validated on **4 platforms** (Windows, macOS, iOS, Android)

**Context**  
Platform serves 4,500+ job roles across 50+ industries with 100+ ATS integrations. Achieved 80% candidate completion rate (2-3x industry average). Companies reported 82% reduction in time-to-hire.

---

## THE REAL CHALLENGE

Most case studies talk about building features. This is about **building structure where none existed.**

**The Daily Reality**  
Founders provided high-level references: "Build something like this competitor feature." No PRDs. No structured documentation. Requirements came from sales calls, client requests, support tickets—often vague, half-defined, missing edge cases.

**My Actual Responsibilities**  
• **Translate ambiguity into clarity:** Convert "make resume screening automatic" into structured flows with defined logic, edge cases, validation rules  
• **Identify what breaks before development:** Model edge cases, data states, cross-module dependencies  
• **Validate technical feasibility:** Align with backend teams on constraints, timelines, implementation approach  
• **Structure undefined requirements:** Create TUX tickets (design proposals) → get approval → move to TF tickets (development-ready specs)  
• **Perform rigorous UAT:** Test across 4 environments, 5 browsers, 4 platforms before each release  
• **Block releases until quality met:** Hold tickets when UX didn't match specs, when cross-browser issues appeared, when logic was broken

**The Complexity**  
This wasn't building linear flows. Every design decision cascaded across multiple surfaces:

One employer toggle could affect:  
→ Candidate status across multiple assessments  
→ Report output structure and PDF generation  
→ Shareable link visibility and access controls  
→ Historical data consistency  
→ Cross-platform behavior (web, iOS, Android)  
→ White-label branding configurations

**The Core Question**  
How do we preserve flexibility without introducing confusion, risk, or unintended consequences?

---

## MY DESIGN PRINCIPLES

These guided 505 tickets across 2.5 years:

**1. Control Over Automation**  
AI should augment, not replace, human judgment. Always provide manual override, pause capabilities, transparency into system decisions.

**2. Transparency in Complexity**  
When systems are complex, make complexity visible and understandable—not hidden. Show sync states, threshold logic, scoring criteria, configuration impact.

**3. Progressive Disclosure**  
Don't overwhelm users with all options at once. Reveal configuration depth based on user journey and technical comfort level.

**4. Guardrails, Not Gates**  
Enable power users while protecting novices. Use confirmation modals, default limits, clear warnings—but don't block capabilities.

**5. Consistency Across Chaos**  
As features expanded rapidly, maintain patterns: status indicators, action buttons, empty states, error handling, sync visibility.

---

## DEEP DIVE: AI RESUME PARSER
*Designing high-stakes automation with human control*

**The Challenge**  
A client requested automated resume screening. Founder wanted it as a scalable platform feature, not a one-off solution. The risk: over-automation could silently reject qualified candidates, creating hiring mistakes, legal liability, and client churn.

**My Design Process**

**Step 1: Structured the Complete Flow**  
I mapped the entire system before touching Figma:  
• ATS connection prerequisites and error states  
• Job selection and stage mapping logic  
• AI criteria suggestion and manual override paths  
• Score threshold configuration and automation rules  
• Batch processing controls and failure recovery  
• Candidate evaluation interface and manual actions

**Step 2: Explored Three Approaches**  

**Option 1: Fully Automatic**  
AI screens all resumes → auto-advances qualified candidates  
✗ Rejected: Too risky—removes human control for high-stakes decisions

**Option 2: Manual Review Required**  
AI extracts data → employers review every candidate  
✗ Rejected: Defeats automation purpose—doesn't save time

**Option 3: AI-Assisted with Guardrails** ✓  
AI parses and scores → employers set thresholds → manual override always available  
✓ Selected: Balanced automation with control—AI does heavy lifting, humans retain authority

**Step 3: Designed 6-Step Flow**

**1. ATS Integration Gate**  
Designed contextual empty states:  
• ATS not connected → Show integration button  
• No jobs exist → Explain requirement  
• No candidates available → Show sync status  
• Job not configured → Guide through setup  
*Why: Prevent broken flow entries. Make prerequisites explicit.*

**2. Job Selection & Stage Mapping**  
Display ATS jobs in "Not Setup" state by default. Employer selects which stage to screen from.  
*Why: Connect external pipeline with internal screening logic.*

**3. AI Criteria Suggestion**  
AI suggests 10 evaluation criteria based on role/description. Employer must select minimum 8. Option to create custom criteria.  
*Why: Balance AI assistance with recruiter judgment.*

**4. Score Threshold Configuration**  
Employer defines High/Medium/Low bands. Sets automation rules per band.  
*Why: Make automation consequences explicit. Force deliberate decision-making.*

**5. Parsing Controls**  
Default limit: 20 candidates per batch. Pause/resume capability. Sync status visibility. Manual re-sync fallback.  
*Why: Prevent bulk processing errors. Allow recovery from mistakes.*

**6. Candidate Evaluation Interface**  
Display High/Medium/Low badges, criteria-level scoring breakdown, manual action controls (Reject, Move stage, Invite).  
*Why: Transparency into AI decisions. Maintain human control.*

**Key Design Decisions**

**Confidence Score Visualization**  
Challenge: Show AI certainty without overwhelming users.  
Solution: Slider with snap points at 50%, 70%, 90%. Color-coded zones (red <50%, yellow 50-70%, green >70%).  
Trade-off: Simplified continuous scores into discrete buckets—but employers needed clear decision points, not granular precision.

**Auto-Advance Toggle**  
Challenge: Some want full automation, others want review checkpoints.  
Solution: Opt-in toggle: "Auto-advance candidates above threshold." When disabled, all candidates wait in review queue.  
Trade-off: Added configuration complexity but gave employers control for high-stakes decisions.

**Rejection Handling**  
Challenge: What happens to candidates below threshold?  
Solution: Two paths—Auto-reject (removes from ATS) or Keep for manual review. Clear warning: "Auto-rejected candidates cannot be recovered."  
Trade-off: Auto-reject is risky but desired by high-volume recruiters.

**Validation Approach**  
Since feature was under development when I left:  
• Founder demos with prospective clients (recorded feedback)  
• Internal stress-testing with sample resumes (identified edge cases)  
• Developer review of technical feasibility (confirmed ATS integrations)

---

## DEEP DIVE: REPORTING AS A PRODUCT
*Structuring complex psychometric data into clear, actionable insights*

**The Problem I Identified**  
Employers needed to evaluate candidates quickly, but our reporting was fragmented:  
• Basic reports lacked depth  
• Psychometric reports weren't branded or had UI inconsistencies  
• No unified export—users downloaded multiple PDFs per candidate  
• Inconsistent visual language across report types  
• Some reports had structural issues that made data hard to interpret

**My Design Approach**

**Explored Three Directions**  

**Option 1: Basic Template Redesign**  
Clean up existing reports; keep separate PDFs.  
✗ Rejected: Quick fix but doesn't solve fragmentation or structural issues.

**Option 2: Unified Report Builder**  
Let employers customize sections, choose tests, design layouts.  
✗ Rejected: Too complex for most users—over-engineered.

**Option 3: Curated Report System** ✓  
Design new reports from scratch where needed; fix and improve existing reports; build smart export.  
✓ Selected: Professional output through structured data presentation without configuration overhead.

**What I Designed**

**1. Three New Psychometric Reports (From Scratch)**  
I designed these reports from the ground up—understanding assessment requirements, structuring how each data type should be presented, and creating interactive PDF formats:

• **Sales Profiler Report:** Structured sales-specific competencies, behavioral indicators, performance predictors  
• **PicOcean Personality & Cultural Fit:** Designed data presentation for personality traits mapped to cultural alignment  
• **360 Degree Feedback Report:** Created comprehensive feedback visualization from multiple evaluators (peers, managers, self-assessment)

Each required: Understanding raw assessment data → Structuring information hierarchy → Designing visual representations → Creating actionable insights format

**2. Seven Report Improvements (UI Fixes & Enhancements)**  
For existing reports, I identified issues and improved UI/structure:

• **Big Five Personality:** Fixed layout issues, improved trait visualization  
• **16 PF (16 Personality Factors):** Enhanced data hierarchy, clarified factor relationships  
• **Leadership Assessment:** Restructured competency display, improved scoring clarity  
• **SMART Personality:** Fixed UI inconsistencies, improved readability  
• **DISC Personality:** Enhanced 4-quadrant visualization, improved behavioral descriptions  
• **Enneagram:** Fixed structural issues, improved type descriptions and score display  
• **Motivational Traits:** Restructured data presentation, improved actionability

**My Core Contribution:**  
Understanding assessment requirements → Structuring complex data into clear formats → Designing interactive, readable PDFs that translate raw scores into hiring insights

**3. Export Architecture**  
Designed one-click ZIP download system:  
• All candidate reports bundled automatically  
• Smart naming (candidate name + test type)  
• Intelligent bundling (only completed tests included)

**Impact**  
• Designed **3 reports from scratch**, improved **7 existing reports** (10 total psychometric reports)  
• Reduced time-to-decision by consolidating fragmented reports  
• Eliminated manual PDF collection (one-click vs. 5-10 separate downloads)  
• Professional output improved perceived platform quality  
• Clear data structure made complex psychometric insights accessible to non-specialist HR teams  
• Psychometric reports became sales demo differentiator

---

## OTHER MAJOR CONTRIBUTIONS

**Test Library Visibility System**  
**Problem:** Employers browse 3,000+ pre-created tests—needed clarity on structure before adding to assessments.  
**What I Designed:** Expandable preview showing question types, time estimates, difficulty levels. Designed empty states, loading states, error states.  
**Impact:** Reduced "wrong test added" support tickets.

**Enterprise Infrastructure (SAML SSO, Billing, Email Config)**  
**Problem:** Enterprise clients needed complex technical configurations accessible to non-technical HR teams.  
**What I Designed:** SSO configuration flows, usage-based billing dashboards, custom email domain setup, admin role management.  
**Impact:** Enabled enterprise sales without requiring technical support.

**Cross-Platform Bug Identification**  
**My Process:** Validated every feature across:  
• **5 browsers:** Chrome, Safari, Edge, Firefox, mobile browsers  
• **4 platforms:** Windows, macOS, iOS, Android  
• **3 viewports:** Desktop, tablet, mobile  
**What I Found:** Video recording issues on iOS Safari, dropdown rendering bugs in Firefox, mobile keyboard overlap issues, cross-browser permission handling inconsistencies.  
**Outcome:** Of 498 issues I reported, significant portion were cross-platform bugs caught before user impact.

---

## OPERATING AT SCALE

**Managing 505 UX-Tracked Tickets**  
This wasn't just execution—it was system stewardship:  
• Created TUX tickets (design proposals) with structured requirements  
• Validated feasibility with backend teams before dev handoff  
• Performed UAT across 4 environments per release  
• Identified cross-browser issues before production  
• Blocked releases when quality didn't meet standards  
• Documented design decisions for team alignment

**Real-Time Request Management**  
Sales, marketing, CS teams posted client requests on Slack:  
• Monitored channel, took ownership of design-relevant requests  
• Assessed technical feasibility and business impact  
• Created Jira tickets with defined scope  
• Designed solutions, validated with founders  
• Coordinated with dev through QA, informed stakeholders  
• Some requests rejected due to technical constraints—learned to push back constructively

**Proactive Bug Reporting (498 Issues Reported)**  
Beyond assigned features, I actively identified:  
• UI/UX bugs across employer and candidate portals  
• Cross-browser rendering inconsistencies  
• Mobile viewport issues  
• Edge case behaviors  
• Accessibility gaps  
Created tickets, defined fixes, ensured resolution—contributed to platform stability.

**Supporting Junior Designers**  
Mentored 2 designers with <2 years experience:  
• Reviewed complex workflows before dev handoff  
• Helped structure ambiguous requirements  
• Maintained pattern consistency  
• Validated logic and edge case handling

**Context Switching**  
Juggled simultaneously:  
• Strategic epics (multi-week initiatives like Resume Parser)  
• Daily feature requests (Slack-to-Jira pipeline)  
• Bug fixes (interrupt-driven work)  
• Design system maintenance (pattern consistency)  
• Cross-platform validation (browser/OS testing)

---

## DESIGN SYSTEM WORK

**Pattern Maintenance Across 505 Tickets**  
As platform expanded, I maintained consistency:  
• Status indicators (consistent color coding, iconography)  
• Empty states (contextual messaging, clear CTAs)  
• Error handling (user-friendly messages, recovery paths)  
• Action buttons (primary, secondary, destructive patterns)  
• Form validation (inline errors, success states)  
• Loading states (skeletons, spinners, progress indicators)

**Cross-Module Consistency**  
Ensured patterns worked across:  
• Employer Portal (complex workflows)  
• Candidate Portal (simple, guided flows)  
• Mobile apps (touch-friendly, reduced density)  
• White-label environments (theme flexibility)

---

## IMPACT

**Delivery Metrics**  
• **505 UX-tracked tickets** delivered over 2.5 years  
• **498 issues reported** (proactive quality management)  
• **130 resolved recently** (active delivery velocity)  
• **122 created recently** (pipeline management)  
• Validated across **4 environments**, **5 browsers**, **4 platforms**

**Platform Impact**  
• Designed for platform serving **4,500+ job roles** across **50+ industries**  
• Work supported **100+ ATS integrations**  
• Platform achieved **80% candidate completion rate** (2-3x industry average)  
• Companies reported **82% reduction in time-to-hire**

**Process Improvements**  
• Established Slack-to-Jira request management workflow  
• Created structured UAT process across 4 environments  
• Implemented cross-browser validation protocol  
• Built design review process for junior designers  
• Documented pattern library for team alignment

**Quality Contributions**  
• Caught critical cross-platform bugs before production  
• Identified logic gaps in ambiguous requirements  
• Prevented automation risks through guardrail design  
• Maintained system coherence during rapid expansion

---

## WHAT I LEARNED

**1. Translating Ambiguity Into Structure**  
Most features started vague: "Build something like competitor X." I learned to:  
• Ask clarifying questions before designing  
• Model edge cases and failure states  
• Document assumptions and validate with stakeholders  
• Structure undefined requirements into actionable specs

**2. Designing for Cascading Dependencies**  
In complex B2B systems, nothing exists in isolation:  
• One toggle affects multiple surfaces  
• Configuration changes impact historical data  
• Cross-platform behavior requires validation  
I learned to map dependencies before designing solutions.

**3. Balancing Speed With Safety**  
Revenue-driven prioritization meant shipping under constraints:  
• Sometimes shipped knowing future polish was needed  
• Documented design debt for future refinement  
• Balanced urgency with minimum viable quality  
• Learned when to push back vs. when to adapt

**4. Proactive Quality Management**  
498 reported issues weren't just bugs found during QA:  
• Proactively tested across browsers and platforms  
• Identified edge cases before they reached users  
• Caught cross-module inconsistencies  
• Prevented downstream problems through validation

**5. Systems Thinking at Scale**  
505 tickets required deep systems thinking:  
• Every decision had cascading effects  
• Patterns needed to scale across surfaces  
• Consistency maintained through documentation  
• Team alignment through clear communication

---

## REFLECTION

Testlify wasn't about designing beautiful screens. It was about **building structure in ambiguity**—where requirements were unclear, timelines were tight, and mistakes had real business consequences.

I evolved from:  
**Feature Execution** → **System Stewardship** → **Risk Reduction** → **Team Multiplier**

**What This Experience Taught Me:**  
• Senior product design means structuring what the product should do when no one else has defined it  
• Great design isn't about individual features—it's about systems that work consistently at scale  
• Quality comes from proactive validation, not just responding to found bugs  
• Team impact extends beyond individual tickets into overall system coherence

**What I Bring to My Next Role:**  
• Proven ability to translate ambiguity into structured, scalable systems  
• Track record of delivering 505 tickets while maintaining quality  
• Deep systems thinking that prevents downstream problems  
• Proactive quality management (498 reported issues)  
• Cross-functional collaboration in fast-moving environments  
• Mentorship capability for growing design teams

The platform served real hiring teams making real decisions about real people's careers. Every design choice carried weight. I'm proud of building scalable structure in genuine operational complexity—and I'm ready to bring that capability to a senior product design role.
