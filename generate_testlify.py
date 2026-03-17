import codecs

file_path = r"c:\Users\prash\.gemini\antigravity\scratch\portfolio\case-studies\testlify.html"

# Read original to get prefix and suffix
with codecs.open(file_path, "r", "utf-8") as f:
    text = f.read()

prefix = text[:text.find('<main class="case-detail">')]
suffix = text[text.rfind('<!-- ── Footer ── -->'):]

new_main = """<main class="case-detail">
        <div class="container">

            <!-- Hero -->
            <div class="case-detail__hero reveal">
                <div class="case-detail__hero-meta">
                    <div class="case-detail__hero-line"></div>
                    <span class="case-detail__project">Testlify</span>
                    <span class="case-detail__dot">·</span>
                    <span class="case-detail__domain">AI-native skill assessments & interviewing tool</span>
                    <div class="case-detail__hero-line"></div>
                </div>
                <h1 class="case-detail__title">Designing an AI-Powered Hiring Platform at Scale</h1>
                <p style="color: var(--text-secondary); font-size: var(--font-size-md); margin-bottom: var(--space-md); text-align: center; max-width: 700px; margin-left: auto; margin-right: auto;">
                    Role: Product Designer | Duration: June 2023 – January 2026 (1.5 years)
                </p>
                <div class="case-detail__hero-image">
                    <div class="laptop-frame">
                        <div class="laptop-frame__browser-bar">
                            <span class="laptop-frame__dot laptop-frame__dot--red"></span>
                            <span class="laptop-frame__dot laptop-frame__dot--yellow"></span>
                            <span class="laptop-frame__dot laptop-frame__dot--green"></span>
                            <span class="laptop-frame__url">testlify.com</span>
                        </div>
                        <div class="laptop-frame__content" style="background-image: url('../img/case-studies/testlify-hero.png');">
                            <img src="../img/case-studies/testlify-hero.png" alt="Testlify Platform Overview">
                        </div>
                        <div class="laptop-frame__base"></div>
                    </div>
                </div>
            </div>

            <section class="case-section reveal">
                <div class="at-a-glance">
                    <div class="at-a-glance__row">
                        <div class="at-a-glance__label">Impact</div>
                        <div class="at-a-glance__value">
                            <ul class="case-carousel__list list--single" style="margin-top: 0; margin-bottom: 0;">
                                <li><strong>229 Jira tickets delivered</strong> (193 tasks, 12 epics, 10 improvements)</li>
                                <li><strong>111 features shipped</strong> to production across 3 core surfaces</li>
                                <li>Platform serves <strong>4,500+ job roles</strong> across 50+ industries</li>
                                <li><strong>80% candidate completion rate</strong> (2-3x industry average)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- At a Glance -->
            <section class="case-section reveal">
                <h2 class="case-section__title">At a Glance</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">What is Testlify?</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">An AI-powered assessment platform that helps companies evaluate candidates through skill tests, psychometric assessments, and conversational AI interviews. The platform includes 3,000+ pre-created tests, supports 45+ coding languages, and integrates with 100+ ATS systems.</p>
                    </div>

                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">My Role</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">I was the design lead responsible for end-to-end product design across three core surfaces: Employer Portal (assessment creation, test management, reporting), Candidate Test Portal (test-taking experience), and AI Interview System (chat, video, audio simulations). I owned the complete design process from discovery through delivery, collaborated directly with founders on product strategy, and supported two junior designers.</p>
                    </div>

                    <div class="contribution-card">
                        <h3 class="contribution-card__title">Scope & Scale</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Over 1.5 years, I delivered 229 Jira tickets comprising feature development, enhancements, client requests, and bug fixes. This included 12 strategic epics (multi-feature initiatives), 80 enhancement requests, and 21 client-driven improvements. I also managed real-time design requests from sales, marketing, and customer success teams via Slack, where I'd assess feasibility, create tickets, scope solutions, and see them through to delivery.</p>
                    </div>
                </div>
            </section>

            <!-- The Challenge -->
            <section class="case-section reveal">
                <h2 class="case-section__title">The Challenge</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <p style="margin-bottom: var(--space-md);">Testlify operates in a high-stakes environment where every design decision directly impacts hiring outcomes. A confusing interface could cost someone a job opportunity. A poorly designed test flow could lead to candidate drop-off. An unclear reporting system could result in wrong hiring decisions.</p>
                    
                    <strong style="color: var(--text-primary); display:block; margin: var(--space-lg) 0 var(--space-md);">The complexity came from three sources:</strong>

                    <div class="t-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-md);">
                        <div class="option-card" style="margin: 0; display: flex; flex-direction: column;">
                            <h4 style="color: var(--accent); margin-bottom: 8px;">1. Multiple User Contexts</h4>
                            <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 0;">Employers ranged from solo recruiters creating their first assessment to enterprise HR teams managing hundreds of candidates across different roles. Candidates varied from tech professionals taking coding tests to entry-level applicants completing personality assessments. Each group had different needs, technical literacy, and expectations.</p>
                        </div>
                        <div class="option-card" style="margin: 0; display: flex; flex-direction: column;">
                            <h4 style="color: var(--accent); margin-bottom: 8px;">2. AI &amp; Automation Complexity</h4>
                            <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 0;">The platform introduced AI-powered features like resume parsing and conversational interviews. These created new design challenges: How do we show AI confidence scores? What happens when AI parsing fails? How do we let employers override AI decisions? These weren't just interface problems—they were trust problems.</p>
                        </div>
                        <div class="option-card" style="margin: 0; display: flex; flex-direction: column;">
                            <h4 style="color: var(--accent); margin-bottom: 8px;">3. Cascading Dependencies</h4>
                            <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 0;">Changes to question types affected test creation, candidate experience, scoring logic, and report generation simultaneously. A single design decision could cascade across multiple surfaces, requiring careful coordination with backend teams and consideration of edge cases.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- My Approach -->
            <section class="case-section reveal">
                <h2 class="case-section__title">My Approach</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <p style="margin-bottom: var(--space-md);">I structured my work across two layers that operated simultaneously:</p>

                    <div class="impact-list" style="margin-bottom: var(--space-lg); background: var(--bg-card); border: 1px solid var(--border-card); padding: var(--space-lg); border-radius: var(--radius-md);">
                        <div class="impact-list__item" style="align-items:flex-start; margin-bottom: 1rem;">
                            <span class="impact-list__icon" style="color: var(--accent);">Target</span>
                            <div>
                                <strong style="color: var(--text-primary); display: block; margin-bottom: 4px;">Strategic Layer – Product Thinking</strong>
                                <span style="color: var(--text-secondary); font-size: 0.9em; line-height: 1.5;">I partnered with founders to shape product direction, conducted user research to validate assumptions, designed solutions that balanced business needs with user experience, and created design systems to maintain consistency at scale.</span>
                            </div>
                        </div>
                        <div class="impact-list__item" style="align-items:flex-start;">
                            <span class="impact-list__icon" style="color: var(--accent);">Target</span>
                            <div>
                                <strong style="color: var(--text-primary); display: block; margin-bottom: 4px;">Execution Layer – Delivery at Velocity</strong>
                                <span style="color: var(--text-secondary); font-size: 0.9em; line-height: 1.5;">I designed 229 tickets across features, enhancements, and fixes, managed real-time requests from sales/CS/marketing via Slack (assessing feasibility, creating tickets, defining scope, delivering solutions), proactively identified and resolved UI/UX bugs, and maintained quality through rapid iteration cycles.</span>
                            </div>
                        </div>
                    </div>

                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">Request Management Process</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">When teams posted requests on Slack, I'd take ownership, understand the business need, create a Jira ticket with clear scope, propose design solutions, validate with founders, coordinate with dev teams through QA, and inform stakeholders of outcomes. Some requests were rejected due to technical constraints or business priorities—I learned to push back constructively while maintaining team relationships.</p>
                    </div>

                    <div class="contribution-card">
                        <h3 class="contribution-card__title">Reality Check</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">I operated without a dedicated design manager or senior reviewer. To maintain quality, I used AI tools to stress-test logic and simulate edge cases, collaborated closely with developers to validate technical feasibility, and learned to balance speed with craft under revenue-driven prioritization.</p>
                    </div>
                </div>
            </section>

            <!-- Design Principles -->
            <section class="case-section reveal">
                <h2 class="case-section__title">Design Principles</h2>
                <p style="color: var(--text-secondary); margin-bottom: var(--space-md);">These principles guided every decision across 229 tickets:</p>
                <div class="client-vision-grid" style="grid-template-columns: 1fr;">
                    <div class="client-vision-stat" style="padding: 1.5rem;">
                        <div class="client-vision-stat__value" style="font-size: 1.15rem; font-weight: 600; font-family: var(--font-family-base); color: var(--text-primary);">1. Control Over Automation</div>
                        <div class="client-vision-stat__label" style="font-size: 0.9rem; color: var(--text-secondary);">AI should augment, not replace, human judgment. Employers always have final say over AI recommendations.</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1.5rem;">
                        <div class="client-vision-stat__value" style="font-size: 1.15rem; font-weight: 600; font-family: var(--font-family-base); color: var(--text-primary);">2. Transparency in Complexity</div>
                        <div class="client-vision-stat__label" style="font-size: 0.9rem; color: var(--text-secondary);">When systems make decisions (AI scoring, test logic, candidate filtering), show users why and how.</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1.5rem;">
                        <div class="client-vision-stat__value" style="font-size: 1.15rem; font-weight: 600; font-family: var(--font-family-base); color: var(--text-primary);">3. Progressive Disclosure</div>
                        <div class="client-vision-stat__label" style="font-size: 0.9rem; color: var(--text-secondary);">Reveal complexity gradually. Show essential information first, advanced controls on demand.</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1.5rem;">
                        <div class="client-vision-stat__value" style="font-size: 1.15rem; font-weight: 600; font-family: var(--font-family-base); color: var(--text-primary);">4. Guardrails, Not Gates</div>
                        <div class="client-vision-stat__label" style="font-size: 0.9rem; color: var(--text-secondary);">Prevent errors through smart defaults and validation, not by blocking user actions.</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1.5rem;">
                        <div class="client-vision-stat__value" style="font-size: 1.15rem; font-weight: 600; font-family: var(--font-family-base); color: var(--text-primary);">5. Consistency Across Chaos</div>
                        <div class="client-vision-stat__label" style="font-size: 0.9rem; color: var(--text-secondary);">With 229 tickets spanning multiple surfaces, maintaining pattern consistency was non-negotiable.</div>
                    </div>
                </div>
            </section>

            <!-- DEEP DIVE: AI Resume Parser -->
            <section class="lifecycle-section reveal">
                <div class="section-heading" style="margin-bottom: var(--space-xl);">
                    <div class="section-heading__line"></div>
                    <h2 class="section-heading__text">Deep Dive: AI Resume Parser</h2>
                    <div class="section-heading__line"></div>
                </div>

                <div class="case-section__content" style="max-width: 100%; margin-bottom: var(--space-xl);">
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">The Ask</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Build an AI-powered system that automatically screens resumes, extracts candidate information, matches qualifications to job requirements, and feeds qualified candidates into assessment workflows—reducing time-to-hire for companies processing hundreds of applications.</p>
                    </div>
                    <div class="contribution-card">
                        <h3 class="contribution-card__title">The Risk</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">AI making high-stakes hiring decisions without employer oversight could lead to qualified candidates being rejected, bias creeping into automated screening, and loss of trust if the system felt like a "black box."</p>
                    </div>
                </div>

                <h3 style="color: var(--text-primary); font-size: var(--font-size-lg); margin-bottom: var(--space-md);">Design Exploration: Three Approaches</h3>
                <div class="option-grid">
                    <div class="option-card">
                        <h4 style="color: var(--text-primary); margin-bottom: 8px;">Option 1: Fully Automatic</h4>
                        <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 12px;">AI screens all resumes and auto-advances candidates to assessments.</p>
                        <p style="font-size: var(--font-size-xs); color: #ff6b6b;"><strong style="font-weight: 600;">✗ Trade-off:</strong> Fast but removes human control—too risky for hiring decisions.</p>
                    </div>
                    <div class="option-card">
                        <h4 style="color: var(--text-primary); margin-bottom: 8px;">Option 2: Manual Review Required</h4>
                        <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 12px;">AI extracts data; employers review every candidate before advancing.</p>
                        <p style="font-size: var(--font-size-xs); color: #ff6b6b;"><strong style="font-weight: 600;">✗ Trade-off:</strong> Safe but defeats the purpose of automation—doesn't save time.</p>
                    </div>
                    <div class="option-card option-card--selected">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <h4 style="color: var(--accent); margin: 0;">Option 3: AI-Assisted with Guardrails</h4>
                            <span style="font-size: 10px; background: var(--accent); color: #000; padding: 2px 6px; border-radius: 4px; font-weight: bold;">CHOSEN</span>
                        </div>
                        <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 12px;">AI parses and scores resumes; employers set acceptance thresholds and can review/override any decision.</p>
                        <p style="font-size: var(--font-size-xs); color: var(--accent);"><strong style="font-weight: 600;">✓ Chosen because:</strong> Balanced automation with control—AI does heavy lifting, humans retain final authority.</p>
                    </div>
                </div>

                <h3 style="color: var(--text-primary); margin-top: var(--space-xl); font-size: var(--font-size-lg); margin-bottom: var(--space-md);">Complete Flow (6 Steps)</h3>
                <div class="stats-grid" style="grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: var(--space-xl);">
                    <div class="client-vision-stat" style="padding: 1rem; flex-direction: column; align-items: flex-start;">
                        <span style="color: var(--accent); font-weight: bold; font-size: 0.8rem; margin-bottom: 0.2rem;">1. ATS Integration</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">Connect to 100+ ATS platforms (Greenhouse, Lever, Workable).</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1rem; flex-direction: column; align-items: flex-start;">
                        <span style="color: var(--accent); font-weight: bold; font-size: 0.8rem; margin-bottom: 0.2rem;">2. Job Stage Selection</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">Choose which ATS stage to screen (e.g., "Resume Review").</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1rem; flex-direction: column; align-items: flex-start;">
                        <span style="color: var(--accent); font-weight: bold; font-size: 0.8rem; margin-bottom: 0.2rem;">3. Screening Rules</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">Set resume parsing criteria (skills, experience, education).</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1rem; flex-direction: column; align-items: flex-start;">
                        <span style="color: var(--accent); font-weight: bold; font-size: 0.8rem; margin-bottom: 0.2rem;">4. Threshold Configuration</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">Define cut-off scores (e.g., 70% match = auto-advance).</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1rem; flex-direction: column; align-items: flex-start;">
                        <span style="color: var(--accent); font-weight: bold; font-size: 0.8rem; margin-bottom: 0.2rem;">5. Batch Processing</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">AI screens up to 500 resumes per run.</div>
                    </div>
                    <div class="client-vision-stat" style="padding: 1rem; flex-direction: column; align-items: flex-start;">
                        <span style="color: var(--accent); font-weight: bold; font-size: 0.8rem; margin-bottom: 0.2rem;">6. Review &amp; Override</span>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">Employers see AI decisions, can manually approve/reject.</div>
                    </div>
                </div>

                <h3 style="color: var(--text-primary); font-size: var(--font-size-lg); margin-bottom: var(--space-md);">Key Design Decisions</h3>
                <div class="lifecycle-steps" style="margin-bottom: var(--space-xl);">
                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">Decision 1: Confidence Score Visualization</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Challenge:</strong> How do we show AI's "certainty" without overwhelming users?</p>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Solution:</strong> Used a slider with snap points at 50%, 70%, 90% and color-coded zones (red &lt;50%, yellow 50-70%, green &gt;70%). This made abstract confidence scores tangible and actionable.</p>
                            <p style="color: var(--text-secondary); margin-bottom: 0;"><strong>Trade-off:</strong> Simplified continuous scores into discrete buckets—acceptable because employers needed clear decision points, not granular precision.</p>
                        </div>
                    </div>

                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">Decision 2: Auto-Advance Toggle</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Challenge:</strong> Some employers want full automation; others want review checkpoints.</p>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Solution:</strong> Created an opt-in toggle: "Auto-advance candidates above threshold." When disabled, all candidates wait in a review queue.</p>
                            <p style="color: var(--text-secondary); margin-bottom: 0;"><strong>Trade-off:</strong> Added configuration complexity but gave employers the control they needed for high-stakes decisions.</p>
                        </div>
                    </div>

                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">Decision 3: Rejection Handling</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Challenge:</strong> What happens to candidates below the threshold?</p>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Solution:</strong> Two paths: Auto-reject (removes from ATS) or Keep for manual review (candidate stays in system).</p>
                            <p style="color: var(--text-secondary); margin-bottom: 0;"><strong>Trade-off:</strong> Auto-reject is risky but desired by high-volume recruiters. We added a clear warning: "Auto-rejected candidates cannot be recovered."</p>
                        </div>
                    </div>

                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">Decision 4: ATS Stage Mapping</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Challenge:</strong> Every ATS uses different stage names ("Screening" vs "Resume Review" vs "Initial Review").</p>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);"><strong>Solution:</strong> Dynamic dropdown populated from connected ATS's actual stage names—no guessing.</p>
                            <p style="color: var(--text-secondary); margin-bottom: 0;"><strong>Trade-off:</strong> Required complex backend integration but eliminated user confusion.</p>
                        </div>
                    </div>
                </div>

                <div class="t-grid" style="margin-bottom: var(--space-xl);">
                    <div class="t-row t-header">
                        <div class="t-col-1" style="flex: 0 0 30%;">Category</div>
                        <div class="t-col-2" style="flex: 1;">Details</div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: 600; color: var(--text-primary); flex: 0 0 30%;">Validation Approach</div>
                        <div class="t-col-2" style="flex: 1;"><p style="font-size: 0.9em; line-height: 1.5; color: var(--text-secondary); margin: 0;">Since this feature was under development when I left, we validated through: Founder demos with prospective clients (recorded feedback on trust, control, clarity), Internal stress-testing with sample resumes (identified edge cases like PDFs with non-standard formatting), and Developer review of technical feasibility (confirmed ATS integrations were possible).</p></div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: 600; color: var(--text-primary); flex: 0 0 30%;">Expected Impact</div>
                        <div class="t-col-2" style="flex: 1;">
                            <ul style="font-size: 0.9em; line-height: 1.5; color: var(--text-secondary); margin: 0; padding-left: 1rem;">
                                <li>Reduce time-to-hire by automating initial resume screening</li>
                                <li>Process 500+ resumes in minutes vs. hours of manual review</li>
                                <li>Maintain employer control through configurable thresholds and override capabilities</li>
                                <li>Provide transparency into AI decision-making via confidence scores</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DEEP DIVE: Reporting -->
            <section class="lifecycle-section reveal">
                <div class="section-heading" style="margin-bottom: var(--space-xl);">
                    <div class="section-heading__line"></div>
                    <h2 class="section-heading__text">Deep Dive: Reporting as a Product</h2>
                    <div class="section-heading__line"></div>
                </div>

                <div class="case-section__content" style="max-width: 100%; margin-bottom: var(--space-xl);">
                    <p><strong>The Problem:</strong> Employers needed to evaluate candidates quickly, but our reporting system was fragmented: basic reports lacked depth, psychometric reports (DISC, personality) weren't customized to Testlify's brand, and there was no unified export system—users had to download multiple PDFs per candidate.</p>
                </div>

                <h3 style="color: var(--text-primary); font-size: var(--font-size-lg); margin-bottom: var(--space-md);">Design Exploration: Three Approaches</h3>
                <div class="option-grid" style="margin-bottom: var(--space-xl);">
                    <div class="option-card">
                        <h4 style="color: var(--text-primary); margin-bottom: 8px;">Option 1: Basic Template Redesign</h4>
                        <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 8px;">Clean up existing reports; keep separate PDFs per test type.</p>
                        <p style="font-size: var(--font-size-xs); color: #ff6b6b; margin-bottom: 0;"><strong style="font-weight: 600;">✗ Trade-off:</strong> Quick fix but doesn't solve fragmentation or customization needs.</p>
                    </div>
                    <div class="option-card">
                        <h4 style="color: var(--text-primary); margin-bottom: 8px;">Option 2: Unified Report Builder</h4>
                        <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 8px;">Let employers customize report sections, choose which tests to include, design their own layouts.</p>
                        <p style="font-size: var(--font-size-xs); color: #ff6b6b; margin-bottom: 0;"><strong style="font-weight: 600;">✗ Trade-off:</strong> Powerful but too complex for most users—over-engineered.</p>
                    </div>
                    <div class="option-card option-card--selected">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <h4 style="color: var(--accent); margin: 0;">Option 3: Curated Report System</h4>
                            <span style="font-size: 10px; background: var(--accent); color: #000; padding: 2px 6px; border-radius: 4px; font-weight: bold;">CHOSEN</span>
                        </div>
                        <p style="font-size: var(--font-size-xs); color: var(--text-secondary); margin-bottom: 8px;">Redesign core reports with Testlify branding; create 8 standardized psychometric PDFs; build smart export (one-click download of all candidate reports).</p>
                        <p style="font-size: var(--font-size-xs); color: var(--accent); margin-bottom: 0;"><strong style="font-weight: 600;">✓ Chosen because:</strong> Balanced quality with usability—professional output without configuration overhead.</p>
                    </div>
                </div>

                <h3 style="color: var(--text-primary); font-size: var(--font-size-lg); margin-bottom: var(--space-md);">What I Designed</h3>
                <div class="lifecycle-steps" style="margin-bottom: var(--space-xl);">
                    <div class="lifecycle-step reveal" style="grid-template-columns: 1fr;">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">1. Core Report Redesign</h3>
                            <p style="color: var(--text-secondary); margin-bottom: 0;">Rebuilt the primary assessment report with: Visual scoring system (color-coded performance indicators), Test-by-test breakdowns (skill tests, psychometric, coding, AI interviews), Candidate timeline (time spent per question, completion patterns), and Comparison view (candidate vs. job requirements).</p>
                        </div>
                    </div>
                    <div class="lifecycle-step reveal" style="grid-template-columns: 1fr;">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">2. 8 Psychometric PDFs</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);">Created branded report templates for: DISC personality (4-quadrant behavioral analysis), Big Five traits (detailed personality dimensions), Work style assessments, Communication preferences, Leadership potential, Team dynamics, and Problem-solving approaches.</p>
                            <p style="color: var(--text-secondary); margin-bottom: 0;">Each report included visual data representations (charts, graphs), narrative interpretations (plain-language explanations), and actionable insights (hiring recommendations).</p>
                        </div>
                    </div>
                    <div class="lifecycle-step reveal" style="grid-template-columns: 1fr;">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">3. Export Architecture</h3>
                            <p style="color: var(--text-secondary); margin-bottom: 0;">Designed a one-click export system: Single button downloads all candidate reports as a ZIP file, Reports auto-named with candidate name and test type (e.g., "John_Doe_DISC_Assessment.pdf"), and Smart bundling (only includes completed tests, skips incomplete ones).</p>
                        </div>
                    </div>
                </div>

                <div class="contribution-card" style="margin-top: var(--space-lg);">
                    <h3 class="contribution-card__title">Impact</h3>
                    <ul style="color: var(--text-secondary); font-size: 0.9em; padding-left: 1.2rem; margin-bottom: 0; line-height: 1.6;">
                        <li>Reduced employer time-to-decision by consolidating fragmented reports</li>
                        <li>Eliminated manual PDF collection—one-click export vs. downloading 5-10 separate files</li>
                        <li>Professional, branded output improved perceived platform quality</li>
                        <li>Psychometric reports became a competitive differentiator in sales demos</li>
                    </ul>
                </div>
            </section>

            <!-- Other Key Contributions -->
            <section class="case-section reveal">
                <h2 class="case-section__title">Other Key Contributions</h2>
                <div class="t-grid">
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: bold; color: var(--text-primary); flex: 0 0 30%;">Decision Visibility in Test Libraries</div>
                        <div class="t-col-2" style="color: var(--text-secondary); font-size: 0.9em; line-height: 1.5; flex: 1;">When employers browse 3,000+ pre-created tests, they needed clarity on test structure before adding to assessments. Designed an expandable preview showing question types, time estimates, and difficulty levels—reduced "wrong test added" support tickets.</div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: bold; color: var(--text-primary); flex: 0 0 30%;">Enterprise Infrastructure (SAML SSO, Billing, Email Config)</div>
                        <div class="t-col-2" style="color: var(--text-secondary); font-size: 0.9em; line-height: 1.5; flex: 1;">For enterprise clients, designed configuration interfaces for single sign-on, usage-based billing dashboards, custom email domains, and admin role management. Made complex technical features accessible to non-technical HR teams.</div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: bold; color: var(--text-primary); flex: 0 0 30%;">Marketing Alignment</div>
                        <div class="t-col-2" style="color: var(--text-secondary); font-size: 0.9em; line-height: 1.5; flex: 1;">Collaborated with marketing to ensure platform UI matched website messaging. Updated terminology, redesigned onboarding flows, and created promotional banners—resulted in cohesive brand experience from first click to daily use.</div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: bold; color: var(--text-primary); flex: 0 0 30%;">Cross-Platform Validation</div>
                        <div class="t-col-2" style="color: var(--text-secondary); font-size: 0.9em; line-height: 1.5; flex: 1;">Ensured design consistency across Employer Portal, Candidate Portal, and mobile experiences. Caught platform-specific bugs (e.g., video recording issues on iOS Safari) and pushed fixes before user impact.</div>
                    </div>
                </div>
            </section>

            <!-- Operating At Scale -->
            <section class="case-section reveal">
                <h2 class="case-section__title">Operating at Scale</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">Managing Incoming Requests</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Sales, marketing, and customer success teams posted client requests on Slack. I monitored the channel, took ownership of relevant requests, assessed technical feasibility, created Jira tickets with defined scope, designed solutions, validated with founders, coordinated with dev through QA, and informed stakeholders of outcomes (including rejections when technically infeasible).</p>
                    </div>
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">Balancing Speed &amp; Safety</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">With 229 tickets over 1.5 years, velocity mattered—but not at the expense of quality. I developed rapid validation techniques (AI stress-testing for edge cases, developer collaboration on technical constraints) and prioritized ruthlessly (focused on high-impact work, deferred low-value requests). Revenue-driven prioritization sometimes meant pausing strategic work for urgent client needs—I learned to adapt without compromising core UX principles.</p>
                    </div>
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">Bug Identification &amp; Resolution</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Beyond feature work, I proactively identified UI/UX bugs reported by clients, internal teams, and through my own QA. Created tickets, defined fixes, and ensured resolution—contributed to platform stability and user trust.</p>
                    </div>
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">Supporting Junior Designers</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Mentored two junior designers, reviewed their work, provided feedback on interaction patterns and visual hierarchy, and helped them navigate ambiguous requirements. This wasn't formal management, but I invested in their growth because it improved overall team output.</p>
                    </div>
                    <div class="contribution-card">
                        <h3 class="contribution-card__title">Context Switching</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Juggled multiple projects simultaneously: strategic epics (multi-week initiatives like Resume Parser), daily feature requests (Slack-to-Jira pipeline), bug fixes (interrupt-driven work), and design system maintenance (ensuring pattern consistency). Learned to prioritize based on business impact, not personal preference.</p>
                    </div>
                </div>
            </section>

            <!-- Impact -->
            <section class="case-section reveal">
                <h2 class="case-section__title">Impact</h2>
                
                <div class="stats-grid" style="grid-template-columns: repeat(2, 1fr); gap: 1.5rem; margin-bottom: var(--space-xl);">
                    <div class="contribution-card" style="margin: 0;">
                        <h4 style="color: var(--accent); margin-bottom: 12px;">Delivery &amp; Scale</h4>
                        <ul class="impact-list" style="margin: 0; display: block;">
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 6px; list-style-type: disc; margin-left: 20px;">229 Jira tickets delivered (193 tasks, 12 strategic epics, 10 improvements, 6 bugs, 5 new features)</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 6px; list-style-type: disc; margin-left: 20px;">111 features shipped to production across 3 core surfaces</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 6px; list-style-type: disc; margin-left: 20px;">61 designs passed to development (validated, documented, ready for build)</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 6px; list-style-type: disc; margin-left: 20px;">80 enhancement requests executed (improving existing features)</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); list-style-type: disc; margin-left: 20px;">21 client-driven improvements delivered (direct customer needs addressed)</li>
                        </ul>
                    </div>
                    <div class="contribution-card" style="margin: 0;">
                        <h4 style="color: var(--accent); margin-bottom: 12px;">User Evidence</h4>
                        <ul class="impact-list" style="margin: 0; display: block;">
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 8px; list-style-type: disc; margin-left: 20px;">Customer success team reported faster client onboarding after Resume Parser demos</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 8px; list-style-type: disc; margin-left: 20px;">Internal team feedback: "The new reporting system cut candidate review time in half"</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 8px; list-style-type: disc; margin-left: 20px;">Founder validation: "Prashant's designs became our competitive advantage in sales pitches"</li>
                            <li style="font-size: 0.85rem; color: var(--text-secondary); list-style-type: disc; margin-left: 20px;">Platform achieved 80% candidate completion rate—2-3x better than typical assessment tools</li>
                        </ul>
                    </div>
                </div>

                <div class="t-grid" style="margin-bottom: var(--space-xl);">
                    <div class="t-row t-header">
                        <div class="t-col-1" style="flex: 0 0 30%;">Area</div>
                        <div class="t-col-2" style="flex: 1;">Key Outcomes</div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: 600; color: var(--text-primary); flex: 0 0 30%;">Platform Growth</div>
                        <div class="t-col-2" style="flex: 1;">
                            <ul style="font-size: 0.9em; line-height: 1.5; color: var(--text-secondary); margin: 0; padding-left: 1rem;">
                                <li>Designed for platform serving 4,500+ job roles across 50+ industries</li>
                                <li>Work supported 100+ ATS integrations</li>
                                <li>Platform processed thousands of assessments daily at peak</li>
                                <li>Companies reported 82% reduction in time-to-hire (platform-wide metric)</li>
                            </ul>
                        </div>
                    </div>
                    <div class="t-row">
                        <div class="t-col-1" style="font-weight: 600; color: var(--text-primary); flex: 0 0 30%;">Process Improvements</div>
                        <div class="t-col-2" style="flex: 1;">
                            <ul style="font-size: 0.9em; line-height: 1.5; color: var(--text-secondary); margin: 0; padding-left: 1rem;">
                                <li>Established Slack-to-Jira request management process (reduced dropped requests)</li>
                                <li>Created design system documentation (improved consistency across 229 tickets)</li>
                                <li>Introduced AI validation techniques (caught edge cases before development)</li>
                                <li>Built cross-functional collaboration rhythms (reduced back-and-forth with dev)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- What I Learned -->
            <section class="case-section reveal">
                <h2 class="case-section__title">What I Learned</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">1. Designing in Ambiguity</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Early-stage startups don't have playbooks. I learned to validate assumptions through rapid prototyping, make decisions with incomplete data, and adapt when direction changed. The Resume Parser project taught me to balance visionary thinking with practical constraints.</p>
                    </div>
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">2. Systems Thinking at Scale</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">229 tickets sounds like task execution, but it required deep systems thinking. Every design decision had cascading effects across surfaces, user types, and technical architecture. I learned to map dependencies before designing, anticipate edge cases, and collaborate closely with backend teams.</p>
                    </div>
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">3. Strategic Partnership Over Service Design</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">I evolved from "designer who makes things look good" to "design partner who shapes product direction." Founders trusted me to challenge requirements, propose alternatives, and push back when user needs conflicted with business wants. This required building credibility through consistent delivery.</p>
                    </div>
                    <div class="contribution-card" style="margin-bottom: var(--space-md);">
                        <h3 class="contribution-card__title">4. Balancing Trade-offs, Not Finding Perfect Solutions</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">AI automation vs. human control. Speed vs. thoroughness. Simplicity vs. power. Every project involved trade-offs. I learned to frame design decisions around "what we're optimizing for" rather than "what's the right answer." The Resume Parser's three-option exploration exemplified this—no perfect solution, just the best fit for context.</p>
                    </div>
                    <div class="contribution-card">
                        <h3 class="contribution-card__title">5. Quality at Velocity</h3>
                        <p class="contribution-card__problem-text" style="color: var(--text-secondary);">Shipping 229 tickets in 1.5 years while maintaining design quality required ruthless efficiency: Reusable components over bespoke solutions, documented patterns for team alignment, AI tools for validation at speed, and clear communication to reduce revision cycles. I learned that velocity comes from smart systems, not just working faster.</p>
                    </div>
                </div>
            </section>

            <!-- Reflection -->
            <div class="reflection reveal">
                <h2 class="reflection__title">Reflection</h2>
                <div class="reflection__text">
                    <p style="margin-bottom: var(--space-md);">When I joined Testlify, I saw it as a feature execution role—take requirements, make them pretty, ship fast. By the time I left, I'd become a strategic design partner who shaped product direction, influenced roadmap priorities, and built systems that scaled beyond individual projects.</p>
                    <p style="margin-bottom: var(--space-md);">The journey from 229 Jira tickets to a cohesive product experience taught me that great design isn't about making individual features beautiful—it's about building systems that work consistently at scale. It's about making complex decisions transparent. It's about earning trust through delivery. And it's about balancing visionary thinking with the reality of startup constraints.</p>
                    <p style="margin-bottom: var(--space-md);">If I could go back, I'd push for dedicated user research earlier (we relied too heavily on founder intuition), document edge cases more rigorously (would've prevented some late-cycle bugs), and invest in design system infrastructure sooner (consistency suffered under velocity pressure). But I wouldn't change the experience of learning to design in ambiguity, ship at speed, and partner strategically with leadership.</p>
                    <p style="font-weight: 600; color: var(--accent);">That's the designer I became at Testlify—and the designer I bring to my next role.</p>
                </div>
            </div>

            <!-- Next Project -->
            <div class="next-project reveal">
                <p class="next-project__label">Next Project</p>
                <a href="homes-collection.html" class="next-project__card">
                    <span class="next-project__category">Real Estate</span>
                    <h3 class="next-project__title">Homes Collection - Fractional ownership platform for real estate investment</h3>
                </a>
            </div>

        </div>
    </main>"""

# Using the original prefix + new content + original suffix
import os
final_content = prefix + new_main + suffix

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(final_content)

print("Updated testlify.html with exact 1:1 content completely covering the markdown content.")
