import wave, struct
print "We have started"
waveFile = wave.open('test_normal_16bit.wav', 'r')
length = waveFile.getnframes()
print "length of division is "
print length
for i in range(0,length):
    waveData = waveFile.readframes(1)
    data = struct.unpack("<h", waveData)
    print int(data[0])