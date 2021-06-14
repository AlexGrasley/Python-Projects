import pyotp
import time


def otp_print():
    totp = pyotp.totp.TOTP('base32secret3232')
    while True:
        print(totp.now())
        time.sleep(30)


if __name__ == '__main__':
    otp_print()
