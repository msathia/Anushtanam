"""Build the Tamil and English landing pages using the shared card layout."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PERIODS = ('pratah-sandhyavandanam', 'madhyanikam', 'saayam-sandhyavandanam')


def build_landing_pages(root=ROOT):
    for english in (False, True):
        lang = 'en' if english else 'ta'
        brand = 'Anushtanam' if english else 'அனுஷ்டானம்'
        heading = 'Daily Sandhyāvandanam' if english else 'தினசரி ஸந்த்யாவந்தனம்'
        intro = 'Choose your Veda and time of day.' if english else 'உங்கள் வேதத்தையும் வேளையையும் தேர்ந்தெடுக்கவும்.'
        language = '<strong>English</strong> / <a href="../" lang="ta" hreflang="ta">தமிழ்</a>' if english else '<a href="en/" lang="en" hreflang="en">English</a> / <strong>தமிழ்</strong>'
        titles = ['Rigveda', 'Yajurveda'] if english else ['ரிக்வேதம்', 'யஜுர்வேதம்']
        traditions = ['Ṛgveda<br>Āśvalāyana · Smārta', 'Kṛṣṇa Yajurveda · Taittirīya<br>Āpastamba · Smārta'] if english else ['ஆச்வலாயன ஸூத்ரம்<br>ஸ்மார்த்த வழிமுறை', 'க்ருஷ்ண யஜுர்வேதம் · தைத்திரீய சாகை<br>ஆபஸ்தம்ப ஸூத்ரம் · ஸ்மார்த்த வழிமுறை']
        times = ['Morning', 'Noon', 'Evening'] if english else ['காலை', 'மதியம்', 'மாலை']
        details = ['Prātaḥ · Sunrise', 'Mādhyāhnika · Solar noon', 'Sāyaṃ · Sunset'] if english else ['ப்ராத: · ஸூர்யோதயம்', 'மாத்யாஹ்நிகம் · நடுப்பகல்', 'ஸாயம் · ஸூர்யாஸ்தமனம்']
        cards = []
        for i, veda in enumerate(('rigveda', 'yajurveda')):
            links = []
            for suffix, time, detail, icon in zip(PERIODS, times, details, ('sunrise', 'sun', 'sunset')):
                links.append(f'<a class="period" href="{veda}-{suffix}/"><svg class="icon" aria-hidden="true"><use href="#{icon}"/></svg><span><strong>{time}</strong><small>{detail}</small></span><span class="arrow" aria-hidden="true">→</span></a>')
            cards.append(f'<section class="veda" aria-labelledby="{veda}-title"><h2 id="{veda}-title">{titles[i]}</h2><p class="tradition">{traditions[i]}</p><nav class="periods" aria-label="{titles[i]}">{chr(10).join(links)}</nav></section>')
        other_heading = 'Other practices' if english else 'பிற அனுஷ்டானங்கள்'
        other_titles = ['Brahmayajña', 'Gāyatrī japa'] if english else ['ப்ரஹ்மயஜ்ஞம்', 'காயத்ரீ ஜபம்']
        other_details = ['Rigveda · Smārta · Tamil guide', '1008 repetitions · Tamil guide'] if english else ['ரிக்வேதி ஸ்மார்த்த வழிமுறை', '1008 காயத்ரீ மந்திர ஜபம்']
        prefix = '../' if english else ''
        other_cards = ''.join(f'<a class="other-card" href="{prefix}{url}"><span><h3>{title}</h3><p>{detail}</p></span><span class="arrow" aria-hidden="true">→</span></a>' for url, title, detail in zip(('brahma-yagnam.html', 'gayathri-japam.html'), other_titles, other_details))
        html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{brand} — {heading}</title><link rel="stylesheet" href="{prefix}landing.css"></head>
<body>
<svg class="symbols" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
<symbol id="sunrise" viewBox="0 0 24 24"><path d="M2 18h20M4 21h16M6 18a6 6 0 0 1 12 0M12 3v5M9 6l3-3 3 3M3 11l2 2M21 11l-2 2"/></symbol>
<symbol id="sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/></symbol>
<symbol id="sunset" viewBox="0 0 24 24"><path d="M2 18h20M4 21h16M6 18a6 6 0 0 1 12 0M12 3v5M9 5l3 3 3-3M3 11l2 2M21 11l-2 2"/></symbol>
</svg>
<main><header class="top"><div class="brand">{brand}</div><nav class="language" aria-label="Language">{language}</nav></header>
<h1>{heading}</h1><p class="intro">{intro}</p>
<div class="vedas">{chr(10).join(cards)}</div>
<section class="other" aria-labelledby="other-title"><h2 id="other-title">{other_heading}</h2><div class="other-grid">{other_cards}</div></section>
</main></body></html>
'''
        path = root / ('en/index.html' if english else 'index.html')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html)


if __name__ == '__main__':
    build_landing_pages()
