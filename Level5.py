def main():
    while True:
        try:
            # ユーザー入力を受け取る
            user_input = input("1以上の整数を入力してください: ")
            number = int(user_input)

            # 入力が1以上かチェック
            if number < 1:
                print("整数を入力してください。")
                continue
        except ValueError:
            print("整数を入力してください。")
            continue

        # 入力が正しい場合の処理
        if number == 1:
            print(0)
        elif number == 2:
            print(1)
        else:
            # 入力された数を-2してNとする
            N = number - 2

            # 初期値
            A, B = 0, 1

            # N回ループ
            for _ in range(N):
                C = A + B
                A, B = B, C

            print(C)

        break

# 実行
if __name__ == "__main__":
    main()
