#!/usr/bin/env python3
"""Build the static Hartland Christian School site.

Every page shares one header, footer and enrolment call-to-action, so they live
here once instead of being copy-pasted into nine HTML files. Run `python3
tools/build.py` from the repo root after editing; the generated .html files are
committed alongside this script so the site can be served straight from the repo
with no build step required at deploy time.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import handbook as HB  # noqa: E402  (needs the path above)

SCHOOL = "Hartland Christian School"
PHONE_HREF = "tel:+12079384250"
PHONE_TEXT = "(207)938-4250"   # rendered exactly as the original site does
EMAIL = "hartlandchristianschool@outlook.com"
ADDRESS = "10 Elm Street, PO Box 510, Hartland, ME 04943"
FACEBOOK = "https://www.facebook.com/profile.php?id=100057050606588"
MAPS_PLACE = ("https://www.google.com/maps/place/Hartland+First+Baptist+Church/"
              "@44.8822617,-69.4478333,16.97z")
MAPS_EMBED = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2827.022014621018"
              "!2d-69.44743048502782!3d44.88220094329502!2m3!1f0!2f0!3f0!3m2!1i1024!2i768"
              "!4f13.1!3m3!1m2!1s0x4cb1d2363154a539%3A0x553e7b67357e24d5"
              "!2sHartland%20Christian%20School!5e0!3m2!1sen!2sus!4v1709358037382!5m2!1sen!2sus")
HANDBOOK = "https://1drv.ms/w/s!ArPiBpygPm4cvQi3ISYCSYvAxMY7?e=aoIQ02"
TUITION_DOC = "https://1drv.ms/w/s!ArPiBpygPm4cvQoY3XyleWATQG-d?e=ohzFXC"

NAV = [
    ("/", "home"),
    ("/about", "about"),
    ("/church", "church"),
    ("/admissions", "admissions"),
    ("/academics", "academics"),
    ("/athletics", "athletics"),
    ("/tuition", "tuition"),
    ("/contact", "contact"),
]

# --------------------------------------------------------------------- icons
ICON = {
    "burger": '<svg viewBox="0 0 512 512" aria-hidden="true"><path d="M96 241h320v32H96zM96 145h320v32H96zM96 337h320v32H96z"/></svg>',
    "close": '<svg viewBox="0 0 512 512" aria-hidden="true"><path d="M405 136.8L375.2 107 256 226.2 136.8 107 107 136.8 226.2 256 107 375.2l29.8 29.8L256 285.8 375.2 405l29.8-29.8L285.8 256"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.33-.04-1.55-.14-2.84-.14C12 2 10.5 3.66 10.5 6.7v2.8H8v4h2.5V22H14z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2m0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .7-.2 1z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7m0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m6.9 6h-3a15.7 15.7 0 0 0-1.4-3.6A8 8 0 0 1 18.9 8M12 4c.8 1.2 1.4 2.5 1.8 4h-3.6c.4-1.5 1-2.8 1.8-4M4.3 14a8 8 0 0 1 0-4h3.4a16.5 16.5 0 0 0 0 4zm.8 2h3a15.7 15.7 0 0 0 1.4 3.6A8 8 0 0 1 5.1 16m3-8h-3a8 8 0 0 1 4.4-3.6A15.7 15.7 0 0 0 8.1 8M12 20c-.8-1.2-1.4-2.5-1.8-4h3.6c-.4 1.5-1 2.8-1.8 4m2.2-6H9.8a14.7 14.7 0 0 1 0-4h4.4a14.7 14.7 0 0 1 0 4m.3 5.6A15.7 15.7 0 0 0 15.9 16h3a8 8 0 0 1-4.4 3.6m1.8-5.6a16.5 16.5 0 0 0 0-4h3.4a8 8 0 0 1 0 4z"/></svg>',
    "building": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21V7l7-4 7 4v3h4v11zM7 17h2v-2H7zm0-4h2v-2H7zm0-4h2V7H7zm4 8h2v-2h-2zm0-4h2v-2h-2zm0-4h2V7h-2zm8 8h2v-2h-2zm0-4h2v-2h-2z"/></svg>',
    "chevL": '<svg viewBox="0 0 24 48" aria-hidden="true"><path d="M18 4 6 24l12 20"/></svg>',
    "chevR": '<svg viewBox="0 0 24 48" aria-hidden="true"><path d="m6 4 12 20L6 44"/></svg>',
    "plus": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11 5h2v14h-2z"/><path d="M5 11h14v2H5z"/></svg>',
    "cross": '<svg viewBox="0 0 32 40" aria-hidden="true" fill="currentColor"><path d="M13 0h6v10h10v6H19v24h-6V16H3v-6h10z"/></svg>',
    "quote": '<svg viewBox="0 0 32 32" aria-hidden="true" fill="currentColor"><path d="M13 6v8H8c0 4 1 6 4 7l-2 5c-5-2-7-6-7-13V6zm16 0v8h-5c0 4 1 6 4 7l-2 5c-5-2-7-6-7-13V6z"/></svg>',
    "star": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.3-6.2 3.3L7 14.2l-5-4.9 6.9-1z"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 1 21h22zm0 6a1 1 0 0 1 1 1v5a1 1 0 0 1-2 0V9a1 1 0 0 1 1-1m0 9.5a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5"/></svg>',
}


def arrow(dir_):
    return ICON["chevL"] if dir_ == "prev" else ICON["chevR"]


# -------------------------------------------------------------------- layout
LAYOUT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://hartlandchristian.com{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{school}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://hartlandchristian.com{canonical}">
<meta property="og:image" content="https://hartlandchristian.com/assets/img/{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/img/hcs_favicon.png">
<link rel="apple-touch-icon" href="/assets/img/hcs_favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;1,400&amp;family=Fjalla+One&amp;family=Libre+Baskerville:ital@0;1&amp;family=Montserrat:wght@300;400;600&amp;family=Playfair+Display:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
{header}
<main id="main">
{body}
</main>
{footer}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""

JSONLD = """{{"@context":"https://schema.org","@type":"School","name":"Hartland Christian School","alternateName":"HCS","foundingDate":"1980","url":"https://hartlandchristian.com","logo":"https://hartlandchristian.com/assets/img/conquerors_logo.png","email":"{email}","telephone":"+1-207-938-4250","sameAs":["{fb}"],"address":{{"@type":"PostalAddress","streetAddress":"10 Elm Street, PO Box 510","addressLocality":"Hartland","addressRegion":"ME","postalCode":"04943","addressCountry":"US"}},"parentOrganization":{{"@type":"Church","name":"Hartland First Baptist Church","foundingDate":"1847"}}}}"""


def header(active, church=False):
    """Site header. The church page carries its own crest, name and founding
    year, exactly as the previous site did, while keeping the shared nav."""
    if church:
        crest, name, est = "church-crest.png", "Hartland First Baptist Church", "1847"
        crest_alt = "Hartland First Baptist Church crest"
    else:
        crest, name, est = "conquerors_logo.png", SCHOOL, "1980"
        crest_alt = "Hartland Christian School Conquerors crest"

    def items(pairs):
        out = []
        for href, label in pairs:
            cur = ' aria-current="page"' if href == active else ""
            out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        return "".join(out)

    # The original splits the eight links either side of the crest, with the
    # hairlines running from each group out to the edge of the window and
    # breaking around the crest. The wordmark sits underneath the whole row.
    left, right = NAV[:4], NAV[4:]
    name_cls = "brand__name brand__name--church" if church else "brand__name"

    return f"""<header class="site-header">
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{ICON['burger']}</button>
  <nav class="site-nav" id="site-nav" aria-label="Primary">
    <button class="nav-close" type="button" aria-label="Close menu">{ICON['close']}</button>
    <ul class="site-nav__list site-nav__list--left">{items(left)}</ul>
    <a class="brand__crest" href="/">
      <span class="brand__est" aria-hidden="true">Est.</span>
      <img src="/assets/img/{crest}" alt="{crest_alt}" width="60" height="100">
      <span class="brand__est" aria-hidden="true">{est}</span>
      <span class="sr-only">{name}, established {est}</span>
    </a>
    <ul class="site-nav__list site-nav__list--right">{items(right)}</ul>
  </nav>
  <a class="{name_cls}" href="/">{name}</a>
