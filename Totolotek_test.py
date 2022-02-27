from Totolotek import lottery


def test_1_lottery():

    assert len(lottery()) == 6


def test_2_lottery():
    assert len(set(lottery())) == 6
    assert type(lottery()) is list
