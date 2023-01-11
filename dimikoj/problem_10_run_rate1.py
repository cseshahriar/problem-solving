T = int(input())
current_run_rate, required_run_rate = 0.00, 0.00

for i in range(T):
    data = list(map(int, input().split()))
    current_run_rate = data[1] / ((300-data[2])/6)
    if data[0] < data[1]:
        required_run_rate = 0
    else:
        required_run_rate = (data[0]-data[1]+1) / (data[2]/6)
    print("%.2f %.2f" % (current_run_rate, required_run_rate))
