new_section = '''
            <!-- RESEARCH AND INSIGHTS -->
            <section class="case-section reveal" aria-labelledby="section-research">
                <div style="text-transform: uppercase; color: var(--text-secondary); font-size: 0.85rem; font-weight: 600; letter-spacing: 0.05em; margin-bottom: 0.5rem;">Research &amp; insights</div>
                <h2 class="case-section__title" id="section-research">How I knew what to design</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.8; margin-bottom: var(--space-xl);">There were no formal research sessions or dedicated UX researchers on this team. Insight came from being embedded in the product process and treating every touchpoint as a source of signal.</p>
                <div class="card-label" style="text-transform: uppercase; margin-bottom: var(--space-sm);">Where insights came from</div>
                <div style="width: 100%; overflow-x: auto; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; margin-bottom: var(--space-xl);">
                    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;">
                        <thead>
                            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); background: rgba(255, 255, 255, 0.03);">
                                <th style="padding: 1.25rem 1.5rem; color: #fff; font-weight: 600; min-width: 200px;">Source</th>
                                <th style="padding: 1.25rem 1.5rem; color: #fff; font-weight: 600;">What it gave me</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05);">
                                <td style="padding: 1.25rem 1.5rem; color: #fff; font-weight: 500; vertical-align: top;">Founders</td>
                                <td style="padding: 1.25rem 1.5rem; color: var(--text-secondary); line-height: 1.6; vertical-align: top;">Business direction, product vision, and priority framing. The founder was my primary lens for understanding what problems actually mattered to the business &mdash; and the final decision-maker on every design solution I proposed</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05);">
                                <td style="padding: 1.25rem 1.5rem; color: #fff; font-weight: 500; vertical-align: top;">Sales &amp; marketing team</td>
                                <td style="padding: 1.25rem 1.5rem; color: var(--text-secondary); line-height: 1.6; vertical-align: top;">Real-world signal on what clients asked about, what confused them in demos, and what competitors were doing. Sales feedback shaped how features were positioned and which gaps were most visible to prospects</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05);">
                                <td style="padding: 1.25rem 1.5rem; color: #fff; font-weight: 500; vertical-align: top;">UAT across pre-production</td>
                                <td style="padding: 1.25rem 1.5rem; color: var(--text-secondary); line-height: 1.6; vertical-align: top;">My primary discovery layer. Testing every feature across 4 environments, 5 browsers, and 4 platforms before release &mdash; I personally identified UX gaps that no one had flagged, proposed solutions with documented reasoning, and got them approved and built before the release shipped</td>
                            </tr>
                            <tr>
                                <td style="padding: 1.25rem 1.5rem; color: #fff; font-weight: 500; vertical-align: top;">Monthly sprint demos</td>
                                <td style="padding: 1.25rem 1.5rem; color: var(--text-secondary); line-height: 1.6; vertical-align: top;">Developers demonstrated completed features to the entire Testlify team including sales and marketing. Feedback from these sessions was collected, taken ownership of by designers, validated across pre-production environments, and pushed to production once verified. Designers then closed the loop &mdash; informing the relevant POC (internal or client-facing) that the feature was live</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="card-label" style="text-transform: uppercase; margin-bottom: var(--space-sm);">How I turned insight into approved solutions</div>
                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.8; margin-bottom: var(--space-xl);">Every solution I brought to the founder was accompanied by clear reasoning: what the problem was, why the proposed solution addressed it, and what the trade-off was if we chose differently. This wasn&rsquo;t a pitch &mdash; it was structured decision support. The outcome: every solution I proposed with clear reasoning was approved by the founder. That consistency wasn&rsquo;t luck &mdash; it was the result of doing the constraint triangulation and dependency mapping before the conversation, not during it.</p>
            </section>

'''

marker = '<!-- \u2500\u2500 HOW I WORKED \u2500\u2500 -->'

with open('case-studies/testlify.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the actual escaped sequence in the file
import re
m = re.search(r'<!--[^>]*HOW I WORKED[^>]*-->', content)
if m:
    actual_marker = m.group()
    content = content.replace(actual_marker, new_section + '            ' + actual_marker)
    with open('case-studies/testlify.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Inserted Research & Insights section successfully.")
else:
    print("Marker still not found.")
