def main():
    # ตัวอย่างของกระดานหมากรุก 1 และ 2
    chess_board1 = ""\
R...
.K..
..P.
....
"""
    chess_board2 = ""\
R...
.K..
"""
    # เรียกฟังก์ชัน checkmate กับกระดานทั้งสอง
    print("Testing Board 1:")
    checkmate(chess_board1)  # ตรวจสอบกระดาน 1
    
    print("Testing Board 2:")
    checkmate(chess_board2)  # ตรวจสอบกระดาน 2

if __name__ == "__main__":
    main()