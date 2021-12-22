require 'pl'
-- function print_board(board)
--     for i = 1, #board do
--         for j = 1, #board[i] do
--             io.write(string.format("%2i ", board[i][j]))
--         end
--         io.write("\n")
--     end
--     io.write("\n")
-- end
-- print_board(BOARD)
function read_input(file)
    local lines = read_lines(file)
    local boards = {}
    while #lines > 6 do
        -- first we read the 5 board lines
        local l5 = read_numbers(table.remove(lines))
        local l4 = read_numbers(table.remove(lines))
        local l3 = read_numbers(table.remove(lines))
        local l2 = read_numbers(table.remove(lines))
        local l1 = read_numbers(table.remove(lines))

        -- add the new board
        boards[#boards + 1] = {l1, l2, l3, l4, l5}

        -- then we drop the empty line
        table.remove(lines)
    end

    print("num lines: ", #lines)
    print(lines[1])

    local all_numbers = read_numbers(table.remove(lines), ",")

    return boards, all_numbers
end

function read_lines(file)
    lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

function read_numbers(line, pattern)
    return map(split(line, pattern), tonumber)
end

function split(line, pattern)
    pattern = pattern or "%S+"

    local tokens = {}
    for token in string.gmatch(line, "%S+") do
        tokens[#tokens + 1] = token
    end
    return tokens
end

function map(arr, fn)
    local res = {}
    for _, x in ipairs(arr) do
        res[#res + 1] = fn(x)
    end
    return res
end

BOARD_SIZE = 5
BOARD = {{30, 46, 94, 20, 2}, {53, 67, 69, 75, 65}, {27, 24, 85, 28, 60}, {57, 58, 42, 36, 78}, {35, 98, 87, 91, 93}}
NUMBERS = {
    [30] = true,
    [53] = true,
    [27] = true,
    [57] = true,
    [35] = true
}

function is_winning_board(board, numbers)
    function is_winning_row(row)
        for col = 1, BOARD_SIZE do
            if not numbers[board[row][col]] then
                return false
            end
        end
        return true
    end

    function is_winning_col(col)
        for row = 1, BOARD_SIZE do
            if not numbers[board[row][col]] then
                return false
            end
        end
        return true
    end

    for row = 1, BOARD_SIZE do
        if is_winning_row(row) then
            return true
        end
    end

    for col = 1, BOARD_SIZE do
        if is_winning_col(col) then
            return true
        end
    end

    return false
end

print(is_winning_board(BOARD, NUMBERS))
