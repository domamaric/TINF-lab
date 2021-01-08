class HuffmanTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def HuffmanCode(node, left=True, digit=''):
    if type(node) is str:
        return {node: digit}

    (l, r) = node.children()
    huffman_code = {}
    huffman_code.update(HuffmanCode(l, True, digit + '0'))
    huffman_code.update(HuffmanCode(r, False, digit + '1'))

    return huffman_code


def main():
    symbols = input("Unesite ulazne simbole: ")
    length = len(symbols)

    frequencies = {}

    for symbol in symbols:
        if symbol in frequencies:
            frequencies[symbol] += 1
        else:
            frequencies[symbol] = 1

    frequencies = sorted(frequencies.items(),
                         key=lambda x: x[1], reverse=True)

    nodes = frequencies
    while len(nodes) > 1:
        (key1, val1) = nodes[-1]
        (key2, val2) = nodes[-2]
        nodes = nodes[:-2]
        node = HuffmanTree(key1, key2)
        nodes.append((node, val1 + val2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    code = HuffmanCode(nodes[0][0])

    print(' Znak | Kod     ')
    print('----------------')
    for (char, frequency) in frequencies:
        print(' %-4r |%6s' % (char, code[char]))


main()
