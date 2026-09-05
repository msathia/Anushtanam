"""IAST texts and original close English meanings for the selected paddhatis.

Ancient Sanskrit texts are public domain. See docs/english-content-review.md
for witnesses, reading choices, and the limits of unaccented transliteration.
"""

# Each pair is (Sanskrit recitation, English meaning). English is never recited.
GANAPATI = (
    'śuklāmbaradharaṃ viṣṇuṃ śaśivarṇaṃ caturbhujam |\nprasannavadanaṃ dhyāyet sarvavighnopaśāntaye ||',
    'One should meditate on the all-pervading one, clothed in white, moon-coloured, four-armed and serene-faced, for the calming of every obstacle.'
)
APO = (
    'āpo hi ṣṭhā mayobhuvaḥ | tā na ūrje dadhātana | mahe raṇāya cakṣase ||\nyo vaḥ śivatamo rasaḥ | tasya bhājayateha naḥ | uśatīr iva mātaraḥ ||\ntasmā araṃ gamāma vaḥ | yasya kṣayāya jinvatha | āpo janayathā ca naḥ ||',
    'Waters, you indeed bring well-being. Give us strength, for great delight and vision. Let us share here in your most auspicious essence, like loving mothers. May we readily approach that dwelling of yours to which you quicken us; waters, bring us into renewed life.'
)
APO_NYASA = (
    'āpohiṣṭheti tṛcasya sindhudvīpa ṛṣiḥ | gāyatrī chandaḥ | āpo devatā | apāṃ prokṣaṇe viniyogaḥ |',
    'For the three verses beginning Āpo hi ṣṭhā: Sindhudvīpa is the seer, Gāyatrī the metre, and the Waters the deity. They are used for sprinkling water.'
)
DADHI = (
    'dadhikrāvṇo akāriṣaṃ jiṣṇor aśvasya vājinaḥ |\nsurabhi no mukhā karat pra ṇa āyūṃṣi tāriṣat ||',
    'I have made praise of Dadhikrāvan, the victorious, vigorous horse. May he make our mouths fragrant and carry our lives onward.'
)
GAYATRI = 'tat savitur vareṇyaṃ bhargo devasya dhīmahi |\ndhiyo yo naḥ pracodayāt ||'
GAYATRI_MEANING = 'We meditate on that worthy-of-choice radiance of the god Savitṛ. May he impel our thoughts.'
PRASHANA = {
    'pratah': (
        'sūryaś ca mā manyuś ca manyupatayaś ca manyukṛtebhyaḥ |\npāpebhyo rakṣantām | yad rātryā pāpam akārṣam |\nmanasā vācā hastābhyām | padbhyām udareṇa śiśnā |\nrātris tad avalumpatu | yat kiñca duritaṃ mayi |\nidam ahaṃ mām amṛtayonau | sūrye jyotiṣi juhomi svāhā ||',
        'May Sūrya, Manyu, and the lords of Manyu protect me from wrongs committed through anger. Whatever wrong I did during the night, with mind, speech, hands, feet, belly or sexual organ, may the night remove it. Whatever fault is in me, I offer this self of mine into the light of the sun, the source of immortality. Svāhā—may the offering be received.'
    ),
    'madhyanikam': (
        "āpaḥ punantu pṛthivīṃ pṛthivī pūtā punātu mām |\npunantu brahmaṇaspatiḥ brahma pūtā punātu mām |\nyad ucchiṣṭam abhojyaṃ yad vā duścaritaṃ mama |\nsarvaṃ punantu mām āpo 'satāṃ ca pratigrahaṃ svāhā ||",
        'May the waters purify the earth; may the purified earth purify me. May the Lord of sacred utterance purify; may the earth, purified by brahman, purify me. Whatever leftover or forbidden food I have eaten, whatever misconduct is mine, and acceptance of gifts from the unworthy—may the waters cleanse me of it all. Svāhā. “Earth” in the second sentence is supplied from the preceding line; brahman here can be understood as sacred knowledge or utterance.'
    ),
    'saayam': (
        'agniś ca mā manyuś ca manyupatayaś ca manyukṛtebhyaḥ |\npāpebhyo rakṣantām | yad ahnā pāpam akārṣam |\nmanasā vācā hastābhyām | padbhyām udareṇa śiśnā |\nahas tad avalumpatu | yat kiñca duritaṃ mayi |\nidam ahaṃ mām amṛtayonau | satye jyotiṣi juhomi svāhā ||',
        'May Agni, Manyu, and the lords of Manyu protect me from wrongs committed through anger. Whatever wrong I did during the day, with mind, speech, hands, feet, belly or sexual organ, may the day remove it. Whatever fault is in me, I offer this self of mine into the light of truth, the source of immortality. Svāhā—may the offering be received.'
    ),
}
PRAYER = (
    'namo brahmaṇyadevāya gobrāhmaṇahitāya ca |\njagaddhitāya kṛṣṇāya govindāya namo namaḥ ||\nā brahmalokād āśeṣād ālokālokaparvatāt |\nye vasanti dvijā devās tebhyo nityaṃ namo namaḥ ||',
    'Salutation to the god devoted to sacred learning, benefactor of cows and Brahmins; repeated salutation to Kṛṣṇa, Govinda, benefactor of the world. To the twice-born and divine beings dwelling throughout the realms, as far as Brahmā’s world and the Lokāloka mountain, my constant salutations.'
)
BHUMI = (
    'apasarpantu te bhūtā ye bhūtā bhuvi saṃsthitāḥ |\nye bhūtā vighnakartāras te gacchantu śivājñayā ||\nugrabhūtapiśācādyā ye ca vai bhūmibhārakāḥ |\neteṣām avirodhena brahmakarma samārabhe ||',
    'May those beings dwelling on the earth withdraw. May those who cause obstacles depart by Śiva’s command. Without opposition from fierce beings, spirits and others that burden the earth, I begin the sacred rite.'
)
ASANA = (
    'pṛthvi tvayā dhṛtā lokā devi tvaṃ viṣṇunā dhṛtā |\ntvaṃ ca dhāraya māṃ devi pavitraṃ kuru cāsanam ||',
    'Earth, the worlds are upheld by you; goddess, you are upheld by Viṣṇu. Uphold me also, goddess, and make this seat pure.'
)
PRANAYAMA_NYASA = (
    'praṇavasya ṛṣir brahmā | devī gāyatrī chandaḥ | paramātmā devatā |\nbhūrādi sapta vyāhṛtīnām atri-bhṛgu-kutsa-vasiṣṭha-gautama-kāśyapa-āṅgirasa ṛṣayaḥ |\ngāyatrī-uṣṇig-anuṣṭub-bṛhatī-paṅkti-triṣṭub-jagatyaś chandāṃsi |\nagni-vāyv-arka-vāgīśa-varuṇendra-viśvedevā devatāḥ |\nprāṇāyāme viniyogaḥ |\nsāvitryā ṛṣir viśvāmitraḥ | devī gāyatrī chandaḥ | savitā devatā |\ngāyatrīśiraso brahmā ṛṣiḥ | anuṣṭup chandaḥ | paramātmā devatā |\nsarveṣāṃ prāṇāyāme viniyogaḥ |',
    'For Oṃ: Brahmā is the seer, Devī Gāyatrī the metre, the Supreme Self the deity. For the seven utterances beginning Bhūḥ: the seers are Atri, Bhṛgu, Kutsa, Vasiṣṭha, Gautama, Kāśyapa and Āṅgirasa; the metres are Gāyatrī, Uṣṇih, Anuṣṭubh, Bṛhatī, Paṅkti, Triṣṭubh and Jagatī; the deities are Agni, Vāyu, Arka, Vāgīśa, Varuṇa, Indra and the All-gods. Their use is in prāṇāyāma. For Sāvitrī: Viśvāmitra, Devī Gāyatrī and Savitṛ. For the Gāyatrī “head” formula: Brahmā, Anuṣṭubh and the Supreme Self. All are used in prāṇāyāma.'
)
AVAHANA_NYASA = (
    'āyātv ity anuvākasya vāmadeva ṛṣiḥ | anuṣṭup chandaḥ | gāyatrī devatā | gāyatrī āvāhane viniyogaḥ |',
    'For the passage beginning Āyātu: Vāmadeva is the seer, Anuṣṭubh the metre, and Gāyatrī the deity. It is used for invoking Gāyatrī.'
)
AVAHANA = (
    "āyātu varadā devī akṣaraṃ brahma sammitam |\ngāyatrīṃ chandasāṃ mātedaṃ brahma juṣasva naḥ ||\nojo 'si saho 'si balam asi bhrājo 'si |\ndevānāṃ dhāma nāmāsi viśvam asi viśvāyuḥ |\nsarvam asi sarvāyur abhibhūr om ||\ngāyatrīm āvāhayāmi | sāvitrīm āvāhayāmi | sarasvatīm āvāhayāmi |",
    'May the boon-giving goddess come, the imperishable sacred syllable commensurate with brahman. Gāyatrī, mother of the metres, accept this sacred utterance of ours. You are vigour, might, strength and brilliance; you are the abode of the gods, their name; you are the universe and the life of all. You are everything, the life of everything, the one surpassing all. Oṃ. I invoke Gāyatrī; I invoke Sāvitrī; I invoke Sarasvatī.'
)
JAPA_NYASA = (
    'sāvitryā ṛṣir viśvāmitraḥ | nicṛd gāyatrī chandaḥ | savitā devatā |\ngāyatrī mahāmantra jape viniyogaḥ |',
    'For Sāvitrī: Viśvāmitra is the seer, Nicṛd Gāyatrī the metre (Gāyatrī with one syllable fewer), and Savitṛ the deity. It is used for repetition of the great Gāyatrī mantra.'
)
DHYANA = (
    'muktāvidrumahemanīladhavalacchāyair mukhais trīkṣaṇaiḥ |\nyuktām indukalānibaddharatnamakuṭāṃ tattvārthavarṇātmikām |\ngāyatrīṃ varadābhayāṅkuśakaśāḥ śubhraṃ kapālaṃ gadāṃ |\nśaṅkhaṃ cakram athāravindayugalaṃ hastair vahantīṃ bhaje ||\nyo devaḥ savitāsmākaṃ dhiyo dharmādigocarāḥ |\nprerayet tasya yad bhargas tad vareṇyam upāsmahe ||',
    'I worship Gāyatrī, whose three-eyed faces have the hues of pearl, coral, gold, blue and white; whose jewelled crown bears the crescent moon; whose syllables embody the meaning of the principles of reality. Her hands show the gestures of granting boons and freedom from fear, and carry a goad, whip, white skull-bowl, mace, conch, discus and a pair of lotuses. We worship that choice radiance of the god Savitṛ who may impel our thoughts towards dharma and the other aims of life.'
)
DISMISS_NYASA = (
    'uttama ity anuvākasya vāmadeva ṛṣiḥ | anuṣṭup chandaḥ | gāyatrī devatā | gāyatrī udvāsane viniyogaḥ |',
    'For the passage beginning Uttame: Vāmadeva is the seer, Anuṣṭubh the metre, and Gāyatrī the deity. It is used for bidding farewell to Gāyatrī.'
)
DISMISS = (
    'uttame śikhare devi bhūmyāṃ parvatamūrdhani |\nbrāhmaṇebhyo hy anujñānaṃ gaccha devi yathāsukham ||',
    'Goddess, to the highest peak, to the mountain summit on earth, go at your pleasure, with leave from the Brahmins. This gives the sense of the ritual farewell reading; other editions have abhyanujñātā (“having been given leave”).'
)
YAMA = (
    'yamāya dharmarājāya mṛtyave cāntakāya ca |\nvaivasvatāya kālāya sarvabhūtakṣayāya ca ||\naudumbarāya dadhnāya nīlāya parameṣṭhine |\nvṛkodarāya citrāya citraguptāya vai namaḥ ||\ncitraguptāya vai nama om nama iti |',
    'Salutation to Yama, king of dharma; to Death and the Ender; to the son of Vivasvat, Time, and the one who brings all beings to their end; to Audumbara, Dadhna, the dark one, the supremely stationed one, the wolf-bellied one, Citra and Citragupta. Salutation again to Citragupta. Oṃ, salutation. Audumbara and Dadhna are retained as traditional names.'
)
HARIHARA = (
    'ṛtaṃ satyaṃ paraṃ brahma puruṣaṃ kṛṣṇapiṅgalam |\nūrdhvaretaṃ virūpākṣaṃ viśvarūpāya vai namo namaḥ ||\nviśvarūpāya vai nama om nama iti |',
    'Repeated salutation to the one whose form is the universe: sacred order, truth, supreme brahman, the Person, dark and tawny, whose generative power rises upward, whose eyes are distinctive. Salutation to the universal form. Oṃ, salutation.'
)
NARMADA = (
    "narmadāyai namaḥ prātar narmadāyai namo niśi |\nnamo 'stu narmade tubhyaṃ trāhi māṃ viṣasarpataḥ ||\napasarpa sarpa bhadraṃ te dūraṃ gaccha mahāyaśāḥ |\njanamejayasya yajñānte āstīkavacanaṃ smaran ||\njaratkāror jaratkārvāṃ samutpanno mahāyaśāḥ |\nāstīkaḥ satyasandho māṃ pannagebhyo 'bhirakṣatu ||\npannagebhyo 'bhirakṣatv om nama iti |",
    'Salutation to Narmadā in the morning and at night. Narmadā, I salute you; protect me from venomous snakes. Withdraw, serpent; may it be well with you. Go far away, renowned one, remembering Āstīka’s words at the end of Janamejaya’s sacrifice. May the renowned, true-to-his-word Āstīka, born to Jaratkāru and Jaratkāru, protect me from serpents. May he protect me from serpents. Oṃ, salutation.'
)
SURYA_NARAYANA = (
    'namaḥ savitre jagadekacakṣuṣe |\njagatprasūtisthitināśahetave |\ntrayīmayāya triguṇātmadhāriṇe |\nviriñcinārāyaṇaśaṅkarātmane ||\ndhyeyaḥ sadā savitṛmaṇḍalamadhyavartī |\nnārāyaṇaḥ sarasijāsanasanniviṣṭaḥ |\nkeyūravān makarakuṇḍalavān kirīṭī |\nhārī hiraṇmayavapur dhṛtaśaṅkhacakraḥ ||\nśaṅkhacakragadāpāṇe dvārakānilayācyuta |\ngovinda puṇḍarīkākṣa rakṣa māṃ śaraṇāgatam ||\nākāśāt patitaṃ toyaṃ yathā gacchati sāgaram |\nsarvadevanamaskāraḥ keśavaṃ prati gacchati ||\nkeśavaṃ prati gacchatv om nama iti |',
    'Salutation to Savitṛ, the world’s single eye, the cause of its birth, continuance and dissolution; embodying the three Vedas and bearing the three qualities; having the nature of Viriñci (Brahmā), Nārāyaṇa and Śaṅkara. Always meditate on Nārāyaṇa in the centre of the solar disc, seated on a lotus, with armlets, makara-shaped earrings, crown and necklace, a golden body, and conch and discus in his hands. Unfailing one dwelling in Dvārakā, bearer of conch, discus and mace, Govinda, lotus-eyed one, protect me who has sought refuge. As water fallen from the sky reaches the ocean, salutation to every deity reaches Keśava. May it reach Keśava. Oṃ, salutation.'
)
SAMARPANA = (
    'kāyena vācā manasendriyair vā buddhyātmanā vā prakṛteḥ svabhāvāt |\nkaromi yad yat sakalaṃ parasmai nārāyaṇāyeti samarpayāmi ||\noṃ tat sat brahmārpaṇam astu |',
    'Whatever I do through body, speech, mind or senses, through understanding or self, or by the disposition of nature, I offer it all to the supreme Nārāyaṇa. Oṃ, That, the Real; may this be an offering to brahman.'
)

