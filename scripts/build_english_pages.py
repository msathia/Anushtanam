#!/usr/bin/env python3
"""Build the six standalone English guides: python3 -B scripts/build_english_pages.py."""
from html import escape
from pathlib import Path
from english_mantras import *

ROOT = Path(__file__).resolve().parents[1]
PERIODS = {
    'pratah': ('Prātaḥ', 'Morning', 'Around sunrise', 3, 108),
    'madhyanikam': ('Mādhyāhnika', 'Noon', 'Around local solar noon', 2, 32),
    'saayam': ('Sāyaṃ', 'Evening', 'Around sunset', 3, 64),
}
PREFIX = 'mamopātta samasta duritakṣayadvārā śrī parameśvara prītyartham |\n'
PREFIX_MEANING = 'For the removal of all wrongs incurred by me, and for the pleasure of the supreme Lord, '
NYASA_INSTRUCTION = 'For nyāsa, touch the head when naming the seer (ṛṣi), the tip of the nose for the metre (chandas), and the chest for the deity (devatā), as taught.'
ACHAMANA_AGAIN = 'Then repeat <a href="#achamanam">ācamana and aṅgavandana</a>, from Acyuta through Dāmodara.'

def slug(veda, period):
    return f'{veda}-' + ('madhyanikam' if period == 'madhyanikam' else f'{period}-sandhyavandanam')

def instruction(text):
    return f'<p class="instruction">{text}</p>'

def note(text):
    return f'<p class="source-note">{text}</p>'

def recite(pair, attrs=''):
    sanskrit = pair[0]
    return (f'<div class="recitation"><p class="label">Sanskrit · IAST</p>'
            f'<p class="mantra" lang="sa-Latn"{attrs}>{escape(sanskrit).replace(chr(10), "<br>")}</p></div>')

def table(headers, rows):
    return '<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th scope="col">{escape(h)}</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{escape(c)}</td>' for c in row) + '</tr>' for row in rows) + '</tbody></table></div>'

def pronunciation():
    return '''<details class="pronunciation" id="pronunciation"><summary>How to pronounce the Sanskrit</summary>
<p>The mantra uses IAST, a precise Roman transliteration of Sanskrit. Read the marked letters as Sanskrit sounds. Recite the Sanskrit block.</p>
<ul><li><strong>a / ā, i / ī, u / ū:</strong> short / long vowels. Hold ā, ī and ū about twice as long. Keep e and o pure and long; ai and au are diphthongs.</li>
<li><strong>ṛ:</strong> a syllabic r, not the English word “ree.” <strong>ṝ</strong> is its long counterpart. <strong>ḷ</strong> in the Rigvedic mṛḷaya is a retroflex lateral consonant.</li>
<li><strong>c:</strong> like ch in “church”; <strong>j:</strong> like j in “judge.” <strong>ś:</strong> a palatal sh; <strong>ṣ:</strong> sh with the tongue curled back; <strong>s:</strong> a dental s.</li>
<li><strong>ṭ, ṭh, ḍ, ḍh, ṇ:</strong> curl the tongue back. For t, th, d, dh and n, place it near the upper teeth.</li>
<li><strong>kh, gh, ch, jh, th, dh, ph, bh:</strong> one consonant released with a breath. Sanskrit th is not English “thin,” and ph is not f. Keep both sounds in clusters such as kṣ and jñ.</li>
<li><strong>ṅ:</strong> ng as in “sing”; <strong>ñ:</strong> a palatal nasal. <strong>ṃ:</strong> anusvāra, a nasal sound whose realization depends on the next sound and the recitation tradition. <strong>ḥ:</strong> visarga, a breath after a vowel; its linked pronunciation depends on what follows.</li>
<li><strong>'</strong> marks an elided a, not a pause. Spaces help reading; do not insert a pause at every space. For example, bhūr bhuvaḥ suvaḥ is linked as bhūr bhuvas suvaḥ. Double consonants are held longer. The bars | and || mark textual divisions.</li></ul>
<p><strong>Vedic svara:</strong> pitch accents and special Vedic nasal realizations are not encoded here. Use the oral recitation taught by your guru for pitch, breath, and connected chanting. IAST alone cannot supply those features.</p></details>'''

