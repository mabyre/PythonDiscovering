REM Affiche les ports COM

Set "CurrentPath=%~dp0"
Set "INPUT_FILE=%CurrentPath%\input.txt"

Mode > "%INPUT_FILE%"

Type "%INPUT_FILE%"

pause