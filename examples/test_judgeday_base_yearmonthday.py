#coding=utf-8

class test_judgeday_base_yearmonthday:
    year=""
    month=""
    day=""
    actoryDay=""

    def years(self):
        print("请输入年份:")
        ye=input()
        if ye.isdigit():
            if int(ye)%4==0:
                return 0
            else:
                return 1
        else:
            print("年份不对，请输入正确的年份")
            alls=test_judgeday_base_yearmonthday()
            alls.years()

    def months(self):
        print("请输入月份")
        t=input()
        if t.isdigit():
            mon = int(t)
            while mon<=0 or mon>12:
                print("请重新输入月份")
                t=input()
                mon=int(t)
                if mon<=12 and mon>0:
                    break
            mon_lists=[0,31,59,90,120,151,181,212,243,273,304,334,365]
            return mon_lists[mon-1]
        else:
            m=test_judgeday_base_yearmonthday()
            m.months()

    def days(self):
        really_day=test_judgeday_base_yearmonthday()
        year=really_day.years()
        month=really_day.months()
        print("请输入天数")
        day=input()
        if day.isdigit():
            intday=int(day)
            while intday>31 or intday<=0:
                print("请重新输入天数")
                day=input()
                intday=int(day)
                if intday<=31 and intday>0:
                    break
            print("这是一年的第 X 天")
            return year+month+intday
        else:
            print("请重新输入天数")
            ju=test_judgeday_base_yearmonthday()
            ju.days()

if __name__=='__main__':
    ju=test_judgeday_base_yearmonthday()
    print(ju.days())