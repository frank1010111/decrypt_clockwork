def rotate(ciphertext: str, key: int = 0):
    """Rotate ciphertext by a set number, returning plain text."""
    plaintext = ""
    start = ord("A")
    for char in ciphertext:
        if "A" <= char <= "Z":
            shifted_char_code = (ord(char) - start + key) % 26 + start
            plaintext += chr(shifted_char_code)
        else:
            plaintext += char
    return plaintext


def decode_text(ciphertext: str, key: str):
    """Decode text using a vigenère cipher.

    Parameters
    ----------
    ciphertext : str
        The encrypted text to decode.
    key : str
        The text that serves as a key

    Returns
    -------
    Decoded text

    References
    ----------
    <https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher>
    """
    i_key = 0
    numeric_key = [ord(char) - ord("A") for char in key]
    plaintext = ""
    for char in ciphertext:
        if ord("A") <= ord(char) <= ord("Z"):
            plaintext += rotate(char, -numeric_key[i_key])
            if i_key >= len(numeric_key) - 1:
                i_key = 0
            else:
                i_key += 1
        else:
            plaintext += char
    return plaintext
