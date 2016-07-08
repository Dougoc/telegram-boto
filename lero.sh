#/bin/bash
#frase=`content=$(curl -L www.lerolero.com) >> /dev/null 2>&1; echo $content | sed -n 's#.*<blockquote id="frase_aqui">\(.*\)</blockquote>.*#\1#p'`


export PEGA=`curl -L www.lerolero.com > temp.html`
export FRASE=$PEGA && cat temp.html | sed -n 's#.*<blockquote id="frase_aqui">\(.*\)</blockquote>.*#\1#p' > frase.txt
$PEGA && $FRASE
cat frase.txt