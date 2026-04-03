# Calculator App

def main():
    print('Welcome to Calculator!')

def add(a, b):
    print(f"Adding {a} + {b}")  # <-- ЭТА НОВАЯ СТРОКА
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    main()