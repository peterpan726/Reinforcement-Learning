import numpy as np
import matplotlib.pyplot as plt


# 宣告圖的大小與圖的名稱
fig = plt.figure(figsize=(5, 5))
ax = plt.gca()

# 繪製紅色牆壁
plt.plot([1, 1], [0, 1], color='red', linewidth=2)
plt.plot([1, 2], [2, 2], color='red', linewidth=2)
plt.plot([2, 2], [2, 1], color='red', linewidth=2)
plt.plot([2, 3], [1, 1], color='red', linewidth=2)

# 標示註解
plt.text(0.5, 2.5, 'S0', size=14, ha='center')
plt.text(1.5, 2.5, 'S1', size=14, ha='center')
plt.text(2.5, 2.5, 'S2', size=14, ha='center')
plt.text(0.5, 1.5, 'S3', size=14, ha='center')
plt.text(1.5, 1.5, 'S4', size=14, ha='center')
plt.text(2.5, 1.5, 'S5', size=14, ha='center')
plt.text(0.5, 0.5, 'S6', size=14, ha='center')
plt.text(1.5, 0.5, 'S7', size=14, ha='center')
plt.text(2.5, 0.5, 'S8', size=14, ha='center')
plt.text(0.5, 2.3, 'START', ha='center')
plt.text(2.5, 0.3, 'GOAL', ha='center')

# 設定繪圖範圍與塗鴉刻度
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 在 S0 繪製綠色圖形
line, = ax.plot([0.5], [2.5], marker="o", color='g', markersize=60)
# plt.show()

# 設定一開始的策略 theta_0
theta_0 = np.array([[np.nan, 1, 1, np.nan],  # s0
                    [np.nan, 1, np.nan, 1],  # s1
                    [np.nan, np.nan, 1, 1],  # s2
                    [1, 1, 1, np.nan],  # s3
                    [np.nan, np.nan, 1, 1],  # s4
                    [1, np.nan, np.nan, np.nan],  # s5
                    [1, np.nan, np.nan, np.nan],  # s6
                    [1, 1, np.nan, np.nan],  # s7、s8 is a terminal so don't need any policy
                    ])

#------- The function for transfer the theta action pi -------#
def simple_convert_into_pi_from_theta(theta):
    '''Simply calcaulate the poportion'''

    [m, n] = theta.shape  # Get the size of theta's martrix
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # calculate the poportion

    pi = np.nan_to_num(pi)  # transfer nan to 0
    
    return pi

pi_0 = simple_convert_into_pi_from_theta(theta_0)

# print(theta_0)
# print(pi_0)

# 自訂計算 1 step 移動後的狀態s函數
def get_next_s(pi, s):
    direction = ['up', 'right', 'down', 'left']
    next_direction = np.random.choice(a=direction, p = pi[s, :], replace=False) # 根據pi[s, :] 的機率，選擇動作
    if next_direction == 'up':
        score = s - 3
    elif next_direction == 'right':
        score = s + 1
    elif next_direction == 'down':
        score = s + 3 
    elif next_direction == 'left':
        score = s - 1
    return score

# 自訂agent不斷在迷宮裡移動，直到抵達終點為止
def goal_maze(pi):
    s = 0 #start state
    state_history = [0]

    while (1): # Keep move until reach goal
        next_s = get_next_s(pi, s)
        state_history.append(next_s) # Record the history move

        if next_s == 8: # If reach goal then break
             break
        else:
            s = next_s
    return state_history

state_history = goal_maze(pi_0)
print(state_history)
print("走出迷宮的總步數為" + str(len(state_history) - 1))







