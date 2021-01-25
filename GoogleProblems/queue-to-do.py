def solution(start, length):
    # Arrays for storing the ids
    ids = []
    # Collection c, containing all numbers that will be noted  
    c = list(range(start, start + length * length))
    # Loop through list, making jumps equal to the length, used for splitting the array
    for i in range(0, len(c), length):
            # Create a slice, based on the current index until the length, which equals
            # One 'line' that is going to be tested eventually
            ids.append(c[i:i + length])
    # Loop through the entire id list, reorganize the ID's which are being tested
    for i in range(len(ids)):
        ids[i] = ids[i][0:len(ids)-i]
    # Temporary XOR value, will eventually be checksum result
    prev_xor = 0
    # Loop over ID's to create the checksum
    for i in ids:
        for j in range(len(i)):
            prev_xor = i[j] ^ prev_xor
    return prev_xor

