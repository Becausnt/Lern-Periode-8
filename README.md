# Lern-Periode-8

## 10/01/2025
### Arbeitspakete
- [x] LB450-Teilauftrag 1
- [x] LB450-Teilauftrag 2
- [x] LB450 Bugfixes im code
- [x] Beenden der [Lottery](https://library.m0unt41n.ch/challenges/lottery) CTF challenge (main.py)

#### Gelerntes
- Testkonzept
- Repetition Testfallspezifikation
- Repetition Testfälle
- Post requests mit python senden
- SQLite3 `GLOB` operation (`LIKE` aber case-sensitive)

#### Schwierigkeiten
Ich hatte keine Ahnung, dass LIKE case-insensitive ist, was es einiges schwerer machte den Fehler in meinem Code für die Challenge zu finden. Danach habe ich versucht das ganze mit `BINARY 'userinput'` abzugleichen was auch case-sensitive wäre, aber dazu geführt hat, dass der server einen Fehler zurückgab. Danach fand ich die `GLOB` operation womit ich das ganze Schlussendlich lösen konnte.

## 17/01/2025
### Arbeitspakete
- [x] LA_295_6409_GIT
- [x] LA_295_6410_GIT_IGNORE
- [x] LA_295_6403_Datenbank


#### Gelerntes
- Connection strings erstellen (C#-API mit Datenbank)
- .gitignore Dateien schreiben
- Git Grundlagen repetiert (init, clone, add, commit, push, pull)

#### Schwierigkeiten
Es dauerte lange, den Connection string richtig hinzubringen, aber jetzt funktioniert soweit alles. (noch)


## 24/01/2025
### Arbeitspakete
- [x] Basics Android (ADB, OS, usw.)
- [x] Basics Android app structure
- [x] Basics Android app reverse engineering/modding
- [x] Basics Android app packaging

#### Gelerntes
- Android emulieren ( [Android Studio](https://developer.android.com/studio) oder [MEmu](https://www.memuplay.com) )
- An APKs kommen (Backup/pull via [ADB](https://developer.android.com/tools/adb) )
- APKs decompilen ( [APKTool](https://apktool.org/) oder [APKToolkit](https://xdaforums.com/t/tool-apk-toolkit-v1-5-windows.4572881/) )
- APKs "lesen" (Code lesen mit bspw. [Jadx](https://github.com/skylot/jadx) )
- APKs bearbeiten ( Mit VSCode [Smali-Dateien](https://fileinfo.com/extension/smali) bearbeiten )
- APKs signieren, repacken und wieder installieren ( Auch APKTool )

#### Schwierigkeiten
Mit MEmu hatte ich Schwierigkeiten, die ADB zu verbinden. Dies konnte ich aber durch die Entwickler- und Netzwerkeinstellungen des Geräts/Emulators fixen. Ansonsten hatte ich noch nicht gross Schwierigkeiten, aber dies sind auch erst mal nur die Grundlagen. Ein richtiges Projekt habe ich auch noch nicht so recht.

## 31/01/2025
### Arbeitspakete
- [ ] LA_347_0047_GA_MovieWebsite
- [x] AM_347_5062_DockerfileBestPractice

#### Gelerntes
- Repetition docker-compose
- Docker netzwerke erstellen
- Docker Docker env dateien

#### Schwierigkeiten
Meine env-Datei `movie.env` wurde nicht gelesen, aber dies ist offenbar, da normalerweise nach einer Datei namens `.env` gesucht wird und nicht nach `*.env`. Diesen Fehler habe ich nun aber behoben. Ansonsten habe ich nur das Problem, dass meine Docker-Fähigkeiten noch nicht gut genug sind. Ich weiss nicht wirklich was ich wie machen sollte, also ist es ein ständiges Präsentationen-durchsuchen. Deshalb bin ich auch mit dem Auftrag noch nicht fertig geworden. Aber der Auftrag war auch noch eine gute auffrischung für alles was wir bisher durchgenommen haben.
