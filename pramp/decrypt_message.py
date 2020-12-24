def decrypt(word):
    decoded_nums = []
    encoded_nums = [ord(c) for c in word]
    for i in range(len(word)):
        if i == 0:
            prev_num = 1
        else:
            prev_num = encoded_nums[i - 1]
        decoded_num = encoded_nums[i] - prev_num
        decoded_num_comp = ((decoded_num - ord("a")) % 26) + ord("a")
        decoded_nums.append(chr(decoded_num_comp))
    return "".join(decoded_nums)
