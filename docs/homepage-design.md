# Full-width homepage

Updated: 2026-10-05

## Research

- [% Arabica](https://arabica.com/en/): observed an edge-to-edge visual hero, minimal overlay navigation and a central brand statement. Applied the image-led opening and restrained copy; the site uses existing Daily TABLE photography.
- [Dandelion Chocolate Japan](https://dandelionchocolate.jp/): inspected desktop and mobile. Its opening photography spans the viewport, followed by separate story regions; mobile keeps the image composition and separates copy. Applied full-width sections and device-specific image/text placement.
- [Aesop](https://www.aesop.com/): official content uses short thematic titles, compact explanations and a primary destination per story. Used as a content hierarchy reference. Visual inspection was blocked by Cloudflare, so no visual-layout claim is based on this source.

## Implementation

The homepage is a refinement of the established cream/green brand, using Impeccable's layout and craft guidance. `assets/css/home.css` is loaded only by the homepage; the shared stylesheet and seven inner pages are unchanged.

1. Full-width product photograph and concise headline. Desktop copy occupies the photograph's open upper-left area. Tablet/mobile place copy below the photograph.
2. Edge-to-edge photo paired with a deep-green brand story panel. Mobile stacks the two regions.
3. Two large photographic links to rituals and guides, with contrast gradients behind copy.

Images remain semantic HTML images with descriptive alt text and dimensions. The lead image is preloaded; lower imagery loads lazily. There is one H1, ordinary crawlable links and the existing homepage metadata/JSON-LD. No new third-party assets, remote fonts or scripts were introduced.

## Verification

- Rendered at 1920×1080, 1440×1000, 1280×720, 768×1024, 390×844 and 320×740.
- All three primary sections span the viewport at every tested width.
- No page overflow, broken images, browser errors or failed local requests; readable minimum 16px for content/controls.
- Mobile navigation, Escape dismissal and the product CTA work.
- Eight-page source checks pass: internal links/anchors, canonical URLs, JSON-LD, sitemap and crawler rules.
- Batched visual review followed by one correction/confirmation pass. Independent desktop/tablet/mobile review found no remaining material layout issue.
- Impeccable detector reported one existing footer padding warning; the footer has a rendered 20px vertical inset and was unchanged.
