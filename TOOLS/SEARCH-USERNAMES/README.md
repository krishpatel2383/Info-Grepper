# Search Usernames

This script of code, using `request` module, will  help to determine weather, a username exists on a platform or not.

## Setup

The script uses universal libraries.

```bash
pip3 install argparse requests
```

## Usage

```bash
usage: search_user.py [-h] -u USERNAMES -t TARGETS [TARGETS ...]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAMES, --usernames USERNAMES
                        Enter the username.
  -t TARGETS [TARGETS ...], --targets TARGETS [TARGETS ...]
                        Enter the website(s). Use Lowercase only
```

## Sample Usage and Output

On the command line interface, use the following command 

```bash
$ python search_user.py -u hack-parthsharma -t instagram

$ python search_user.py -u hack-parthsharma -t instagram github
```

## Supported Platforms

The list of supported platforms can be found [here](./platfrom.txt)
