const fs = require('fs');

const htmlFiles = [
    'index.html',
    'case-studies/testlify.html',
    'case-studies/milestone.html',
    'case-studies/homes-collection.html',
    'case-studies/gray-institute.html',
    'case-studies/asvi-thoughtworks.html'
];

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    const oldFooterRegex = /<!-- ── Footer ── -->[\s\S]*?<\/footer>/;

    // Adjusting internal padding/margins and changing to a solid subtle divider line
    const newFooter = `<!-- ── Footer ── -->
    <footer class="site-footer reveal">
        <div class="container">
            <div class="site-footer__row-top" style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: var(--space-lg); flex-wrap: wrap; gap: var(--space-xl);">
                <div class="site-footer__content-left" style="text-align: left; max-width: 400px;">
                    <h2 class="site-footer__title" style="margin-bottom: var(--space-sm);">Let's build something great.</h2>
                    <p class="site-footer__text" style="margin: 0;">I'm currently looking for new opportunities. Whether you have a question or just want to say hi, I'll try my best to get back to you!</p>
                </div>
                <div class="site-footer__action-right" style="display: flex; align-items: flex-start;">
                    <a href="https://www.linkedin.com/in/prashantuxuidesign/" target="_blank" rel="noopener noreferrer" class="site-footer__link" style="margin-top: 0;">
                        Say Hello
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="22" y1="2" x2="11" y2="13"></line>
                            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                        </svg>
                    </a>
                </div>
            </div>

            <div style="width: 100%; height: 1px; background-color: var(--border-subtle); margin: 0;"></div>

            <div class="site-footer__row-bottom" style="text-align: center; padding-top: var(--space-lg);">
                <div class="site-footer__copy" style="margin-top: 0;">
                    &copy; 2026 Prashant Ahire. All rights reserved.
                </div>
            </div>
        </div>
    </footer>`;

    if (oldFooterRegex.test(content)) {
        content = content.replace(oldFooterRegex, newFooter);
        fs.writeFileSync(file, content, 'utf8');
        console.log(`Updated ${file}`);
    } else {
        console.log(`Could not find footer in ${file}`);
    }
});
