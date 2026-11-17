# DirectX 9 Memory Model & Anti-Aliasing Overhead in MTA

> Technical Analysis of Render Targets, VRAM Virtualization, and LAA Limitations.

---

## 1. Render Target Allocation at 1440p / 4K

Direct3D 9 handles anti-aliasing via multisample render targets created at device initialization. Unlike modern deferred engines (TAA, DLSS, FSR), MTA:SA relies on native MSAA:

* When **3x Anti-Aliasing** (Direct3D 9 8x MSAA) is selected at **2560x1440x32**:
  $$\text{Color Buffer} = 2560 \times 1440 \times 4 \text{ bytes} \approx 14.06 \text{ MB}$$
  $$\text{Multisample Color (8x)} = 14.06 \times 8 \approx 112.5 \text{ MB}$$
  $$\text{Depth/Stencil (D24S8, 8x)} = 2560 \times 1440 \times 4 \times 8 \approx 112.5 \text{ MB}$$
  $$\text{Total Swapchain Overhead} \approx 225 \text{ MB}$$

In a 32-bit application, GPU resources allocated without hardware virtual memory pagination consume critical entries in the process address translation table. When combined with hundreds of uncompressed 2048x2048 car body textures, MSAA 3x pushes the process over the 3.8 GB allocation threshold.

---

## 2. Anisotropic Filtering: Free Texture Sharpness

Unlike MSAA, **16x Anisotropic Filtering** (`<anisotropic>4</anisotropic>` in `coreconfig.xml`) does not allocate additional render targets. 
* Modern GPUs (such as RTX 40/50 series and Radeon 7000/8000 series) perform anisotropic texture sampling in hardware texture units with less than 0.1% performance penalty.
* **Recommendation:** Keep Anisotropic Filtering at **16x (level 4)** for maximum clarity on road markings, asphalt, and custom vehicle liveries.

---

## 3. Comparison of Anti-Aliasing Modes in MTA

| Anti-Aliasing Level | D3D9 MSAA Level | VRAM / Address Space Overhead | Recommended Resolution | Visual Result |
| :--- | :--- | :--- | :--- | :--- |
| **Off (0x)** | None | **0 MB** | 1440p / 4K | Crisp, high FPS, zero crash risk |
| **1x** | 2x MSAA | **~56 MB** | 1080p | Minor edge smoothing, low impact |
| **2x** | 4x MSAA | **~112 MB** | 1080p | Balanced, moderate memory load |
| **3x** | 8x MSAA | **~225 MB** | 720p / 1080p only | ⚠️ **High risk of 0xC0000005 crash at 1440p+** |

**Conclusion:** At 2560x1440 and above, pixel density is already high enough that edge aliasing is minimal. Running **Off** or **1x** provides a massive stability boost.