</header>"""


def cta(enroll="/admissions", visit="/contact", ask="/contact"):

    return f"""<section class="section section--navy" aria-labelledby="cta-h">
  <div class="wrap">
    <div class="cta">
      <div>
        <h2 id="cta-h">Ready to Enroll?</h2>
        <p>Is your family ready to become part of our nurturing, academically enriching community at {SCHOOL}? We invite you to take the next step in providing your child with an exceptional education grounded in faith, character, and excellence.</p>
      </div>
      <div class="cta__actions">
        <a class="btn btn--cta" href="{enroll}">get enrollment information</a>
        <a class="btn btn--cta" href="{visit}">schedule a visit</a>
        <a class="btn btn--cta" href="{ask}">questions? contact us</a>
      </div>
    </div>
    <p class="cta__verse">&ldquo;In all these things we are more than conquerors through Him that loved us.&rdquo; &mdash; Romans 8:37 KJV</p>
  </div>
</section>"""


def footer():
    col1 = ["home", "about", "church", "admissions"]
    col2 = ["academics", "athletics", "tuition", "contact"]
    hrefs = dict((label, href) for href, label in NAV)

    def col(items):
        return "<ul>" + "".join(
            f'<li><a href="{hrefs[i]}">{i}</a></li>' for i in items) + "</ul>"

    # Side columns are equal width so the centre column sits on the page's
    # centre line, as it does on the original — which is what the copyright
    # line underneath needs to align with.
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <nav class="footer-nav" aria-label="Footer">
        {col(col1)}
        <span class="footer-nav__rule" aria-hidden="true"></span>
        {col(col2)}
      </nav>
      <span class="footer-rule" aria-hidden="true"></span>
      <div class="footer-main">
        <a class="footer-main__name" href="/">hartland christian school</a>
        <p class="footer-main__bold"><a href="{MAPS_PLACE}" target="_blank" rel="noopener">10 elm street, hartland, me 04943</a></p>
        <p class="footer-main__bold"><a href="{PHONE_HREF}">{PHONE_TEXT}</a></p>
        <p class="footer-main__email"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <span class="footer-rule" aria-hidden="true"></span>
      <div class="footer-aside">
        <img src="/assets/img/conquerors_logo.png" alt="" width="90" height="140" loading="lazy">
        <div class="footer-social">
          <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Hartland Christian School on Facebook">{ICON['facebook']}</a>
          <span class="footer-social__rule" aria-hidden="true"></span>
          <a href="mailto:{EMAIL}" aria-label="Email the school">{ICON['mail']}</a>
          <span class="footer-social__rule" aria-hidden="true"></span>
          <a href="{PHONE_HREF}" aria-label="Call the school">{ICON['phone']}</a>
        </div>
      </div>
    </div>
    <p class="footer-legal">&copy; {{year}} {SCHOOL} &middot; A ministry of Hartland First Baptist Church</p>
  </div>
</footer>"""


def carousel(cid, slides, label, fade=True, dots=True):
    out = [f'<div class="carousel" data-fade="{"true" if fade else "false"}" '
           f'role="group" aria-roledescription="carousel" aria-label="{label}" tabindex="0">']
    out.append(f'<button class="carousel__btn carousel__btn--prev" type="button" aria-label="Previous">{arrow("prev")}</button>')
    out.append('<div class="carousel__viewport"><div class="carousel__track">')
    for i, s in enumerate(slides):
        out.append(f'<div class="carousel__slide" role="group" aria-roledescription="slide" '
                   f'aria-label="{i + 1} of {len(slides)}">{s}</div>')
    out.append("</div></div>")
    out.append(f'<button class="carousel__btn carousel__btn--next" type="button" aria-label="Next">{arrow("next")}</button>')
    if dots:
        out.append('<div class="carousel__dots"></div>')
    out.append("</div>")
    return "\n".join(out)


def sec_head(first, accent, left=False):
    cls = "sec-head sec-head--left" if left else "sec-head"
    return f'<div class="{cls}"><h2>{first} <em>{accent}</em></h2></div>'


# ==========================================================================
#  Page bodies
# ==========================================================================

