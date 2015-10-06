#!/bin/bash
pushd /data/alessiobot
export DJANGO_SETTINGS_MODULE=alessiobot.settings

#get the "parabla del dia"
PALABRA=""
TRANSLATE=""
while [ "X$PALABRA" == X -o $TRANSLATE == $PALABRA ]; do
 PALABRA=$(wget -qO- http://www.spanishdict.com/wordoftheday/random | grep -E '<strong class="word"><a href="http://www.spanishdict.com/translate/.*">.*</a></strong>' | html2text -utf8 | sed 's/_/ /g')
 TRANSLATE=$(curl -s -i --user-agent "" -d "sl=es" -d "tl=it" --data-urlencode "text=$PALABRA" https://translate.google.com | iconv -f ISO-8859-1 |  awk 'BEGIN {RS="</div>"};/<span[^>]* id=["'\'']?result_box["'\'']?/' | html2text -utf8)
done

#get the fortune
FORT_LINES=51
while [ $FORT_LINES -gt 50 ]
do
    FORT=$(fortune)
    FORT_LINES=$(echo $FORT | wc -w)
done

#send the email
rm -rf mail_template
DAY=$(date +"%A")
GIORNO=$(curl -s -i --user-agent "" -d "sl=es" -d "tl=it" --data-urlencode "text=$DAY" https://translate.google.com | iconv -f ISO-8859-1 |  awk 'BEGIN {RS="</div>"};/<span[^>]* id=["'\'']?result_box["'\'']?/' | html2text -utf8)
echo -e "subject: Pranzo "$GIORNO" "`date +"%d/%m/%Y"` >> mail_template
echo -e "from: organizzatoribot@gmail.com" >> mail_template
python getemails.py >> mail_template
echo -e "Hola chicos! Chi si presenta oggi?" >> mail_template
echo -e "12.45 @R2!" >> mail_template
echo -e "\n\nPalabra del dia: "${PALABRA}" -> "${TRANSLATE} >> mail_template
echo -e "\n$FORT" >> mail_template
echo -e "\nMessaggio editato da AlessioBot, l'emulatore più fedele di OrganizzaTori(tm)" >> mail_template

cat mail_template | /usr/sbin/sendmail -t
popd
