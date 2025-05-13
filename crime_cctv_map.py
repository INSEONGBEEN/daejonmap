import folium
import pandas as pd
from IPython.display import display, HTML

# 1️⃣ 지도 초기화 (대전역 중심으로!)
m = folium.Map(location=[36.3325, 127.4348], zoom_start=16)  # 확대 레벨도 살짝 올림

# 2️⃣ 범죄주의구간 WMS 레이어 추가
api_key = '9IVIERCH-9IVI-9IVI-9IVI-9IVIERCH81'
wms_url = f'http://www.safemap.go.kr/openApiService/wms/getLayerData.do?apikey={api_key}'

folium.raster_layers.WmsTileLayer(
    url=wms_url,
    layers='A2SM_CRMNLHSPOT_TOT',
    styles='A2SM_CrmnlHspot_Tot_Tot',
    fmt='image/png',
    transparent=True,
    name='범죄주의구간(전체)',
    overlay=True,
    control=True
).add_to(m)

# 3️⃣ CCTV 데이터 불러오기
cctv_df = pd.read_csv('/Users/sayongja/Downloads/안전지도/cctv.csv', encoding='cp949')

# 4️⃣ CCTV 탐지 범위(30m 반경) + 위치 시각화
for idx, row in cctv_df.iterrows():
    # 탐지 범위 (30m)
    folium.Circle(
        location=[row['위도'], row['경도']],
        radius=30,  # 반경 30미터
        color='#9b59b6',
        fill=True,
        fill_opacity=0.2,
        popup='CCTV 탐지범위 (30m)'
    ).add_to(m)
    
    # CCTV 점 표시
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=3,
        color='#8e44ad',
        fill=True,
        fill_opacity=0.8,
        popup='CCTV'
    ).add_to(m)

# 5️⃣ 지도 출력
display(HTML(m._repr_html_()))

# (선택) 지도 저장
m.save('crime_cctv_with_circle_buffer_daejeon.html')
