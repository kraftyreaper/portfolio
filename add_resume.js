const fs = require('fs');
const glob = require('glob'); // Make sure glob is available or just use fs.readdir

const htmlFiles = [
    'case-studies/testlify.html',
    'case-studies/milestone.html',
    'case-studies/homes-collection.html',
    'case-studies/gray-institute.html',
    'case-studies/asvi-thoughtworks.html'
];

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    // Add resume link to nav
    const oldNav = `<nav class="header__nav" id="nav">
                <a href="https://www.linkedin.com/in/prashantuxuidesign/" target="_blank" rel="noopener noreferrer"`;

    const newNav = `<nav class="header__nav" id="nav">
                <a href="../resume.pdf" target="_blank" class="header__link" style="margin-right: var(--space-md);">
                    Resume
                </a>
                <a href="https://www.linkedin.com/in/prashantuxuidesign/" target="_blank" rel="noopener noreferrer"`;

    if (content.includes(oldNav)) {
        content = content.replace(oldNav, newNav);
        fs.writeFileSync(file, content, 'utf8');
        console.log(`Updated ${file}`);
    } else {
        console.log(`Could not find nav in ${file}`);
    }
});
