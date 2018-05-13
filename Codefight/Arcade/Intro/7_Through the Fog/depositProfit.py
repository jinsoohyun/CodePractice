def depositProfit(deposit, rate, threshold):
    cnt = 0
    while deposit < threshold:
        deposit*=(1+(rate)/100.0)
        cnt += 1
        #print deposit
    return cnt



deposit = 100
rate = 20
threshold = 170
print depositProfit(deposit, rate, threshold)

