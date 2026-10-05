# Centered full-screen homepage

Updated: 2026-10-05

## Visual research

- [% Arabica](https://arabica.com/en/): inspected a desktop screenshot with an edge-to-edge video, centered brand statement, a single action below it and light navigation over the image. Adopted the central axis, restrained copy and uninterrupted opening photograph. Its single-screen homepage is not a reference for the lower page structure.
- [Bang & Olufsen](https://www.bang-olufsen.com/en/int): inspected the desktop homepage after dismissing the cookie overlay. The lead title, description and button share a horizontal center, positioned toward the lower part of the hero. The video did not render in the research browser, so only the visible text composition informed this work.

These are composition references. The site keeps its own product photography, Chinese typography, cream and green palette, copy and multipage navigation.

## Implementation

Applied Impeccable's layout, typesetting and craft guidance to a continuous, centered homepage:

1. A viewport-height photograph, centered headline, short product specification and single product button. The navigation overlays the image.
2. A centered brand introduction on cream, with a link to the brand story.
3. One full-width lifestyle photograph with centered copy and the rituals link.
4. A short centered guide introduction and link, followed by the existing footer.

The former half-width green panel and pair of image tiles are removed. All four sections share the same center axis. Mobile retains the photographic hero, with phrase-aware title wrapping and an opaque green menu when expanded. With JavaScript disabled, navigation remains visible in normal document flow.

`assets/css/home.css` is homepage-only. The seven inner pages, shared stylesheet and navigation script are unchanged. Existing canonical metadata, JSON-LD, semantic image descriptions and crawlable multipage links remain intact. The lead image is preloaded; the lower image loads lazily. No new remote fonts, scripts or image assets are required.

## Verification

- Six rendered sizes: 1920×1080, 1440×1000, 1280×720, 768×1024, 390×844 and 320×740.
- Checked full-width sections and mathematically centered text groups at every size, one H1, content/control text at least 16px, image loading, page overflow, console errors and failed requests.
- Checked mobile menu opening, Escape dismissal, the product destination and navigation without JavaScript.
- Independent fresh visual review of desktop and mobile prompted corrections to narrow-screen title wrapping, followed by a confirmation pass.
- Eight-page source validation covers links/fragments, independent canonicals/schema, FAQs, six retailer entries, sitemap, llms.txt, robots.txt and removed contact information.
- Impeccable's static detector flagged padding around two full-bleed photographs and the footer. Rendered copy has at least 24px horizontal padding in the photo sections; footer content retains its existing 20px vertical inset. The images intentionally extend to the page edges.
