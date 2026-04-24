@echo off
REM ============================================================
REM  create_pdf.bat — EBC Paper PDF-Erstellung (EN + DE)
REM  Aufruf: create_pdf.bat <VERSION>
REM  Beispiel: create_pdf.bat 2
REM            create_pdf.bat 3
REM ============================================================

setlocal

REM ── Versionsparameter prüfen ─────────────────────────────────
if "%~1"=="" (
    echo FEHLER: Bitte Versionsnummer angeben.
    echo Beispiel: create_pdf.bat 2
    exit /b 1
)

set VERSION=%~1
set PREFIX=EBC_v%VERSION%

REM ── Pfade (relativ zum Vault-Root, anpassen falls nötig) ─────
set PAPER_DIR=..\Paper
set FIG_DIR=..\Figures
set BUILD_DIR=.
set TEMPLATE=%BUILD_DIR%\EBC_pandoc_template.tex

REM ── Eingabedateien ───────────────────────────────────────────
set INPUT_EN=%PAPER_DIR%\EBC_paper_v%VERSION%.md
set INPUT_DE=%PAPER_DIR%\EBC_paper_v%VERSION%_DE.md

REM ── Ausgabedateien ───────────────────────────────────────────
set OUTPUT_EN=%PAPER_DIR%\%PREFIX%_paper.pdf
set OUTPUT_DE=%PAPER_DIR%\%PREFIX%_paper_DE.pdf

REM ── Prüfen ob Eingabedateien existieren ──────────────────────
if not exist "%INPUT_EN%" (
    echo FEHLER: Eingabedatei nicht gefunden: %INPUT_EN%
    exit /b 1
)

REM ── Englische Version ─────────────────────────────────────────
echo Erstelle englische PDF: %OUTPUT_EN%
pandoc "%INPUT_EN%" ^
    --template="%TEMPLATE%" ^
    --pdf-engine=xelatex ^
    --resource-path="%FIG_DIR%" ^
    -o "%OUTPUT_EN%"

if errorlevel 1 (
    echo FEHLER bei englischer PDF-Erstellung.
    exit /b 1
)
echo OK: %OUTPUT_EN%

REM ── Deutsche Version (nur wenn Datei vorhanden) ───────────────
if exist "%INPUT_DE%" (
    echo Erstelle deutsche PDF: %OUTPUT_DE%
    pandoc "%INPUT_DE%" ^
        --template="%TEMPLATE%" ^
        --pdf-engine=xelatex ^
        --resource-path="%FIG_DIR%" ^
        -o "%OUTPUT_DE%"

    if errorlevel 1 (
        echo FEHLER bei deutscher PDF-Erstellung.
        exit /b 1
    )
    echo OK: %OUTPUT_DE%
) else (
    echo HINWEIS: Keine deutsche Version gefunden ^(%INPUT_DE%^), wird uebersprungen.
)

echo.
echo Fertig. Erzeugte Dateien:
echo   %OUTPUT_EN%
if exist "%INPUT_DE%" echo   %OUTPUT_DE%

endlocal
