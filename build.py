import json,base64,io
from pathlib import Path
d=Path(__file__).parent
t=(d/'template.html').read_text(encoding='utf-8')
data=(d/'data.json').read_text(encoding='utf-8')
import re,os
page=t.replace('/*DATA*/null',data)
(d/'artifact.html').write_text(page,encoding='utf-8')
cfgp=d/'cloud.json'
if cfgp.exists():
    cfg=json.dumps(json.loads(cfgp.read_text(encoding='utf-8')),ensure_ascii=False)
    page=re.sub(r'/\*CLOUDCFG\*/.*?/\*END\*/',lambda m:'/*CLOUDCFG*/'+cfg+'/*END*/',page,flags=re.S)
icon=''
try:
    from PIL import Image,ImageDraw,ImageFont
    im=Image.new('RGB',(180,180),'#1b6d8c');dr=ImageDraw.Draw(im)
    f=ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',108)
    dr.text((90,92),'解',font=f,fill='white',anchor='mm')
    b=io.BytesIO();im.save(b,'PNG');icon='<link rel="apple-touch-icon" href="data:image/png;base64,%s">'%base64.b64encode(b.getvalue()).decode()
except Exception as e: print('icon skipped',e)
head='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="解剖クイズ"><meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#1b6d8c">%s
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style></head><body>'''%icon
(d/'解剖過去問クイズ.html').write_text(head+page+'</body></html>',encoding='utf-8')
print(len(page))
