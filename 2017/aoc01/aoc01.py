with open('input.txt') as f:
    captcha = f.readline()

#captcha = '12131415'
bucket = 0
half_distance = 1

for i in range(-half_distance, len(captcha)-half_distance):
    if captcha[i] == captcha[i + half_distance]:
        bucket += int(captcha[i])

print(bucket)

bucket = 0
half_distance = len(captcha) // 2

for i in range(-half_distance, len(captcha)-half_distance):
    if captcha[i] == captcha[i + half_distance]:
        bucket += int(captcha[i])

print(bucket)
