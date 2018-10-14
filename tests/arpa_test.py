from datasets import arpa


def test_to_arpa():
    actual = arpa.to_arpa('تَسْدِيدَةٍ اسْتَعْصَتْ عَلَى الْحَارِسْ')
    expected = '{t a s d ii0 d a t i1 n} {s t a E S A t} {E a l a} {< a l H aa r i1 s}'
    assert actual == expected


def test_to_arpa_2():
    actual = arpa.to_arpa('تسديدة استعصت')
    expected = '{t s d ii0 d} {s t E S t}'
    assert actual == expected

def test_to_arpa_3():
    actual = arpa.to_arpa('الْف وَارْبَعَمِائَةٍ وَارْبَعُونَ حَرْفٌ')
    expected = '{< a l f} {w aa r b a E a m i0 < a t i1 n} {w aa r b a E uu0 n a} {H a r f u1 n}'
    assert actual == expected