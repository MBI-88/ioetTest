"""
payKeys: dict[str, list[tuple[datetime, datetime, int]]] = {
    "Week": [
        (datetime.strptime("00:01", "%H:%M").time(),
         datetime.strptime("09:00", "%H:%M").time(), 25),  
        (datetime.strptime("09:01", "%H:%M").time(),
         datetime.strptime("18:00", "%H:%M").time(), 15),
        (datetime.strptime("18:01", "%H:%M").time(),
         datetime.strptime("23:00", "%H:%M").time(), 20),
    ],
    "Weekend": [
        (datetime.strptime("00:01", "%H:%M").time(),
         datetime.strptime("09:00", "%H:%M").time(), 30),
        (datetime.strptime("09:01", "%H:%M").time(),
         datetime.strptime("18:00", "%H:%M").time(), 20),
        (datetime.strptime("18:01", "%H:%M").time(),
         datetime.strptime("23:00", "%H:%M").time(), 25),
    ]
}
def process_data(data_employee: list) -> dict[str,int]:
    resultTopay = {}
    for value in data_employee:
        name, data = value.split("=")[0], value.split("=")[1].split(",")
        resultTopay[name] = 0
        for dt in data:
            day = dt[0:2]
            timeRange = dt[2:].split("-")
            start = datetime.strptime(timeRange[0], "%H:%M").time()
            end = datetime.strptime(timeRange[1], "%H:%M").time()

            match day:
                case "MO" | "TU" | "WE" | "TH" | "FR":
                    payRange = payKeys["Week"]
                    # Funcion para estetica  10:00-12:00
                    for i in range(len(payRange)):
                        # out side of range
                        if start >= payRange[i][0] and start > payRange[i][1]:
                            continue
                        else:
                            # range worker into the range payments
                            if start >= payRange[i][0] and start <= payRange[i][1] and end <= payRange[i][1]:
                                hours = end.hour - start.hour
                                resultTopay[name] += hours * payRange[i][2]

                            # middle range worker into the range payments
                            elif start >= payRange[i][0] and start <= payRange[i][1] and end > payRange[i][1]:
                                hours = payRange[i][1].hour - start.hour
                                hours = hours if hours != 0 else 1
                                resultTopay[name] += hours * payRange[i][2]

                                for x in range(len(payRange[i+1:])):
                                    if end >= payRange[x][0] and end <= payRange[x][1]:
                                        hours = end.hour - payRange[x][0].hour
                                        hours = hours if hours != 0 else 1
                                        resultTopay[name] += hours * \
                                            payRange[x][2]
                                    else:
                                        hours = payRange[x][1].hour - \
                                            payRange[x][0].hour
                                        resultTopay[name] += hours * \
                                            payRange[x][2]

                case "SA" | "SU":
                    payRange = payKeys["Weekend"]
                    # Funcion para estetica
                    for i in range(len(payRange)):
                        # out side of range
                        if start >= payRange[i][0] and start > payRange[i][1]:
                            continue
                        else:
                            # range worker into the range payments
                            if start >= payRange[i][0] and start <= payRange[i][1] and end <= payRange[i][1]:
                                hours = end.hour - start.hour
                                resultTopay[name] += hours * payRange[i][2]

                            # middle range worker into the range payments
                            elif start >= payRange[i][0] and start <= payRange[i][1] and end > payRange[i][1]:
                                hours = payRange[i][1].hour - start.hour
                                hours = hours if hours != 0 else 1
                                resultTopay[name] += hours * payRange[i][2]

                                for x in range(len(payRange[i+1:])):
                                    if end >= payRange[x][0] and end <= payRange[x][1]:
                                        hours = end.hour - payRange[x][0].hour
                                        hours = hours if hours != 0 else 1
                                        resultTopay[name] += hours * \
                                            payRange[x][2]
                                    else:
                                        hours = payRange[x][1].hour - \
                                            payRange[x][0].hour
                                        resultTopay[name] += hours * \
                                            payRange[x][2]


                case _:
                    continue
    return resultTopay
"""
from acme.acme import ACME 
import re,os,sys


pathRe = re.compile(r'\.txt$')

def cleanData(f) -> object:
    """
        This decorator is for checking the path.
    """
    def wrapper(args:str) -> object:
        if pathRe.search(args) and os.path.isfile(args):
            return f(args)
        else:
            print("Error file")
            exit(1)
    return wrapper


@cleanData
def readData(path:str) -> list:
    """
    This function read a file .txt and return\n
    an array of data.
    """
    data:list[str] = []
    data_employee:list[str] = []
    with open(path,'r') as file:
        data = file.readlines()
    file.close()
    for dt in data:
        data_employee.append(dt.replace("\n",""))
    return data_employee


if __name__ == "__main__":
    data = readData(sys.argv[1] if len(sys.argv) == 2 else "Error path")
    acme = ACME()
    acme.proccessData(data)
    for k,y in acme.moneyToPay.items():
        print(f"The amount to pay {k} is {y} USD")

