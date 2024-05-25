# PlayStation Save Icon Generator

## Description

Python script that generates folder icons for each save folder.
Compatible only with PSP and PS3, as those are the only save types that included an unpacked image alongside saves.
Windows only.

## Requirements

- Having python installed.
- Running `pip install -r requirements.txt` to install the required dependencies.

## Running

- Run `generate-ps-save-icons.py` as administrator.
- Run `python generate-ps-save-icons.py` in the terminal, as administrator.

(Administrator rights are required to be able to write the `desktop.ini` files).

## Notes

The OS will only load up the icons when it feels like it; it usually seems to be at random.  
There are some workarounds but they only sometimes work.  
Often the best solution is to sign out or restart the computer.
