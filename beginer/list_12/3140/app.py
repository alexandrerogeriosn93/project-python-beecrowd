while True:
    try:
        entry = input()
        
        if "<body>" in entry:
            while True:
                text = input()
                
                if "</body>" in text:
                    break
                
                print(text)
    except EOFError:
        break
