from Crypto.Cipher import AES
import base64


def zero_pad(data: bytes, block_size=16):
    padding_len = block_size - (len(data) % block_size)

    # jeśli tekst już jest wielokrotnością bloku,
    # ZeroPadding nie dodaje dodatkowego bloku
    if padding_len == block_size:
        return data

    return data + b'\x00' * padding_len


def encrypt(text: str, key: str) -> str:
    key_bytes = key.encode("utf-8")

    if len(key_bytes) != 32:
        raise ValueError(
            "Klucz musi mieć dokładnie 32 znaki (AES-256)"
        )

    # CrypTool: IV = 16 zer
    iv = bytes(16)

    cipher = AES.new(
        key_bytes,
        AES.MODE_CBC,
        iv
    )

    data = zero_pad(text.encode("utf-8"))

    encrypted = cipher.encrypt(data)

    return base64.b64encode(
        encrypted
    ).decode("utf-8")


def decrypt(cipher_b64: str, key: str) -> str:
    key_bytes = key.encode("utf-8")

    if len(key_bytes) != 32:
        raise ValueError(
            "Klucz musi mieć dokładnie 32 znaki (AES-256)"
        )

    iv = bytes(16)

    cipher = AES.new(
        key_bytes,
        AES.MODE_CBC,
        iv
    )

    encrypted = base64.b64decode(cipher_b64)

    decrypted = cipher.decrypt(encrypted)

    # usunięcie zerowego paddingu
    return decrypted.rstrip(
        b'\x00'
    ).decode("utf-8")


# TEST
text = "sigma"
key = "12345678901234567890123456789012"

enc = encrypt(text, key)
print("Zaszyfrowane:", enc)
#enc = "1OFA+AaxdAjm4xInrhElTQ=="

dec = decrypt(enc, key)
#print("Odszyfrowane:", dec)