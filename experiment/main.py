
# coding: utf-8

# # Stroop課題を作ってみる
# まず，Jupyterでデバッグしながら作ってみます．完成したら「File」→「Download as」でpythonファイルとして吐き出し，好みでコメントを編集・削除して整形します．
# 
# ![実験の流れ](実験の流れ.png)

# ## 0. ライブラリのインポート

# In[1]:

from __future__ import division, unicode_literals, print_function
import itertools
import numpy as np
import pandas as pd
from psychopy import visual, core, event


# In[2]:

SUBJECT_ID = 1  # 被験者番号
N_REPEAT = 3  # 繰り返し数
UNIT = 30  # 視角1度の大きさ


# ## 1. 前準備
# ### 1.1. 出力データの作成

# In[3]:

conditions = list(itertools.product(('R', 'G', 'B'), ('赤', '緑', '青')))
df = pd.DataFrame(conditions, columns=['ink', 'text'])
df['subj']  = SUBJECT_ID
df['RT'] = 0
df['key'] = ''

# 繰り返し 
df = pd.concat([df for i in range(N_REPEAT)])

# 被験者IDをつけておく
df['subj'] = SUBJECT_ID

# ランダマイズ
randomized_index = np.random.permutation(len(df))
df = df.iloc[randomized_index, :]
df.reset_index(inplace=True, drop=True)


# ### 1.2. 実験刺激の作成

# In[4]:

# 事前準備
BLACK = [-1, -1, -1]
WHITE = [1, 1, 1]
RED = [1, -1, -1]
GREEN = [-1, 1, -1]
BLUE = [-1, -1, 1]


# In[5]:

# win = visual.Window(color=WHITE, units='pix')  # 下書き用
win = visual.Window(color=WHITE, units='pix', fullscr=True, allowGUI=False)  # 本番用


# In[6]:

# メッセージ
msg_ready = visual.TextStim(win, 'Ready?', color=BLACK, height=UNIT)
msg_gratitude = visual.TextStim(win, 'Thank you!', color=BLACK, height=UNIT)


# In[7]:

# 注視点
shape = [[-UNIT, 0], [UNIT, 0], [0, 0], [0, -UNIT], [0, UNIT], [0, 0]]
fixation = visual.ShapeStim(win, vertices=shape, lineWidth=3, lineColor=BLACK)


# In[8]:

# 文字刺激
stim = {
    ('R', '赤'): visual.TextStim(win, '赤', color=RED, height=2 * UNIT, font='ipaexgothic'),
    ('R', '緑'): visual.TextStim(win, '緑', color=RED, height=2 * UNIT, font='ipaexgothic'),
    ('R', '青'): visual.TextStim(win, '青', color=RED, height=2 * UNIT, font='ipaexgothic'),
    ('G', '赤'): visual.TextStim(win, '赤', color=GREEN, height=2 * UNIT, font='ipaexgothic'),
    ('G', '緑'): visual.TextStim(win, '緑', color=GREEN, height=2 * UNIT, font='ipaexgothic'),
    ('G', '青'): visual.TextStim(win, '青', color=GREEN, height=2 * UNIT, font='ipaexgothic'),
    ('B', '赤'): visual.TextStim(win, '赤', color=BLUE, height=2 * UNIT, font='ipaexgothic'),
    ('B', '緑'): visual.TextStim(win, '緑', color=BLUE, height=2 * UNIT, font='ipaexgothic'),
    ('B', '青'): visual.TextStim(win, '青', color=BLUE, height=2 * UNIT, font='ipaexgothic'),
}


# In[9]:

# ストップウォッチ
clock = core.Clock()


# ## 2. 実験ループ

# In[10]:

for index, values in df.iterrows():
    msg_ready.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fixation.draw()
    win.flip()
    core.wait(0.5)

    # 2.1. 刺激呈示
    stim[(values.ink, values.text)].draw()
    win.flip()

    # 2.2. 反応取得
    start = clock.getTime()
    keys = event.waitKeys(keyList=['j', 'k', 'l'])
    end = clock.getTime()

    # 2.3. 反応記録
    rt = (end - start) * 1000  # 反応時間 (in ms)
    key = keys[0]  # 反応キー
    df.loc[index, ['RT', 'key']] = [rt, key]


# In[11]:

# 終了処理
msg_gratitude.draw()
win.flip()
core.wait(3)
win.close()


# In[12]:

# 2.4. ファイル出力
filename = 'output/result{}.csv'.format(SUBJECT_ID)
df.to_csv(filename, encoding='utf-8')  # or shift-JIS for Excel


# ちゃんと動作することを「Kernel」→「Restart & Run All」で確認できたら，「File」→「Download as」→「Python (.py)」で保存します．
# 
# デフォルトのファイル名「draft.py」はちょっと名前が格好悪いので，適宜「main.py」等にリネームしてください．
# 
# 保存したファイルはPsychoPy (ソフトウェアのほう) から開けばすぐに実行できます．<br>
# あるいはAnacondaに同梱されているSpyderで実行しても良いし，以下のようにして，ターミナルやAnaconda Promptから直接実行しても良いです．
# 
# ```
# python main.py
# ```
