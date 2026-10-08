# Local-first Feeding — Interactive PM Portfolio

One-page responsive portfolio concept, based on frozen research and product-design work. Not a commercial brand, a purchasable product or evidence of a launch. No hardware validation, usability testing or PMF claim.

## Local development

```sh
cd portfolio_website
npm install
npm run dev
```

Open Vite's printed URL, normally http://127.0.0.1:5173/.

## Static build and preview

```sh
npm run build
npm run preview
```

Build output: `dist/`. Preview normally uses http://127.0.0.1:4173/. Use HTTP rather than opening the module entry via file://. For a subdirectory deployment use an appropriate base, e.g. `npm run build -- --base=/portfolio/`. No deployment or Git push is performed.

## Structure and sources

Vite plus HTML/CSS/vanilla JS; no runtime framework, backend, database, payment, authentication or analytics. `src/content.js` selects frozen presentation content. `src/main.js` contains semantic sections, menu, screen enlargement and safe bounded Markdown rendering. `src/styles.css` contains responsive layout and visible focus states.

Five app SVGs in `public/assets/app/` are exact copies of Phase9D WF01/WF03/WF05/WF06/WF08. `public/prototype/` copies the complete frozen prototype, with a CSS-only narrow-screen adaptation in its copied HTML; source logic/text and original files are unchanged. It opens in a new tab and simulates conditions, not hardware. English/Chinese public Phase9F case studies preserve facts with public-path packaging into `public/case-study/` and rendered in a dialog. Their app-image/prototype links map to website assets; workspace-only source-document links render as source names instead of broken links. No research workspace, raw review corpus or credentials are shipped.

Hero illustration is an abstract concept representation, not final industrial design or hardware specification. No capacity, sensing capability or hardware dimensions are inferred. Concept capabilities, price window and channels remain hypotheses. Metrics are future definitions; tests are unexecuted. Sampled reviews are not representative and relative searches are not sales.

## Readiness

Prepared for local visual review and separately authorized static deployment. Internal QA reports remain outside this public website. No trackers or external fonts. Native dialog provides keyboard dismissal and focus containment. Browser checks validate presentation functionality, not product usability. Modern browsers required. Only public portfolio content is shipped.

Prototype-copy metadata includes a same-origin favicon reference to avoid a missing icon request; the prototype script and product text remain unchanged.

## Vercel deployment (manual, pending)

Import the existing australia-pet-feeder-market-analysis GitHub repository. Set Root Directory to portfolio_website, Framework Preset to Vite, Install Command to npm ci, Build Command to npm run build, Output Directory to dist. Use Node 22.x (22.12+ required by this Vite version). Root base is /, the default; no vite.config.js or vercel.json is needed for this one-page hash-navigation site. No SPA route rewrite required.

PORTFOLIO_URL_PENDING. Publish only after explicit authorization; configure the real URL and recheck HTTPS, mobile, cases and prototype. No canonical/og:url is invented before deployment. No environment variables required. Sources, not node_modules or dist, belong in Git.
