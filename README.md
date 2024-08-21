# Caesar Cipher GUI Application

## Introduction

The Caesar Cipher GUI Application is a simple Python-based program that allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The application provides a graphical user interface (GUI) where users can input a message and a shift value to perform encryption and decryption. This project is built using the PySide6 library, which offers the necessary tools for creating desktop applications with a native look and feel.

## Features

- **Encryption and Decryption**: Easily encrypt and decrypt messages using the Caesar Cipher.
- **Custom Shift Value**: Users can specify a custom shift value for encryption/decryption.
- **Input Validation**: The application validates user input to ensure that the shift value is an integer and that the message is not empty.
- **Copy to Clipboard**: Encrypted and decrypted messages can be copied to the clipboard with a single click.
- **Custom Icons**: The application and its dialog windows support custom icons, enhancing the visual appeal.

## Requirements

To run this application, you need the following:

- **Python 3.x**: Make sure you have Python installed on your system.
- **PySide6**: This is the Python module used to create the GUI. You can install it using pip:

  ```bash
  pip install PySide6