def home():
    reviews = [
        ("review-sinclair.png", "The Sinclair family", "-the sinclair family",
         "hartland christian school is a very significant part of the lives of my husband and i. "
         "aside from being where we met and started our relationship together, hcs is where i "
         "established a foundation for my life spiritually, professionally, and socially.<br>"
         "Hcs is more than a great school.<br>it is a family and will always hold a very special "
         "place in my heart."),
        ("review-brooks.jpg", "The Brooks family", "-the Brooks family",
         "Hartland Christian School has been a wonderful place for both of our children. The thing "
         "we appreciate the most about HCS, is that the teachers and staff not only care about the "
         "student&rsquo;s academic excellence, but they deeply care for the students on an emotional "
         "and spiritual level. We loved being involved with the sports teams as well as the art and "
         "music programs. HCS is a Christ-centered education and learning environment that we are "
         "very thankful for."),
        ("review-butler.jpg", "The Butler family", "-the Butler family",
         "My family has always been appreciative of Hartland Christian School and the values and "
         "ethics it instilled in us. Both of my children attended Hartland Christian and it gave "
         "them everything they needed fundamentally to move on to college degrees. Olivia is now a "
         "successful RN and Ethan holds a Masters in Accounting and has plans to continue on to get "
         "his CPA. if you are looking for a place to educate your children successfully and instill "
         "in them Godly values, schools don&rsquo;t get much better than HCS."),
        ("review-curtis.jpg", "The Curtis family", "-the curtis family",
         "Having been a part of Hartland Christian School from my early years through graduation, I "
         "can attest to the school&rsquo;s dedication to both academic excellence and spiritual "
         "growth. Hartland not only prepared me for higher education, but also nurtured my values as "
         "a future spouse and active church member. I&rsquo;m confident in recommending Hartland to "
         "others seeking a nurturing environment that fosters both academic growth and spiritual "
         "development."),
    ]
    slides = []
    for img, alt, by, text in reviews:
        slides.append(f"""<div class="review">
  <blockquote class="review__quote">
    <span class="review__mark" aria-hidden="true">&ldquo;</span>
    <p class="review__text">{text}</p>
    <footer class="review__by">{by}</footer>
  </blockquote>
  <div class="review__media"><img src="/assets/img/{img}" alt="{alt}" width="561" height="405"></div>
</div>""")

    cards = [
        ("early-learning.jpg", "/academics#early-learning", "early learning", "Young students at work in an early learning classroom"),
        ("kids.jpg", "/academics#primary-learning", "Primary Education", "Primary grade students at Hartland Christian School"),
        ("chapel.jpg", "/academics#secondary-learning", "Secondary Education", "Students gathered in chapel"),
        ("athletics-card.png", "/athletics", "athletics", "Hartland Christian School Conquerors athletics"),
        ("classroom.jpg", "/tuition", "tuition and fees", "A Hartland Christian School classroom"),
        ("visit.jpg", "/contact", "schedule a visit", "Students outside the school"),
    ]
    card_html = "".join(
        f"""<a class="card" href="{href}">
  <span class="card__media"><img src="/assets/img/{img}" alt="{alt}" loading="lazy" width="287" height="260"></span>
  <span class="card__label">{label}</span>
</a>""" for img, href, label, alt in cards)

    return f"""<section class="hero">
  <img src="/assets/img/church-hero.jpg" alt="Hartland First Baptist Church, home of Hartland Christian School" width="1280" height="808" fetchpriority="high">
</section>

<section class="section section--grey" aria-labelledby="purpose-h">
  <div class="wrap">
    <div class="split">
      <div class="split__media split__media--tall">
        <img src="/assets/img/purpose-bible.jpg" alt="An open Bible" loading="lazy" width="340" height="492">
      </div>
      <div class="split__body prose">
        <div class="sec-head sec-head--left"><h2 id="purpose-h"><span class="tone-deep">our</span> <em>purpose</em></h2></div>
        <p>At {SCHOOL}, our purpose is clear: to provide a nurturing environment where students can grow academically, spiritually, and socially. Grounded in the belief that ALL truth comes from God, we are committed to integrating faith into every aspect of education.</p>
        <p>Our goal is to prepare students for a life centered around Christ, empowering them to reach their full potential in college, careers, and beyond. Through our curriculum, which utilizes the Accelerated Christian Education (ACE) pace system, students receive a comprehensive education from grades 1 through 12. Additionally, we offer extracurricular activities such as sports, art, music and more.</p>
        <p>At {SCHOOL}, we are dedicated to guiding and equipping students for success in all areas of life.</p>
        <p class="mt-2"><a class="btn btn--ghost" href="/about">learn more <span class="arw" aria-hidden="true">&rarr;</span></a></p>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="offer-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="offer-h">what we <em>offer</em></h2></div>
    <div class="cards">{card_html}</div>
  </div>
</section>

<section class="section section--grey" aria-labelledby="reviews-h">
  <div class="wrap">
    <h2 id="reviews-h" class="sr-only">What our families say</h2>
    {carousel("reviews", slides, "Family testimonials")}
  </div>
</section>

{cta(enroll="/admissions", visit="/contact", ask="/contact")}"""


def about():

    pillars = [
        ("pillar-spiritual.jpg", "Spiritual", "Our Christian School cultivates spiritual learning in children through daily scripture study, prayer, and fostering a supportive community grounded in Faith.", "Students in a school hallway"),
        ("church-exterior.jpg", "Academic", "Our Christian School ensures academic growth by offering challenging coursework, innovative teaching methods, and individualized support to foster a love for learning.", "Hartland First Baptist Church"),
        ("pillar-character.jpg", "Character", "Our Christian School promotes the development of strong character in children through teachings of compassion, integrity, and service to others, preparing them to become responsible and resilient individuals.", "An open Bible on a table"),
    ]
    pillar_html = "".join(f"""<li class="pillar">
  <span class="pillar__media"><img src="/assets/img/{img}" alt="{alt}" loading="lazy" width="227" height="180"></span>
  <h3>{title}</h3>
  <span class="pillar__rule" aria-hidden="true"></span>
  <p>{text}</p>
</li>""" for img, title, text, alt in pillars)

    overview = [
        ("Our Mission", "At HCS, we recognize the essential role parents play in shaping their children&rsquo;s spiritual foundation. We complement this parental guidance by fostering an education that molds students into Christ-like leaders. Our curriculum seamlessly weaves faith into academics, character building, and spiritual development to equip students with the skills and values needed for success in an ever-evolving world. Our ultimate purpose is to empower students to positively impact their communities, embodying the teachings of Jesus."),
        ("Our Curriculum", "HCS proudly utilizes the Accelerated Christian Education (ACE) curriculum, trusted since 1970 for its academic excellence and integration of Christian principles. ACE is globally recognized, providing students with a comprehensive education that fosters both academic excellence and spiritual growth. We ensure our students are equipped for success in a supportive Christian environment."),
        ("Our Faculty", "Our faculty is comprised of passionate individuals dedicated to fostering both academic excellence and spiritual growth in our students. Each member of our team is a born-again believer who has committed their life to Christ and to the mission of our school."),
        ("Our Athletics", "At HCS, we offer volleyball for girls and basketball for boys, catering to students in grades 6-12 who meet eligibility criteria. We promote a supportive atmosphere, encouraging good sportsmanship from all attendees. HCS competes with other Christian schools in the ACEL Christian Education league."),
        ("Our Conduct", "Our conduct guidelines are rooted in Christ&rsquo;s teachings, emphasizing love for God and others. Students are expected to show respect, obey rules cheerfully, and use good manners. Further details on conduct expectation can be found in our demerit policy."),
        ("Our Resources", 'For additional information, please consult the '
         '<a class="doc-link" href="/handbook">HCS Handbook 2026-2027</a>.'),
    ]
    ov_html = "".join(f"""<div class="overview__item">
  <h3><span class="pill">{t}</span></h3>
  <p>{b}</p>
</div>""" for t, b in overview)

    return f"""<section class="section section--tight section--photo" style="--bg:url('/assets/img/bg-scripture.jpg');--bg-opacity:.4" aria-labelledby="verse-h">
  <div class="wrap">
    <div class="verse-panel">
      <h2 id="verse-h" class="sr-only">Deuteronomy 6:4-7</h2>
      <div class="rule-mark" aria-hidden="true"><span class="rule-mark__glyph">{ICON['quote']}</span></div>
      <p class="verse-caps verse-caps--lg">hear, o israel: the lord our god is one lord:<br>
      and thou shalt love the lord thy god with all thine heart, and with all thy soul, and with all thy might.<br>
      and these words, which i command thee this day, shall be in thine heart:<br>
      and thou shalt teach them diligently unto thy children, and shalt talk of them when thou sittest in thine house, and when thou walkest by the way, and when thou liest down, and when thou risest up.</p>
      <p class="verse-caps verse-caps--lg verse-caps__ref">- deuteronomy 6:4-7 kjv</p>
    </div>
  </div>
</section>

<section class="section section--gradient" aria-labelledby="about-h">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media">
        <img src="/assets/img/church-about.jpg" alt="Hartland First Baptist Church building" loading="lazy" width="508" height="381">
        <p class="t-quote mt-1">Committed to education and faithfully serving since 1980</p>
      </div>
      <div class="split__body prose">
        <div class="sec-head sec-head--left"><h2 id="about-h">ABOUT <em>HCS</em></h2></div>
        <p>Established in 1980, {SCHOOL} (HCS) has been an integral part of the ministry of First Baptist Church of Hartland, Maine, serving communities for over 43 years. Our core mission is to blend academic excellence with Christian values, providing students with a solid foundation for both their education and spiritual growth.</p>
        <p>At HCS we strive to develop well-rounded individuals who embody Christ-like character and are prepared to lead in various spheres of life. We believe in the importance of partnering with parents, offering an approach that integrates academic learning with biblical principles. Together, we equip students to navigate the challenges of the world while staying rooted in their faith.</p>
      </div>
    </div>

  </div>
</section>

<section class="section" aria-labelledby="mission-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="mission-h">OUR <em>MISSION</em></h2></div>
    <ul class="pillars">{pillar_html}</ul>
  </div>
</section>

<section class="section section--warm" aria-labelledby="overview-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="overview-h">SCHOOL <em>OVERVIEW</em></h2></div>
    <div class="overview">{ov_html}</div>
  </div>
</section>

{cta()}"""


