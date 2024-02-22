from mypackage import myModule

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert myModule.top_n([7,3,10,1,4,5], 4) == [10,7,5,4], 'incorrect'
    assert myModule.top_n([12,24,15,3,79], 2) == [79,24], 'incorrect'
    assert myModule.top_n([2,8,9,1,15,22,27,20,7], 6) == [27,22,20,15,9,8], 'incorrect'