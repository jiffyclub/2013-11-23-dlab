import animals

def test_read_animals():
    date, time, species, count = animals.read_animals('animals.txt')

    assert date == ['2011-04-22', '2011-04-23', '2011-04-23', '2011-04-23', '2011-04-23']
    assert time == ['21:06', '14:12', '10:24', '20:08', '18:46']
    assert species == ['Grizzly', 'Elk', 'Elk', 'Wolverine', 'Muskox']
    assert count == [36, 25, 26, 31, 20]


def test_filter_animals():
    d, t, s, c = animals.read_animals('animals.txt')
    date, time, species, count = animals.filter_animals(d, t, s, c, 'Grizzly')

    assert date == ['2011-04-22']
    assert time == ['21:06']
    assert species == ['Grizzly']
    assert count == [36]


# def test_mean():
#     m = animals.mean([0])
#     assert m == 0

#     m = animals.mean([0, 10])
#     assert m == 5

#     m = animals.mean([7, 8])
#     assert m == 7.5

#     m = animals.mean([1, 2, 3, 4])
#     assert m == 2.5


def test_mean_animals():
    m = animals.mean_animals('animals.txt', 'Grizzly')
    assert m == 36

    m = animals.mean_animals('animals.txt', 'Elk')
    assert m == 25.5
