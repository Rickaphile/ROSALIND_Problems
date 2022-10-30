f = open('ROSALIND_Problems/Rabbits and Recurrence Relations/rosalind_fib.txt')

metrics = f.read()
n, k = int(metrics.split(' ')[0]), int(metrics.split(' ')[1])

# 1, 1, 1+k, (1+k)+k, (1+k+k)+k(1+k)
def wabbits(n, k):
    if n == 0: return 0
    if n == 1: return 1
    else:
        return wabbits(n-1, k) + k*wabbits(n-2, k)

print(wabbits(n, k))