def church():
    missions = [
        ("Our Missions", None, None, None, f"""<div class="verse-card" style="margin-inline:auto">
  <p>&ldquo;Go therefore and make disciples of all the nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, teaching them to observe all things that I have commanded you; I am with you always, even to the end of the age.&rdquo;</p>
  <cite>&mdash;Matthew 28:19-20 KJV</cite>
</div>"""),
    ]
    # Each slide carries a faded photograph of where that family serves, at the
    # opacity the original used - 50% behind the opening verse, 20% behind the
    # rest - so the picture stays scenery and the family stays the subject.
    people = [
        ("The King Family", "mission-king.png", "Dwayne &amp; Kathy King", "Sutton, Alaska", "Kingdom Air Corps", False, "bg-alaska.jpg"),
        ("The Page Family", "mission-page.jpg", "John &amp; Christy Page", "South Africa", "Word of Life", False, "bg-south-africa.jpg"),
        ("The Gbeblewou Family", "mission-gbeblewou.jpg", "Theo &amp; Isabelle Gbeblewou", "West Africa", "Landmark Baptist Missions", False, "bg-west-africa.jpg"),
        ("The Briscoe Family", "mission-briscoe.jpg", "Eric &amp; Diane Briscoe", "Boston, Massachusetts", "Open Air Campaigners", True, "bg-boston.jpg"),
        ("The Steward Family", "mission-steward.jpg", "Curtis &amp; Diane Steward", "South America", "Gospel Mission of South America", False, "bg-south-america.jpg"),
    ]
    slides = [f"""<div class="mission-slide mission-slide--bg" style="--bg:url('/assets/img/bg-missions-map.jpg');--bg-opacity:.5;grid-template-columns:minmax(0,1fr)">
  <h3>Our Missions</h3>
  {missions[0][4]}
</div>"""]
    for name, img, who, where, org, tall, bg in people:
        cls = "mission-slide__media mission-slide__media--tall" if tall else "mission-slide__media"
        slides.append(f"""<div class="mission-slide mission-slide--bg" style="--bg:url('/assets/img/{bg}')">
  <h3>Our Missionaries: {name}</h3>
  <div class="mission-facts">
    <div>{ICON['building']}<span><strong>Name:</strong> {who}</span></div>
    <div>{ICON['pin']}<span><strong>Location:</strong> {where}</span></div>
    <div>{ICON['globe']}<span><strong>Organization:</strong> {org}</span></div>
  </div>
  <div class="{cls}"><img src="/assets/img/{img}" alt="{name}" width="441" height="313"></div>
</div>""")

    others = [
        ("Child Evangelism Fellowship", "India"),
        ("Global Missions South America", "South America"),
        ("Hartland Baptist Missions", "Hermon, Maine"),
        ("Biblical Ministries Worldwide", "Spain"),
    ]
    other_html = "".join(f"<li><h4>{n}</h4><p>&mdash; {p}</p></li>" for n, p in others)
    slides.append(f"""<div class="mission-slide--bg" style="--bg:url('/assets/img/bg-maine.jpg')">
  <h3 class="mission-slide" style="display:block;text-align:center;margin-bottom:2.5rem">Other Missions</h3>
  <ul class="other-missions">{other_html}</ul>
</div>""")

    # The original floats the verse over the photograph in a translucent white
    # card, low and to the right, rather than sitting it underneath.
    return f"""<section class="photo-hero">
  <img src="/assets/img/church-hero.jpg" alt="Hartland First Baptist Church" width="1280" height="808" fetchpriority="high">
  <div class="photo-hero__overlay">
    <div class="wrap">
      <div class="verse-card verse-card--float">
        <p>&ldquo;For God so loved the world, that He gave His only begotten Son, that whosoever believeth in Him should not perish, but have everlasting life.&rdquo;</p>
        <cite>&mdash;John 3:16 KJV</cite>
      </div>
    </div>
  </div>
</section>

<section class="section section--grey" aria-labelledby="welcome-h">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media">
        <img src="/assets/img/pillar-spiritual.jpg" alt="Three crosses against an overcast sky" loading="lazy" width="428" height="328">
      </div>
      <div class="split__body">
        <h2 id="welcome-h" class="t-title" style="text-align:left;color:#000;font-size:clamp(1.9rem,4.4vw,2.9rem)">Welcome to our Church</h2>
        <div class="prose mt-2" style="font-family:'Times New Roman',Times,serif;font-size:1.0625rem;letter-spacing:.02em">
          <p>Welcome to Hartland Baptist Church! We&rsquo;re delighted to have you here. At HBC, our mission is rooted in the greatest commandments: to love God with all our heart, soul, mind, and strength, and to love our neighbors as ourselves. We are a community of believers committed to living out this mission in everything we do.</p>
          <p>Our passion is to go and make disciples, sharing the transformative love of Jesus Christ with all whom we encounter. As we gather together in worship, fellowship, and service, we seek to grow deeper in our faith and reach out to those in need, both locally and globally.</p>
          <p>Join us as we journey together in faith, hope, and love, seeking to glorify God and make a difference in the world.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="banner-split banner-split--photo" style="--bg:url('/assets/img/bg-empowering.jpg')">
  <h2>Empowering Faith, Embracing Community</h2>
</section>

<section class="section" aria-labelledby="services-h">
  <div class="wrap">
    <div class="sec-head sec-head--serif"><h2 id="services-h">Service Times &amp; Location</h2></div>
    <div class="service-grid">
      <div class="map-frame">
        <iframe class="map-embed" src="{MAPS_EMBED}" title="Map to Hartland First Baptist Church" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
      <div class="service-list">
        <div class="service-day">
          <h3>Sunday</h3>
          <ul>
            <li><span class="service-day__name">Sunday School</span><span class="service-day__time">9:30 A.M.</span></li>
            <li><span class="service-day__name">Morning Service</span><span class="service-day__time">10:30 A.M.</span></li>
            <li><span class="service-day__name">Evening Service</span><span class="service-day__time">6:00 P.M.</span></li>
          </ul>
        </div>
        <div class="service-day">
          <h3>Wednesday</h3>
          <ul>
            <li><span class="service-day__name">Prayer Meeting</span><span class="service-day__time">6:30 P.M.</span></li>
          </ul>
        </div>
        <p class="service-note">Classes available for all ages. Nursery is available for children 2 and under.</p>
        <div class="service-address">
          {ICON['pin']}
          <div>
            <h3>Address</h3>
            <address>10 Elm Street, Hartland, ME, 04943</address>
            <a class="service-directions" href="{MAPS_PLACE}" target="_blank" rel="noopener">get directions <span class="arw" aria-hidden="true">&rarr;</span></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--grey" aria-labelledby="missions-h">
  <div class="wrap">
    <h2 id="missions-h" class="sr-only">Our missions</h2>
    {carousel("missions", slides, "Missionaries supported by Hartland First Baptist Church")}
  </div>
</section>"""


