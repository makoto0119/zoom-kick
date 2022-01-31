# zoom-kick
zoom-kick は、パスコード付き zoom の起動情報をまるごとクリップボードに入れ、直接起動できる URL を生成して zoom をキックするツールです。

#クリップボードからIDとPWを取り出して、zoom の URL をキックする
import pyperclip
import webbrowser

zoom_id = ''
zoom_pc = ''
zoom_url = ''
xmi = 0
xpw = 0
xpc = 0
count = 0

lines = pyperclip.paste().split()
count = len(lines)

# ミーティング ID のみを指定した際の、例外処理

if count == 0 :
	print ('ERR クリップボードが空です')
	input ()
	exit()

if count == 2 :
	print ('ERR クリップボードに２つしか単語がありません')
	input ()
	exit()

if count == 1 :
	zoom_id = lines[0]
elif count == 3 :
	zoom_id = lines[0] + lines[1] + lines[2]

if zoom_id != '' :
	zoom_url = 'zoommtg://zoom.us/join?confno=' + zoom_id
	webbrowser.open(zoom_url)
	exit()

try:
	xmi = lines.index('ミーティングID:')

except ValueError :
	# エラーを表示
	print ('ERR ID 取得に失敗 / ミーディングID: が見当たりません')
	input ()
	exit()

zoom_id = lines[xmi+1] + lines[xmi+2] + lines[xmi+3]

try:
	xpc = lines.index('パスコード:')
except ValueError :
	pass

if xpc == 0 :
	try:
		xpw = lines.index('パスワード:') #古い記載の救済
	except ValueError :
		pass

if xpw != 0 : #パスワード発見
	zoom_pc = lines[xpw+1]

if xpc != 0 : #パスコード発見 パスワードよりパスコードを優先
	zoom_pc = lines[xpc+1]

if zoom_pc =='' :
	print ('WRN Pass 取得に失敗 / パスコード: が見当たりませんが起動します')
	input ()

zoom_url = 'zoommtg://zoom.us/join?confno=' + zoom_id + '&pwd=' + zoom_pc
webbrowser.open(zoom_url)



# Name（リポジトリ/プロジェクト/OSSなどの名前）

分かりやすくてカッコイイ名前をつける（今回は"hoge"という名前をつける）

"hoge"が何かを簡潔に紹介する

# DEMO

"hoge"の魅力が直感的に伝えわるデモ動画や図解を載せる

# Features

"hoge"のセールスポイントや差別化などを説明する

# Requirement

"hoge"を動かすのに必要なライブラリなどを列挙する

* huga 3.5.2
* hogehuga 1.0.2

# Installation

Requirementで列挙したライブラリなどのインストール方法を説明する

```bash
pip install huga_package
```

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```

# Note

注意点などがあれば書く

# Author

作成情報を列挙する

* 作成者
* 所属
* E-mail

# License
ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる

"hoge" is Confidential.
## 
