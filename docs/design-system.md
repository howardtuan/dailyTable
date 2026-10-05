# Website layout and typography

Updated: 2026-10-05

## Design reference

Applied [Impeccable](https://github.com/pbakaus/impeccable), version 4.5.0, installed locally with Codex's skill installer. The typography, layout, distill and craft-floor guidance informed this refinement. The established cream/deep-green identity, Chinese serif headings and owned product photography remain the visual authority.

## Reading hierarchy

- Body: 18px desktop/tablet, 17px mobile; approximately 1.85 line height.
- Navigation, buttons and tables: 16px. Metadata: 14px minimum.
- Section headings: 30–40px; article section headings: 26–30px.
- Main content: at most 1200px wide; article body: at most 760px.
- Mobile gutters: 20px. Major sections: 88px desktop, 64px tablet, 48px mobile.
- Native/system font fallback remains, with no blocking remote font request.

## Content and page roles

All eight URLs remain independent static pages. The homepage introduces the product and leads to dedicated pages. Product information appears once in the product summary; FAQ holds practical brewing, baking and storage answers. The brand page presents a short story, rituals gives three uses, and guides prioritize reading. The purchase page presents six verified retailer destinations with logos and explicit availability states.

Removed repeated promises, duplicate summaries, decorative English labels, non-sequential numbers, repeated purchase invitations and the oversized footer. FAQ structured data follows visible questions. No hidden keyword copy, telephone or contact form was added.

## Verification

- Eight pages × four widths: 1440, 768, 390 and 320px.
- Desktop/mobile full-page visual inspection, followed by one correction and confirmation batch.
- Single H1, unique IDs, canonical/JSON-LD consistency, internal links/fragments, sitemap and crawler rules.
- Mobile menu, Escape dismissal, FAQ toggles, legacy links and navigation without JavaScript.
- No horizontal page overflow, broken images, browser errors or failed local requests.
- Text contrast: primary 11.34:1; secondary on paper 5.39:1, on sage 4.93:1; white on green 9.79:1.
- Impeccable detector reported 19 cramped-padding warnings. Rendered review found these to be static-analysis limitations around logical padding, CSS variables and padded descendants; actual insets and separation were verified.

Search visibility and AI citation are indexing outcomes; layout verification does not establish search ranking.
