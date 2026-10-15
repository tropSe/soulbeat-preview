# SoulBeat designsystem: Gryning

Version 2, 2026-10-15. Gryning är sajten som den är live på soulbeat.se, och den är källan för allt som byggs för SoulBeat, av människor och av Claude. Samma regler finns som designsystem i claude.ai: https://claude.ai/artifact/TfKjMB6R528qbitHXxRZif (privat tills Alexis delar det).

En annan riktning ("fältriktningen": färgfält, Anybody och Familjen Grotesk) togs fram samma dag och valdes bort. Den ligger i `_Arkiv/Ovrigt/soulbeat-designsystem-falt-2026-10-15/` och på grenen `arkiv/designsystem-falt`. Bygg inte vidare på den.

## Filer

| Fil | Vad |
|---|---|
| `index.html` | Sajten. Dess `<style>` är sanningen; allt nedan är hämtat därifrån |
| `design/tokens.json` | Färger, typografi, mått, radier, kanter och skuggan i W3C Design Tokens-format (DTCG) |
| `design/gryning-komponenter.css` | Sajtens CSS utan `:root`, som den ligger i designsystemet i claude.ai |
| `design/kontrast.md` | WCAG 2.2 och APCA för sajtens färgpar |
| `design/logga/` | Solpuls på ljust och på ink, favicon, den randiga solen |
| `design/lighthouserc.json` | Lighthouse CI-budget för typsnitt och laddning |
| `design/verktyg/` | `gryning_gen.py` (tokens och CSS ur index.html) och `gryning_komp.py` (komponenterna ur index.html) |

Ändras sajtens CSS ska tokens och designsystemet följa med: kör `py -3.12 design/verktyg/gryning_gen.py .` och uppdatera designsystemet i claude.ai.

## Komponenter

Klasserna är sajtens egna. Varje komponent har en levande förhandsvisning i designsystemet.

| Komponent | Markup | Regel i korthet |
|---|---|---|
| Hero | `header.hero` | Kicker, Soul*Beat*, tagline, faktarader, två knappar, valv framför randig sol, horisont 10 px |
| Premiärblock | `.cal > .datecard` + `ul.ev-facts` | Datumkort i ink med Solpuls, fyra faktarutor, "Snart" i kursiv rust |
| Knapp | `.btn.btn-main`, `.btn.btn-line` | Piller, 1,5 px kant, hover rust eller sand |
| Bildvalv | `div.arch` | Valv 999px 999px 0 0; bara alexis-dans utan valv, i `.band` |
| Punktlista | `ul.pillars`, `ul.who`, `.bring` | Solpunkter som går genom solskalan |
| Upplägget | `ol.day` | Fem delar, ordningsord i stället för klockslag, solen stiger |
| Kalenderknappar | `.cal-actions` | Google (UTC) som huvudknapp, .ics, webcal |
| Frågor | `.faq-grid` + `details` | Cirkelmarkör, rust stängd, sun-2 öppen |
| Röster | `.quotes` + `figure.quote` | Ordagranna citat, 2 px ink-linje ovanför |
| Nyhetsbrev | `form.nl-form` | Netlify Forms-attributen exakt, pillerfält |
| Sidfot | `footer` | Ink, Solpuls, kursivt ord i sun-1, krämfylld knapp |

## Bygga en sida

- **CSS:** tokens först, sedan `components/bundle.css`. bundle.css är sajtens egen CSS; färger och mått som `--bg`, `--ink` och `--rust` kommer från tokens under samma namn. Klasserna (`wrap`, `pad`, `alt`, `kicker`, `h2`, `lead`, `btn` med flera) är sajtens egna och används som de är.
- **Typsnitt:** Instrument Serif (rak och kursiv) och Manrope 400, 500 och 700 från Google Fonts. bundle.css laddar dem.
- **Sektioner:** `section.pad` på `bg`, varannan `section.pad.alt` på `bg-2`. Ordningen på sajten: Hero → Om → Louna (alt) → Upplevelsen → För vem (alt) → Röster → bandet med alexis-dans → Kalender och plats (alt) → Frågor → Bakom SoulBeat (alt) → Kontakt och nyhetsbrev → Sidfot (ink).
- **Sektionens huvud:** `.kicker` (versal etikett i rust), `.h2` med ett ord i kursiv rust (`<i>`), sedan `.lead` i muted. Exempel från sajten: "Från landning till *lounge*", "Boka in nästa *morgon*".
- **Ett tema.** Sajten är alltid ljus och följer inte telefonens mörka läge. Mörkt förekommer bara som ytor: datumkortet och sidfoten i `ink`.
- **Klockslag och datum** hålls ihop med `span.nw`: `<span class="nw">08–12</span>`.

