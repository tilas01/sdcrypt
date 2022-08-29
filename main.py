def main():
    import os
    import sys
    from base64 import urlsafe_b64encode, urlsafe_b64decode
    from time import sleep
    from hashlib import pbkdf2_hmac
    from getpass import getpass
    from cryptography.fernet import Fernet, InvalidToken
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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
            if os.path.isdir(dir):
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
        except OSError:
            print(f"OSError occured while encrypting {oldname}.")
        except:
            print(f"Unknown error occured while encrypting {oldname}.")

    def decrypt(dir):
        try:
            if os.path.isdir(dir):
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
            raise StopIteration
        except OSError:
            print(f"OSError occured while decrypting {oldname}.")
        except:
            print(f"Unknown error occured while decrypting {oldname}.")

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
    print("Welcome to sdcrypt!\nThis program will securely encrypt/decrypt all files and folders in a specified location recursively.\n")
    print("Remember:")
    print("Do not rename any encrypted files or folders.")
    print("Do not encrypt a folder or drive more than once.")
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
            print("\nPlease enter the full path of the folder/disk you want to recursively encrypt.")
            print("e.g. /path/to/folder/or/disk")
            filepath = input("Response: ")
            if not os.path.isdir(filepath):
                print("Invalid Encryption Request\n")
            else:
                for dirpath, dirname, filename in os.walk(filepath):
                    for x in filename:
                        path = os.path.join(dirpath, x)
                        encrypt(path)
                for dirpath, dirname, filename in os.walk(filepath):
                    for x in dirname:
                        path = os.path.join(dirpath, x)
                        encrypt(path)
                print("Encryption complete!\n")

        elif a == "d":
            print("\nPlease enter the full path of the folder/disk you want to recursively decrypt.")
            print("e.g. /path/to/folder/or/disk")
            filepath = input("Response: ")
            if not os.path.isdir(filepath):
                print("Invalid Decryption Request\n")
            else:
                try:
                    for dirpath, dirname, filename in os.walk(filepath):
                        for x in filename:
                            path = os.path.join(dirpath, x)
                            decrypt(path)
                    for dirpath, dirname, filename in os.walk(filepath):
                        for x in dirname:
                            path = os.path.join(dirpath, x)
                            decrypt(path)
                    print("Decryption complete!\n")
                except StopIteration:
                    print("File(s) are not encrypted.\n")

        elif a == "c":
            clear()

        elif a == "q":
            leave()

if __name__ == '__main__':
    main()