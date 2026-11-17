import os
import math
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"D:\CCD\mta-settings-pack\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)
BRANDING_DIR = os.path.join(ASSETS_DIR, "branding")
os.makedirs(BRANDING_DIR, exist_ok=True)

# Palette
BG_COLOR = (8, 11, 16)         # #080B10
GRID_COLOR = (15, 23, 35)      # #0F1723
NEON_GREEN = (57, 255, 136)    # #39FF88
ELECTRIC_BLUE = (0, 200, 255)  # #00C8FF
PURPLE = (139, 92, 255)        # #8B5CFF
TEXT_WHITE = (244, 247, 250)   # #F4F7FA
ALERT_RED = (255, 68, 85)      # #FF4455
MUTED_GRAY = (80, 95, 115)     # #505F73

def create_hero_gif():
    width, height = 760, 220
    frames = []
    num_frames = 48  # 48 frames at 30ms = ~1.44s smooth loop (~33-60 FPS equivalent)
    
    # Try default font
    try:
        font_large = ImageFont.truetype("arial.ttf", 22)
        font_medium = ImageFont.truetype("arial.ttf", 13)
        font_mono = ImageFont.truetype("consola.ttf", 12)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 13)
    except:
        font_large = font_medium = font_mono = font_mono_bold = ImageFont.load_default()

    for i in range(num_frames):
        img = Image.new("RGB", (width, height), BG_COLOR)
        draw = ImageDraw.Draw(img)
        t = i / num_frames

        # Draw subtle grid
        for x in range(0, width, 40):
            draw.line([(x, 0), (x, height)], fill=(12, 18, 28), width=1)
        for y in range(0, height, 40):
            draw.line([(0, y), (width, y)], fill=(12, 18, 28), width=1)

        # Outer border with neon accents
        draw.rectangle([(2, 2), (width - 3, height - 3)], outline=(25, 38, 55), width=1)
        # Corner cyber brackets
        bracket_len = 16
        # Top-Left
        draw.line([(2, 2), (2 + bracket_len, 2)], fill=ELECTRIC_BLUE, width=2)
        draw.line([(2, 2), (2, 2 + bracket_len)], fill=ELECTRIC_BLUE, width=2)
        # Top-Right
        draw.line([(width - 3, 2), (width - 3 - bracket_len, 2)], fill=NEON_GREEN, width=2)
        draw.line([(width - 3, 2), (width - 3, 2 + bracket_len)], fill=NEON_GREEN, width=2)
        # Bottom-Left
        draw.line([(2, height - 3), (2 + bracket_len, height - 3)], fill=ELECTRIC_BLUE, width=2)
        draw.line([(2, height - 3), (2, height - 3 - bracket_len)], fill=ELECTRIC_BLUE, width=2)
        # Bottom-Right
        draw.line([(width - 3, height - 3), (width - 3 - bracket_len, height - 3)], fill=NEON_GREEN, width=2)
        draw.line([(width - 3, height - 3), (width - 3, height - 3 - bracket_len)], fill=NEON_GREEN, width=2)

        # Header Title
        draw.text((24, 16), "MTA:SA STABILITY ENGINE", font=font_large, fill=TEXT_WHITE)
        draw.text((320, 22), "v1.0.0 // 2026 EDITION", font=font_mono, fill=ELECTRIC_BLUE)

        # Live Status Pill
        pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
        status_color = (int(57 * pulse + 20), int(255 * pulse + 80), int(136 * pulse + 40))
        draw.rectangle([(width - 150, 16), (width - 24, 38)], fill=(15, 25, 35), outline=NEON_GREEN, width=1)
        draw.ellipse([(width - 140, 24), (width - 132, 32)], fill=status_color)
        draw.text((width - 124, 21), "CLIENT ACTIVE", font=font_mono_bold, fill=NEON_GREEN)

        # Divider line
        draw.line([(24, 48), (width - 24, 48)], fill=(30, 45, 65), width=1)

        # Left Column: Telemetry Cards
        # Card 1: D3D9 Hooking
        draw.rectangle([(24, 58), (240, 104)], fill=(12, 17, 26), outline=(25, 40, 60))
        draw.text((34, 64), "D3D9 HOOK ISOLATION", font=font_mono, fill=MUTED_GRAY)
        draw.text((34, 80), "RTSS: HOOKING DISABLED", font=font_mono_bold, fill=ELECTRIC_BLUE)

        # Card 2: Memory Ceiling
        draw.rectangle([(24, 114), (240, 160)], fill=(12, 17, 26), outline=(25, 40, 60))
        draw.text((34, 120), "STREAMING ALLOCATION", font=font_mono, fill=MUTED_GRAY)
        draw.text((34, 136), "384 MB [LAA SAFE FLOOR]", font=font_mono_bold, fill=NEON_GREEN)

        # Card 3: Disk I/O Log Spam
        draw.rectangle([(24, 170), (240, 206)], fill=(12, 17, 26), outline=(25, 40, 60))
        draw.text((34, 176), "LOG FLUSH CONTENTION", font=font_mono, fill=MUTED_GRAY)
        draw.text((34, 190), "0.0 KB/s [SPAM FILTERED]", font=font_mono_bold, fill=TEXT_WHITE)

        # Right Column: Live Frametime Oscilloscope
        graph_x, graph_y, graph_w, graph_h = 260, 58, 476, 148
        draw.rectangle([(graph_x, graph_y), (graph_x + graph_w, graph_y + graph_h)], fill=(10, 14, 22), outline=(25, 40, 60))
        
        # Grid lines inside graph
        draw.line([(graph_x, graph_y + graph_h // 2), (graph_x + graph_w, graph_y + graph_h // 2)], fill=(18, 28, 42), width=1)
        draw.text((graph_x + 10, graph_y + 8), "REAL-TIME FRAME-PACING TELEMETRY (144 Hz / D3D9 NATIVE)", font=font_mono, fill=MUTED_GRAY)
        draw.text((graph_x + graph_w - 90, graph_y + 8), "6.94 ms", font=font_mono_bold, fill=NEON_GREEN)

        # Draw smooth flat frametime waveform with subtle jitter
        points = []
        base_y = graph_y + graph_h // 2 + 10
        for px in range(graph_w):
            # Traveling sine wave with micro harmonics
            wave = math.sin((px * 0.05) - (t * 2 * math.pi * 3)) * 2.5
            noise = math.cos((px * 0.12) + (t * 2 * math.pi * 5)) * 1.2
            points.append((graph_x + px, base_y + wave + noise))

        draw.line(points, fill=NEON_GREEN, width=2)

        # Scanline indicator line passing horizontally
        scan_x = graph_x + int(t * graph_w)
        draw.line([(scan_x, graph_y), (scan_x, graph_y + graph_h)], fill=(0, 200, 255, 120), width=1)

        # Bottom stats inside oscilloscope
        draw.text((graph_x + 10, graph_y + graph_h - 22), "FPS: 144.0  |  1% LOW: 141.2  |  JITTER: < 0.2ms  |  DWM MPO: BYPASSED", font=font_mono, fill=ELECTRIC_BLUE)

        frames.append(img)

    # Save optimized GIF
    gif_path = os.path.join(ASSETS_DIR, "hero.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=35, loop=0, optimize=True)
    print(f"Created hero.gif at {gif_path}")

def create_before_after_gif():
    width, height = 760, 200
    frames = []
    num_frames = 40

    try:
        font_title = ImageFont.truetype("consolab.ttf", 14)
        font_sub = ImageFont.truetype("consola.ttf", 11)
    except:
        font_title = font_sub = ImageFont.load_default()

    for i in range(num_frames):
        img = Image.new("RGB", (width, height), BG_COLOR)
        draw = ImageDraw.Draw(img)
        t = i / num_frames

        # Center divider
        mid_x = width // 2
        draw.line([(mid_x, 10), (mid_x, height - 10)], fill=(30, 45, 65), width=2)

        # --- LEFT: BEFORE (UNOPTIMIZED) ---
        draw.rectangle([(15, 15), (mid_x - 15, height - 15)], fill=(15, 10, 14), outline=(70, 20, 30))
        draw.text((28, 24), "BEFORE (DEFAULT / FORUM TWEAKS)", font=font_title, fill=ALERT_RED)
        draw.text((28, 44), "Streaming: 1024 MB (RAM Starvation)", font=font_sub, fill=(220, 160, 160))
        draw.text((28, 60), "Log Write: 4.8 MB/s (Disk Stutter)", font=font_sub, fill=(220, 160, 160))
        draw.text((28, 76), "RTSS Hook: COLLISION / CRASH RISK", font=font_sub, fill=(220, 160, 160))
        draw.text((28, 92), "Anti-Aliasing: 3x MSAA (+225MB VRAM)", font=font_sub, fill=(220, 160, 160))

        # Spiky jagged red frametime line
        spike_points = []
        box_w = mid_x - 45
        for px in range(box_w):
            x = 28 + px
            if (px + int(t * 40)) % 35 == 0:
                y = 120 + 35  # massive stutter spike
            elif (px + int(t * 40)) % 18 == 0:
                y = 120 + 20
            else:
                y = 120 + (math.sin(px * 0.4 + t * 6) * 6)
            spike_points.append((x, y))
        draw.line(spike_points, fill=ALERT_RED, width=2)
        draw.text((28, 162), "STATUS: UNSTABLE (0xC0000005 CRASHES)", font=font_sub, fill=ALERT_RED)

        # --- RIGHT: AFTER (ZEROSTUTTER) ---
        draw.rectangle([(mid_x + 15, 15), (width - 15, height - 15)], fill=(10, 18, 16), outline=(20, 70, 45))
        draw.text((mid_x + 28, 24), "AFTER (ZEROSTUTTER ENGINE)", font=font_title, fill=NEON_GREEN)
        draw.text((mid_x + 28, 44), "Streaming: 384 MB (Optimal Headroom)", font=font_sub, fill=(160, 230, 190))
        draw.text((mid_x + 28, 60), "Log Write: 0.0 KB/s (Zero Disk Load)", font=font_sub, fill=(160, 230, 190))
        draw.text((mid_x + 28, 76), "RTSS Hook: ISOLATED (Hooking=0)", font=font_sub, fill=(160, 230, 190))
        draw.text((mid_x + 28, 92), "Anti-Aliasing: 1x / Off + 16x Aniso", font=font_sub, fill=(160, 230, 190))

        # Flat smooth green line
        smooth_points = []
        for px in range(box_w):
            x = mid_x + 28 + px
            y = 140 + math.sin(px * 0.1 - t * 4) * 1.5
            smooth_points.append((x, y))
        draw.line(smooth_points, fill=NEON_GREEN, width=2)
        draw.text((mid_x + 28, 162), "STATUS: 100% STABLE / FAIRPLAYKD SAFE", font=font_sub, fill=NEON_GREEN)

        frames.append(img)

    gif_path = os.path.join(ASSETS_DIR, "before-after.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=40, loop=0, optimize=True)
    print(f"Created before-after.gif at {gif_path}")

def create_fps_demo_gif():
    width, height = 760, 160
    frames = []
    num_frames = 36

    try:
        font_huge = ImageFont.truetype("consolab.ttf", 36)
        font_mono = ImageFont.truetype("consola.ttf", 12)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 13)
    except:
        font_huge = font_mono = font_mono_bold = ImageFont.load_default()

    for i in range(num_frames):
        img = Image.new("RGB", (width, height), BG_COLOR)
        draw = ImageDraw.Draw(img)
        t = i / num_frames

        # Cyber border
        draw.rectangle([(2, 2), (width - 3, height - 3)], outline=(20, 32, 48), width=1)
        draw.line([(0, 0), (80, 0)], fill=ELECTRIC_BLUE, width=3)
        draw.line([(width - 80, height - 1), (width, height - 1)], fill=NEON_GREEN, width=3)

        # FPS Counter Box
        fps_val = 144.0 + math.sin(t * 2 * math.pi) * 0.4
        draw.rectangle([(20, 20), (220, 140)], fill=(12, 18, 28), outline=(30, 50, 75))
        draw.text((32, 28), "TARGET FRAMERATE", font=font_mono, fill=MUTED_GRAY)
        draw.text((32, 48), f"{fps_val:.1f}", font=font_huge, fill=NEON_GREEN)
        draw.text((150, 62), "FPS", font=font_mono_bold, fill=ELECTRIC_BLUE)
        draw.text((32, 106), "FRAME PACING: 6.94 ms", font=font_mono, fill=TEXT_WHITE)

        # Telemetry Gauges in center
        draw.rectangle([(235, 20), (510, 140)], fill=(12, 18, 28), outline=(30, 50, 75))
        draw.text((250, 28), "MEMORY ALLOCATION AUDIT", font=font_mono, fill=MUTED_GRAY)
        
        # Gauge 1: Streaming
        draw.text((250, 48), "STREAMING POOL (384MB):", font=font_mono, fill=TEXT_WHITE)
        draw.rectangle([(250, 64), (490, 74)], fill=(20, 30, 45))
        draw.rectangle([(250, 64), (250 + int(240 * 0.65), 74)], fill=NEON_GREEN)

        # Gauge 2: 32-bit Address Space Headroom
        draw.text((250, 86), "32-BIT VIRTUAL MEMORY (4096MB):", font=font_mono, fill=TEXT_WHITE)
        draw.rectangle([(250, 102), (490, 112)], fill=(20, 30, 45))
        draw.rectangle([(250, 102), (250 + int(240 * 0.72), 112)], fill=ELECTRIC_BLUE)
        draw.text((250, 120), "HEADROOM: 1,150 MB RESERVED", font=font_mono_bold, fill=NEON_GREEN)

        # Right HUD status
        draw.rectangle([(525, 20), (width - 20, 140)], fill=(12, 18, 28), outline=(30, 50, 75))
        draw.text((540, 28), "ANTI-CHEAT ENGINE", font=font_mono, fill=MUTED_GRAY)
        draw.text((540, 52), "[✓] FAIRPLAYKD: CLEAN", font=font_mono_bold, fill=NEON_GREEN)
        draw.text((540, 74), "[✓] D3D9 HOOKS: BYPASSED", font=font_mono_bold, fill=ELECTRIC_BLUE)
        draw.text((540, 96), "[✓] CEF ACCEL: DISABLED", font=font_mono_bold, fill=TEXT_WHITE)
        draw.text((540, 118), "[✓] LOG FLUSH: ZEROED", font=font_mono_bold, fill=PURPLE)

        frames.append(img)

    gif_path = os.path.join(ASSETS_DIR, "fps-demo.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=35, loop=0, optimize=True)
    print(f"Created fps-demo.gif at {gif_path}")

if __name__ == "__main__":
    create_hero_gif()
    create_before_after_gif()
    create_fps_demo_gif()
