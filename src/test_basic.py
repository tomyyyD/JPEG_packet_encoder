from encoder import ImageBufferedMessage

filepath = "/Users/tbdamiani/Documents/CMU/Sophomore/lab/rf_testing/img/back_to_fsk.jpeg"
wfilepath = "/Users/tbdamiani/Documents/CMU/Sophomore/lab/rf_testing/img/back_to_fsk_write.jpeg"

encoder = ImageBufferedMessage(filepath, 237)

packeting = True

while packeting:
    packet = encoder.Packet()
    print(len(packet))
    print(packet)
    print(packet[0])

    if packet[0] == 0xED:
        packeting = False
    else:
        encoder.ack()


# packet = encoder.Packet()
# print(len(packet))
# print(packet)
# print(packet[0])
# encoder.ack()

# packet = encoder.Packet()
# print(len(packet))
# print(packet)
# encoder.ack()

# packet = encoder.Packet()
# print(len(packet))
# print(packet)

# packet = encoder.Packet()
# print(len(packet))
# print(packet)
# encoder.ack()

# packet = encoder.Packet()
# print(len(packet))
# print(packet)
# encoder.ack()

# packet = encoder.Packet()
# print(len(packet))
# print(packet)
