import bitcoinfees


def test_recommended():
    response = bitcoinfees.recommended()
    for speed in ["fastestFee", "halfHourFee", "hourFee"]:
        assert speed in response
