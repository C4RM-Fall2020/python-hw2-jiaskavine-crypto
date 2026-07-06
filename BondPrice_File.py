import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    periods = np.arange(1, n + 1)

    coupon = face * couponRate / ppy
    discount = (1 + y / ppy) ** periods

    coupon_pv = np.sum(coupon / discount)
    face_pv = face / ((1 + y / ppy) ** n)

    return coupon_pv + face_pv
