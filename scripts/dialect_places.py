"""Where each regional dialect is spoken — as a Wikidata PLACE, never a typed point.

Glottolog gives a point to every languoid it catalogues, but it does not catalogue
dialects like Portuense, Paisa, or the Aragonese of the Bielsa valley. Those specs
are exactly the ones where geography matters most: a dialect continuum IS a
geographic object.

So each such spec is anchored to a **place**, identified by its Wikidata item, and
the coordinate is fetched from that item's P625 at generation time by
``scripts/gen_locations.py``. Nothing here is a hand-typed latitude. A wrong entry
can therefore only ever be the wrong PLACE — never a transposed or invented
coordinate — and ``--check`` verifies each place still sits in the country it is
supposed to, by reading the item's P17.

Each entry says:

* ``qid``    — the Wikidata item for the place or region.
* ``label``  — the item's expected English label. Guards against a QID typo silently
               resolving to some unrelated item.
* ``country``— the expected value of the item's P17 (``None`` for historical items
               that predate any modern state). Guards against the wrong-country class
               of bug that has bitten this project before.
* ``note``   — what the point actually REPRESENTS. A city where the variety is
               centred is strong; a country standing in for a national variety is
               weak, and the note must say so.
"""
from __future__ import annotations

# A spec deliberately left with no location, and why. Absence is a finding, not a
# gap: a made-up point would silently corrupt every geographic comparison.
UNLOCATABLE = {
    "ar-x-mashriqi": "Abstract reconstructed ancestor node for Eastern Arabic. A "
                     "proto-language has no attested territory; its homeland would "
                     "be a guess.",
    "xpa": "Proto-Arabic / Old Arabic is reconstructed. The Arabic Urheimat is "
           "debated (North Arabian oases vs. wider Arabia); this project does not "
           "pick a side in an open question.",
    "brx-x-proto-boro-garo": "Reconstructed proto-language. The Boro-Garo homeland "
                             "(Brahmaputra valley vs. further east) is contested.",
    "fa-x-early": "Classical Persian is a supraregional literary koine — written "
                  "from Khorasan and Transoxiana to Anatolia and India. No single "
                  "point represents it; the corpus is the language, not a place.",
    "x-clade-gallorom": "Classification-only clade node — an abstraction, not a "
                        "speech community.",
    "x-clade-iberrom": "Classification-only clade node.",
    "x-clade-italorom": "Classification-only clade node.",
    "x-clade-tyrsen": "Classification-only clade node.",
    "x-clade-vascon": "Classification-only clade node.",
}

