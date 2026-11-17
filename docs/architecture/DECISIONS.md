# Architecture Decision Records (ADR) — ZeroStutter-MTA

> Log of significant engineering decisions, context, and consequences.

---

## ADR-001: Application-Specific RTSS Isolation Over Process Termination

* **Status:** Accepted  
* **Date:** 2026-11-17  

### Context
RivaTuner Statistics Server (RTSS) is widely used by PC gamers for system monitoring. However, its global Direct3D 9 Present hook collides with MTA:SA's integrity verification and causes black-screen hangs or anti-cheat warnings (`Warn #15`).

### Decision
Rather than advising users to close RTSS or force-killing the process, we deploy an application profile at `C:\Program Files (x86)\RivaTuner Statistics Server\Profiles\gta_sa.exe.cfg` with `EnableHooking=0`.

### Consequences
* **Positive:** RTSS continues monitoring other modern games seamlessly while completely disengaging from `gta_sa.exe`.
* **Positive:** Zero risk of hook collision or false anti-cheat flags.
* **Negative:** Users cannot display RTSS in-game OSD inside MTA (must use native F5 or built-in HUD).

---

## ADR-002: Hard Capping of Streaming Memory at 384 MB

* **Status:** Accepted  
* **Date:** 2026-11-17  

### Context
Many community guides erroneously recommend setting `streaming_memory` in `coreconfig.xml` to 512, 1024, or higher, assuming "more RAM = better performance". Because GTA SA is a 32-bit Large Address Aware binary capped at 4,096 MB of virtual address space, allocating 1,024 MB to vehicle geometry and textures starves the heap, causing unavoidable `0xC0000005` access violation crashes when loading dense custom vehicle fleets.

### Decision
Enforce a calibrated value of **384 MB** across all profiles.

### Consequences
* **Positive:** Prevents texture pop-in during high-speed driving while maintaining a safe 200+ MB buffer against heap fragmentation.
* **Positive:** Completely eliminates out-of-memory crashes during server rallies and car meets.

---

## ADR-003: Non-Destructive Log Truncation via Shared File Streams

* **Status:** Accepted  
* **Date:** 2026-11-17  

### Context
Client runtime logs (`clientscript.log`, `logfile.txt`, `CEGUI.log`) accumulate hundreds of thousands of lines, causing disk write contention and hitching during streaming. Simply deleting active files fails if background processes hold open file handles.

### Decision
`Invoke-CleanLogs.ps1` first copies logs to a timestamped `_backup/` directory, then performs truncation using `[System.IO.File]::WriteAllText($file, [string]::Empty)` within a `try/catch` block.

### Consequences
* **Positive:** Resets log file size to 0 bytes without breaking existing file handles or causing I/O access exceptions.
* **Positive:** Preserves full forensic history for debugging in the backup directory.

---

## ADR-004: Native D3D9 Presentation Over Third-Party API Wrappers

* **Status:** Accepted  
* **Date:** 2026-11-17  

### Context
Vulkan and D3D11 wrappers (such as DXVK and dgVoodoo2) offer modern presentation features but place foreign DLLs (`d3d9.dll`, `dxgi.dll`) into the game root.

### Decision
Strictly forbid third-party API translation layers. Optimize native D3D9 presentation via Windows DWM MPO adjustments and process priority.

### Consequences
* **Positive:** 100% compliant with server kernel anti-cheat systems (`FairplayKD.sys`, MTA AC).
* **Positive:** Zero risk of account or hardware bans.
