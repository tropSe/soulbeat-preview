"""Gryning-komponenter: README + preview.html per komponent, markup klippt ordagrant ur index.html."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(sys.argv[1], "index.html"), encoding="utf-8").read()
BASE = os.path.join(HERE, "g", "project", "components")
BLOB = {
    "louna-shamantrumma": "2f500108bcf064362858e43232042a76", "alexis-dans": "25fb9949c8be4196cc995d51d2319bb0",
    "louna-kora": "4e3ce8a86e56e4140924d2fb4572adeb", "louna-ponyo-ramtrummor": "b2d8306debdaa32bd7b4275141ad297f",
    "louna-handpan": "63e5598e5c8c803dcd1c73ed43f90630", "louna-gong-ljus": "695ba76673f40e08b6a664a3a0ab6e63",
    "louna-gong-meditation": "e5cde3c443d2decce21a8fe7318a9410",
}

def cut(start, end, from_=0):
    i = SRC.index(start, from_)
    j = SRC.index(end, i) + len(end)
    return SRC[i:j]

def fix(html):
    html = re.sub(r'bilder/([a-z0-9-]+)\.webp', lambda m: "/_blob/" + BLOB[m.group(1)] if m.group(1) in BLOB else m.group(0), html)
    return html.replace(' loading="lazy"', "")

def doc(marker, body):
    return (f"{marker}\n<!doctype html>\n<html lang=\"sv\">\n<head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>SoulBeat</title></head>\n"
            f"<body>\n{fix(body)}\n<script></script>\n</body>\n</html>\n")

hero = cut('<header class="hero"', "</header>")
day = cut('<ol class="day">', "</ol>")
exp_top = cut('<div class="exp-top">', '</div>\n    </div>')
cal_all = cut('<div class="cal">', "</div>\n\n    <div class=\"bring\">")
datecard_facts = cal_all[:cal_all.index('<div class="cal-actions">')] + "</div>\n    </div>"
cal_actions = cut('<div class="cal-actions">', "</div>")
faq = cut('<div class="wrap faq-grid">', "</div>\n  </div>\n</section>").replace("</div>\n  </div>\n</section>", "</div>\n  </div>")
quotes = cut('<div class="quotes">', "</figure>\n    </div>")
nl = cut('<div id="nyhetsbrev">', "</form>\n    </div>")
footer = cut("<footer>", "</footer>")
instr = cut('<ul class="instr">', "</ul>")
band = cut('<div class="wrap"><div class="band">', "</div></div>")
pillars = cut('<ul class="pillars">', "</ul>")
who = cut('<ul class="who">', "</ul>")
bring = cut('<div class="bring">', "</div>\n    </div>")
ctas = cut('<div class="ctas">', "</div>")
contact = cut('<ul class="contact">', "</ul>")

C = {}
C["Hero"] = ("""# Hero

Första skärmen: etikett, namnet med kursivt Beat, tagline, faktarader, två knappar och valvet framför den randiga solen.

**Konsumenten ger:** menyn (`nav.nav` med logga och fyra länkar, där bara `li.keep` syns på mobil), `.kicker`, `h1.wordmark` med `Soul<i>Beat</i>`, `.tagline`, `.intro`, `ul.facts` (Premiär, Tid, Plats), `.ctas` med `btn-main` och `btn-line`, och `.hero-art` med `svg.sun` och `.arch.hero-arch` runt louna-shamantrumma.webp.

- Heron slutar med `.horizon`: 10 px `ink` i full bredd.
- Solen (`svg.sun`) är den randiga halvsolen ur tillgångarna, med gradienten sun-1 till sun-3 och fyra ränder som blir tjockare nedåt (5, 7, 9, 11 px).
- Valvet har 6 px ram i `bg` och skuggan `arch-lift`. Det är sajtens enda skugga.
- Från 960 px står text och bild i 1.1fr / .9fr, solen är 640 px och valvet 360 px.
""", doc('<!-- @dsCard group="Sidan" height=760 width=1200 subtitle="Ordagrant från soulbeat.se" -->', hero))

C["Premiarblock"] = ("""# Premiarblock

Datumkortet i ink bredvid fyra faktarutor (När, Tid, Plats, Pris).

**Konsumenten ger:** `.cal > .datecard` (veckodag i `.dow`, dag i `.day-n`, månad och år i `.mon`, tid i `.tm`, Solpuls på ink), och `ul.ev-facts` med fyra `li` som har `small` (etikett) och `strong` (värde). Pris som inte är satt skrivs "Snart" i `strong.tbd`.

