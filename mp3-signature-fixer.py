#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file     mp3-signature-fixer.py
@date     2023-10-19
@version  0.1.0
@license  GNU General Public License v3.0
@author   Alejandro Gonzalez Momblan (agelrenorenardo@gmail.com)
@desc     Script to add the MP3 file signature to a binary file.
"""
import os
import sys
from tkinter import Tk, filedialog

from hexdump import hexdump
from rich import print
from rich.traceback import install

DEBUG = False

ID3_SIGNATURE = b"\x49\x44\x33"  # ID3v2 file signature
MAX_BYTES_TO_PRINT = 1000
MP3_EXTENSION = ".mp3"


def print_beauty_hex(data: bytes) -> None:
    """
    Print the hexdump of the data in a beautiful way.

    Args:
        data (bytes): The binary data to print.
    """
    content = hexdump(data, result="return")
    print(content[:MAX_BYTES_TO_PRINT])


def ensure_file_signature(data: bytes) -> bool:
    """
    Check if the provided data starts with the MP3 file signature.

    Args:
        data (bytes): The binary data to check.

    Returns:
        bool: True if the data starts with the MP3 signature, False otherwise.
    """
    return data.startswith(ID3_SIGNATURE)


def select_mp3_file() -> str:
    """
    Open a file dialog to select an MP3 file.

    Returns:
        str: The path to the selected MP3 file.
    """
    try:
        print("Select an MP3 file")
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            defaultextension=MP3_EXTENSION,
            filetypes=[("MP3 files", f"*{MP3_EXTENSION}")],
        )
        return file_path
    except FileNotFoundError:
        print("Selected file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while selecting a file: {str(e)}")
        sys.exit(1)


def add_mp3_signature(content: bytes) -> bytes:
    """
    Add the MP3 file signature to the given binary content. For the MP3 file
    signature, the first 3 bytes of the file must be "ID3" which in hex is
    "49 44 33", according to the ID3v2 container specification. For more
    information, see https://en.wikipedia.org/wiki/MP3#File_structure.

    Args:
        content (bytes): The binary data to which the signature will be added.

    Returns:
        bytes: The content with the MP3 signature added.
    """
    return ID3_SIGNATURE + content


def save_mp3_file(content: bytes) -> None:
    """
    Save binary content as an MP3 file using a file dialog.

    Args:
        content (bytes): The binary data to save.
    """
    try:
        new_file_path = filedialog.asksaveasfilename(
            defaultextension=MP3_EXTENSION,
            filetypes=[("MP3 files", f"*{MP3_EXTENSION}")],
        )
        if new_file_path:
            with open(new_file_path, "wb", encoding="utf-8") as f:
                f.write(content)
            print("File saved successfully.")
        else:
            print("File save operation canceled.")
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")
        sys.exit(1)


def main():
    file_path = select_mp3_file()
    if not file_path:
        print("No file selected")
        sys.exit(1)

    file_name = os.path.basename(file_path)
    assert file_name.endswith(MP3_EXTENSION)

    with open(file_path, "rb") as f:
        content = f.read()

    print("File content:")
    print_beauty_hex(content)

    if ensure_file_signature(content):
        print("The file contains the MP3 signature")
        return

    print("The file does not contain any MP3 signature")
    print("Adding MP3 signature...")
    new_content = add_mp3_signature(content)
    print("New file content:")
    print_beauty_hex(new_content)
    save_mp3_file(new_content)

    with open(file_path, "rb") as f:
        content = f.read()
    assert ensure_file_signature(content)


if __name__ == "__main__":
    install(show_locals=DEBUG)
    main()
