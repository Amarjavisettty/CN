def bitstuff(payload):
    count = 0
    stuffed = ''
    for bit in payload:
        if bit == '1':
            count += 1
            stuffed += bit
            if count == 5:   
                stuffed += '0'
                count = 0
        else:
            stuffed += bit
            count = 0
    return stuffed
def bitdestuff(stuffed):
    count = 0
    destuffed = ''
    i = 0
    while i < len(stuffed):
        bit = stuffed[i]
        destuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                i += 1
                count = 0
        else:
            count = 0
        i += 1
    return destuffed
msg = input('Enter message (bits only, e.g. 110111111011): ')

print('Original message:', msg)
stuffed_msg = bitstuff(msg)
print('Message after bit stuffing:', stuffed_msg)
destuffed_msg = bitdestuff(stuffed_msg)
print('Message after bit destuffing:', destuffed_msg)
output
Enter message (bits only, e.g. 110111111011): 011011111111110010
Original message: 011011111111110010
Message after bit stuffing: 01101111101111100010
Message after bit destuffing: 011011111111110010
