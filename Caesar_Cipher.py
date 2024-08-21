import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QClipboard

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Preserve case
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabetically
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetical characters are added as-is
            result += char

    return result

class CaesarCipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Caesar Cipher')
        self.setGeometry(100, 100, 400, 200)  # Set window position and size (x, y, width, height)

        # Layout
        layout = QVBoxLayout()

        # Message input
        self.message_label = QLabel('Enter your message:')
        self.message_input = QLineEdit(self)
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        # Shift input
        self.shift_label = QLabel('Enter shift value:')
        self.shift_input = QLineEdit(self)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_input)

        # Encrypt button
        self.encrypt_button = QPushButton('Encrypt', self)
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        # Decrypt button
        self.decrypt_button = QPushButton('Decrypt', self)
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

    def validate_input(self):
        # Validate message input
        if not self.message_input.text():
            QMessageBox.warning(self, 'Validation Error', 'Message is required.')
            return False

        # Validate shift input
        try:
            int(self.shift_input.text())
        except ValueError:
            QMessageBox.warning(self, 'Validation Error', 'Shift value must be a valid integer.')
            return False

        return True

    def encrypt_message(self):
        if self.validate_input():
            text = self.message_input.text()
            shift = int(self.shift_input.text())
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            self.show_result_popup('Encrypted Message', encrypted_text)

    def decrypt_message(self):
        if self.validate_input():
            text = self.message_input.text()
            shift = int(self.shift_input.text())
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            self.show_result_popup('Decrypted Message', decrypted_text)

    def show_result_popup(self, title, message):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)

        layout = QVBoxLayout(dialog)

        message_label = QLabel(message)
        message_label.setWordWrap(True)
        layout.addWidget(message_label)

        button_layout = QHBoxLayout()

        copy_button = QPushButton('Copy')
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(message))
        button_layout.addWidget(copy_button)

        ok_button = QPushButton('OK')
        ok_button.clicked.connect(dialog.accept)
        button_layout.addWidget(ok_button)

        layout.addLayout(button_layout)

        dialog.setLayout(layout)
        dialog.exec()

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, 'Copied', 'The text has been copied to the clipboard.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CaesarCipherApp()
    ex.show()
    sys.exit(app.exec())