PLACES: dict[str, dict] = {
    # ── Aragonese: each variety IS a Pyrenean valley ──────────────────────────
    "an-x-belsetan": dict(
        qid="Q21036658", label="Bielsa Valley", country="Spain",
        note="the Bielsa valley (Sobrarbe, Huesca) — the valley the variety is "
             "named for and confined to."),
    "an-x-cheso": dict(
        qid="Q1766550", label="Valle de Hecho", country="Spain",
        note="the Echo/Hecho valley (Huesca) — the valley the variety is named "
             "for and confined to."),
    "an-x-chistabin": dict(
        qid="Q3102588", label="Gistau Valley", country="Spain",
        note="the Gistaín/Chistau valley (Sobrarbe, Huesca) — the valley the "
             "variety is named for and confined to."),
    "an-x-tensino": dict(
        qid="Q3054031", label="Tena Valley", country="Spain",
        note="the Valle de Tena (Alto Gállego, Huesca) — the valley the variety is "
             "named for and confined to."),

    # ── Astur-Leonese ─────────────────────────────────────────────────────────
    "ast-ES-x-leon": dict(
        qid="Q71140", label="León Province", country="Spain",
        note="the province of León — the core of the Leonese area, which also "
             "reaches into Zamora and Salamanca. A province-wide point, not a town."),
    "ast-PT-x-guadramil": dict(
        qid="Q8965253", label="Guadramil, Aveleda e Rio de Onor, Bragança",
        country="Portugal",
        note="Guadramil (Bragança) — the single border village the variety is "
             "spoken in."),
    "ast-PT-x-rionor": dict(
        qid="Q2119682", label="Freguesia de Rio de Onor", country="Portugal",
        note="Rio de Onor (Bragança) — the single border village, straddling the "
             "frontier with Rihonor de Castilla, that the variety is spoken in."),
    "ast-PT-x-medieval": dict(
        qid="Q373475", label="Miranda do Douro", country="Portugal",
        note="Miranda do Douro — the centre of the Terra de Miranda, where the "
             "medieval Asturleonese of Portugal took root. A historical variety: "
             "the point is the surviving core of its area, not a capital."),
    "ast-x-sanabria": dict(
        qid="Q2605814", label="Sanabria", country="Spain",
        note="the Sanabria comarca (Zamora) — the centre of the Sanabrese area, "
             "which continues across the border into Guadramil and Rio de Onor."),

    # ── Historical / superstrate ──────────────────────────────────────────────
    "cel-x-gallaecia": dict(
        qid="Q369692", label="Gallaecia", country=None,
        note="the Roman province of Gallaecia — the NW-Iberian territory the "
             "Gallaecian Celtic epigraphic and toponymic record comes from. A "
             "province-wide point for an extinct language: weak by construction."),
    "gem-x-suebi": dict(
        qid="Q83247", label="Braga", country="Portugal",
        note="Braga (Bracara Augusta) — capital of the Suebic kingdom of Gallaecia "
             "(411–585). Suebic Germanic is attested only as a superstrate here; "
             "the point marks the kingdom's seat, not a speech community."),
    "la-x-gallia": dict(
        qid="Q38060", label="Gaul", country=None,
        note="Gaul — the territory whose spoken Latin this stage describes. A point "
             "for a whole Roman diocese: a centroid, and weak."),
    "xlg": dict(
        qid="Q9671294", label="Cabeço das Fráguas", country="Portugal",
        note="Cabeço das Fráguas (Guarda) — the site of the principal Lusitanian "
             "inscription, and the centre of the handful of finds the language is "
             "known from. Glottolog has the languoid but no coordinate."),
    "xaq": dict(
        qid="Q715376", label="Gallia Aquitania", country=None,
        note="Roman Aquitania — the province the Aquitanian onomastic inscriptions "
             "come from. A province-wide point for a fragmentarily attested language."),

    # ── Standard national varieties (weak points — a nation is not a place) ───
    "da-x-copenhagen": dict(
        qid="Q1748", label="Copenhagen", country="Denmark",
        note="Copenhagen — the city rigsdansk is the speech of."),
    "sv-x-rikssvenska": dict(
        qid="Q1754", label="Stockholm", country="Sweden",
        note="Stockholm — Rikssvenska is the Central Swedish standard of the "
             "Stockholm area."),
    "de-AT": dict(
        qid="Q40", label="Austria", country="Austria",
        note="Austria's representative point. A national standard has no single "
             "locus; this is a weak, country-level stand-in."),
    "de-CH": dict(
        qid="Q39", label="Switzerland", country="Switzerland",
        note="Switzerland's representative point — and only the German-speaking "
             "north and east are meant. A weak, country-level stand-in."),
    "nl-BE": dict(
        qid="Q9337", label="Flemish Region", country="Belgium",
        note="the Flemish Region — the Dutch-speaking part of Belgium, not Belgium "
             "as a whole. A region-level point."),
    "en-GB-x-scotland": dict(
        qid="Q22", label="Scotland", country="United Kingdom",
        note="Scotland's representative point. A country-wide variety: weak."),
    "en-US": dict(
        qid="Q30", label="United States", country="United States",
        note="the geographic centre of the United States. General American is a "
             "media/education reference accent with NO regional home at all — this "
             "is the weakest point in the dataset and should be read as such."),
    "ar-NG": dict(
        qid="Q130626", label="Borno State", country="Nigeria",
        note="Borno State — the Nigerian heartland of Shuwa Arabic, which also "
             "reaches Yobe, Cameroon and Niger."),

    # ── Basque ────────────────────────────────────────────────────────────────
    "eu-x-nafarra-beherea": dict(
        qid="Q638503", label="Lower Navarre", country="France",
        note="Lower Navarre (Basse-Navarre, Pyrénées-Atlantiques) — the historical "
             "province the dialect is named for."),
    "eu-x-nafarra-garaia": dict(
        qid="Q10282", label="Pamplona", country="Spain",
        note="Pamplona — the centre of the Pamplona basin and of the High Navarrese "
             "area."),

    # ── Galician ──────────────────────────────────────────────────────────────
    "gl-x-occidental": dict(
        qid="Q12411", label="Pontevedra", country="Spain",
        note="Pontevedra — a representative locality of the western Galician block "
             "(Pontevedra province and coastal A Coruña), the gheada heartland."),
    "gl-x-central": dict(
        qid="Q11125", label="Lugo", country="Spain",
        note="Lugo — a representative locality of the central Galician block (Lugo, "
             "eastern A Coruña, Ourense)."),
    "gl-x-oriental": dict(
        qid="Q1465213", label="A Fonsagrada", country="Spain",
        note="A Fonsagrada (eastern Lugo, on the Asturian border) — a representative "
             "locality of the eastern Galician block, where Asturleonese contact is "
             "strongest."),
    "gl-x-reintegrado": dict(
        qid="Q3908", label="Galicia", country="Spain",
        note="Galicia. This spec is an ORTHOGRAPHY, not a speech variety — it shares "
             "its phonology and its territory with `gl`, so it shares its point."),

    # ── Spanish: Iberia ───────────────────────────────────────────────────────
    "es-ES-x-cantabria": dict(
        qid="Q3946", label="Cantabria", country="Spain",
        note="Cantabria — the autonomous community the Montañés variety is spoken in."),
    "es-ES-x-extremadura": dict(
        qid="Q5777", label="Extremadura", country="Spain",
        note="Extremadura (Cáceres and Badajoz) — the autonomous community the "
             "variety is spoken in."),

    # ── Spanish: the Americas and Africa ──────────────────────────────────────
    "es-CO": dict(
        qid="Q2841", label="Bogotá", country="Colombia",
        note="Bogotá — the highland city whose rolo speech this spec models."),
    "es-CO-x-paisa": dict(
        qid="Q48278", label="Medellín", country="Colombia",
        note="Medellín — the centre of the Paisa/Antioqueño area."),
    "es-CO-x-costa": dict(
        qid="Q62823", label="Barranquilla", country="Colombia",
        note="Barranquilla — a representative city of the Colombian Caribbean coast "
             "(with Cartagena and Santa Marta)."),
    "es-CO-x-llanero": dict(
        qid="Q749224", label="Villavicencio", country="Colombia",
        note="Villavicencio — the gateway city of the Llanos Orientales; the Llanero "
             "area continues across the border into Venezuela."),
    "es-CO-x-pacifico": dict(
        qid="Q996581", label="Buenaventura", country="Colombia",
        note="Buenaventura — the principal city of the Colombian Pacific coast "
             "(Chocó–Valle littoral)."),
    "es-CO-x-santander": dict(
        qid="Q243766", label="Bucaramanga", country="Colombia",
        note="Bucaramanga — the capital of Santander and centre of the "
             "Santandereano area."),
    "es-VE-x-maracucho": dict(
        qid="Q171632", label="Maracaibo", country="Venezuela",
        note="Maracaibo — the centre of the Maracucho/Zuliano area."),
    "es-VE-x-andino": dict(
        qid="Q23551", label="Mérida", country="Venezuela",
        note="Mérida (Venezuela) — the principal city of the Venezuelan Andes "
             "(Mérida/Táchira 'gocho' highlands)."),
    "es-VE-x-llanero": dict(
        qid="Q695623", label="Barinas", country="Venezuela",
        note="Barinas — a representative city of the Venezuelan interior plains "
             "(Llanos)."),
    "es-EC": dict(
        qid="Q2900", label="Quito", country="Ecuador",
        note="Quito — the highland capital whose sierra speech this spec models."),
    "es-EC-x-andino": dict(
        qid="Q2900", label="Quito", country="Ecuador",
        note="Quito — the centre of the Ecuadorian sierra."),
    "es-EC-x-costa": dict(
        qid="Q43509", label="Guayaquil", country="Ecuador",
        note="Guayaquil — the centre of the Ecuadorian coast."),
    "es-PE": dict(
        qid="Q5582862", label="Cusco", country="Peru",
        note="Cusco — a representative city of the Peruvian Andean highlands, which "
             "is what this national spec actually describes."),
    "es-PE-x-andino": dict(
        qid="Q5582862", label="Cusco", country="Peru",
        note="Cusco — a representative city of the Peruvian Andean highlands."),
    "es-PE-x-lima": dict(
        qid="Q2868", label="Lima", country="Peru",
        note="Lima — the coastal capital whose speech this spec models."),
    "es-PE-x-amazonico": dict(
        qid="Q193289", label="Iquitos", country="Peru",
        note="Iquitos — the principal city of the Peruvian Amazon (Loreto/Ucayali)."),
    "es-BO-x-camba": dict(
        qid="Q170688", label="Santa Cruz de la Sierra", country="Bolivia",
        note="Santa Cruz de la Sierra — the centre of the Camba eastern lowlands."),
    "es-CL-x-andino": dict(
        qid="Q2203", label="Arica", country="Chile",
        note="Arica — the northern Chilean city at the Andean/Altiplano edge."),
    "es-CL-x-chilote": dict(
        qid="Q177608", label="Chiloé Archipelago", country="Chile",
        note="the Chiloé archipelago — the island group the variety is named for."),
    "es-AR-x-cordoba": dict(
        qid="Q44210", label="Córdoba", country="Argentina",
        note="Córdoba (Argentina) — the centre of the Cordobés area."),
    "es-AR-x-cuyo": dict(
        qid="Q1146743", label="Cuyo", country="Argentina",
        note="the Cuyo region (Mendoza, San Juan, San Luis) — a region-level point."),
    "es-AR-x-litoral": dict(
        qid="Q44211", label="Corrientes", country="Argentina",
        note="Corrientes — a representative city of the Guaraní-contact Litoral "
             "(Corrientes and Misiones)."),
    "es-AR-x-norte": dict(
        qid="Q36307", label="Salta", country="Argentina",
        note="Salta — the principal city of the Argentine Andean northwest."),
    "es-AR-x-patagonia": dict(
        qid="Q1507", label="Patagonia", country=None,
        note="Patagonia — a region-level centroid spanning Argentina and Chile; the "
             "spec is the Argentine side. A weak point."),
    "es-MX-x-costa": dict(
        qid="Q173270", label="Veracruz", country="Mexico",
        note="Veracruz — a representative city of the Mexican Gulf lowlands "
             "(Veracruz, Tabasco)."),
    "es-MX-x-yucatan": dict(
        qid="Q165204", label="Mérida", country="Mexico",
        note="Mérida (Yucatán) — the centre of the Yucatán peninsula."),
    "es-CR": dict(
        qid="Q3070", label="San José", country="Costa Rica",
        note="San José — the Central Valley capital, the reference for the "
             "conservative Costa Rican norm."),
    "es-GT": dict(
        qid="Q1555", label="Guatemala City", country="Guatemala",
        note="Guatemala City — the highland capital. A national variety: the point "
             "stands in for the country."),
    "es-HN": dict(
        qid="Q3238", label="Tegucigalpa", country="Honduras",
        note="Tegucigalpa. A national variety: the capital stands in for the country."),
    "es-NI": dict(
        qid="Q3274", label="Managua", country="Nicaragua",
        note="Managua. A national variety: the capital stands in for the country."),
    "es-SV": dict(
        qid="Q3110", label="San Salvador", country="El Salvador",
        note="San Salvador. A national variety: the capital stands in for the country."),
    "es-PA": dict(
        qid="Q3306", label="Panama City", country="Panama",
        note="Panama City. A national variety: the capital stands in for the country."),
    "es-PY": dict(
        qid="Q2933", label="Asunción", country="Paraguay",
        note="Asunción. A national variety: the capital stands in for the country."),
    "es-UY": dict(
        qid="Q1335", label="Montevideo", country="Uruguay",
        note="Montevideo. A national variety: the capital stands in for the country."),
    "es-GQ": dict(
        qid="Q3818", label="Malabo", country="Equatorial Guinea",
        note="Malabo. A national L2 variety: the capital stands in for the country, "
             "and the point ignores the mainland/island split. Weak."),

    # ── Persian ───────────────────────────────────────────────────────────────
    "fa-x-tehran": dict(
        qid="Q3616", label="Tehran", country="Iran",
        note="Tehran — the city whose speech IS the Iranian standard."),
    "fa-x-isfahani": dict(
        qid="Q42053", label="Isfahan", country="Iran",
        note="Isfahan — the city the variety is named for."),
    "fa-x-kermani": dict(
        qid="Q171714", label="Kerman", country="Iran",
        note="Kerman — the city the variety is named for."),
    "fa-x-mashhadi": dict(
        qid="Q121157", label="Mashhad", country="Iran",
        note="Mashhad — the city the variety is named for."),
    "fa-x-shirazi": dict(
        qid="Q6397066", label="Shiraz", country="Iran",
        note="Shiraz — the city the variety is named for."),
    "fa-x-yazdi": dict(
        qid="Q182394", label="Yazd", country="Iran",
        note="Yazd — the city the variety is named for."),

    # ── Italian ───────────────────────────────────────────────────────────────
    "it-IT-x-abruzzo": dict(
        qid="Q1284", label="Abruzzo", country="Italy",
        note="Abruzzo — the region the dialect is named for (it reaches into Molise)."),
    "it-IT-x-calabria": dict(
        qid="Q1458", label="Calabria", country="Italy",
        note="Calabria — a region-level point for an internally diverse area "
             "(northern Calabria patterns with Neapolitan, southern with Sicilian)."),
    "it-IT-x-marche": dict(
        qid="Q1279", label="Marche", country="Italy",
        note="Marche — a region-level point for a transitional dialect area."),
    "it-IT-x-puglia": dict(
        qid="Q1447", label="Apulia", country="Italy",
        note="Puglia — a region-level point; the Salento south differs from the north."),
    "it-IT-x-roma": dict(
        qid="Q220", label="Rome", country="Italy",
        note="Rome — the city Romanesco is the dialect of."),
    "it-IT-x-toscana": dict(
        qid="Q1273", label="Tuscany", country="Italy",
        note="Tuscany — the region whose dialect is the basis of standard Italian."),
    "it-IT-x-umbria": dict(
        qid="Q1280", label="Umbria", country="Italy",
        note="Umbria — the region the (modern Romance) dialect is named for."),

    # ── Mirandese ─────────────────────────────────────────────────────────────
    "mwl-x-ifanes": dict(
        qid="Q1657046", label="Freguesia de Ifanes", country="Portugal",
        note="Ifanes (Infainç) — the northern Terra de Miranda village the "
             "sub-dialect is named for."),
    "mwl-x-sendim": dict(
        qid="Q2121828", label="Freguesia de Sendim", country="Portugal",
        note="Sendim — the southern Terra de Miranda village the sub-dialect is "
             "named for."),

    # ── European Portuguese ───────────────────────────────────────────────────
    "pt-PT-x-porto": dict(
        qid="Q36433", label="Porto", country="Portugal",
        note="Porto — the city the Portuense variety is named for."),
    "pt-PT-x-braga": dict(
        qid="Q83247", label="Braga", country="Portugal",
        note="Braga — the city the Bracarense variety is named for."),
    "pt-PT-x-minho": dict(
        qid="Q512317", label="Minho", country="Portugal",
        note="the historical Minho province — the Baixo-Minho zone (Braga, "
             "Guimarães, Vizela) the variety covers."),
    "pt-PT-x-viana": dict(
        qid="Q208158", label="Viana do Castelo", country="Portugal",
        note="Viana do Castelo — the centre of the Alto Minho."),
    "pt-PT-x-trasosmontes": dict(
        qid="Q369458", label="Trás-os-Montes e Alto Douro", country="Portugal",
        note="the centre of the Trás-os-Montes e Alto Douro dialect area (Bragança, "
             "Chaves, Valpaços) — a province-level point, not a town."),
    "pt-PT-x-alfena": dict(
        qid="Q1971893", label="Alfena", country="Portugal",
        note="Alfena (Valongo, Greater Porto) — the single locality the "
             "vowel-breaking variety is described for."),
    "pt-PT-x-aveiro": dict(
        qid="Q485581", label="Aveiro", country="Portugal",
        note="Aveiro — the centre of the Beira Litoral coastal zone (Aveiro, Vagos)."),
    "pt-PT-x-beira": dict(
        qid="Q117676", label="Viseu", country="Portugal",
        note="Viseu — a representative locality of the Beiras (Beira Litoral, Alta "
             "and Baixa), an area far larger than any one town."),
    "pt-PT-x-coimbra": dict(
        qid="Q45412", label="Coimbra", country="Portugal",
        note="Coimbra — the city the Conimbricense variety is named for."),
    "pt-PT-x-lisbon": dict(
        qid="Q597", label="Lisbon", country="Portugal",
        note="Lisbon — the city the Estremenho urban variety is named for."),
    "pt-PT-x-alentejo": dict(
        qid="Q443376", label="Upper Alentejo", country="Portugal",
        note="the Alto Alentejo (Portalegre, Évora, Beja) — a subregion-level point."),
    "pt-PT-x-algarve": dict(
        qid="Q26831", label="Algarve", country="Portugal",
        note="the Algarve — Portugal's southernmost region (Faro, Portimão, Lagos)."),
    "pt-PT-x-acores": dict(
        qid="Q25263", label="Azores", country="Portugal",
        note="the Azores archipelago — a centroid over islands whose accents differ "
             "sharply from each other. Weak by construction."),
    "pt-PT-x-sao-miguel": dict(
        qid="Q209036", label="São Miguel Island", country="Portugal",
        note="São Miguel — the eastern Azorean island the micro-variety is named for."),
    "pt-PT-x-madeira": dict(
        qid="Q26253", label="Madeira", country="Portugal",
        note="Madeira (Funchal reference) — the autonomous region the variety is "
             "named for."),
    "ext-PT-x-barrancos": dict(
        qid="Q368867", label="Barrancos", country="Portugal",
        note="Barrancos (Baixo Alentejo) — the single border municipality "
             "Barranquenho is spoken in."),

    # ── Brazilian Portuguese ──────────────────────────────────────────────────
    "pt-BR-x-sp": dict(
        qid="Q174", label="São Paulo", country="Brazil",
        note="São Paulo city — the Paulistano reference variety."),
    "pt-BR-x-rj": dict(
        qid="Q8678", label="Rio de Janeiro", country="Brazil",
        note="Rio de Janeiro city — the Carioca variety."),
    "pt-BR-x-fluminense": dict(
        qid="Q41428", label="Rio de Janeiro", country="Brazil",
        note="the state of Rio de Janeiro — this spec is the state BEYOND the "
             "capital, so the point is the state's centroid, not the city's."),
    "pt-BR-x-mg": dict(
        qid="Q42800", label="Belo Horizonte", country="Brazil",
        note="Belo Horizonte — the centre of the Mineiro area."),
    "pt-BR-x-bahia": dict(
        qid="Q36947", label="Salvador", country="Brazil",
        note="Salvador — the centre of the Baiano area."),
    "pt-BR-x-recife": dict(
        qid="Q48344", label="Recife", country="Brazil",
        note="Recife — the centre of the Pernambucano area."),
    "pt-BR-x-ce": dict(
        qid="Q43463", label="Fortaleza", country="Brazil",
        note="Fortaleza — the centre of the Cearense area."),
    "pt-BR-x-norte": dict(
        qid="Q12829733", label="Belém", country="Brazil",
        note="Belém — the reference city of the Nortista/Amazônico area (with "
             "Manaus, 1,300 km west: a single point is a poor summary of Amazonia)."),
    "pt-BR-x-brasilia": dict(
        qid="Q2844", label="Brasília", country="Brazil",
        note="Brasília — the planned capital whose migration koiné this spec models."),
    "pt-BR-x-caipira": dict(
        qid="Q330175", label="Piracicaba", country="Brazil",
        note="Piracicaba — a representative locality of the caipira area, whose "
             "retroflex-rhotic region stretches from interior São Paulo across "
             "Goiás and Mato Grosso. A point badly under-describes it."),
    "pt-BR-x-pr": dict(
        qid="Q4361", label="Curitiba", country="Brazil",
        note="Curitiba — the centre of the Curitibano/Paranaense area."),
    "pt-BR-x-sul": dict(
        qid="Q40269", label="Porto Alegre", country="Brazil",
        note="Porto Alegre — the centre of the Sulista/Gaúcho area."),

    # ── Portuguese beyond Europe and Brazil ───────────────────────────────────
    "pt-AO": dict(
        qid="Q3897", label="Luanda", country="Angola",
        note="Luanda. A national L2/second-norm variety: the capital stands in for "
             "the country. Weak."),
    "pt-MZ": dict(
        qid="Q3889", label="Maputo", country="Mozambique",
        note="Maputo. A national L2 variety: the capital stands in for the country. "
             "Weak."),
    "pt-CV": dict(
        qid="Q3751", label="Praia", country="Cape Verde",
        note="Praia. The formal L2 Portuguese of Cape Verde — the capital stands in "
             "for the archipelago."),
    "pt-GW": dict(
        qid="Q3739", label="Bissau", country="Guinea-Bissau",
        note="Bissau. Portuguese here is an elite L1/official register — the capital "
             "stands in for the country."),
    "pt-ST": dict(
        qid="Q3932", label="São Tomé", country="São Tomé and Príncipe",
        note="the city of São Tomé. Note the spec's wikidata_qid (Q36536) is Forro "
             "CREOLE, a different language from this Portuguese variety, so it was "
             "NOT used as the source of this point."),
    "pt-TL": dict(
        qid="Q9310", label="Dili", country="Timor-Leste",
        note="Dili. Portuguese is an L2 for nearly all speakers: the capital stands "
             "in for the country."),
    "pt-MO": dict(
        qid="Q14773", label="Macau", country="People's Republic of China",
        note="Macau — the territory this co-official variety is confined to."),
    "pt-UY": dict(
        qid="Q646498", label="Rivera", country="Uruguay",
        note="Rivera — the border city at the heart of the DPU (Uruguayan "
             "Portuguese) area along the Brazilian frontier."),

    # ── Russian ───────────────────────────────────────────────────────────────
    "ru-x-moscow": dict(
        qid="Q649", label="Moscow", country="Russia",
        note="Moscow — the Central Russian city the standard is based on."),
    "ru-x-northern": dict(
        qid="Q2015", label="Vologda Oblast", country="Russia",
        note="Vologda Oblast — a representative point in the Northern Russian "
             "dialect zone (Arkhangelsk–Vologda–Kostroma). A dialect GROUP: the "
             "point is a stand-in for a very large area."),
    "ru-x-arkhangelsk": dict(
        qid="Q1851", label="Arkhangelsk", country="Russia",
        note="Arkhangelsk — the city the Northern subtype is named for."),
    "ru-x-vologda": dict(
        qid="Q1957", label="Vologda", country="Russia",
        note="Vologda — the city the Northern subtype is named for."),
    "ru-x-southern": dict(
        qid="Q2746", label="Ryazan", country="Russia",
        note="Ryazan — a representative point in the Southern Russian dialect zone "
             "(Ryazan, Kursk, Voronezh, Tula). A dialect GROUP: a weak point."),
    "ru-x-kursk-orel": dict(
        qid="Q3159", label="Kursk", country="Russia",
        note="Kursk — the western half of the Kursk–Orel Southern zone."),
    "ru-x-don": dict(
        qid="Q908", label="Rostov-on-Don", country="Russia",
        note="Rostov-on-Don — the principal city of the Don Cossack region."),
    "ru-x-pskov": dict(
        qid="Q2214", label="Pskov", country="Russia",
        note="Pskov — the city of the Pskov–Novgorod transitional zone."),
    "ru-x-siberian": dict(
        qid="Q883", label="Novosibirsk", country="Russia",
        note="Novosibirsk — a representative city of the Siberian old-settler zone "
             "(with Tomsk and Krasnoyarsk). Siberia is 13 million km²: this point "
             "is close to meaningless as a summary and should be treated as such."),
    "ru-x-ural": dict(
        qid="Q887", label="Yekaterinburg", country="Russia",
        note="Yekaterinburg — the principal city of the Urals (with Perm)."),

    # ═════════════════════════════════════════════════════════════════════════
    # Specs that DO have a glottocode, but whose Glottolog point is useless.
    #
    # Glottolog-CLDF gives a dialect the coordinates of its parent LANGUOID. So
    # every Spanish variety it catalogues — Cuban, Mexican, Rioplatense — comes
    # back at 40.44N 1.12W, in Aragón. Brazilian Portuguese comes back in
    # Portugal, Australian English in England, Emirati Arabic near Basra. Those
    # points are not merely coarse, they are in the WRONG COUNTRY, which is the
    # exact failure the geographic axis must never have. The anchors below take
    # precedence over Glottolog for these specs, and ``gen_locations.py --check``
    # reports any newly-duplicated Glottolog point that is not yet anchored.
    # ═════════════════════════════════════════════════════════════════════════

    # ── Spanish ───────────────────────────────────────────────────────────────
    "es-ES": dict(
        qid="Q2807", label="Madrid", country="Spain",
        note="Madrid — the centre of the Castilian norm. Glottolog's point for "
             "cast1244 is the generic Spanish point and says nothing about "
             "Castilian specifically."),
    "es-419": dict(
        qid="Q12585", label="Latin America", country=None,
        note="the centroid of Latin America. A continent-wide cover variety: the "
             "weakest possible point, and only meaningful as 'not Spain' — which "
             "is where Glottolog put it."),
    "es-AR": dict(
        qid="Q1486", label="Buenos Aires", country="Argentina",
        note="Buenos Aires — the city Rioplatense is centred on."),
    "es-BO": dict(
        qid="Q1491", label="La Paz", country="Bolivia",
        note="La Paz — the highland seat of government; this national spec is "
             "Andean-centred."),
    "es-BO-x-andino": dict(
        qid="Q1491", label="La Paz", country="Bolivia",
        note="La Paz — the centre of the Bolivian Andean highlands."),
    "es-CL": dict(
        qid="Q2887", label="Santiago", country="Chile",
        note="Santiago — the central-valley capital, the Chilean reference norm."),
    "es-CU": dict(
        qid="Q1563", label="Havana", country="Cuba",
        note="Havana. A national variety: the capital stands in for the island."),
    "es-DO": dict(
        qid="Q34820", label="Santo Domingo", country="Dominican Republic",
        note="Santo Domingo. A national variety: the capital stands in for the "
             "country."),
    "es-PR": dict(
        qid="Q41211", label="San Juan", country=None,
        note="San Juan, Puerto Rico. A national variety: the capital stands in for "
             "the island."),
    "es-VE": dict(
        qid="Q1533", label="Caracas", country="Venezuela",
        note="Caracas. A national variety: the capital stands in for the country."),
    "es-MX": dict(
        qid="Q1489", label="Mexico City", country="Mexico",
        note="Mexico City — the highland centre this spec models."),
    "es-MX-x-norte": dict(
        qid="Q81033", label="Monterrey", country="Mexico",
        note="Monterrey — the principal city of northern Mexico."),
    "es-CO-x-valluno": dict(
        qid="Q51103", label="Cali", country="Colombia",
        note="Cali — the centre of the Valle del Cauca."),
    "es-ES-x-andalusia-w": dict(
        qid="Q8717", label="Seville", country="Spain",
        note="Seville — the centre of the western Andalusian area."),
    "es-ES-x-andalusia-e": dict(
        qid="Q8810", label="Granada", country="Spain",
        note="Granada — a representative city of the eastern Andalusian area "
             "(with Almería and Jaén)."),
    "es-ES-x-canarias": dict(
        qid="Q5813", label="Canary Islands", country="Spain",
        note="the Canary Islands — the archipelago the variety is spoken in."),
    "es-ES-x-murcia": dict(
        qid="Q5772", label="Region of Murcia", country="Spain",
        note="the Region of Murcia — the community the Panocho variety is spoken in."),

    # ── Portuguese ────────────────────────────────────────────────────────────
    "pt-BR": dict(
        qid="Q155", label="Brazil", country="Brazil",
        note="Brazil's representative point. A national variety spanning a "
             "continent: weak — but Glottolog placed Brazilian Portuguese in "
             "PORTUGAL, which is worse than weak."),

    # ── English ───────────────────────────────────────────────────────────────
    "en-AU": dict(
        qid="Q408", label="Australia", country="Australia",
        note="Australia's representative point. A national variety: weak."),
    "en-CA": dict(
        qid="Q16", label="Canada", country="Canada",
        note="Canada's representative point. A national variety: weak."),
    "en-IE": dict(
        qid="Q27", label="Ireland", country="Ireland",
        note="Ireland's representative point. A national variety: weak."),
    "en-ZA": dict(
        qid="Q258", label="South Africa", country="South Africa",
        note="South Africa's representative point. A national variety: weak."),

    # ── Catalan ───────────────────────────────────────────────────────────────
    "ca-x-valencia": dict(
        qid="Q8818", label="Valencia", country="Spain",
        note="Valencia — the centre of the Valencian area."),
    "ca-x-balear": dict(
        qid="Q8826", label="Palma", country="Spain",
        note="Palma — the centre of the Balearic islands."),
    "ca-x-occidental": dict(
        qid="Q15090", label="Lleida", country="Spain",
        note="Lleida — the centre of the north-western (Lleidatà) area."),
    "ca-x-nord": dict(
        qid="Q6730", label="Perpignan", country="France",
        note="Perpignan — the centre of Northern Catalan (Rossellonès), the only "
             "Catalan variety spoken in France."),

    # ── Asturian ──────────────────────────────────────────────────────────────
    "ast-x-occidental": dict(
        qid="Q737421", label="Cangas del Narcea", country="Spain",
        note="Cangas del Narcea — a representative locality of western Asturias."),
    "ast-x-oriental": dict(
        qid="Q503094", label="Llanes", country="Spain",
        note="Llanes — a representative locality of eastern Asturias."),
    "ast-x-cantabrian": dict(
        qid="Q3946", label="Cantabria", country="Spain",
        note="Cantabria — the community the Cantabrian variety is spoken in."),
    "ast-x-leon": dict(
        qid="Q71140", label="León Province", country="Spain",
        note="the province of León — the core of the Leonese area."),

    # ── Aragonese ─────────────────────────────────────────────────────────────
    "an-x-ansotano": dict(
        qid="Q570484", label="Ansó", country="Spain",
        note="the Ansó valley (Huesca) — the valley the variety is named for."),
    "an-x-occidental": dict(
        qid="Q49581", label="Jaca", country="Spain",
        note="Jaca — a representative locality of the western Aragonese area."),
    "an-x-oriental": dict(
        qid="Q1425491", label="Ribagorza", country="Spain",
        note="the Ribagorza comarca — the eastern (Ribagorçan) Aragonese area, "
             "transitional to Catalan."),

    # ── Basque ────────────────────────────────────────────────────────────────
    "eu-x-bizkaiera": dict(
        qid="Q93366", label="Biscay", country="Spain",
        note="Bizkaia — the province the dialect is named for."),
    "eu-x-gipuzkera": dict(
        qid="Q95010", label="Gipuzkoa", country="Spain",
        note="Gipuzkoa — the province the dialect is named for."),
    "eu-x-lapurtera": dict(
        qid="Q671023", label="Labourd", country="France",
        note="Lapurdi (Labourd) — the historical province the dialect is named for."),
    "eu-x-zuberera": dict(
        qid="Q673040", label="Soule", country="France",
        note="Zuberoa (Soule) — the historical province the dialect is named for."),
    "eu-x-erronkariera": dict(
        qid="Q2165565", label="Roncal-Erronkari Valley", country="Spain",
        note="the Roncal/Erronkari valley (Navarre) — the valley the extinct "
             "dialect was spoken in."),

    # ── Arabic ────────────────────────────────────────────────────────────────
    "ar-JO": dict(
        qid="Q3805", label="Amman", country="Jordan",
        note="Amman — the city the Ammani koine is named for."),
    "ar-LB": dict(
        qid="Q3820", label="Beirut", country="Lebanon",
        note="Beirut — the city the Beiruti variety is named for."),
    "ar-SY": dict(
        qid="Q3766", label="Damascus", country="Syria",
        note="Damascus — the city the Damascene variety is named for."),
    "ar-PS": dict(
        qid="Q158119", label="Ramallah", country=None,
        note="Ramallah — a representative city of the Palestinian area."),
    "ar-AE": dict(
        qid="Q1519", label="Abu Dhabi", country="United Arab Emirates",
        note="Abu Dhabi. A national variety within the Gulf continuum: the capital "
             "stands in for the country."),
    "ar-BH": dict(
        qid="Q3882", label="Manama", country="Bahrain",
        note="Manama. A national variety within the Gulf continuum."),
    "ar-KW": dict(
        qid="Q35178", label="Kuwait City", country="Kuwait",
        note="Kuwait City. A national variety within the Gulf continuum."),
    "ar-QA": dict(
        qid="Q3861", label="Doha", country="Qatar",
        note="Doha. A national variety within the Gulf continuum."),

    # ── Other over-broad Glottolog points ─────────────────────────────────────
    "fa-x-khorasani": dict(
        qid="Q587090", label="Razavi Khorasan Province", country="Iran",
        note="Razavi Khorasan — the province the Khorasani variety is named for. "
             "Glottolog's point for it is the generic Persian point in central Iran."),
    "oc-x-aranes": dict(
        qid="Q12602", label="Val d'Aran", country="Spain",
        note="the Val d'Aran — the single valley Aranese is spoken in. Glottolog's "
             "point for it is the generic Occitan point in Provence."),
}
