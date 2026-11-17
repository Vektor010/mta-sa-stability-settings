# Project Roadmap — ZeroStutter-MTA

> Strategic Development Goals for 2026–2027.

---

## [v1.0.0] — Foundation & Frame Pacing (Current Release)
- [x] Initial repository structure and AI Handoff documentation.
- [x] RTSS profile exclusion template to prevent D3D9 Present collisions.
- [x] Calibrated `coreconfig.template.xml` (384 MB streaming memory, log filtering, CEF GPU off).
- [x] Automated log maintenance and archival script (`Invoke-CleanLogs.ps1`).
- [x] Windows DWM MPO registry optimization and safe rollback files.
- [x] NVIDIA DXCache cleanup automation (`Clear-NvidiaCache.bat`).
- [x] Automated Pester test suite (`ZeroStutter.Tests.ps1`).

---

## [v1.1.0] — Automated Diagnostics & GUI CLI (Q1 2027)
- [ ] Implement `Test-MTAHealth.ps1` to inspect active installations for blacklisted DLLs and memory pressure.
- [ ] Add automatic detection of MTA installation directories via Windows Registry (`HKLM\SOFTWARE\WOW6432Node\Multi Theft Auto: San Andreas All`).
- [ ] Single-click PowerShell WPF graphical installer for non-technical users.

---

## [v1.2.0] — Telemetry & Frame Pacing Analytics (Q2 2027)
- [ ] Integration with CapFrameX / PresentMon CSV logs to automatically plot frametime percentiles (p95, p99, 1% low).
- [ ] Automatic hardware profile detection (AMD X3D vs Intel Hybrid).
