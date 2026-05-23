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

Vor dem Start der Anwendung muss ein eigener OpenAI API-Key als Sealed Secret erstellt werden, sowie die .env Datei erstellt werden.

kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/latest/download/controller.yaml

Sealed Secrets Controller installieren

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

NGINX Ingress Controller installieren

Erstellen sie die .env Datei im Root-Ordner dieses Projekt und fügen sie hinzu

OPENAI_API_KEY=YOUR_API_KEY
DATA_SERVICE_URL=http://data-service:8000/metrics
OPENAI_MODEL=gpt-4o-mini

Diese Datei darf nur Lokal gespeichert sein

Erstellen sie eine unverschlüsselte ai-api-secrect

kubectl create secret generic ai-api-secret `
  --from-literal=OPENAI_API_KEY=YOUR_AI_KEY `
  --dry-run=client -o yaml > k8s/ai-api-secret.yaml

Anschließend wird daraus ein verschlüsseltes Sealed Secret erzeugt:

Get-Content k8s/ai-api-secret.yaml | kubeseal --format yaml > k8s/ai-api-sealed-secret.yaml

unverschlüsseltes Secret löschen

Remove-Item k8s/ai-api-secret.yaml

Das Programm kann über zwei Möglichkeiten gestartet werden. Bei beiden Varianten muss zunächst in den Root-Ordner des Projekts gewechselt werden. 

Die erste Möglichkeit erfolgt automatisiert über das Skript:

bash deploy.sh

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

Die Analyse der Google-Trends-Daten zeigt, dass die meisten Suchanfragen im betrachteten Zeitraum relativ konstant geblieben sind. Für Begriffe wie Kreatin, Proteinpulver und Omega 3 konnten nur kleinere Schwankungen erkannt werden, jedoch keine starken Anstiege oder deutlichen Rückgänge im Suchinteresse. Insgesamt ist das Suchverhalten bei diesen Begriffen gleichmäßig und stabil, wodurch kein großer Popularitätsschub oder langfristiger Verfall erkennbar ist.

Besonders hervorgehoben hat sich Vitamin D. Hier konnte kurzfristig ein deutlich stärkeres Suchinteresse beobachtet werden, vor allem ist hier der peak am 5.Mai besonders aufällig wo das Intresse sich fast verdoppelt hat, dadurch hat sich dieser Begriff klar von den anderen Supplements abgesetzt. Whey Protein zeigte dagegen im Vergleich die niedrigsten Werte und war damit der am wenigsten gesuchte Begriff innerhalb des Datensatzes.

5. Visualisierung – Welche Visualisierungen wurden erstellt und warum?  
Wie helfen diese, die Daten besser zu verstehen? 

Für die Analyse der Google-Trends-Daten wurden zwei zentrale Visualisierungen eingesetzt: ein Vergleich mehrerer Begriffe sowie ein Ranking nach durchschnittlichem Suchinteresse. Beide Darstellungen dienen dazu, die relativen Unterschiede zwischen den untersuchten Supplements schnell und übersichtlich erkennbar zu machen.

Der Vergleich mehrerer Begriffe ermöglicht es, die Entwicklungen von Proteinpulver, Kreatin, Whey Protein, Vitamin D und Omega 3 direkt gegenüberzustellen.

Das Ranking nach Interesse fasst die Daten zusätzlich zusammen und zeigt auf einen Blick die relative Beliebtheit der einzelnen Suchbegriffe innerhalb des Datensatzes. Diese Darstellung erleichtert die schnelle Einordnung, welcher Begriff insgesamt am häufigsten gesucht wurde, ohne die Zeitreihen im Detail betrachten zu müssen.

In Kombination ermöglichen beide Visualisierungen eine neue Sichtweise für die Interpretation der Daten, da Trends, Unterschiede und Prioritäten unmittelbar erkennbar werden.

6. Herausforderungen und Learnings – Welche technischen oder fachlichen Probleme sind aufgetreten?  
Wie wurden diese gelöst?  
Was haben Sie aus dem Projekt gelernt?  

Die größte Herausforderung bestand darin, dass das ursprüngliche Programm aus der Vorlesung nur einen einzelnen Begriff aus den CSV-Dateien verarbeiten konnte. Da für das Projekt mehrere Suchbegriffe gleichzeitig analysiert werden sollten, musste die Verarbeitung erweitert werden. Dieses Problem wurde durch den Einsatz von Schleifen gelöst.

Die erste Schleife in der main.py des Data-Services liest die Werte aus der CSV-Datei ein und sortiert diese nach ihren jeweiligen Begriffen. Anschließend verarbeitet eine zweite Schleife die gesammelten Werte weiter, berechnet Kennzahlen wie Mean, Peak und Trend und speichert die Ergebnisse im JSON-Format innerhalb einer Liste. Dadurch können mehrere Begriffe automatisiert analysiert und strukturiert weitergegeben werden.

Aus dem Projekt mitgenommen wurde die Kommunikation zwischen Services über APIs, die Nutzung von KI zur Analyse und Darstellung der Ergebnisse, sowie die Implementierung von Kubernetes zur Überwachung der Services.

7. Zukunftsvision – Wie könnte Ihr System weiterentwickelt werden?  
Welche zusätzlichen Daten, Features oder AI-Methoden könnten integriert werden? 

Das System könnte in Zukunft erweitert werden, indem die Daten nicht mehr manuell als CSV-Dateien importiert werden müssen. Stattdessen könnte die Anwendung automatisch Daten von Google Trends abrufen, verarbeiten und analysieren.

Zusätzlich könnten weitere AI-Methoden integriert werden, um externe Ereignisse oder Entwicklungen zu erkennen, die Veränderungen im Suchinteresse beeinflussen. Beispielsweise könnte die KI Nachrichten, Social-Media-Trends oder saisonale Ereignisse analysieren und daraus mögliche Ursachen für steigende oder fallende Suchanfragen ableiten.

Eine weitere mögliche Erweiterung wäre die Untersuchung, ob sich aus den Daten Aussagen über zukünftige Entwicklungen ableiten lassen. Dabei könnte geprüft werden, ob Trends aus der Vergangenheit Hinweise auf zukünftige Nachfrage geben.

Außerdem könnte analysiert werden, ob ein Zusammenhang zwischen dem Suchinteresse bei Google Trends und tatsächlichen Verkaufszahlen besteht. Dadurch könnte das System langfristig auch für Marktanalysen oder Prognosen genutzt werden.