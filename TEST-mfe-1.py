import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import datetime
import re

#tmpArr = []
#for root, dirs, files in os.walk("data/rw-mfe/2024-02-12/",topdown=True):
#    for name in files:
#        if name.endswith(("log")):
#            fullPath=os.path.join(root, name)
#            tmpArr.append(fullPath)
#
#print(tmpArr)

#selection=['data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-41-35.log', 'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-21-08-33.log', 'data/rw-mfe/2024-02-12/single-reg-rw-mfe-0x8000-20240212-19-03-46.log', 'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-12-27.log', 'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-18-59.log', 'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-55-13.log']

selection=[
    'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-12-27.log',
    'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-18-59.log',
    'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-41-35.log',
    'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-20-55-13.log'
    'data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-21-08-33.log',
]


name='data/rw-mfe/2024-02-12/single-reg-rw-mfe-20240212-21-08-33.log'

df=pd.read_csv(name,delimiter='\t',header=3,names=['Time', 'R/W', 'Register', 'Data', 'F/N'])

namesArr=[
    '0x8000',
    '0x8001',
    '0x8400',
    '0x8401'
]

allFlipsArr=[]
for r in namesArr:
    allFlipsArr.append([1 if i == 'F' else 0 for i in [df['F/N'][i] for i in range(len(df['F/N'])) if df['Register'][i] == r]])

# logTimes = dataFrame['Time'].values
# formatedTimes=[datetime.datetime.strptime(i, '%Y-%m-%d-%H-%M-%S-%f').strftime('%H:%M:%S.%f') for i in logTimes]
# tickSpace = int(len(formatedTimes)/14)
# plotTicks = [formatedTimes[i] for i in range(0,len(formatedTimes),tickSpace)]
# plotTicksInt = [i for i in range(0,len(formatedTimes),tickSpace)]

num=len(allFlipsArr)
fig, ax = plt.subplots(num)
fig.suptitle('Observed bit-flips, MFEs, F=flipped, N=not flipped', fontsize=16)

for i in range(num):
    ax[i].plot(allFlipsArr[i],linewidth=3.0)
    ax[i].set_ylabel(namesArr[i], rotation=0, fontsize=10, labelpad=20, va='center')
    ax[i].set_ylim(0,1)
    ax[i].set_yticks([0, 1], ['N', 'F'])
    # if i != num-1:
    #     ax[i].set_yticklabels([])
    if i != num-1:
        ax[i].set_xticks([])
    if i == num-1:
        ax[i].set_xlabel('# of reads', rotation=0, fontsize=10, labelpad=10, va='center')
    ax[i].spines['top'].set_visible(False)
    ax[i].spines['right'].set_visible(False)
    ax[i].spines['bottom'].set_visible(False)
    #ax[i].tick_params(axis='x', labelrotation=45, labelsize=10)
    #ax[i].set_xticks(plotTicksInt, plotTicks)

#plt.tight_layout(pad=.5)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.9)
plt.savefig('allmfes.png')
