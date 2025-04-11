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

I developed this in 2022 it is now 2025 I would fully test the program is working before using it to reliabily store data especially if you are using the newest python build as it has only been fully tested to be working and developed using Python 3.9 meaning I can only guarentee its reliability and functionality with this version as I do not control changes to the Python project and therefore if a major syntax update was to come out it could theoretically break the program and possibly cause data loss. I mainly made this app for myself and so would like to highlight this point for anyone intending to use it. If the app code ever gets updated (you can simply check the commmit history) I intend to remove this message as I would of course guarentee its functionality. I am simply putting this up as it has been roughly ~3 years since the projects code was developed or reviewed. Thank you for understanding.

### Why?

---

I wanted to encrypt my SD cards so I modified my [`pylocker`](https://www.github.com/tilas01/pylocker) project to support recursive encryption/decryption

### Requirements

---

To use this program you will require [`python`](https://www.python.org/) 3.9 or higher (Most recent build of Python tested and confirmed to be fully working with sdcrypt with no errors and was developed using Python 3.9, if it ever stops working with the leatest build of Python or has any errors please report it under "Issues", thank you.)

### Installation

ℹ️ If you have previously used PyLocker and are updating after installing by running the below please review the [Use](#use) section to update from your current config, if this is your first time using sdcrypt and have never used PyLocker you can safely ignore this message. ℹ️

Install with [`git`](https://git-scm.com/) ([Python](https://www.python.org/downloads) 3.9 or higher required)

```
$ git clone https://github.com/tilas0/sdcrypt.git
$ cd sdcrypt
$ pip3 install -r requirements.txt
$ python3 main.py
```

Install without git ([Python](https://www.python.org/downloads) 3.9 or higher required)

How to install Python3 on Linux with the apt package manager:

```
$ sudo apt update
$ sudo apt install python3
```

How to install Python 3.9 or higher on any other OS:

Visit the [Python3](https://www.python.org/downloads) official website (This is simply the official download site and will download the most recent build as any package manager would when installing or updating Python. SDCrypt should be working on all later python builds as of writing this please report it under "Issues" if the project stops working with the latest build please). Then go to downloads and install the version of Python3 that matches your Operating System

You may then follow the above stepts under "Install with git" excluding the command that clones this repository using git clone and instead by downloading the repo directly from GitHub and extracting the archive then simply cd into it and install using pip3 with python3. These installation steps can be followed to install sdcrypt on any operating system python3 supports (Windows, MacOS, Linux, etc) making sdcrypt highly cross-compatible with many operating systems. [`git`](https://git-scm.com/) is also cross compatible but if you dont wish to install another application to support cloning the repository from the terminal but is not *required* to run the program. So this may be easier or you if you are not on Linu and/or Do not have a package manager where you can easily install [`git`](https://git-scm.com/) with a command like `$ sudo apt install git`. If you are on Linux and/or have a package manager I recommend following the git steps, installing [`git`](https://git-scm.com/) with your package manager first of course with the command above or a similar one if you have a different package manager, apt is simply the most common pre-installed package manager. If you are on Arch Linux or a distro based on it your package manager will be pacman type `man pacman` (or whatever the name of your package manager is) for more a manual on how to use the program and more info about how to use the program.



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
