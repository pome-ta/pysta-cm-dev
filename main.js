"use strict";
import CodeMirror from './src/codemirror.js'


let myCodeMirror = CodeMirror(document.body, {
  value: "print('なぁ😭')\n# ほげー",
  mode: 'python',
  lineNumbers: true,
  }
  
);
console.log(myCodeMirror);


