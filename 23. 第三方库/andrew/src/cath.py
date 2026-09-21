from ai_totails import completions


def main() -> None:
    print("开始ai聊天")
    masg: list[dict[str, str]] = []
    while True:
        user_input: str = input("\n你: ").strip()
        if user_input == "/exit":
            print("再见！")
            break
        if not user_input:
            continue
        masg.append({"role": "user", "content": user_input})
        ruesout = completions(massge=masg)
        print("AI: ", end="", flush=True)
        aistr: str = ""
        for str in ruesout:
            print(str, end="", flush=True)
            aistr += str
        masg.append({"role": "assistant", "content": aistr})
        print()


if __name__ == "__main__":
    main()
