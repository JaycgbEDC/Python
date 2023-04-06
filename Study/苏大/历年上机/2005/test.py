# 将一个数拆分成多个素数之和
import math

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

def find_primes(n):
    prime_list = [i for i in range(n,1,-1) if is_prime(i)] # 生成0~n的所有素数

    def DFS(n, index, sum, prime_list, current=[]):
        """
        n: 求解的数， index：下一个要判断的在prime_list中的索引
        sum：当前的和  prime_list: 0~n的素数列表  current：当前的求解组合
        """
        if sum > n or index >= len(prime_list):
            return False
        if sum == n:
            print(current)
            return True
        else:
            current.append(prime_list[index])
            if DFS(n, index+1, sum+prime_list[index], prime_list, current):
                return True
            else:
                current.pop()
                return DFS(n, index+1, sum, prime_list, current)

    DFS(n, 0, 0, prime_list)
        
if __name__ == "__main__":
    find_primes(int(input()))