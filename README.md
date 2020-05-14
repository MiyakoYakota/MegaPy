# MegaPy

## Intro
This is a proxyless Python mega.nz checker designed to be run in the cloud. You can see it running in action [here](http://accounts.miyako.rocks/hits/mega.nz.txt).

## Setup
To set up this program run the following to install required libraries:

```pip3 install -r requirements.txt```

## Running
To run this program, put your combos into a file called ``combo.txt`` and run the program with

```python3 MegaChecker.py```

## Warning
Because of Mega's login process, this uses a *lot* of processing power. It needs to generate an AES encrypted hash on the client side before sending it to the authserver to login. I reccomend that you run this in a cloud VPS and come back later.
