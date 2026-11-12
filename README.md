# 카트 썸네일 구도 스케치 영상 만들기

SVG 도형을 하나씩 추가하며 프레임을 그리고, ffmpeg로 MP4로 묶는 스크립트입니다.

## 준비
- Python 3
- ffmpeg
- `pip install cairosvg`
- 한글 폰트: Noto Sans CJK KR

## 실행
```
mkdir -p frames
python3 make.py
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -preset veryfast -pix_fmt yuv420p cart_sketch.mp4
```

결과: 1280x720, 9초 MP4 (도형이 순서대로 나타난 뒤 땀방울이 흔들림)
