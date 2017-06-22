import bitprim
import os
import signal
import sys
import time

# ------------------------------------------------------
# 
# ------------------------------------------------------
def signal_handler(signal, frame):
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)
    print('You pressed Ctrl-C')
    sys.exit(0)

def history_fetch_handler(e, l): 
    # print('history_fetch_handler: {0:d}'.format(e))
    # print(l)
    # if (e == 0):
    #     print('history_fetch_handler: {0:d}'.format(e))

    count = l.count()
    print('history_fetch_handler count: {0:d}'.format(count))

    for n in range(count):
        h = l.nth(n)
        # print(h)
        print(h.point_kind())
        print(h.height())
        print(h.value_or_spend())

        # print(h.point())
        print(h.point().hash())
        print(h.point().is_valid())
        print(h.point().index())
        print(h.point().get_checksum())



def last_height_fetch_handler(e, h): 
    if (e == 0):
        print('Last Height is: {0:d}'.format(h))

# ------------------------------------------------------
# Main Real
# ------------------------------------------------------
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as e:
# with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as e:
    # res = e.initchain()
    res = e.run()
    # print(res)
    
    time.sleep(3)

    while True:
        e.fetch_last_height(last_height_fetch_handler)
        e.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
        # e.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Satoshi
        time.sleep(10)

    # print('Press Ctrl-C')
    # signal.pause()

# bx fetch-history [-h] [--config VALUE] [--format VALUE] [PAYMENT_ADDRESS]