defaultTree = {
    1962: {
        2012: {
            1961: 0,
            1994: 1
        },
        2002: 2
    },
    1965: {
        1990: 3,
        2003: {
            2012: 4,
            2002: {
                'X10': 5,
                'MESON': 6
            }
        }
    },
    1959: {
        1961: {
            2012: 7,
            2002: {
                'X10': 8,
                'MESON': 9
            }
        },
        1994: 10
    }
}


def main(data, tree=None):
    if tree is None:
        tree = defaultTree
    if type(tree) is int:
        return tree
    for val in tree.keys():
        if val in data:
            data.remove(val)
            return main(data, tree[val])
   

print(main([1959, 2003, 'MESON', 2012, 1994]),  # = 10
      main([1965, 2003, 'MESON', 2002, 1994]),  # = 6
      main([1962, 2003, 'X10', 2002, 1961]),  # = 2
      main([1965, 1990, 'X10', 2002, 1961]),  # = 3
      main([1965, 2003, 'MESON', 2012, 1994]))  # = 4)
