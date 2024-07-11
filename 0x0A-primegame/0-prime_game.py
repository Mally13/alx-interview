#!/usr/bin/python3
"""
Contains a function that determines the winner of a
prime game
"""

def sieve_of_eratosthenes(max_num):
    """Identifies prime numbers within range max_num"""
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= max_num:
        if primes[p]:
            for i in range(p * p, max_num + 1, p):
                primes[i] = False
        p += 1
    return [num for num, is_prime in enumerate(primes) if is_prime]

def isWinner(x, nums):
    """
    Determines the winner of a prime game
    """
    if x <= 0 or not nums:
        return None
    
    max_num = max(nums)
    prime_list = sieve_of_eratosthenes(max_num)
    prime_set = set(prime_list)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n < 2:
            ben_wins += 1
            continue
        
        current_set = set(range(1, n + 1))
        player_turn = 0  # 0 for Maria, 1 for Ben
        
        while True:
            available_primes = [p for p in prime_list if p in current_set]
            if not available_primes:
                if player_turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            
            selected_prime = available_primes[0]
            multiples = set(range(selected_prime, n + 1, selected_prime))
            current_set -= multiples
            player_turn = 1 - player_turn
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
