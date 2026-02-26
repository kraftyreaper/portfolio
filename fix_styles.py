import os
import glob
import re

css_path = "css/styles.css"
with open(css_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if ". c a s e - c a r o u s e l _ _ l i s t" in line or "\x00" in line:
        break
    new_lines.append(line)
        
css_append = """
.case-carousel__list {
    list-style: none;
    padding-left: 0;
    color: var(--text-secondary);
    line-height: 1.6;
    font-size: var(--font-size-md);
    text-align: left;
}
.case-carousel__list li {
    position: relative;
    padding-left: var(--space-xl);
    margin-bottom: var(--space-sm);
}
.case-carousel__list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 10px;
    width: 6px;
    height: 6px;
    background: var(--accent);
    border-radius: 50%;
}
"""

new_lines.append("\n")
new_lines.append(css_append)

with open(css_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

for html_file in glob.glob("case-studies/*.html"):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # The exact string I injected:
    bad_ul = 'style="list-style-position: inside; padding-left: 0; color: var(--text-secondary); line-height: 1.6; font-size: var(--font-size-md);"'
    content = content.replace(bad_ul, 'class="case-carousel__list"')
    
    # And replace li styles:
    bad_li = 'style="margin-bottom: var(--space-sm);"'
    content = content.replace(bad_li, '')
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Success!")
