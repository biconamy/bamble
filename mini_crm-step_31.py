# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MiniCRM
PROFILE_DIR = Path.home() / ".minicrm" / "profiles"
if not PROFILE_DIR.exists():
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)


class Profile:
    def __init__(self, name="default", email=None):
        self.name = name
        self.email = email

    def save(self):
        path = PROFILE_DIR / f"{self.name}.json"
        with open(path, "w") as f:
            json.dump({"name": self.name, "email": self.email}, f)


class ProfileManager:
    _profiles = {}
    _active = None

    @classmethod
    def load(cls):
        if cls._active is not None:
            return cls._active
        for p in sorted(PROFILE_DIR.glob("*.json")):
            with open(p) as f:
                data = json.load(f)
                prof = Profile(name=data["name"], email=data.get("email"))
                cls._profiles[prof.name] = prof
        if not cls._profiles:
            default = Profile()
            default.save()
            cls._profiles["default"] = default
            return cls._profiles["default"]
        return next(iter(cls._profiles.values()))

    @classmethod
    def switch(cls, name):
        profs = cls.load()
        if name not in profs:
            raise ValueError(f"Профиль '{name}' не найден")
        cls._active = profs[name]
        return cls._active

    @classmethod
    def create(cls, name="default", email=None):
        if name == "default":
            raise ValueError("Имя профиля 'default' зарезервировано")
        p = Profile(name=name, email=email)
        p.save()
        profs = cls.load()
        profs[name] = p
        cls._active = p
        return p
