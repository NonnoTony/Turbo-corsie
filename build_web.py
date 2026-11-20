# Crea la versione del gioco per un sito web normale (cartella docs/), partendo da index.html.
import re,os
src=open('index.html',encoding='utf-8').read()
cut=src.index('<div class="app">')
head,body=src[:cut],src[cut:]
head=re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?','',head)
import hashlib,json
VER=hashlib.sha1(src.encode('utf-8')).hexdigest()[:10]
# controllo degli aggiornamenti: se su GitHub c'è una versione più nuova, la pagina si ricarica da sola con quella
UPD='<script>(function(){var V="'+VER+'";function chk(){try{fetch("version.json?t="+Date.now(),{cache:"no-store"}).then(function(r){return r.json()}).then(function(j){if(!j||!j.v||j.v===V)return;var k="tc-upd-"+j.v;try{if(sessionStorage.getItem(k))return;sessionStorage.setItem(k,"1")}catch(e){}var u=new URL(location.href);u.searchParams.set("v",j.v);location.replace(u.toString())}).catch(function(){})}catch(e){}}chk();document.addEventListener("visibilitychange",function(){if(!document.hidden)chk()})})();</script>'
page=f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="description" content="Turbo Corsie: corse di mini 4WD su piste giocattolo. Modifica e colora le tue auto nel garage 3D, gioca in due sullo stesso telefono o online con chi vuoi.">
<meta name="theme-color" content="#1b4a3a">
{UPD}
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<style>:root{{color-scheme:dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}</head>
<body>
{body}
</body>
</html>
'''
os.makedirs('docs',exist_ok=True)
open('docs/index.html','w',encoding='utf-8').write(page)
open('docs/.nojekyll','w').write('')
open('docs/version.json','w').write(json.dumps({'v':VER}))
open('docs/manifest.webmanifest','w',encoding='utf-8').write('''{
  "name": "Turbo Corsie",
  "short_name": "Turbo Corsie",
  "description": "Corse di mini 4WD su piste giocattolo",
  "start_url": "./",
  "display": "standalone",
  "orientation": "any",
  "background_color": "#143a2d",
  "theme_color": "#1b4a3a",
  "icons": [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
    {"src": "icon.svg", "sizes": "any", "type": "image/svg+xml"}
  ]
}
''')
print('docs/index.html', len(page))
