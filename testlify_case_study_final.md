
# TESTLIFY: DESIGNING AN AI-POWERED HIRING PLATFORM AT SCALE

**Role:** Product Designer  
**Duration:** June 2023 – January 2026 (2.5 years)  
**Platform:** AI-native skill assessments & interviewing tool

**Impact:**  
• 229 Jira tickets delivered (193 tasks, 12 epics, 10 improvements)  
• 111 features shipped to production across 3 core surfaces  
• Platform serves 4,500+ job roles across 50+ industries  
• 80% candidate completion rate (2-3x industry average)

---

## AT A GLANCE

**What is Testlify?**  
An AI-powered assessment platform that helps companies evaluate candidates through skill tests, psychometric assessments, and conversational AI interviews. The platform includes 3,000+ pre-created tests, supports 45+ coding languages, and integrates with 100+ ATS systems.

**My Role**  
I was the design lead responsible for end-to-end product design across three core surfaces: Employer Portal (assessment creation, test management, reporting), Candidate Test Portal (test-taking experience), and AI Interview System (chat, video, audio simulations). I owned the complete design process from discovery through delivery, collaborated directly with founders on product strategy, and supported two junior designers.

**Scope & Scale**  
Over 2.5 years, I delivered 229 Jira tickets comprising feature development, enhancements, client requests, and bug fixes. This included 12 strategic epics (multi-feature initiatives), 80 enhancement requests, and 21 client-driven improvements. I also managed real-time design requests from sales, marketing, and customer success teams via Slack, where I'd assess feasibility, create tickets, scope solutions, and see them through to delivery.

---

## THE CHALLENGE

Testlify operates in a high-stakes environment where every design decision directly impacts hiring outcomes. A confusing interface could cost someone a job opportunity. A poorly designed test flow could lead to candidate drop-off. An unclear reporting system could result in wrong hiring decisions.

**The complexity came from three sources:**

**1. Multiple User Contexts**  
Employers ranged from solo recruiters creating their first assessment to enterprise HR teams managing hundreds of candidates across different roles. Candidates varied from tech professionals taking coding tests to entry-level applicants completing personality assessments. Each group had different needs, technical literacy, and expectations.

**2. AI & Automation Complexity**  
The platform introduced AI-powered features like resume parsing and conversational interviews. These created new design challenges: How do we show AI confidence scores? What happens when AI parsing fails? How do we let employers override AI decisions? These weren't just interface problems—they were trust problems.

**3. Cascading Dependencies**  
Changes to question types affected test creation, candidate experience, scoring logic, and report generation simultaneously. A single design decision could cascade across multiple surfaces, requiring careful coordination with backend teams and consideration of edge cases.

---

## MY APPROACH

I structured my work across two layers that operated simultaneously:

**Strategic Layer – Product Thinking**  
I partnered with founders to shape product direction, conducted user research to validate assumptions, designed solutions that balanced business needs with user experience, and created design systems to maintain consistency at scale.

**Execution Layer – Delivery at Velocity**  
I designed 229 tickets across features, enhancements, and fixes, managed real-time requests from sales/CS/marketing via Slack (assessing feasibility, creating tickets, defining scope, delivering solutions), proactively identified and resolved UI/UX bugs, and maintained quality through rapid iteration cycles.

**Request Management Process**  
When teams posted requests on Slack, I'd take ownership, understand the business need, create a Jira ticket with clear scope, propose design solutions, validate with founders, coordinate with dev teams through QA, and inform stakeholders of outcomes. Some requests were rejected due to technical constraints or business priorities—I learned to push back constructively while maintaining team relationships.

**Reality Check**  
I operated without a dedicated design manager or senior reviewer. To maintain quality, I used AI tools to stress-test logic and simulate edge cases, collaborated closely with developers to validate technical feasibility, and learned to balance speed with craft under revenue-driven prioritization.

---

## DESIGN PRINCIPLES

These principles guided every decision across 229 tickets:

**1. Control Over Automation**  
AI should augment, not replace, human judgment. Employers always have final say over AI recommendations.

**2. Transparency in Complexity**  
When systems make decisions (AI scoring, test logic, candidate filtering), show users why and how.

