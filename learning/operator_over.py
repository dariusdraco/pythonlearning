class pocket_money:
    def __init__(self,bal=0) -> float:
        self.bal = bal
    def __str__(self) -> str:
        return f'pocket money : {self.bal}'
    
    def __add__(self,other) -> float:
        return self.bal + other.get_bal()
       
    def __sub__(self,other) -> float:
        return self.bal - other.get_bal()
    
    def __lt__(self, other) -> bool:
        return self.bal < other.bal

    def __gt__(self,other) -> bool:
        return self.bal > other.bal

    def __le__(self,other) -> bool:
        pass
    
    def __ge__(self, other) -> bool:
        pass

    def __eq__(self, other) -> bool:
        pass
     
    def get_bal(self)->float:
        return self.bal


def main():
    dar_pm = pocket_money(50)
    chi_pm = pocket_money(51)
    #tot = dar_pm.get_bal() + chi_pm.get_bal()
    #print(f'total pocket money : {tot}')
    total_pm = dar_pm + chi_pm
    diff_pm = chi_pm - dar_pm

if __name__ == "__main__":
    main()