- Datumkortet har radien `card` (22 px) och centrerad text. Solpuls där är varianten på ink.
- Faktarutorna står två och två på mobil och fyra i rad från 760 px, med `line` som avdelare.
- Klockslag inom morgonen skrivs aldrig ut, bara 08–12.
""", doc('<!-- @dsCard group="Sidan" height=520 width=1000 subtitle="Datumkort och faktarutor" -->', '<section class="pad alt"><div class="wrap">' + datecard_facts + "</div></section>"))

C["Knapp"] = ("""# Knapp

Pillerformad knapp med 1,5 px kant: `btn btn-main` (ink-fylld) och `btn btn-line` (bara kant).

**Konsumenten ger:** text med verb först och meningsversaler, `href` eller `type`. Knappar i rad ligger i `.ctas` (12 px mellanrum, bryts på smal skärm).

- Hover på `btn-main`: fyllningen blir `rust`. Hover på `btn-line`: grunden blir `bg-2` (på sand-sektioner `bg`).
- I sidfoten är knappen krämfylld med ink-text och hover i `sun-1`.
- Huvudknappen högst en gång per vy.
""", doc('<!-- @dsCard group="Kontroller" height=150 subtitle="Huvudknapp och linjeknapp" -->', '<div class="wrap" style="padding-top:24px">' + ctas + "</div>"))

C["Bildvalv"] = ("""# Bildvalv

Bilder i valv: `div.arch` med radien 999px 999px 0 0 runt en `img` med object-fit cover.

**Konsumenten ger:** `div.arch` med storleksklass (`hero-arch`, `louna-photo`, `small-arch` eller inne i `.instr`/`.team-photos`), och `img` med `alt`, `width` och `height`. Bildtext i `.name` (instrument) eller `figcaption` (team).

- Valven håller de mjuka bilderna små: heroens valv högst 360 px, Louna 320 px, upplägget 220 px, instrumenten 150 px.
- Den enda bilden utan valv är `alexis-dans.webp` i `.band`: rundade hörn (22 px), högst 600 px hög, object-position 62 % 12 %. Den är skarp nog för full bredd.
- Använd aldrig `louna-ponyo-dans.webp` (för suddig).
""", doc('<!-- @dsCard group="Bild" height=640 width=1000 subtitle="Instrumentvalv och bandet" -->', '<section class="pad alt"><div class="wrap">' + instr + "</div></section>\n" + band))

C["Punktlista"] = ("""# Punktlista

Listor med solpunkter: pelarna i Om, För vem-listan och Ta med / Bra att veta.

**Konsumenten ger:** `ul.pillars` (rubrik i `b`, förklaring i `.t`), `ul.who` (en mening per rad) eller `.bring` (h3 och lista). Varje rad börjar med `span.sun-dot`.

- Punkternas färg går genom solskalan uppifrån: sun-1, sun-12, sun-2, sun-23, sun-3, rust. Solen stiger listan nedåt.
- Raderna skiljs med 1 px `line`. För vem står i två kolumner från 760 px.
- Punkterna är dekor och bär ingen betydelse (sun-2 når bara 2,2:1 mot bg).
""", doc('<!-- @dsCard group="Sidan" height=760 width=1000 subtitle="Pelare, För vem, Ta med" -->',
          '<section class="pad"><div class="wrap">' + pillars + '</div></section><section class="pad alt"><div class="wrap">' + who + "\n" + bring + "</div></section>"))

C["Upplagget"] = ("""# Upplagget

Morgonens fem delar i ordning, med en solpunkt som stiger för varje del på desktop.

**Konsumenten ger:** `ol.day` med fem `li`: `div.dot` med en cirkel (fyllning sun-1, sun-12, sun-2, sun-23, sun-3 i den ordningen), `span.step` (Först, Sedan, Morgonens kärna, Mot slutet, Efteråt), `h3` och en mening i `p`.

- Från 960 px står delarna i fem kolumner och punkterna stiger som en soluppgång (bottom: -23, 0, 34, 64, 74 px).
- Skriv aldrig ut klockslag för delarna. Ordningsorden ersätter dem.
""", doc('<!-- @dsCard group="Sidan" height=720 width=1200 subtitle="Fem delar, solen stiger" -->', '<section class="pad"><div class="wrap">' + exp_top + "\n" + day + "</div></section>"))

C["Kalenderknappar"] = ("""# Kalenderknappar

Tre knappar för kalendern: Google Kalender (huvudknapp), .ics och prenumeration.

