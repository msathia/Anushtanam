"""Protect the reviewed Apastamba readings from period or Veda mix-ups."""

import unittest

from test_sandhyavandanam import Document, ROOT


PAGES = {
    "pratah-sandhyavandanam": {
        "period": "ப்ராத: ஸந்த்யா", "worship": "ப்ராத: ஸந்த்யாம் உபாஸிஷ்யே",
        "direction": "கிழக்கு", "arghyas": 3, "japa": 108,
        "prashana": ("ஸூர்யச்ச மா", "யத்ராத்ர்யா", "ராத்ரிஸ்ததவலும்பது", "ஸூர்யே ஜ்யோதிஷி"),
        "upasthana": ("சர்ஷணீத்ருத: ச்ரவோ", "ஸத்யம் சித்ரச்ரவஸ்தமம்", "யாதயதி ப்ரஜாநந்", "ஸத்யாய ஹவ்யம் க்ருதவத் விதேம", "ப்ர ஸ மித்ர"),
        "parts": 3,
    },
    "madhyanikam": {
        "period": "மாத்யாஹ்நிக", "worship": "மாத்யாஹ்நிகம் கரிஷ்யே",
        "direction": "கிழக்கு", "arghyas": 2, "japa": 32,
        "prashana": ("ஆப: புநந்து", "ப்ருதிவீ பூதா", "மாமாபோऽஸதாம் ச ப்ரதிக்ரஹம்"),
        "upasthana": ("ஆ ஸத்யேந ரஜஸா", "பச்யந்தோ ஜ்யோதிருத்தரம்", "உது த்யம் ஜாதவேதஸம்", "சித்ரம் தேவாநாம்", "ஸூர்ய ஆத்மா", "தச்சக்ஷுர்தேவஹிதம்", "ஜ்யோக்ச ஸூர்யம் த்ருசே", "ஸலிலஸ்ய மத்யாத்", "விபச்சிந்மநஸா புநாது"),
        "parts": 6,
    },
    "saayam-sandhyavandanam": {
        "period": "ஸாயம் ஸந்த்யா", "worship": "ஸாயம் ஸந்த்யாம் உபாஸிஷ்யே",
        "direction": "மேற்கு", "arghyas": 3, "japa": 64,
        "prashana": ("அக்நிச்ச மா", "யதஹ்நா", "அஹஸ்ததவலும்பது", "ஸத்யே ஜ்யோதிஷி"),
        "upasthana": ("இமம் மே வருண", "ம்ருடய", "அஹேடமாநோ", "யச்சித்தி தே", "யத்கிஞ்சேதம்", "கிதவாஸோ", "வருண ப்ரியாஸ:"),
        "parts": 5,
    },
}


class YajurvedaSandhyavandanamTests(unittest.TestCase):
    def test_period_specific_sankalpams_and_prashanam(self):
        for suffix, expected in PAGES.items():
            with self.subTest(page=suffix):
                doc = Document(ROOT / ("yajurveda-" + suffix) / "index.html")
                self.assertIn(expected["worship"], doc.section("sankalpam"))
                for section, ending in (
                    ("japa-sankalpam", "காயத்ரீ மஹாமந்த்ர ஜபம் கரிஷ்யே"),
                    ("prayaschitta", "காலாதீத ப்ராயச்சித்தார்த்தம் அர்க்யப்ரதாநம் கரிஷ்யே"),
                    ("upasthana-sankalpam", "உபஸ்தாநம் கரிஷ்யே"),
                ):
                    text = doc.section(section)
                    self.assertIn(expected["period"] + " " + ending, text)
                    self.assertIn("ஸ்ரீ பரமேச்வர ப்ரீத்யர்த்தம்", text)
                    for other in PAGES.values():
                        if other is not expected:
                            self.assertNotIn(other["period"], text)
                for phrase in expected["prashana"]:
                    self.assertIn(phrase, doc.section("prashanam"))
                for other in PAGES.values():
                    if other is not expected:
                        self.assertNotIn(other["prashana"][0], doc.section("prashanam"))

    def test_complete_yajurveda_upasthana_readings(self):
        for suffix, expected in PAGES.items():
            with self.subTest(page=suffix):
                path = ROOT / ("yajurveda-" + suffix) / "index.html"
                doc = Document(path)
                for phrase in expected["upasthana"]:
                    self.assertIn(phrase, doc.section("upasthanam"))
                for other in PAGES.values():
                    if other is not expected:
                        self.assertNotIn(other["upasthana"][0], doc.section("upasthanam"))
                self.assertEqual(path.read_text().count('data-upasthana-part="'), expected["parts"])
                self.assertEqual(doc.verses, [])
                for phrase in ("சர்ஷணீத்ருதோऽவோ", "யாதயதி ப்ருவாணோ", "ஜ்யோதிஷ்பச்யந்த உத்தரம்", "ம்ருளய", "அஹேளமாநோ"):
                    self.assertNotIn(phrase, doc.section("upasthanam"))

    def test_apastamba_identity_arghyam_and_no_rigveda_only_steps(self):
        for suffix, expected in PAGES.items():
            with self.subTest(page=suffix):
                doc = Document(ROOT / ("yajurveda-" + suffix) / "index.html")
                text = " ".join(doc.text)
                self.assertIn("க்ருஷ்ண யஜுர்வேதம்", text)
                self.assertIn("தைத்திரீய சாகை", text)
                self.assertIn("ஆபஸ்தம்ப ஸூத்ர: யஜுச்சாகாத்யாயீ", doc.section("abhivadanam"))
                for forbidden in ("ஆச்வலாய", "ருக்சாகாத்யாயீ", "யதத்ய கச்ச", "உத்கேதபி", "ந தஸ்ய மாயயா", "பிசங்கப்ருஷ்டிம்", "கேச்யக்நிம்", "பூர்புவஸ்ஸ்வ:"):
                    self.assertNotIn(forbidden, text)
                self.assertNotIn("brahma-yagnam-section", doc.ids)
                self.assertFalse(any("brahma-yagnam.html" in link for link in doc.links))
                self.assertIn("ஆஸன ப்ரார்த்தனை", doc.section("asanam"))
                self.assertIn("தன்ம ஆ ஸுவ", doc.section("completion"))
                for section in ("arghyam", "prayaschitta", "gayatri-japam"):
                    self.assertIn("ஓம் பூர்புவஸ்ஸுவ:", doc.section(section))
                for section in ("arghyam", "upasthanam"):
                    self.assertIn(expected["direction"] + " நோக்கி நின்று", doc.section(section))
                self.assertIn(str(expected["arghyas"]) + " முறை", doc.section("arghyam"))
                self.assertIn(str(expected["japa"]) + " முறை", doc.section("gayatri-japam"))
                self.assertIn("காலம் கடந்திருந்தால்", doc.section("prayaschitta"))
                self.assertIn("ஒரு முறை கூடுதல் அர்க்யம்", doc.section("prayaschitta"))

    def test_home_and_period_navigation(self):
        home = Document(ROOT / "index.html")
        for suffix in PAGES:
            self.assertEqual(home.links.count("yajurveda-" + suffix + "/"), 1)
            self.assertEqual(home.links.count("rigveda-" + suffix + "/"), 1)
            doc = Document(ROOT / ("yajurveda-" + suffix) / "index.html")
            for target in PAGES:
                self.assertEqual(doc.links.count("../yajurveda-" + target + "/"), 1)


if __name__ == "__main__":
    unittest.main()
