def get_frequency(string: str) -> list[str, float]:
    """
        str - строка с шифром
        list - список частотности
        Данная функция создает список с частотой каждого символа
        """
    len_s = len(s)
    res = dict()
    for symbol in string:
        if symbol not in res:
            res[symbol] = 1
        else:
            res[symbol] += 1
    for item in res:
        res[item] /= len_s
    res = [[item, res[item]] for item in res]
    res.sort(key=lambda x: x[1])
    return reversed(res)


def write_file(pathname: str, string: str) -> None:
    """
    pathname - путь к файлу, в которую идёт запись
    string - записываемая строка
    Данная функция осуществляет запись строки string в файл по пути pathname
    """
    with open(pathname, 'w', encoding='utf-8') as file_write:
        file_write.write(string)
        file_write.close()


def replace_symbols(s, f_symbol, s_symbol):
    """
        s - рабочая строка
        f_symbol - первый символ замены
        s_symbol - второй символ замены
        Данная функция меняет два символа местами
        """
    new_s = ''
    for symbol in s:
        if symbol == f_symbol:
            new_s += s_symbol
        elif symbol == s_symbol:
            new_s += f_symbol
        else:
            new_s += symbol
    return new_s


s = '''И7У24>2 >МР4ДД >М2ЕПЧЙМД48 О4ЙАИЛМrЕt48ДЕ2ЧММИЙtЕХ4МШ4Ф1МЙ>ХИЙМУ1УМРОЕУ<Д >МР4ДД >МУ1УМЕЪУШtЕО4ДД 
ФМИ-УПД41МИМЙЕ<ХУМ8t>ДУЛМЙ>ЕtУУМrt>РrЕ14П4>ЙИЛМ<ЙЕМР4ДД 
>МrtЕУ8ОЕРЛЙИЛМУИЙЕ<ДУХЕ2МУМrt>РЕИЙ4О1ЛКЙИЛМХЕ2rt>ИИЕtЧМОМОУР>МИУ2ОЕ14МД4РМД>ХЕЙЕt 
2М41Ш4ОУЙЕ2Мt4ДАЫ>МО>ИАМrtЕЪ>ИИМИ74ЙУЛМД48 О41УМХЕРУtЕО4ДУ>2МУИЙЕ<ДУХ4МrЕИХЕ1АХЧМЕДЕМrtУ8О4ДЕМЧР41УЙАМУ85 
ЙЕ<ДЕИЙАМОМР4ДД ЩМД4МЕИДЕО>МУЩМrt>РИХ48Ч>2ЕИЙУМrЧЙ>2МУДЕПЕМrt>РИЙ4О1>ДУЛМР4ДД 
ЩММЙЕМ>ИЙАМУЩМХЕРУtЕО4ДУЛМ84МРО4МrЕИ1>РДУЩМР>ИЛЙУ1>ЙУЛМХ4tЙУД4МД>ИХЕ1АХЕМУ82>ДУ14ИАМr>tОЕФМ14ИЙЕ<ХЕФМИЙ414МУР>ЛМt48
Р>1УЙАМrtЕЪ>ИИМИ74ЙУЛМД4МРО4МО84У2ЕИОЛ84ДД ЩМrtЕЪ>ИИ4МХЕРУtЕО4ДУ>МД>rЕИt>РИЙО>ДДЕМОЕИrtЕУ8ОЕРЛЬ>>МИ74Й 
ФМrЕЙЕХ-МИУ2ОЕ1ЕОМУМ2ЕР>1УtЕО4ДУ>Мrt>РЕИЙ4О1ЛКЬ>>МОИКМД>Е5ЩЕРУ2ЧКМР1ЛМХЕРУtЕО4ДУЛМУДШЕt24ЪУК'''

res = get_frequency(s)
for a in res:
    print(a)
print()