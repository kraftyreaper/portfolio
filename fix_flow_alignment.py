
import os

content = """                    <div class="card-label" style="text-transform: uppercase; margin-bottom: var(--space-xl); text-align: center;">The complete flow — 6 decision points</div>
                    
                    <div style="padding-left: 1rem; position: relative;">
                        <!-- Vertical connection line -->
                        <div style="position: absolute; left: 31px; top: 16px; bottom: 100px; width: 2px; background: rgba(59, 130, 246, 0.2); z-index: 0;"></div>

                        <!-- Step 1 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; position: relative; z-index: 1;">1</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">ATS Integration</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Connect to 100+ ATS platforms (Greenhouse, Lever, Workable). Designed contextual empty states for each prerequisite blocker — ATS not connected, no jobs available, no candidates synced, job not configured — making each blocker actionable, not just an error.</p>
                            </div>
                        </div>

                        <!-- Step 2 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; position: relative; z-index: 1;">2</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Job Stage Selection</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Dynamic dropdown populated from the connected ATS's actual stage names — eliminating guessing across different ATS naming conventions. Required complex backend integration, but eliminated an entire class of user confusion.</p>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; position: relative; z-index: 1;">3</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Screening Rules</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">AI suggests relevant criteria based on role; employers can add custom requirements or override defaults. The AI assists. The employer decides what matters for their specific hire.</p>
                            </div>
                        </div>

                        <!-- Step 4 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; position: relative; z-index: 1;">4</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Threshold Configuration</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Slider with snap points at 50%, 70%, 90%. Colour-coded zones — red <50%, yellow 50–70%, green >70%. <strong>Trade-off:</strong> Simplified continuous AI scores into discrete buckets. Accepted because employers needed clear decision points, not statistical precision.</p>
                            </div>
                        </div>

                        <!-- Step 5 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; position: relative; z-index: 1;">5</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Batch Processing</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Processes up to 500 resumes per run. Auto-advance toggle is <em>opt-in and off by default</em> — when disabled, all candidates queue for review. Added configuration complexity to give employers the control that high-stakes decisions demand.</p>
                            </div>
                        </div>

                        <!-- Step 6 -->
                        <div style="position: relative; display: flex; gap: 2rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; position: relative; z-index: 1;">6</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Review & Override</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Two rejection paths: Auto-reject (removes from ATS) or Keep for manual review. <strong>Critical guardrail:</strong> Auto-reject carries a persistent, unmissable warning — "Auto-rejected candidates cannot be recovered." Desired by high-volume recruiters; required an irreversibility signal to prevent bulk rejections made under time pressure.</p>
                            </div>
                        </div>
                    </div>
"""

file_path = 'case-studies/testlify.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find the region between "The complete flow" and the end of the section content
pattern = re.compile(r'<div class="card-label"[^>]*>The complete flow .*?<!-- Step 6 -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
matches = list(pattern.finditer(text))

if matches:
    # Use the last match as it's the one we just edited
    last_match = matches[-1]
    new_text = text[:last_match.start()] + content + text[last_match.end():]
    
    # Fix the bottom of the line dynamically in the script
    # To end at center of step 6, bottom should be height_of_step6 - 16px.
    # Since I can't know the height, I'll just use the absolute line approach on the whole thing
    # but I'll set bottom: 100px and hope it's not sticking out.
    # Actually, the user screenshot shows circle 6's bottom is roughly the section bottom.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced.")
else:
    print("Pattern not found.")
