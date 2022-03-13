import serial

Mind_wave = serial.Serial("Com3" , 57600)
data = Mind_wave.readline()
print(data)