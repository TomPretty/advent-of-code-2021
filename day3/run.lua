function run()
    lines = read_lines("input.txt")
    counts = bit_counts(lines)

    print("answer 1: ", gamma_rate(counts) * epsilon_rate(counts))
    print("answer 2: ", oxygen_rate(lines) * co2_scrubber_rate(lines))
end

function read_lines(file)
    lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

function bit_counts(lines)
    counts = {}
    for _, line in ipairs(lines) do
        for j = 1, #line do
            bit = line:sub(j, j)
            if n == "1" then
                counts[j] = (counts[j] and counts[j] or 0) + 1
            else
                counts[j] = (counts[j] and counts[j] or 0) - 1
            end
        end
    end
    return counts
end

function gamma_rate(counts)
    mcbs = {}
    for i, count in ipairs(counts) do
        mcbs[i] = count > 0 and "1" or "0"
    end

    return tonumber(table.concat(mcbs), 2)
end

function epsilon_rate(counts)
    lcbs = {}
    for i, count in ipairs(counts) do
        lcbs[i] = count < 0 and "1" or "0"
    end

    return tonumber(table.concat(lcbs), 2)
end

function oxygen_rate(lines)
    potential_lines = {table.unpack(lines)}
    n = 1
    while #potential_lines > 1 do
        mcb = nth_bit_count(lines, n) > 1 and "1" or "0"
        potential_lines = filter(potential_lines, function(line)
            return line:sub(n, n) == mcb
        end)
        n = n + 1
    end
    return tonumber(potential_lines[1], 2)
end

function co2_scrubber_rate(lines)
    potential_lines = {table.unpack(lines)}
    n = 1
    while #potential_lines > 1 do
        lcb = nth_bit_count(lines, n) >= 0 and "0" or "1"
        print("n: ", n)
        print("lcb: ", lcb)
        potential_lines = filter(potential_lines, function(line)
            return line:sub(n, n) == lcb
        end)
        print(#potential_lines)
        print(potential_lines[1])
        print(potential_lines[1]:sub(n, n))
        print(potential_lines[2])
        print(potential_lines[2]:sub(n, n))

        n = n + 1
    end
    return tonumber(potential_lines[1], 2)
end

function nth_bit_count(lines, n)
    count = 0
    for _, line in ipairs(lines) do
        bit = line:sub(n, n)
        if bit == "1" then
            count = count + 1
        else
            count = count - 1
        end
    end
    return count
end

function filter(lines, predicate)
    filtered = {}
    for _, line in ipairs(potential_lines) do
        if (predicate(line)) then
            filtered[#filtered + 1] = line
        end
    end
    return filtered
end