**3. Progressive Disclosure**  
Reveal complexity gradually. Show essential information first, advanced controls on demand.

**4. Guardrails, Not Gates**  
Prevent errors through smart defaults and validation, not by blocking user actions.

**5. Consistency Across Chaos**  
With 229 tickets spanning multiple surfaces, maintaining pattern consistency was non-negotiable.

---

## DEEP DIVE: AI RESUME PARSER

**The Ask**  
Build an AI-powered system that automatically screens resumes, extracts candidate information, matches qualifications to job requirements, and feeds qualified candidates into assessment workflows—reducing time-to-hire for companies processing hundreds of applications.

**The Risk**  
AI making high-stakes hiring decisions without employer oversight could lead to qualified candidates being rejected, bias creeping into automated screening, and loss of trust if the system felt like a "black box."

**Design Exploration: Three Approaches**

**Option 1: Fully Automatic**  
AI screens all resumes and auto-advances candidates to assessments.  
✗ Trade-off: Fast but removes human control—too risky for hiring decisions.

**Option 2: Manual Review Required**  
AI extracts data; employers review every candidate before advancing.  
✗ Trade-off: Safe but defeats the purpose of automation—doesn't save time.

**Option 3: AI-Assisted with Guardrails** ✓  
AI parses and scores resumes; employers set acceptance thresholds and can review/override any decision.  
✓ Chosen because: Balanced automation with control—AI does heavy lifting, humans retain final authority.

**Complete Flow (6 Steps)**  
1. **ATS Integration**: Connect to 100+ ATS platforms (Greenhouse, Lever, Workable)  
2. **Job Stage Selection**: Choose which ATS stage to screen (e.g., "Resume Review")  
3. **Screening Rules**: Set resume parsing criteria (skills, experience, education)  
4. **Threshold Configuration**: Define cut-off scores (e.g., 70% match = auto-advance)  
5. **Batch Processing**: AI screens up to 500 resumes per run  
6. **Review & Override**: Employers see AI decisions, can manually approve/reject

**Key Design Decisions**

**Decision 1: Confidence Score Visualization**  
Challenge: How do we show AI's "certainty" without overwhelming users?  
Solution: Used a slider with snap points at 50%, 70%, 90% and color-coded zones (red <50%, yellow 50-70%, green >70%). This made abstract confidence scores tangible and actionable.  
Trade-off: Simplified continuous scores into discrete buckets—acceptable because employers needed clear decision points, not granular precision.

**Decision 2: Auto-Advance Toggle**  
Challenge: Some employers want full automation; others want review checkpoints.  
Solution: Created an opt-in toggle: "Auto-advance candidates above threshold." When disabled, all candidates wait in a review queue.  
Trade-off: Added configuration complexity but gave employers the control they needed for high-stakes decisions.

**Decision 3: Rejection Handling**  
Challenge: What happens to candidates below the threshold?  
Solution: Two paths: Auto-reject (removes from ATS) or Keep for manual review (candidate stays in system).  
Trade-off: Auto-reject is risky but desired by high-volume recruiters. We added a clear warning: "Auto-rejected candidates cannot be recovered."

**Decision 4: ATS Stage Mapping**  
Challenge: Every ATS uses different stage names ("Screening" vs "Resume Review" vs "Initial Review").  
Solution: Dynamic dropdown populated from connected ATS's actual stage names—no guessing.  
Trade-off: Required complex backend integration but eliminated user confusion.

**Validation Approach**  
Since this feature was under development when I left, we validated through: Founder demos with prospective clients (recorded feedback on trust, control, clarity), Internal stress-testing with sample resumes (identified edge cases like PDFs with non-standard formatting), and Developer review of technical feasibility (confirmed ATS integrations were possible).

**Expected Impact**  
• Reduce time-to-hire by automating initial resume screening  
• Process 500+ resumes in minutes vs. hours of manual review  
• Maintain employer control through configurable thresholds and override capabilities  
• Provide transparency into AI decision-making via confidence scores

---

## DEEP DIVE: REPORTING AS A PRODUCT

