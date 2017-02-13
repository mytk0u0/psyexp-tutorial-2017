# Pythonで心理学実験・分析

## 1. 目次

(リンク先はPCから開かないとうまく表示されません)

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

## 2. インストールするもの

### 2.1. 当日まで

**[Anaconda](https://www.continuum.io/)**をインストールしておいてください．<br>
Anacondaとは分析環境が全て整ったPythonみたいなものです．<br>
(HAD付きExcelとか，PsychoToolBox付きMatlabみたいなもの)．

実験作成と分析には，Anacondaについてくる**Jupyter Notebook**という開発環境を使います．<br>

なお，AnacondaはPython2版とPython3版があります．**Python2**版にしましょう．<br>
(本当はPython3版がおすすめなのですが，2系でなければPsychoPyが動きません)

* [Anaconda for Windows](https://www.continuum.io/downloads#windows)
* [Anaconda for Mac](https://www.continuum.io/downloads#osx)

### 2.2. 当日

これらは当日インストールします．

* [IPAexフォント](http://ipafont.ipa.go.jp/node26#jp)
  * ページ下段，"IPAexゴシック"のzipファイルをダウンロードしてください．
  * zipを展開し，中の"ipaexg.ttf"にフォントパスを通してください．
    * Windows: ファイルを右クリックしたらインストールできます．
    * Mac: ファイルを~/Library/Fontsの中にコピペします．
  * このフォントは，日本語を含む刺激呈示や作図に使用します．
* [ANOVA君](http://riseki.php.xdomain.jp/index.php?ANOVA%E5%90%9B)
  * ページ中上段，"anovakun_◯◯◯.txt"をダウンロードしてください．
  * ANOVA君はRで分散分析をラクラク行うための関数です．
  * これがあまりに使いやすいため，分散分析だけはRを用いることにします．

### 2.3. あると便利

一応，PsycoPyがあると役に立つかもしれません (使う予定はありません)．

* [(Win向け) Portable PsychoPy](http://www.s12600.net/psy/etc/python.html)
* [(Mac向け) PsychoPy](http://psychopy.org/installation.html)

## 3. Jupyter Notebookの設定

ここから先は慣れてないと面倒くさいかもしれないので，できる範囲でOKです．

### 3.1. 動作確認

Jupyter Notebookを起動できるかどうか確認してください．

* Windowsなら，スタートメニューの中に「Jupyter Notebook」があるはずです．
* Macなら，以下の2つの方法で起動できます．
  * 「Anaconda Navigator」を開き，「Jupyter Notebook」をクリック．
  * ターミナルを開き，「jupyter notebook」を入力 (**オススメ!**)．

うまく起動すると，ブラウザが立ち上がり，以下のような画面が表示されます．

![起動画面](menu-screenshot.png)

### 3.2. 追加設定

WindowsユーザーはAnaconda Promptを起動してください．Macユーザーはターミナルを起動してください．
その後，以下を実行します．

```
conda install psychopy
```
