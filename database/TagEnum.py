from enum import Enum,auto


class Tags(Enum):
    geometry = auto()
    graphs = auto()
    meet_in_the_middle = auto()
    binary_search = auto()
    binary_masks = auto()
    fast_Fourier_transform = auto()
    two_pointers = auto()
    trees = auto()
    dynamic_programming = auto()
    hungry_algorithms = auto()
    games = auto()
    interactive = auto()
    chinese_remainder_theorem = auto()
    combinatorics = auto()
    the_shortest_path = auto()
    mathematics = auto()
    matrix = auto()
    matching = auto()
    deep_search = auto()
    streams = auto()
    realisation = auto()
    disjoint_set_structure = auto()
    sorting = auto()
    strings = auto()
    data_structures = auto()
    probability_theory = auto()
    number_theory = auto()
    ternary_search = auto()
    hash = auto()

if __name__=="__main__":
    for data in Tags:
        print('{:15} = {}'.format(data.name, data.value))