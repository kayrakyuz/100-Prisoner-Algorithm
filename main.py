import random

trial_count = 10000
count = 0
prisoner_count = 100

for n in range(trial_count):
    success = 0
    random_list = list(range(100))
    random.shuffle(random_list)
    for i in range(prisoner_count):
        number_of_person = i
        box = random_list[number_of_person]
        if box != number_of_person:
            for j in range(49):
                box = random_list[box]
                if box == number_of_person:
                    success += 1
                    break
                else:
                    continue
        else:
            success += 1
    # print("success count", success)
    if success == 100:
        count += 1

print(count / trial_count)