# Changelog — ZeroStutter-MTA

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-17

### Added
* Initial release of ZeroStutter-MTA framework.
* `configs/coreconfig.template.xml`: Calibrated configuration baseline featuring 384 MB streaming memory, log filtering, software-rendered CEF, and D3D9 stability toggles.
* `configs/rtss/gta_sa.exe.cfg`: Target profile preventing RivaTuner Statistics Server hook collisions.
* `scripts/Invoke-CleanLogs.ps1`: Safe PowerShell archival and zero-byte truncation of runtime log files.
* `scripts/Clear-NvidiaCache.bat`: Automated purge of stale DirectX shader blobs.
* `scripts/Launch-MTAOptimized.bat`: One-click pre-launch pipeline with priority elevation.
* `registry/disable_mpo_windowed.reg`: Desktop Window Manager MPO stutter remediation.
* `registry/restore_mpo_default.reg`: Full rollback registry file for MPO settings.
* Complete documentation suite: `README.md`, `README.ru.md`, `AGENTS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `KNOWN_ISSUES.md`, `GRAPHICS_GUIDE.md`, `D3D9_MEMORY_MODEL.md`.
* Automated test suite `tests/ZeroStutter.Tests.ps1`.
