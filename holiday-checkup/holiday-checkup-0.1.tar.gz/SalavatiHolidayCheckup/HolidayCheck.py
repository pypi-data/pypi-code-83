from hijri_converter import convert
import jdatetime


class HolidayCheck:
    def __init__(self):
        self.lst_weekend_holidays = ['Fri']
        self.lst_iran_holidays = [
                {'month':1,'day':1,'comment':"norooz"},
                {'month':1,'day':2,'comment':"norooz"},
                {'month':1,'day':3,'comment':"norooz"},
                {'month':1,'day':4,'comment':"norooz"},
                {'month':1,'day':12,'comment':"islamic republic of iran day "},
                {'month':1,'day':13,'comment':"nature day"},
                {'month':3,'day':14,'comment':"death of mr.khomeini"},
                {'month':3,'day':15,'comment':"ghiam 15 khordad"},
                {'month':10,'day':22,'comment':"iranian revolution - 1357"},
                {'month':12,'day':29,'comment':"melli shodan naft"},
                ]
        self.lst_islam_holidays = [
                {'month':1,'day':9,'comment':"tasooa"},
                {'month':1,'day':10,'comment':"ashoora"},
                {'month':2,'day':20,'comment':"arbaeen"},
                {'month':2,'day':28,'comment':"death of prophet & imam hassan"},
                {'month':1,'day':29,'comment':"death of imam reza"},
                {'month':1,'day':39,'comment':"death of imam reza"},
                {'month':3,'day':8,'comment':"death of Imam hassan askari"},
                {'month':3,'day':17,'comment':"birth of prophet & Imam sadegh"},
                {'month':6,'day':3,'comment':"death of mis.zahra as"},
                {'month':7,'day':13,'comment':"birth of Imam ali"},
                {'month':7,'day':27,'comment':"mabas"},
                {'month':8,'day':15,'comment':"birth of imam zaman "},
                {'month':9,'day':21,'comment':"death of imam ali"},
                {'month':10,'day':1,'comment':"eid fetr"},
                {'month':10,'day':2,'comment':"eid fetr"},
                {'month':10,'day':25,'comment':"death of imam sadegh"},
                {'month':12,'day':10,'comment':"eid ghorban"},
                {'month':12,'day':18,'comment':"eid ghadir"},
                ]
        
        
    def get_holiday_status_of_datetime(self,specific_datatime):
        day_holiday_status = {}

        # Check the day could be weekend holiday or not.
        # input : gregorian date
        s_day = jdatetime.date.fromgregorian(date=specific_datatime).strftime("%a")
        # print(s_day)
        f_weekend_holidayflagbit= 0
        if s_day in self.lst_weekend_holidays:
            f_weekend_holidayflagbit=1
            day_holiday_status['weekend_status']={'status':True,'comment':'it is %s and is in the iran\'s weekend list'%s_day}
            print('it is iranian weekend holiday')
        else:
            day_holiday_status['weekend_status']={'status':False,'comment':'it is %s and is a normal day in iran'%s_day}
            # print('normal day of iranian\'s weekend holidays')
        #===============================================================================
        # Check the day could be iran holiday or not.
        # input : gregorian date
        our_jdate = jdatetime.date.fromgregorian(date=specific_datatime)
        n_month = our_jdate.month
        n_day = our_jdate.day
        f_iran_holidayflagbit = 0
        for hday in self.lst_iran_holidays:
            if hday['month']==n_month and hday['day']==n_day:
                f_iran_holidayflagbit=f_iran_holidayflagbit+1
                day_holiday_status['official_iran_holiday_status']={'status':True,'comment':'it is %s and is in the iran\'s official holiday list'%hday['comment']}
                # print('it is iranian\'official holiday',hday['comment'])
        if 'official_iran_holiday_status' not in day_holiday_status:
            day_holiday_status['official_iran_holiday_status'] = {'status':False,'comment':'it is %s and is in the iran\'s official holiday list'%hday['comment']}
        #===============================================================================
        # Check the day could be islam holiday or not.
        # input : gregorian date
        our_jdate = convert.Gregorian(specific_datatime.year,specific_datatime.month,specific_datatime.day).to_hijri()
        n_month = our_jdate.month
        n_day = our_jdate.day
        f_islam_holidayflagbit = 0
        for hday in self.lst_islam_holidays:
            if hday['month']==n_month and hday['day']==n_day:
                f_islam_holidayflagbit=f_islam_holidayflagbit+1
                day_holiday_status['official_islam_holiday_status']={'status':True,'comment':'it is %s and is in the islam\'s official holiday list'%hday['comment']}
                # print('it is islamic holiday',hday['comment'])
        if 'official_islam_holiday_status' not in day_holiday_status:
            day_holiday_status['official_islam_holiday_status'] = {'status':False,'comment':'it is %s and is in the islam\'s official holiday list'%hday['comment']}

        return day_holiday_status