MITRA_LAST = (
    'pra sa mitra marto astu prayasvān yas ta āditya śikṣati vratena |\nna hanyate na jīyate tvoto nainam aṃho aśnoty antito na dūrāt ||',
    'Mitra, may that mortal who honours you, Āditya, through observance be rich in offerings. Protected by you, he is neither slain nor overcome; distress reaches him neither from nearby nor from afar.'
)
YAJUR_MITRA = [
    ('oṃ mitrasya carṣaṇīdhṛtaḥ śravo devasya sānasim |\nsatyaṃ citraśravastamam ||', 'The fame of the god Mitra, sustainer of peoples, is gainful, true and most splendid in renown.'),
    ('mitro janān yātayati prajānan mitro dādhāra pṛthivīm uta dyām |\nmitraḥ kṛṣṭīr animiṣābhicaṣṭe satyāya havyaṃ ghṛtavad vidhema ||', 'Mitra, knowing, sets people in order; Mitra has upheld earth and heaven. Mitra watches the peoples without blinking. To the true one let us offer oblation rich in ghee.'),
    MITRA_LAST,
]
RIG_MITRA = [
    ("mitrasya carṣaṇīdhṛto 'vo devasya sānasi |\ndyumnaṃ citraśravastamam ||", 'The favour of the god Mitra, sustainer of peoples, brings gain: splendour most brilliant in renown.'),
    ('mitro janān yātayati bruvāṇo mitro dādhāra pṛthivīm uta dyām |\nmitraḥ kṛṣṭīr animiṣābhicaṣṭe mitrāya havyaṃ ghṛtavaj juhota ||', 'Mitra, speaking, sets people in order; Mitra has upheld earth and heaven. Mitra watches the peoples without blinking. Pour for Mitra an oblation rich in ghee.'),
    MITRA_LAST,
]
YAJUR_VARUNA = [
    ('imaṃ me varuṇa śrudhī havam adyā ca mṛḍaya |\ntvām avasyur ā cake ||', 'Varuṇa, hear this call of mine and show mercy today. Seeking help, I call upon you.'),
    ('tat tvā yāmi brahmaṇā vandamānas tadā śāste yajamāno havirbhiḥ |\naheḍamāno varuṇeha bodhy uruśaṃsa mā na āyuḥ pra moṣīḥ ||', 'I approach you for this, bowing with sacred utterance; the sacrificer asks this with offerings. Varuṇa, be attentive here without anger. Widely praised one, do not take away our life.'),
    ('yac cid dhi te viśo yathā pra deva varuṇa vratam |\nminīmasi dyavi dyavi ||', 'Whatever ordinance of yours, god Varuṇa, we violate day after day, as people do…'),
    ("yat kiñcedaṃ varuṇa daivye jane 'bhidrohaṃ manuṣyāś carāmasi |\nacittī yat tava dharmā yuyopima mā nas tasmād enaso deva rīriṣaḥ ||", 'Whatever offence we humans commit against the divine folk, Varuṇa, whatever laws of yours we have disregarded through lack of understanding—god, do not harm us for that fault.'),
    ('kitavāso yad riripur na dīvi yad vā ghā satyam uta yan na vidma |\nsarvā tā viṣya śithireva devāthā te syāma varuṇa priyāsaḥ ||', 'Whatever wrong we have done, as gamblers cheat at play, whether knowingly or without knowing—loosen all those bonds, god, as things loosely tied; then, Varuṇa, may we be dear to you.'),
]
RIG_VARUNA = [(s.replace('mṛḍaya', 'mṛḷaya').replace('aheḍamāno', 'aheḷamāno'), m) for s, m in YAJUR_VARUNA[:2]]
YAJUR_SURYA = [
    ('ā satyena rajasā vartamāno niveśayann amṛtaṃ martyaṃ ca |\nhiraṇyayena savitā rathenā devo yāti bhuvanā vipaśyan ||', 'Moving through the true expanse, settling immortal and mortal alike, the god Savitṛ travels in his golden chariot, looking over the worlds.'),
    ('ud vayaṃ tamasas pari paśyanto jyotir uttaram |\ndevaṃ devatrā sūryam aganma jyotir uttamam ||', 'Rising beyond darkness, seeing the higher light, we have reached Sūrya, the god among the gods, the highest light.'),
    ('udu tyaṃ jātavedasaṃ devaṃ vahanti ketavaḥ |\ndṛśe viśvāya sūryam ||', 'The rays carry upward that all-knowing god, Sūrya, for everyone to see.'),
    ('citraṃ devānām udagād anīkaṃ cakṣur mitrasya varuṇasyāgneḥ |\nāprā dyāvāpṛthivī antarikṣaṃ sūrya ātmā jagatas tasthuṣaś ca ||', 'The radiant face of the gods has risen, the eye of Mitra, Varuṇa and Agni. Sūrya has filled heaven, earth and the space between: the self of all that moves and all that stands.'),
    ('tac cakṣur devahitaṃ purastāc chukram uccarat |\npaśyema śaradaḥ śataṃ | jīvema śaradaḥ śataṃ |\nnandāma śaradaḥ śataṃ | modāma śaradaḥ śataṃ |\nbhavāma śaradaḥ śataṃ | śṛṇavāma śaradaḥ śataṃ |\nprabravāma śaradaḥ śataṃ | ajītāḥ syāma śaradaḥ śataṃ |\njyok ca sūryaṃ dṛśe ||', 'That eye, set by the gods, rises bright in the east. May we see for a hundred autumns, live for a hundred autumns, rejoice, delight, continue to be, hear, speak, and remain unconquered for a hundred autumns; and long may we see the sun.'),
    ("ya udagān mahato 'rṇavād vibhrājamānaḥ salilasya madhyāt |\nsa mā vṛṣabho lohitākṣaḥ sūryo vipaścin manasā punātu ||", 'He who has risen from the great ocean, shining from the midst of the waters—that mighty, red-eyed, discerning Sūrya—may he purify me through his mind.'),
]
RIG_SURYA = [
    YAJUR_SURYA[2],
    ('apa tye tāyavo yathā nakṣatrā yanty aktubhiḥ |\nsūrāya viśvacakṣase ||', 'Like thieves, those stars depart with the nights before the all-seeing sun.'),
    ('adṛśram asya ketavo vi raśmayo janāṃ anu |\nbhrājanto agnayo yathā ||', 'His beams have appeared, his rays spreading among the peoples, shining like fires.'),
    ('taraṇir viśvadarśato jyotiṣkṛd asi sūrya |\nviśvam ā bhāsi rocanam ||', 'Swift-moving, visible to all, you are the maker of light, Sūrya. You illuminate the whole shining realm.'),
    ('pratyaṅ devānāṃ viśaḥ pratyaṅṅ udeṣi mānuṣān |\npratyaṅ viśvaṃ svar dṛśe ||', 'Facing the hosts of gods, facing human beings, you rise, facing all, so that the sunlight may be seen.'),
    ('yenā pāvaka cakṣasā bhuraṇyantaṃ janāṃ anu |\ntvaṃ varuṇa paśyasi ||', 'With that purifying eye, Varuṇa, you look upon the active one among the peoples. The solar eye is addressed here in relation to Varuṇa.'),
    ('vi dyām eṣi rajas pṛthv ahā mimāno aktubhiḥ |\npaśyañ janmāni sūrya ||', 'You traverse heaven and the broad expanse, measuring days with nights, Sūrya, looking upon living generations.'),
    ('sapta tvā harito rathe vahanti deva sūrya |\nśociṣkeśaṃ vicakṣaṇa ||', 'Seven bay steeds carry you in your chariot, god Sūrya, far-seeing one with flame-like hair.'),
    ('ayukta sapta śundhyuvaḥ sūro rathasya naptyaḥ |\ntābhir yāti svayuktibhiḥ ||', 'The sun has yoked the seven pure daughters of the chariot; with these, yoked by himself, he travels.'),
    ('ud vayaṃ tamasas pari jyotiṣ paśyanta uttaram |\ndevaṃ devatrā sūryam aganma jyotir uttamam ||', YAJUR_SURYA[1][1]),
    ('udyann adya mitramaha ārohann uttarāṃ divam |\nhṛdrogaṃ mama sūrya harimāṇaṃ ca nāśaya ||', 'Rising today, great in friendly radiance, ascending the higher heaven, Sūrya, dispel my heart disease and yellowness.'),
    ('śukeṣu me harimāṇaṃ ropaṇākāsu dadhmasi |\natho hāridraveṣu me harimāṇaṃ ni dadhmasi ||', 'We place my yellowness in the parrots and ropaṇākā birds; we place my yellowness in the hāridrava birds. The exact identification of the latter bird names is uncertain.'),
    ('ud agād ayam ādityo viśvena sahasā saha |\ndviṣantaṃ mahyaṃ randhayan mo ahaṃ dviṣate radham ||', 'This Āditya has risen with all his might, subduing the one who hates me; may I not fall subject to the one who hates me.'),
]
RIG_LATE = {
    'pratah': ('yad adya kac ca vṛtrahann udagā abhi sūrya |\nsarvaṃ tad indra te vaśe ||', 'Whatever you have risen over today, sun, slayer of Vṛtra, all of that, Indra, is under your power.'),
    'madhyanikam': ('ud ghed abhi śrutāmaghaṃ vṛṣabhaṃ naryāpasam |\nastāram eṣi sūrya ||', 'You rise, sun, towards him whose bounty is renowned, the mighty bull of manly deeds, the archer.'),
    'saayam': ('na tasya māyayā cana ripur īśīta martyaḥ |\nyo agnaye dadāśa havyadātibhiḥ ||', 'No mortal foe, even through cunning, shall gain mastery over the one who has given to Agni with offerings of oblation.'),
}
RIG_PRAYERS = [
    ('1.99.1', 'kāśyapa', 'triṣṭup', 'agniḥ', 'jātavedase sunavāma somam arātīyato ni dahāti vedaḥ |\nsa naḥ parṣad ati durgāṇi viśvā nāveva sindhuṃ duritāty agniḥ ||', 'Let us press Soma for Jātavedas, who burns up the possessions of the hostile one. May Agni carry us across all difficulties, across evils, as a boat across a river.'),
    ('1.133.5', 'parucchepa', 'gāyatrī', 'indraḥ', 'piśaṅgabhṛṣṭim ambhṛṇaṃ piśācim indra saṃ mṛṇa |\nsarvaṃ rakṣo ni barhaya ||', 'Indra, crush the tawny-pointed, roaring female fiend. Strike down every malevolent being. The descriptive epithets admit differing translations.'),
    ('1.89.8', 'gotama', 'triṣṭup', 'viśvedevāḥ', 'bhadraṃ karṇebhiḥ śṛṇuyāma devā bhadraṃ paśyemākṣabhir yajatrāḥ |\nsthirair aṅgais tuṣṭuvāṃsas tanūbhir vyaśema devahitaṃ yad āyuḥ ||', 'Gods, may we hear what is auspicious with our ears; worshipful ones, may we see what is auspicious with our eyes. Praising with firm limbs and bodies, may we live out the lifespan allotted by the gods.'),
    ('10.136.1', 'jūti', 'anuṣṭup', 'agniḥ', 'keśy agniṃ keśī viṣaṃ keśī bibharti rodasī |\nkeśī viśvaṃ svar dṛśe keśīdaṃ jyotir ucyate ||', 'The long-haired one bears fire, poison, and the two worlds. The long-haired one bears all the sunlight for seeing; the long-haired one is called this light.'),
]
