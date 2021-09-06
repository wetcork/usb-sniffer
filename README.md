# usb-sniffer

**usb-sniffer** is a python script that listen for connected drives and silently copy their content to a specified folder

## Installation/Requirements

`pip install -r requirements.txt`

## Usage

```text
usage: usb-sniffer [-h] [-o PATH] [-d SECONDS] [-sd SECONDS] [-s]

optional arguments:
  -o PATH, --output PATH
                        Set where the drives will be copied
  -d SECONDS, --delay SECONDS
                        Set the delay between detections
  -sd SECONDS, --self-destruct SECONDS
                        Set how long the script must run before killing itself
  -s, --silent          Hide the console while running
  -v, --version         Show program's version number and exit
  ```

## TODO

- I think i can clean up the code a bit
- Option to autokill the script after certain number of drives copied
- Option to filter drives to copy by size
- Option to send copied files to an FTP server or via email

## Changelog

```text
v0.1
- Initial relase
```