def build_page(veda, period):
    yajur = veda == 'yajurveda'
    name, english_period, timing, arghyas, japam = PERIODS[period]
    direction = 'west' if period == 'saayam' else 'east'
    seated = 'north' if period == 'saayam' else 'east'
    veda_title = 'Yajurveda' if yajur else 'Rigveda'
    tradition = 'Kṛṣṇa Yajurveda · Taittirīya śākhā · Āpastamba sūtra · Smārta' if yajur else 'Ṛgveda · Āśvalāyana sūtra · Smārta'
    period_sa = {'pratah': 'prātaḥ sandhyā', 'madhyanikam': 'mādhyāhnika' if yajur else 'mādhyāhnika sandhyā', 'saayam': 'sāyaṃ sandhyā'}[period]
    worship = 'mādhyāhnikaṃ kariṣye' if yajur and period == 'madhyanikam' else period_sa + 'm upāsiṣye'
    vyahrti = 'oṃ bhūr bhuvaḥ ' + ('suvaḥ' if yajur else 'svaḥ') + ' |'
    vyahrti_pair = (vyahrti, 'Oṃ. Earth, the intermediate realm, heaven: the three sacred utterances.')
    gayatri = (vyahrti + '\n' + GAYATRI, vyahrti_pair[1] + ' ' + GAYATRI_MEANING)
    pranayama = ('oṃ bhūḥ oṃ bhuvaḥ oṃ ' + ('suvaḥ' if yajur else 'svaḥ') + ' oṃ mahaḥ oṃ janaḥ oṃ tapaḥ oṃ satyam |\noṃ ' + GAYATRI + '\noṃ āpo jyotī raso ’mṛtaṃ brahma bhūr bhuvaḥ ' + ('suvar' if yajur else 'svar') + ' om ||',
                 'Oṃ: Bhūḥ, Bhuvaḥ, Suvaḥ (heaven), Mahaḥ, Janaḥ, Tapaḥ, Satyam—the seven sacred utterances, naming the worlds. ' + GAYATRI_MEANING + ' Oṃ. Waters, light, essence, immortality—all are brahman. Earth, the intermediate realm, heaven: Oṃ.')
    if not yajur:
        pranayama = (pranayama[0], pranayama[1].replace('Suvaḥ', 'Svaḥ'))
    cards = []
    def card(identifier, title, body):
        cards.append(f'<section class="card" id="{identifier}"><h2>{len(cards)+1}. {title}</h2>{body}</section>')
    def breath(identifier, before_japa=False):
        extra = (' This guide uses 10 repetitions before japa; follow the number taught to you.' if not yajur else ' Follow the number taught to you.') if before_japa else ''
        card(identifier, 'Prāṇāyāma — regulated breath', instruction('Use the inhalation, retention and exhalation method taught by your guru.' + extra) + recite(pranayama) + instruction('Touch the right ear at the end.'))
    def sankalpa(action, meaning):
        return recite((PREFIX + action + ' |', PREFIX_MEANING + meaning))
    names = ['Keśava', 'Nārāyaṇa', 'Mādhava', 'Govinda', 'Viṣṇu', 'Madhusūdana', 'Trivikrama', 'Vāmana', 'Śrīdhara', 'Hṛṣīkeśa', 'Padmanābha', 'Dāmodara']
    parts = [('Thumb', 'Right cheek'), ('Thumb', 'Left cheek'), ('Ring finger', 'Right eye'), ('Ring finger', 'Left eye'), ('Index finger', 'Right nostril'), ('Index finger', 'Left nostril'), ('Little finger', 'Right ear'), ('Little finger', 'Left ear'), ('Middle finger', 'Right shoulder'), ('Middle finger', 'Left shoulder'), ('Fingers' if yajur else 'Four fingers', 'Navel' if yajur else 'Chest'), ('All five fingers', 'Head')]
    card('achamanam', 'Ācamana — sipping water', instruction(f'Sit facing {seated}. Place a small quantity of clean water in the right palm and sip once for each of these three names.') + recite(('acyutāya namaḥ | anantāya namaḥ | govindāya namaḥ |', 'Salutation to Acyuta, the unfailing one; to Ananta, the endless one; to Govinda, protector of cows.')) + instruction('Wipe the lips and clean the hand as taught. Begin aṅgavandana by saying the first four names and touching the indicated places with the right hand.') + table(['Name to recite', 'Finger', 'Touch'], [(names[i], *parts[i]) for i in range(4)]))
    card('anga-vandanam', 'Aṅgavandana — touching the limbs', instruction('Continue with the remaining eight names, using the right hand.') + table(['Name to recite', 'Finger', 'Touch'], [(names[i], *parts[i]) for i in range(4, 12)]))
    card('ganapati', 'Gaṇapati meditation', recite(GANAPATI) + instruction('Gently tap both sides of the forehead five times with the hands, following the method taught.') + note('A meditation verse used here for Gaṇapati.'))
    breath('pranayama')
    card('sankalpam', 'Saṅkalpa — intention for this worship', instruction(f'Sit facing {seated}. Rest the right hand over the left palm on the right thigh and state the intention.') + sankalpa(worship, f'I shall perform the {english_period.lower()} Sandhyā worship.') + instruction('Then touch water with the ring finger and place a water mark on the forehead while reciting:') + recite(('oṃ śrī keśavāya namaḥ |', 'Oṃ. Salutation to the blessed Keśava.')))
    water_instruction = instruction('Sprinkle water on the head with the ring finger for the first seven phrases; at “yasya kṣayāya jinvatha” sprinkle the feet, and at “āpo janayathā ca naḥ” sprinkle the head again.')
    circle = instruction('Circle the head clockwise with water, as taught.')
    card('marjanam', 'Mārjana — sprinkling water', (instruction(NYASA_INSTRUCTION) + recite(APO_NYASA) if not yajur else '') + note('Āpo hi ṣṭhā: a prayer to the Waters, also found in Ṛgveda 10.9.1–3.') + water_instruction + recite(APO) + recite(vyahrti_pair) + circle)
    prashana_nyasa = {
        'pratah': ('sūryaś cety anuvākasya agnir ṛṣiḥ | devī gāyatrī chandaḥ | sūryo devatā | apāṃ prāśane viniyogaḥ |', 'For the Sūryaś ca passage: Agni is the seer, Devī Gāyatrī the metre, and Sūrya the deity. It is used for sipping water.'),
        'madhyanikam': ('āpaḥ punantv ity anuvākasya viśvedevā ṛṣayaḥ | anuṣṭup chandaḥ | āpo devatā | apāṃ prāśane viniyogaḥ |', 'For the Āpaḥ punantu passage: the All-gods are the seers, Anuṣṭubh the metre, and the Waters the deity. It is used for sipping water.'),
        'saayam': ('agniś cety anuvākasya sūrya ṛṣiḥ | devī gāyatrī chandaḥ | agnir devatā | apāṃ prāśane viniyogaḥ |', 'For the Agniś ca passage: Sūrya is the seer, Devī Gāyatrī the metre, and Agni the deity. It is used for sipping water.'),
    }
    card('prashanam', 'Mantra prāśana — purification by sipping', (instruction(NYASA_INSTRUCTION) + recite(prashana_nyasa[period]) if not yajur else '') + instruction('Hold a little water in the right palm. Recite the entire mantra, then sip the water.') + recite(PRASHANA[period]) + note('The period-specific text is transmitted in the Taittirīya Āraṇyaka / Mahānārāyaṇa Upaniṣad tradition.') + instruction(ACHAMANA_AGAIN))
    dadhi_nyasa = ('dadhikrāvṇa ity asya mantrasya vāmadeva ṛṣiḥ | anuṣṭup chandaḥ | dadhikrāvā devatā | apāṃ prokṣaṇe viniyogaḥ |', 'For the Dadhikrāvan mantra: Vāmadeva is the seer, Anuṣṭubh the metre, and Dadhikrāvan the deity. It is used for sprinkling water.')
    card('punarmarjanam', 'Punarmārjana — sprinkling again', (instruction(NYASA_INSTRUCTION) + recite(dadhi_nyasa) if not yajur else '') + instruction('Sprinkle water on the head while reciting Dadhikrāvṇo.') + note('Ṛgveda 4.39.6, addressed to Dadhikrāvan, the divine horse.') + recite(DADHI) + (recite(APO_NYASA) if not yajur else '') + water_instruction + recite(APO) + recite(vyahrti_pair) + circle)
    card('arghyam', 'Arghya — offering water', instruction(f'Stand facing {direction}. Hold water in both cupped palms. Recite the complete mantra and offer the water {arghyas} times, reciting once for each offering. Release the water into a clean place or the receiving vessel.') + recite(gayatri) + note('The Sāvitrī verse addresses Savitṛ, the divine impeller; Ṛgveda 3.62.10. The offering count follows this guide’s selected practice.'))
    breath('pranayama-after-arghya')
    late = gayatri if yajur else RIG_LATE[period]
    late_ref = {'pratah': '8.93.4', 'madhyanikam': '8.93.1', 'saayam': '8.23.15'}[period]
    card('prayaschitta', 'Late-time expiation — only if the proper time has passed', instruction('If the proper Sandhyā time has passed, state this intention after prāṇāyāma. Otherwise continue to the next step.') + sankalpa(period_sa + ' kālātīta prāyaścittārtham arghyapradānaṃ kariṣye', f'I shall offer water as expiation for performing the {english_period.lower()} Sandhyā after its proper time.') + (note('Selected late-arghya verse: Ṛgveda ' + late_ref + '.') if not yajur else '') + recite(late) + instruction(f'Stand facing {direction} and offer water one additional time with this mantra.'))
    card('atma-pradakshina', 'Ātma-pradakṣiṇa — turning clockwise', recite(vyahrti_pair) + instruction('With a little water in the hand, recite and turn clockwise around yourself once, releasing the water as taught.'))
    card('atmanusandhanam', 'Ātmānusandhāna — contemplation of the Self', instruction(f'Sit facing {seated}. Contemplate the sun as brahman and yourself as brahman.') + recite(('asāv ādityo brahma brahmaivāham asmi |', 'That sun is brahman. I myself am brahman.')) + instruction(ACHAMANA_AGAIN))
    tarpanam = ['ādityaṃ', 'somaṃ', 'aṅgārakaṃ', 'budhaṃ', 'bṛhaspatiṃ', 'śukraṃ', 'śanaiścaraṃ', 'rāhuṃ', 'ketuṃ', 'keśavaṃ', 'nārāyaṇaṃ', 'mādhavaṃ', 'govindaṃ', 'viṣṇuṃ', 'madhusūdanaṃ', 'trivikramaṃ', 'vāmanaṃ', 'śrīdharaṃ', 'hṛṣīkeśaṃ', 'padmanābhaṃ', 'dāmodaraṃ']
    card('tarpanam', 'Navagraha and Keśavādi tarpaṇa', instruction(f'Sit facing {seated}. For each “tarpayāmi,” release water through the fingertips into the receiving vessel.') + recite((' |\n'.join(n + ' tarpayāmi' for n in tarpanam) + ' |', '“Tarpayāmi” means “I satisfy with an offering of water.” The first nine offerings are to Āditya (Sun), Soma (Moon), Aṅgāraka (Mars), Budha (Mercury), Bṛhaspati (Jupiter), Śukra (Venus), Śanaiścara (Saturn), Rāhu and Ketu (the lunar nodes). The remaining twelve are to the forms of Viṣṇu named in aṅgavandana above, in the same order.')) + instruction(ACHAMANA_AGAIN))
    card('prarthana', 'Prayer', instruction(f'Pray facing {direction}.') + recite(PRAYER))
    card('bhumi', 'Bhūmi prayer — optional in some families', instruction('Recite this preliminary prayer if it belongs to the practice taught to you.') + recite(BHUMI))
    if yajur:
        card('asanam', 'Āsana prayer — preparing the seat', instruction('Join the palms in prayer to the Earth goddess, then touch the seat for japa and recite.') + recite(ASANA))
    card('ganapati-before-japa', 'Gaṇapati meditation before japa', recite(GANAPATI) + instruction('Gently tap both sides of the forehead five times, as taught.'))
    breath('pranayama-before-sankalpa')
    card('japa-sankalpam', 'Saṅkalpa for Gāyatrī japa', sankalpa(period_sa + ' gāyatrī mahāmantra japaṃ kariṣye', f'I shall repeat the great Gāyatrī mantra for the {english_period.lower()} Sandhyā.'))
    card('pranayama-nyasa', 'Nyāsa for the prāṇāyāma mantras', instruction(NYASA_INSTRUCTION) + recite(PRANAYAMA_NYASA))
    breath('pranayama-before-japa', True)
    card('avahanam', 'Gāyatrī āvāhana — invocation', instruction(NYASA_INSTRUCTION) + recite(AVAHANA_NYASA) + instruction('Recite the invocation. At each “āvāhayāmi,” bring the joined palms towards yourself in the gesture of inviting, as taught.') + recite(AVAHANA))
    card('gayatri-nyasa', 'Nyāsa for Gāyatrī japa', instruction(NYASA_INSTRUCTION) + recite(JAPA_NYASA))
    card('gayatri-dhyanam', 'Gāyatrī meditation', recite(DHYANA) + note('These are meditation verses, distinct from the Vedic Sāvitrī mantra that follows.'))
    card('gayatri-japam', 'Gāyatrī mantra japa', instruction(f'Sit facing {direction} in the posture taught by your guru. This guide uses {japam} repetitions for {english_period.lower()}; follow the count given in your instruction.') + recite(gayatri) + note('Seer: Viśvāmitra. Metre: Nicṛd Gāyatrī. Deity: Savitṛ.'))
    if not yajur and period == 'madhyanikam':
        card('brahma-yagnam-section', 'Brahmayajña — this guide’s noon family practice', instruction('If you follow the original guide’s sequence, perform Brahmayajña here. <a href="../../brahma-yagnam.html" target="_blank" rel="noopener">Open the Brahmayajña guide (Tamil; new tab)</a>. Return to this tab afterwards and continue below.') + note('This is the existing separate Rigveda Brahmayajña guide. Its placement here is a family practice.'))
    breath('pranayama-after-japa')
    card('upasthana-sankalpam', 'Upasthāna intention and farewell to Gāyatrī', sankalpa(period_sa + ' upasthānaṃ kariṣye', f'I shall perform the standing attendance of the {english_period.lower()} Sandhyā.') + recite(DISMISS_NYASA) + instruction('Stand, bend to touch the earth with the ring finger, recite the farewell, then stand upright.') + recite(DISMISS))
    verses = {('yajurveda', 'pratah'): YAJUR_MITRA, ('yajurveda', 'madhyanikam'): YAJUR_SURYA, ('yajurveda', 'saayam'): YAJUR_VARUNA, ('rigveda', 'pratah'): RIG_MITRA, ('rigveda', 'madhyanikam'): RIG_SURYA, ('rigveda', 'saayam'): RIG_VARUNA}[veda, period]
    up_nyasa = {
        'pratah': ('mitrasyeti tṛcasya viśvāmitra ṛṣiḥ | gāyatrītriṣṭubhau chandāṃsi | mitro devatā | prātaḥ sandhyopasthāne viniyogaḥ |', 'For the three Mitra verses: Viśvāmitra is the seer, the metres are Gāyatrī and Triṣṭubh, and Mitra the deity. Their use is in morning Sandhyā attendance.'),
        'madhyanikam': ("udu tyam iti trayodaśarcasya sūktasya praskaṇva ṛṣiḥ | ādyā nava gāyatryaḥ | antyāś catasro 'nuṣṭubhaḥ | sūryo devatā | mādhyāhnika upasthāne viniyogaḥ |", 'For the thirteen-verse hymn beginning Udu tyam: Praskaṇva is the seer; the first nine verses are Gāyatrī, the final four Anuṣṭubh; Sūrya is the deity. It is used in noon attendance.'),
        'saayam': ('imaṃ me tat tvā yāmīti mantrāṇāṃ śunaḥśepa ṛṣiḥ | gāyatrītriṣṭubhau chandāṃsi | varuṇo devatā | sāyaṃ sandhyopasthāne viniyogaḥ |', 'For the verses beginning Imaṃ me and Tat tvā yāmi: Śunaḥśepa is the seer, Gāyatrī and Triṣṭubh the metres, and Varuṇa the deity. They are used in evening Sandhyā attendance.'),
    }
    up_title = {'pratah': 'Mitra', 'madhyanikam': 'Sūrya', 'saayam': 'Varuṇa'}[period]
    up = instruction(f'Stand facing {direction}, with palms joined, and recite the passages in order.')
    if not yajur:
        up += instruction(NYASA_INSTRUCTION) + recite(up_nyasa[period])
    for i, pair in enumerate(verses, 1):
        if not yajur:
            ref = {'pratah': ['3.59.6', '3.59.1', '3.59.2'], 'madhyanikam': [f'1.50.{n}' for n in range(1, 14)], 'saayam': ['1.25.19', '1.24.11']}[period][i-1]
            up += f'<h3>Ṛgveda {ref}</h3>' + recite(pair, f' data-rv="{ref}"')
        else:
            up += f'<h3>Passage {i}</h3>' + recite(pair, f' data-upasthana-part="{i}"')
    if yajur and period == 'saayam':
        up += note('The short “yac cid dhi” passage is a selected verse from a longer hymn; it introduces the admission of wrongdoing, continued here by the following prayers.')
    card('upasthanam', up_title + ' upasthāna — standing prayer', up)
    if not yajur:
        extra = instruction('Continue with these four prayers. Use the nyāsa and hand gestures around the face, ears and hair tuft taught by your guru.')
        for ref, rishi, metre, deity, mantra, meaning in RIG_PRAYERS:
            extra += f'<h3>Ṛgveda {ref}</h3>' + recite((f'{rishi} ṛṣiḥ | {metre} chandaḥ | {deity} ' + ('devatāḥ' if deity == 'viśvedevāḥ' else 'devatā') + ' | sandhyopasthāne viniyogaḥ |', f'Ritual nyāsa in this guide: seer {rishi}; metre {metre}; deity {deity}; used in Sandhyā attendance.')) + recite((mantra, meaning))
        card('upasthana-prayers', 'Prayers following upasthāna', extra + note('The deity assignments above follow this ritual nyāsa; these do not establish a single interpretation of every hymn.'))
    dirs = ['east', 'south', 'west', 'north'] if yajur or period != 'saayam' else ['west', 'north', 'east', 'south']
    sandhya_names = ['sandhyāyai namaḥ', 'sāvitryai namaḥ', 'gāyatryai namaḥ', 'sarasvatyai namaḥ']
    card('sandhya-vandanam', 'Salutations to the Sandhyā deities', instruction('Turn clockwise through ' + ', '.join(dirs) + f', joining the palms in each direction. Then face {direction}.') + table(['Recitation', 'Direction'], [(n + ' |', d.title()) for n, d in zip(sandhya_names, dirs)]) + recite(('sarvābhyo devatābhyo namo namaḥ |\nkāmo ’kārṣīn manyur akārṣīt namo namaḥ |', 'Repeated salutations to all the deities. Desire did it; anger did it: repeated salutations. This acknowledges the impulses behind wrongdoing.')))
    identity = 'āpastamba sūtraḥ yajuśśākhādhyāyī' if yajur else 'āśvalāyana sūtraḥ ṛkśākhādhyāyī'
    abhi_direction = 'north' if yajur and period == 'madhyanikam' else direction
    card('abhivadanam', 'Abhivādana — stating lineage and saluting', instruction(f'Face {abhi_direction}. Supply the pravara sages, their count, gotra and personal name exactly as taught in your family. Do not recite the bracketed English prompts. Then bow in the manner taught.') + recite(('abhivādaye [your pravara sages] [your pravara count] pravarānvitaḥ |\n[your gotra] gotraḥ ' + identity + ' |\n[your name] śarmā nāmāham asmi bhoḥ ||', 'I respectfully salute. I belong to the lineage marked by [the named sages and their number], of [the named gotra], following the ' + ('Āpastamba sūtra and studying the Yajurveda branch' if yajur else 'Āśvalāyana sūtra and studying the Rigveda branch') + '. My name is [name] Śarmā, revered sir.')) + note('The personal fields are not guessed. Use your own instructed lineage formula.'))
    direction_rows = [('prācyai diśe namaḥ |', 'East'), ('dakṣiṇāyai diśe namaḥ |', 'South'), ('pratīcyai diśe namaḥ |', 'West'), ('udīcyai diśe namaḥ |', 'North')]
    if period == 'saayam':
        direction_rows = direction_rows[2:] + direction_rows[:2]
    card('dig-vandanam', 'Digvandana — salutations to the directions', instruction(f'Begin facing {direction} and turn clockwise for the four horizontal directions.') + table(['Recitation', 'Direction'], direction_rows) + recite(('ūrdhvāya namaḥ | adharāya namaḥ | antarikṣāya namaḥ |\nbhūmyai namaḥ | brahmaṇe namaḥ | viṣṇave namaḥ | yamāya namaḥ |', 'Salutation to what is above, to what is below, to the intermediate space, to Earth, to Brahmā, to Viṣṇu and to Yama.')) + instruction('Acknowledge above and below as taught; face south for Yama.'))
    card('yama', 'Yama vandana', instruction('Stand facing south.') + recite(YAMA))
    card('harihara', 'Harihara vandana', instruction('Stand facing north, with palms joined.') + recite(HARIHARA))
    card('narmada', 'Narmadā and serpent prayer — optional in some families', instruction('If this prayer belongs to your family’s practice, stand facing west and recite.') + recite(NARMADA))
    card('suryanarayana', 'Sūryanārāyaṇa vandana', instruction(f'Stand facing {direction}, palms joined.') + recite(SURYA_NARAYANA) + instruction('Repeat <a href="#abhivadanam">abhivādana</a> and bow. ' + ACHAMANA_AGAIN))
    card('samarpanam', 'Samarpaṇa — offering all actions', instruction(f'Sit facing {seated}. Hold a little water, recite, and release it at “brahmārpaṇam astu.”') + recite(SAMARPANA) + instruction(ACHAMANA_AGAIN))
    close = 'adyā no deva savitaḥ prajāvat sāvīḥ saubhagam | parā duḥṣvapnyaṃ suva ||\nviśvāni deva savitar duritāni parā suva | yad bhadraṃ tan ' + ('ma' if yajur else 'na') + ' ā suva ||'
    card('completion', 'Japasthāna prokṣaṇa — completing the practice', instruction('Sprinkle a little water on the place where you sat for japa. Touch it with the ring finger, recite these prayers and place a water mark on the forehead.') + recite((close, 'God Savitṛ, bring us good fortune today, with offspring; drive away bad dreams. God Savitṛ, drive away all evils; bring what is good to ' + ('me' if yajur else 'us') + '.')) + instruction(f'This completes {veda_title} {name} Sandhyāvandanam.'))
    nav = '<nav class="period-nav" aria-label="Guide navigation"><a href="../">All English guides</a>' + ''.join(f'<a href="../{slug(veda, p)}/"' + (' aria-current="page"' if p == period else '') + f'>{PERIODS[p][1]}</a>' for p in PERIODS) + '</nav>'
    language = f'<nav class="language-nav" aria-label="Language"><strong>English</strong> · <a href="../../{slug(veda, period)}/" lang="ta" hreflang="ta">தமிழ்</a></nav>'
    sources = ('<li><a href="https://sanskritdocuments.org/doc_veda/Sandhyavandanam.pdf">Smārta Āpastamba Sandhyāvandanam</a> — selected ritual sequence and readings.</li><li><a href="https://srikkt.org/yajurveda-sandhyavandanam-english/">Shri Kainkaryam Kriya Trust</a> — comparison of Yajurveda upasthāna texts; its sectarian intentions are not used here.</li>' if yajur else '<li><a href="https://www.sriebrvvdsgurukulam.com/trikala-sandhya-vandhanam">Rigveda Gurukulam</a> — comparison of three-period mantras.</li><li><a href="https://sanskritdocuments.org/doc_veda/r01.html">Ṛgveda Maṇḍala 1</a>, <a href="https://sanskritdocuments.org/doc_veda/r03.html">3</a>, <a href="https://sanskritdocuments.org/doc_veda/r08.html">8</a> — Saṃhitā readings.</li>')
    sources += '<li><a href="https://sanskritdocuments.org/doc_upanishhat/mahanarayana.html">Mahānārāyaṇa Upaniṣad</a> — related water, invocation and concluding texts; editions differ in some readings.</li>'
    toc = '<nav class="toc" aria-label="Jump to a step">' + ''.join(f'<a href="#{i}">{t}</a>' for i, t in [('sankalpam', 'Intention'), ('prashanam', 'Water purification'), ('arghyam', 'Arghya'), ('gayatri-japam', 'Gāyatrī japa'), ('upasthanam', 'Upasthāna'), ('abhivadanam', 'Lineage')]) + '</nav>'
    title = f'{veda_title} {name} Sandhyāvandanam'
    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — English instructions and Sanskrit IAST</title>
