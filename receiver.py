#!/usr/bin/env python
import socket
import numpy as np
import cv2

host = "000.000.0.0"
#IP address of computer that is broadcasting
port = 10000
buf = 1024
addr = (host, port)
fName = 'img.jpg'
timeOut = 0.05


def foo():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))
        data, address = s.recvfrom(buf)
        data = data.decode()
        f = open(data, 'wb')

        data, address = s.recvfrom(buf)
        try:
            while (data):
                f.write(data)
                s.settimeout(timeOut)
                data, address = s.recvfrom(buf)
        except:
            f.close()
            s.close()
        image = cv2.imread(fName)
        cv2.imshow('recv', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    foo()
    cv2.destroyAllWindows()