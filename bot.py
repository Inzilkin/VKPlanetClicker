import vk_advanced_api
import time
import random
import sys
from threading import *


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def start():
    generatestr = '"' + "tap" + str(useridout)+ '"'
    print("started")
    while True:
        print("Номер сообщения: ", utils.messages.send(peer_id=-181268215, random_id=random.randint(-100000, 1000000),
                                  message="🌍",
                                  payload=generatestr))
        time.sleep(2)


thread1 = Thread(target=start)
while 1:
    checker = input("auth/start/exit: ")
    if checker == 'auth':
        token = input("Enter you token ")
        captcha = input("Enter you captcha ")
        global utils
        api = vk_advanced_api.VKAPI(
            access_token=token,
            captcha_key=token,
            version=5.71,
            warn_level=1
        )
        utils = api.utils
        userid = utils.users.get()
        global useridnormal, useridout
        useridnormal = userid[0]['id']
        useridout = convert_base(useridnormal, to_base=8)
    if checker == 'start':
        thread1.start()
    if checker == 'exit':
        sys.exit()
