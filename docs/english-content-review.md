# English Sandhyavandanam guides

Prepared 2026-09-05. Six new `/en/` pages preserve the separate Rigveda
(Ashvalayana, Smarta) and Krishna Yajurveda (Taittiriya, Apastamba, Smarta)
procedures. The English landing page puts Yajurveda first. Tamil pages remain
available through reciprocal language links.

## Text and translation policy

The Sanskrit is rendered in IAST from the selected Sanskrit readings, rather
than mechanically romanizing Tamil spellings. This distinguishes vowel length,
aspiration, dental/retroflex consonants, the sibilants, anusvara and visarga.
It is an **unaccented reading aid**, not a recording or a full Vedic phonetic
transcription. Spaces occasionally separate sandhi-linked words for reading.
The pronunciation key explains that spaces are not pauses and that svara and
special Vedic nasal realizations require oral instruction.

Each recitation block has a separate, initially visible close English meaning.
Meanings are original prose renderings, not copied modern translations. Proper
names and terms with uncertain or multiple senses are retained and explained.
The limb names and directional formulas are translated beside their tables.
The user can collapse individual meanings for chanting; reading needs no JS.

Sources consulted for the ancient texts and selected ritual readings:

- [Smarta Apastamba Sandhyavandanam](https://sanskritdocuments.org/doc_veda/Sandhyavandanam.pdf):
  the selected Yajurveda procedure, particularly the three upasthana sequences.
  Its font encoding/OCR is damaged in places, so its extracted Roman text is
  not treated as an automatic transliteration source.
- [Vaidhika Dharma: Apastamba morning](https://vaidhikadharma.org/iast/apastamba-sandhyavandanam/prata/):
  common Sanskrit prayers and ritual framework, cross-checked with the existing
  content review. Its count/direction variants do not override the selected guide.
- [Shri Kainkaryam Kriya Trust](https://srikkt.org/yajurveda-sandhyavandanam-english/):
  comparison of Yajurveda upasthana readings. Its Vaishnava intentions and
  other procedural differences are not imported. Its evening prashana excerpt
  incorrectly repeats `ratris`; the period-specific `ahas` is retained here.
- Sanskrit Documents: [RV 1](https://sanskritdocuments.org/doc_veda/r01.html),
  [RV 3](https://sanskritdocuments.org/doc_veda/r03.html),
  [RV 8](https://sanskritdocuments.org/doc_veda/r08.html), and
  [Mahanarayana Upanishad](https://sanskritdocuments.org/doc_upanishhat/mahanarayana.html).
  These are textual witnesses, not a claim that every ritual formula comes
  from one Samhita or has a single undisputed interpretation.

## Reading choices

- Yajurveda keeps `suvaḥ / suvar om`; Rigveda keeps `svaḥ / svar om`.
- Yajurveda noon begins `ā satyena rajasā`, translated with “true expanse,”
  not the “dark expanse” appropriate to the different `ā kṛṣṇena` reading.
- Yajurveda morning retains `śravo ... satyaṃ`, `prajānan` and
  `satyāya ... vidhema`; Rigveda retains `avo ... dyumnaṃ`, `bruvāṇo` and
  `mitrāya ... juhota`. Evening retains Yajurvedic ḍ versus Rigvedic ḷ.
- The full thirteen-verse Rigveda 1.50 hymn remains at noon, including the
  ancient disease/yellowness prayers, translated as prayers rather than
  claims of medical efficacy. Bird identifications in 1.50.12 are uncertain.
- Water prayers retain the selected `avalumpatu / amṛtayonau` readings;
  the linked Mahanarayana edition has variants. Noon retains **asatām**,
  “from the unworthy,” rather than reversing that meaning to “from the good.”
- The farewell retains this guide’s `brāhmaṇebhyo hy anujñānam`; the meaning
  explains the alternate `abhyanujñātā` reading rather than pretending the
  two printed forms are identical.
- Optional Bhumi prayer retains the existing `bhūmibhārakāḥ` (“burdening
  the earth”); other manuals print `bhūmidhārakāḥ` (“supporting the earth”).
- Completion retains Yajurveda `tan ma ā suva` (“bring to me”) and Rigveda
  `tan na ā suva` (“bring to us”). The linked Upanishad edition instead has
  `tan mama ā suva`; the site follows its selected ritual reading.
- Abhivadana keeps personal placeholders. No gotra, pravara, count of sages,
  or personal name is invented. The three daily intentions name only their
  own time of day.

The Rigveda noon Brahmayajna handoff opens the existing Tamil guide in a new
tab, explicitly labelled Tamil, so the English Sandhya position remains open.
That separate ritual and the special 1008-japa page are outside this six-page
Sandhyavandanam translation.

## Maintenance and validation

Edit `scripts/english_mantras.py` (texts/meanings) or
`scripts/build_english_pages.py` (instructions/layout), then run:

```
python3 -B scripts/build_english_pages.py
python3 -B -m unittest discover -s tests -v
```

Tests check English coverage, all local links and fragments, language round
trips, period and recension contrasts, full hymn counts, ritual directions,
personal placeholders, and consistency of checked-in HTML with the generator.
These are regression checks, not certification of Sanskrit interpretation,
oral pronunciation, or every family's paddhati.
