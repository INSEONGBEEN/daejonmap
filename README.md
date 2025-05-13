# 🚨 대전역 주변 CCTV & 범죄주의구간 시각화 프로젝트

*@injjang*

2025.05 ~ 2025.05

---

## Live Demo

https://inseongbeen.github.io/daejonmap/crime_cctv_with_circle_buffer_daejeon.html

## GitHub Repo

https://github.com/INSEONGBEEN/daejonmap

## Dev Log

https://lnjjang.tistory.com/

---

> 대전역 주변의 **범죄주의구간 밀도 지도와 CCTV 위치 및 탐지 범위(30m)**를 지도 위에 시각화한 토이 프로젝트입니다. Python과 folium을 활용하여 시각적 안전지도를 구현했으며, 생활안전지도 API를 연동하여 실제 데이터 기반의 지도 시각화를 진행했습니다.

---

## ✅ 주요 기능

- **생활안전지도 API 연동**  
  WMS 방식으로 범죄주의구간 밀도지도 표시

- **CCTV 위치 시각화**  
  CCTV 위치를 지도 위에 CircleMarker로 시각화 (진보라색)

- **CCTV 탐지범위(30m) 표시**  
  `folium.Circle`로 반경 30m 탐지범위 시각화 (연보라색)

- **지도 저장 및 결과물 출력**  
  HTML로 지도 저장 및 주피터에서 실시간 시각화

---

## 🚧 구현 예정 기능

- CCTV 커버리지와 범죄주의구간의 **사각지대 탐색** (디지털라이징 필요)
- 가로등 등 **다른 안전 인프라 연동**

---

## 🛠 기술 스택

| 항목 | 내용 |
|------|------|
| Programming Languages | Python |
| Data Processing | pandas, geopandas |
| Visualization | folium |
| API | 생활안전지도 API(WMS) |
| Development Tools | Jupyter Notebook |
| Deployment | HTML 파일로 결과물 저장 |

---

## 📁 프로젝트 구조

```
📦 daejeon-cctv-crime-map
├── README.md
├── crime_cctv_map.py
├── crime_cctv_with_circle_buffer_daejeon.html
├── data
│   └── cctv.csv
```

---

## 🚀 실행 예시

```bash
# 패키지 설치
pip install folium pandas

# 프로젝트 실행
python crime_cctv_map.py
```

생성된 HTML 파일(`crime_cctv_with_circle_buffer_daejeon.html`)을 브라우저에서 열면 대전역 주변 CCTV 위치 및 범죄주의구간 시각화 결과를 확인할 수 있습니다.

---

## 📌 진행 과정

### 1️⃣ 생활안전지도 API 연동

생활안전지도 WMS API를 활용하여 **범죄주의구간 밀도 지도** 가져오기  
API KEY로 인증 후 `folium.raster_layers.WmsTileLayer`로 시각화 구현

📌 범례는 직접 만든 HTML/CSS 구성으로 지도 하단에 삽입하여 가독성 향상

### 2️⃣ CCTV 위치 시각화

- CCTV 좌표 데이터를 pandas로 불러온 후,
- `folium.CircleMarker`로 진보라색 마커로 시각화

### 3️⃣ CCTV 탐지 범위(30m 반경) 시각화

- `folium.Circle`을 활용하여 CCTV 주변 반경 30m를 연보라 색상으로 표시

### 4️⃣ 시각화 결과 저장

- `folium.Map().save()`로 HTML 파일 저장
- 로컬에서 결과물 확인 가능

---

## 🧩 결과물 예시

> 결과 지도:
> `(https://inseongbeen.github.io/daejonmap/crime_cctv_with_circle_buffer_daejeon.html)`

대전역 주변의 CCTV와 범죄주의구간을 한눈에 볼 수 있도록 시각화 완료  
CCTV 커버리지를 원형으로 표현하여 시각적으로 직관적인 이해 가능

---

## 🧪 보완할 점 및 향후 아이디어

| 한계점 | 보완 아이디어 |
|--------|----------------|
| 범죄주의구간이 WMS 이미지여서 벡터 분석 불가능 | QGIS를 활용한 디지털라이징 후 GeoJSON 벡터 분석 시도 |
| CCTV 사각지대 분석 미수행 | 디지털라이징된 범죄구간과 CCTV 탐지 범위의 교차 분석 진행 |
| 가로등 데이터 부재 | 가로등 위치 데이터 확보 후 추가 시각화 구현 |

---

## ✍️ 느낀 점

- Python 기반의 **공간 시각화**에 대한 이해도가 높아졌고,
- folium의 WMS API 연동 및 Circle 시각화 기능을 처음으로 활용해봄
- 실무에서는 **정제된 벡터 데이터 확보 및 디지털라이징**의 중요성을 체감함

---
