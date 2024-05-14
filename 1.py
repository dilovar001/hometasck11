def format_date(vremya):
    from datetime import datetime
    vremya=datetime.strptime(vremya,"%m/%d/%Y")
    vremya=datetime.strftime(vremya,"%Y%d%m")
    return vremya
date=input()
print(format_date(date))