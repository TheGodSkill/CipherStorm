import string
import tkinter as tk


def encrypt(word, passphrase):
    alphabet = string.ascii_lowercase
    encrypted = ''
    for i, char in enumerate(word):
        shift = alphabet.index(passphrase[i % len(passphrase)])
        encrypted += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
    return encrypted

def decrypt(encrypted, passphrase):
    alphabet = string.ascii_lowercase
    word = ''
    for i, char in enumerate(encrypted):
        shift = alphabet.index(passphrase[i % len(passphrase)])
        word += alphabet[(alphabet.index(char) - shift) % len(alphabet)]
    return word

def on_encrypt_click():
    word = word_entry.get()
    passphrase = passphrase_entry.get()
    encrypted = encrypt(word, passphrase)
    result_label.config(text=f'Encrypted: {encrypted}')

def on_decrypt_click():
    encrypted = encrypted_entry.get()
    passphrase = passphrase_entry.get()
    decrypted = decrypt(encrypted, passphrase)
    result_label.config(text=f'Decrypted: {decrypted}')


root = tk.Tk()
root.title('Encryption/Decryption Tool')

word_label = tk.Label(root, text='Word:')
word_label.grid(row=0, column=0, padx=5, pady=5)
word_entry = tk.Entry(root)
word_entry.grid(row=0, column=1, padx=5, pady=5)


passphrase_label = tk.Label(root, text='Passphrase:')
passphrase_label.grid(row=1, column=0, padx=5, pady=5)
passphrase_entry = tk.Entry(root)
passphrase_entry.grid(row=1, column=1, padx=5, pady=5)


encrypt_button = tk.Button(root, text='Encrypt', command=on_encrypt_click)
encrypt_button.grid(row=2, column=0, padx=5, pady=5)
decrypt_button = tk.Button(root, text='Decrypt', command=on_decrypt_click)
decrypt_button.grid(row=2, column=1, padx=5, pady=5)


encrypted_label = tk.Label(root, text='Encrypted:')
encrypted_label.grid(row=3, column=0, padx=5, pady=5)
encrypted_entry = tk.Entry(root)
encrypted_entry.grid(row=3, column=1, padx=5, pady=5)


result_label = tk.Label(root, text='')
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
