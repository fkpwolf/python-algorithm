import datetime

def validate(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%Y-%m-%d').strftime('%Y%m%d')
    except ValueError:
        return None

print(validate('2003-12-23'))
print(validate('2003-12-32'))