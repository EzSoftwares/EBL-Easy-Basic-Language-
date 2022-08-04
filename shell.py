import ebl_interpreter
print("Welcome to EBL Copyright 2022 By Adnan and Youssef")

while True:
    text = input('EBL > ')
    if text.strip() == "": continue
    result, error = ebl_interpreter.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
