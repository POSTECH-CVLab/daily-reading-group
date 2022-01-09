import paho.mqtt.client as mqtt
import pdb
from ast import literal_eval
import cv2
import numpy as np
import base64

import time

cnt = 0
flag = False
st = 0.001

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    global cnt
    global flag
    global st

    json_str = msg.payload.decode("utf-8")

    try:
        # pdb.set_trace()

        if json_str == "null":
            print(json_str)

        else:
            jso_dict = literal_eval(json_str)
            cur_time = list(json_dict.keys())[0]

            for cam_id in list(json_dict[cur_time].keys()):
                encoding_img = json_dict[cur_time][cam_id]['image']
                jpg_original = base64.b64decode(encoding_img)
                jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
                img = cv2.imdecode(jpg_as_np, flags=cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                cv2.imshow('img_{}'.format(cam_id), img)

            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()

            if not flag:
                st = time.time()
                flag = True
            cnt += 1
            print("received frames: ", cnt, "\tfps: ", cnt/(time.time()-st))

    except:
        print("on message error")


def main():

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    # f = open("../broker_ip.txt", 'r')
    # line = f.readline()
    # broker = line
    # f.close()
    broker = "164.125.190.131"
    client.connect(broker, 1883)

    client.subscribe('json',0)
    client.loop_forever()


if __name__ == "__main__":
    main()
