def BruteForce(text, pattern):
    for j in range(len(text)-len(pattern)+1):
        cnt = 0
        for i in range(len(pattern)):
            if text[i+j] != pattern[i]:
                break
            else: cnt += 1
        if cnt >= len(pattern):
            return j
    else:
        return -1
text = "TTTTAACCA"
pattern = "TTA"
print("{}".format(BruteForce(text,pattern)))
print(text.find(pattern))