def academics():
    faith = [
        'We <strong>believe</strong> that &ldquo;all scripture is given by inspiration of god&rdquo; (2 Timothy 3:16 KJV), by which we understand the whole bible is inspired in the sense that holy men &ldquo;were moved by the holy spirit&rdquo; to write the very words of scripture.',
        'we <strong>believe</strong> that god is one god, eternally existing in three persons &mdash; the father, the son, and the holy spirit &mdash; having precisely the same nature, attributes, and perfections, and worthy of precisely the same homage, confidence and obedience.',
        'we <strong>believe</strong> that the father is perfect in holiness, infinite in wisdom, measureless in power. we rejoice that he concerns himself mercifully in the affairs of men, that he hears and answers prayers, and that he saves from sin and death all who come to him through the lord jesus christ.',
        'we <strong>believe</strong> that, as provided and proposed by, and as preannounced in the prophecies of scriptures, the eternal son of god came into the world that he might manifest god to men, fulfill prophecy, and become the redeemer of a lost world. to this end, he was born of a virgin, received a human body, and a sinless human nature.',
    ]
    faith_html = "".join(f"<li>{f}</li>" for f in faith)

    return f"""<section class="hero">
  <img src="/assets/img/academics-hero.jpg" alt="An empty classroom ready for students" width="1200" height="465" fetchpriority="high">
</section>

<section class="section section--tight" id="title-academics">
  <div class="wrap page-title">
    <h1>academics</h1>
    <div class="rule" aria-hidden="true"></div>
    <p class="text-center" style="max-width:820px;margin-inline:auto">At HCS, we offer a comprehensive educational journey from first grade through 12th grade, guided by the esteemed Accelerated Christian Education (A.C.E.) curriculum. Our goal is to train students in a Christian worldview, equipping them with the tools they need to thrive academically and spiritually.</p>
  </div>
</section>

<section class="band band--navy" id="early-learning" aria-labelledby="early-h">
  <div class="band__media"><img src="/assets/img/early-learning.jpg" alt="Early learning students at work" loading="lazy" width="485" height="601"></div>
  <div class="band__body">
    <h2 id="early-h">Early Learning</h2>
    <div class="band__rule" aria-hidden="true"></div>
    <p class="band__grades">Grades 1-2</p>
    <p>Our early learning journey begins with 1st through 2nd grade at {SCHOOL}. Designed as the foundational years for our young learners, grades 1-2 serve as the cornerstone of their educational experience.</p>
    <p>Rooted in Christian values, our curriculum integrates hands-on learning experiences with teachings about God&rsquo;s love and teachings. We cover essential subjects such as language arts, math, science, and social studies. With dedicated teachers who prioritize individual attention, grades 1-2 set the stage for future success, both academically and spiritually.</p>
  </div>
</section>

<section class="band band--warm band--rev" id="primary-learning" aria-labelledby="primary-h">
  <div class="band__media"><img src="/assets/img/kids.jpg" alt="Primary grade students" loading="lazy" width="485" height="749"></div>
  <div class="band__body">
    <h2 id="primary-h">primary learning</h2>
    <div class="band__rule" aria-hidden="true"></div>
    <p class="band__grades">grades 3-6</p>
    <p>Our primary education program encompasses grades 3-6, where students continue their journey of academic and personal growth. Building upon the foundational skills developed in kindergarten, our elementary curriculum emphasizes both academic excellence and character development.</p>
    <p>In grades 3-6, students engage in a diverse range of subjects including language arts, mathematics, science, social studies, and more. Our curriculum is designed to challenge students intellectually while fostering a love for learning and critical thinking skills.</p>
  </div>
</section>

<section class="band band--navy" id="secondary-learning" aria-labelledby="secondary-h">
  <div class="band__media"><img src="/assets/img/chapel.jpg" alt="Students gathered in chapel" loading="lazy" width="485" height="601"></div>
  <div class="band__body">
    <h2 id="secondary-h">secondary learning</h2>
    <div class="band__rule" aria-hidden="true"></div>
    <p class="band__grades">grades 7-12</p>
    <p>Our secondary education program offers a comprehensive curriculum for students in grades 7-12. Our program emphasizes academic excellence, spiritual growth, and character development, preparing students for success in higher education and beyond. Students engage in a diverse range of subjects including Math, English (Grammar), Literature (Reading), Social Studies, Science (includes Health), and Word Building (Spelling).</p>
    <p>Our secondary program offers three different tracks: Honors Program, College Prep Program, and General Course Program. Each program is tailored to meet the needs and aspirations of our diverse student body.</p>
  </div>
</section>

<section class="section section--grey" aria-labelledby="faith-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="faith-h">STATEMENT OF <em>FAITH</em></h2></div>
    <div class="split">
      <div class="split__media" style="display:grid;place-items:center">
        <img src="/assets/img/conquerors_logo.png" alt="" loading="lazy" width="238" height="373" style="max-height:373px;width:auto;object-fit:contain">
      </div>
      <ul class="creed creed--plain">{faith_html}</ul>
    </div>
  </div>
</section>

{cta()}"""


