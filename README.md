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
tuition/fees/           the fee schedule, typeset from the school's Word document
handbook/               the HCS Handbook 2026-2027, typeset from the school's Word document
menu/                   plain link list, kept so the old /menu URL still resolves
404.html
assets/css/site.css     design tokens and every section pattern
assets/js/site.js       mobile nav, carousels, accordion, handbook search
assets/img/             41 images, downloaded from the previous site
tools/build.py          page content and the generator
tools/handbook.py       handbook content, kept apart so build.py stays readable
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
- **Romans 8:37** is set in normal capitalisation with "Him" capitalised, and
  reads "more than conquerors" on every page. The old site wrote "then" on all
  pages except academics; that was corrected at the school's request.
- **Spelling and grammar corrected** across the site at the school's request.
  Twelve fixes, all in copy inherited from the old site: "ecompasses",
  "throughoughly", "unforseen", "out students", "HSC competes", "on the basis or
  race", "attend our game", "externally existing", "of the Sons" in Matthew
  28:19, "Join us as journey together", "grades 1-2 serves", and a missing "and"
  in the academics statement of faith.

### Two deliberate deviations

Everything else matches the source. These two do not, for stated reasons:

1. **Email address.** The original hides it behind Cloudflare's JavaScript
   obfuscation, which renders as "[email protected]" without scripting. The
   rebuild prints `hartlandchristianschool@outlook.com` as a plain `mailto:`
   link, which is what a visitor to the original actually ends up seeing.
2. **The tuition message form.** Visually reproduced ("let's do this.", a
   message box, SUBMIT, and the same thank-you state). The original posted to
   Showit's contact-form service, which stops existing once the site leaves
   Showit, so submitting now opens the sender's mail client addressed to the
   school. Swap `initForm()` in `assets/js/site.js` for a real form handler
   (Netlify Forms, Formspree, etc.) when one is available. Its heading is set
   in white rather than the original's dark green, which was near-illegible on
   the navy band.

## Keeping tuition current

`/tuition/fees` replaces the Word document the tuition button used to open. The
figures are transcribed from the school's "Financial Information — Grades 1-12"
sheet and **are a snapshot that will go stale**. When fees change, edit the
`fee_card(...)` calls in the `fees()` function in `tools/build.py` — one row per
line — and rebuild.

The source document is still at `TUITION_DOC` in `tools/build.py` for reference.
Its letterhead lists an out-of-date `@roadrunner.com` address; the site uses the
current `@outlook.com` one throughout.

`/handbook` is the same idea for the student handbook. Its content lives in
`tools/handbook.py` as one `SECTIONS` list — each entry becomes a section and a
contents-rail entry, so adding, editing or reordering a section is a local
change. When the school issues a new handbook, update that file and bump
`SCHOOL_YEAR` and `REVISED` at the top.

The handbook page carries a search box that indexes each section's text in the
browser on load — no build step and no service to keep running. It matches the
whole phrase first, falling back to sections containing every word typed, and
lists the section, its hit count and the surrounding sentence. Sections are
indexed straight from the rendered DOM, so new sections are searchable with no
extra work.

## Things worth knowing

- The tuition and handbook links point at OneDrive and Google Docs documents
  owned by the school; the fee amounts were never on the website itself.
- Google Maps embeds and Google Fonts are the only third-party requests.
- The church page intentionally shows its own crest, name and "Est. 1847" in the
  header, as the previous site did, while keeping the shared navigation.
