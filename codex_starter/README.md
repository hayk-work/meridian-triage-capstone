# Codex capstone starter

Work through the Sana course in order. An offline copy is in ../Advanced_Codex_Capstone_Instructions.md. All ticket records are fictional.

## Access and first checks
Use Python 3.10 or newer and authenticated Codex access with GPT-6 Astra available in an approved environment that can edit this folder and run Python. The supplied application uses only the standard library and needs no model API key. The ZIP is sufficient; GitHub is optional.

Run commands from this codex_starter folder. On Windows, replace python3 with py -3.

If the version is older than 3.10, select or install an approved newer Python before continuing. If it has a different command name, use that command throughout the lab—for example, `python3.12` on macOS/Linux or `py -3.12` on Windows. Confirm the version with that same command.

```bash
python3 --version
python3 app.py
python3 -m unittest discover -s tests -v
```

The initial application returns P3 for all eight records. Expect two test passes and seven intentional failures. Resolve a missing Python command or import error before continuing.

## Work with Codex
Read ACCEPTANCE_CRITERIA.md. Ask Codex to inspect and plan before editing, with a clear goal, allowed files, rule precedence, output contract, test command and stop conditions. Preserve existing approval controls. Edit only triage.py and tests/test_learner.py; keep all supplied data, application files and tests intact.

Implement the requested rules and add at least two useful tests, including the 24-hour boundary. Inspect the changes yourself and rerun:

```bash
python3 -m unittest discover -s tests -v
python3 app.py
```

Save your initial prompt, a useful interaction, the complete final test summary and outputs for T101, T105, T106 and T108. Explain a correction or a specific risk you checked. If Codex access is missing, ask your organization's Codex administrator to arrange it before implementation.

## Submit
Use SUBMISSION_TEMPLATE.md for S1–S5. The recommended upload is one ZIP containing report.pdf and this completed codex_starter folder. Alternatively, upload a PDF report containing a reviewer-accessible repository URL and exact commit. Exclude keys, caches and unrelated files. Use the Sana submission activity.
