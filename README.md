# Pythonで心理学実験・分析

心理学実験プログラム・分析スクリプトをPythonコードから作っていきます．

## 1. 目次

### 1.1. 導入

PythonとPsychoPyの基本的な使い方です．

* [1.1.0. Pythonとは](introduction/0.Pythonとは.ipynb)
* [1.1.1. Pythonの基本](introduction/1.Pythonの基本.ipynb)
* [1.1.2. 心理学実験のための知識](introduction/2.心理学実験のための知識.ipynb)
* [1.1.3. PsychoPyの主な機能](introduction/3.PsychoPyの主な機能.ipynb)

### 1.2. 実験

Stroop課題を作ります．

* [1.2.1. 実験の下書きを作る](experiment/draft.ipynb)
* [1.2.2. 実験プログラムを清書する](experiment/main.py)

### 1.3. 分析

Stroop課題の結果 (ダミー) を分析します．

* [1.3.1. 前処理](analysis/1.前処理.ipynb)
* [1.3.2. 1要因分析](analysis/2.一致不一致の分析.ipynb)
* [1.3.3. 2要因分析](analysis/3.色別の分析.ipynb)
* [1.3.4. Rとの連携](analysis/4.Rとの連携.ipynb)

### 1.4. Appendix

* [実験・分析でよく使う操作](appendix.ipynb)

## 2. インストールするもの

### 2.1. Anaconda

