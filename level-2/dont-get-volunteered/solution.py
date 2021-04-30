def solution(src, dest):
    x_len = 8
    y_len = 8
    knight_moves = {'nw': (-2 * y_len) - 1, 'ne': (-2 * y_len) + 1, 'en': (2 * 1) - y_len, 'es': (2 * 1) + y_len,
                    'se': (2 * y_len) + 1, 'sw': (2 * y_len) - 1, 'ws': (-2 * 1) + y_len, 'wn': (-2 * 1) - y_len}

    def is_valid_move(src, direction):
        if src - y_len < 0 and 'n' in direction:
            return False
        if src - (2 * y_len) < 0 and direction[0] == 'n':
            return False
        if src % x_len == 0 and 'w' in direction:
            return False
        if src % x_len == 1 and direction[0] == 'w':
            return False
        if src % x_len == x_len - 1 and 'e' in direction:
            return False
        if src % x_len == x_len - 2 and direction[0] == 'e':
            return False
        if src + y_len >= x_len * y_len and 's' in direction:
            return False
        if src + (2 * y_len) >= x_len * y_len and direction[0] == 's':
            return False
        return True


    next_squares = [src]
    distance = {src: 0}
    history = [src]

    while next_squares:
        this_square = next_squares[0]
        next_squares.pop(0)

        if this_square == dest:
            return distance[this_square]
        
        for direction in knight_moves:
            if is_valid_move(this_square, direction):
                next_square = this_square + knight_moves[direction]
                if not next_square in history:
                    history.append(next_square)
                    distance[next_square] = distance[this_square] + 1
                    next_squares.append(next_square)