## Det som gör Gryning till SoulBeat

Kräm, rost och en serif med ett kursivt ord är också vad en AI väljer när ingen säger emot. Det som skiljer SoulBeat är motiven nedan. Varje ny sida, bild eller annons ska ha minst ett av dem, gärna två.

- **Solpuls:** loggan, där horisonten slår ett hjärtslag upp genom solen.
- **Den randiga solen:** halvsolen med fyra ränder som blir tjockare nedåt (5, 7, 9, 11 px av 280), i gradienten sun-1 → sun-2 → sun-3.
- **Solen som stiger:** solpunkterna går genom skalan sun-1, sun-12, sun-2, sun-23, sun-3, rust, och i Upplägget stiger de från vänster till höger som en soluppgång.
- **Horisonten:** 10 px `ink` under heron och ovanför platsraden vid kartan.
- **Lounas bilder i valv.**

## Är och är inte

| SoulBeat är | SoulBeat är inte |
|---|---|
| En morgon: dagsljus, 08–12, te efteråt | Natt, klubbmörker, laser, neon |
| Fri dans utan steg, kroppsligt | Yogastudio, stretch, "hitta din inre frid" |
| Levande musik: shamantrumma, kora, handpan, gong | DJ-bås, lineup, headliners |
| Gemenskap: man kommer ensam och går hem med folk | VIP, exklusivitet, "community" som säljord |
| Jordnära: trägolv, gräs, orange tyg, bara fötter | Wellness-app: pastell, gradientbollar, glas |
| Lokalt i Malmö, en fredag i månaden | Festival, retreatresa, Bali |
| Nyktert som en självklarhet | Nykterhetskampanj, pekpinne |

## Håll dig inom Gryning

