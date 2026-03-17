import re

with open('case-studies/testlify.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the section 'IMPACT AT A GLANCE'
pattern = r'(<!-- ── IMPACT AT A GLANCE ── -->.*?<\/section>)'
match = re.search(pattern, text, flags=re.DOTALL)
if match:
    section_content = match.group(1)
    
    # Replace the style for the cards
    new_section_content = section_content.replace('style="margin: 0; text-align: left;"', 'style="margin: 0; text-align: left; padding: 2rem;"')
    
    # Write back
    text = text.replace(section_content, new_section_content)
    with open('case-studies/testlify.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Replaced inline style successfully!')
else:
    print('Section not found')
