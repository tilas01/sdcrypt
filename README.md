
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
---
Install with [`git`](https://git-scm.com/)
```
$ git clone https://github.com/tilas0/sdcrypt.git
$ cd sdcrypt
$ pip3 install -r requirements.txt
$ python3 main.py
```

### Use
---

#### Update:

Clone the git repo and move your config folder into it. Then replace the old folder with the new one.
or
Run the following commands with [`git`](https://git-scm.com/) installed in your [`sdcrypt`](https://www.github.com/tilas01/sdcrypt) directory:

```
$ git pull
$ pip3 install -r requirements.txt
```

This will check the git repo for updates and install any new requirements if possible.

#### Reset your password:

Ensure all files are in a decrypted state. Then delete the "hash" file located in the config directory.

#### Reset your salt:

Ensure all files are in a decrypted state. Then delete the "hash" and "salt" files located in the config directory. This will also reset your password.

#### Use a backed up salt:

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