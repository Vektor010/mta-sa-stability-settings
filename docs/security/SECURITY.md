# Security Policy & Anti-Cheat Compliance — ZeroStutter-MTA

---

## 1. Anti-Cheat Compliance Guarantee

ZeroStutter-MTA is designed to be **100% compliant** with all major MTA:SA server security frameworks, including:
* Native Multi Theft Auto Anti-Cheat (`MTA AC`, modules 1 through 23).
* Server-side kernel integrity drivers (e.g. `FairplayKD.sys` on CCDPlanet).
* Community server integrity checks.

### Why ZeroStutter-MTA is Safe:
1. **No Code Injection:** ZeroStutter does not inject threads, DLLs, or hooks into the `gta_sa.exe` process.
2. **No Binary Modification:** The original game binaries (`gta_sa.exe`, `proxy_sa.exe`) and MTA libraries are never modified.
3. **No File Overrides:** We do not replace system or DirectX runtime DLLs.
4. **Standard API Configuration:** Settings are applied via standard XML parameters recognized by MTA's built-in settings parser.

---

## 2. Reporting Security Vulnerabilities

If you identify a configuration or script in this repository that triggers a false-positive anti-cheat warning or exposes user systems to instability, please report it via GitHub Private Vulnerability Reporting or open an issue labeled `security`.
