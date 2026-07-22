# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MiniCRM
def user_system():
    users = {}

    def register(name, email):
        if name in users: return "Already exists"
        users[name] = {"email": email}

    def login(name, password=None):
        u = users.get(name)
        return u and u["name"]

    def logout():
        print("Logged out")

    def profile():
        name = input("Name: ")
        email = input("Email: ")
        register(name, email)
        print(f"Registered as {name}")

    while True:
        cmd = input("\n(user: ) ").strip() or "menu"
        if cmd == "user": profile()
        elif cmd == "logout": logout()
        else: break
