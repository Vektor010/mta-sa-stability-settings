# AGENTS.md — Universal AI Agent Guidelines (2026 Standard)

> **Audience**: AI Coding Agents (Claude Code, ChatGPT, Gemini, Copilot, Cursor, Windsurf, Antigravity) and Human Contributors.  
> **Status**: Living Document | Single Source of Truth for Autonomous Agents.

---

## 1. Project Context & Mission

`ZeroStutter-MTA` is a non-invasive, anti-cheat safe performance, frame-pacing, and zero-spam diagnostic toolkit for **Multi Theft Auto: San Andreas (MTA:SA)**.

MTA:SA is a 32-bit (x86) DirectX 9 application with a hard virtual address space limit of **3.7–4.0 GB (Large Address Aware)**. On heavy modification servers (such as CCDPlanet, Radmir, Province), uncalibrated settings cause:
1. Out-of-memory crashes (`0xC0000005` Access Violation).
2. Direct3D 9 Present hook collisions with monitoring software (RTSS, OBS, Discord).
3. Severe disk I/O micro-stutters caused by uncontrolled log spam (`clientscript.log`, `CEGUI.log`, `cefdebug.txt`).
4. Windows 11 DWM Multi-Plane Overlay (MPO) frame pacing hitches in borderless mode.

**Core Mission**: Deliver deterministic, verified stability without violating kernel-level anti-cheat engines (`FairplayKD.sys`, MTA AC).

---

## 2. Invariant Engineering Rules (Agent Boundaries)

Any AI Agent modifying this repository MUST enforce the following constraints:

1. **ZERO INJECTION TOLERANCE**:
   - **NEVER** place third-party wrappers (`d3d9.dll`, `dxgi.dll`, `dinput8.dll`, ENB, ReShade, DXVK) inside the game directories.
   - Doing so trips kernel anti-cheat heuristics (`FairplayKD.sys`, MTA `AC #4` / `Warn #15`) resulting in permanent hardware/serial bans.
2. **STRICT 32-BIT MEMORY CONFINEMENT**:
   - `streaming_memory` in `coreconfig.xml` must NEVER exceed **384 MB**.
   - Setting it to 512–1024 MB exhausts the 32-bit address space, causing guaranteed crashes during dense vehicle streaming.
3. **IDEMPOTENCE & NON-DESTRUCTIVE ROLLBACK**:
   - Any script making configuration changes MUST generate a timestamped backup before touching target files.
   - Every registry tweak (`.reg`) MUST have a corresponding `restore_*.reg` file.
4. **NO SYNTHETIC CLAIMS**:
   - Never invent fictitious FPS numbers. All telemetry claims must reference real presentmon/frametime logs or documented D3D9 metrics.

---

## 3. Repository Architecture Map

```
ZeroStutter-MTA/
├── .github/
│   └── workflows/ci.yml         # CI pipeline
├── assets/
│   └── branding/                # Vector assets (banner.svg, logo.svg)
├── configs/                     # Reference configuration templates
│   ├── coreconfig.template.xml  # Calibrated MTA configuration
│   └── rtss/gta_sa.exe.cfg      # RTSS hook exclusion profile
├── docs/                        # Modular technical documentation
│   ├── architecture/
│   │   ├── ARCHITECTURE.md      # D3D9 & memory subsystem design
│   │   ├── DECISIONS.md         # Architecture Decision Records (ADR)
│   │   └── D3D9_MEMORY_MODEL.md # 32-bit LAA calculations
│   ├── development/
│   │   ├── CONTRIBUTING.md      # Developer contribution guidelines
│   │   └── DEVELOPMENT.md       # Local testing & build environment
│   ├── guides/
│   │   └── GRAPHICS_GUIDE.md    # In-game slider reference guide
│   ├── project/
│   │   ├── CHANGELOG.md         # Semantic release history
│   │   ├── KNOWN_ISSUES.md      # Upstream bugs & hardware boundaries
│   │   ├── PROJECT_STATE.md     # Active session state & handoff
│   │   └── ROADMAP.md           # Strategic release roadmap
│   └── security/
│       └── SECURITY.md          # Anti-cheat compliance & reporting
├── registry/                    # DWM & Windows compatibility tweaks
│   ├── disable_mpo_windowed.reg
│   ├── restore_disable_mpo_windowed.reg
│   ├── gta_sa_compat_flags.reg
│   └── restore_gta_sa_compat_flags.reg
├── scripts/                     # Core automation tools
│   ├── Clear-NvidiaCache.bat    # NVIDIA DXCache cleaner
│   ├── Invoke-CleanLogs.ps1     # Automated log backup & zeroing
│   └── Launch-MTAOptimized.bat  # High priority launcher
├── tests/                       # Automated validation suite
│   └── ZeroStutter.Tests.ps1    # AST & schema verification tests
├── AGENTS.md                    # Universal AI agent instructions (this file)
├── README.md                    # Primary international documentation
└── README_RU.md                 # Native Russian documentation
```

---

## 4. Standard Agent Workflow for Tasks

When an AI Agent is prompted to continue or extend this repository:

1. **Read State First**: Check `docs/project/PROJECT_STATE.md` to identify the last completed milestone and pending items.
2. **Execute Tests**: Run `powershell -File tests\ZeroStutter.Tests.ps1` to ensure the existing tree is clean.
3. **Make Atomic Changes**: Only edit or add files within the defined architecture.
4. **Verify AST & Formatting**: Run syntax validation on any modified PowerShell or Batch files.
5. **Update State**: Append your changes, test results, and next recommendations to `docs/project/PROJECT_STATE.md`.

---

## 5. Verification Commands

```powershell
# 1. Run full test suite (AST, config validation, registry matching)
powershell.exe -ExecutionPolicy Bypass -File "tests\ZeroStutter.Tests.ps1"

# 2. Test clean script in DryRun / Execution mode
powershell.exe -ExecutionPolicy Bypass -File "scripts\Invoke-CleanLogs.ps1" -GameRoot "D:\CCD"

# 3. Check git tree status
git status
```
