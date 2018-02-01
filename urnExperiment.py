import random
import seaborn as sns
import matplotlib.pyplot as plt


def run_one_exp(ntrials, num_to_add, num_w_start, num_b_start):
    num_white = num_w_start
    num_black = num_b_start
    for i in range(ntrials):
        if random.random() < (num_white/(num_white+num_black)):
            num_white += num_to_add
        else:
            num_black += num_to_add
    return num_white/(num_white+num_black)


def run_full_exp(ntimes, ntrials, num_to_add, num_w_start, num_b_start):
    data = []
    for i in range(ntimes):
        data.append(run_one_exp(ntrials, num_to_add, num_w_start, num_b_start))

    return data


ratios = run_full_exp(10000, 500, 1, 1, 1)
sns.set_style('whitegrid')
sns.distplot(ratios, bins=75, kde=False, rug=True)
plt.show()