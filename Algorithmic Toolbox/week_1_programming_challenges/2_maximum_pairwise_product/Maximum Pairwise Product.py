from numpy import sort


def MaxPairwiseProduct(A):
    n = len(A)
    A=sort(A)
    return A[n-2]*A[n-1]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(MaxPairwiseProduct(input_numbers))