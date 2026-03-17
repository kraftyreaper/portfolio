
import os

new_flow_content = """
                    <div class="card-label" style="text-transform: uppercase; margin-bottom: var(--space-xl);">The complete flow — 6 decision points</div>
                    
                    <div style="position: relative; padding-left: 1rem;">
                        <!-- Vertical connection line -->
                        <div style="position: absolute; left: 25px; top: 16px; bottom: 16px; width: 2px; background: rgba(59, 130, 246, 0.2); z-index: 0;"></div>

                        <!-- Step 1 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; box-shadow: 0 0 0 4px var(--bg-primary);">1</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">ATS Integration</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Connect to 100+ ATS platforms (Greenhouse, Lever, Workable). Designed contextual empty states for each prerequisite blocker — ATS not connected, no jobs available, no candidates synced, job not configured — making each blocker actionable, not just an error.</p>
                            </div>
                        </div>

                        <!-- Step 2 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; box-shadow: 0 0 0 4px var(--bg-primary);">2</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Job Stage Selection</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Dynamic dropdown populated from the connected ATS's actual stage names — eliminating guessing across different ATS naming conventions. Required complex backend integration, but eliminated an entire class of user confusion.</p>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; box-shadow: 0 0 0 4px var(--bg-primary);">3</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Screening Rules</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">AI suggests relevant criteria based on role; employers can add custom requirements or override defaults. The AI assists. The employer decides what matters for their specific hire.</p>
                            </div>
                        </div>

                        <!-- Step 4 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; box-shadow: 0 0 0 4px var(--bg-primary);">4</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Threshold Configuration</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Slider with snap points at 50%, 70%, 90%. Colour-coded zones — red <50%, yellow 50–70%, green >70%. <strong>Trade-off:</strong> Simplified continuous AI scores into discrete buckets. Accepted because employers needed clear decision points, not statistical precision.</p>
                            </div>
                        </div>

                        <!-- Step 5 -->
                        <div style="position: relative; display: flex; gap: 2rem; margin-bottom: 2.5rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; box-shadow: 0 0 0 4px var(--bg-primary);">5</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Batch Processing</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Processes up to 500 resumes per run. Auto-advance toggle is <em>opt-in and off by default</em> — when disabled, all candidates queue for review. Added configuration complexity to give employers the control that high-stakes decisions demand.</p>
                            </div>
                        </div>

                        <!-- Step 6 -->
                        <div style="position: relative; display: flex; gap: 2rem; z-index: 1;">
                            <div style="width: 32px; height: 32px; background: #3b82f6; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; box-shadow: 0 0 0 4px var(--bg-primary);">6</div>
                            <div style="padding-top: 4px;">
                                <h4 style="color: #fff; font-size: 1rem; font-weight: 600; margin-bottom: 0.75rem;">Review & Override</h4>
                                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; margin: 0;">Two rejection paths: Auto-reject (removes from ATS) or Keep for manual review. <strong>Critical guardrail:</strong> Auto-reject carries a persistent, unmissable warning — "Auto-rejected candidates cannot be recovered." Desired by high-volume recruiters; required an irreversibility signal to prevent bulk rejections made under time pressure.</p>
                            </div>
                        </div>
                    </div>
"""

file_path = 'case-studies/testlify.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start of "The Complete 6-Step"
start_idx = -1
for i, line in enumerate(lines):
    if "The Complete 6-Step Flow I Designed" in line or "The complete flow — 6 decision points" in line:
        # Go back a few lines if it's the wrapper etc. 
        # Actually I just want to replace the title and the following steps div.
        start_idx = i
        break

# Find the end of the steps container
# The steps container is after the title, so we look for the next </style> and then the flex div then its end.
# Actually I'll just look for the "Candidate Evaluation Interface" which was step 6.
end_idx = -1
for i in range(start_idx, len(lines)):
    if "Candidate EvaluationInterface" in lines[i] or "Candidate Evaluation Interface" in lines[i] or "Candidate Evaluation\n" in lines[i]:
        # found step 6, now find its closing divs.
        # it was in a flex column div.
        for j in range(i, len(lines)):
            if "</div>" in lines[j] and "</div>" in lines[j+1] and "</div>" in lines[j+2]:
                end_idx = j + 2 # approximate
                break
        if end_idx != -1: break

if start_idx != -1:
    # Let's be more precise about the start by looking for the card-label or h3
    real_start = start_idx
    while real_start > 0 and "<h3" not in lines[real_start] and "<div class=\"card-label\"" not in lines[real_start]:
        real_start -= 1
    
    # And end by finding the closing </div> of the steps container
    real_end = -1
    count = 0
    # The div starts after the title h3/div
    # Let's just find the closing tag of the flex div.
    for i in range(real_start, len(lines)):
        if "display: flex; flex-direction: column;" in lines[i]:
            # This is the container.
            # find its closing div.
            open_divs = 1
            for j in range(i+1, len(lines)):
                open_divs += lines[j].count("<div")
                open_divs -= lines[j].count("</div")
                if open_divs == 0:
                    real_end = j
                    break
            break
            
    if real_start != -1 and real_end != -1:
        new_lines = lines[:real_start] + [new_flow_content] + lines[real_end+1:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Successfully replaced flow section from lines {real_start+1} to {real_end+1}.")
    else:
        print(f"Could not find exact boundaries. Start: {real_start}, End: {real_end}")
else:
    print("Could not find start marker.")
