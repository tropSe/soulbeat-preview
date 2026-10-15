"""SoulBeat Gryning: tokens och komponent-CSS ur soulbeat.se:s index.html (live 2026-10-15).
Skriver:
  g/project/tokens.json            (Design System-artefaktens listformat)
  g/project/components/bundle.css  (sajtens CSS utan :root, värdena kommer från tokens)
  <repo>/design/tokens.json        (W3C Design Tokens, DTCG)
Användning: py gryning_gen.py <repo>"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1]
SRC = open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
STYLE = SRC[SRC.index("<style>") + 7:SRC.index("</style>")]

# ---------- Färg: exakt som :root i index.html, plus de hex som står direkt i reglerna ----------
COLORS = [
    ("bg", "#f7f0e6", "Kräm. Sidans grund, varannan sektion. ink och muted på den."),
    ("bg-2", "#efe2cf", "Sand. Grund för sektioner med klassen alt (Louna, För vem, Kalender, Bakom). ink och muted på den."),
    ("ink", "#2a1810", "Rubriker och brödtext på bg och bg-2. Grund för datumkortet och sidfoten. Huvudknappens fyllning."),
    ("muted", "#5e4234", "Ingress (lead), förklaringar, små etiketter på bg och bg-2."),
    ("rust", "#a3391a", "Etiketten ovanför rubriker (kicker), det kursiva ordet i h2, \"Snart\", länk- och knapphover. Den enda accentfärgen för text."),
    ("sun-1", "#f6c08f", "Solens ljusaste ton. Kursivt ord i sidfotens rubrik (på ink), knapphover i sidfoten, första solpunkten."),
    ("sun-12", "#f2a46f", "Mellanton i solskalan. Andra solpunkten i Upplägget och För vem."),
    ("sun-2", "#ec8a52", "Solens mitt. Solpunkter, öppen FAQ-markör. Grafik, aldrig text (2,2:1 mot bg)."),
    ("sun-23", "#dc6c3e", "Mellanton i solskalan. Fjärde solpunkten."),
    ("sun-3", "#c8502c", "Solens mörkaste ton. Femte solpunkten, solens nederkant."),
    ("cream-on-ink", "#f7f0e6", "Text på ink: datumkortet och sidfoten."),
    ("muted-on-ink", "#d9c6b4", "Dämpad text på ink: klockslaget i datumkortet, sidfotens rader."),
    ("line", "rgba(42,24,16,.16)", "Tunna avdelare (1 px) i faktarader, listor och FAQ. Dekor, bär ingen betydelse."),
    ("input-bg", "#fffaf3", "Bakgrund i e-postfältet."),
    ("placeholder", "#7d6152", "Platshållartext i e-postfältet (5,5:1 mot input-bg)."),
]
SPACING = [
    ("gutter", "20px", "Sidmarginal under 760 px (.wrap)."),
    ("gutter-lg", "40px", "Sidmarginal från 760 px."),
    ("section", "76px", "Luft över och under en sektion under 760 px (.pad)."),
    ("section-lg", "110px", "Luft över och under en sektion från 760 px."),
    ("gap-sm", "12px", "Mellan knappar (.ctas), formulärfält."),
    ("gap-md", "26px", "Avstånd ovanför knappraden och faktalistan i heron."),
    ("gap-lg", "34px", "Mellan kolumner som staplas på mobil (om, Louna, team)."),
    ("gap-xl", "70px", "Mellan kolumner från 960 px."),
]
RADIUS = [
    ("pill", "999px", "Knappar och e-postfältet. Valvet är samma radie på de två övre hörnen (999px 999px 0 0)."),
    ("card", "22px", "Datumkortet och bandbilden. Kartans två övre hörn."),
    ("dot", "50%", "Solpunkter och FAQ-markören."),
]
BORDER = [
    ("hairline", "1px", "Avdelare i line."),
    ("button", "1.5px", "Knappkant och e-postfältets kant."),
    ("quote", "2px", "Linjen ovanför varje röst (citat), i ink."),
    ("arch-frame", "6px", "Kräm ram runt heroens valv."),
    ("horizon", "10px", "Horisonten under heron och ovanför platsraden vid kartan, i ink."),
]
LAYOUT = [("maxw", "1180px", "Max innehållsbredd (.wrap)."), ("hero-arch", "360px", "Heroens valv från 960 px; 280 px eller 74 % under.")]
SHADOW = [("arch-lift", "0 30px 60px -30px rgba(42,24,16,.5)", "Bara heroens valv. Ingen annan skugga på sajten.")]

FAMILIES = {"serif": "\"Instrument Serif\", Georgia, serif", "sans": "\"Manrope\", system-ui, sans-serif"}
TYPE = [
    {"name": "Rubriker", "family": "serif", "styles": [
        {"name": "typ-wordmark", "fontSize": "168px", "lineHeight": 0.86, "fontWeight": 400, "letterSpacing": "-0.02em", "sample": "SoulBeat",
         "usage": "Namnet i heron: Soul rak + Beat kursiv i rust. clamp(4.6rem, 24vw, 10.5rem)."},
        {"name": "typ-h2", "fontSize": "73.6px", "lineHeight": 0.95, "fontWeight": 400, "letterSpacing": "-0.01em", "sample": "Från landning till lounge",
         "usage": "Sektionsrubrik. clamp(2.6rem, 11vw, 4.6rem). Ett ord i kursiv rust (i)."},
        {"name": "typ-tagline", "fontSize": "33.6px", "lineHeight": 1.2, "fontWeight": 400, "fontStyle": "italic", "sample": "Börja dagen i kroppen, inte i huvudet.",
         "usage": "Heroens tagline, alltid kursiv. clamp(1.45rem, 6vw, 2.1rem)."},
        {"name": "typ-lead-big", "fontSize": "30.4px", "lineHeight": 1.25, "fontWeight": 400, "sample": "Ingen prestation, inga steg att lära sig.",
         "usage": "Stor ingress i serif. clamp(1.45rem, 5.6vw, 1.9rem)."},
        {"name": "typ-h3", "fontSize": "27.2px", "lineHeight": 1.1, "fontWeight": 400, "sample": "Öppningscirkel", "usage": "Underrubrik, 1.7rem."},
        {"name": "typ-quote", "fontSize": "23.2px", "lineHeight": 1.3, "fontWeight": 400, "sample": "Magiskt!", "usage": "Röster och FAQ-frågor, 1.45rem."},
        {"name": "typ-date-number", "fontSize": "102.4px", "lineHeight": 0.9, "fontWeight": 400, "sample": "27", "usage": "Dagen i datumkortet, 6.4rem."},
    ]},
    {"name": "Text", "family": "sans", "styles": [
        {"name": "typ-body", "fontSize": "16.32px", "lineHeight": 1.65, "fontWeight": 400, "sample": "Kom och gå som du vill.", "usage": "All brödtext, 1.02rem."},
        {"name": "typ-button", "fontSize": "15.36px", "lineHeight": 1.2, "fontWeight": 700, "sample": "Kom på premiären", "usage": "Knappar, .96rem."},
        {"name": "typ-kicker", "fontSize": "12.48px", "lineHeight": 1.4, "fontWeight": 700, "letterSpacing": "0.2em", "sample": "MORGONDANS I MALMÖ",
         "usage": "Etiketten ovanför h2, versaler, rust. .78rem."},
        {"name": "typ-label", "fontSize": "11.52px", "lineHeight": 1.4, "fontWeight": 700, "letterSpacing": "0.16em", "sample": "PLATS",
         "usage": "Små versala etiketter i faktarader och kontaktlistan, muted. .72rem."},
    ]},
]

def lst(rows):
    return {"tokens": [{"name": n, "value": v, "usage": u} for n, v, u in rows]}

ds = {"name": "SoulBeat", "version": 2,
      "meta": {"source": "soulbeat.se index.html, Gryning, live 2026-10-15"},
      "color": {"themes": [{"id": "gryning", "name": "Gryning"}],
                "tokens": [{"name": n, "value": v, "usage": u} for n, v, u in COLORS]},
      "type": {"fonts": [], "families": FAMILIES, "groups": TYPE},
      "spacing": lst(SPACING), "radius": lst(RADIUS), "borderWidth": lst(BORDER), "layout": lst(LAYOUT), "shadow": lst(SHADOW)}

out = os.path.join(HERE, "g", "project")
os.makedirs(os.path.join(out, "components"), exist_ok=True)
json.dump(ds, open(os.path.join(out, "tokens.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- bundle.css: sajtens CSS, :root flyttad till tokens ----------
css = re.sub(r":root\s*\{[^}]*\}\n", "", STYLE, count=1)
css = ("/* SoulBeat Gryning — komponenter, ordagrant ur soulbeat.se/index.html (live 2026-10-15).\n"
       "   Färger och mått som var :root-variabler kommer nu från tokens.json under samma namn. */\n"
       "@import url(\"https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;700&display=swap\");\n"
       + css.strip("\n") + "\n")
open(os.path.join(out, "components", "bundle.css"), "w", encoding="utf-8", newline="\n").write(css)

# ---------- DTCG ----------
def dim(v):
    m = re.match(r"^([\d.]+)(px|%)$", v)
    return {"value": float(m.group(1)), "unit": m.group(2)} if m else v
def col(v):
    if v.startswith("#"):
        r, g, b = [int(v[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        return {"colorSpace": "srgb", "components": [round(r, 4), round(g, 4), round(b, 4)], "hex": v}
    r, g, b, a = [float(x) for x in re.findall(r"[\d.]+", v)]
    return {"colorSpace": "srgb", "components": [round(r / 255, 4), round(g / 255, 4), round(b / 255, 4)], "alpha": a}
d = {"$description": "SoulBeat Gryning, W3C Design Tokens (DTCG). Källa: soulbeat.se index.html live 2026-10-15. Genererad av design/verktyg/gryning_gen.py.",
     "farg": {"$type": "color"}, "typsnitt": {}, "typografi": {}, "rum": {"$type": "dimension"}, "radie": {"$type": "dimension"},
     "kant": {"$type": "dimension"}, "layout": {"$type": "dimension"}, "skugga": {}}
for n, v, u in COLORS:
    d["farg"][n] = {"$value": col(v), "$description": u}
d["typsnitt"]["serif"] = {"$type": "fontFamily", "$value": ["Instrument Serif", "Georgia", "serif"]}
d["typsnitt"]["sans"] = {"$type": "fontFamily", "$value": ["Manrope", "system-ui", "sans-serif"]}
for g in TYPE:
    for st in g["styles"]:
        ls = st.get("letterSpacing", "0em")
        d["typografi"][st["name"]] = {"$type": "typography", "$description": st["usage"], "$value": {
            "fontFamily": "{typsnitt." + g["family"] + "}", "fontSize": dim(st["fontSize"]), "fontWeight": st["fontWeight"],
            "lineHeight": st["lineHeight"], "letterSpacing": {"value": float(ls.replace("em", "")), "unit": "em"}}}
for key, rows in (("rum", SPACING), ("radie", RADIUS), ("kant", BORDER), ("layout", LAYOUT)):
    for n, v, u in rows:
        d[key][n] = {"$value": dim(v), "$description": u}
d["skugga"]["arch-lift"] = {"$type": "shadow", "$description": SHADOW[0][2], "$value": {
    "color": {"colorSpace": "srgb", "components": [0.1647, 0.0941, 0.0627], "alpha": 0.5},
    "offsetX": {"value": 0, "unit": "px"}, "offsetY": {"value": 30, "unit": "px"},
    "blur": {"value": 60, "unit": "px"}, "spread": {"value": -30, "unit": "px"}}}
os.makedirs(os.path.join(REPO, "design"), exist_ok=True)
json.dump(d, open(os.path.join(REPO, "design", "tokens.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(css), "tecken CSS")
