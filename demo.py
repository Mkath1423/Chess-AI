from communicate import *
from Constants import Communications

def NumToPosition(num):

    return ()

def main():
    ser = InitSerial()
    WarmUp(ser)
    current_board = set()
    play = True
    while play:
        print(current_board)
        if input() == 'x':
            play = False

        else:
            new_board = GetNewBoardPosition(ser)
            print(new_board)
            changes = ""
            for i in current_board.difference(new_board):
                changes += f'{i % Communications.FILES.value}{i // Communications.FILES.value}0'

            for i in new_board.difference(current_board):
                changes += f'{i % Communications.FILES.value}{i // Communications.FILES.value}2'

            print(changes)
            if changes != '':
                SendChanges(ser, changes)


            current_board = new_board

        time.sleep(0.1)


if __name__ == "__main__":
    main()