**[Anaconda](https://www.continuum.io/)**をインストールしておいてください．<br>
Anacondaとは分析環境が全て整ったPythonみたいなものです．<br>
(雑に言えばHAD付きExcelとか，PsychToolBox付きMatlabみたいなもの)．

実験作成と分析には，Anacondaについてくる**Jupyter Notebook**という開発環境を使います．<br>

なお，AnacondaはPython2版とPython3版があります．**Python2**版にしましょう．<br>
(本当はPython3版がおすすめですが，2系でなければPsychoPyが動きません)

* [Anaconda for Windows](https://www.continuum.io/downloads#windows)
* [Anaconda for Mac](https://www.continuum.io/downloads#osx)

### 2.2. 日本語フォント

チュートリアルでは日本語刺激呈示のために[IPAexフォント](http://ipafont.ipa.go.jp/node26#jp)を使います．次のようにしてインストールしましょう．

* ページ下段，"IPAexゴシック"のzipファイルをダウンロードしてください．
* 次に，zipを展開し，中の"ipaexg.ttf"にフォントパスを通してください．
  * Windows: ファイルを右クリックしたらインストールできます．
  * Mac: ファイルを~/Library/Fontsの中にコピペします．

また，このフォントを作図にも使いたい場合，以下のように設定します (分析はRで，という人は読み飛ばしてください)．

* 「Anaconda2」があるディレクトリに移動します．
* 「.matplotlib」というディレクトリに移動します (なければ作ってから入ります)．
* 「matplotlibrc」というファイルを作成し，「font.family : IPAexGothic」と書き保存します．

### 2.3. ANOVA君

Pythonでは分散分析ができません．したがってRを呼び出して[ANOVA君](http://riseki.php.xdomain.jp/index.php?ANOVA%E5%90%9B)を使うのが良いと思います．

## 3. Jupyter Notebookの設定

### 3.1. 動作確認

Jupyter Notebookを起動できるかどうか確認してください．

* Windowsなら，以下の2つのいずれかの方法で起動できます．
  1. スタートメニューの中の「Jupyter Notebook」をクリックします (環境によっては落ちるかも)．
  2. スタートメニューの中の「Anaconda Navigator」を開き，「Jupyter Notebook」をクリックします．
* Macなら，以下の2つのいずれかの方法で起動できます．
  1. ターミナルを開き，「jupyter notebook」を入力します (ターミナルが使える人はこっちを使ったほうが絶対楽です)．
  2. 「Anaconda Navigator」を開き，「Jupyter Notebook」をクリックします．

うまく起動すると，ブラウザが立ち上がり，以下のような画面が表示されます．

![起動画面](screenshot/img1.png)

なお，Jupyter Notebookはウイルスバスターに引っかかって起動しない場合があります．その場合，Anaconda2フォルダを監視の例外設定に追加してください．

### 3.2. 追加設定

WindowsユーザーはAnaconda Promptを起動してください．<br>
Macユーザーはターミナルを起動してください．

その後，以下を入力してください．

```
python -m ipykernel install --user
pip install pyglet pygame psychopy configobj
```

* 1行目はとりあえず，jupyter notebookを使えるようにする魔法の呪文ということで．気になる人は調べてみてください．
* pipはPythonのパッケージ管理ツールです．
* PsychoPyと一緒にインストールしたPygletとPygameは，PsychoPyが裏で動かしている描画ライブラリです．
* configobjはPsychoPyの一部のモジュールの使用に必要なので入れています．
* ここらへんのインストール方法は様々です．pipの代わりにcondaを使っても，また併用しても良いと思います．
* もし今後，プログラム実行時に`No module named '◯◯'`が表示された場合，大抵は`pip install ◯◯`で解決します．
  * `pip install`時の名前とインポート時の名前が異なる場合もありますが，ググればすぐに`pip install`すべきパッケージ名が分かるはずです．


## 4. Rとの連携

せっかくJupyterでRが使えるのでざっくり説明します ([参考](https://irkernel.github.io/installation/))

Rを開いて，以下を実行してください．ただし，実行前に後述の注意書きを読んで下さい．

```
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()
```

### 4.1. 注意点 (Windows)

1. https://cran.ism.ac.jp/ から「Download R for Windows」を開き，baseと**Rtoolsを**ダウンロードしインストールしておいてください．
2. Rは**管理者権限で開いてください**

### 4.2. 注意点 (Mac)

1. https://cran.ism.ac.jp/ から「Download R for Mac」を開き，最新のpkgをダウンロードしインストールしてください．
2. Rは**ターミナルから開いてください**，

うまくいけば，Jupyter Notebook右上「New」からRが選択できるようになっているハズです．

![起動画面](screenshot/img2.png)

## 5. ハマりどころ

### 呈示したウィンドウが「応答なし」になる

* 無視して良いです．ちゃんと刺激は呈示されます．

### 出力ファイルをExcelで開くと文字化けする

Excelは何故かShift-JISでファイルを開こうとします．以下のいずれかの方法で対策してください．

1. Excelは使わない．
2. `df.to_csv(filename, encoding='Shitf-JIS')`のように，ファイル出力時のエンコーディングを変える．
    * Excelで分析したいなら一番楽．
    * この対策をとった場合，RやPythonでcsvを読む際にエンコーディングを指定する必要がある．
3. Excelを開いて，`データ` -> `外部データの取り込み` -> `テキストファイル`で，UTF-8を選択して開く．

### 時間制御が不安

正確な時間制御が必要な場合，呈示時間ではなく呈示フレーム数で指定すれば良いです．例えば60Hzのディスプレイで，

```python
for i in range(6):
    something_to_draw.draw()
    win.flip()
```

は，

```python
win.flip()
core.wait(0.1)
```

と同じ (しかし正確な) 挙動になります．`win.flip()`は「次のフレームで，予め描画しておいた刺激を呈示する」ので，6回実行すると必ず6フレーム (= 100ms) 呈示になります．

### No module named ◯◯とエラーが出る

単にそのモジュールが入ってないだけです．`pip install ◯◯`で大抵解決します<br>

### UnicodeDecodeError

つらい．原因は色々です．よくあるのは，

* ログインユーザー名に全角文字が混じっている．
* ファイルパスに全角文字が混じっている．「`Desktop/experiments/実験1/main.py`」の場合もアウト．"実験1"を"exp1"等に修正しましょう．
* `from __future__ import unicode_liserals`してない．
