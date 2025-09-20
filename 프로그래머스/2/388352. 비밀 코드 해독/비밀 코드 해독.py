from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    guess_sets = [set(guess) for guess in q]
    
    cnt = 0
    for comb in combinations(range(1, n + 1),5):
        is_valid = True
        
        for i, guess_set in enumerate(guess_sets):
            match_cnt = len(set(comb) & guess_set)
            
            if match_cnt != ans[i]:
                is_valid = False
                break
        
        if is_valid:
            cnt += 1
    
    return cnt