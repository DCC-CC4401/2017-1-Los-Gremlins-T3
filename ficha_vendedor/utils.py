from datetime import datetime


def check_fixed_seller_active(start, end):
    now = datetime.now().time()
    if start <= end:
        return start <= now <= end
    else:
        return start <= now or now <= end


