def add_word(trie, word):
    node = trie

    for char in word:
        if char not in node[2]:
            node[2][char] = [0, 0, {}]

        node = node[2][char]
        node[0] += 1
        node[1] = max(node[1], len(word))


def query_word(trie, word):
    node = trie

    for char in word:
        if char not in node[2]:
            return (-1, -1)

        node = node[2][char]

    return (node[0], node[1])


trie = [0, 0, {}]

while True:
    try:
        n = int(input())
        for _ in range(n):
            add_word(trie, input())

        q = int(input())
        for _ in range(q):
            count, max_length = query_word(trie, input())
            print(f"{count} {max_length}" if count != -1 else -1)
    except EOFError:
        break
