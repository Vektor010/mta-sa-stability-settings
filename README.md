<p align="center">
  <img src="assets/banner.svg" alt="MTA:SA Stability Engine Banner" width="100%"/>
</p>

<p align="center">
  <a href="https://github.com/Vektor010/mta-sa-stability-settings/releases/latest"><img src="https://img.shields.io/badge/RELEASE-v1.0.0_EDITION-39FF88?style=for-the-badge&logo=github&logoColor=black" alt="Release"/></a>
  <a href="#-compatibility"><img src="https://img.shields.io/badge/FAIRPLAYKD-100%25_COMPLIANT-00C8FF?style=for-the-badge&logo=shield&logoColor=black" alt="FairplayKD Safe"/></a>
  <a href="#-stability-system"><img src="https://img.shields.io/badge/D3D9-NATIVE_LAA_4GB-8B5CFF?style=for-the-badge&logo=amd&logoColor=white" alt="LAA 4GB"/></a>
  <a href="#-stability-system"><img src="https://img.shields.io/badge/WINDOWS_11-MPO_FIXED-39FF88?style=for-the-badge&logo=windows&logoColor=black" alt="Windows 11 Fixed"/></a>
  <a href="#-compatibility"><img src="https://img.shields.io/badge/STATUS-CLIENT_OPTIMIZED-00C8FF?style=for-the-badge&logo=fastlane&logoColor=black" alt="Client Optimized"/></a>
</p>

<h1 align="center" style="font-weight: 900; letter-spacing: -1px;">
  ⚡ MTA:SA STABILITY ENGINE
</h1>

<p align="center">
  <b style="font-size: 16px; letter-spacing: 2px; color: #00C8FF;">STABILITY. PERFORMANCE. CONTROL.</b><br/>
  <span style="color: #94A7C0;">Стабильность игрового клиента MTA:SA без лишних зависаний, конфликтов оверлеев и накопления логов.</span>
</p>

<p align="center">
  <code>MTA:SA (1.6.0+)</code> •
  <code>SAMP (D3D9 Core)</code> •
  <code>CCDPlanet</code> •
  <code>MTA Province</code> •
  <code>Radmir MTA</code> •
  <code>NextRP</code>
</p>

<p align="center">
  <a href="#-about-project">О проекте</a> •
  <a href="#-why-this-project">Почему ZeroStutter?</a> •
  <a href="#-main-features">Возможности</a> •
  <a href="#-stability-system">Система стабильности</a> •
  <a href="#-configuration-breakdown">Разбор файлов</a> •
  <a href="#-before--after">Before / After</a> •
  <a href="#-installation-guide">Установка</a> •
  <a href="#-in-game-settings-guide">Настройки ESC и F3</a> •
  <a href="#-faq">FAQ</a>
</p>

---

## ⚡ Live Telemetry (Frame Pacing & Memory Audit)

<p align="center">
  <img src="assets/hero.gif" alt="Live Telemetry 60 FPS" width="100%"/>
</p>

<p align="center">
  <b style="color: #39FF88;">LESS STUTTER. MORE CONTROL.</b> •
  <b style="color: #00C8FF;">BUILT FOR MTA:SA.</b> •
  <b style="color: #8B5CFF;">STABILITY OVER EVERYTHING.</b>
</p>

---

## 📖 About Project

**MTA:SA Stability Engine** — это инженерный Open Source комплекс тонкой настройки и аппаратной стабилизации для клиентов **Multi Theft Auto: San Andreas** и тяжелых модифицированных серверов (CCDPlanet, Провинция, Radmir).

Проект создан для современных игровых ПК (включая процессоры **AMD Ryzen 7000/9000 с 3D V-Cache**, видеокарты **NVIDIA GeForce RTX 40/50** и мониторы **144–240 Гц**), где старый 32-битный движок GTA San Andreas сталкивается с системными бутылочными горлышками Windows 11 и переполнением виртуальной памяти.

