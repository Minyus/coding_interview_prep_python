def find_busiest_period(data):
    cumsum_at_prev = 0
    cumsum_at_prev_ts = 0
    prev_ts = 0
    highest_increase = 0
    busiest_ts = 0
    data.append([float("Inf"), 0, 0])
    for ts, num_ppl, flag in data:
        if ts != prev_ts:
            increase = cumsum_at_prev - cumsum_at_prev_ts
            if increase > highest_increase:
                highest_increase = increase
                busiest_ts = prev_ts
        if flag == 1:
            cumsum_at_prev += num_ppl
        if flag == 0:
            cumsum_at_prev -= num_ppl
        prev_ts = ts

    return busiest_ts


"""
input:  data = [ [1487799425, 14, 1], >> cumsum = 14
                 [1487799425, 4,  0], >> cumsum = 10
                 [1487799425, 2,  0], >> cumsum =  8 >> increase from prev timestamp: + 8
                 [1487800378, 10, 1], >> cumsum = 18 >> increase from prev timestamp: +10 >> highest increase
                 [1487801478, 18, 0], >> cumsum =  0
                 [1487801478, 18, 1], >> cumsum = 18 >> increase from prev timestamp: + 0
                 [1487901013, 1,  0], >> cumsum = 17 >> increase from prev timestamp: - 1
                 [1487901211, 7,  1], >> cumsum = 24
                 [1487901211, 7,  0] ]>> cumsum = 17 >> increase from prev timestamp: + 0
output: 1487800378 # since the increase in the number of people
                   # in the mall is the highest at that point
time complexity O(n)
space complexity O(1)
"""
