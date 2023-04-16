# python3

def read_input():
    pattern=""
    text=""
    input_type = input().rstrip()

    if input_type == 'I':

        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        
        with open(f"./tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    if p_hash == t_hash and pattern == text[:p_len]:
        occurrences.append(0)

    for i in range(1, t_len - p_len + 1):
        t_hash = hash(text[i:i + p_len])
        if p_hash == t_hash and pattern == text[i:i + p_len]:
            occurrences.append(i)

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
