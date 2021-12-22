function run()
    lines = read_lines("input.txt")
    instructions = parse_instructions(lines)

    l1 = execute_instructions(instructions)
    l2 = execute_instructions_with_aim(instructions)

    print("answer 1: ", l1.x * l1.y)
    print("answer 2: ", l2.x * l2.y)
end

function read_lines(file)
    lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

function parse_instructions(lines)
    instructions = {}
    for _, line in ipairs(lines) do
        tokens = split(line)
        instructions[#instructions + 1] = {
            direction = tokens[1],
            distance = tonumber(tokens[2])
        }
    end
    return instructions
end

function execute_instructions(instructions)
    location = {
        x = 0,
        y = 0
    }
    for _, instruction in ipairs(instructions) do
        if instruction.direction == "forward" then
            location.x = location.x + instruction.distance
        elseif instruction.direction == "up" then
            location.y = location.y - instruction.distance
        elseif instruction.direction == "down" then
            location.y = location.y + instruction.distance
        end
    end
    return location
end

function execute_instructions_with_aim(instructions)
    location = {
        x = 0,
        y = 0,
        aim = 0
    }
    for _, instruction in ipairs(instructions) do
        if instruction.direction == "forward" then
            location.x = location.x + instruction.distance
            location.y = location.y + instruction.distance * location.aim
        elseif instruction.direction == "up" then
            location.aim = location.aim - instruction.distance
        elseif instruction.direction == "down" then
            location.aim = location.aim + instruction.distance
        end
    end
    return location
end

function split(line)
    tokens = {}
    for token in string.gmatch(line, "%S+") do
        tokens[#tokens + 1] = token
    end
    return tokens
end