<meta name="description" content="{veda_title} {english_period.lower()} Sandhyavandanam: full English instructions, Sanskrit IAST pronunciation and period-specific sankalpas.">
<link rel="stylesheet" href="../style.css"><link rel="alternate" hreflang="ta" href="../../{slug(veda, period)}/"></head>
<body><a class="skip-link" href="#steps">Skip to the steps</a><main class="container">{language}{nav}
<header><p class="eyebrow">{english_period} · {timing}</p><h1>{title}</h1><p class="tradition">{tradition}</p>
<p>Follow the English ritual instructions and recite the Sanskrit mantras in Roman transliteration.</p>
<p class="source-note">This follows the selected family procedure on this site. Counts, posture, nyāsa and some readings vary: follow your guru’s instruction. {'This is not a Śukla Yajurveda guide.' if yajur else ''}</p></header>
{pronunciation()}{toc}<div id="steps">{''.join(cards)}</div>
<details class="sources" id="sources"><summary>Sources and recitation notes</summary><ul>{sources}</ul>
<p>Nyāsa formulas and later prayer verses are identified separately from Saṃhitā verses. Spaces aid reading; pitch accents are not shown.</p></details>
<footer>English text review: 5 September 2026 · <a href="#pronunciation">Pronunciation key</a> · <a href="../">All English guides</a></footer>
</main></body></html>'''
    path = ROOT / 'en' / slug(veda, period) / 'index.html'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html + '\n')

def main():
    for veda in ('yajurveda', 'rigveda'):
        for period in PERIODS:
            build_page(veda, period)
    from build_landing_pages import build_landing_pages
    build_landing_pages(ROOT)

if __name__ == '__main__':
    main()
