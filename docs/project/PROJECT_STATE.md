# PROJECT_STATE.md — Active Handoff & Session State

> **Standard**: Universal Open Source Standard 2026 (AI + Human Continuation).  
> **Last Updated**: 2026-11-17  
> **Status**: Reorganization Complete | Clean Modular Architecture.

---

## 1. What Was Implemented

* **Repository Restructuring**:
  - Relocated all deep documentation from root into categorized `docs/` subdirectories:
    - `docs/architecture/`: `ARCHITECTURE.md`, `DECISIONS.md`, `D3D9_MEMORY_MODEL.md`
    - `docs/development/`: `DEVELOPMENT.md`, `CONTRIBUTING.md`
    - `docs/guides/`: `GRAPHICS_GUIDE.md`
    - `docs/project/`: `PROJECT_STATE.md`, `ROADMAP.md`, `CHANGELOG.md`, `KNOWN_ISSUES.md`
    - `docs/security/`: `SECURITY.md`
  - Preserved essential entry points in root: `README.md`, `README_RU.md`, `AGENTS.md`.
  - Moved visual assets to `assets/branding/` (`banner.svg`, `logo.svg`).
* **Relative Link Remediation**:
  - Updated all relative image and document links in `README.md`, `README_RU.md`, and `AGENTS.md`.
* **Automated Testing**:
  - Verified with `tests/ZeroStutter.Tests.ps1`: AST parsing, XML validity, registry rollback pairs, and RTSS flags all pass.

---

## 2. Directory Tree

```
ZeroStutter-MTA/
├── .github/
│   └── workflows/ci.yml
├── assets/
│   └── branding/
│       ├── banner.svg
│       └── logo.svg
├── configs/
│   ├── coreconfig.template.xml
│   └── rtss/
│       └── gta_sa.exe.cfg
├── docs/
│   ├── architecture/
│   │   ├── ARCHITECTURE.md
│   │   ├── D3D9_MEMORY_MODEL.md
│   │   └── DECISIONS.md
│   ├── development/
│   │   ├── CONTRIBUTING.md
│   │   └── DEVELOPMENT.md
│   ├── guides/
│   │   └── GRAPHICS_GUIDE.md
│   ├── project/
│   │   ├── CHANGELOG.md
│   │   ├── KNOWN_ISSUES.md
│   │   ├── PROJECT_STATE.md
│   │   └── ROADMAP.md
│   └── security/
│       └── SECURITY.md
├── registry/
│   ├── disable_mpo_windowed.reg
│   ├── gta_sa_compat_flags.reg
│   ├── restore_disable_mpo_windowed.reg
│   └── restore_gta_sa_compat_flags.reg
├── scripts/
│   ├── Clear-NvidiaCache.bat
│   ├── Invoke-CleanLogs.ps1
│   └── Launch-MTAOptimized.bat
├── tests/
│   └── ZeroStutter.Tests.ps1
├── AGENTS.md
├── README.md
└── README_RU.md
```

---

## 3. Verification & Test Commands

```powershell
# 1. Run automated test suite
powershell.exe -ExecutionPolicy Bypass -File "D:\CCD\ZeroStutter-MTA\tests\ZeroStutter.Tests.ps1"

# 2. Verify git status
cd D:\CCD\ZeroStutter-MTA
git status
```
