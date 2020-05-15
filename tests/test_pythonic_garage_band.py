from pythonic_garage_band.band import Musicians, Band, Guitarist, Bassist, Drummer


def test_BandName():
    actual = Band("radiohead").name
    expected = "radiohead"
    assert expected == actual

def test_GuitarName():
    actual = Guitarist("jonny").name
    expected = "jonny"
    assert expected == actual

# def test_GuitarName():
#     actual = Guitarist("jonny").name
#     expected = "jonny"
#     assert expected == actual

def test_memberlist():
    actual = Musicians("jonny, thom, ed")
    expected = "jonny, thom, ed"
    assert expected == actual

# def
#     assert Band.to_list{} == []
#     radiohead

