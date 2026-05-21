# Spezielle-Programmierung

1. Executive Summary – Geben Sie eine kurze Zusammenfassung Ihres Projekts.  
Welche Kategorie wurde analysiert und welche zentralen Erkenntnisse wurden gewonnen?  

Das Projekt analysiert das Suchverhalten in der Kategorie Supplements. Untersucht wurden die Begriffe Proteinpulver, 
Kreatin, Whey Protein, Vitamin D und Omega 3. Die Daten stammen aus Google Trends und beziehen sich auf das Suchverhalten 
in Deutschland im Zeitraum des letzten Monats anhand der Suchanfragen. Google Trends stellt die Werte relativ dar, wodurch 
beispielsweise sichtbar wird, wie viel höher das Interesse an Vitamin D im Vergleich zu Kreatin war.

Die zentralen Erkenntnisse zeigen, dass innerhalb des Datensatzes Unterschiede im Suchinteresse der untersuchten Supplements 
erkennbar sind. Durch die automatisierte Verarbeitung der CSV-Dateien können Trends und Entwicklungen strukturiert dargestellt 
und analysiert werden. Dabei wurde deutlich, dass sich die Suchbegriffe hinsichtlich ihrer relativen Popularität unterscheiden 
und verschiedene Verlaufsmuster aufweisen. Die Auswertung bildet damit die Grundlage für eine weiterführende Analyse von 
Google-Trends-Daten mithilfe von KI.

2. Ziele des Projekts – Welches Ziel verfolgt Ihr Projekt?  
Welches Problem oder welche Fragestellung im Kontext von Google Trends wird untersucht?

Das Ziel des Projekts ist die automatisierte Aufbereitung und Analyse von Daten aus Google Trends für eine spätere Weiterverarbeitung. 
Die Anwendung bereinigt und strukturiert die exportierten CSV-Dateien, damit die enthaltenen Informationen besser lesbar und einfacher 
auswertbar sind. Anschließend werden die aufbereiteten Daten an eine KI übergeben, die die Ergebnisse übersichtlich darstellt und analysiert.

Im Kontext von Google Trends untersucht das Projekt, wie sich das Suchinteresse einzelner Begriffe im Zeitverlauf entwickelt und wie sich 
verschiedene Suchbegriffe relativ zueinander verändern. Dabei ist zu beachten, dass Google Trends keine absoluten Suchzahlen liefert, 
sondern ausschließlich relative Werte verwendet. Dadurch können die Begriffe nur innerhalb desselben Datensatzes sinnvoll miteinander verglichen werden. 
Ein direkter Vergleich mit anderen Datensätzen oder die Ableitung konkreter Suchmengen ist daher nicht möglich.

3. Anwendung und Nutzung – Wie wird die Anwendung gestartet (How to start, Step by step)?  
Wie wird Ihre Anwendung genutzt? Wer sind die potenziellen Nutzer?

Das Programm kann über zwei Möglichkeiten gestartet werden. Bei beiden Varianten muss zunächst in den Root-Ordner des Projekts gewechselt werden. 
Zusätzlich muss vor dem Start in der .env-Datei im Root-Ordner der OpenAI-Schlüssel eingetragen werden, indem your ai key durch den eigenen API-Key ersetzt wird.

Die erste Möglichkeit erfolgt automatisiert über das Skript:

./deploy.sh

Alternativ kann die Anwendung auch manuell gestartet werden:

docker compose up --build -d 

kubectl apply -f k8s/

Zur Überprüfung, ob die Anwendung erfolgreich gestartet wurde, können folgende Tests verwendet werden:

kubectl get pods

Überprüft, ob die Pods gestartet wurden.

kubectl get services

Zeigt die laufenden Services an.

Zusätzlich stehen folgende Endpunkte zur Verfügung:

http://ai.localhost/live

Überprüft, ob die AI erreichbar ist.

http://ai.localhost/ready

Überprüft, ob der Data-Service erreichbar ist.

http://ai.localhost/analysis

Gibt die Analyse inklusive Interpretation und Visualisierung aus.

Zum Beenden der Anwendung können folgende Befehle verwendet werden:

docker compose down
kubectl delete -f k8s/

Potenzielle Nutzer sind aktuell hauptsächlich Entwickler, die das System weiterentwickeln oder analysieren möchten. Für den Vertrieb oder Marktanalysen kann die Anwendung 
ebenfalls genutzt werden, allerdings sind die Ergebnisse aufgrund der relativen Daten von Google Trends nur eingeschränkt aussagekräftig und vor allem für Vergangenheitsanalysen geeignet.

4. Datenanalyse und Ergebnisse – Welche Muster oder Trends konnten Sie erkennen?  
Gab es auffällige Peaks, Unterschiede oder Entwicklungen? Welche Begriffe haben sich besonders hervorgehoben?