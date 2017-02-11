# coding: utf-8

from __future__ import division, unicode_literals, print_function
import numpy as np
import pandas as pd
from psychopy import visual, core, event

SUBJECT_ID = 1  # 被験者番号
N_REPEAT = 3  # 繰り返し数
UNIT = 30  # 視角1度の大きさ

index = pd.MultiIndex.from_product([['R', 'G', 'B'], ['赤', '緑', '青']],
                                   names=['ink', 'text'])
columns = ['subj', 'RT']
df = pd.DataFrame(0, index=index, columns=columns)
df = pd.concat([df for i in range(N_REPEAT)])
df['subj'] = SUBJECT_ID
randomized_index = np.random.permutation(len(df))
df = df.iloc[randomized_index, :]

win = visual.Window(color=[1, 1, 1], units='pix', fullscr=True, allowGUI=False)

black = [-1, -1, -1]
red = [1, -1, -1]
green = [-1, 1, -1]
blue = [-1, -1, 1]

msg_ready = visual.TextStim(win, 'Ready?', color=black, height=UNIT)
msg_gratitude = visual.TextStim(win, 'Thank you!', color=black, height=UNIT)
shape = [[-UNIT, 0], [UNIT, 0], [0, 0], [0, -UNIT], [0, UNIT], [0, 0]]
fixation = visual.ShapeStim(win, vertices=shape, lineWidth=3, lineColor=black)
stim = {
    ('R', '赤'): visual.TextStim(
        win, '赤', color=red, height=2 * UNIT, font='ipaexgothic'),
    ('R', '緑'): visual.TextStim(
        win, '緑', color=red, height=2 * UNIT, font='ipaexgothic'),
    ('R', '青'): visual.TextStim(
        win, '青', color=red, height=2 * UNIT, font='ipaexgothic'),
    ('G', '赤'): visual.TextStim(
        win, '赤', color=green, height=2 * UNIT, font='ipaexgothic'),
    ('G', '緑'): visual.TextStim(
        win, '緑', color=green, height=2 * UNIT, font='ipaexgothic'),
    ('G', '青'): visual.TextStim(
        win, '青', color=green, height=2 * UNIT, font='ipaexgothic'),
    ('B', '赤'): visual.TextStim(
        win, '赤', color=blue, height=2 * UNIT, font='ipaexgothic'),
    ('B', '緑'): visual.TextStim(
        win, '緑', color=blue, height=2 * UNIT, font='ipaexgothic'),
    ('B', '青'): visual.TextStim(
        win, '青', color=blue, height=2 * UNIT, font='ipaexgothic'),
}
clock = core.Clock()

for cond, value in df.iterrows():
    msg_ready.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fixation.draw()
    win.flip()
    core.wait(0.5)

    stim[cond].draw()
    win.flip()

    start = clock.getTime()
    keys = event.waitKeys(keyList=['j', 'k', 'l'])
    end = clock.getTime()

    rt = (end - start) * 1000  # in ms
    value['RT'] = rt

msg_gratitude.draw()
win.flip()
core.wait(3)
win.close()

filename = 'output/result' + str(SUBJECT_ID) + '.csv'
df.to_csv(filename, encoding='utf-8')
