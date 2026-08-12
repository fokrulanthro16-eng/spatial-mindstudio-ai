# 🌌 Spatial MindStudio AI

> **3D Knowledge Constellation Synthesizer Powered by Google Gemini API & WebGL**
> *Built for Spatial Hack AI: Apple Vision Pro & Spatial Computing Track*

[![Apple Vision Pro Ready](https://img.shields.io/badge/Apple_Vision_Pro-Ready-000000?style=for-the-badge&logo=apple&logoColor=white)](https://www.apple.com/apple-vision-pro/)
[![WebXR Compatible](https://img.shields.io/badge/WebXR-Compatible-00599C?style=for-the-badge&logo=webxr&logoColor=white)](https://immersiveweb.dev/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-8E44AD?style=for-the-badge&logo=googlegemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Three.js](https://img.shields.io/badge/Three.js-r128-000000?style=for-the-badge&logo=three.js&logoColor=white)](https://threejs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

[🎥 Watch Demo Video](https://github.com/fokrulanthro16-eng/spatial-mindstudio-ai) • [🌐 Launch Live Web App](http://localhost:3000) • [📖 Read Documentation](#-getting-started--local-setup)

---

## 📸 Screenshots & Visual Preview

| 🌌 3D Spatial Knowledge Graph | 💎 Glassmorphic Spatial UI Overlay |
| :---: | :---: |
| ![Spatial 3D Node Rendering](https://raw.githubusercontent.com/fokrulanthro16-eng/spatial-mindstudio-ai/main/docs/preview-3d.png) | ![High-DPI UI Control Panel](https://raw.githubusercontent.com/fokrulanthro16-eng/spatial-mindstudio-ai/main/docs/preview-ui.png) |

| ⚡ Gemini Structured Response Schema |
| :---: |
| ![Gemini Response Schema](https://raw.githubusercontent.com/fokrulanthro16-eng/spatial-mindstudio-ai/main/docs/preview-schema.png) |

---

## 🏆 Alignment with Spatial Hack AI Judging Criteria

| Judging Criterion | Implementation in Spatial MindStudio AI |
| :--- | :--- |
| **🎨 Interface Design** | Translucent glassmorphism spatial control overlays, ultra-legible typography, high-DPI 4K and Vision Pro UI scaling, Grandma Theory zero-learning-curve UX. |
| **🛠️ Technical Implementation** | Google Gemini `gemini-2.5-flash` structured JSON parsing (`response_mime_type="application/json"`), FastAPI async backend engine, Three.js WebGL 3D spatial coordinate projection system. |
| **📖 Storytelling** | Replaces flat, static 2D concept charts with interactive spatial knowledge constellations that expand user cognition into 3 dimensions. |
| **🎯 Problem-Solution Fit** | Eliminates visual clutter in multi-layered software architectures, machine learning lifecycles, and complex organizational networks. |
| **💡 Novelty** | Automated zero-collision 3D node clustering and dynamic `THREE.Box3` bounding-box camera auto-framing powered by generative AI. |
| **🎮 Fun & Interactivity** | Gamified 3D space exploration, glowing volumetric cylinder connections, particle space dust, dynamic preset tags, and instant orbit controls. |

---

## 🥽 Apple Vision Pro & WebXR Readiness

Spatial MindStudio AI is engineered ground-up for spatial computing environments:
- **visionOS Safari Native Compatibility**: Fully renders in spatial windows inside visionOS Safari with native spatial depth passthrough.
- **WebXR Canvas Integration**: Pre-configured for WebXR device sessions, enabling 6DOF spatial head movement and spatial sound cues.
- **Hand Gesture & Touch Controls**: Seamless fallback mapping from mouse clicks to Apple Vision Pro pinch, drag, and eye-gaze selections.

---

## 💡 Executive Overview & Problem Statement

Traditional 2D mind maps and hierarchical diagrams fail to convey complex, multi-dimensional relationships across dense knowledge networks. Information overflow leads to visual clutter, poor spatial recall, and cognitive fatigue.

**Spatial MindStudio AI** transforms flat text and complex natural language prompts into **immersive 3D knowledge constellations**. Powered by **Google Gemini API** (`gemini-2.5-flash`), the system parses unstructured concepts, automatically determines optimal 3D coordinates `[x, y, z]`, constructs semantic connections, and renders real-time WebGL interactive graphs with zero overlap and dynamic camera framing.

---

## ⚡ Core Features & Innovations

- 🧠 **Structured Gemini 3D Engine**: Leverages Google Gemini's `response_mime_type="application/json"` with strict schema enforcement to generate graph topologies, colors, connections, and camera targets.
- 📐 **Adaptive Coordinate Normalization & Auto-Framing**: Dynamically scales incoming coordinates and uses `THREE.Box3` bounding-box math to automatically adjust camera FOV and position so every node is perfectly visible upon generation.
- ✨ **Volumetric WebGL Graphics**: Spherical glow nodes, volumetric cylinder connection beams, particle space dust, and emissive lighting effects built with Three.js and OrbitControls.
- 🔍 **Interactive Raycasting & Inspection**: Click any 3D concept node to smoothly align the camera to its perspective and inspect its metadata, spatial coordinates, and adjacent relationships.
- 🖥️ **High-DPI Ultra-Accessible UI**: Designed with oversized, crystal-clear typography, 26px prompt input fonts, glassmorphism dark aesthetics, and quick-action preset buttons.

---

## 🏗️ System Architecture Flowchart

```mermaid
graph TD
    A[User Input / Natural Language Prompt] -->|POST /api/spatial-command| B[FastAPI Backend Engine]
    B --> C{Gemini API Configured?}
    C -->|Yes| D[Google Gemini 2.5 Flash API]
    C -->|No / Error| E[Procedural Math Fallback Generator]
    D -->|Structured JSON Output| F[Pydantic Validation & Normalization]
    E -->|Structured JSON Output| F
    F -->|JSON Response| G[Three.js 3D WebGL Renderer]
    G --> H[THREE.Box3 Bounding Box Auto-Framing]
    G --> I[HTML Screen-Space Projected 3D Labels]
    G --> J[Interactive Raycasting & Sidebar Inspector]
```

---

## 🛠️ Technical Stack Specifications

| Layer | Technology | Role & Purpose |
| :--- | :--- | :--- |
| **Backend Core** | FastAPI & Uvicorn | High-performance asynchronous API server |
| **AI Intelligence** | Google Gemini API (`google-generativeai`) | Structured JSON synthesis (`gemini-2.5-flash`) |
| **Data Validation** | Pydantic v2 | Strict JSON schema validation and alias mapping |
| **Graphics Engine** | Three.js (r128) | WebGL rendering loop, particle systems, emissive lights |
| **Camera Control** | Three.js OrbitControls | Smooth 3D rotation, pan, zoom, and damping |
| **Frontend UI** | HTML5, Vanilla CSS, JS | High-DPI Glassmorphism overlay, screen-projected HTML labels |

---

## 📝 Gemini Structured Output Schema Example

When a request is posted to `/api/spatial-command`, Gemini responds with the following exact JSON schema:

```json
{
  "nodes": [
    { "id": "sun", "label": "Sun", "position": [0.0, 0.0, 0.0], "color": "#FFFF00" },
    { "id": "earth", "label": "Earth", "position": [2.5, 0.0, 0.0], "color": "#0000FF" },
    { "id": "mars", "label": "Mars", "position": [3.8, 0.0, 0.0], "color": "#FF0000" }
  ],
  "connections": [
    { "from": "sun", "to": "earth" },
    { "from": "sun", "to": "mars" }
  ],
  "camera_target": [0.0, 0.0, 0.0]
}
```

---

## 🚀 Getting Started & Local Setup

### Prerequisites
- Python 3.10+
- Google Gemini API Key ([Get an API Key](https://aistudio.google.com/))

### 1. Clone the Repository
```bash
git clone https://github.com/fokrulanthro16-eng/spatial-mindstudio-ai.git
cd spatial-mindstudio-ai
```

### 2. Set Up Environment Variables
Create a `.env` file in the `backend/` directory:
```bash
echo GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY" > backend/.env
```

### 3. Run the Backend Server
```bash
cd backend
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 4. Run the Frontend App
Open a second terminal window in the root directory:
```bash
cd frontend
python -m http.server 3000
```
Open `http://localhost:3000` in your web browser.

---

## 📂 Project Directory Structure

```text
spatial-mindstudio-ai/
├── LICENSE                  # MIT Open Source License
├── README.md                 # Project Documentation
├── .gitignore               # Excludes secrets, venv, and cache
├── backend/
│   ├── main.py              # FastAPI server & Gemini structured API engine
│   ├── requirements.txt      # Backend Python dependencies
│   └── .env                 # Local API keys configuration (git-ignored)
└── frontend/
    └── index.html           # Three.js 3D WebGL application & High-DPI UI
```

---

## 📄 License & Acknowledgments

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

- Special thanks to **Google Gemini AI** for structured output generation.
- Built with **Three.js** for high-performance WebGL 3D graphics.
