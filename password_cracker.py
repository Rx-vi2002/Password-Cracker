import hashlib

def crack_sha256_hash(hash_to_crack, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for word in file:
                word = word.strip()
                if hashlib.sha256(word.encode()).hexdigest() == hash_to_crack:
                    print(f"[+] Password Found: {word}")
                    return word
        print("[-] Password not found in wordlist.")
        return None
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
        return None

if __name__ == "__main__":
    hash_input = input("Enter SHA-256 hash to crack: ")
    wordlist = input("Enter path to wordlist: ")
    crack_sha256_hash(hash_input, wordlist)
