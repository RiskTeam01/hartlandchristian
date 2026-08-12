# hartlandchristian.com

A rebuild of the Hartland Christian School website as a plain static site.
The previous site was built on Showit, which renders every page as absolutely
positioned elements on a fixed 1200px canvas with a separate mobile canvas.
This version keeps the same content, photography, colours and typography, but
rebuilds the layout as responsive HTML and CSS.

## Serving it

There is no build step at deploy time. Push the repo to any static host
(Netlify, Cloudflare Pages, GitHub Pages, S3, nginx) and point it at the repo
root. URLs use directories, so `/about` resolves to `about/index.html` with no
rewrite rules required.

To preview locally:

```
python3 -m http.server 8000
```

then open <http://localhost:8000>.

## Editing content

Page content lives in `tools/build.py`, not in the HTML files. Each page is a
Python function returning its `<main>` markup, and the shared header, footer and
"Ready to Enroll?" band are defined once at the top. After editing, regenerate:

```
python3 tools/build.py
```

That rewrites the nine `*.html` files plus `sitemap.xml` and `robots.txt`. Commit
the regenerated HTML along with your change — the generated files are tracked so
the site can be served straight from the repo.

Editing an `.html` file by hand works, but the next build overwrites it.

## Layout

```
index.html              home
about/ church/ admissions/ academics/ athletics/ tuition/ contact/
menu/                   plain link list, kept so the old /menu URL still resolves
404.html
assets/css/site.css     design tokens and every section pattern
assets/js/site.js       mobile nav, carousels, statement-of-faith accordion
assets/img/             41 images, downloaded from the previous site
tools/build.py          page content and the generator
```

### Design tokens

Colours and type are declared as custom properties at the top of `site.css` and
match the previous site: Playfair Display for display titles, Cardo for the
wordmark and nav, Fjalla One for section headings and buttons, Montserrat for
body copy, Libre Baskerville for scripture pull-quotes. The accent blues
(`--blue-accent`, `--blue-deep`, `--navy`) are taken from the old per-element
overrides rather than the unused Showit theme defaults.

## What changed from the old site

Structure, wording and imagery were kept as close to the original as possible.
These are the deliberate differences:

- **Responsive layout.** One fluid layout replaces the separate fixed desktop and
  mobile canvases.
- **Real mobile navigation.** The old site linked to a standalone `/menu` page;
  this uses an in-page drawer. `/menu` still exists so the old URL keeps working.
- **Accessibility.** Semantic landmarks, a skip link, visible focus states, alt
  text on all images, labelled carousels and an ARIA accordion. Carousels work
  with arrow keys and touch swipes.
- **Performance.** Images carry `width`/`height` to avoid layout shift and are
  lazy-loaded outside carousels. No jQuery or Showit runtime.
- **SEO.** Per-page titles, meta descriptions, Open Graph tags, a `School`
  JSON-LD block, `sitemap.xml` and `robots.txt`.
- **Email address.** Published as a plain `mailto:` link instead of the old
  Cloudflare obfuscation, so it works without JavaScript.
- **Spelling fixes** in body copy. The originals were: "more then conquerors"
  (→ "than", matching the KJV and the old academics page), "ecompasses"
  (→ "encompasses"), "throughoughly" (→ "thoroughly"), "out students"
  (→ "our students"), "unforseen" (→ "unforeseen"), "HSC competes"
  (→ "HCS"), "on the basis or race" (→ "of race"), "attend our game"
  (→ "our games"), "externally existing" (→ "eternally", matching the about
  page), and "of the Sons" in Matthew 28:19 (→ "of the Son"). Revert any of
  these in `tools/build.py` if the wording was intentional.

## Things worth knowing

- The tuition and handbook links point at OneDrive and Google Docs documents
  owned by the school; the fee amounts were never on the website itself.
- Google Maps embeds and Google Fonts are the only third-party requests.
- The church page intentionally shows its own crest, name and "Est. 1847" in the
  header, as the previous site did, while keeping the shared navigation.