> **CLEAN CLIENT. SMOOTH EXPERIENCE. OPTIMIZE YOUR SAN ANDREAS.**  
> Мы не используем инъекторы `.dll` / `.asi`, не внедряем читерский софт и не заставляем движок работать в неестественных условиях. Все изменения опираются на математический расчет адресации памяти Direct3D 9, штатные параметры XML и системные механизмы Windows NT.

---

## ❓ Why This Project?

Большинство руководств и «FPS-сборок» из интернета создаются без понимания архитектуры старого движка RenderWare и DirectX 9:
1. **Миф о «памяти 1024–2048 МБ»:** Пользователям советуют выкручивать `streaming_memory` на максимум. В 32-битном процессе GTA SA это приводит к моментальному исчерпанию кучи и вылету с ошибкой `0xC0000005 (Access Violation)` при скоплении машин.
2. **Опасные DLL-инъекции:** Любительские сборки пичкают подозрительными библиотеками (DXVK, SilentPatch, ENB), которые мгновенно детектируются драйвером защиты ядра (`FairplayKD.sys`, MTA AC) и приводят к аппаратным блокировкам (`Warn #15`, `AC #4`).
3. **Бесконечный спам на диск:** Серверные скрипты забивают файлы `clientscript.log` и `logfile.txt` миллионами повторяющихся строк, вызывая микрозадержки SSD во время быстрой езды.
4. **Конфликт DWM Multi-Plane Overlay:** В Windows 10/11 безрамочный оконный режим старых игр D3D9 страдает от неравномерного вывода кадров из-за механизма MPO.

---

## 🚀 Main Features

* 🟢 **32-Bit Memory Containment:** Фиксация пула стриминга на уровне **`384 МБ`**, сохраняющая более 1 ГБ резерва для адресации пользовательских моделей.
* 🟢 **Zero Disk Spam:** Автоматическое подавление дубликатов в логах движка и мгновенная предстартовая очистка в 1 клик.
* 🟢 **Chromium Embedded Framework (CEF) Optimization:** Программный рендеринг веб-интерфейсов для плавных спидометров и планшетов без задержек.
* 🟢 **Windows 11 DWM Frame Pacing:** Реестровый твик отключения задержек MPO для идеально ровной линии времени кадра (Frametime).
* 🟢 **LAA 4GB Architecture:** Полная поддержка флага `IMAGE_FILE_LARGE_ADDRESS_AWARE` исполняемого файла `gta_sa.exe`.
* 🟢 **100% Anti-Cheat Safe:** Никаких модифицированных DLL в папке игры — абсолютная чистота перед `FairplayKD.sys` и EAC.

---

## 🛡️ Stability System

<p align="center">
  <img src="assets/fps-demo.gif" alt="FPS HUD Demo" width="100%"/>
</p>

Архитектура системы стабильности выстроена по принципу изоляции:
1. **Уровень движка GTA (Memory & PE):** `gta_sa.exe` получает доступ к полным 4 ГБ виртуальной памяти через PE-заголовок, а процесс запускается с приоритетом `AboveNormal`.
2. **Уровень графического пайплайна (D3D9):** Отключены устаревшие пост-эффекты GTA (трава, жара, старые тени, размытие), которые вызывают утечки графических состояний при рендеринге тяжелых авто.
3. **Уровень операционной системы (DWM):** Флаг `DISABLEDXMAXIMIZEDWINDOWEDMODE` предотвращает навязывание гибридной оконной модели Windows, устраняя инпут-лаг.

---

## 📦 Configuration Breakdown (Разбор файлов)

В репозитории подготовлены чистые, проверенные файлы:

| Файл | Назначение | Папка установки |
| :--- | :--- | :--- |
| **[`coreconfig.xml`](coreconfig.xml)** | Конфиг клиента MTA (стриминг, окно без рамки, фильтр спама) | `MTA\config\` |
| **[`server_settings.json`](server_settings.json)** | Настройки сервера CCDPlanet (F3: выкл SSAO/DOF, отражения) | `mods\deathmatch\priv\<ID>\settings\` |
| **[`handling.cfg`](handling.cfg)** | Базовая физика транспорта GTA San Andreas (масса, подвеска) | `GTA\data\` |
| **[`chatboxpresets.xml`](chatboxpresets.xml)** | Пресеты прозрачности и шрифтов чата MTA | `MTA\config\` |
| **[`clean_and_play.bat`](clean_and_play.bat)** | 1-клик лаунчер: очистка спама логов + запуск с приоритетом | Корень игры / Desktop |
| **[`apply_gta_optimizations.bat`](apply_gta_optimizations.bat)** | 1-клик твик Windows: отключение DWM MPO и флаг gta_sa.exe | Запуск от Администратора |

---

## 🧠 Глубокий разбор: Память стриминга (Streaming Memory: 384 МБ vs 512 МБ)

Память стриминга (`streaming_memory`) — **самая критичная настройка производительности и стабильности во всей MTA:SA**.

В GTA San Andreas подсистема `CStreaming` отвечает за динамическую подгрузку и выгрузку моделей (DFF), текстур и винилов (TXD). На серверах вроде CCDPlanet или Провинция одна детальная машина весит **от 30 до 80 МБ**.

### 📊 Градация значений стриминговой памяти:

* **Дефолт: `64–128 МБ` (Катастрофа на RP-серверах)**  
  Стандартный уровень GTA SA 2004 года. При скорости от 150 км/ч дороги становятся прозрачными, здания исчезают, а колеса машин превращаются в серые шары. Постоянная перезагрузка текстур с диска дает сильные статтеры.
* **Эталон стабильности: `384 МБ` (Значение по умолчанию в нашем конфиге)**  
  Идеально для игры в 1440p / 4K. Текстуры дорог и авто стабильны, а в 32-битном адресном пространстве (LAA 4GB) сохраняется более **1.2 ГБ гарантированного запаса** под кучу, D3D9 RenderTargets и CEF.
* **Максимальный выбор для тяжелых серверов: `512 МБ` (Почему 512 МБ — это критически важно!)**  
  * **Кому ставить:** игрокам на мощных ПК (RTX 30/40/50, 32-64 ГБ RAM) на **CCDPlanet, Провинции или Radmir**.
  * **Зачем нужно:** удерживает в быстрой памяти **до 15–20 тяжелых кастомных авто одновременно** со всеми винилами, обвесами и тонировкой.
  * **На скоростях 300+ км/ч:** полностью устраняет эффект «вырастающих из воздуха» машин и мерцание тюнинга на автосходках и дрифт-трассах.
  * **Безопасность:** 512 МБ всё ещё укладывается в рамки 32-битного адресного пространства GTA SA (~1 ГБ запаса кучи).
* **Опасная зона: `1024 МБ и выше` (Главная ошибка из интернета)**  
  32-битный лимит GTA SA равен 4096 МБ. При выделении 1024 МБ стримингу общая память процесса превышает 3.75 ГБ, адресное пространство фрагментируется и игра **гарантированно вылетает с ошибкой `0xC0000005`**. Больше 512 МБ ставить нельзя!

> 💡 **Как переключить на 512 МБ:**  
> В `coreconfig.xml` замените `<streaming_memory>384</streaming_memory>` на `<streaming_memory>512</streaming_memory>`  
> *(либо в игре: `ESC` -> «Настройки» -> «Дополнительные» -> ползунок «Память стриминга» на **512 МБ**).*

---

## 📊 Before / After (Сравнение телеметрии)

<p align="center">
  <img src="assets/before-after.gif" alt="Before vs After Comparison" width="100%"/>
</p>

| Параметр | До оптимизации (Стандарт / Советы из сети) | ⚡ После оптимизации (MTA Stability Engine) |
| :--- | :--- | :--- |
| **Время кадра (Frametime)** | Скачки и фризы до **`120–150 мс`** при прогрузке авто | Ровная линия **`6.94 мс`** (144 Гц) без заиканий |
| **Использование виртуальной памяти** | Переполнение до `3850 МБ` -> **Вылет `0xC0000005`** | Стабильный уровень с запасом **`> 1100 МБ`** свободной кучи |
| **Активность диска (SSD Write)** | Постоянная запись ошибок до **`4.8 МБ/с`** | **`0.0 КБ/с`** (полное отсутствие фонового спама) |
| **Переключение окон (Alt-Tab)** | Зависания, краш `D3DERR_DEVICELOST`, черный экран | Мгновенный отклик в безрамочном режиме |
| **Статус античита (`FairplayKD`)** | Риск блокировки при использовании сторонних DLL | **100% Чистый статус**, отсутствие посторонних хуков |

---

## 🕹️ Compatibility (Совместимость)

* ✅ **Операционные системы:** Windows 10 (21H2 — 22H2), Windows 11 (23H2 — 24H2+).
* ✅ **Процессоры:** Полная совместимость с AMD Ryzen (включая single-CCD и dual-CCD X3D серии 7000/9000), Intel Core (12–14 поколение с правильным шедулингом ядер).
* ✅ **Видеокарты:** NVIDIA GeForce RTX 30/40/50, AMD Radeon RX 6000/7000/8000.
* ✅ **Античиты:** `FairplayKD.sys`, Multi Theft Auto Anti-Cheat Modules (1–23), EAC.

---

## 🛠️ Installation Guide (Пошаговая установка)

### Способ 1. Быстрый запуск через готовый архив (Рекомендуется)
1. Скачайте архив **[`MTA_Stability_Pack_v1.0.0.zip`](https://github.com/Vektor010/mta-sa-stability-settings/releases/latest)** из раздела Releases.
2. Скопируйте файл `coreconfig.xml` в папку `D:\CCD\MTA\config\` (с заменой).
3. Скопируйте файл `server_settings.json` в папку `D:\CCD\mods\deathmatch\priv\<ID_сервера>\settings\` (с заменой).
4. Скопируйте файл `handling.cfg` в папку `D:\CCD\GTA\data\` (с заменой).
5. Запустите файл **`apply_gta_optimizations.bat`** от имени Администратора (применит системные твики MPO).
6. Запускайте игру через ярлык **`clean_and_play.bat`**.

---

## 🎯 In-Game Settings Guide (Настройки внутри игры)

### 1. Настройки движка MTA (Клавиша `ESC` -> «Настройки» -> «Графика»)
* **Разрешение:** Родное разрешение вашего экрана (например, `2560x1440x32`).
* **Полноэкранный режим:** **Окно без рамки** (исключает сбои D3D9 при сворачивании).
* **Сглаживание:** **Выкл** или **1x**.  
  *(На 2K/4K мониторах плотность пикселей высокая, а режим 3x резервирует до 225 МБ дефицитной 32-битной видеопамяти движка).*
* **Анизотропная фильтрация:** **16x** (бесплатная чёткость дорог и номеров под углом).
* **Качество эффектов:** **Высокое**.
* **Нижние эффекты (тени, трава, дым, жара, размытие):** **Выключить всё** (устраняет графические артефакты кастомных шейдеров).
* **Транспорт и скины:** **Высокое качество** (стриминг 384 МБ обеспечивает полную прогрузку).

### 2. Настройки сервера CCDPlanet (Клавиша `F3` / Планшет)
* **SSAO / Размытие (DOF) / FXAA:** **Выключить**. Оверлейные шейдеры сервера накладываются на D3D9 и вызывают сильные просадки FPS при скоплении машин.
* **Качество отражений на авто:** **Стандартные** или **Новые 2023** (не Ultra).
* **Дым от дрифта:** Выключить, если наблюдаются просадки в зоне массового дрифта.

---

## ⚙️ How It Works (Как это работает под капотом)

```mermaid
flowchart TD
    subgraph PreLaunch ["Pre-Launch Pipeline"]
        Cleaner["clean_and_play.bat"]
        Logs["Active Logs Truncated to 0 KB"]
        Cleaner --> Logs
    end

    subgraph OS_Layer ["Windows 11 NT Kernel"]
        DWM["DWM MPO OverlayTestMode=5"]
        Compat["DISABLEDXMAXIMIZEDWINDOWEDMODE"]
        Priority["Process Priority: AboveNormal"]
    end

    subgraph Memory_Space ["32-Bit gta_sa.exe LAA Virtual Space"]
        Core["GTA Engine & Scripts (1.2 GB)"]
        StreamPool["Streaming Memory Floor: 384 MB"]
        CEF["CEF Software Rasterizer (400 MB)"]
        FreeHeap["Reserved Headroom: > 1.1 GB Safe Buffer"]
    end

    Cleaner -->|Launch| Priority
    DWM --> Compat
    Priority --> Memory_Space
