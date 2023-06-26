from encoder import ImageBufferedMessage

rfilepath = "/Users/tbdamiani/Documents/CMU/Sophomore/lab/rf_testing/img/reference_image.jpeg"
wfilepath = "/Users/tbdamiani/Documents/CMU/Sophomore/lab/rf_testing/img/back_to_fsk_write.jpeg"

encoder = ImageBufferedMessage(rfilepath, 237)

packeting = True

while packeting:
    packet = encoder.Packet()
    if packet[0] == 0xEF:
        try:
            with open(wfilepath, "wb") as fd:
                fd.write(packet[1:])
            encoder.ack()
        except Exception as e:
            print(f"could not start create image file: {e}")
    else:
        try:
            with open(wfilepath, "ab") as fd:
                fd.write(packet[1:])
            encoder.ack()
        except Exception as e:
            print(f"could not write to iamge file: {e}")
    if packet[0] == 0xED:
        packeting = False

    print(len(packet))
    print(packet)
    print("-----------------------")
    # print(packet[0])

    # if packet[0] == 0xED:
    #     packeting = False


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
