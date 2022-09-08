def main():
    import os
    import sys
    from requests import get
    from base64 import urlsafe_b64encode, urlsafe_b64decode
    from time import sleep
    from hashlib import pbkdf2_hmac
    from getpass import getpass
    from cryptography.fernet import Fernet, InvalidToken
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    currentversion = "1.0.0"

    try:
        version = get("https://raw.githubusercontent.com/tilas01/sdcrypt/main/version")
        if str(version) != "<Response [200]>":
            print("Could not reach update server.\nYou can manually check for updates at https://www.github.com/tilas01/sdcrypt.\n")
        elif version.text != currentversion:
            print(f"An update is avaliable at https://www.github.com/tilas01/sdcrypt\nYour Version: {currentversion}\nNew Version: {version.text}\n")
    except Exception as error:
        print("Could not reach update server.\nYou can manually check for updates at https://www.github.com/tilas01/sdcrypt.\n")

    systemfilenames = ["System Volume Information", "$RECYCLE.BIN", "desktop.ini"]

    def leave():
        while True:
            confirm = input("Are you sure [y/n]? ")
            if confirm.lower() == "y":
                print("Quitting...")
                sys.exit()
            elif confirm.lower() == "n":
                break

    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def encrypt(dir):
        try:
            if os.path.basename(dir) in systemfilenames:
                filename = os.path.basename(dir)
                print(f"Ignoring {filename} as it is a system file.")
            elif os.path.isdir(dir):
                 oldname = os.path.basename(dir)
                 newname = f.encrypt(oldname.encode())
                 os.chdir(os.path.dirname(dir))
                 os.rename(oldname, newname)
                 print(f"Encrypted {oldname}")
            elif os.path.isfile(dir):
                oldname = os.path.basename(dir)
                newname = f.encrypt(oldname.encode())
                os.chdir(os.path.dirname(dir))
                os.rename(oldname, newname)
                with open(newname, "rb") as file:
                    data = file.read()
                data = f.encrypt(data)
                with open(newname, "wb") as file:
                    file.write(data)
                print(f"Encrypted {oldname}")
        except OSError as error:
            print(f"\nOSError occured while encrypting {oldname}.\n{error}\n")
        except Exception as error:
            print(f"\nUnknown error occured while encrypting {oldname}.\n{error}\n")

    def decrypt(dir):
        try:
            if os.path.basename(dir) in systemfilenames:
                filename = os.path.basename(dir)
                print(f"Ignoring {filename} as it is a system file.")
            elif os.path.isdir(dir):
                oldname = os.path.basename(dir)
                newname = f.decrypt(oldname.encode())
                os.chdir(os.path.dirname(dir))
                os.rename(oldname, newname)
                print("Decrypted " + newname.decode())
            elif os.path.isfile(dir):
                oldname = os.path.basename(dir)
                newname = f.decrypt(oldname.encode())
                os.chdir(os.path.dirname(dir))
                os.rename(oldname, newname)
                with open(newname, "rb") as file:
                    data = file.read()
                data = f.decrypt(data)
                with open(newname, "wb") as file:
                    file.write(data)
                print("Decrypted " + newname.decode())
        except InvalidToken:
            print(f"{oldname} is not encrypted.")
        except OSError as error:
            print(f"\nOSError occured while decrypting {oldname}.\n{error}\n")
        except Exception as error:
            print(f"\nUnknown error occured while decrypting {oldname}.\n{error}\n")

    if not os.path.isdir("config"):
        print("Creating config...")
        try:
            os.mkdir("config")
        except OSError:
            print('Could not create "config"')
            leave()

    if not os.path.isfile("config/salt"):
        salt = os.urandom(32)
        b64salt = urlsafe_b64encode(salt).decode()
        print("Writing salt...\n")
        try:
            with open("config/salt", "w") as file:
                file.write(b64salt)
        except OSError:
            print('Could not open "salt"')
            leave()

    try:
        with open("config/salt", "r") as file:
            salt = file.read()
            salt = urlsafe_b64decode(salt)
    except OSError:
        print('Could not open "salt"')
        leave()

    if not os.path.isfile("config/hash"):
        print("Please enter the password you would like to encrypt/decrypt your files with.")
        print("Keep this password safe, if it is lost all your data WILL be unrecoverable if in an encrypted state.\n")
        while True:
            firstpass = getpass("Master Password: ")
            secondpass = getpass("Confirm Master Password: ")
            if firstpass != secondpass:
                print("Passwords do not match.")
            else:
                del secondpass
                firstpass = pbkdf2_hmac('sha256', firstpass.encode('utf-8'), salt, 100000)
                try:
                    with open("config/hash", "wb") as file:
                        file.write(firstpass)
                except OSError:
                    print('Could not open "hash"')
                    leave()
                print()
                break

    try:
        with open("config/hash", "rb") as file:
            checkhash = file.read()
    except OSError:
        print('Could not open "hash"')
        leave()

    if 'b64salt' in locals():
        print('Your salt is "' + b64salt + '". Keep it safe.')
        print("If you lose your salt all data encrypted with it WILL be unrecoverable.\n")
    print("Welcome to sdcrypt!")
    if version.text == currentversion:
        print("You are on the latest version.")
    print("This program will securely encrypt/decrypt all files and folders in a specified location recursively.\nIt can also encrypt single files.\n")
    print("Remember:")
    print("Do not rename any encrypted files or folders.")
    print("Do not encrypt a folder or drive more than once.")
    print("Do not modify files, folders or their contents while encrypted")
    print("Use this program at your own risk. I am not responsbile for your data.")
    print("Always keep a backup.\n")
    while True:
        key = getpass("Master Password: ")
        keyhash = pbkdf2_hmac('sha256', key.encode('utf-8'), salt, 100000)
        if keyhash == checkhash:
            print("Correct Password!\n")
            break
        else:
            print("Incorrect Password.")
    key = key.encode()
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(key))
    f = Fernet(key)

    while True:
        a = input("Choose a command: [(e)ncrypt / (d)ecrypt / (c)lear / (q)uit]: ")

        if a == "e":
            print("\nPlease enter the full path of the file/folder you want to encrypt.")
            print("e.g. /path/to/file/or/folder")
            filepath = input("Response: ")
            if os.path.isdir(filepath):
                for dirpath, dirname, filename in os.walk(filepath):
                    for x in filename:
                        path = os.path.join(dirpath, x)
                        encrypt(path)
                for dirpath, dirname, filename in os.walk(filepath):
                    for x in dirname:
                        path = os.path.join(dirpath, x)
                        encrypt(path)
                print("Encryption complete!\n")
            elif os.path.isfile(filepath):
                encrypt(filepath)
                print("Encryption complete!\n")
            else:
                print("Invalid Encryption Request\n")

        elif a == "d":
            print("\nPlease enter the full path of the file/folder you want to decrypt.")
            print("e.g. /path/to/file/or/folder")
            filepath = input("Response: ")
            if os.path.isdir(filepath):
                for dirpath, dirname, filename in os.walk(filepath):
                    for x in filename:
                        path = os.path.join(dirpath, x)
                        decrypt(path)
                for dirpath, dirname, filename in os.walk(filepath):
                    for x in dirname:
                        path = os.path.join(dirpath, x)
                        decrypt(path)
                print("Decryption complete!\n")
            elif os.path.isfile(filepath):
                decrypt(filepath)
                print("Decryption complete!\n")
            else:
                print("Invalid Decryption Request\n")

        elif a == "c":
            clear()

        elif a == "q":
            leave()

if __name__ == '__main__':
    main()