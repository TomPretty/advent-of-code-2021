from collections import Counter

CHAIN = "SNVVKOBFKOPBFFFCPBSF"

INSERTIONS_RAW = [
    "HH -> P",
    "CH -> P",
    "HK -> N",
    "OS -> N",
    "HV -> S",
    "VC -> C",
    "VO -> K",
    "OC -> C",
    "FB -> S",
    "NP -> S",
    "OK -> H",
    "OO -> N",
    "PP -> B",
    "VK -> B",
    "BV -> N",
    "PN -> K",
    "HC -> C",
    "NS -> K",
    "BO -> C",
    "BN -> O",
    "SP -> H",
    "FK -> K",
    "KF -> N",
    "VP -> H",
    "NO -> N",
    "OH -> N",
    "CC -> O",
    "PK -> P",
    "BF -> K",
    "CP -> N",
    "SH -> V",
    "VS -> P",
    "BH -> B",
    "KS -> H",
    "HB -> K",
    "BK -> S",
    "KV -> C",
    "SF -> B",
    "BB -> O",
    "PC -> S",
    "HN -> S",
    "FP -> S",
    "PH -> C",
    "OB -> O",
    "FH -> K",
    "CS -> P",
    "OF -> N",
    "FF -> V",
    "PV -> B",
    "PF -> C",
    "FC -> S",
    "KC -> O",
    "PS -> V",
    "CO -> F",
    "CK -> O",
    "KH -> H",
    "OP -> O",
    "SK -> S",
    "VB -> P",
    "FN -> H",
    "FS -> P",
    "FV -> N",
    "HP -> O",
    "SB -> N",
    "VN -> V",
    "KK -> P",
    "KO -> V",
    "BC -> B",
    "FO -> H",
    "OV -> H",
    "CF -> H",
    "HF -> K",
    "SS -> V",
    "SC -> N",
    "CB -> B",
    "SV -> C",
    "SN -> P",
    "PB -> B",
    "KP -> S",
    "PO -> B",
    "CN -> F",
    "ON -> B",
    "CV -> S",
    "HO -> O",
    "NF -> F",
    "VH -> P",
    "NN -> S",
    "HS -> S",
    "NV -> V",
    "NH -> C",
    "NB -> B",
    "SO -> K",
    "NC -> C",
    "VF -> B",
    "BS -> V",
    "VV -> N",
    "BP -> P",
    "KN -> C",
    "NK -> O",
    "KB -> F",
]


def parse_insertions(raw):
    insertions = {}
    for line in raw:
        pair, inserted = line.split(" -> ")
        insertions[pair] = inserted
    return insertions


def steps(chain, insertions, num_steps):
    @cached
    def after_steps(pair, steps):
        if steps < 1 or not pair in insertions:
            return Counter(pair)

        p1 = pair[0] + insertions[pair]
        p2 = insertions[pair] + pair[1]

        return (
            after_steps(p1, steps - 1)
            + after_steps(p2, steps - 1)
            - Counter(insertions[pair])
        )

    counts = [after_steps(f"{a}{b}", num_steps) for a, b in zip(chain, chain[1:])]
    total = Counter()
    for count in counts:
        total += count
    total -= Counter(chain[1:-1])

    return total


def cached(f):
    cache = {}

    def wrapped(*args):
        if not args in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapped


if __name__ == "__main__":
    insertions = parse_insertions(INSERTIONS_RAW)
    counter = steps(CHAIN, insertions, 40)
    ordered = counter.most_common()

    _, most = ordered[0]
    _, least = ordered[-1]

    print(f"ans: {most - least}")