**The Problem**  
Employers needed to evaluate candidates quickly, but our reporting system was fragmented: basic reports lacked depth, psychometric reports (DISC, personality) weren't customized to Testlify's brand, and there was no unified export system—users had to download multiple PDFs per candidate.

**Design Exploration: Three Approaches**

**Option 1: Basic Template Redesign**  
Clean up existing reports; keep separate PDFs per test type.  
✗ Trade-off: Quick fix but doesn't solve fragmentation or customization needs.

**Option 2: Unified Report Builder**  
Let employers customize report sections, choose which tests to include, design their own layouts.  
✗ Trade-off: Powerful but too complex for most users—over-engineered.

**Option 3: Curated Report System** ✓  
Redesign core reports with Testlify branding; create 8 standardized psychometric PDFs; build smart export (one-click download of all candidate reports).  
✓ Chosen because: Balanced quality with usability—professional output without configuration overhead.

**What I Designed**

**1. Core Report Redesign**  
Rebuilt the primary assessment report with: Visual scoring system (color-coded performance indicators), Test-by-test breakdowns (skill tests, psychometric, coding, AI interviews), Candidate timeline (time spent per question, completion patterns), and Comparison view (candidate vs. job requirements).

**2. 8 Psychometric PDFs**  
Created branded report templates for: DISC personality (4-quadrant behavioral analysis), Big Five traits (detailed personality dimensions), Work style assessments, Communication preferences, Leadership potential, Team dynamics, and Problem-solving approaches.  
Each report included visual data representations (charts, graphs), narrative interpretations (plain-language explanations), and actionable insights (hiring recommendations).

**3. Export Architecture**  
Designed a one-click export system: Single button downloads all candidate reports as a ZIP file, Reports auto-named with candidate name and test type (e.g., "John_Doe_DISC_Assessment.pdf"), and Smart bundling (only includes completed tests, skips incomplete ones).

**Impact**  
• Reduced employer time-to-decision by consolidating fragmented reports  
• Eliminated manual PDF collection—one-click export vs. downloading 5-10 separate files  
• Professional, branded output improved perceived platform quality  
• Psychometric reports became a competitive differentiator in sales demos

---

## OTHER KEY CONTRIBUTIONS

**Decision Visibility in Test Libraries**  
When employers browse 3,000+ pre-created tests, they needed clarity on test structure before adding to assessments. Designed an expandable preview showing question types, time estimates, and difficulty levels—reduced "wrong test added" support tickets.

**Enterprise Infrastructure (SAML SSO, Billing, Email Config)**  
For enterprise clients, designed configuration interfaces for single sign-on, usage-based billing dashboards, custom email domains, and admin role management. Made complex technical features accessible to non-technical HR teams.

**Marketing Alignment**  
Collaborated with marketing to ensure platform UI matched website messaging. Updated terminology, redesigned onboarding flows, and created promotional banners—resulted in cohesive brand experience from first click to daily use.

**Cross-Platform Validation**  
Ensured design consistency across Employer Portal, Candidate Portal, and mobile experiences. Caught platform-specific bugs (e.g., video recording issues on iOS Safari) and pushed fixes before user impact.

---

## OPERATING AT SCALE

**Managing Incoming Requests**  
Sales, marketing, and customer success teams posted client requests on Slack. I monitored the channel, took ownership of relevant requests, assessed technical feasibility, created Jira tickets with defined scope, designed solutions, validated with founders, coordinated with dev through QA, and informed stakeholders of outcomes (including rejections when technically infeasible).

**Balancing Speed & Safety**  
With 229 tickets over 2.5 years, velocity mattered—but not at the expense of quality. I developed rapid validation techniques (AI stress-testing for edge cases, developer collaboration on technical constraints) and prioritized ruthlessly (focused on high-impact work, deferred low-value requests). Revenue-driven prioritization sometimes meant pausing strategic work for urgent client needs—I learned to adapt without compromising core UX principles.

**Bug Identification & Resolution**  
Beyond feature work, I proactively identified UI/UX bugs reported by clients, internal teams, and through my own QA. Created tickets, defined fixes, and ensured resolution—contributed to platform stability and user trust.

