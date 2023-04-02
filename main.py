from acme.acme import ACME 
from decorators import decorator
import sys



if __name__ == "__main__":
    data = decorator.readData(sys.argv[1] if len(sys.argv) == 2 else "Error path")
    acme = ACME()
    acme.processData(data)
    for k,y in acme.moneyToPay.items():
        print(f"The amount to pay {k} is {y} USD")

