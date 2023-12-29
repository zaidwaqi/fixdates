import difflib
import re

def fix_month_name(dt):
    monmap = {
        'january': 'jan',
        'february': 'feb',
        'march': 'mar',
        'april': 'apr',
        'may': 'may',
        'june': 'jun',
        'july': 'jul',
        'august': 'aug',
        'september': 'sep',
        'october': 'oct',
        'november': 'nov',
        'december': 'dec',
        'januari': 'jan',
        'februari': 'feb',
        'mac': 'mar',
        'ogos': 'aug',
        'september': 'sep',
        'oktober': 'oct',
        'november': 'nov',
        'disember': 'dec'
    }
    try:
        # split 20-APR-2020 to d = 20, m = APR, y = 2020, applicable to all separators
        d, m, y = re.split(r"[ :\-/\s]+", dt.strip())
    except(ValueError):
        # split 20APR2020 to d = 20, m = APR, y = 2020
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', dt)
        regex_pattern = re.compile(r'[a-zA-Z]+')
        matches = regex_pattern.findall(cleaned_text)
        idx = dt.index(matches[0])
        d = dt[:idx]
        m = matches[0]
        y = dt[idx+len(m):]
    months = list(set(monmap.keys()) | set(monmap.values()))
    close_match = difflib.get_close_matches(m.lower(), months, 1)
    if close_match == []:
        return dt
    
    m = monmap.get(close_match[0])
    return f'{d}-{m}-{y}'.upper()