**Supporting Junior Designers**  
Mentored two junior designers, reviewed their work, provided feedback on interaction patterns and visual hierarchy, and helped them navigate ambiguous requirements. This wasn't formal management, but I invested in their growth because it improved overall team output.

**Context Switching**  
Juggled multiple projects simultaneously: strategic epics (multi-week initiatives like Resume Parser), daily feature requests (Slack-to-Jira pipeline), bug fixes (interrupt-driven work), and design system maintenance (ensuring pattern consistency). Learned to prioritize based on business impact, not personal preference.

---

## IMPACT

**Delivery & Scale**  
• 229 Jira tickets delivered (193 tasks, 12 strategic epics, 10 improvements, 6 bugs, 5 new features)  
• 111 features shipped to production across 3 core surfaces  
• 61 designs passed to development (validated, documented, ready for build)  
• 80 enhancement requests executed (improving existing features)  
• 21 client-driven improvements delivered (direct customer needs addressed)

**User Evidence**  
• Customer success team reported faster client onboarding after Resume Parser demos  
• Internal team feedback: "The new reporting system cut candidate review time in half"  
• Founder validation: "Prashant's designs became our competitive advantage in sales pitches"  
• Platform achieved 80% candidate completion rate—2-3x better than typical assessment tools  

**Platform Growth**  
• Designed for platform serving 4,500+ job roles across 50+ industries  
• Work supported 100+ ATS integrations  
• Platform processed thousands of assessments daily at peak  
• Companies reported 82% reduction in time-to-hire (platform-wide metric)

**Process Improvements**  
• Established Slack-to-Jira request management process (reduced dropped requests)  
• Created design system documentation (improved consistency across 229 tickets)  
• Introduced AI validation techniques (caught edge cases before development)  
• Built cross-functional collaboration rhythms (reduced back-and-forth with dev)

---

## WHAT I LEARNED

**1. Designing in Ambiguity**  
Early-stage startups don't have playbooks. I learned to validate assumptions through rapid prototyping, make decisions with incomplete data, and adapt when direction changed. The Resume Parser project taught me to balance visionary thinking with practical constraints.

**2. Systems Thinking at Scale**  
229 tickets sounds like task execution, but it required deep systems thinking. Every design decision had cascading effects across surfaces, user types, and technical architecture. I learned to map dependencies before designing, anticipate edge cases, and collaborate closely with backend teams.

**3. Strategic Partnership Over Service Design**  
I evolved from "designer who makes things look good" to "design partner who shapes product direction." Founders trusted me to challenge requirements, propose alternatives, and push back when user needs conflicted with business wants. This required building credibility through consistent delivery.

**4. Balancing Trade-offs, Not Finding Perfect Solutions**  
AI automation vs. human control. Speed vs. thoroughness. Simplicity vs. power. Every project involved trade-offs. I learned to frame design decisions around "what we're optimizing for" rather than "what's the right answer." The Resume Parser's three-option exploration exemplified this—no perfect solution, just the best fit for context.

**5. Quality at Velocity**  
Shipping 229 tickets in 2.5 years while maintaining design quality required ruthless efficiency: Reusable components over bespoke solutions, documented patterns for team alignment, AI tools for validation at speed, and clear communication to reduce revision cycles. I learned that velocity comes from smart systems, not just working faster.

---

## REFLECTION

When I joined Testlify, I saw it as a feature execution role—take requirements, make them pretty, ship fast. By the time I left, I'd become a strategic design partner who shaped product direction, influenced roadmap priorities, and built systems that scaled beyond individual projects.

The journey from 229 Jira tickets to a cohesive product experience taught me that great design isn't about making individual features beautiful—it's about building systems that work consistently at scale. It's about making complex decisions transparent. It's about earning trust through delivery. And it's about balancing visionary thinking with the reality of startup constraints.

If I could go back, I'd push for dedicated user research earlier (we relied too heavily on founder intuition), document edge cases more rigorously (would've prevented some late-cycle bugs), and invest in design system infrastructure sooner (consistency suffered under velocity pressure). But I wouldn't change the experience of learning to design in ambiguity, ship at speed, and partner strategically with leadership.

That's the designer I became at Testlify—and the designer I bring to my next role.
