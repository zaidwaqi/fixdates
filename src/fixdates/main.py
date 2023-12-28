import difflib

def fixdate(d):
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
    d, m, y = d.split()
    months = list(set(monmap.keys()) | set(monmap.values()))
    m = difflib.get_close_matches(m.lower(), months, 1) or [m]
    m = monmap.get(m[0], m[0])

    return f'{d} {m} {y}'.upper()

print(fixdate('25 ugust 2014'))
print(fixdate('14 Auust 2014'))
print(fixdate('18 Marc 2015'))
print(fixdate('18 desember 2015'))
print(fixdate('18 Marc 2015'))
print(fixdate('18 og 2015'))