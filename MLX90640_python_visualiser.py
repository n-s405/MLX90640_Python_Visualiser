import serial
import numpy as np
# import cv2 





def main():  
    # cv2.namedWindow('output', cv2.WINDOW_NORMAL)  
    ser = serial.Serial('/dev/cu.usbmodem42045401', 115200)

    while True:
        frame = ser.readline().decode('utf-8')
        final = frame.split(',')[0:768]
        results = list(map(float, final))
        newarr = np.asarray(results, dtype = float) 

        two_d = np.reshape(newarr, (32, 24))
        print(two_d)
        # plt.imshow(two_d, cmap="gray")
        # plt.show()
        # # cv2.imshow('output',two_d*5)
        # # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break


if __name__ == "__main__":
    main()