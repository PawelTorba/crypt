import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key

class EncryptionError(Exception):
    pass


def generate_aes_key():
    # AES-256 => 32 bytes
    return os.urandom(32)


def generate_nonce():
    # Recommended nonce size for GCM = 12 bytes
    return os.urandom(12)


def save_binary_file(path, data):
    with open(path, "wb") as f:
        f.write(data)


def encrypt_file_aes_gcm(
    input_file,
    output_file,
    aes_key,
    nonce
):
    try:

        with open(input_file, "rb") as f:
            plaintext = f.read()

        aesgcm = AESGCM(aes_key)

        ciphertext = aesgcm.encrypt(
            nonce,
            plaintext,
            None
        )

        with open(output_file, "wb") as f:
            f.write(ciphertext)

    except Exception as e:
        raise EncryptionError(f"Błąd szyfrowania AES-GCM: {str(e)}")


def encrypt_aes_key_with_rsa(
    aes_key,
    public_key_file
):
    try:

        with open(public_key_file, "rb") as key_file:
            public_key = load_pem_public_key(
                key_file.read()
            )

        encrypted_key = public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted_key

    except Exception as e:
        raise EncryptionError(
            f"Błąd szyfrowania klucza AES kluczem RSA: {str(e)}"
        )


def encrypt_dispatcher(
    algorithm,
    input_file,
    output_file,
    rsa_enabled=False,
    rsa_public_key_file=None
):

    if algorithm == "AES-256-GCM":

        aes_key = generate_aes_key()

        nonce = generate_nonce()

        encrypt_file_aes_gcm(
            input_file=input_file,
            output_file=output_file,
            aes_key=aes_key,
            nonce=nonce
        )

        base_name = output_file

        key_file = base_name + ".key"
        nonce_file = base_name + ".nonce"

        if rsa_enabled:

            encrypted_key = encrypt_aes_key_with_rsa(
                aes_key,
                rsa_public_key_file
            )

            save_binary_file(
                key_file + ".enc",
                encrypted_key
            )

        else:

            save_binary_file(
                key_file,
                aes_key
            )

        save_binary_file(
            nonce_file,
            nonce
        )

    else:
        raise EncryptionError(
            f"Nieobsługiwany algorytm: {algorithm}"
        )
    
def decrypt_aes_key_with_rsa(encrypted_key_path, private_key_path):
    with open(private_key_path, "rb") as f:
        private_key = load_pem_private_key(f.read(), password=None)

    with open(encrypted_key_path, "rb") as f:
        encrypted_key = f.read()

    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return aes_key

def decrypt_file_aes_gcm(input_file, output_file, aes_key, nonce):
    try:
        with open(input_file, "rb") as f:
            ciphertext = f.read()

        aesgcm = AESGCM(aes_key)

        plaintext = aesgcm.decrypt(
            nonce,
            ciphertext,
            None
        )

        with open(output_file, "wb") as f:
            f.write(plaintext)

    except Exception as e:
        raise EncryptionError(f"Błąd odszyfrowania AES-GCM: {str(e)}")

def decrypt_dispatcher(
    algorithm,
    input_file,
    output_file,
    aes_key_file=None,
    nonce_file=None,
    rsa_enabled=False,
    rsa_private_key_file=None
):

    if algorithm != "AES-256-GCM":
        raise ValueError("Nieobsługiwany tryb AES")

    # --- AES KEY ---
    if rsa_enabled:
        aes_key = decrypt_aes_key_with_rsa(
            encrypted_key_path=aes_key_file,
            private_key_path=rsa_private_key_file
        )
    else:
        with open(aes_key_file, "rb") as f:
            aes_key = f.read()

    # --- NONCE (OSOBNY PLIK) ---
    if not nonce_file:
        raise ValueError("Brak pliku nonce/IV")

    with open(nonce_file, "rb") as f:
        nonce = f.read()

    # --- DECRYPT ---
    decrypt_file_aes_gcm(
        input_file=input_file,
        output_file=output_file,
        aes_key=aes_key,
        nonce=nonce
    )