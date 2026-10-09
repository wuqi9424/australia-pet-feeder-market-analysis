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

Build output: `dist/`. Preview normally uses http://127.0.0.1:4173/. Use HTTP rather than opening the module entry via file://. For a subdirectory deployment use an appropriate base, e.g. `npm run build -- --base=/portfolio/`.

## Structure and sources

Vite plus HTML/CSS/vanilla JS; no runtime framework, backend, database, payment, authentication or analytics. `src/content.js` selects frozen presentation content. `src/main.js` contains semantic sections, menu, screen enlargement and safe bounded Markdown rendering. `src/styles.css` contains responsive layout and visible focus states.

Five app SVGs in `public/assets/app/` are exact copies of five frozen low-fidelity wireframes (Home, Schedule/Edit, Delivery Unconfirmed, Offline, Maintenance). `public/prototype/` copies the complete frozen prototype, with a CSS-only narrow-screen adaptation in its copied HTML; source logic/text and original files are unchanged. It opens in a new tab and simulates conditions, not hardware. The English and Chinese public case studies preserve facts with public-path packaging into `public/case-study/` and rendered in a dialog. Their app-image/prototype links map to website assets; workspace-only source-document links render as source names instead of broken links. No research workspace, raw review corpus or credentials are shipped.

Hero illustration is an abstract concept representation, not final industrial design or hardware specification. No capacity, sensing capability or hardware dimensions are inferred. Concept capabilities, price window and channels remain hypotheses. Metrics are future definitions; tests are unexecuted. Sampled reviews are not representative and relative searches are not sales.

## Status and deployment

Final, frozen website. This directory is the single source of truth for https://australia-pet-feeder.vercel.app.

Vercel is connected to the GitHub repository and builds automatically on every push to `main`: Root Directory `portfolio_website`, Framework Preset Vite, Install `npm ci`, Build `npm run build`, Output `dist`, Node 22.x (22.12+ required by this Vite version). No `vite.config.js`, `vercel.json` or environment variables are needed. Sources, not `node_modules` or `dist`, belong in Git.

No trackers or external fonts. The native dialog provides keyboard dismissal and focus containment. Prototype-copy metadata includes a same-origin favicon reference; the prototype script and product text are unchanged.
