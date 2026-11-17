# Known Issues & Hardware Edge-Cases — ZeroStutter-MTA

> Catalog of documented upstream engine behaviors, OS interactions, and architectural boundaries.

---

## 1. Upstream Engine Limitations (MTA:SA 1.6.x)

* **32-Bit Address Space Ceiling:**
  The MTA client remains a 32-bit (x86) application. No software modification can lift the 4,096 MB Large Address Aware limit until the upstream MTA 1.7 64-bit client branch is stabilized and deployed by server operators.
* **Upstream Bug #5550 (Disconnect / Reconnect Race):**
  Rapid reconnects without terminating `gta_sa.exe` can leak D3D9 device pools. Always restart the game client if switching servers after long sessions.
* **Upstream Bug #5501 (Alpha Sorting with Skybox):**
  Vehicles featuring glass or light textures with alpha values under 140 can appear partially occluded by distant skybox shaders. This is an engine-level D3D9 depth sorting limitation.

---

## 2. Windows 11 DWM & Multi-Plane Overlay (MPO)

* **Behavior:** On Windows 11 (22H2 through 24H2+), the Desktop Window Manager attempts to promote borderless Direct3D 9 windows into dedicated hardware overlay planes. On certain GPU driver branches, this introduces micro-stutters and 1–2 frame presentation delays.
* **Mitigation:** Apply `registry/disable_mpo_windowed.reg` and restart the system.

---

## 3. Multi-CCD and 3D V-Cache Processors (AMD Ryzen 7900X3D / 7950X3D / 9950X)

* **Behavior:** Dual-CCD processors featuring one 3D V-Cache die and one frequency die may schedule `gta_sa.exe` threads onto the non-V-Cache CCD if Windows Game Bar / CPPC drivers fail to classify MTA as a game.
* **Mitigation:** On single-CCD V-Cache CPUs (Ryzen 7800X3D / 9800X3D / 9850X3D), all 8 physical cores have direct access to the 3D V-Cache, requiring no manual pinning. On dual-CCD models, use Process Lasso or set process affinity to CCD0 (Cores 0–15).
