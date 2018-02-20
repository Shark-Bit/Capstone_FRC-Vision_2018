import smbus2
import numpy as np
import time
import random

rpi_bus = smbus2.SMBus(1)
rpi_wrapper = smbus2.SMBusWrapper(1)



slave_add = 0x04

def send_w_wrapper(number):
    with smbus2.SMBusWrapper(1) as bus:
        bus.write_i2c_block_data(slave_add, 0, number)

def send_regular(number):
    rpi_bus.write_i2c_block_data(slave_add, 0, number)

def main():

    list_1 = []

    for x in range(0, 10):
        num = random.randint(1, 9999)
        list_1.append(num)
    length = len(list_1)
    for y in range(0, length):
        number = list_1[y]
        print(number)
        send_w_wrapper(number)
        time.sleep(.2)


if __name__ == '__main__':
    main()