class UK:

    def __init__(self):
        pass

    def capital(self):
        return "London"

    def language(self):
        return "English"

    def currency(self):
        return "Pound"

    def type(self):
        return "Developed"

class USA:
    def __init__(self):
        pass

    def capital(self):
        return "Washington, D.C."

    def language(self):
        return "English"

    def currency(self):
        return "Dollar"

    def type(self):
        return "Developed"

class India:

    def __init__(self):
        pass

    def capital(self):
        return "New Delhi"

    def language(self):
        return "Hindi"

    def currency(self):
        return "Rupee"

    def type(self):
        return "Developing"

class Australia:

    def __init__(self):
        pass

    def capital(self):
        return "Canberra"

    def language(self):
        return "English"

    def currency(self):
        return "Australian Dollar"

    def type(self):
        return "Developed"

obj_uk = UK()
obj_usa = USA()
obj_india = India()
obj_australia = Australia()

for country in (obj_uk, obj_usa, obj_india, obj_australia):
    print(f"Country: {country.__class__.__name__}")
    print(f"Capital: {country.capital()}")
    print(f"Language: {country.language()}")
    print(f"Currency: {country.currency()}")
    print(f"Type: {country.type()}")
    print()