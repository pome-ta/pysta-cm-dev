# 📝 2020/06/16


まずは、前回に倣って環境構築


## CodeMirror

version : `5.54.0`


## WKWebView


- [pythonista-webview](https://github.com/mikaelho/pythonista-webview)

> WKWebView implementation for Pythonista

### メモ

- Pythonista のWebView が UIWebView のため
- CodeMirror の日本語入力問題解決のため


## Eruda

- [main](https://eruda.liriliri.io/)
- [GitHub](https://github.com/liriliri/eruda)
- [CDN](https://www.jsdelivr.com/package/npm/eruda)


version : `2.3.3`

### メモ

- JavaScript のデバッグコンソール用
- `jsdelivr` なのは、GitHub の指定リンクが最初だったから


# CodeMirror の対応

- html の`script`タグを`type="module"`に
	- `main.js` から、CodeMirror `/src` を呼び出す
	- `/src` 内は、現在追記せず
- `mode` ディレクトリ
	- 各言語の`hoge.js` の先頭に以下を追加

``` addScript.js
import CodeMirror from '../../src/codemirror.js'
```

	- `meta.js` に挿しても、機能せず

