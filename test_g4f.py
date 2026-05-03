import g4f

try:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello"}],
        provider=g4f.Provider.Blackbox
    )
    print("Blackbox:", response)
except Exception as e:
    print("Blackbox Error:", e)

try:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello"}],
        provider=g4f.Provider.You
    )
    print("You:", response)
except Exception as e:
    print("You Error:", e)
