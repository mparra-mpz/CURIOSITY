import bluetooth

if __name__ == "__main__":

    target_name = "CURIOSITY"
    target_address = None

    nearby_devices = bluetooth.discover_devices()

    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
            target_address = bdaddr
            break

    bd_addr = target_address
    port = 1

    print "Creating the bluetooth socket with protocol RFCOMM."
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    print "Trying to connect to the bluetooth..."
    sock.connect((bd_addr, port))
    print "Bluetooth connected."

    while True:
        print "Type 1 to turn on the led, 0 to turn off and x to exit."
        data = str(raw_input())
        if data == "x": break
        print data + " send to bluetooth."
        sock.send(data)

    sock.close()