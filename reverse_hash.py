def reverse_hash(hash_value):
    LETTERS = 'acdegilmnoprstuw'
    value = []
    while hash_value > 37:
        for i, letter in enumerate(LETTERS):
            if (hash_value - i) % 37 == 0:
                value.append(letter)
                hash_value = (hash_value - i) / 37
                break

    return ''.join(reversed(value))


def main():
    key_to_hash = 930846109532517
    print("Internal Tools Developer code answer: " + reverse_hash(key_to_hash))


if __name__ == '__main__':
    main()
