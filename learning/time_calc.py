import math as mt
'''
 t1 = Time(21, 55, 23)
 t2 = Time(22, 43, 23)

 add two times , t1 + t2
 sub two times = t2 - t1
'''

class Time:
    def __init__(self,hr,mi,se) -> None:
        self.hr=hr
        self.min=mi
        self.sec=se
    
    def __str__(self) -> str:
        return f'Time : {self.hr}:{self.min}:{self.sec}'

    def __add__(self,others):
        hr,min,sec=self.hr+others.hr,self.min+others.min,self.sec+others.sec
        if sec > 60:
            min += sec/60
            sec = sec%60
        if min > 60:
            hr += min/60
            min = min%60   
        return Time(mt.floor(hr),mt.floor(min),mt.floor(sec))
    
    def __lt__ (self,other) -> bool:
        if self.hr < other.hr:
            return True
        elif self.hr == other.hr:
            if self.min < other.min:
                return True
            elif self.min == other.hr:
                if self.sec < self.hr:
                    return True
        return False
    
    def __eq__(self, others) -> bool:
        return self.hr == others.hr and self.min == others.min and self.sec == others.sec
            
    def __sub__(self,others):
        if self < others or self == others:
            hr = others.hr-self.hr
            min = others.min-self.min
            sec = others.sec-self.sec
        else:
            hr = self.hr-others.hr
            min = self.min-others.min
            sec = self.sec-others.sec
        return Time(hr,min,sec)

       
def main():
    t1 = Time(6,35,35)
    t2 = Time(8,35,35)
    t3 = t1 - t2

    print(t3)


if __name__ == '__main__':
    main()