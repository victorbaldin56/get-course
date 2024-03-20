def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
