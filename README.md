# sdcrypt

An easy-to-use python application to encrypt/decrypt your files or folders.

Contents
========

 * [Disclaimer](#disclaimer)
 * [Why?](#why)
 * [Requirements](#requirements)
 * [Installation](#installation)
 * [Use](#use)
 * [Features](#features)
 * [Note](#note)
 * [To-Do](#to-do)
 * [License](#license)

### Disclaimer

---

Use this program at your own risk. I am not responsible your data. Always keep a backup

### Why?

---

I wanted to encrypt my SD cards so I modified my [`pylocker`](https://www.github.com/tilas01/pylocker) project to support recursive encryption/decryption

### Requirements

---

To use this program you will require [`python`](https://www.python.org/) 3.9 or higher

### Installation

ℹ️ If you have previously used PyLocker and are updating after installing by running the below please review the [Use](#use) section to update from your current config, if this is your first time using sdcrypt and have never used PyLocker you can safely ignore this message. ℹ️

Install with [`git`](https://git-scm.com/) ([Python3](https://www.python.org/downloads) required)

```
$ git clone https://github.com/tilas0/sdcrypt.git
$ cd sdcrypt
$ pip3 install -r requirements.txt
$ python3 main.py
```

Install without git ([Python3](https://www.python.org/downloads) required)

How to install Python3 on Linux with the apt package manager:

```
$ sudo apt update
$ sudo apt install python3
```

How to install Python3 on any other OS:

Visit the [Python3](https://www.python.org/downloads) official website, go to downloads and install the version of Python3 that matches your Operating System

You may then follow the above stepts under "Install with git" excluding the git clone page and instead by downloading the repo directly from GitHub and extracting the archive then simply cd into it and install using pip3 with python3. These installation steps can be followed to install sdcrypt on any operating system python3 supports (Windows, MacOS, Linux, etc) making sdcrypt highly cross-compatible with many operating systems.



### Use

---

#### Disclaimer: Dont ignore instructions when they guide you to ensure your files are encrypted as it can lead to irrecoverable data loss.

#### Update from DEPRECATED PyLocker:

Clone the git repo and move your config folder into it. Then replace the old folder with the new one.
or
Run the following commands with [`git`](https://git-scm.com/) installed in your [`sdcrypt`](https://www.github.com/tilas01/sdcrypt) directory:

```
#Updates repo to latest version of sdcrypt.
$ git pull
#Installs needed requirements. If you're migrating from pylocker, you already have these installed, but its always a good idea to update your requirements as the cryptography module (only requirement) may have bug fixes and improvements in newer versions which is all the below installs to allow the program to function.
$ pip3 install -r requirements.txt
```

This will check the git repo for updates and install any new requirements if possible.

#### Reset your password:

Ensure all files are in a decrypted state. Then delete the "hash" file located in the config directory.

#### Reset your salt:

Ensure all files are in a decrypted state. Then delete the "hash" and "salt" files located in the config directory. This will also reset your password.

#### Use a backed up salt:

The salt can be from sdcrypt or PyLocker if you're migrating, the programs are both compatible as sdcrypt is just a more advanced version of pylocker.

Create a "config" directory in the same location as pylocker. Then in that config directory create an extensionless file named "salt" and put the salt into that file.

### Features

---

- Cryptographically secure encryption/decryption, password hashing and salt generation
- Base64 salt so it can be written down or stored easily
- Any file or folder can be encrypted
- Recursive encryption
- File and folder name encryption/decryption
- Password input is not displayed
- Cross-platform support

### License

---

Licensed under the [MIT License](LICENSE)
