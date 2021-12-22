require 'pl'

stringx.import()
seq.import()

BOARD_SIZE = 5

function run()
    local boards, all_numbers = read_input("input.txt")
    local numbers = {
        [all_numbers[1]] = true,
        [all_numbers[2]] = true,
        [all_numbers[3]] = true,
        [all_numbers[4]] = true
    }
    local n = 5

    local winning_board = nil
    while winning_board == nil do
        numbers[all_numbers[n]] = true
        n = n + 1

        for _, board in ipairs(boards) do
            if is_winning_board(board, numbers) then
                winning_board = board
                break
            end

        end
    end

    print_board(winning_board)
end

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

    local all_numbers = read_numbers(table.remove(lines), ",")

    return boards, all_numbers
end

function read_lines(file)
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

function read_numbers(line, pattern)
    return seq.copy(seq.map(tonumber, line:split(pattern or " ")))
end

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

function print_board(board)
    for i = 1, #board do
        for j = 1, #board[i] do
            io.write(string.format("%2i ", board[i][j]))
        end
        io.write("\n")
    end
    io.write("\n")
end
