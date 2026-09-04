# Rigveda Sandhyavandanam content review

Reviewed 2026-09-04. The three standalone Tamil pages retain the project's
Smarta framework and explicitly identify the Ashvalayana/Rigveda tradition.
They require no JavaScript to read. This is a textual cross-check, not a
certification of oral svara or every family's paddhati.

## Time-specific passages

| Passage | Pratah | Madhyanikam | Saayam |
| --- | --- | --- | --- |
| Worship sankalpa | prātaḥ sandhyām upāsiṣye | mādhyāhnika sandhyām upāsiṣye | sāyaṃ sandhyām upāsiṣye |
| Prashanam | sūryaś ca; yad rātryā; rātris; sūrye jyotiṣi | āpaḥ punantu; **asatāṃ** ca pratigraham | agniś ca; yad ahnā; ahas; satye jyotiṣi |
| Late arghya verse | yad adya kac ca, RV 8.93.4 | ud ghed abhi, RV 8.93.1 | na tasya māyayā, RV 8.23.15 |
| Upasthana | Mitra: RV 3.59.6, 1, 2, in that order | Surya: all 13 verses of RV 1.50 | Varuna: RV 1.25.19 and 1.24.11 |
| Arghya / upasthana direction | East | East | West |
| Arghya count in the selected procedure | 3 | 2 | 3 |

Japa, late-arghya and upasthana sankalpams each name only the current period.
The Smarta `mamopātta ... śrī parameśvara prītyartham` introduction remains.
No dates, locations, gotras, pravaras or personal names are invented.

## Sources and interpretation

- [Rigveda Gurukulam: Trikala Sandhya Vandhanam](https://www.sriebrvvdsgurukulam.com/trikala-sandhya-vandhanam)
  supplies the three-period mantra comparison. It explicitly follows a
  Vaishnava sampradaya: its sectarian sankalpams, sattvika-tyaga and optional
  Ashtakshara japa have **not** been transplanted into this Smarta guide.
- [Vaidhika Dharma: Ashvalayana Pratah](https://vaidhikadharma.org/iast/aswalayana-sandhyavandanam/prata/)
  supports the Smarta common framework, nyasa and Ashvalayana/Rigveda
  abhivadanam, and gives 3/2/3 arghyas. Its evening page, as fetched during
  review, repeats several morning passages, including the opening sankalpa,
  prashanam and Mitra upasthana. Those were not used as evening authority.
- Sanskrit Documents' Samhita editions:
  [Mandala 1](https://sanskritdocuments.org/doc_veda/r01.html),
  [Mandala 3](https://sanskritdocuments.org/doc_veda/r03.html),
  [Mandala 8](https://sanskritdocuments.org/doc_veda/r08.html).
  These confirm the Rigvedic readings and verse numbers. In particular,
  Pratah uses `carṣaṇīdhṛto 'vo ... dyumnaṃ`, `bruvāṇo`, and
  `mitrāya havyaṃ ghṛtavaj juhota`; noon uses
  `jyotiṣ paśyanta uttaram`; evening preserves the Rigvedic lateral in
  `mṛḷaya` / `aheḷamāno` in Tamil.

The prashanam texts are also transmitted in the Taittiriya Aranyaka /
Mahanarayana Upanishad. Their use in a Rigveda paddhati does not mean every
recited text is a Rigveda Samhita verse. The pages distinguish these texts,
Vedic riks, nyasas and later dhyana/prayer slokas.

## Corrections and preserved family practices

- Replaced the old Apastamba/Yajurveda abhivadanam with Ashvalayana/Rigveda
  and explicit personal placeholders.
- Corrected `janaḥ`, the noon `asatāṃ` reading, Dadhikrava as the deity of
  RV 4.39.6, and corrupted Tamil words in the Surya hymn and closing prayers.
- Identified the four subsequent upasthana prayers separately: RV 1.99.1,
  1.133.5, 1.89.8 and 10.136.1. Restored Jatavedase, absent from the old page.
- Removed the duplicated, unconditional late-arghya instruction. The selected
  time-specific late-arghya verse is explicitly conditional on lateness.
- Preserved the existing 108/32/64 japa counts as this guide's practice, with
  a note to follow the count actually taught. Nyasa and mudra variations are
  not presented as universal; late-arghya rishi attributions differ between
  sources, so the page identifies the rik without inventing a universal nyasa.
- Preserved Brahmayajna after noon japa as the original guide's family
  practice, with its return anchor and scroll restoration. It is not inserted
  into morning or evening.
- Preserved the initial east/east/north achamana orientation, while evening
  arghya, upasthana and directional salutations start facing west.

## Validation

`python3 -m unittest discover -s tests -v` checks period-specific sankalpams,
prashanam contrasts, arghya/upasthana selection and directions, all thirteen
noon verses, identity, local links/anchors, and legacy redirect targets.
These regression checks do not replace textual or oral review.
