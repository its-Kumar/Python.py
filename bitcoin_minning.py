from hashlib import sha256

MAX_NONCE = 100000000000


def SHA256(text: str):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number: int, transections: str, previous_hash: str,
         prefix_zeros: int) -> str:
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transections + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            return new_hash
    raise BaseException(
        f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == "__main__":
    transactions = """
    Kumar -> Aditya -> 20,
    Mando -> Cara -> 45
    """
    difficulty = 10
    previous_hash = '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7'
    import time

    start = time.time()
    print("START MINING....")
    new_hash = mine(5, transactions, previous_hash, difficulty)
    total_time = str(time.time() - start)
    print(new_hash)
    print(f"END MINING.... Mining took  {total_time} seconds")
