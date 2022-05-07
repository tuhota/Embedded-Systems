import time
import smbus

#define bus
bus = smbus.SMBus(1)
#for Lux data read from sensor
read_in = 0
#subjective luminosity
sub_lum = ""


#convert raw bytes to decimal data
def lux_to_decimal(data):
	return ((data[1] + (256 * data[0])) / 1.2)

#read Lux from sensor
def get_lux():
	#read block of byte data from bh1750 i2c address at low res
	data = bus.read_i2c_block_data(0x23, 0x23)
	return lux_to_decimal(data)

#loops until interrupt
while True:
	#get sensor data in integer form
	read_in = int(get_lux())
	
	#determines subjective luminosity
	if read_in < 10:
		sub_lum = "Too dark"
	elif read_in < 20:
		sub_lum = "Dark"
	elif read_in < 30:
		sub_lum = "Medium"
	elif read_in < 40:
		sub_lum = "Bright"
	else:
		sub_lum = "Too bright"
	
	#converts data back to string
	read_in = str(read_in)
	
	#outputs Lux and Subjective luminosity to serial monitor every second
	print("Lux: " + read_in + ": " + sub_lum)
	time.sleep(0.5)