def admissions():
    steps = [
        ("please read our handbook thoroughly",
         'Before proceeding with enrollment, we encourage all prospective families to thoroughly review our handbook. This document outlines our school policies, procedures, and expectations, ensuring that all parties have a clear understanding of our educational philosophy and community standards. Our handbook can be found <a href="/handbook">here</a>.'),
        ("complete and submit the application form",
         'After reviewing our handbook, the next step is to complete and submit the application form. This form provides us with essential information about the student, their academic history, and their family background, helping us ensure that we can meet the student&rsquo;s educational needs. To obtain our application form, kindly <a href="/contact">contact us</a>.'),
        ("diagnostic testing",
         "As part of our commitment to personalized education, we conduct diagnostic testing to assess each student&rsquo;s academic abilities and identify any areas that may require additional support or enrichment. This testing helps us tailor our instructional approach to meet the unique needs of each student."),
        ("meet with school board",
         "Following the completion of diagnostic testing, prospective families are invited to meet with the school board. This meeting serves as an opportunity for families to learn more about our school&rsquo;s mission, values, and educational programs, as well as to address any questions or concerns they may have."),
        ("submit registration packet",
         "Upon acceptance into our school, families are required to submit a registration packet, which includes various forms and documents, such as emergency contact information, medical records, and transcripts from previous schools attended. These documents help us ensure that we can provide appropriate support and accommodations for each student."),
        ("sign the financial &amp; handbook policy agreement",
         "Before finalizing enrollment, families are asked to review and sign the Financial &amp; Handbook Policy Agreement. This document outlines our tuition and fee schedule, as well as our policies regarding attendance, behavior, and other important matters. By signing this agreement, families commit to upholding our school&rsquo;s policies and meeting their financial obligations."),
        ("probationary period for new students",
         "To ensure our school is the right fit for each student, new enrollees are given a probationary period of 30 days. During this time, we assess the student&rsquo;s academic progress, social integration, and overall attitude and behavior. We look for a positive attitude and a willingness to work, as these qualities are indicative of a student&rsquo;s readiness to thrive in our educational environment."),
    ]
    steps_html = "".join(f"""<li class="step">
  <span class="step__num" aria-hidden="true">{i}</span>
  <div><h3>{t}</h3><p>{b}</p></div>
</li>""" for i, (t, b) in enumerate(steps, 1))

    return f"""<section class="hero">
  <img src="/assets/img/admissions-hero.jpg" alt="Students at Hartland Christian School" width="1200" height="465" fetchpriority="high">
</section>

<section class="section section--tight" id="title-admissions">
  <div class="wrap page-title">
    <h1>admissions</h1>
    <div class="rule" aria-hidden="true"></div>
    <div class="prose mt-2" style="max-width:920px;margin-inline:auto;text-align:center">
      <p>At HCS we embrace diversity and inclusivity as core principles in our admissions process. We value each applicant as an individual and assess them solely based on their academic achievements, without any discrimination on the basis of race, color, sex, or national origin. We believe in creating a welcoming and supportive environment where every student can thrive academically, socially, and spiritually.</p>
      <p>We appreciate your interest in our school, which is dedicated to equipping students to navigate an ever-changing world with a Christian worldview. To begin the enrollment process, please refer to the information below. For further assistance, feel free to <a href="/contact">contact us</a>.</p>
    </div>
  </div>
</section>

<section class="section section--warm" id="how-to-enroll" aria-labelledby="enroll-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="enroll-h">how to <em>enroll</em></h2></div>
    <div class="enroll">
      <div class="enroll__media">
        <img src="/assets/img/enrollment.jpg" alt="A student writing" loading="lazy" width="441" height="1000">
      </div>
      <ol class="steps">{steps_html}</ol>
    </div>
  </div>
</section>

{cta(enroll="#how-to-enroll")}"""


def athletics():
    bball_years = ["bball-year-1.jpg", "bball-year-4.jpg", "bball-year-3.jpg",
                   "bball-year-5.jpg", "bball-year-2.jpg"]
    vball_years = ["vball-year-4.jpg", "vball-year-2.jpg", "vball-year-5.jpg",
                   "vball-year-3.jpg", "vball-year-1.jpg"]

    def team(name, hero, hero_alt, caption, years, label):
        collage = "".join(
            f'<li><img src="/assets/img/{y}" alt="{label} through the years" width="300" height="400"></li>'
            for y in years)
        return [
            f"""<div class="team-slide">
  <h3>{name}</h3>
  <div class="team-slide__media"><img src="/assets/img/{hero}" alt="{hero_alt}" width="1800" height="1286"></div>
  <p class="team-slide__caption">{caption}</p>
</div>""",
            f"""<div class="team-slide">
  <h3>{name}</h3>
  <ul class="collage">{collage}</ul>
  <p class="team-slide__caption">Through the years</p>
</div>""",
        ]

    bball = team("boys basketball", "basketball-team.jpg",
                 "The Hartland Christian School boys basketball team, 2025-2026",
                 "headcoach: Mark Hansen<br>assistant coaches: Ben Clukey, Aaron Lamoreau, Rick Savage",
                 bball_years, "Boys basketball")
    vball = team("girls volleyball", "volleyball-team.jpg",
                 "The Hartland Christian School girls volleyball team, 2025-2026",
                 "headcoach: Rachael Parker<br>assistant coach: Julia Brooks",
                 vball_years, "Girls volleyball")

    return f"""<section class="hero hero--contain" style="background:#fff">
  <div class="wrap" style="padding-block:1.5rem">
    <img src="/assets/img/vball.jpg" alt="The Hartland Conquerors, 2025-2026" width="1800" height="1263" fetchpriority="high" style="margin-inline:auto">
  </div>
</section>

<section class="section section--gradient" id="title-athletics" aria-labelledby="ath-h">
  <div class="wrap">
    <div class="page-title page-title--blue">
      <h1 id="ath-h">ATHLETICS</h1>
      <div class="rule-mark" aria-hidden="true"><span class="rule-mark__glyph">{ICON['quote']}</span></div>
      <p class="verse-caps">in the same way, let your light shine before others, so that they may see your good works and give glory to your father who is in heaven.</p>
      <p class="verse-caps verse-caps__ref">-matthew 5:16</p>
    </div>

    <div class="athletics-lede" style="margin-top:clamp(2.5rem,5vw,3.5rem)">
      <div class="prose">
        <p>At {SCHOOL}, our athletic program is dedicated to fostering physical discipline, promoting good sportsmanship, and nurturing Christian character development. Our school mascot, the Conqueror, symbolizes the virtues of determination, resilience, and triumph &mdash; qualities that align with our faith and values. We believe that through sports, students have the opportunity to embody these traits and grow spiritually.</p>
        <p>Throughout the school year, we offer girls volleyball grades 6-12 and guys basketball for grades 6-12, providing consistent opportunities for both genders to participate and excel in athletics while reinforcing the values of teamwork and dedication. HCS competes with other Christian schools in the ACEL (Athletes for Christian Education League), an athletic league comprising nine private Christian schools.</p>
        <p>We warmly invite students, staff, parents/guardians, friends, and relatives to attend our games with good sportsmanship and encouragement for all teams. Additionally, we welcome parents/guardians to contribute by volunteering in our snack shop, fostering a sense of community and support within our school.</p>
      </div>
      <div class="athletics-lede__media">
        <img src="/assets/img/conquerors-crest.png" alt="The Hartland Christian School Conquerors crest" loading="lazy" width="900" height="1072">
      </div>
    </div>
  </div>
</section>

<section class="section section--grey" aria-labelledby="bball-h">
  <div class="wrap">
    <h2 id="bball-h" class="sr-only">Boys basketball</h2>
    {carousel("bball", bball, "Boys basketball photos")}
  </div>
</section>

<section class="section" aria-labelledby="vball-h">
  <div class="wrap">
    <h2 id="vball-h" class="sr-only">Girls volleyball</h2>
    {carousel("vball", vball, "Girls volleyball photos")}
  </div>
</section>

{cta()}"""


