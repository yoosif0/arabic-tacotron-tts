from text import cleaners

def test_transliteration_cleaners():
    actual = cleaners.transliteration_cleaners('تَسْدِيدَةٍ اسْتَعْصَتْ عَلَى الْحَارِسْ')
    expected = 'tasdiyda@in sta`sat `ala~ lharis'
    assert actual == expected


def test_basic_cleaner():
    actual = cleaners.basic_cleaners('تَسْدِيدَةٍ اسْتَعْصَتْ عَلَى الْحَارِسْ')
    expected = 'تَسْدِيدَةٍ اسْتَعْصَتْ عَلَى الْحَارِسْ'
    assert actual == expected

def english_cleaner():
    actual = cleaners.english_cleaners('I want to be there early on the day. Please organize')
    expected = 'I want to be there early on the day. Please organize'
    assert actual == expected

def test_phones_cleaner():
    actual = cleaners.basic_cleaners('{hh aw1 s s t ah0 n}. {y e s}, {hh aw1 s s t ah0 n}. {y e s}')
    expected = '{hh aw1 s s t ah0 n}. {y e s}, {hh aw1 s s t ah0 n}. {y e s}'
    assert actual == expected

def test_phones_cleaner_convert_arabic_comma():
    actual = cleaners.arabic_cleaners('{hh aw1 s s t ah0 n}. {y e s}، {hh aw1 s s t ah0 n}. {y e s}')
    expected = '{hh aw1 s s t ah0 n}. {y e s}, {hh aw1 s s t ah0 n}. {y e s}'
    assert actual == expected

def test_phones_cleaner_convert_dash():
    actual = cleaners.arabic_cleaners('{hh aw1 s s t ah0 n}. {y e s} - {hh aw1 s s t ah0 n}. {y e s} dsd sd')
    expected = '{hh aw1 s s t ah0 n}. {y e s} - {hh aw1 s s t ah0 n}. {y e s} dsd sd'
    assert actual == expected
