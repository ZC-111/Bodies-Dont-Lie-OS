# AGENTS.md

Agent and operational guidance only. Domain knowledge lives in the Living Tree ([README.md](README.md), [Constitution/](Constitution/BDL-000-Constitution.md)) — link to it here, don't restate it.

## Environment

Python 3.12 on the default base image; dependencies from [requirements.txt](requirements.txt) are installed by the `install` step in [.cursor/environment.json](.cursor/environment.json). No extra setup.

## The one executable

The only runnable component is the acupuncture pipeline. To run or verify it, follow [Research/acupuncture/pipeline-usage.md](Research/acupuncture/pipeline-usage.md).

## Cursor Cloud specific instructions

- Documentation-only changes (markdown under `Constitution/`, `Knowledge/`, `Projects/`, `Reflection/`, `Templates/`, `Archive/`, and READMEs) need only a proofread — no run required.
- Changes to the pipeline scripts (`Research/acupuncture/scripts/*.py`) or their input data **must** be validated by running and confirming the expected counts — see [pipeline-usage.md](Research/acupuncture/pipeline-usage.md). This is the Wayfinding **Validate** stage ([BDL-001](Constitution/BDL-001-Wayfinding-Kernel.md)).
- There is no web UI; verify pipeline changes with terminal output, not the computer-use browser.
