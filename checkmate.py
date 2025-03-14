def checkmate(chess_board):  
    rows = chess_board.splitlines()

    # ตรวจสอบความกว้างของกระดานให้เท่ากัน
    board_width = len(rows[0])
    index = 0
    while index < len(rows):
        if len(rows[index]) != board_width:
            print("Fail")
            return
        index += 1

    # หาตำแหน่งของราชา
    king_pos = next(((row_idx, line.index('K')) for row_idx, line in enumerate(rows) if 'K' in line), None)
    
    if not king_pos:
        print("Error")
        return

    king_x, king_y = king_pos  # ตำแหน่งของราชา

    # ฟังก์ชันตรวจสอบการโจมตี
    def is_under_attack(delta_x, delta_y, attackers):
        i, j = king_x + delta_x, king_y + delta_y
        while 0 <= i < len(rows) and 0 <= j < len(rows[0]):
            if rows[i][j] in attackers:
                return True
            if rows[i][j] != '.':
                break
            i, j = i + delta_x, j + delta_y
        return False

    # ตรวจสอบเบี้ย
    if king_x + 1 < len(rows) and ((king_y - 1 >= 0 and rows[king_x + 1][king_y - 1] == 'P') or (king_y + 1 < board_width and rows[king_x + 1][king_y + 1] == 'P')):
        print("Success")
        return

    # ตรวจสอบการโจมตีจากเรือ (R), ราชินี (Q) แนวตรงและแนวนอน
    if any(is_under_attack(dx, dy, {'R', 'Q'}) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        print("Success")
        return

    # ตรวจสอบการโจมตีจากบิชอป (B), ราชินี (Q) แนวทแยง
    if any(is_under_attack(dx, dy, {'B', 'Q'}) for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]):
        print("Success")
        return

    print("Fail")