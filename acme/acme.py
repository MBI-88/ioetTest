from datetime import datetime
from .datastruct import payKeys


class ACME():
    def __init__(self) -> None:
        self.moneyToPay:dict[str,int] = {}
    
    def handlerData(self,payRange:list,name:str,start:datetime,end:datetime) -> None:
        """
            This method saves information about workers.
        """
        try:
            for i in range(len(payRange)):
                if start >= payRange[i][0] and start > payRange[i][1]:
                        continue
                else:
                    if start >= payRange[i][0] and start <= payRange[i][1] and end <= payRange[i][1]:
                        hours = end.hour - start.hour
                        hours = abs(hours)
                        self.moneyToPay[name] += hours * payRange[i][2]
                    elif start >= payRange[i][0] and start <= payRange[i][1] and end > payRange[i][1]:
                        hours = payRange[i][1].hour - start.hour
                        hours = hours if hours != 0 else 1
                        hours = abs(hours)
                        self.moneyToPay[name] += hours * payRange[i][2]
                        for x in range(len(payRange[i+1:])):
                            if end >= payRange[x][0] and end <= payRange[x][1]:
                                hours = end.hour - payRange[x][0].hour
                                hours = hours if hours != 0 else 1
                                hours = abs(hours)
                                self.moneyToPay[name] += hours * \
                                                    payRange[x][2]
                            else:
                                hours = payRange[x][1].hour - payRange[x][0].hour
                                hours = abs(hours)
                                self.moneyToPay[name] += hours * payRange[x][2]
        except TypeError | ValueError as f:
            print(f"Error data {f}")
            exit(1)
            
    def processData(self,data_employee:list[str]) -> None:
          """
            This method return the payments for employees.\n
            The file must have this structure NAME=MO00:01-09:00,TU02:00-03:00,...\n
            MO: Monday\n
            TU: Tuesday\n
            WE: Wednesday\n
            TH: Thursday\n
            FR: Friday\n
            SA: Saturday\n
            SU: Sunday\n
          """
          for value in data_employee:
            try:
                name, data = value.split("=")[0], value.split("=")[1].split(",")
                self.moneyToPay[name] = 0
                for dt in data:
                    day = dt[0:2]
                    timeRange = dt[2:].split("-")
                    start = datetime.strptime(timeRange[0], "%H:%M").time()
                    end = datetime.strptime(timeRange[1], "%H:%M").time()
                    match day:
                        case "MO" | "TU" | "WE" | "TH" | "FR":
                            payRange = payKeys["Week"]
                            self.handlerData(payRange,name,start,end)

                        case "SA" | "SU":
                            payRange = payKeys["Weekend"]
                            self.handlerData(payRange,name,start,end)
                        case _:
                            continue
            except ValueError as f:
                print(f"Error data {f}")
                exit(1)
 
                    
            
    
        