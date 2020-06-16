import wkwebview, ui
from os import path

#src = get_path()
src = path.abspath('index.html')

r = ui.View(background_color='black')

wv = wkwebview.WKWebView(swipe_navigation=True, flex='WH')

wv.load_url(src)
r.add_subview(wv)

r.present('fullscreen')
#wv.present('panel')