def tuition():
    return f"""<section class="section section--gradient" id="title-tuition" aria-labelledby="tui-h">
  <div class="wrap">
    <div class="page-title page-title--ink">
      <h1 id="tui-h">TUITION &amp; FEES</h1>
      <div class="rule" aria-hidden="true"></div>
    </div>
    <div class="tuition-note prose" style="margin-top:clamp(2rem,4vw,3rem)">
      <p>At {SCHOOL}, we prioritize affordable education without compromising on the quality of our Christian teachings. We place a high value on maintaining a good testimony with our creditors. Therefore we ask that you help us to be able to keep our financial commitments by paying your tuition bills and fees faithfully and in a timely manner. Tuition responsibility is spread over 10 months, from August to May, with statements dispatched in the first week of each month and payment due by month-end. A $25.00 late fee will apply if payments are missed, with final payment expected before the school year concludes.</p>
      <p>We recognize that unforeseen financial difficulties can arise. If you foresee a delay in your payment, please contact the school immediately to discuss arrangements with the board. Failure to communicate regarding missed payments may result in a temporary withdrawal of your child from school until financial stability is regained.</p>
    </div>
    <div class="tuition-actions">
      <a class="btn btn--solid" href="/tuition/fees">tuition &amp; fees information</a>
    </div>
  </div>
</section>

{cta()}"""


def fee_card(title, rows):
    """rows: (label, sublabel|None, amount, subamount|None)"""
    items = []
    for label, sub, amt, subamt in rows:
        name = f"{label}<small>{sub}</small>" if sub else label
        value = f"{amt}<small>{subamt}</small>" if subamt else amt
        items.append(f'<div><span class="fee-name">{name}</span>'
                     f'<span class="fee-amt">{value}</span></div>')
    return f'<div class="fee-card"><h3>{title}</h3><div class="fee-list">{"".join(items)}</div></div>'


def fees():
    """The school's "Financial Information — Grades 1-12" sheet, typeset as a
    page instead of a Word download. Figures transcribed from that document."""
    general = fee_card("General Fees", [
        ("Tuition", None, "$2,600.00", "per student"),
        ("Convention Fee", None, "$250.00", "per student"),
        ("Art Fee", None, "$100.00", "per student"),
        ("Graduation Fee", "12th grade", "$100.00", "per student"),
        ("Hot Lunch Fee", None, "$180.00", "per student"),
    ])
    new_student = fee_card("New Student Fees", [
        ("Academic Testing Fee", "grades 1-12", "$75.00", "per student"),
        ("Registration Fee", "first student", "$150.00", None),
        ("Registration Fee", "each additional student", "$50.00", None),
    ])
    home_school = fee_card("Home School Fees", [
        ("Academic Electives", None, "$150.00", "per student, per semester"),
        ("Arts &amp; Activities", None, "$55.00", "per student, per semester"),
        ("Sports", None, "$150.00", "per student"),
    ])
    late = fee_card("Late Fees", [
        ("Late payment", None, "$25.00", "per billing cycle"),
    ])

    policies = [
        "HCS places a high value on maintaining a good testimony with its creditors. Therefore, we ask that you help us be able to keep our financial commitments by paying your tuition bills and fees faithfully and in a timely manner.",
        "Your tuition obligation will be mailed to you each month over a ten-month period from August to May. Statements will be mailed out on the first week of the month, and the due date will be the end of the month. If the due date is missed, a $25.00 late fee will be added to the next month&rsquo;s statement. Final payment is due prior to the last day of school.",
        "We understand that from time-to-time true financial hardships occur. If you know that your remittance is going to be late, please call the school immediately so that arrangements can be discussed with the school board. If a payment is missed and no contact is made with the school, then you may be asked to withdraw your child from school until such time as you are financially able to resume tuition payments.",
        "Unless prior arrangements have been made, students with unpaid tuition and/or fee balances at the end of a semester may not be allowed to return to HCS the next semester until such time as the balance is paid in full. HCS will not release transcripts until all financial obligations are met. HCS Seniors will not receive diplomas until all financial obligations are met.",
    ]
    policy_html = "".join(f"<p>{p}</p>" for p in policies)

    return f"""<div class="wrap page-back">
  <a class="back-link" href="/tuition#title-tuition"><span class="arw" aria-hidden="true">&larr;</span> back to tuition overview</a>
</div>

<section class="section section--gradient section--tight" aria-labelledby="fees-title">
  <div class="wrap">
    <div class="page-title page-title--ink">
      <h1 id="fees-title">TUITION &amp; FEES</h1>
      <div class="rule" aria-hidden="true"></div>
      <p class="band__grades" style="margin-top:1.25rem;color:var(--blue-deep)">Financial information &middot; Grades 1-12</p>
    </div>
    <div class="letterhead">
      <p>10 Elm Street, Hartland, ME 04943</p>
      <p class="letterhead__contact"><a href="{PHONE_HREF}">{PHONE_TEXT}</a><span class="sep">&nbsp;|&nbsp;</span><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="schedule-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="schedule-h">schedule of <em>fees</em></h2></div>
    <div class="fee-grid">
      {general}
      {new_student}
      {home_school}
      {late}
    </div>

    <div class="stack" style="margin-top:clamp(2rem,4vw,3rem);max-width:940px;margin-inline:auto">
      <div class="callout callout--gold">
        {ICON['star']}
        <div>
          <h3>Discounts</h3>
          <p>If the entire tuition bill (excluding all fees) is paid in full by the first (September 15th) billing cycle, a 10% discount over the entire applicable tuition will be applied.</p>
        </div>
      </div>
      <div class="callout">
        {ICON['alert']}
        <div>
          <h3>Please note</h3>
          <p>Mandatory parent and school board meeting after two or more months delinquency in tuition payments.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--warm" aria-labelledby="policies-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="policies-h">payment <em>policies</em></h2></div>
    <div class="split" style="align-items:start">
      <div class="tuition-crest">
        <img src="/assets/img/conquerors_logo.png" alt="" width="190" height="286" loading="lazy">
      </div>
      <div class="policy-list prose">{policy_html}</div>
    </div>
    <div class="tuition-actions">
      <a class="btn btn--solid" href="/admissions">start the enrollment process</a>
      <a class="btn btn--ghost" href="/contact">ask about tuition</a>
    </div>
  </div>
</section>

{cta()}"""


def handbook_page():
    """The HCS Handbook, typeset as a page with a sticky contents rail."""
    toc = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label, _h, _b in HB.SECTIONS)
    body = "".join(f"""<section class="hb-section" id="{sid}" aria-labelledby="{sid}-h">
  <h2 id="{sid}-h">{heading}</h2>
  {content}
</section>""" for sid, _label, heading, content in HB.SECTIONS)
    staff = "".join(f"<div><dt>{role}</dt><dd>{name}</dd></div>" for role, name in HB.STAFF)

    return f"""<div class="wrap page-back">
  <a class="back-link" id="hb-back" href="/contact"><span class="arw" aria-hidden="true">&larr;</span> <span class="back-link__label">back to contact</span></a>
</div>

<section class="section section--gradient section--tight" aria-labelledby="hb-title">
  <div class="wrap">
    <div class="page-title page-title--ink">
      <h1 id="hb-title">HCS HANDBOOK</h1>
      <div class="rule" aria-hidden="true"></div>
      <p class="band__grades" style="margin-top:1.25rem;color:var(--blue-deep)">{HB.SCHOOL_YEAR}</p>
    </div>
    <div class="letterhead">
      <dl class="hb-staff">{staff}</dl>
      <p>PO Box 510, 10 Elm St., Hartland, ME 04943</p>
      <p class="letterhead__contact"><a href="{PHONE_HREF}">{PHONE_TEXT}</a><span class="sep">&nbsp;|&nbsp;</span><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="hb-revised">{HB.REVISED}</p>
    </div>
  </div>
</section>

<div class="wrap hb-layout">
  <nav class="hb-toc" aria-labelledby="hb-toc-h">
    <h2 id="hb-toc-h">Contents</h2>
    <ol>{toc}</ol>
  </nav>
  <div class="hb-body">
    {body}
  </div>
</div>

{cta()}"""


