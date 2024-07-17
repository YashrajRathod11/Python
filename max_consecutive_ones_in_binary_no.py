def consecutive(n):
    str = bin(n)[2:]
    print('Binary conversion of ', n, 'is:  ', str)
    result = max(len(group) for group in str.split('0'))
    return result

if __name__ == '__main__':
    n = int(input("Enter the value of n: ").strip())
    max_ones = consecutive(n)
    print('Maximun number of consecutive 1 are: ',max_ones)