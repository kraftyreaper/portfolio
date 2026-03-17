import re

html_content = """
    <!-- ── Case Study Content ── -->
    <main class="case-detail">
        <div class="container">

            <!-- Hero -->
            <div class="case-detail__hero reveal">
                <div class="case-detail__hero-meta">
                    <div class="case-detail__hero-line"></div>
                    <span class="case-detail__project">Testlify</span>
                    <span class="case-detail__dot">·</span>
                    <span class="case-detail__domain">AI-Powered Hiring Platform</span>
                    <div class="case-detail__hero-line"></div>
                </div>
                <h1 class="case-detail__title">Scaling a Configurable Hiring Platform</h1>
                <p style="color: var(--text-secondary); font-size: var(--font-size-md); margin-bottom: var(--space-md); text-align: center; max-width: 700px; margin-left: auto; margin-right: auto;">
                    Building structure in ambiguity and scaling an AI-powered B2B hiring platform.
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

            <!-- At a Glance -->
            <section class="case-section reveal">
                <div class="at-a-glance">
                    <div class="at-a-glance__row">
                        <div class="at-a-glance__label">What is Testlify?</div>
                        <div class="at-a-glance__value">
                            <p>AI-powered B2B hiring platform evaluated through skill assessments, automated resume parsing, and psychometric profiles.</p>
                        </div>
                    </div>
                    <div class="at-a-glance__row">
                        <div class="at-a-glance__label">My Role</div>
                        <div class="at-a-glance__value">
                            <p>Lead Product Designer scaling features, managing design debts, and shaping core system architecture over 18 months.</p>
                        </div>
                    </div>
                    <div class="at-a-glance__row">
                        <div class="at-a-glance__label">Scope &amp; Scale</div>
                        <div class="at-a-glance__value">
                            <ul class="case-carousel__list list--single" style="margin-top: 0; margin-bottom: 0;">
                                <li>500+ Jira tickets across Employer Portal &amp; Candidate App</li>
                                <li>Owned white-label enterprise system capabilities</li>
                                <li>Mentored 2-3 junior designers on the team</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- The Real Problem & Setup -->
            <section class="case-section reveal">
                <h2 class="case-section__title">The Real Problem</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <p>Hiring software operates in a high-stakes environment where design mistakes directly lead to <strong>wrong hires, biased evaluations, and operational chaos.</strong></p>
                    
                    <p>When I joined, Testlify had functional depth but severe growing complexity. The challenge wasn't just adding new AI features—it was preventing the platform from collapsing under its own configuration matrix. A single employer toggle on a test could radically cascade into:</p>
                    
                    <ul class="impact-list" style="margin-bottom: var(--space-xl); background: var(--bg-card); border: 1px solid var(--border-card); padding: var(--space-lg); border-radius: var(--radius-md);">
                        <li class="impact-list__item"><span class="impact-list__icon" style="color: var(--text-tertiary);">↳</span><span>Candidate statuses across the pipeline</span></li>
                        <li class="impact-list__item"><span class="impact-list__icon" style="color: var(--text-tertiary);">↳</span><span>Report output structure and psychometric weightings</span></li>
                        <li class="impact-list__item"><span class="impact-list__icon" style="color: var(--text-tertiary);">↳</span><span>PDF generation logic for external sharing</span></li>
                        <li class="impact-list__item"><span class="impact-list__icon" style="color: var(--text-tertiary);">↳</span><span>Cross-platform rendering and permissions on mobile</span></li>
                    </ul>

                    <div style="border-left: 2px solid var(--accent); padding-left: var(--space-md); margin-bottom: var(--space-xl);">
                        <span style="font-family: var(--font-family-heading); font-size: var(--font-size-md); color: var(--text-primary); font-weight: 500; line-height: 1.4;">The core design objective: Preserve enterprise flexibility without introducing systemic risks or candidate bias.</span>
                    </div>
                </div>
            </section>

            <!-- How I Worked -->
            <section class="case-section reveal">
                <h2 class="case-section__title">How I Worked</h2>
                <div class="table-wrapper">
                    <table class="decision-table" style="min-width: 100%; table-layout: fixed; margin: 0;">
                        <colgroup>
                            <col style="width: 35%;">
                            <col style="width: 65%;">
                        </colgroup>
                        <thead>
                            <tr>
                                <th>The Raw Reality</th>
                                <th>How I Handled It</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Founders provided high-level references without detailed PRDs. Requirements were often vague or half-baked.</td>
                                <td><strong>Structured ambiguity into logic:</strong> Modeled failure states, identified edge cases, and wrote TUX (design architecture) tickets before pushing anything to development.</td>
                            </tr>
                            <tr>
                                <td>Client-requested feature building overtook UX refinement due to revenue pressure.</td>
                                <td><strong>Feasibility and constraint validation:</strong> Acted as the bridge to engineering to align heavily on technical timelines, stopping scope creep.</td>
                            </tr>
                            <tr>
                                <td>No senior UX reviewer or structured UI critique processes in place.</td>
                                <td><strong>UAT Gatekeeping:</strong> Supported junior designers tightly and blocked releases across 4 prep environments if UX quality or data logic was flawed.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- Cross-Platform (Moved Up) -->
            <section class="case-section reveal">
                <h2 class="case-section__title">Cross-Platform Considerations</h2>
                <div class="case-section__content" style="max-width: 100%;">
                    <p style="margin-bottom: var(--space-md);">Because Testlify is multi-faceted, design decisions were never isolated to a single screen. Employer portal configurations heavily muttered candidate-side interactions across devices.</p>
                    
                    <div class="cascade-flow" style="margin-bottom: var(--space-xl); background: rgba(255, 255, 255, 0.02);">
                        <p style="color: var(--text-primary); font-weight: 600; font-size: var(--font-size-md); margin-bottom: var(--space-sm);">A concrete cross-platform cascade example:</p>
                        An employer flags a "video-response" required on an assessment.
                        <br><span class="cascade-flow__arrow">↳</span> This triggers mobile camera permission requests for candidates (Android/iOS).
                        <br><span class="cascade-flow__arrow">↳</span> Safari handles these permissions differently than Chrome natively.
                        <br><span class="cascade-flow__arrow">↳</span> High bitrate video responses tank performance on older mobile devices.
                        <br><strong style="color: var(--text-primary); display: inline-block; margin-top: 8px;">The Result:</strong> We had to design unified pre-flight hardware checks and graceful degradation fallbacks before the candidate even saw question one.
                    </div>
                </div>
            </section>

            <!-- Major Contribution Section (Consolidated) -->
            <section class="lifecycle-section reveal">
                <div class="section-heading" style="margin-bottom: var(--space-xl);">
                    <div class="section-heading__line"></div>
                    <h2 class="section-heading__text">Flagship Feature: AI Resume Parser</h2>
                    <div class="section-heading__line"></div>
                </div>
                
                <div class="case-section__content" style="max-width: 100%; margin-bottom: var(--space-2xl);">
                    <p style="margin-bottom: var(--space-md);">A client requested automated resume screening integrated with their ATS workflow. The risk of over-automation was high: silent algorithmic rejections of qualified candidates due to poor threshold setups could spark legal liabilities.</p>
                </div>

                <div class="lifecycle-steps" style="margin-bottom: var(--space-3xl);">
                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">1. ATS Gate &amp; Stage Mapping</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);">Connected the parser strictly to established ATS workflows (Greenhouse) with distinct error states. Once connected, recruiters select existing stages (e.g., "Screening") to pull candidate pools from.</p>
                        </div>
                        <div class="lifecycle-step__media placeholder-image" style="background: #111;">
                            <span class="placeholder-image__icon">🔌</span>
                            <span class="placeholder-image__label">ATS Sync Controls</span>
                        </div>
                    </div>

                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">2. AI Criteria Suggestions</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);">Based on the job description, the AI suggests 10 criteria. We hard-coded a requirement forcing employers to manually select/verify the minimum 8 criteria, balancing AI generation with necessary human judgment.</p>
                        </div>
                        <div class="lifecycle-step__media placeholder-image" style="background: #111;">
                            <span class="placeholder-image__icon">✨</span>
                            <span class="placeholder-image__label">Criteria Generation</span>
                        </div>
                    </div>

                    <div class="lifecycle-step reveal">
                        <div class="lifecycle-step__content">
                            <h3 class="lifecycle-step__title">3. Evaluation &amp; Overrides</h3>
                            <p style="color: var(--text-secondary); margin-bottom: var(--space-xs);">The interface breaks down AI processing into High/Medium/Low bands with visual reasoning per criteria. Crucially, manual review actions persist natively over all recommendations.</p>
                        </div>
                        <div class="lifecycle-step__media placeholder-image" style="background: #111;">
                            <span class="placeholder-image__icon">👥</span>
                            <span class="placeholder-image__label">Evaluation UI</span>
                        </div>
                    </div>
                </div>
                
                <h3 class="case-section__title" style="margin-top: var(--space-2xl); font-size: var(--font-size-lg);">Designing for Safety: Principles &amp; Trade-Offs</h3>
                <p class="case-section__content" style="margin-bottom: var(--space-lg);">To actively prevent algorithmic bias, I mapped strict safety principles into my design elements, sacrificing pure automation speed for deep system reliability.</p>
                
                <div class="principles-grid">
                    <div class="principle-card">
                        <span class="principle-card__number">Control Over Automation</span>
                        <h3 class="principle-card__title">Mandatory Confirmation</h3>
                        <p class="principle-card__desc">Rejection is irreversible. Employers must explicitly confirm bulk rejections triggered by score thresholds before they activate in the system.</p>
                    </div>
                    <div class="principle-card">
                        <span class="principle-card__number">Guardrails, Not Gates</span>
                        <h3 class="principle-card__title">Pause Caps &amp; Defaults</h3>
                        <p class="principle-card__desc">A hard default cap of processing 20 candidates per batch shields employers from volume errors. A global pause capability allows immediate overrides.</p>
                    </div>
                    <div class="principle-card">
                        <span class="principle-card__number">Transparency in Complexity</span>
                        <h3 class="principle-card__title">Exposed Sync States</h3>
                        <p class="principle-card__desc">Rather than abstracting ATS sync issues under a loading spinner, we exposed granular sync states with distinct manual failover controls.</p>
                    </div>
                </div>
            </section>

            <!-- Other Key Contributions -->
            <section class="case-section reveal">
                <h2 class="case-section__title">System-wide Structural Solutions</h2>

                <div class="contribution-card">
                    <h3 class="contribution-card__title">Decision Visibility Across Libraries</h3>
                    <p class="contribution-card__problem-text" style="margin-bottom: var(--space-md);"><strong style="color: var(--text-primary);">The Problem:</strong> Choosing between 3,000+ tests and 182,000+ questions involved pure guesswork.</p>
                    <p class="contribution-card__problem-text"><strong style="color:var(--accent);">The Solution:</strong> Surfaced "Candidates Assessed" telemetry immediately on listing cards. This tiny UI introduction organically guided employers toward historically proven testing assets over dead weight.</p>
                </div>

                <div class="contribution-card">
                    <h3 class="contribution-card__title">Reporting as a Shareable Product</h3>
                    <div class="table-wrapper">
                        <table class="decision-table" style="min-width: 100%; table-layout: fixed; margin: 0;">
                            <colgroup>
                                <col style="width: 35%;">
                                <col style="width: 65%;">
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td>Psychometric PDFs</td>
                                    <td>Turned chaotic data points into gorgeous, modular insights supporting 8 frameworks (Big Five, 16 Personality, Enneagram, etc.) drastically improving client trust when they shared exports internally.</td>
                                </tr>
                                <tr>
                                    <td>Export Architecture</td>
                                    <td>Redesigned the export tree allowing granular extraction (Single report, Library-only, Merged bundles).</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="contribution-card">
                    <h3 class="contribution-card__title">Cleaning the Employer Portal</h3>
                    <div class="table-wrapper">
                        <table class="decision-table" style="min-width: 100%; table-layout: fixed; margin: 0;">
                            <colgroup>
                                <col style="width: 35%;">
                                <col style="width: 65%;">
                            </colgroup>
                            <tbody>
                                <tr>
                                    <td>Billing &amp; SSO</td>
                                    <td>Centralized scattered billing into a single dashboard. Mapped massive enterprise SAML SSO setup into a clear configuration tab.</td>
                                </tr>
                                <tr>
                                    <td>Marketing &amp; Product Alignment</td>
                                    <td>Identified misalignments regarding "AI perfection" claims on the marketing site. Regulated terminology to emphasize "AI Assistance" rather than full automation to set safe user expectations.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- Parallel Projects -->
            <section class="case-section reveal">
                <h2 class="case-section__title">Maintaining Quality Under Volume</h2>
                <p class="case-section__content" style="margin-bottom: var(--space-xl);">In parallel with Testlify's ecosystem, I consistently output UI work for adjacent brands—showcasing rapid context-switching capabilities.</p>
                
                <div class="parallel-projects">
                    <a href="https://metanotes.ai/" target="_blank" class="project-mini-card" style="text-decoration: none;">
                        <span class="project-mini-card__role">UI Designer (Solo)</span>
                        <h3 class="project-mini-card__name">Metanotes Pricing Site</h3>
                        <p class="project-mini-card__desc">Conducted competitor research against Otter/Fireflies to architect a clean WordPress marketing foundation.</p>
                        <span style="font-size: var(--font-size-xs); color: var(--accent); margin-top: var(--space-sm); display: inline-block;">View Site →</span>
                    </a>
                    <a href="https://www.dymon.ca/" target="_blank" class="project-mini-card" style="text-decoration: none;">
                        <span class="project-mini-card__role">UI Designer</span>
                        <h3 class="project-mini-card__name">DYMON Storage</h3>
                        <p class="project-mini-card__desc">Deployed robust, system-aligned e-commerce pages relying heavily on rigorous existing brand guardrails.</p>
                        <span style="font-size: var(--font-size-xs); color: var(--accent); margin-top: var(--space-sm); display: inline-block;">View Site →</span>
                    </a>
                    <a href="https://appforest.io/" target="_blank" class="project-mini-card" style="text-decoration: none;">
                        <span class="project-mini-card__role">UI Designer</span>
                        <h3 class="project-mini-card__name">Appforest Time Tracking</h3>
                        <p class="project-mini-card__desc">Researched standard tools like Tempo to map robust UI requirements natively into the Jira Marketplace standard.</p>
                        <span style="font-size: var(--font-size-xs); color: var(--accent); margin-top: var(--space-sm); display: inline-block;">View Site →</span>
                    </a>
                </div>
            </section>

            <!-- Reflection -->
            <div class="reflection reveal">
                <h2 class="reflection__title">Reflection</h2>
                <div class="reflection__text">
                    <p>Building in a B2B SaaS environment means accepting that requirements are ambiguous, timelines are ruthless, and UI aesthetics are secondary to functional reliability. A beautiful interface means nothing if the underlying parsing engine generates biased candidate rejections.</p>
                    <p>Over 18 months, my role evolved from purely executing feature screens to policing the architecture—reducing long-term risk and maintaining coherence across an exponentially growing tech stack. I learned to leverage friction deliberately to protect the end-user, proving that thoughtful design isn't just visually engaging—it's structurally defensive.</p>
                </div>
            </div>

            <!-- Next Project -->
            <div class="next-project reveal">
                <p class="next-project__label">Next Project</p>
                <a href="homes-collection.html" class="next-project__card">
                    <span class="next-project__category">Real Estate</span>
                    <h3 class="next-project__title">Homes Collection - Revolutionizing fractional ownership platform for
                        real estate investment</h3>
                </a>
            </div>

        </div>
    </main>
"""

with open(r"c:\Users\prash\.gemini\antigravity\scratch\portfolio\case-studies\testlify.html", "r", encoding='utf-8') as f:
    text = f.read()

prefix = text.split('<!-- ── Case Study Content ── -->')[0]
suffix = text.split('<!-- ── Footer ── -->')[1]

new_text = prefix + html_content + '    <!-- ── Footer ── -->' + suffix

with open(r"c:\Users\prash\.gemini\antigravity\scratch\portfolio\case-studies\testlify.html", "w", encoding='utf-8') as f:
    f.write(new_text)

print("Updated testlify.html completely replacing the redundant content")
