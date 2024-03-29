"""
Author: Helios Staking 2021
"""

import requests
import time
from erdpy.accounts import Account
from erdpy.transactions import Transaction
from erdpy.proxy import ElrondProxy

sender = "erd1hpu42hjnx6hm8fjv48cff2qmmqwjh7w3wzf00v2m538w5x2jcnpqhgsggr"
wallet1 = "erd1wcpwsg6ysjrgea7zuhj3f8xzzyhdjv8t65me574h52f99he0tltsvq474v"
wallet2 = "erd1gjkd9lajx530ny84clqld7m6l869mz2hgdjlkpkqdtq40334ty4s625sd4"
wallet3 = "erd1l32u0h5nhcwrq2ts0rkhnanndwgt06jgd2z275zf8ey39lvxy6fsl6fmc2"
urlBalance = "https://devnet-api.elrond.com/address/" + sender + "/balance"
urlNonce = "https://devnet-api.elrond.com/address/" + sender + "/nonce"

account = Account(key_file="erdjsonexample.json",  # replace these place holders with your .json and password files
                  pass_file="password.txt")


def main():
    tx1()
    tx2()
    tx3()



def getbalance():
    # access JSOn content
    response = requests.get(urlBalance)
    data = response.json()
    # parse json and convert result to int
    x = int((data["data"]["balance"]))

    return x


def getNonce():
    # access JSOn content
    response = requests.get(urlNonce)
    data = response.json()
    # parse json and convert result to int
    x = int((data["data"]["nonce"]))

    return x


num = getbalance() * .2 / 100  # This will set the send amount at .2% of the current balance. Can be adjusted as needed.
sendAmount1 = str(f"{num:.0f}")
num2 = getbalance() * 41.7 / 100
sendAmount2 = str(f"{num2:.0f}")
num3 = getbalance() * 10 / 100
sendAmount3 = str(f"{num3:.0f}")


def tx1():
    tx1 = Transaction()
    tx1.nonce = getNonce()
    tx1.value = sendAmount1
    tx1.sender = sender
    tx1.receiver = wallet1
    tx1.gasPrice = 1000000000
    tx1.gasLimit = 50000
    tx1.data = ""
    tx1.chainID = "D"  # Currently set to the Devnet Chain
    tx1.version = 1
    tx1.sign(account)
    proxy1 = ElrondProxy("https://devnet-api.elrond.com")
    tx1.send(proxy1)
    print("Sent " + sendAmount1 + " to " + wallet1)


def tx2():
    time.sleep(60)

    tx2 = Transaction()
    tx2.nonce = getNonce()
    tx2.value = sendAmount2
    tx2.sender = sender
    tx2.receiver = wallet2
    tx2.gasPrice = 1000000000
    tx2.gasLimit = 50000
    tx2.data = ""
    tx2.chainID = "D"  # Currently set to the Devnet Chain
    tx2.version = 1
    tx2.sign(account)
    proxy1 = ElrondProxy("https://devnet-api.elrond.com")
    tx2.send(proxy1)
    print("Sent " + sendAmount2 + " to " + wallet2)


def tx3():
    time.sleep(60)

    tx3 = Transaction()
    tx3.nonce = getNonce()
    tx3.value = sendAmount3
    tx3.sender = sender
    tx3.receiver = wallet3
    tx3.gasPrice = 1000000000
    tx3.gasLimit = 50000
    tx3.data = ""
    tx3.chainID = "D"  # Currently set to the Devnet Chain
    tx3.version = 1
    tx3.sign(account)
    proxy1 = ElrondProxy("https://devnet-api.elrond.com")
    tx3.send(proxy1)
    print("Sent " + sendAmount3 + " to " + wallet3)


if __name__ == "__main__":
    main()
