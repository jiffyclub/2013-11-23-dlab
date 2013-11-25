import sys

import animals

if len(sys.argv) != 3:
    print 'Usage: mean_animals.py file_name species_name'
else:
    file_name = sys.argv[1]
    species_name = sys.argv[2]
    mean = animals.mean_animals(file_name, species_name)
    print mean