def contact():
    return f"""<section class="section" id="title-contact" aria-labelledby="con-h">
  <div class="wrap">
    <div class="page-title page-title--serif" style="margin-bottom:clamp(2rem,5vw,3.25rem)">
      <h1 id="con-h">Contact</h1>
      <div class="rule" style="width:min(160px,40%)" aria-hidden="true"></div>
    </div>

    <div class="contact-grid">
      <div class="contact-grid__media">
        <img src="/assets/img/church-exterior.jpg" alt="Hartland First Baptist Church, home of Hartland Christian School" width="555" height="338" fetchpriority="high">
      </div>
      <div class="contact-card">
        <h2>{SCHOOL}</h2>
        <div class="contact-card__rule" aria-hidden="true"></div>
        <div class="contact-list">
          <div class="contact-row">
            {ICON['pin']}
            <div>
              <a href="{MAPS_PLACE}" target="_blank" rel="noopener">
                <address>10 Elm Street PO Box 510<br>Hartland, ME 04943</address>
              </a>
            </div>
          </div>
          <div class="contact-row">
            {ICON['phone']}
            <div>
              <a href="{PHONE_HREF}">{PHONE_TEXT}</a>
              <p class="contact-note">School Administrator &mdash; Kevin Breau</p>
            </div>
          </div>
          <div class="contact-row">
            {ICON['mail']}
            <div><a href="mailto:{EMAIL}">{EMAIL}</a></div>
          </div>
        </div>
        <p class="mt-2" style="font-size:.95rem">For additional information, please consult the <a class="doc-link" href="/handbook">HCS Handbook 2026-2027</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" style="background:#e9e9ec">
  <div class="wrap">
    <h2 class="sr-only">Find us</h2>
    <iframe class="map-embed" src="{MAPS_EMBED}" title="Map to Hartland Christian School" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  </div>
</section>"""


def menu():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    return f"""<section class="menu-page">
  <div class="wrap text-center">
    <img src="/assets/img/conquerors_logo.png" alt="Hartland Christian School Conquerors crest" width="60" height="90">
    <h1 class="t-eyebrow" style="font-size:1.1rem">menu</h1>
    <ul class="mt-2">{links}</ul>
  </div>
</section>"""


def not_found():
    return f"""<section class="menu-page">
  <div class="wrap text-center">
    <img src="/assets/img/conquerors_logo.png" alt="" width="60" height="90">
    <h1 class="t-title" style="font-size:clamp(1.75rem,4vw,2.75rem)">Page not found</h1>
    <p class="mt-2">We couldn&rsquo;t find that page. Try one of these instead:</p>
    <ul class="mt-2">{"".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)}</ul>
  </div>
</section>"""


# ==========================================================================
PAGES = [
    ("index.html", "/", "Home", f"{SCHOOL} | Christian education in Hartland, Maine",
     "A Christ-centered K-12 education in Hartland, Maine. Established 1980, a ministry of Hartland First Baptist Church.",
     "church-hero.jpg", home, False),
    ("about/index.html", "/about", "About", f"About | {SCHOOL}",
     "Established in 1980 as a ministry of First Baptist Church of Hartland, Maine — our mission, faculty, curriculum and statement of faith.",
     "church-about.jpg", about, False),
    ("church/index.html", "/church", "Church", "Hartland First Baptist Church",
     "Service times, location and the missionaries supported by Hartland First Baptist Church in Hartland, Maine.",
     "church-hero.jpg", church, True),
    ("admissions/index.html", "/admissions", "Admissions", f"Admissions | {SCHOOL}",
     "How to enroll at Hartland Christian School — our seven-step admissions process, from handbook to registration.",
     "admissions-hero.jpg", admissions, False),
    ("academics/index.html", "/academics", "Academics", f"Academics | {SCHOOL}",
     "Grades 1-12 taught through the Accelerated Christian Education (A.C.E.) curriculum: early, primary and secondary learning.",
     "academics-hero.jpg", academics, False),
    ("athletics/index.html", "/athletics", "Athletics", f"Athletics | {SCHOOL}",
     "Conquerors athletics — girls volleyball and boys basketball for grades 6-12, competing in the ACEL league.",
     "vball.jpg", athletics, False),
    ("tuition/index.html", "/tuition", "Tuition", f"Tuition & Fees | {SCHOOL}",
     "Affordable Christian education: how tuition is scheduled across the school year, and where to find the fee schedule.",
     "classroom.jpg", tuition, False),
    ("tuition/fees/index.html", "/tuition/fees", "Fees", f"Tuition & Fee Schedule | {SCHOOL}",
     "The full Hartland Christian School fee schedule for grades 1-12: tuition, general, new-student and home-school fees, discounts and payment policies.",
     "classroom.jpg", fees, False, "/tuition"),
    ("contact/index.html", "/contact", "Contact", f"Contact | {SCHOOL}",
     "Visit, call or email Hartland Christian School at 10 Elm Street, Hartland, Maine 04943.",
     "church-exterior.jpg", contact, False),
    ("handbook/index.html", "/handbook", "Handbook", f"HCS Handbook {HB.SCHOOL_YEAR} | {SCHOOL}",
     f"The Hartland Christian School handbook for {HB.SCHOOL_YEAR}: admissions, attendance, curriculum, daily procedures, conduct, personal appearance, fees and reconciliation.",
     "classroom.jpg", handbook_page, False, "/about"),
    ("menu/index.html", "/menu", "Menu", f"Menu | {SCHOOL}",
     "Site menu for Hartland Christian School.",
     "church-hero.jpg", menu, False),
    ("404.html", "/404", "404", f"Page not found | {SCHOOL}",
     "That page could not be found.",
     "church-hero.jpg", not_found, False),
]


def build():
    jsonld = JSONLD.format(email=EMAIL, fb=FACEBOOK)
    foot = footer().replace("{year}", "2026")
    written = []
    for entry in PAGES:
        path, url, _label, title, desc, og, fn, is_church = entry[:8]
        # a sub-page can light up its parent's nav item
        nav_active = entry[8] if len(entry) > 8 else url
        html = LAYOUT.format(
            title=title, description=desc, canonical=url, school=SCHOOL, og=og,
            jsonld=jsonld, header=header(nav_active, church=is_church), body=fn(), footer=foot,
        )
        dest = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(html)
        written.append(path)

    # sitemap
    urls = "".join(
        f"<url><loc>https://hartlandchristian.com{u}</loc></url>"
        for e in PAGES for u in [e[1]] if u not in ("/menu", "/404"))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                + urls + "</urlset>\n")

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: https://hartlandchristian.com/sitemap.xml\n")

    print("built:")
    for w in written:
        print("  ", w)
    print("   sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
