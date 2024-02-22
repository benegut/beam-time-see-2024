import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import datetime
import re

#tmpArr = []
#for root, dirs, files in os.walk("data/rw-dacs/2024-02-12/",topdown=True):
#    for name in files:
#        if name.endswith(("log")):
#            fullPath=os.path.join(root, name)
#            tmpArr.append(fullPath)
#
#print(tmpArr)

#selection=['data/rw-dacs/2024-02-12/single-reg-rw-0x46-20240212-17-02-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x42-20240212-16-26-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x40-20240212-16-56-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4d-20240212-16-37-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x45-20240212-16-29-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x41-20240212-16-57-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x40-20240212-16-24-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4e-20240212-16-38-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x43-20240212-16-27-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x44-20240212-17-00-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4a-20240212-16-34-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x47-20240212-17-03-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x48-20240212-17-04-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x43-20240212-16-59-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x48-20240212-16-32-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x45-20240212-17-01-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4c-20240212-17-08-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x47-20240212-16-31-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x49-20240212-17-05-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4b-20240212-16-35-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x44-20240212-16-28-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4c-20240212-16-36-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4d-20240212-17-09-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4a-20240212-17-06-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x46-20240212-16-30-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x49-20240212-16-33-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x42-20240213-09-22-43.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x42-20240212-16-58-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x41-20240212-16-25-46.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4b-20240212-17-07-55.log', 'data/rw-dacs/2024-02-12/single-reg-rw-0x4e-20240212-17-10-55.log']

selection=[
    'data/rw-dacs/2024-02-12/single-reg-rw-0x40-20240212-16-24-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x41-20240212-16-25-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x42-20240212-16-26-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x43-20240212-16-27-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x44-20240212-16-28-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x45-20240212-16-29-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x46-20240212-16-30-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x47-20240212-16-31-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x48-20240212-16-32-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x49-20240212-16-33-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x4a-20240212-16-34-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x4b-20240212-16-35-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x4c-20240212-16-36-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x4d-20240212-16-37-46.log',
    'data/rw-dacs/2024-02-12/single-reg-rw-0x4e-20240212-16-38-46.log'
]

namesArr=[]
for d in selection:
    namesArr.append(re.findall(r'0x[0-9A-F]+', d, re.I)[0])

dfArr=[]
for d in selection:
    dfArr.append(pd.read_csv(d,delimiter='\t',header=3,names=['Time', 'R/W', 'Register', 'Data', 'F/N']))

allFlipsArr=[]
for d in dfArr:
    allFlipsArr.append([1 if i == 'F' else 0 for i in d['F/N'].values])

num=len(allFlipsArr)
fig, ax = plt.subplots(num)
fig.suptitle('Observed bit-flips, DACs, F=flipped, N=not flipped', fontsize=16)

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

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.9)
plt.savefig('alldacs.png')
