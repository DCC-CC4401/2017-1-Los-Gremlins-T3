from datetime import datetime

actual_hour = datetime.now().hour
actual_minute = datetime.now().minute
now = datetime.strptime(str(actual_hour) + ':' + str(actual_minute), '%H:%M').time()

def check_fixed_seller_active(start, end):
    start = datetime.strptime(start, '%H:%M').time()
    end = datetime.strptime(end, '%H:%M').time()
    if start <= end:
        return start <= now <= end
    else:
        return start <= now or now <= end

print (check_fixed_seller_active('11:00', '12:00'))
print (check_fixed_seller_active('12:30', '21:30'))
