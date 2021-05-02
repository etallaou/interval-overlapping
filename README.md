# Coding Task 2: Überlappen von intervallen
eine Funktion MERGE die eine Liste von Intervallen entgegennimmt und als Ergebnis wiederum eine Liste von Intervallen 
zurückgibt. Im Ergebnis sollen alle sich überlappenden Intervalle gemerged sein. 
Alle nicht überlappenden Intervalle bleiben unberührt.

# Bearbeitungszeit:
1 Tag

# Test
```
python -m doctest -v src/app.py
```


# how to start
## without docker
```
python src/app.py <interval> <interval> <interval> 
python src/app.py [25,30] [2,19] [14,23] [8,6]
```


## build and running with docker
```
docker build -t interval-overlapping .
docker run interval-overlapping <intervals>
docker run interval-overlapping [25,30] [2,19] [14,23] [8,6]
```



## Bearbeitungszeit:
1 Tag

## Wie es funktioniert:

### gehen wir davon aus,
*  der Benutzer gibt eine Folge von Intervallen als Args an das Python-Programm
*  jedes Intervall ist eine Liste von zwei Zahlen und soll gut sortiert sein, d.h. der Anfang ist immer kleiner als das Ende, 

### um die Intervalle zu mergen, 
*  wir sortieren zunächst alle Intervalle mit dem kleinsten Anfang
*  dann erfolgt eine Überlappung, immer wenn der Anfang des ersten Intervalls größer ist als das Ende des zweiten Intervalls.
*  Am Ende wird die Laufzeit des programm geloggt werden.

```
Edmonds-MBP:interval-overlapping edmondtallaouafeu$ python src/app.py [25,30] [2,19] [14,23] [4,8]
INFO:root:the function takes 7.86781311035e-06 ms
[[2, 23], [25, 30]]
```

## Wie kann die Robustheit sichergestellt werden, vor allem auch mit Hinblick auf sehr große Eingaben ?
*  Um die Robustheit zu gewährleisten, haben wir eine Methode erstellt, die eine Exception auslöst, wenn die Eingabe nicht 
unserer Annahme entspricht. d.h. ein unnötiges Koma, oder ein Leerzeichen oder ein ungültiges Intervall, führt zu einer 
Exception.

* wir verwenden noch zwei python-Methoden, um die Intervalle zu sortieren und die obere Grenze eines Intervalls mit der 
unteren Grenze des nächsten Intervalls zu vergleichen. Allerdings kann es sein, dass nach einem Update von python diese 
Methode nicht mehr funktioniert. Aus diesem Grund ist es notwendig, die Tests vor der Verwendung des Programms durchzuführen.
Weitere Testfälle könnten hinzugefügt werden.

## Wie verhält sich der Speicherverbrauch ihres Programms ?
je mehr Intervalle getestet werden, desto mehr Speicher wird verwendet, je mehr Intervalle sich überlappen, desto mehr 
Speicher wird verwendet.
Diese hyphothese sollte aber noch bestätigt werden.


 