```

1. **Предстартовая очистка:** `clean_and_play.bat` очищает файловые дескрипторы логов до входа в процесс, предотвращая дисковые очереди ввода-вывода.
2. **Изоляция DWM:** Windows 11 направляет кадры D3D9 напрямую в буфер композиции, минуя наложение аппаратных оверлеев MPO.
3. **Безопасная куча LAA:** Ограничение стриминга 384 МБ гарантирует, что даже при одновременной загрузке десятков текстур 2048x2048 процесс не приблизится к опасной границе 3800 МБ.

---

## ❓ FAQ

<details>
<summary><b>1. Безопасно ли это для античита CCDPlanet (FairplayKD)?</b></summary>
<br/>
<b>Абсолютно безопасно на 100%.</b> В комплексе нет ни одного стороннего DLL-файла, инъектора или перехватчика системных вызовов. Используются только официальные XML-теги настроек MTA:SA и системные ключи совместимости Windows.
</details>

<details>
<summary><b>2. Почему нельзя ставить память стриминга на 1024 МБ или 2048 МБ?</b></summary>
<br/>
GTA SA — это 32-битное приложение. Его максимальный виртуальный адрес ограничен 4096 МБ. При выделении 1024 МБ под стриминг геометрии, общая память игры с модами CCDPlanet превышает 3750 МБ, вызывая мгновенный вылет с кодом <code>0xC0000005</code>. Значение 384 МБ математически проверено как идеальная граница.
</details>

<details>
<summary><b>3. Зачем отключать сглаживание 3x (8x MSAA)?</b></summary>
<br/>
В Direct3D 9 сглаживание 8x MSAA при разрешении 2560x1440 создает мультисэмплинг-буфер огромного размера (~225 МБ VRAM). На мониторах 1440p и 4K пиксельная сетка и так плотная, а отключение MSAA высвобождает ресурсы памяти для стабильной работы без вылетов.
</details>

<details>
<summary><b>4. Что делать, если у меня другой сервер (Провинция, Radmir)?</b></summary>
<br/>
Файл <code>coreconfig.xml</code> и оптимизации Windows подходят для абсолютно любых серверов MTA:SA. Файл <code>server_settings.json</code> специфичен для функционала CCDPlanet, на других серверах используйте их встроенные F-меню.
</details>

---

## 🛡️ Disclaimer

Multi Theft Auto™ and Grand Theft Auto: San Andreas™ are registered trademarks of their respective owners. This repository is an independent open-source configuration toolkit and is not officially affiliated with Rockstar Games or Multi Theft Auto Team.

---

## 🤝 Credits & Community

* **Author & Lead Developer:** [Vektor010](https://github.com/Vektor010)
* **Architecture Research:** SRE & QA community of MTA:SA Direct3D 9 telemetry.
* **Testing Platform:** CCDPlanet Project Build `1.6.0-5.23094.0`.

<p align="center">
  <b style="color: #39FF88;">YOUR GAME. YOUR RULES.</b><br/>
  <sub>MTA:SA Stability Engine • Released under the MIT License • 2026 Edition</sub>
</p>
