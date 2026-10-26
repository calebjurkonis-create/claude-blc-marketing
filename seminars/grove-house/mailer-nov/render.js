// Render each postcard HTML to a print PDF (9.25 x 6.25 in with bleed) and PNG previews.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const code of ['A', 'B']) {
    const p = await b.newPage({ viewport: { width: 888, height: 600 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.resolve(`postcard-${code}.html`), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: `postcard-${code}.pdf`, width: '9.25in', height: '6.25in', printBackground: true });
    const pages = await p.$$('.page');
    await pages[0].screenshot({ path: `preview-${code}-front.png` });
    await pages[1].screenshot({ path: `preview-${code}-back.png` });
    await p.close();
  }
  await b.close();
})();
