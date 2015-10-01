#!/bin/bash
pushd /data
PALABRA=""
TRANSLATE=""
while [ "X$PALABRA" == X -o $TRANSLATE == $PALABRA ]; do
 PALABRA=$(wget -qO- http://www.spanishdict.com/wordoftheday/random | grep -E '<strong class="word"><a href="http://www.spanishdict.com/translate/.*">.*</a></strong>' | html2text -utf8 | sed 's/_/ /g')
 TRANSLATE=$(curl -s -i --user-agent "" -d "sl=es" -d "tl=it" --data-urlencode "text=$PALABRA" https://translate.google.com | iconv -f ISO-8859-1 |  awk 'BEGIN {RS="</div>"};/<span[^>]* id=["'\'']?result_box["'\'']?/' | html2text -utf8)
done

rm -rf mail_template
DAY=$(date +"%A")
GIORNO=$(curl -s -i --user-agent "" -d "sl=es" -d "tl=it" --data-urlencode "text=$DAY" https://translate.google.com | iconv -f ISO-8859-1 |  awk 'BEGIN {RS="</div>"};/<span[^>]* id=["'\'']?result_box["'\'']?/' | html2text -utf8)
echo -e "subject: Pranzo "$GIORNO" "`date +"%d/%m/%Y"` >> mail_template
echo -e "from: organizzatoribot@gmail.com" >> mail_template
echo -e "Hola chicos! Chi si presenta oggi?" >> mail_template
echo -e "12.45 @R2!" >> mail_template
echo -e "\n\n\nPalabra del dia: "${PALABRA}" -> "${TRANSLATE} >> mail_template
echo -e "Messaggio editato da AlessioBot, l'emulatore più fedele di OrganizzaTori(tm)" >> mail_template

cat mail_template | /usr/sbin/sendmail -t
popd