**Konsumenten ger:** `.cal-actions` med tre länkar exakt:
1. `btn btn-main` till Google Kalender i UTC, `dates=20261127T070000Z/20261127T110000Z`, med `recur=RRULE:FREQ%3DMONTHLY;BYDAY%3D4FR`, `target="_blank" rel="noopener"`. Text: "Lägg till i Google Kalender".
2. `btn btn-line` till `soulbeat.ics` med `download`. Text: "Ladda ner (.ics)". Rör aldrig filens UID.
3. `btn btn-line` till `webcal://soulbeat.se/soulbeat.ics`. Text: "Prenumerera på serien".

- Staplade på mobil, i rad från 760 px.
""", doc('<!-- @dsCard group="Kontroller" height=260 subtitle="Google, .ics, webcal" -->', '<section class="pad alt" style="padding:32px 0"><div class="wrap">' + cal_actions + "</div></section>"))

C["Fragor"] = ("""# Fragor

Vanliga frågor som `details`/`summary` med en liten cirkel som markör.

**Konsumenten ger:** `.faq-grid` med rubrikkolumn (kicker, h2, lead) och `.faq` med ett `details` per fråga: frågan i `summary` (Instrument Serif 1.45rem), svaret i `p` (muted).

- Stängd: cirkelns kant i `rust`. Öppen: cirkeln fylls med `sun-2`. Öppet läge syns också på att svaret visas, så färgen bär inte ensam betydelsen.
- Ordet nykter får bara stå här, i ett lugnt svar.
- Alla sju frågor finns på sajten; ändra inte svaren i sak.
""", doc('<!-- @dsCard group="Sidan" height=640 width=1200 subtitle="Sju frågor, den första öppen" -->',
          '<section class="pad">' + faq.replace("<details>", "<details open>", 1) + "</section>"))

C["Roster"] = ("""# Roster

Tre deltagarcitat, ordagrant, med en 2 px ink-linje ovanför varje.

**Konsumenten ger:** `.quotes` med tre `figure.quote`: citatet i `blockquote` (Instrument Serif 1.45rem), förnamnet i `figcaption` (versaler, spärrat, rust).

- Citaten från Ole, Miranda och Lottika står exakt som de skrevs, med utropstecken.
- En kolumn på mobil, tre från 760 px.
- Hitta aldrig på citat eller namn.
""", doc('<!-- @dsCard group="Sidan" height=420 width=1200 subtitle="Ole, Miranda, Lottika" -->', '<section class="pad" style="padding-top:20px"><div class="wrap">' + quotes + "</div></section>"))

C["Nyhetsbrev"] = ("""# Nyhetsbrev

E-postformuläret, kopplat till Netlify Forms.

**Konsumenten ger:** formuläret exakt: `name="nyhetsbrev"`, `method="POST"`, `data-netlify="true"`, `netlify-honeypot="bot-field"`, dolt fält `form-name=nyhetsbrev`, honeypot `bot-field` i `p.hp`, synlig etikett `.email-label`, `input type="email" name="email" required autocomplete="email"` och `button.btn.btn-main` "Prenumerera".

- Fältet är pillerformat med 1,5 px ink-kant och bakgrund `input-bg`. Platshållaren i `placeholder`.
- Från 760 px står fält och knapp på samma rad.
- Efter skick visar Netlify sin egen tacksida.
""", doc('<!-- @dsCard group="Kontroller" height=360 width=900 subtitle="Netlify Forms" -->', '<section class="pad" style="padding-top:24px"><div class="wrap">' + nl + "</div></section>"))

C["Sidfot"] = ("""# Sidfot

Sidfoten i ink: Solpuls, en sista rubrik, datumraden, en knapp och kontaktraderna.

**Konsumenten ger:** `footer > .wrap > .foot-cta` (Solpuls på ink, h2 med ett kursivt ord i `sun-1`, en rad i `muted-on-ink`, `a.btn`) och `.foot-bottom` med tre rader: beskrivning, e-post och telefon, domän och år.

- Text på ink: `cream-on-ink` och `muted-on-ink`, aldrig `muted` eller `rust` (för mörkt på ink).
- Knappen är krämfylld; hover i `sun-1`.
""", doc('<!-- @dsCard group="Sidan" height=560 width=1000 subtitle="Ink, Solpuls, sista knappen" -->', footer))

for name, (readme, preview) in C.items():
    d = os.path.join(BASE, name); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "README.md"), "w", encoding="utf-8", newline="\n").write(readme)
    open(os.path.join(d, "preview.html"), "w", encoding="utf-8", newline="\n").write(preview)
left = [m for m in re.findall(r'bilder/[a-z0-9-]+\.webp', "".join(p for _, p in C.values()))]
print("klart", list(C), "olänkade bilder:", sorted(set(left)))
