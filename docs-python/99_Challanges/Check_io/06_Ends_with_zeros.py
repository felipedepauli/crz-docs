from numpy import number


def numberOfZeros(sequence):
    count = 0
    string_sequence = str(sequence)[::-1]
    for i in string_sequence:
        if int(i) % 10 == 0:
            count += 1;
        else:
            break
    return count

sequence = 11
print(numberOfZeros(sequence))