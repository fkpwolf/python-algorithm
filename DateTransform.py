import datetime
def validate(date_str):
    for fmt in ('%Y/%m/%d', '%d/%m/%Y', '%m-%d-%Y'):
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    return None

def validate2(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y/%m/%d')
    except ValueError:
        try:
            return datetime.datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            try:
                return datetime.datetime.strptime(date_str, '%m-%d-%Y')
            except ValueError:
                return None

        
class DateTransform:
    
    @staticmethod
    def change_date_format(dates):
        valid_dates = []
        for date in dates:
            print('will validate ', date)
            valid_date = validate(date)
            if valid_date:
                valid_dates.append(valid_date.strftime('%Y%m%d'))
        return valid_dates

dates = DateTransform.change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"])
print(*dates, sep='\n')