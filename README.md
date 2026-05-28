# Meflix, en program som kan ladda ner tv program från Npo Start

### Innehåll:

 * Information

 * Hur man ska använda Meflix

 * Länkar

   
## Information

En webbsida där man kan ladda ner tv program från Npo Start. Gjort med html och Flask som backend. Html filerna är server side rendered med Flask. Ser about sidan på webbsidan för mer information: https://slutprojekt.megames.se/about


## Hur man ska använda Meflix

Man använder Meflix genom att öppna sidan (Se länkar för att få korrekt sida) och välja ett av de rekommenderade programmen, eller genom att skriva in ett program i sökformuläret.

Efter att man har sökt på något visas sökresultaten. Där kan man se flera tv-program som är relaterade till sökningen. Man väljer ett av dem genom att klicka på det.

När man har valt ett program kommer man till en sida med information om programmet samt två fält där man kan välja säsong och avsnitt. Man börjar med att välja en säsong. När en säsong har valts laddar programmet in de avsnitt som tillhör den säsongen. Detta tar ungefär en sekund, och under tiden visas texten ”LOADING” i avsnittsfältet.

När man har valt sitt avsnitt laddar man ner det genom att klicka på knappen ”Download”. Då börjar avsnittet laddas ner, och efter en stund får man filen.


## Länkar

Där finns 2 typer av den här webbsidan:

Typ 1, statiskt version:

Den här typen är gjort för att testa layouten och används som en template. Alltså det är inte möjligt att ladda ner med den här versionen.

Länk: https://megames074he.github.io/slutprojekt/


typ 2 dynamiskt version:

Den här typen är dynamiskt. Alltå den får data från flask. Man kan ladda ner med den här typen. 

Länk: https://slutprojekt.megames.se/
