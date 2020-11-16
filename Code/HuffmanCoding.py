global probabilities
probabilities = []


class HuffmanCodeNode:
    def __init__(self, p):
        self.p = p
        self.left = None
        self.right = None

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def main():
    symbols = input("Unesite ulazne simbole: ")
    length = len(symbols)

    frequencies = {}

    for symbol in symbols:
        if symbol in frequencies:
            frequencies[symbol] += 1
        else:
            frequencies[symbol] = 1

    frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    probabilities = [float("{:.3f}".format(frequency[1]/length))
                     for frequency in frequencies]
    probabilities = sorted(probabilities, reverse=True)

    huffmanCode = HuffmanCodeNode(probabilities)

    print(probabilities)


main()
