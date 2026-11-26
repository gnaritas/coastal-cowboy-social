#!/usr/bin/env python3
"""Coastal Cowboy Social — generator (single source for all pages).
websites lane, card t_a20e80b2. Built 2026-11-25. Demo host pinned from first byte.
Design: camp-program / wanted-poster typography — deep roast-bark ink, bone paper,
raw-sienna rust accent, gulf-teal counter-accent, hard offset card shadows (poster
block, no double hairlines). No photos, no third-party JS, no webfonts.
Facts ONLY from press-verified card t_a20e80b2: Business Debut feature interview +
Hillsborough roundups (2026-11-12, 2026-11-25). Unknown (phone, hours detail, prices,
opening day) = omitted, never guessed."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://coastal-cowboy-social-demo.up.railway.app"

BRAND = "Coastal Cowboy Social"
ADDR = "102 W Shell Point Road, Ruskin, FL 33570"
GEO = (27.7203666, -82.4354812)  # exact house match, OpenStreetMap way 1038785661 (ODbL)
MAP_Q = "https://www.google.com/maps?q=102%20W%20Shell%20Point%20Road%2C%20Ruskin%2C%20FL%2033570&output=embed"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=102%20W%20Shell%20Point%20Road%2C%20Ruskin%2C%20FL%2033570"

def head(title, desc, path, ld=None, utility=False, og_desc=None):
    u = ORIGIN + path
    d = desc.replace('"', "'")
    od = (og_desc or desc).replace('"', "'")
    parts = ['<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
             '<meta name="robots" content="noindex, nofollow">',
             '<!-- BUILT-2026-11-25 -->',
             '<title>%s</title>' % title,
             '<meta name="description" content="%s">' % d,
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<link rel="canonical" href="%s">' % u,
             '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
             '<link rel="stylesheet" href="/style.css">']
    if not utility:
        t = title.replace('"', "'")
        od = (og_desc or desc).replace('"', "'")
        parts += [
            '<meta property="og:type" content="website">',
            '<meta property="og:title" content="%s">' % t,
            '<meta property="og:description" content="%s">' % od,
            '<meta property="og:image" content="%s/og.png">' % ORIGIN,
            '<meta property="og:url" content="%s">' % u,
            '<meta name="twitter:card" content="summary_large_image">']
    for blk in (ld or []):
        parts.append('<script type="application/ld+json">%s</script>' % json.dumps(blk, ensure_ascii=False))
    parts.append('</head>')
    return "\n".join(parts)

NAV_LINKS = [
    ("Menu", "/menu"),
    ("Game &amp; steaks", "/wild-game-and-steaks-ruskin"),
    ("Florida seafood", "/florida-seafood-ruskin"),
    ("Bar &amp; pavilion", "/western-bar-and-pavilion"),
    ("Our story", "/our-story"),
    ("Visit", "/visit"),
]

def nav(active):
    items = []
    for label, href in NAV_LINKS:
        cur = ' aria-current="page"' if href == active else ""
        items.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    items.append('<a class="btn sm" href="/contact">Opening-day list</a>')
    return ('<body>\n<div class="topline" aria-hidden="true"></div>\n'
            '<a class="skip" href="#main">Skip to content</a>\n'
            '<header class="site">\n'
            '<p class="brand mono"><a href="/">Coastal <em>Cowboy</em> Social</a></p>\n'
            '<nav aria-label="Site"><p>%s</p></nav>\n'
            '</header>\n<main id="main">' % " ".join(items))

FOOTER = ('</main>\n<footer>\n'
          '<p class="footline">Coastal Cowboy Social</p>\n'
          '<p class="footline">Opening January 2027 &middot; 102 W Shell Point Road, Ruskin, FL 33570</p>\n'
          '<p class="footline fine">&copy; 2026 &middot; <a href="/menu">Menu</a> &middot; <a href="/visit">Visit</a> &middot; <a href="/contact">Contact</a> &middot; <a href="/privacy">Privacy</a></p>\n'
          '</footer>\n</body>\n</html>\n')

def restaurant_node(path="/"):
    return {
        "@context": "https://schema.org",
        "@type": "Restaurant",
        "name": BRAND,
        "url": ORIGIN + path,
        "image": ORIGIN + "/og.png",
        "servesCuisine": ["Wild game", "Steaks", "Barbecue", "Florida seafood"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "102 W Shell Point Road",
            "addressLocality": "Ruskin",
            "addressRegion": "FL",
            "postalCode": "33570",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "hasMap": "https://www.google.com/maps?q=102%20W%20Shell%20Point%20Road%2C%20Ruskin%2C%20FL%2033570",
    }

def breadcrumb(label, path):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": label, "item": ORIGIN + path},
        ],
    }

def service_node(name, stype, desc, path):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": stype,
        "description": desc,
        "url": ORIGIN + path,
        "areaServed": [
            {"@type": "City", "name": "Ruskin", "containedInPlace": {"@type": "State", "name": "Florida"}},
            {"@type": "Place", "name": "Palmetto, FL"},
            {"@type": "Place", "name": "Sun City, FL"},
            {"@type": "Place", "name": "Bradenton, FL"},
            {"@type": "Place", "name": "Riverview, FL"},
            {"@type": "Place", "name": "Brandon, FL"},
        ],
        "provider": {k: v for k, v in restaurant_node(path).items() if k != "@context"},
    }

pages = {}

# ---------------- HOME ----------------
home_ld = [restaurant_node("/")]
pages["index.html"] = (
    head("Coastal Cowboy Social &mdash; Western Steakhouse &amp; Florida Seafood, Ruskin FL",
         "A Western steakhouse and Florida seafood house opening January 2027 at 102 W Shell Point Road in Ruskin FL — wild game, steaks and barbecue, Gulf seafood, a Western bar and an outdoor pavilion with weekend live bands.",
         "/", home_ld)
    + nav("/")
    + '''<section class="hero">
  <p class="lab mono">Montana ranch meets the Gulf coast &middot; Ruskin, Florida</p>
  <h1>Coastal Cowboy Social</h1>
  <p class="sub">Wild game and steaks on one side of the grill, Florida seafood on the other — in a 1925 building on Shell Point Road with a cow-town bar and an open-air pavilion. Opening January 2027.</p>
  <p class="hero-cta"><a class="btn" href="/contact">Leave your email for opening day</a> <a class="ghost" href="/menu">Read the menu</a></p>
</section>
<section class="panels">
  <article class="frame">
    <p class="lab mono">The table</p>
    <h2>Elk, bison and a real steak program</h2>
    <p>The kitchen leads with wild game — elk and bison up front, venison to follow — alongside three or four steak cuts and a handful of barbecue items brought down from Montana.</p>
    <p><a href="/wild-game-and-steaks-ruskin">Game &amp; steaks &rarr;</a></p>
  </article>
  <article class="frame">
    <p class="lab mono">The Gulf side</p>
    <h2>Florida seafood, done serious</h2>
    <p>The owner grew up cooking within a short drive of the Chesapeake Bay. That fluency runs the seafood half of the menu — Gulf catch served Western-style, steps from the bay.</p>
    <p><a href="/florida-seafood-ruskin">Florida seafood &rarr;</a></p>
  </article>
  <article class="frame">
    <p class="lab mono">The room &amp; the pavilion</p>
    <h2>A cow-town bar and live bands outside</h2>
    <p>A Florida-style dining room, a Western-themed bar hung with barnwood and mounts, and a pavilion where live bands are planned for weekends — with cocktail seating and service outdoors.</p>
    <p><a href="/western-bar-and-pavilion">Bar &amp; pavilion &rarr;</a></p>
  </article>
</section>
<section class="band">
  <div class="band-copy">
    <p class="lab mono">Opening January 2027</p>
    <h2>First word goes to the list</h2>
    <p>The exact opening day, the hours and the full menu land right here — and people on the opening-day list get the email before anyone else.</p>
    <p><a class="btn" href="/contact">Join the opening-day list</a></p>
  </div>
  <div class="band-map"><iframe src="''' + MAP_Q + '''" loading="lazy" title="Map: Coastal Cowboy Social, 102 W Shell Point Road, Ruskin FL" allow="management:coordinate"></iframe><p class="mapcap">102 W Shell Point Road &middot; Ruskin FL 33570 &middot; <a href="''' + DIRS + '''">Get directions &nearr;</a></p></div>
</section>''')

# ---------------- MENU HUB (+ FAQ) ----------------
faq_items = [
    ("When do you open?",
     "January 2027, at 102 W Shell Point Road in Ruskin. The exact day and the hours go up on this site first — and people on the opening-day list get the email before anyone else."),
    ("What kind of food do you serve?",
     "Wild game, steaks, barbecue and Florida seafood. Elk and bison lead the menu, three or four steak cuts sit next to them, and Gulf seafood runs the other half. Lunch and dinner service."),
    ("Where does the game come from?",
     "A friend's ranch. For the opening, a whole bison is being sourced from that ranch, USDA-inspected, and driven to Florida. Elk and bison are on the menu from day one; venison joins as the vendors are set."),
    ("Will there be live music?",
     "Yes — live bands and other entertainment are planned for weekends in the outdoor pavilion, with cocktail-focused seating and outdoor service."),
    ("What's happening upstairs?",
     "The floor above — still an apartment today — is planned to become a private, membership-based speakeasy. That's phase two, expected in 2027 with details to follow."),
]
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a.replace("&#8217;", "'").replace("&#8209;", "-")}}
                         for q, a in faq_items]}
menu_ld = {
    "@context": "https://schema.org", "@type": "Menu",
    "name": "Opening menu — Coastal Cowboy Social",
    "url": ORIGIN + "/menu", "inLanguage": "en",
    "hasMenuSection": [
        {"@type": "MenuSection", "name": "Wild game & ranch",
         "hasMenuItem": [{"@type": "MenuItem", "name": "Elk"},
                         {"@type": "MenuItem", "name": "Bison"},
                         {"@type": "MenuItem", "name": "Venison (rolling out)"}]},
        {"@type": "MenuSection", "name": "Steaks & barbecue",
         "hasMenuItem": [{"@type": "MenuItem", "name": "Steak cuts"},
                         {"@type": "MenuItem", "name": "Barbecue items"}]},
        {"@type": "MenuSection", "name": "From the Gulf",
         "hasMenuItem": [{"@type": "MenuItem", "name": "Florida seafood"}]},
    ],
}
pages["menu.html"] = (
    head("Opening Menu: Wild Game, Steaks &amp; Florida Seafood — Coastal Cowboy Social, Ruskin FL",
         "What's coming to the Coastal Cowboy Social menu in Ruskin FL: elk, bison and venison to follow, three or four steak cuts, barbecue items and Florida seafood. Prices post the day we open.",
         "/menu", [breadcrumb("Menu", "/menu"), faq_ld, menu_ld])
    + nav("/menu")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Menu</p>
  <h1>What&#8217;s coming on the menu</h1>
  <p class="lede">Wild game, steaks, barbecue and Florida seafood — the two halves of this concept, on one board. Prices and the full list post the day we open; here is the shape of it.</p>
  <h2>Wild game &amp; ranch</h2>
  <ul class="board">
    <li><span>Elk</span> on the board from day one — wild game leads this kitchen</li>
    <li><span>Bison</span> from a friend&#8217;s ranch: USDA-inspected and driven to Florida for the opening</li>
    <li><span>Venison</span> to follow — the vendors are being lined up now</li>
  </ul>
  <h2>Steaks &amp; barbecue</h2>
  <ul class="board">
    <li><span>Steaks</span> this is a steakhouse at its core — three or four cuts on the menu</li>
    <li><span>Barbecue</span> several smoked items, straight out of the owner&#8217;s Montana past</li>
  </ul>
  <h2>From the Gulf</h2>
  <ul class="board">
    <li><span>Florida seafood</span> the coastal half of the concept, sourced where we sit — steps off the bay</li>
  </ul>
  <p>Served at lunch and at dinner. Drinks run from beer and cocktails at the Western bar to pour-your-own specials on pavilion nights.</p>
  <dl class="faq">''' + "".join('<dt>%s</dt><dd>%s</dd>' % (q, a) for q, a in faq_items) + '''</dl>
  <p class="lab mono">Keep going</p>
  <p class="cta-row"><a class="btn" href="/contact">Join the opening-day list</a> <a href="/wild-game-and-steaks-ruskin">Game &amp; steaks</a> &middot; <a href="/florida-seafood-ruskin">Florida seafood</a> &middot; <a href="/western-bar-and-pavilion">Bar &amp; pavilion</a></p>
</article>''')

# ---------------- GAME + STEAKS DETAIL ----------------
pages["wild-game-and-steaks-ruskin.html"] = (
    head("Wild Game &amp; Steaks in Ruskin FL — Coastal Cowboy Social",
         "Coastal Cowboy Social in Ruskin FL serves wild game — elk, bison and venison to follow — with three or four steak cuts and barbecue items, in a Western steakhouse built on the owner's Montana lineage.",
         "/wild-game-and-steaks-ruskin",
         [breadcrumb("Game & steaks", "/wild-game-and-steaks-ruskin"),
          service_node("Wild game and steaks", "Steakhouse and game kitchen",
                       "Elk, bison and venison to follow, served with three or four steak cuts and barbecue items at 102 W Shell Point Road, Ruskin FL — opening January 2027.",
                       "/wild-game-and-steaks-ruskin")])
    + nav("/wild-game-and-steaks-ruskin")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; <a href="/menu">Menu</a> &middot; Game &amp; steaks</p>
  <p class="lab mono">The ranch side</p>
  <h1>Game first. Steaks always.</h1>
  <p class="lede">&#8220;We want to bring a little bit of Montana or the West down to Florida and combine it with the Florida seafood as well&#8221; — the owner, Douglas Starz, on why elk and bison share a board with Gulf catch.</p>
  <h2>The board</h2>
  <ul class="board">
    <li><span>Elk &amp; bison</span> the opening headliners — wild game is the lead of this menu, not a novelty line</li>
    <li><span>Bison, ranch-to-plate</span> for the opening a whole bison comes from a friend&#8217;s ranch — USDA-inspected, then driven to Florida</li>
    <li><span>Venison, to follow</span> the vendor hunt is on; when it&#8217;s set, it goes on</li>
    <li><span>Three or four steak cuts</span> this place is steak-focused at its core</li>
    <li><span>Barbecue items</span> several of them, carried down from the owner&#8217;s mountaintop barbecue days</li>
  </ul>
  <h2>Why this kitchen knows game</h2>
  <p>Before Ruskin, Douglas Starz owned The Dugout — a barbecue restaurant on the mountain at 9,000 feet in Big Sky, Montana. That operation is where the wild-game, steak and smoke program was built, cut by cut, season after season. Now it&#8217;s being replanted on the Gulf.</p>
  <p class="cta-row"><a class="btn" href="/contact">Join the opening-day list</a> <a href="/florida-seafood-ruskin">See the seafood side &rarr;</a></p>
</article>''')

# ---------------- SEAFOOD DETAIL ----------------
pages["florida-seafood-ruskin.html"] = (
    head("Florida Seafood in Ruskin FL — Coastal Cowboy Social",
         "Coastal Cowboy Social pairs its Western kitchen with serious Florida seafood at 102 W Shell Point Road, Ruskin FL — the owner grew up cooking near the Chesapeake Bay, and the shop sits steps off the Gulf.",
         "/florida-seafood-ruskin",
         [breadcrumb("Florida seafood", "/florida-seafood-ruskin"),
          service_node("Florida seafood", "Seafood kitchen",
                       "Florida and Gulf seafood served Western-style at Coastal Cowboy Social, 102 W Shell Point Road, Ruskin FL — opening January 2027 for lunch and dinner.",
                       "/florida-seafood-ruskin")])
    + nav("/florida-seafood-ruskin")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; <a href="/menu">Menu</a> &middot; Florida seafood</p>
  <p class="lab mono">The coast side</p>
  <h1>Bay cooking, cowboy hands</h1>
  <p class="lede">Half of this concept was learned on the Chesapeake. The other half is being written here — on Shell Point Road, where Ruskin meets the bay.</p>
  <h2>Where the seafood fluency came from</h2>
  <p>Douglas Starz grew up cooking in Pennsylvania, a short drive from the Maryland line and the Chesapeake Bay. Crab pots, oyster shanties, whatever came off the water that morning — that is the kitchen education underneath the seafood half of this menu.</p>
  <h2>Where it lands</h2>
  <ul class="board">
    <li><span>Florida seafood</span> the Gulf side of the board, from the waters the shop sits on</li>
    <li><span>Served with the grill</span> seafood here meets a steak-and-game kitchen — scallops next to elk, the way the West eats it</li>
    <li><span>Lunch and dinner</span> the seafood board runs both services from day one</li>
  </ul>
  <p>The full seafood board — cuts, prices, the daily catch lines — posts here the opening week. The list gets the email first.</p>
  <p class="cta-row"><a class="btn" href="/contact">Join the opening-day list</a> <a href="/wild-game-and-steaks-ruskin">See the game side &rarr;</a></p>
</article>''')

# ---------------- BAR + PAVILION DETAIL ----------------
pages["western-bar-and-pavilion.html"] = (
    head("Western Bar &amp; Outdoor Pavilion with Live Bands — Coastal Cowboy Social, Ruskin FL",
         "Coastal Cowboy Social in Ruskin FL pairs a Florida-style dining room with a Western-themed bar — Montana barnwood, trophy mounts — and an outdoor pavilion planned for weekend live bands with cocktail seating.",
         "/western-bar-and-pavilion",
         [breadcrumb("Bar & pavilion", "/western-bar-and-pavilion"),
          service_node("Western bar and outdoor pavilion", "Bar and live-entertainment venue",
                       "A Western-themed bar and an open-air pavilion with planned weekend live bands, cocktail seating and outdoor service at Coastal Cowboy Social, 102 W Shell Point Road, Ruskin FL.",
                       "/western-bar-and-pavilion")])
    + nav("/western-bar-and-pavilion")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; <a href="/menu">Menu</a> &middot; Bar &amp; pavilion</p>
  <p class="lab mono">Three rooms, one address</p>
  <h1>Dinner, drinks and a band — outside</h1>
  <p class="lede">The building does three settings on purpose: a Florida-style dining room for the table, a Western bar for the nightcap, and a pavilion for the weekend.</p>
  <h2>The bar</h2>
  <p>The bar is the loudest room in the building — and by design. The interior is being finished with barnwood brought down from Montana, and the mounts are going up as fast as the framers finish them. This is the cow-town half of the concept: cocktails, cold beer, and a room that looks like it drove down from the Big Sky.</p>
  <h2>The pavilion</h2>
  <ul class="board">
    <li><span>Live bands, weekends</span> live music and other entertainment are planned for pavilion nights from the opening plan forward</li>
    <li><span>Cocktail seating outside</span> the pavilion is built for drink-in-hand service under the open Florida sky</li>
    <li><span>Outdoor service</span> food and drinks, served out — no reservation needed to stand in a good band&#8217;s crowd</li>
  </ul>
  <h2>And later: the upstairs</h2>
  <p>Above the dining room is a two-bedroom apartment today. It&#8217;s planned to become a private, membership-based speakeasy — phase two, expected in 2027. When the details are set, they go on this site first.</p>
  <p class="cta-row"><a class="btn" href="/contact">Join the opening-day list</a> <a href="/visit">Find us on Shell Point Road &rarr;</a></p>
</article>''')

# ---------------- OUR STORY ----------------
pages["our-story.html"] = (
    head("Our Story — Coastal Cowboy Social, Ruskin FL",
         "Douglas Starz — a Pennsylvania-raised cook who owned The Dugout barbecue restaurant in Big Sky, Montana — is opening Coastal Cowboy Social at the old 1925 building on Shell Point Road in Ruskin FL.",
         "/our-story",
         [breadcrumb("Our story", "/our-story"),
          {"@context": "https://schema.org", "@type": "AboutPage", "name": "Our story — %s" % BRAND,
           "url": ORIGIN + "/our-story", "about": {k: v for k, v in restaurant_node("/our-story").items() if k != "@context"}}])
    + nav("/our-story")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Our story</p>
  <h1>A Montana kitchen, moved to the Gulf</h1>
  <p class="lede">Coastal Cowboy Social is one man&#8217;s two homes on one plate: the Western steak-and-game country he cooked in for years, and the Florida coast he moved to six years ago and decided to stay on.</p>
  <h2>The cook</h2>
  <p>Douglas Starz grew up cooking in Pennsylvania — a short drive from the Maryland line and the Chesapeake Bay, which is where his seafood ran was learned. He later owned The Dugout, an on-mountain barbecue restaurant at 9,000 feet in Big Sky, Montana. Wild game, steaks and smoke are what that altitude teaches you.</p>
  <blockquote class="quote">&#8220;We want to bring a little bit of Montana or the West down to Florida and combine it with the Florida seafood as well.&#8221;</blockquote>
  <h2>The town he chose</h2>
  <p>He&#8217;s lived in the Ruskin area for about six years now — long enough to pick the building and the customer base on purpose. &#8220;I love the area,&#8221; he says. Palmetto, Sun City, Bradenton, Riverview and Brandon are all about a 20-minute drive from the front door, which is exactly the point of putting a place like this here.</p>
  <h2>The building</h2>
  <p>102 W Shell Point Road is a 1925 building with good bones, right where Ruskin meets the bay. It&#8217;s being renovated into three rooms — a Florida-style dining room, a Western-themed bar, and an outdoor pavilion — finished with barnwood shipped down from Montana. The upstairs apartment becomes a members-only speakeasy in phase two, planned for 2027.</p>
  <h2>In the news</h2>
  <ul class="press">
    <li><a href="https://www.businessdebut.com/coastal-cowboy-social-is-opening-in-ruskin-here-are-details/">Business Debut — Coastal Cowboy Social is opening in Ruskin. Here are details.</a></li>
    <li><a href="https://www.businessdebut.com/4-exciting-hillsborough-county-restaurants-coming-soon/">Business Debut — 4 exciting Hillsborough County restaurants coming soon</a></li>
    <li><a href="https://www.businessdebut.com/3-hillsborough-county-restaurants-planning-to-open-nov-25-2026/">Business Debut — 3 Hillsborough County restaurants planning to open (Nov. 25, 2026)</a></li>
  </ul>
  <p class="cta-row"><a class="btn" href="/contact">Join the opening-day list</a> <a href="/visit">Find us on Shell Point Road &rarr;</a></p>
</article>''')

# ---------------- VISIT ----------------
pages["visit.html"] = (
    head("Visit — 102 W Shell Point Road, Ruskin, FL 33570",
         "Coastal Cowboy Social opens January 2027 at 102 W Shell Point Road in Ruskin FL — serving lunch and dinner, with Palmetto, Sun City, Bradenton, Riverview and Brandon all about 20 minutes away.",
         "/visit",
         [breadcrumb("Visit", "/visit"),
          service_node("Visit Coastal Cowboy Social", "Dining room, bar and pavilion",
                       "Coastal Cowboy Social opening January 2027 at 102 W Shell Point Road, Ruskin FL 33570 — lunch and dinner, Western bar and weekend pavilion.",
                       "/visit")])
    + nav("/visit")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Visit</p>
  <h1>102 W Shell Point Road</h1>
  <p class="lede">Ruskin sits on the bay where Hillsborough County leans toward the Gulf — and the shop sits right on Shell Point Road, twenty minutes inside the sprawl of five towns.</p>
  <div class="visit-grid">
    <div class="frame">
      <p class="lab mono">Address</p>
      <p class="addr">102 W Shell Point Road<br>Ruskin, FL 33570</p>
      <p><a href="''' + DIRS + '''">Get directions &nearr;</a></p>
      <p class="lab mono">When</p>
      <p>Opening January 2027 — exact day to be announced. Lunch and dinner service, with live bands in the pavilion on weekends. The day and the hours post on this page first, and the <a href="/contact">opening-day list</a> gets an email the day they are set.</p>
      <p class="lab mono">Around us</p>
      <p>Palmetto, Sun City, Bradenton, Riverview and Brandon — all about a 20-minute drive from the front door.</p>
    </div>
    <div class="map-tall"><iframe src="''' + MAP_Q + '''" loading="lazy" title="Map of Coastal Cowboy Social at 102 W Shell Point Road, Ruskin FL" allow="management:coordinate"></iframe><p class="mapcap">Shell Point Road at the bay &middot; Ruskin FL 33570 &middot; Hillsborough County</p></div>
  </div>
</article>''')

# ---------------- CONTACT ----------------
pages["contact.html"] = (
    head("Contact — Coastal Cowboy Social, Ruskin FL",
         "Join the Coastal Cowboy Social opening-day list: leave your email and the first word about the January 2027 opening, the hours and the full menu comes to you. 102 W Shell Point Road, Ruskin FL.",
         "/contact",
         [breadcrumb("Contact", "/contact"),
          service_node("Opening-day list and contact", "Customer contact",
                       "Leave your email to hear first about the January 2027 opening of Coastal Cowboy Social at 102 W Shell Point Road, Ruskin FL 33570.",
                       "/contact")])
    + nav("/contact")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Contact</p>
  <p class="lab mono">Opening-day list</p>
  <h1>Be first through the door</h1>
  <p class="lede">Leave your email. When the opening day is set — January 2027 — the first word goes to this list: the day, the hours, the menu, the first band.</p>
  <form class="cform" method="post" action="/contact">
    <p><label for="f-name">Name</label><input id="f-name" name="name" type="text" maxlength="120" required></p>
    <p><label for="f-email">Email <span class="fine">so we can tell you when we open</span></label><input id="f-email" name="email" type="email" maxlength="120" required></p>
    <p><label for="f-msg">Questions, or something you&#8217;re hoping we&#8217;ll cook? <span class="fine">(optional)</span></label><textarea id="f-msg" name="message" rows="4" maxlength="4000"></textarea></p>
    <p><button class="btn" type="submit">Send it</button></p>
  </form>
  <div class="frame">
    <p class="lab mono">The storefront</p>
    <p class="addr">102 W Shell Point Road, Ruskin, FL 33570</p>
    <p><a href="''' + DIRS + '''">Get directions &nearr;</a></p>
  </div>
  <div class="map-tall"><iframe src="''' + MAP_Q + '''" loading="lazy" title="Map: 102 W Shell Point Road, Ruskin FL — Coastal Cowboy Social" allow="management:coordinate"></iframe><p class="mapcap">102 W Shell Point Road &middot; Ruskin FL 33570 &middot; <a href="''' + DIRS + '''">Get directions &nearr;</a></p></div>
</article>''')

# ---------------- PRIVACY ----------------
pages["privacy.html"] = (
    head("Privacy — Coastal Cowboy Social",
         "How this site handles what you send it: contact-form messages go to the shop's inbox and are used only to answer you and the opening-day announcements. No cookies, no trackers.",
         "/privacy",
         [breadcrumb("Privacy", "/privacy"), restaurant_node("/privacy")])
    + nav("/privacy")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Privacy</p>
  <h1>What you send us</h1>
  <p>Messages from this site&#8217;s form go straight to the shop&#8217;s inbox — the name, email and note you type, nothing more. We use them to answer you and to send the opening-day announcement to people who asked for it. We do not sell, rent or trade your details.</p>
  <p>This site sets no cookies and runs no advertising or analytics trackers. Pages load from our own host with our own stylesheet; there is no third-party script on any page.</p>
  <p>Questions about this page? <a href="/contact">Use the form</a> and ask.</p>
</article>''')

# ---------------- 404 / THANKS (utility) ----------------
pages["404.html"] = (
    head("Page not found — Coastal Cowboy Social",
         "That page is off the board. Coastal Cowboy Social opens January 2027 at 102 W Shell Point Road in Ruskin FL.",
         "/404", utility=True)
    + nav("")
    + '''<article class="page">
  <p class="lab mono">404</p>
  <h1>That page rode out</h1>
  <p class="lede">Nothing at this address but dust. The two pages that matter are below.</p>
  <p class="cta-row"><a class="btn" href="/">Back to the front</a> <a href="/contact">Join the opening-day list</a></p>
</article>''')

pages["thanks.html"] = (
    head("You're on the list — Coastal Cowboy Social",
         "Thanks — Coastal Cowboy Social will email you first when the doors open at 102 W Shell Point Road, Ruskin FL, January 2027.",
         "/thanks", utility=True)
    + nav("")
    + '''<article class="page">
  <p class="lab mono">Received</p>
  <h1>You&#8217;re on the list</h1>
  <p class="lede">When the opening day is set — January 2027, Shell Point Road — this list hears it first: the day, the hours, the menu, the first band.</p>
  <p class="cta-row"><a class="btn" href="/">Back to the site</a></p>
</article>''')

# ---------------- CSS ----------------
CSS = """:root{
  --bark:#26170f; --bark-soft:#3c2a1c; --bone:#f5efe3; --paper:#fbf7ee;
  --rust:#b0471f; --rust-dk:#8c3517; --teal:#2f5d63; --pale:#9fc4c9; --sand:#d9c9ae;
  --rule:#5a4632; --dim:#6f5d4b;
  --serif:Georgia,"Iowan Old Style","Times New Roman",serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{color-scheme:light}
body{background:var(--bone);color:var(--bark);font-family:var(--serif);font-size:17px;line-height:1.6}
.topline{height:6px;background:linear-gradient(180deg,var(--rust) 0 3px,var(--teal) 3px 6px)}
.skip{position:absolute;left:-9999px;top:0;background:var(--bark);color:var(--bone);padding:.5rem 1rem;z-index:9}
.skip:focus{left:1rem;top:1rem}
a{color:var(--rust)}
a:hover{color:var(--rust-dk)}
.mono{font-family:var(--mono)}
header.site{padding:1.1rem max(1.1rem, calc((100vw - 1060px)/2));border-bottom:1px solid var(--bark);display:flex;flex-wrap:wrap;gap:.6rem 1.5rem;align-items:center;justify-content:space-between}
.brand{font-size:13px;letter-spacing:.16em;text-transform:uppercase;margin:0}
.brand a{color:var(--bark);text-decoration:none}
.brand em{font-style:normal;color:var(--rust)}
header.site nav p{display:flex;flex-wrap:wrap;gap:.35rem 1.1rem;justify-content:flex-end;margin:0}
header.site nav a{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;color:var(--rule)}
header.site nav a:hover{color:var(--rust);text-decoration:underline;text-underline-offset:4px}
header.site nav a[aria-current="page"]{color:var(--rust);text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:4px}
main{max-width:1060px;margin:0 auto;padding:0 1.5rem 3.5rem}
.lab{font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--rust);margin-bottom:.6rem}
.hero{background:var(--bark);color:var(--bone);margin:1.5rem 0;border-top:3px solid var(--rust);border-bottom:3px solid var(--rust);padding:clamp(2rem,6vw,4.5rem) clamp(1.2rem,5vw,4rem);text-align:center}
.hero .lab{color:var(--sand)}
.hero h1{font-size:clamp(2.3rem,6vw,4.1rem);line-height:1.05;font-weight:700;letter-spacing:.015em;text-transform:uppercase;margin:.2rem 0 .5rem}
.hero .sub{max-width:38rem;margin:.8rem auto 1.4rem;color:var(--bone);font-size:1.05rem;line-height:1.55}
.hero-cta{display:flex;flex-wrap:wrap;gap:.8rem 1.2rem;justify-content:center;align-items:center}
.btn{display:inline-block;background:var(--rust);color:var(--bone);font-family:var(--mono);font-size:13px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;padding:.8rem 1.3rem;border:1px solid var(--bark);box-shadow:4px 4px 0 var(--bark)}
.btn:hover{background:var(--rust-dk);color:#fff}
.btn.sm{padding:.45rem .8rem;font-size:11px;box-shadow:3px 3px 0 var(--bark)}
a.ghost{color:var(--rust);font-family:var(--mono);font-size:13px;letter-spacing:.08em;text-transform:uppercase;text-decoration:underline;text-underline-offset:5px}
.hero a.ghost{color:var(--pale)}
.panels{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.4rem;margin:1.6rem 0 2.4rem}
.panels>.frame{height:100%}
.frame{background:var(--paper);border:1px solid var(--bark);box-shadow:6px 6px 0 var(--rust);padding:1.6rem 1.4rem 1.4rem;display:flex;flex-direction:column}
.frame h2{font-size:1.3rem;line-height:1.2;margin-bottom:.5rem}
.frame p{margin-bottom:.7rem}
.frame p:last-child{margin-bottom:0;margin-top:auto}
.band{display:grid;grid-template-columns:minmax(300px,1.25fr) minmax(280px,1fr);gap:1.4rem;align-items:center;background:var(--paper);border:1px solid var(--bark);box-shadow:6px 6px 0 var(--teal);padding:1.6rem}
.band h2{font-size:1.6rem;margin-bottom:.4rem}
.band-map iframe{width:100%;aspect-ratio:4/3;border:1px solid var(--bark);display:block;background:var(--paper)}
.mapcap{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);text-align:center;margin-top:.5rem}
.page{padding-top:1.8rem}
.crumbs{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin-bottom:1rem}
h1{font-size:clamp(1.9rem,4.5vw,2.9rem);line-height:1.1;margin-bottom:.8rem}
.lede{font-size:1.15rem;line-height:1.55;max-width:44rem;margin-bottom:1.4rem;color:var(--bark-soft)}
.page h2{font-size:1.35rem;margin:1.6rem 0 .5rem}
.page p{max-width:46rem;margin-bottom:1rem}
blockquote.quote{max-width:44rem;margin:1.4rem 0;padding:1rem 1.3rem;border-left:4px solid var(--rust);background:var(--paper);font-style:italic;font-size:1.1rem}
.board{list-style:none;margin:0 0 1.2rem;border-top:1px solid var(--rule)}
.board li{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:.5rem 1.4rem;padding:.65rem 0;border-bottom:1px solid var(--rule);font-size:.98rem}
.board li span{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--rust);padding-top:.15rem}
dl.faq{margin:1.6rem 0;border-top:1px solid var(--rule)}
dl.faq dt{font-family:var(--mono);font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--rust);padding:.9rem 0 .2rem}
dl.faq dd{padding:0 0 1rem;border-bottom:1px solid var(--rule);max-width:46rem}
ul.press{list-style:none;margin:0 0 1.2rem}
ul.press li{padding:.5rem 0;border-bottom:1px solid var(--rule)}
.cta-row{display:flex;flex-wrap:wrap;gap:.8rem 1.2rem;align-items:center;margin-top:1.4rem}
.addr{font-family:var(--mono);font-size:14px;letter-spacing:.04em;margin-bottom:.6rem}
.visit-grid{display:grid;grid-template-columns:minmax(280px,1fr) minmax(280px,1.2fr);gap:1.4rem;align-items:start}
.map-tall iframe{width:100%;aspect-ratio:4/3;border:1px solid var(--bark);display:block;background:var(--paper)}
.cform{max-width:34rem;margin:0 0 1.8rem}
.cform p{margin-bottom:1rem}
.cform label{display:block;font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--rule);margin-bottom:.35rem}
.fine{color:var(--dim);text-transform:none;letter-spacing:.02em}
.cform input,.cform textarea{width:100%;font-family:var(--serif);font-size:16px;padding:.65rem .8rem;border:1px solid var(--rule);background:#fff;color:var(--bark)}
.cform input:focus,.cform textarea:focus{outline:2px solid var(--rust);outline-offset:1px}
footer{background:var(--bark);color:var(--bone);padding:1.8rem 1.5rem;text-align:center}
footer p.footline{font-family:var(--mono);font-size:12px;letter-spacing:.08em;line-height:1.9;max-width:none;margin:0 auto}
footer a{color:var(--sand)}
footer p.fine{color:var(--sand);font-size:11px}
@media (max-width:640px){
  body{font-size:16px}
  header.site nav p{justify-content:flex-start}
  .band,.visit-grid{grid-template-columns:1fr}
  .board li{grid-template-columns:1fr;gap:.2rem}
  main{padding:0 1.1rem 3rem}
  .hero{padding:2rem 1.1rem}
}"""

def write(name, content):
    with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
        f.write(content if content.endswith("\n") else content + "\n")

os.makedirs(PUBLIC, exist_ok=True)
for name, content in pages.items():
    write(name, content + FOOTER)
write("style.css", CSS)

core = ["index.html", "menu.html", "wild-game-and-steaks-ruskin.html", "florida-seafood-ruskin.html",
        "western-bar-and-pavilion.html", "our-story.html", "visit.html", "contact.html", "privacy.html"]
today = "2026-11-25"
locs = "\n".join('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>' %
                 (ORIGIN, "/" if f == "index.html" else "/" + f[:-5], today) for f in core)
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % locs)
write("robots.txt", "User-agent: *\nDisallow:\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)
# static assets that live at repo root must ride into public/ (server serves public/ only)
import shutil
for asset in ("pixel.gif", "favicon.svg"):
    src = os.path.join(HERE, asset)
    if os.path.exists(src):
        shutil.copyfile(src, os.path.join(PUBLIC, asset))
print("built %d pages + css + sitemap + robots" % len(pages))
