# Test Report Generator

Dit project leest logbestanden uit een opgegeven loglocatie, verwerkt deze, en genereert HTML-rapporten in een opgegeven rapportlocatie. Het maakt gebruik van verschillende modules en een FastAPI-server voor het beheren van de endpoints.

## Functionaliteiten

- **Leest logs uit opgegeven log locatie**: De logbestanden worden gelezen uit de locatie die is opgegeven in `settings.cfg`.
- **Bouwt HTML-bestanden naar opgegeven rapportlocatie**: De HTML-rapporten worden gegenereerd en opgeslagen in de locatie die is opgegeven in `settings.cfg`.
- **Installeert vereiste pakketten**: De benodigde Python-pakketten worden geïnstalleerd via `requirements.txt`.
- **Configuratie via `settings.cfg`**: De configuratie van mappen en serverinstellingen gebeurt via het `settings.cfg` bestand.
- **Gebruik van `template` map**: De `template` map bevat het templatebestand dat wordt gebruikt voor het genereren van HTML-bestanden.
- **Gebruik van `public` map**: De `public` map bevat CSS-bestanden voor het stylen van de gegenereerde HTML-bestanden.
- **Modules voor verwerking**: De `modules` directory bevat alle logica voor het ophalen, converteren, en aanpassen van bestanden.
- **FastAPI endpoints**: `main.py` bevat de FastAPI endpoints voor het beheren van de API.

## Installatie

1. **Clone de repository**:
    ```bash
    git clone https://github.com/sidge4real/junit-xml-to-html-test-report-generator.git
    cd junit-xml-to-html-test-report-generator
    ```

2. **Installeer vereiste pakketten**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configuratie**:
    - **settings.cfg**: Pas de configuratie aan volgens je behoeften.
    - **Voorbeeld van `settings.cfg`**:
        ```ini
        [directories]
        reports_dir = ./reports
        logs_dir = ./logs

        [server]
        host = 127.0.0.1
        port = 8000
        ```

## Structuur van het Project

- **`/template`**: Bevat het templatebestand `report_template.html` dat wordt gebruikt om de HTML-rapporten te bouwen.
- **`/public`**: Bevat CSS-bestanden voor de styling van de HTML-rapporten.
- **`/modules`**: Bevat de logica voor het ophalen, converteren, en aanpassen van de bestanden:
    - `configuration.py`: Bevat het beheer van de configuratie-instellingen.
    - `XML_to_HTML.py`: Bevat de logica voor het converteren van XML naar HTML.
    - `report_management.py`: Bevat functies voor het beheren van de rapportbestanden.
- **`main.py`**: Bevat de FastAPI endpoints voor het beheren van de API.

## Gebruik

1. **Start de server**:
    ```bash
    python main.py
    ```

2. **Endpoints**:
    - **GET /**: Geeft een lijst van alle beschikbare rapporten.
    - **GET /{file_name}**: Geeft het specifieke HTML-rapport terug.