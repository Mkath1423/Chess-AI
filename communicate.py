import random
import serial
import time
from Constants import Communications
from utilis import uci_to_num

def InitSerial():
    ser = serial.Serial('COM5', 9600, timeout=5)
    time.sleep(2)
    print("made connection")
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    return ser

def SendChanges(ser, changes):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write(f"sb {changes} ".encode("utf-8"))

def WarmUp(ser):
    for i in range(3):
        print(i)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.write("echo".encode("utf-8"))
        i -= 1 if ser.readline().decode().strip() == "echo" else 0
        time.sleep(0.1)
    print("warmup complete")

def GetNewBoardPosition(ser):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write("rb".encode("utf-8"))
    data = ser.readline().decode().strip()
    time.sleep(0.1)

    # decode into 2d array
    board = [[i for i in data[Communications.FILES.value*rank:(rank+1)*Communications.FILES.value]] for rank in range(Communications.RANKS.value)]
    return board

def GetNewBoardPosition(ser):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write("rb".encode("utf-8"))
    data = ser.readline().decode().strip()
    time.sleep(0.1)

    return set([i for i, char in enumerate(data) if char == "1"])

class Communicator:

    def __init__(self):
        self.red = set()
        self.blue = set()
        self.green = set()

        self.initialize_sets()

    def initialize_sets(self):
        self.green = {i*2 for i in range(32)}

    def remove_color(self, uci, color):
        if color == Communications.RED_VALUE.value:
            self.red.discard(uci_to_num(uci))

        elif color == Communications.GREEN_VALUE.value:
            self.green.discard(uci_to_num(uci))

        elif color == Communications.BLUE_VALUE.value:
            self.blue.discard(uci_to_num(uci))

    def remove_colors(self, ucis, color):
        for uci in ucis:
            self.remove_color(uci, color)

    def add_color(self, uci, color):
        if color == Communications.RED_VALUE.value:
            self.red.add(uci_to_num(uci))

        elif color == Communications.GREEN_VALUE.value:
            self.green.add(uci_to_num(uci))

        elif color == Communications.BLUE_VALUE.value:
            self.blue.add(uci_to_num(uci))

    def add_colors(self, ucis, color):
        for uci in ucis:
            self.add_color(uci, color)

    def sets_to_grid(self):
        r = self.red.copy()
        g = self.green.copy()
        b = self.blue.copy()

        colors = ['0' for _ in range(64)]

        g.difference_update(r)
        g.difference_update(b)

        b.difference_update(r)

        for led in r:
            colors[led] = Communications.RED_VALUE.value

        for led in g:
            colors[led] = Communications.GREEN_VALUE.value

        for led in b:
            colors[led] = Communications.BLUE_VALUE.value

        return colors

    def generate_color_string(self, colors):
        return ''.join(self.sets_to_grid())

def main():

    ser = InitSerial()
    WarmUp(ser)

    play = True
    while play:
        if input() == 'x':
            play = False
        else:
            print(GetNewBoardPosition(ser))

    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.close()


'''
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f'({self.r} {self.g} {self.b})'


grid = [[Color(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)) for _ in range(8)] for _ in range(8)]
print(grid)

def generate_color_strings(colors):
    red = ''
    green = ''
    blue = ''
    for row in colors:
        for pixel in row:
            red += f'{pixel.r},'
            green += f'{pixel.g},'
            blue += f'{pixel.b},'

        red += ','
        green += ','
        blue += ','

    return red[:-2], green[:-2], blue[:-2]


print(generate_color_strings(grid))

def split_to_array(str : str):
    arr = []

    line = ''
    for char in str:
        if char != ']':
            line += char

        else:
            arr = line.split(", ")

    return arr

'''

if __name__ == "__main__":
    main()
