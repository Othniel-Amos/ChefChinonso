from configure import ChatBot

bot = ChatBot()


while True:
    user_input = input("You:")

    if user_input.lower() in ["exit", "quit", "bye"]:
        break

    res = bot.chat(user_input)
    print(res)
