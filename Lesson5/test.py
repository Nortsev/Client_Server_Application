import logging
import os

import random
import sys

Meaning = [True, False, None]
_format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s")
crit_hand = logging.FileHandler(filename='logs/app.logs')
crit_hand.setLevel(logging.DEBUG)
crit_hand.setFormatter(_format)
log = logging.getLogger('basic')
log.addHandler(crit_hand)

def test_log(operation):
    if operation == True:
        print("Значение равно True")
        log.info(f"Log:Значение равно True")
    elif operation == False:
        print("Значение равно False")
        log.warning(f"Log:Значение равно False")
    else:
        print("Не известное занечение")
        log.critical(f"Log:Не известное занечение")

print(__file__)
if __name__ == '__main__':
    test_log(random.choice(Meaning))
    print(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

