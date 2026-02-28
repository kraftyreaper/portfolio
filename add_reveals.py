import os
import re

def add_reveal_classes(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add reveal to lifecycle-step if not already present
            new_content = re.sub(r'class="lifecycle-step"', 'class="lifecycle-step reveal"', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

# Targeted update for case-studies folder as well
add_reveal_classes(os.getcwd())
if os.path.exists("case-studies"):
    add_reveal_classes(os.path.join(os.getcwd(), "case-studies"))