- Inga andra typsnitt än Instrument Serif och Manrope.
- Inga andra färger än tokens. Ingen lila, rosa eller blå. Den gamla identiteten (mörk bas #12090f, gradient #ff4f2e → #ff4fa3 → #b84dff, Space Grotesk och Inter) används inte.
- Ingen gradient utom solens (sun-1 → sun-2 → sun-3), och bara i solen och Solpuls.
- En enda skugga, `arch-lift`, och bara på heroens valv.
- Inga animationer. Rörelse finns bara i hover (0,15 s) och mjuk scroll; `prefers-reduced-motion` stänger av den.
- Inga emoji, inga ikoner som dekor. Solpunkterna gör ikonernas jobb.

## Text

- Skriv **SoulBeat** i ett ord, stort S och stort B. I ordbilden sätts det som Soul + kursivt *Beat* i rust.
- **Louna** stavas så, aldrig Luna. Hennes fullständiga namn är Louise Carmvall.
- Tilltala läsaren med *du*. Arrangörerna säger *vi*.
- Meningsversaler i rubriker och knappar. Etiketten (`.kicker`) skrivs med meningsversaler i koden ("Morgondans i Malmö") och visas i versaler via CSS.
- Ett kursivt ord per rubrik, aldrig fler, och aldrig i brödtext.
- Inga utropstecken och inga emoji i egen text. Deltagarnas citat står ordagrant, med sina utropstecken.
- Ordet *nykter* står bara i FAQ. Aldrig i rubriker, knappar, annonser eller kalendertext.
- Klockslag skrivs 08–12 med tankstreck. Skriv aldrig ut tider för delarna av morgonen; upplägget formas efter månadens tema.
- Exempel på rätt ton: "Börja dagen i kroppen, inte i huvudet." "Kom och gå som du vill."

## Färg

| Token | Värde | Används till |
|---|---|---|
| `bg` | #f7f0e6 | Kräm. Sidans grund |
| `bg-2` | #efe2cf | Sand. Varannan sektion (`.alt`) |
| `ink` | #2a1810 | Text, huvudknapp, datumkort, sidfot, horisont |
| `muted` | #5e4234 | Ingress, förklaringar, små etiketter |
| `rust` | #a3391a | Etiketten, det kursiva ordet, "Snart", hover |
| `sun-1` · `sun-12` · `sun-2` · `sun-23` · `sun-3` | #f6c08f · #f2a46f · #ec8a52 · #dc6c3e · #c8502c | Solen, solpunkterna, Solpuls. Grafik, aldrig brödtext |
| `cream-on-ink` · `muted-on-ink` | #f7f0e6 · #d9c6b4 | Text på ink |
| `line` | rgba(42,24,16,.16) | Tunna avdelare |
| `input-bg` · `placeholder` | #fffaf3 · #7d6152 | E-postfältet |

Kontroll 2026-10-15: all text på sajten klarar WCAG 2.2 AA (lägst rust på bg-2, 5,2:1). Två par klarar inte allt, och de står kvar som sajten har dem:
- `sun-2` på `bg` når 2,2:1, alltså under 3:1 för grafiska markörer. Det gäller solpunkterna och den öppna FAQ-markören. Punkterna är dekor, och i FAQ syns det öppna läget också på att svaret visas.
- `.kicker` i rust på `bg-2` klarar WCAG men når bara APCA Lc 66, vilket är lågt för 12,5 px. Gör den inte mindre, och lägg den inte på något mörkare än `bg-2`.

## Typografi

| Stil | Familj | Storlek | Används till |
|---|---|---|---|
| `typ-wordmark` | Instrument Serif 400, radavstånd .86, spärrning −.02em | clamp(4.6rem, 24vw, 10.5rem) | Bara SoulBeat i heron |
| `typ-h2` | Instrument Serif 400, .95, −.01em | clamp(2.6rem, 11vw, 4.6rem) | Sektionsrubrik |
| `typ-tagline` | Instrument Serif kursiv, 1.2 | clamp(1.45rem, 6vw, 2.1rem) | Heroens tagline |
| `typ-lead-big` | Instrument Serif, 1.25 | clamp(1.45rem, 5.6vw, 1.9rem) | Stor ingress |
| `typ-h3` | Instrument Serif, 1.1 | 1.7rem | Underrubrik |
| `typ-quote` | Instrument Serif, 1.3 | 1.45rem | Citat, FAQ-frågor, faktavärden |
| `typ-date-number` | Instrument Serif, .9 | 6.4rem | Dagen i datumkortet |
| `typ-body` | Manrope 400, 1.65 | 1.02rem | Brödtext |
| `typ-button` | Manrope 700 | .96rem | Knappar |
| `typ-kicker` | Manrope 700, versaler, spärrning .2em | .78rem | Etiketten ovanför h2, i rust |
| `typ-label` | Manrope 700, versaler, .16em | .72rem | Etiketter i faktarader och kontaktlista |

## Form

- **Valv:** radie 999px 999px 0 0 på `div.arch`. Alla bilder utom bandet ligger i valv.
- **Piller:** knappar och e-postfältet har radien `pill` (999px) och kanten `button` (1,5 px ink).
- **Kort:** datumkortet och bandet har radien `card` (22 px). Inga andra kort finns.
- **Linjer:** 1 px `line` mellan rader; 2 px `ink` ovanför citat; 10 px `ink` som horisont.
- **Fokus:** 2 px `rust` med 3 px avstånd.
- **Mått:** innehållet högst `maxw` 1180 px. Sidmarginal 20 px, från 760 px 40 px. Sektionsluft 76 px, från 760 px 110 px.

## Bilder

Bara `alexis-dans.webp` är skarp i fullbredd. De andra är uppskalade och mjuka, därför ligger de i små valv.

| Kvalitet | Filer | Visas högst |
|---|---|---|
| skarp | alexis-dans | Bandet: full innehållsbredd, högst 600 px hög, object-position 62 % 12 % |
| god | louna-shamantrumma | Heroens valv, 360 px |
| mjuk | alexis-gitarr, alexis-piippo, louna-trad-meditation, louna-ponyo-eld, louna-dans-1, louna-dans-2, louna-ponyo-dans-glad, louna-grounding, soulbeat-altare | Valv 220–320 px |
| mjukast | louna-kora, louna-handpan, louna-gong-meditation, louna-gong-ljus, louna-ponyo-ramtrummor | Valv högst 150–220 px |
| används inte | louna-ponyo-dans | För suddig |

## Logga

Solpuls: en halv sol i solgradienten, en ljus rand över solen och horisontlinjen som slår ett hjärtslag upp genom solen. viewBox 0 0 120 72.

- `solpuls.svg`: på bg och bg-2. Randen i `bg`, linjen i `ink`.
- `solpuls-pa-ink.svg`: på ink (datumkortet, sidfoten). Randen i `ink`, linjen i `cream-on-ink`.
- `favicon.svg`: 64 × 64 med rundade hörn, på bg.
- `sol-randig.svg`: heroens halvsol, 560 × 280.

Bredvid märket i menyn står "SoulBeat" i Instrument Serif 1.5rem. Märket är 50 px brett i menyn och 150 px i sidfoten.

## Laddning

Typsnitten kommer från Google Fonts: tre filer (Instrument Serif rak och kursiv, Manrope variabel), 55 kB överfört, från två domäner (fonts.googleapis.com och fonts.gstatic.com). Lighthouse mobil 2026-10-15: FCP 3,5 s, LCP 3,6 s, CLS 0,033. Budget: högst tre typsnittsfiler och 70 kB. Lägg inte till fler vikter eller familjer.

### Lighthouse-budget

`design/lighthouserc.json` (Lighthouse CI, `npx @lhci/cli autorun --config=design/lighthouserc.json`). Lighthouse 12 och senare har tagit bort `--budget-path`, så budgeten finns bara i CI-formatet.

| | Mätt 2026-10-15 (mobil) | Budget |
|---|---|---|
| Typsnittsfiler | 3 (Instrument Serif rak + kursiv, Manrope) | högst 3 |
| Typsnittsvikt | 55 kB | högst 70 kB |
| Tredjepartsdomäner | 2 (Google Fonts) | högst 3 (varning) |
| FCP / LCP | 3,5 s / 3,6 s | varning över 1,8 s / 2,5 s |
| CLS | 0,033 | högst 0,05 |

LCP och FCP ligger över riktvärdena i dag. Den största delen är Google Fonts-CSS:en som blockerar renderingen. Det billigaste steget, om det blir aktuellt, är att självhosta samma tre typsnittsfiler; utseendet ändras inte.

## Blindtest: ser Gryning AI-gjord ut?

Testsidan för mobilen: https://claude.ai/artifact/9XxLohLidc2rvjBJfcVN4r (privat tills du delar den; du kan också visa den från din egen inloggning).

**Material.** Första skärmen för fem eventsajter med samma typ av innehåll och samma bilder: soulbeat.se (Gryning) och fyra sajter som separata Claude-agenter byggde 2026-10-15 utan designanvisningar (Daybreak Malmö, Vakna, Rytm & Ro, Morgonpuls). Alla fyra valde själva kräm, terrakotta, en serif med ett kursivt ord i rubriken och pillerknappar, alltså samma familj som Gryning. Testet visar om SoulBeat ändå sticker ut.

**Upplägg (fem personer, ca 3 minuter var).**

1. Öppna testsidan på mobilen och välj person 1–5 och Mobil. Varje person får sajterna i egen ordning.
2. Säg: "Du får se fem webbsidor för event, fem sekunder var. Efter varje får du svara på en fråga." Nämn inte AI eller vilken som är vår.
3. Efter varje sajt: "Hur ser sajten ut att vara gjord, 1 = av en människa, 5 = av en AI?"
4. Efter alla fem: "Vilken skulle du helst gå på?" och "Vilket eventnamn minns du utan att titta?"
5. Kopiera personens rad till tabellen. Välj personer som inte jobbar med webb och inte har sett soulbeat.se.

**Godkänt** om alla tre stämmer: B har lägst snitt på AI-frågan; högst en av fem ger B en 4:a eller 5:a; minst tre av fem minns namnet SoulBeat. Klarar Gryning inte testet är det mest lönsamma steget att förstärka de egna motiven (Solpuls, den randiga solen, solen som stiger) snarare än att byta stil.

**Facit:** A = Rytm & Ro, B = SoulBeat (Gryning), C = Daybreak Malmö, D = Morgonpuls, E = Vakna.

| Person | A | B | C | D | E | Helst | Minns |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| Snitt | | | | | | | |

## Öppna frågor till Alexis

1. **"Redo för både jobbet och helgen"** står kvar i Om-texten och FAQ:n från tiden när det slutade 11. Ska jobbvinkeln vara kvar nu när det slutar 12?
2. **Mappen `design/` och DESIGN.md publiceras** med sajten vid nästa push (Netlify publicerar hela repot). Det är ofarligt, men säg till om de hellre ska ligga utanför.
