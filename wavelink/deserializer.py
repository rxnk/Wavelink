import re

FILTER_RULES = {
    "CLEAN_EXPLICIT_FILTER_RULES": [
        (r'\s[([]Explicit[)\]]', ''),
        (r'\s[([]Clean[)\]]', ''),
    ],
    "FEATURE_FILTER_RULES": [
        (r'\s[([]feat\. .+[)\]]', ''),
        (r'\s(feat\. .+)', ''),
    ],
    "LIVE_FILTER_RULES": [
        (r'\s-\sLive(\s.+)?$', ''),
        (r'\s[([]Live[)\]]$', ''),
    ],
    "NORMALIZE_FEATURE_FILTER_RULES": [
        (r'\s[([](feat\. .+)[)\]]', r' \1'),
    ],
    "PARODY_FILTER_RULES": [
        (r'\s\(Parody of ".*" by .*\)$', ''),
        (r'\s\(Parody of ".*" by .* feat\. .*\)$', ''),
        (r'\s\(Lyrical Adaption of ".*"\)$', ''),
    ],
    "REISSUE_FILTER_RULES": [
        (r'\sRe-?issue$', ''),
        (r'\s\[.*?Re-?issue.*?\]', ''),
        (r'\s\(.*?Re-?issue.*?\)', ''),
    ],
    "REMASTERED_FILTER_RULES": [
        (r'Live\s\/\sRemastered', 'Live'),
        (r'\s[([].*Re-?[Mm]aster(ed)?.*[)\]]$', ''),
        (r'\s-\s\d{4}(\s-)?\s.*Re-?[Mm]aster(ed)?.*$', ''),
        (r'\s-\sRe-?[Mm]aster(ed)?.*$', ''),
        (r'\s\[Remastered\]\s\(Remastered\sVersion\)$', ''),
    ],
    "SUFFIX_FILTER_RULES": [
        (r'-\s(.+?)\s((Re)?mix|edit|dub|mix|vip|version)$', r'(\1 \2)'),
        (r'-\s(Remix|VIP|Instrumental)$', r'(\1)'),
    ],
    "TRIM_SYMBOLS_FILTER_RULES": [
        (r'\(+\s*\)+', ''),
        (r'^[/,:;~\s"-]+', ''),
        (r'[/,:;~\s"-]+$', ''),
        (r'\u0020{1,}', ' '),
    ],
    "VARIOUS_ARTISTS_FILTER_RULES": [
        (r'(Various Artists).+', r'\1'),
    ],
    "VERSION_FILTER_RULES": [
        (r'\s[([]Album Version[)\]]$', ''),
        (r'\s[([]Re-?recorded[)\]]$', ''),
        (r'\s[([]Single Version[)\]]$', ''),
        (r'\s[([]Edit[)\]]$', ''),
        (r'\s-\sMono Version$', ''),
        (r'\s-\sStereo Version$', ''),
        (r'\s\(Deluxe Edition\)$', ''),
        (r'\s[([]Expanded.*[)\]]$', ''),
        (r'\s-\sExpanded Edition$', ''),
        (r'\s[([]Explicit Version[)\]]', ''),
        (r'\s[([]Bonus Track Edition[)\]]', ''),
        (r'\s[([]\d+th\sAnniversary.*[)\]]', ''),
        (r'\s-\sOriginal$', ''),
        (r'\s-\sOriginal.*Version(\s\d{4})?$', ''),
    ],
    "YOUTUBE_TRACK_FILTER_RULES": [
        (r'^\s+|\s+$', ''),
        (r'\*+\s?\S+\s?\*+$', ''),
        (r'\[[^\]]+\]', ''),
        (r'【[^\]]+】', ''),
        (r'（[^\]]+）', ''),
        (r'\([^)]*version\)$', ''),
        (r'\.(avi|wmv|mpg|mpeg|flv)$', ''),
        (r'\(.*lyrics?\s*(video)?\)', ''),
        (r'\((of+icial\s*)?(track\s*)?stream\)', ''),
        (r'\((of+icial\s*)?((music|hd)\s*)?(video|audio)\)', ''),
        (r'-\s(of+icial\s*)?(music\s*)?(video|audio)$', ''),
        (r'\(.*Album\sTrack\)', ''),
        (r'\(\s*of+icial\s*\)', ''),
        (r'\(\s*[0-9]{4}\s*\)', ''),
        (r'\(\s*(HD|HQ)\s*\)$', ''),
        (r'(HD|HQ)\s?$', ''),
        (r'(vid[\u00E9e]o)?\s?clip\sof+ici[ae]l', ''),
        (r'of+iziel+es\s*video', ''),
        (r'vid[\u00E9e]o\s?clip', ''),
        (r'\sclip', ''),
        (r'full\s*album', ''),
        (r'\(live.*?\)$', ''),
        (r'\|.*$', ''),
        (r'^(|.*\s)"(.{5,})"(\s.*|)$', r'\2'),
        (r"^(|.*\s)'(.{5,})'(\s.*|)$", r'\2'),
        (r'\(.*[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}.*\)', ''),
        (r'sub\s*español', ''),
        (r'\s\(Letra\)', ''),
        (r'\s\(En\svivo\)', ''),
    ],
    "ADDITIONAL_ARTISTS_FILTER_RULES": [
        (r'\s(& .+)', ''),
        (r'\s(x .+)', ''),
    ],
}


def apply_filter_rules(text, rules):
    """Apply a list of filter rules to a given text.
    Each rule is a tuple (pattern, replacement).
    """

    for pattern, replacement in rules:
        text = re.sub(pattern, replacement, text)
    return text


def deserialize(text: str):
    """Apply all filter rules to the given text."""

    for rule_set in FILTER_RULES.values():
        text = apply_filter_rules(text, rule_set)

    return text