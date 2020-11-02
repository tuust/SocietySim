# SocietySim
Georg Karu ja Margus Burk
Üritame teha võimalikult reaalse simuleeritud ühiskonna, kust saaks koguda andmeid näiteks viiruse leviku kohta. Peale andmete kogumist tahame neid kindlasti ka graafiliselt kuidagi väjastada, head vahend selleks on ilmselt matplotlib. Lahe oleks ka seda ühiskonda kuidagi visualiseerida, võibolla ka matplotlib'i animatsiooni kasutades. Idee jaoks saime palju [inspiratsiooni](https://www.youtube.com/channel/UCKzJFdi57J53Vr_BkTfN3uQ).
## Installation
3D keskkond vajab OpenGL'i mingit versiooni, 4.6.0 töötab kindlasti.\
Vist töötab moodulite kättesaamiseks :)
```pip install -r requirements.txt```
## Tööjaotus
**Georg Karu** - Tegeleb graafilise poolega. Kood asub graphs branchis.\
graphics.py peab praegu käivitama. WASD liigutab kaamerat, SHIFT liigutab üles, CTRL liigutab alla. Teoorias töötab ka hiirega ringi vaatamine vajutades SPACE ning kunagi töötas ka vabalt ringi lendamine, kuid seda on nüüdseks piiratud.\
graphics.py rida 217 listi suurust muutes saab linna teha suuremaks/väiksemaks.\
**Margus Burk** - Tegeleb back-endiga. Kood põhiliselt sim branchis. Käivitada main.py ja kirjutada valmis viiruse levimise kood. Linna sissegenereerimisega on ka tegeletud, mis väljastab kus mis mingi hoone asub hetkel 10x10 ruudustikus, kasutades infot karu kirjutatud graphics.py ja buildings.py kohta. Vaja on math-i, randinti ja veel teisi lisasid. Lisaks on tehtud inimese nn spawnpoint, liikumispoint ja viiruse levik.
## Lingid
[Trello projekt](https://trello.com/invite/b/Jpmwlrf9/fbb6f7eab0eaf6a5f503c68ed731657c/programming)\
[Paber prototüübist pilt](https://drive.google.com/file/d/1HQ8DyVgav7QS9_rUDR6P6Z7sZj3u1z3w/view?usp=drivesdk)\
[Testlugu](https://docs.google.com/document/d/1cpls7_8X-8xKpTxBhHj9saon5NaK-EKF1s3iKGBTOQw/edit?usp=drivesdk)
