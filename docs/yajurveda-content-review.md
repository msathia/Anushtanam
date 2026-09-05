# Yajurveda Sandhyavandanam content review

Reviewed 2026-09-04. These three Tamil guides explicitly follow **Krishna
Yajurveda, Taittiriya shakha, Apastamba sutra, Smarta sampradaya**. They are
not labeled as a universal procedure for Shukla Yajurveda or every sutra.
The short daily sankalpams retain the Smarta Parameshvara-prityartham opening.

## Source selection

- [Sanskrit Documents: Smarta Apastamba Sandhyavandanam](https://sanskritdocuments.org/doc_veda/Sandhyavandanam.pdf)
  is the main procedure reference: printed/PDF pages 3 (sankalpams), 5
  (prashanam), 7–8 (arghyam), 13–17 (japa and udvasanam), 17–21
  (upasthana), and 21–26 (conclusion). Page numbers here are one-based.
- [Vaidhika Dharma: Apastamba Pratah](https://vaidhikadharma.org/iast/apastamba-sandhyavandanam/prata/)
  cross-checks the common Smarta prayers, asana, avahanam and abhivadanam.
  Its fetched pages omit the actual upasthana text, so they are not used
  alone to construct that part.
- [Shri Kainkaryam Kriya Trust: Yajurveda Sandhyavandanam](https://srikkt.org/yajurveda-sandhyavandanam-english/)
  independently supplies all three upasthana sequences. Its Sri Vaishnava
  sankalpams and different noon direction are not imported into these
  Smarta pages.

Ancient mantras were cross-checked rather than trusting OCR/transliteration
alone. For example, the main PDF's evening Roman transliteration incorrectly
repeats `rātris`; the Sanskrit and independent source give `ahas`. The new
Saayam page uses `yad ahnā ... ahas tad avalumpatu ... satye jyotiṣi`.
Noon preserves `asatāṃ ca pratigraham`, not `satāṃ`.

## Distinctions from the existing Rigveda pages

| Section | Yajurveda treatment |
| --- | --- |
| Opening noon sankalpa | `mādhyāhnikaṃ kariṣye`, as in the selected Smarta guide |
| Morning upasthana | `carṣaṇīdhṛtaḥ śravo ... sānasim; satyaṃ`, `prajānan`, `satyāya havyaṃ ghṛtavad vidhema` |
| Noon upasthana | Six complete sections: Ā satyena; Ud vayam with **paśyanto jyotir uttaram**; Udu tyam; Citram; Tac cakṣur with the full longevity prayer; Ya udagān |
| Evening upasthana | Full five sections: Imam me; Tat tvā; Yac cid dhi; Yat kiñcedam; Kitavāso. Yajur readings `mṛḍaya` and `aheḍamāno` |
| Late arghya | One additional Gayatri arghya when late; none of the three Rigveda-specific late-arghya riks |
| Pronunciation spelling | `suvaḥ` / `suvarom`, not the Rigveda template's `svaḥ` / `svarom` |
| Abhivadanam | Apastamba sutra, Yajur shakha; personal pravara, gotra and name remain placeholders |
| Closing Savitr prayer | `yad bhadraṃ tan ma ā suva`, as in the selected Yajur paddhati |

The Rigveda four-mantra upasthana continuation and Rigveda Brahmayajna link
are omitted. The Yajur pages include the asana prayer and a closing achamana.
Common water mantras are recited directly, as in the selected Smarta guide,
instead of copying the Rigveda template's water-mantra nyasas.

## Procedure choices and limitations

The main Smarta PDF and Vaidhika Dharma both give arghya counts 3/2/3 and
the main PDF gives japa counts 108/32/64. These are presented as this
procedure's practice, not universal counts. Initial achamana is east/east/north;
arghya and upasthana are east/east/west. Noon namaskara faces north.
For sandhyadi salutations the PDF begins at east, including evening, then
returns to west in evening; directional salutations separately start from
west in evening. These two sections are kept distinct.

Tamil rendering does not encode the full Vedic svaras or every nasal
allophone. The pages explicitly refer pronunciation, asana, nyasa and
family variations to the practitioner's received instruction. Textual checks
are not certification of oral chanting.

## Validation

Run `python3 -m unittest discover -s tests -v`.
Tests check all six routes and local anchors, period-specific sankalpams and
prashanam, complete Yajur upasthana sections, the Yajur/Rig textual contrasts,
conditional Gayatri late arghya, identity and navigation. Deployment runs
these checks before publishing.
