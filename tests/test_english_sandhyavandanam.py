"""Protect English recitation coverage and the two traditions' distinctions."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

from test_sandhyavandanam import Document, ROOT

PERIODS = ('pratah', 'madhyanikam', 'saayam')


def slug(veda, period):
    return f'{veda}-' + ('madhyanikam' if period == 'madhyanikam' else f'{period}-sandhyavandanam')


class EnglishSandhyaTests(unittest.TestCase):
    def pages(self):
        for veda in ('yajurveda', 'rigveda'):
            for period in PERIODS:
                path = ROOT / 'en' / slug(veda, period) / 'index.html'
                yield veda, period, path, Document(path)

    def test_english_instructions_and_recitations_without_meanings(self):
        for veda, period, path, doc in self.pages():
            with self.subTest(veda=veda, period=period):
                html = path.read_text()
                self.assertIn('<html lang="en">', html)
                # Only the Tamil language switch may contain Tamil.
                self.assertNotRegex(html.replace('தமிழ்', ''), '[\u0b80-\u0bff]')
                self.assertNotIn('class="meaning"', html)
                self.assertNotIn('meaning', html.lower())
                self.assertGreater(html.count('class="mantra"'), 40)
                count = 39 if veda == 'rigveda' and period == 'madhyanikam' else 38
                self.assertEqual(html.count('<section class="card"'), count)
                for required in ('achamanam', 'anga-vandanam', 'pranayama', 'marjanam', 'punarmarjanam', 'tarpanam', 'avahanam', 'gayatri-nyasa', 'gayatri-dhyanam', 'samarpanam', 'completion'):
                    self.assertIn(required, doc.ids)
                self.assertIn('Vedic svara', doc.section('pronunciation'))
                self.assertIn('not encoded here', doc.section('pronunciation'))
                self.assertIn('ṛ', doc.section('pronunciation'))
                self.assertIn('ṣ', doc.section('pronunciation'))

    def test_period_specific_intentions_and_water_prayers(self):
        prayers = {
            'pratah': ('sūryaś ca mā', 'yad rātryā', 'rātris tad avalumpatu', 'sūrye jyotiṣi'),
            'madhyanikam': ('āpaḥ punantu', "āpo 'satāṃ"),
            'saayam': ('agniś ca mā', 'yad ahnā', 'ahas tad avalumpatu', 'satye jyotiṣi'),
        }
        for veda, period, _, doc in self.pages():
            with self.subTest(veda=veda, period=period):
                label = {'pratah': 'prātaḥ sandhyā', 'madhyanikam': 'mādhyāhnika', 'saayam': 'sāyaṃ sandhyā'}[period]
                for section in ('sankalpam', 'japa-sankalpam', 'upasthana-sankalpam', 'prayaschitta'):
                    text = doc.section(section)
                    self.assertIn(label, text)
                    self.assertIn('śrī parameśvara prītyartham', text)
                    for other in ('prātaḥ sandhyā', 'mādhyāhnika', 'sāyaṃ sandhyā'):
                        if other != label:
                            self.assertNotIn(other, text)
                if period == 'madhyanikam':
                    self.assertIn('mādhyāhnikaṃ kariṣye' if veda == 'yajurveda' else 'mādhyāhnika sandhyām upāsiṣye', doc.section('sankalpam'))
                for phrase in prayers[period]:
                    self.assertIn(phrase, doc.section('prashanam'))
                for other in PERIODS:
                    if other != period:
                        self.assertNotIn(prayers[other][0], doc.section('prashanam'))

    def test_recension_specific_upasthana_and_identity(self):
        for veda, period, path, doc in self.pages():
            with self.subTest(veda=veda, period=period):
                yajur = veda == 'yajurveda'
                up = doc.section('upasthanam')
                self.assertIn('āpastamba sūtraḥ yajuśśākhādhyāyī' if yajur else 'āśvalāyana sūtraḥ ṛkśākhādhyāyī', doc.section('abhivadanam'))
                for field in ('[your pravara sages]', '[your pravara count]', '[your gotra]', '[your name]'):
                    self.assertIn(field, doc.section('abhivadanam'))
                self.assertIn('bhūr bhuvaḥ suvaḥ' if yajur else 'bhūr bhuvaḥ svaḥ', doc.section('gayatri-japam'))
                if yajur:
                    self.assertNotIn('upasthana-prayers', doc.ids)
                    self.assertNotIn('brahma-yagnam-section', doc.ids)
                    self.assertIn('asanam', doc.ids)
                    self.assertEqual(path.read_text().count('data-upasthana-part='), {'pratah': 3, 'madhyanikam': 6, 'saayam': 5}[period])
                    self.assertIn('tat savitur vareṇyaṃ', doc.section('prayaschitta'))
                else:
                    self.assertIn('upasthana-prayers', doc.ids)
                    self.assertIn('duritāty agniḥ', doc.section('upasthana-prayers'))
                    self.assertNotIn('asanam', doc.ids)
                    self.assertIn({'pratah': 'yad adya kac ca', 'madhyanikam': 'ud ghed abhi', 'saayam': 'na tasya māyayā'}[period], doc.section('prayaschitta'))
                if period == 'pratah':
                    self.assertIn('prajānan' if yajur else 'bruvāṇo', up)
                    self.assertIn('satyāya havyaṃ ghṛtavad vidhema' if yajur else 'mitrāya havyaṃ ghṛtavaj juhota', up)
                elif period == 'saayam':
                    self.assertIn('mṛḍaya' if yajur else 'mṛḷaya', up)
                    self.assertEqual('kitavāso' in up, yajur)
                elif yajur:
                    for phrase in ('ā satyena rajasā', 'paśyanto jyotir uttaram', 'citraṃ devānām', 'nandāma śaradaḥ śataṃ', 'lohitākṣaḥ'):
                        self.assertIn(phrase, up)
                else:
                    self.assertEqual(doc.verses, [f'1.50.{n}' for n in range(1, 14)])
                    self.assertIn('jyotiṣ paśyanta uttaram', up)
                    self.assertIn('brahma-yagnam-section', doc.ids)

    def test_counts_directions_and_language_round_trip(self):
        for veda, period, _, doc in self.pages():
            with self.subTest(veda=veda, period=period):
                direction = 'west' if period == 'saayam' else 'east'
                for section in ('arghyam', 'upasthanam'):
                    self.assertIn('Stand facing ' + direction, doc.section(section))
                self.assertIn(str(2 if period == 'madhyanikam' else 3) + ' times', doc.section('arghyam'))
                self.assertIn(str({'pratah': 108, 'madhyanikam': 32, 'saayam': 64}[period]) + ' repetitions', doc.section('gayatri-japam'))
                self.assertIn('facing south', doc.section('yama'))
                self.assertIn('facing north', doc.section('harihara'))
                self.assertIn('facing ' + direction, doc.section('prarthana'))
                if period == 'saayam':
                    self.assertIn('north', doc.section('achamanam'))
                    self.assertIn('east, south, west, north' if veda == 'yajurveda' else 'west, north, east, south', doc.section('sandhya-vandanam'))
                name = slug(veda, period)
                self.assertIn(f'../../{name}/', doc.links)
                self.assertIn(f'../en/{name}/', Document(ROOT / name / 'index.html').links)
                self.assertIn(f'{name}/', Document(ROOT / 'en/index.html').links)
        self.assertIn('en/', Document(ROOT / 'index.html').links)

    def test_checked_in_pages_match_generator(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        try:
            spec = importlib.util.spec_from_file_location('english_builder', ROOT / 'scripts/build_english_pages.py')
            builder = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(builder)
            with tempfile.TemporaryDirectory() as directory:
                builder.ROOT = Path(directory)
                builder.main()
                for generated in builder.ROOT.rglob('*.html'):
                    checked_in = ROOT / generated.relative_to(builder.ROOT)
                    self.assertEqual(generated.read_text(), checked_in.read_text(), str(checked_in))
        finally:
            sys.path.pop(0)


if __name__ == '__main__':
    unittest.main()
