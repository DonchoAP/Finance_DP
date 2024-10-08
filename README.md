# Finanz-App

## Beschreibung

Dieses Projekt ist eine **Flask**-basierte Webanwendung zur Verwaltung und Analyse von Finanztransaktionen. Sie wurde entwickelt, um Aufgaben eines Praktikanten im Bereich Finanzen zu simulieren, einschließlich der Erstellung von Berichten, der Datenanalyse und des monatlichen Abschlusses. Die Anwendung ermöglicht es den Benutzern, die folgenden Aktionen durchzuführen:
- Finanztransaktionen hinzufügen
- Monats- und Quartalsberichte erstellen
- Berichte als PDF oder Excel exportieren
- Analyse von Ausgaben- und Einnahmentrends
- Einfache Finanzprognosen erstellen
- Monatliche finanzielle Abschlüsse durchführen
- Mehrsprachige Unterstützung (Deutsch und Englisch)

## Hauptfunktionen

1. **Transaktionsverwaltung**: Ermöglicht das Hinzufügen, Löschen und Bearbeiten von Finanztransaktionen wie Einnahmen und Ausgaben, kategorisiert nach Kategorie und Abteilung.
2. **Berichterstellung**: Möglichkeit, monatliche und vierteljährliche Finanzberichte im PDF- oder Excel-Format zu erstellen.
3. **Finanzanalyse**: Analysiert historische Finanzdaten, berechnet Ausgabentrends, Gewinnspannen und bietet einfache Vorhersagen mittels gleitendem Durchschnitt.
4. **Monatlicher Abschluss**: Simuliert einen monatlichen Finanzabschluss zur Berechnung der Bilanz von Einnahmen und Ausgaben.
5. **Sicherheit**: Benutzer-Authentifizierung mit verschlüsselten Passwörtern über `Flask-Login` und `Werkzeug`.
6. **Mehrsprachigkeit**: Unterstützung für das Umschalten zwischen Deutsch und Englisch.

## Voraussetzungen

Stellen Sie sicher, dass die folgenden Werkzeuge installiert sind, bevor Sie fortfahren:
- **Python 3.x** 
- **PostgreSQL** (oder ein anderes mit SQLAlchemy kompatibles Datenbanksystem)

## Installation

1. Klonen Sie dieses Repository:

    ```bash
    git clone https://github.com/benutzername/finanz-app.git
    cd finanz-app
    ```

2. Erstellen Sie eine virtuelle Umgebung (optional, aber empfohlen):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # In Windows: venv\Scripts\activate
    ```

3. Installieren Sie die erforderlichen Abhängigkeiten aus der Datei `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Konfigurieren Sie die Datenbank. Ändern Sie in der Datei `app.py` die Variable `SQLALCHEMY_DATABASE_URI` mit Ihrer PostgreSQL-Konfiguration:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://benutzer:passwort@localhost/financeapp'
    ```

5. Initialisieren Sie die Datenbank:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Starten Sie die Anwendung:

    ```bash
    flask run
    ```

Die Anwendung wird unter [http://localhost:5000](http://localhost:5000) verfügbar sein.

## Verwendung

### Eine Finanztransaktion hinzufügen
Senden Sie eine `POST`-Anfrage an `/add_transaction` mit folgendem JSON-Inhalt:

```json
{
    "date": "2024-10-07",
    "amount": 500.00,
    "category": "Marketing",
    "department": "Vertrieb",
    "type": "income"
}

Einen Bericht generieren
Senden Sie eine POST-Anfrage an /generate_report mit dem Berichtstyp und dem Ausgabeformat:
{
    "type": "monthly",
    "format": "pdf"
}

Monatlicher Finanzabschluss
Greifen Sie auf /monthly_closing zu, um eine Bilanz des letzten Monats zu erhalten.

Sprache ändern
Senden Sie eine GET-Anfrage an /change_language mit dem Parameter lang, um zwischen Deutsch und Englisch zu wechseln:
/change_language?lang=de

Verwendete Technologien
Flask: Framework zur Webentwicklung.
SQLAlchemy: ORM zur Datenbankverwaltung.
pandas: Zur Datenverarbeitung und -analyse.
matplotlib: Zur Erstellung von Diagrammen.
xlsxwriter: Zum Exportieren von Berichten in Excel.
ReportLab: Zum Erstellen von PDF-Berichten.
Flask-Login: Zur Benutzer-Authentifizierung.
Werkzeug: Zum sicheren Hashen von Passwörtern.
Mitwirken
Forken Sie das Repository.
Erstellen Sie einen neuen Branch (git checkout -b feature-neue-funktion).
Führen Sie Ihre Änderungen durch und committen Sie sie (git commit -am 'Neue Funktion hinzufügen').
Pushen Sie den Branch (git push origin feature-neue-funktion).
Erstellen Sie einen Pull Request.
Lizenz
Dieses Projekt steht unter der MIT-Lizenz.


---

### Zusammenfassung:
- Der `README.md` enthält eine vollständige Anleitung zur Installation, Nutzung und Konfiguration der Finanz-App auf Deutsch.
- Es beschreibt die wichtigsten Funktionen, wie das Hinzufügen von Transaktionen, das Generieren von Berichten und den monatlichen Abschluss.
- Zudem erklärt es, wie die Anwendung auf einem lokalen Server gestartet wird, und beschreibt die verwendeten Technologien.
