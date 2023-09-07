#get flag emoji
def get_flag(input_name):

    flag_dict={
        #Includes the only flags of the 193 UN Member states (and limited coverage for alternate names and spellings).
        'afghanistan': '🇦🇫',
        'albania': '🇦🇱',
        'algeria': '🇩🇿',
        'andorra': '🇦🇩',
        'angola' : '🇦🇴',
        'antingua & barbuda': '🇦🇬',
        'antigua and barbuda': '🇦🇬',
        'argentina': '🇦🇷',
        'armenia': '🇦🇲',
        'australia': '🇦🇺',
        'austria': '🇦🇹',
        'azerbaijan':'🇦🇿',
        'bahamas':'🇧🇸',
        'bahrain':'🇧🇭',
        'bangladesh': '🇧🇩',
        'barbados': '🇧🇧',
        'belarus':'🇧🇾',
        'belgium':'🇧🇪',
        'belize':'🇧🇿',
        'benin':'🇧🇯',
        'bhutan': '🇧🇹',
        'bolivia': '🇧🇴',
        'bosnia & herzegovina': '🇧🇦',
        'bosnia and herzegovina': '🇧🇦',
        'botswana': '🇧🇼',
        'brazil': '🇧🇷',
        'brunei': '🇧🇳',
        'bulgaria': '🇧🇬',
        'burkina faso': '🇧🇫',
        'burundi': '🇧🇮',
        'cambodia': '🇰🇭',
        'cameroon': '🇨🇲',
        'canada': '🇨🇦',
        'cape verde': '🇨🇻',
        'cabo verde': '🇨🇻',
        'central african republic': '🇨🇫',
        'chad': '🇹🇩',
        'chile': '🇨🇱',
        'china': '🇨🇳',
        'colombia': '🇨🇴',
        'comoros': '🇰🇲',
        'republic of the congo': '🇨🇬',
        'congo': '🇨🇬',
        'democratic republic of the congo': '🇨🇩',
        'costa rica': '🇨🇷',
        'cote divoire': '🇨🇮',
        'cote d\'ivoire': '🇨🇮',
        'côte d\'ivoire': '🇨🇮',
        'ivory coast': '🇨🇮',
        'croatia': '🇭🇷',
        'cuba': '🇨🇺',
        'cyprus': '🇨🇾',
        'czechia': '🇨🇿',
        'czech republic': '🇨🇿',
        'denmark': '🇩🇰',
        'djibouti': '🇩🇯',
        'dominica': '🇩🇲',
        'dominican republic': '🇩🇴',
        'ecuador': '🇪🇨',
        'egypt': '🇪🇬',
        'el salvador': '🇸🇻',
        'equatorial guinea': '🇬🇶',
        'eritrea': '🇪🇷',
        'estonia': '🇪🇪',
        'eswatini': '🇸🇿',
        'swaziland': '🇸🇿',
        'ethiopia': '🇪🇹',
        'fiji': '🇫🇯',
        'finland': '🇫🇮',
        'france': '🇫🇷',
        'gabon': '🇬🇦',
        'gambia': '🇬🇲',
        'georgia': '🇬🇪',
        'germany': '🇩🇪',
        'ghana': '🇬🇭',
        'greece': '🇬🇷',
        'grenada': '🇬🇩',
        'guatemala': '🇬🇹',
        'guinea': '🇬🇳',
        'guinea-bissau': '🇬🇼',
        'guinea bissau': '🇬🇼',
        'guyana': '🇬🇾',
        'haiti': '🇭🇹',
        'honduras': '🇭🇳',
        'hungary': '🇭🇺',
        'iceland': '🇮🇸',
        'india': '🇮🇳',
        'indonesia': '🇮🇩',
        'iran': '🇮🇷',
        'iraq': '🇮🇶',
        'ireland': '🇮🇪',
        'israel': '🇮🇱',
        'italy': '🇮🇹',
        'jamaica': '🇯🇲',
        'japan': '🇯🇵',
        'jordan': '🇯🇴',
        'kazakhstan': '🇰🇿',
        'kenya': '🇰🇪',
        'kiribati': '🇰🇮',
        'kuwait': '🇰🇼',
        'kyrgyzstan': '🇰🇬',
        'laos': '🇱🇦',
        'latvia': '🇱🇻',
        'lebanon': '🇱🇧',
        'lesotho': '🇱🇸',
        'liberia': '🇱🇷',
        'libya': '🇱🇾',
        'liechtenstein': '🇱🇮',
        'lithuania': '🇱🇹',
        'luxembourg': '🇱🇺',
        'madagascar': '🇲🇬',
        'malawi': '🇲🇼',
        'malaysia': '🇲🇾',
        'maldives': '🇲🇻',
        'mali': '🇲🇱',
        'malta': '🇲🇹',
        'marshall islands': '🇲🇭',
        'mauritania': '🇲🇷',
        'mauritius': '🇲🇺',
        'mexico': '🇲🇽',
        'micronesia': '🇫🇲',
        'moldova': '🇲🇩',
        'monaco': '🇲🇨',
        'mongolia': '🇲🇳',
        'montenegro': '🇲🇪',
        'morocco': '🇲🇦',
        'mozambique': '🇲🇿',
        'myanmar': '🇲🇲',
        'burma': '🇲🇲',
        'namibia': '🇳🇦',
        'nauru': '🇳🇷',
        'nepal': '🇳🇵',
        'netherlands': '🇳🇱',
        'new zealand': '🇳🇿',
        'nicaragua': '🇳🇮',
        'niger': '🇳🇪',
        'nigeria': '🇳🇬',
        'north korea': '🇰🇵',
        'north macedonia': '🇲🇰',
        'norway': '🇳🇴',
        'oman': '🇴🇲',
        'pakistan': '🇵🇰',
        'palau': '🇵🇼',
        'panama': '🇵🇦',
        'papua new guinea': '🇵🇬',
        'paraguay': '🇵🇾',
        'peru': '🇵🇪',
        'philippines': '🇵🇭',
        'poland': '🇵🇱',
        'portugal': '🇵🇹',
        'qatar': '🇶🇦',
        'romania': '🇷🇴',
        'russia': '🇷🇺',
        'rwanda': '🇷🇼',
        'samoa': '🇼🇸',
        'san marino': '🇸🇲',
        'sao tome and prinipe': '🇸🇹',
        'sao tome & prinipe': '🇸🇹',
        'são tomé and príncipe': '🇸🇹',
        'são tomé & príncipe': '🇸🇹',
        'saudi arabia': '🇸🇦',
        'senegal': '🇸🇳',
        'serbia': '🇷🇸',
        'seychelles': '🇸🇨',
        'sierra leone': '🇸🇱',
        'singapore': '🇸🇬',
        'slovakia': '🇸🇰',
        'slovenia': '🇸🇮',
        'solomon islands': '🇸🇧',
        'somalia': '🇸🇴',
        'south africa': '🇿🇦',
        'south korea': '🇰🇷',
        'south sudan': '🇸🇸',
        'spain': '🇪🇸',
        'sri lanka': '🇱🇰',
        'saint kitts and nevis': '🇰🇳',
        'saint kitts & nevis': '🇰🇳',
        'saint lucia': '🇱🇨',
        'saint vincent and the grenadines': '🇻🇨',
        'saint vincent & the grenadines': '🇻🇨',
        'sudan': '🇸🇩',
        'suriname': '🇸🇷',
        'sweden': '🇸🇪',
        'switzerland': '🇨🇭',
        'syria': '🇸🇾',
        'tajikistan': '🇹🇯',
        'tanzania': '🇹🇿',
        'thailand': '🇹🇭',
        'timor-leste': '🇹🇱',
        'timor leste': '🇹🇱',
        'togo': '🇹🇬',
        'tonga': '🇹🇴',
        'trinidad and tobago': '🇹🇹',
        'trinidad & tobago': '🇹🇹',
        'tunisia': '🇹🇳',
        'turkey': '🇹🇷',
        'türkiye': '🇹🇷',
        'turkiye': '🇹🇷',
        'turkmenistan': '🇹🇲',
        'tuvalu': '🇹🇻',
        'uganda': '🇺🇬',
        'ukraine': '🇺🇦',
        'uae': '🇦🇪',
        'united arab emirates': '🇦🇪',
        'uk': '🇬🇧',
        'gb': '🇬🇧',
        'united kingdom': '🇬🇧',
        'united kingdom of great britain and northern ireland': '🇬🇧',
        'great britain': '🇬🇧',
        'usa': '🇺🇸',
        'united states': '🇺🇸',
        'united states of america': '🇺🇸',
        'uruguay': '🇺🇾',
        'uzbekistan': '🇺🇿',
        'vanuatu': '🇻🇺',
        'venezuela': '🇻🇪',
        'vietnam': '🇻🇳',
        'yemen': '🇾🇪',
        'zambia': '🇿🇲',
        'zimbabwe': '🇿🇼'
    }

    flag = flag_dict.get(input_name.lower())

    if flag:
        return flag
    else:
        return '🏴'