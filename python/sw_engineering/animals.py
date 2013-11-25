import numpy

def read_animals(file_name):
    """
    Takes a file name and returns four lists:
    the date, time, species, and count columns.
    The count column is converted to integers.

    """
    date = []
    time = []
    species = []
    count = []

    with open(file_name) as f:
        for line in f:
            d, t, s, c = line.split()
            date.append(d)
            time.append(t)
            species.append(s)
            count.append(int(c))

    return date, time, species, count


def filter_animals(date, time, species, count, species_name):
    """
    Takes data lists and a single species name and filters the
    data for that animal.

    Returns four new filtered lists.

    """
    date_new = []
    time_new = []
    species_new = []
    count_new = []

    for i, s in enumerate(species):
        if s == species_name:
            date_new.append(date[i])
            time_new.append(time[i])
            species_new.append(s)
            count_new.append(count[i])

    return date_new, time_new, species_new, count_new


def mean_animals(file_name, species_name):
    date, time, species, count = read_animals(file_name)
    date, time, species, count = filter_animals(date, time, species, count, species_name)
    mean = numpy.mean(count)
    return mean
