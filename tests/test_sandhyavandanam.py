"""Guard against mixing the three daily Rigveda procedures.

Run: python3 -m unittest discover -s tests -v
These checks protect reviewed distinctions; they do not certify pronunciation.
"""

from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "rigveda-pratah-sandhyavandanam": {
        "period": "ப்ராத:", "direction": "கிழக்கு", "arghyas": 3,
        "prashana": ("ஸூர்யச்ச மா", "யத்ராத்ர்யா", "ராத்ரிஸ்ததவலும்பது", "ஸூர்யே ஜ்யோதிஷி"),
        "late": "யதத்ய கச்ச", "up": "மித்ரஸ்ய சர்ஷணீத்ருதோ", "japa": 108,
    },
    "rigveda-madhyanikam": {
        "period": "மாத்யாஹ்நிக", "direction": "கிழக்கு", "arghyas": 2,
        "prashana": ("ஆப: புநந்து", "ப்ருதிவீ பூதா", "மாமாபோऽஸதாம்"),
        "late": "உத்கேதபி", "up": "உது த்யம் ஜாதவேதஸம்", "japa": 32,
    },
    "rigveda-saayam-sandhyavandanam": {
        "period": "ஸாயம்", "direction": "மேற்கு", "arghyas": 3,
        "prashana": ("அக்நிச்ச மா", "யதஹ்நா", "அஹஸ்ததவலும்பது", "ஸத்யே ஜ்யோதிஷி"),
        "late": "ந தஸ்ய மாயயா", "up": "இமம் மே வருண", "japa": 64,
    },
}


class Document(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, path):
        super().__init__()
        self.ids = []
        self.sections = {}
        self.stack = []
        self.links = []
        self.verses = []
        self.text = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        identifier = attrs.get("id")
        if identifier:
            self.ids.append(identifier)
            self.sections[identifier] = []
        if tag not in self.VOID:
            self.stack.append((tag, identifier))
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if "data-rv" in attrs:
            self.verses.append(attrs["data-rv"])

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.text.append(data)
        for _, identifier in self.stack:
            if identifier:
                self.sections[identifier].append(data)

    def section(self, identifier):
        return " ".join(self.sections[identifier])


class SandhyavandanamTests(unittest.TestCase):
    def test_each_page_uses_only_its_own_sankalpams_and_mantras(self):
        for slug, expected in PAGES.items():
            with self.subTest(page=slug):
                doc = Document(ROOT / slug / "index.html")
                for section in ("sankalpam", "japa-sankalpam", "prayaschitta", "upasthana-sankalpam"):
                    text = doc.section(section)
                    self.assertIn(expected["period"] + " ஸந்த்யா", text)
                    self.assertIn("ஸ்ரீ பரமேச்வர ப்ரீத்யர்த்தம்", text)
                    for other in PAGES.values():
                        if other is not expected:
                            self.assertNotIn(other["period"] + " ஸந்த்யா", text)
                for phrase in expected["prashana"]:
                    self.assertIn(phrase, doc.section("prashanam"))
                self.assertIn(expected["late"], doc.section("prayaschitta"))
                self.assertIn(expected["up"], doc.section("upasthanam"))
                for other in PAGES.values():
                    if other is not expected:
                        self.assertNotIn(other["prashana"][0], doc.section("prashanam"))
                        self.assertNotIn(other["late"], doc.section("prayaschitta"))
                        self.assertNotIn(other["up"], doc.section("upasthanam"))
                for section in ("arghyam", "upasthanam"):
                    self.assertIn(expected["direction"] + " நோக்கி நின்று", doc.section(section))
                self.assertIn(str(expected["arghyas"]) + " முறை", doc.section("arghyam"))
                self.assertIn(str(expected["japa"]) + " முறை", doc.section("gayatri-japam"))
                self.assertIn("ஆச்வலாயந ஸூத்ர: ருக்சாகாத்யாயீ", doc.section("abhivadanam"))
                self.assertNotIn("ஆபஸ்தம்ப", " ".join(doc.text))
                self.assertNotIn("யஜு:", " ".join(doc.text))
                self.assertNotRegex(" ".join(doc.text), r"பக்கம்\s+\d")

    def test_noon_has_all_thirteen_surya_verses_and_brahma_yagnam_return(self):
        for slug in PAGES:
            doc = Document(ROOT / slug / "index.html")
            if slug == "rigveda-madhyanikam":
                self.assertEqual(doc.verses, [f"1.50.{n}" for n in range(1, 14)])
                self.assertIn("brahma-yagnam-section", doc.ids)
                self.assertIn("../brahma-yagnam.html", doc.links)
            else:
                self.assertEqual(doc.verses, [])
                self.assertNotIn("brahma-yagnam-section", doc.ids)
        back = Document(ROOT / "brahma-yagnam.html")
        self.assertEqual(back.links.count("rigveda-madhyanikam/#brahma-yagnam-section"), 2)

    def test_all_local_links_and_fragments_resolve(self):
        for path in ROOT.rglob("*.html"):
            doc = Document(path)
            self.assertEqual(len(doc.ids), len(set(doc.ids)), str(path))
            for href in doc.links:
                with self.subTest(page=str(path.relative_to(ROOT)), href=href):
                    url = urlsplit(href)
                    if url.scheme or url.netloc:
                        continue
                    target = (path.parent / unquote(url.path)).resolve() if url.path else path
                    if target.is_dir():
                        target = target / "index.html"
                    self.assertTrue(target.is_file(), str(target))
                    if url.fragment:
                        self.assertIn(unquote(url.fragment), Document(target).ids)

    def test_home_has_three_entries_and_legacy_urls_preserve_anchors(self):
        home = Document(ROOT / "index.html")
        for slug in PAGES:
            self.assertEqual(home.links.count(slug + "/"), 1)
        for name in ("index.html", "Madhyanikam.html"):
            text = (ROOT / "Madhyanikam" / name).read_text()
            self.assertIn("location.replace('../rigveda-madhyanikam/' + location.search + location.hash)", text)
            self.assertIn('content="0; url=../rigveda-madhyanikam/"', text)


if __name__ == "__main__":
    unittest.main()
