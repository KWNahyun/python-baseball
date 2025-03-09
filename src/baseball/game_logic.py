import random

def generate_numbers():
    return random.sample(range(1, 10), 3)

def get_hint(secret, guess):
    strike = sum(s == g for s, g in zip(secret, guess))
    ball = sum(g in secret for g in guess) - strike
    
    if strike == 3:
        return "3스트라이크"
    elif strike > 0 and ball > 0:
        return f"{ball}볼 {strike}스트라이크"
    elif strike > 0:
        return f"{strike}스트라이크"
    elif ball > 0:
        return f"{ball}볼"
    else:
        return "낫싱"

def validate_input(user_input):
    if not user_input.isdigit() or len(user_input) != 3:
        raise ValueError("잘못된 입력입니다. 1~9 사이의 서로 다른 3자리 숫자를 입력하세요.")
    user_numbers = [int(digit) for digit in user_input]
    if len(set(user_numbers)) != 3 or any(d < 1 or d > 9 for d in user_numbers):
        raise ValueError("잘못된 입력입니다. 1~9 사이의 서로 다른 3자리 숫자를 입력하세요.")
    return user_numbers