from game_logic import generate_numbers, get_hint, validate_input

def main():
    print("숫자 야구 게임을 시작합니다.")
    
    while True:
        secret_numbers = generate_numbers()
        
        while True:
            try:
                user_input = input("숫자를 입력해주세요 : ")
                user_numbers = validate_input(user_input)
                result = get_hint(secret_numbers, user_numbers)
                print(result)
                if result == "3스트라이크":
                    print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
                    break
            except ValueError as e:
                print(e)
                return
        
        while True:
            retry = input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요. : ")
            if retry == "1":
                break
            elif retry == "2":
                print("게임을 종료합니다.")
                return
            else:
                print("잘못된 입력입니다. 1 또는 2를 입력하세요.")

if __name__ == "__main__":
    main()