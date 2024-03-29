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
