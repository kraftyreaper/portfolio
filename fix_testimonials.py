import re

with open('case-studies/testlify.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Soft Yellow: #FEF3C7
# Dark Slate Text: #27272A (WCAG AAA)
# Medium Slate Cite: #52525B (WCAG AA)
# Very Dark Slate Name: #18181B (WCAG AAA)
# Very soft quote mark: rgba(0,0,0,0.06)

# Card 1 Replacement
card1_old = """                    <div
                        style="background: #facc15; border-radius: 14px; padding: 28px 30px; position: relative; overflow: hidden;">
                        <div
                            style="font-size: 72px; line-height: 1; color: rgba(0, 0, 0, 0.1); font-family: Georgia, serif; position: absolute; top: -10px; left: 18px; pointer-events: none;">
                            &ldquo;</div>
                        <blockquote
                            style="font-size: 0.95rem; line-height: 1.7; color: #171717; position: relative; z-index: 1; margin: 0 0 14px; font-style: italic;">
                            &ldquo;Proud of the growth you&rsquo;ve shown during your time with us. You consistently
                            brought thoughtfulness to problems, cared deeply about users, and kept raising the quality
                            bar. Wishing you an amazing next chapter.&rdquo;</blockquote>
                        <cite style="font-size: 0.8rem; color: #3f3f46; font-style: normal;"><strong
                                style="color: #000;">Abhishek Shah</strong> &mdash; Co-founder &amp; CEO, Testlify
                            &nbsp;&middot;&nbsp; LinkedIn comment, Jan 2026</cite>
                    </div>"""

card1_new = """                    <div
                        style="background: #FEF3C7; border-radius: 14px; padding: 28px 30px; position: relative; overflow: hidden;">
                        <div
                            style="font-size: 72px; line-height: 1; color: rgba(0, 0, 0, 0.06); font-family: Georgia, serif; position: absolute; top: -10px; left: 18px; pointer-events: none;">
                            &ldquo;</div>
                        <blockquote
                            style="font-size: 0.95rem; line-height: 1.7; color: #27272A; position: relative; z-index: 1; margin: 0 0 14px; font-style: italic;">
                            &ldquo;Proud of the growth you&rsquo;ve shown during your time with us. You consistently
                            brought thoughtfulness to problems, cared deeply about users, and kept raising the quality
                            bar. Wishing you an amazing next chapter.&rdquo;</blockquote>
                        <cite style="font-size: 0.8rem; color: #52525B; font-style: normal;"><strong
                                style="color: #18181B;">Abhishek Shah</strong> &mdash; Co-founder &amp; CEO, Testlify
                            &nbsp;&middot;&nbsp; LinkedIn comment, Jan 2026</cite>
                    </div>"""

text = text.replace(card1_old, card1_new)

# Card 2 Replacement
card2_old = """                    <div
                        style="background: #facc15; border-radius: 14px; padding: 28px 30px; position: relative; overflow: hidden;">
                        <div
                            style="font-size: 72px; line-height: 1; color: rgba(0, 0, 0, 0.1); font-family: Georgia, serif; position: absolute; top: -10px; left: 18px; pointer-events: none;">
                            &ldquo;</div>
                        <blockquote
                            style="font-size: 0.95rem; line-height: 1.7; color: #171717; position: relative; z-index: 1; margin: 0 0 14px; font-style: italic;">
                            &ldquo;We&rsquo;re grateful for the energy, curiosity, and ownership you brought to the
                            team. We&rsquo;ll be cheering you on.&rdquo;</blockquote>
                        <cite style="font-size: 0.8rem; color: #3f3f46; font-style: normal;"><strong
                                style="color: #000;">Testlify</strong> &mdash; Official company
                            LinkedIn comment, Jan 2026</cite>
                    </div>"""

card2_new = """                    <div
                        style="background: #FEF3C7; border-radius: 14px; padding: 28px 30px; position: relative; overflow: hidden;">
                        <div
                            style="font-size: 72px; line-height: 1; color: rgba(0, 0, 0, 0.06); font-family: Georgia, serif; position: absolute; top: -10px; left: 18px; pointer-events: none;">
                            &ldquo;</div>
                        <blockquote
                            style="font-size: 0.95rem; line-height: 1.7; color: #27272A; position: relative; z-index: 1; margin: 0 0 14px; font-style: italic;">
                            &ldquo;We&rsquo;re grateful for the energy, curiosity, and ownership you brought to the
                            team. We&rsquo;ll be cheering you on.&rdquo;</blockquote>
                        <cite style="font-size: 0.8rem; color: #52525B; font-style: normal;"><strong
                                style="color: #18181B;">Testlify</strong> &mdash; Official company
                            LinkedIn comment, Jan 2026</cite>
                    </div>"""

text = text.replace(card2_old, card2_new)

with open('case-studies/testlify.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated testimonials to WCAG compliant soft yellow.")
