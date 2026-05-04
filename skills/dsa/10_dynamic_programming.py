"""
10 - Dynamic Programming Classics
====================================
Implementations of four fundamental DP problems:
Fibonacci, 0/1 Knapsack, Longest Common Subsequence, and Coin Change.

Key Concepts:
    - Overlapping subproblems & optimal substructure
    - Memoization (top-down) vs tabulation (bottom-up)
    - Space optimization techniques
"""


# --- 1. Fibonacci ---

def fibonacci_memo(n, memo=None):
    """Fibonacci using memoization (top-down). O(n) time, O(n) space."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_tab(n):
    """Fibonacci using tabulation (bottom-up). O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# --- 2. 0/1 Knapsack ---

def knapsack(weights, values, capacity):
    """
    0/1 Knapsack Problem using tabulation.
    Returns the maximum value achievable within the given capacity.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # don't take item i
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]


# --- 3. Longest Common Subsequence ---

def lcs(text1, text2):
    """
    Longest Common Subsequence — returns the length and the subsequence itself.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual subsequence
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            result.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(result))


# --- 4. Coin Change ---

def coin_change(coins, amount):
    """
    Minimum number of coins needed to make the given amount.
    Returns -1 if not possible.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    # Fibonacci
    print("--- Fibonacci ---")
    for n in [10, 20, 30, 40]:
        print(f"  F({n}) = {fibonacci_tab(n)}")

    # Knapsack
    print("\n--- 0/1 Knapsack ---")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    cap = 8
    print(f"  Items: weights={weights}, values={values}")
    print(f"  Capacity: {cap}")
    print(f"  Max value: {knapsack(weights, values, cap)}")

    # LCS
    print("\n--- Longest Common Subsequence ---")
    s1, s2 = "ABCBDAB", "BDCAB"
    length, subseq = lcs(s1, s2)
    print(f"  Text1: '{s1}', Text2: '{s2}'")
    print(f"  LCS length: {length}, LCS: '{subseq}'")

    # Coin Change
    print("\n--- Coin Change ---")
    coins = [1, 5, 10, 25]
    amount = 63
    print(f"  Coins: {coins}, Amount: {amount}")
    print(f"  Min coins: {coin_change(coins, amount)}")

    amount2 = 11
    coins2 = [1, 5, 6, 9]
    print(f"  Coins: {coins2}, Amount: {amount2}")
    print(f"  Min coins: {coin_change(coins2, amount2)}")
