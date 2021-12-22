with open("day3/input.txt") as f:
    lines = f.read().splitlines()


def oxygen_rate(lines):
    potential_lines = [l for l in lines]
    n = 0
    while len(potential_lines) > 1:
        bit_count = nth_bit_count(potential_lines, n)
        mcb = "1" if bit_count >= 0 else "0"
        potential_lines = [l for l in potential_lines if l[n] == mcb]
        n += 1
    return int(potential_lines[0], 2)


def co2_scrubber_rate(lines):
    potential_lines = [l for l in lines]
    n = 0
    while len(potential_lines) > 1:
        bit_count = nth_bit_count(potential_lines, n)
        lcb = "0" if bit_count >= 0 else "1"
        potential_lines = [l for l in potential_lines if l[n] == lcb]
        n += 1
    return int(potential_lines[0], 2)


def nth_bit_count(lines, n):
    count = 0
    for line in lines:
        bit = line[n]
        if bit == "1":
            count += 1
        else:
            count -= 1
    return count


print(co2_scrubber_rate(lines) * oxygen_rate(lines))
