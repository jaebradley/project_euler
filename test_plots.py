__author__ = 'jaebradley'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


u_cols = ['placement_id', 'year', 'month', 'day', 'timestamp', 'hour (UTC)', 'action_rate']
pre = pd.read_csv('prelaunch.csv', sep='\t', names=u_cols)

u_cols = ['placement_id', 'year', 'month', 'day', 'timestamp', 'hour (UTC)', 'action_rate']
post = pd.read_csv('postlaunch.csv', sep='\t', names=u_cols)


# Two subplots, unpack the axes array immediately
plt.figure()


# plt.scatter( (pre['hour (UTC)']-7) % 24, pre['action_rate'], c='b')
# plt.scatter( (post['hour (UTC)']-7) % 24, post['action_rate'], c='r')



f, axarr = plt.subplots(2, sharex=True)
s1 = axarr[0].scatter( (pre['hour (UTC)']-7) % 24, pre['action_rate'], c='b')
axarr[0].set_ylabel('Registration Rate',fontsize = 10)
axarr[0].set_xlabel('Time of Day (Pacific)',fontsize = 10)
s2 = axarr[1].scatter( (post['hour (UTC)']-7) % 24, post['action_rate'], c='r')
axarr[1].set_ylabel('Registration Rate',fontsize = 10)
axarr[1].set_xlabel('Time of Day (Pacific)',fontsize = 10)
plt.legend((s1, s2),('Pre-launch', 'Post-launch'))
plt.show()