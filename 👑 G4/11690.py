n = int(input())
mod = 1 << 32
isPrime = [1]*(n+1)
for i in range(2, int(n**0.5)+1):
  if isPrime[i]:
    j = i
    while i*j <= n:
      isPrime[i*j] = 0
      j += 1

res = 1
primes = [2]
for i in range(3, n+1, 2):
  if isPrime[i]:
    primes.append(i)
  
for i in primes:
  power = i
  while power*i <= n:
    power *= i
  res = (res * power) % mod
print(res)

# convert to c++
# #include <iostream>
# #include <vector>
# #include <cmath>

# using namespace std;

# const int MAX_N = 100000001;
# const unsigned long MOD = 1UL << 32;;

# vector<bool> isPrime(MAX_N + 1, true);

# void sieve() {
#     for (int i = 2; i <= sqrt(MAX_N); i++) {
#         if (isPrime[i]) {
#             for (int j = i * i; j <= MAX_N; j += i) {
#                 isPrime[j] = false;
#             }
#         }
#     }
# }

# int main() {
#     int n;
#     cin >> n;

#     sieve();

#     vector<int> primes;
#     primes.push_back(2);
#     for (int i = 3; i <= n; i += 2) {
#         if (isPrime[i]) {
#             primes.push_back(i);
#         }
#     }

#     long long res = 1;
#     for (int i = 0; i < primes.size(); i++) {
#         long long power = primes[i];
#         while (power * primes[i] <= n) {
#             power *= primes[i];
#         }
#         res = (res * power) % MOD;
#     }

#     cout << res << endl;

#     return 0;
# }