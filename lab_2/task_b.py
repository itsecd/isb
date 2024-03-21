from math import sqrt
from scipy.special import erfc


def main():
    bit = '11001000001111111010100100100110101011101101101110100111111001000000000101000110110000001001011000111110001010110001111000101110'
    one_count = bit.count('1') 
    f1=one_count/128
    if(abs(f1-0.5)<2/sqrt(128)):
        count = 0
        for i in range (127):
            if bit[i] != bit[i+1]:
                count+=1
        P = erfc(abs(count-2*128*f1*(1-f1))/(2*sqrt(2*128)*f1*(1-f1)))
    else:
        P=0;
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")

if __name__ == "__main__":
    main()
