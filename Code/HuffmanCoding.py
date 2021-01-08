import math

global code
code = []


class HuffmanTree:
    """
    Huffmanovo kodiranje 
    ====================
    Kodira pojedinačne simbole kodnim riječima promjenjive duljine,
    ovisno o vjerojatnostima njihova pojavljivanja
    >Podatkovna struktura algoritma je binarno stablo

    """
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
    """
    Algoritam stvaranja koda:
        1. Pronađi dva simbola s najmanjim vjerojatnostima
        2. Jednom od njih dodijeli simbol "0", drugom "1"
        3. Kombiniraj ta dva simbola u jedan nadsimbol i zapiši ih kao dvije 
           grane binarnog stabla, a nadsimbol kao račvanje iznad njih
    """
    if type(node) is str:
        return {node: digit}

    (l, r) = node.children()
    huffman_code = {}
    huffman_code.update(HuffmanCode(l, True, digit + '0'))
    huffman_code.update(HuffmanCode(r, False, digit + '1'))

    return huffman_code


def CodeStatistics(frequencies, length, code_length):
    """
    Funkcija računa:
        1. Srednju duljinu kodne riječi L(X) koristeći formulu sume 
        vjerojatnosti pojavljivanja simbola i njihove duljine 
        kodne riječi.
        2. Entropiju koda, koju koristi za računanje učinkovitosti
        koda kao omjer H(X)/L(X)
    """
    probabilities = [float("{:.3f}".format(frequency[1]/length))
                     for frequency in frequencies]
    probabilities = sorted(probabilities, reverse=True)

    mean_length = sum(
        [a*b for a, b in zip(code_length, probabilities)])

    entropy = -1 *sum([a*math.log2(a) for a in probabilities])

    print("Srednja duljina kodne riječi: {:.3f}".format(mean_length))
    print("Efikasnost koda: {:.3f}".format(entropy/mean_length))


def main():
    # Učitaj simbole, te izračunaj duljinu simbola
    symbols = input("Unesite ulazne simbole: ")
    length = len(symbols)
    #Ako nije uneseno ništa, prekini izvođenje programa
    if length == 0:
        print("Neispravan unos podataka. Pokušajte ponovno!")
        return

    frequencies = {}

    for symbol in symbols:
        if symbol in frequencies:
            frequencies[symbol] += 1
        else:
            frequencies[symbol] = 1
    # Sortiraj frekvencije projavljivanja pojedinih simbola silazno
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
    code_length = []

    print(' Znak | Kôd     ')
    print('----------------')
    for (char, frequency) in frequencies:
        print(' %-4r |%6s' % (char, code[char]))
        code_length.append(len(code[char]))

    CodeStatistics(frequencies, length, code_length)


main()
