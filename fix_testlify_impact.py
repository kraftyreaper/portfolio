import re

with open('case-studies/testlify.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_content_pattern = r'<!--[^>]*?IMPACT AT A GLANCE[^>]*?-->.*?<\/section>'
new_content = r'''<!-- ── IMPACT AT A GLANCE ── -->
            <section class="case-section reveal" aria-labelledby="section-at-a-glance">
                <h2 class="case-section__title" id="section-at-a-glance">IMPACT AT A GLANCE</h2>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;" class="impact-grid-2">
                    <div class="contribution-card" style="margin: 0; text-align: left;">
                        <div class="card-label" style="text-transform: uppercase;">WHAT IS TESTLIFY?</div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.8; margin: 0;">B2B SaaS AI-powered assessment platform &mdash; 3,000+ tests, 45+ coding languages, 100+ ATS integrations</p>
                    </div>
                    <div class="contribution-card" style="margin: 0; text-align: left;">
                        <div class="card-label" style="text-transform: uppercase;">MY SCOPE</div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.8; margin: 0;">Design lead across Employer Portal, Candidate Portal (web, Android, iOS), and AI Interview System &mdash; working directly with founders on product strategy</p>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-bottom: var(--space-xl);" class="impact-grid-4">
                    <div class="contribution-card" style="margin: 0; text-align: left;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--accent); margin-bottom: 4px; line-height: 1;">229</div>
                        <h3 style="font-size: 0.9rem; font-weight: 600; color: #fff; margin-bottom: 8px;">Jira tickets delivered</h3>
                        <p style="color: var(--text-secondary); font-size: 0.85rem; line-height: 1.6; margin: 0;">193 tasks &middot; 12 epics &middot; 10 improvements across 4 pre-production environments</p>
                    </div>
                    <div class="contribution-card" style="margin: 0; text-align: left;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--accent); margin-bottom: 4px; line-height: 1;">111</div>
                        <h3 style="font-size: 0.9rem; font-weight: 600; color: #fff; margin-bottom: 8px;">Features shipped</h3>
                        <p style="color: var(--text-secondary); font-size: 0.85rem; line-height: 1.6; margin: 0;">To production across 3 core surfaces &mdash; employer portal, candidate portal, and reporting system</p>
                    </div>
                    <div class="contribution-card" style="margin: 0; text-align: left;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--accent); margin-bottom: 4px; line-height: 1;">80%</div>
                        <h3 style="font-size: 0.9rem; font-weight: 600; color: #fff; margin-bottom: 8px;">Candidate completion rate</h3>
                        <p style="color: var(--text-secondary); font-size: 0.85rem; line-height: 1.6; margin: 0;">Platform-wide &mdash; 2&ndash;3&times; better than industry average for skill assessments</p>
                    </div>
                    <div class="contribution-card" style="margin: 0; text-align: left;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--accent); margin-bottom: 4px; line-height: 1;">498</div>
                        <h3 style="font-size: 0.9rem; font-weight: 600; color: #fff; margin-bottom: 8px;">Issues surfaced proactively</h3>
                        <p style="color: var(--text-secondary); font-size: 0.85rem; line-height: 1.6; margin: 0;">Caught through UAT across 5 browsers, 4 environments, and 4 platforms before user impact</p>
                    </div>
                </div>

                <style>
                    @media (max-width: 900px) {
                        .impact-grid-4 { grid-template-columns: repeat(2, 1fr) !important; }
                    }
                    @media (max-width: 640px) {
                        .impact-grid-2 { grid-template-columns: 1fr !important; }
                        .impact-grid-4 { grid-template-columns: 1fr !important; }
                    }
                </style>
            </section>'''

text = re.sub(old_content_pattern, new_content, text, flags=re.DOTALL)
with open('case-studies/testlify.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done replacement')
