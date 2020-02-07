def print_hello():
     print("Hello from app")

def second_print_hello():
     print("test second")

#the global variable __name__, in the app module and compare it with __main__ at the entry point
if __name__ == "__main__":
     second_print_hello()
     print_hello()