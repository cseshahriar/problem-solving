T = int(input())
for i in range(T):
    data = list(map(int, input().split()))
    opponent_total_run = data[0]
    win_run = opponent_total_run + 1
    side_current_run = data[1]
    left_ball = data[2]
    current_played_ball = 300 - left_ball
    current_played_over = current_played_ball / 6
    current_run_rate = side_current_run / current_played_over
    left_over = left_ball / 6
    left_run = win_run - side_current_run
    side_run_rate = left_run / left_over
    print("%.2f %.2f" % (current_run_rate, side_run_rate))