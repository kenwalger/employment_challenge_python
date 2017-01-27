def hasher(string_to_hash):
    hash_key = 7
    LETTERS = 'acdegilmnoprstuw'

    for i in range(0, len(string_to_hash)):
        hash_key = (hash_key * 37 + LETTERS.index(string_to_hash[i]))

    return hash_key


def main():
    key_to_hash = 'leepadg'
    print(hasher(key_to_hash))


if __name__ == '__main__':
    main()
