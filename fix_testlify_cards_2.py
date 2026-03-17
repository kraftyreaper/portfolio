import re

with open('case-studies/testlify.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace "MY SCOPE" card in IMPACT AT A GLANCE
my_scope_rx = re.compile(
    r'<div class="contribution-card"[^>]*?>\s*<div class="card-label"[^>]*?>MY SCOPE</div>.*?working directly with founders on product strategy\s*</p>\s*</div>', 
    re.DOTALL
)

new_scope_html = '''<div class="contribution-card" style="margin: 0; text-align: left; padding: 2rem;">
                        <div class="card-label" style="text-transform: uppercase;">Scope &amp; Complexity</div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.8; margin-bottom: 0.5rem;">Testlify operates across multiple surfaces where every design decision cascades:</p>
                        <ul style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                            <li><strong>Employer Portal</strong> &mdash; assessment creation, test management, reporting</li>
                            <li><strong>Candidate Portal</strong> &mdash; web, Android, iOS test-taking experience</li>
                            <li><strong>AI Interview System</strong> &mdash; chat, video, audio simulations</li>
                            <li><strong>White-label &amp; Reseller configurations</strong></li>
                            <li><strong>PDF Reports</strong> &mdash; 10 psychometric assessments</li>
                        </ul>
                    </div>'''

if my_scope_rx.search(text):
    text = my_scope_rx.sub(new_scope_html, text)
    print("Replaced MY SCOPE card.")
else:
    print("MY SCOPE card not found.")


# 2. Remove "Scope & Complexity" card entirely
scope_complexity_rx = re.compile(
    r'<div class="contribution-card"[^>]*?>\s*<div class="card-label"[^>]*?>Scope &amp; Complexity</div>\s*<p[^>]*?>\s*Testlify operates across multiple surfaces.*?</ul>\s*</div>',
    re.DOTALL
)

if scope_complexity_rx.search(text):
    text = scope_complexity_rx.sub('', text)
    print("Removed Scope & Complexity card.")
else:
    print("Scope & Complexity card not found.")


# 3. Remove "Career Context" card entirely
career_context_rx = re.compile(
    r'<div class="contribution-card"[^>]*?>\s*<div class="card-label"[^>]*?>Career Context</div>\s*<p[^>]*?>\s*This\s*role marked my evolution.*?</div>',
    re.DOTALL
)

if career_context_rx.search(text):
    text = career_context_rx.sub('', text)
    print("Removed Career Context card.")
else:
    print("Career Context card not found.")


# Write back
with open('case-studies/testlify.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done updating testlify.html")
