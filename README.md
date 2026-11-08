# Python interview prep

Practice problems for this folder run in a local virtual environment named `.venv`. That folder is gitignored, so each clone needs its own environment.

## Requirements

- Windows
- Python 3.14, available as `py -3.14`

Check the launcher:

```powershell
py -0p
```

## Create the environment

From this folder:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

## Activate it

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, allow it for the current user and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Confirm the active interpreter:

```powershell
python --version
where.exe python
```

`where.exe python` should point at `.venv\Scripts\python.exe`.

## Cursor

Workspace settings already select `.venv\Scripts\python.exe` and activate it in new terminals. If the status bar shows another interpreter, run **Python: Select Interpreter** and choose `.venv`.
