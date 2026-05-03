try:
    from ddgs import DDGS
    with DDGS() as ddgs:
        response = ddgs.chat("Hello")
        print("DDGS:", response)
except Exception as e:
    print("Error:", e)
