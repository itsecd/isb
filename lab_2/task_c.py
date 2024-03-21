from scipy.special import gammaincc


def main():
    bits = '11001000001111111010100100100110101011101101101110100111111001000000000101000110110000001001011000111110001010110001111000101110'
    max_list = []
    for i in range(16):
        block = bits[i * 8: (i + 1) * 8]
        one_count = 0
        max_one_in_block = 0
        for bit in block:
            if bit == '1':
                one_count += 1
                max_one_in_block = max(max_one_in_block, one_count)
            else:
                one_count = 0
        max_list.append(max_one_in_block)
    v1 = max_list.count(0)+max_list.count(1)
    v2 = max_list.count(2)
    v3 = max_list.count(3)
    v4 = 16-v1-v2-v3
    pi0 = 0.2148
    pi1 = 0.3672
    pi2 = 0.2305
    pi3 = 0.1875
    X = ((v1-16*pi0)**2)/(16*pi0) + ((v2-16*pi1)**2)/(16*pi1) + ((v3-16*pi2)**2)/(16*pi2) + ((v4-16*pi3)**2)/(16*pi3)
    P=gammaincc(3/2,X/2)
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")
    
if __name__ == "__main__":
    main()
