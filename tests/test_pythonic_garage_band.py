from pythonic_garage_band.band import Musicians, Band


def test_BandName():
    actual = Band("radiohead").name
    expected = "radiohead"
    assert expected == actual

