# Lern-Periode-8

## 10/01/2025
### Arbeitspakete
- [x] LB450-Teilauftrag 1
- [x] LB450-Teilauftrag 2
- [x] LB450 Bugfixes im code
- [x] Beenden der [Lottery](https://library.m0unt41n.ch/challenges/lottery) CTF challenge (main.py)

#### Gelerntes
Testkonzept
Repetition Testfallspezifikation
Repetition Testfälle
Post requests mit python senden
SQLite3 `GLOB` operation (`LIKE` aber case-sensitive)

#### Schwierigkeiten
Ich hatte keine Ahnung das LIKE case-insensitive ist, was es einiges schwerer machte den Fehler in meinem Code für die Challenge zu finden. Danach habe ich versucht das ganze mit `BINARY 'userinput'` abzugleichen was auch case-sensitive wäre, aber dazu geführt hat, dass der server einen Fehler zurückgab. Danach fand ich die `GLOB` operation womit ich das ganze Schlussendlich lösen konnte.
