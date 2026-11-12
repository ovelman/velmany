import cairosvg, math
E = '''<rect x="0" y="0" width="680" height="200" fill="#9fd6f7"/>
<ellipse cx="90" cy="40" rx="45" ry="14" fill="#ffffff" opacity="0.9"/>
<ellipse cx="600" cy="55" rx="55" ry="15" fill="#ffffff" opacity="0.9"/>
<path d="M0 175 L90 120 L170 160 L260 110 L360 165 L450 115 L560 160 L680 125 L680 200 L0 200 Z" fill="#8fb7a8"/>
<rect x="0" y="185" width="680" height="198" fill="#7cc46b"/>
<ellipse cx="60" cy="190" rx="50" ry="40" fill="#3f8f4a"/>
<ellipse cx="625" cy="190" rx="55" ry="42" fill="#3f8f4a"/>
<rect x="150" y="34" width="380" height="20" rx="8" fill="#f4f4f4" stroke="#b8b8b8" stroke-width="1"/>
<rect x="162" y="54" width="8" height="200" fill="#c9c9c9"/>
<rect x="510" y="54" width="8" height="200" fill="#c9c9c9"/>
<rect x="175" y="150" width="330" height="80" rx="10" fill="#e9e3d6" stroke="#bdb39f" stroke-width="1"/>
<rect x="170" y="228" width="340" height="28" rx="8" fill="#d8cfbc" stroke="#bdb39f" stroke-width="1"/>
<rect x="196" y="190" width="48" height="44" rx="14" fill="#f2a7bf"/>
<circle cx="220" cy="168" r="27" fill="#fde2cf"/>
<path d="M193 160 Q220 128 247 160 Z" fill="#ffffff" stroke="#c9c9c9" stroke-width="1"/>
<rect x="190" y="156" width="60" height="7" rx="3" fill="#ffffff" stroke="#c9c9c9" stroke-width="1"/>
<g><ellipse cx="212" cy="176" rx="3" ry="2" fill="#4a3426"/><ellipse cx="228" cy="176" rx="3" ry="2" fill="#4a3426"/></g>
<rect x="210" y="200" width="18" height="26" rx="3" fill="#333a44"/>
<rect x="436" y="190" width="48" height="44" rx="14" fill="#9fe0cc"/>
<circle cx="460" cy="168" r="27" fill="#fde2cf"/>
<path d="M433 160 Q460 128 487 160 Z" fill="#e8e1d2" stroke="#c9c9c9" stroke-width="1"/>
<rect x="430" y="156" width="60" height="7" rx="3" fill="#e8e1d2" stroke="#c9c9c9" stroke-width="1"/>
<g><ellipse cx="470" cy="172" rx="3" ry="3" fill="#4a3426"/><ellipse cx="482" cy="172" rx="3" ry="3" fill="#4a3426"/><path d="M466 186 Q474 190 482 185" fill="none" stroke="#8a5a44" stroke-width="2"/></g>
<path d="M300 258 L300 196 Q340 176 380 196 L380 258 Z" fill="#253a6b"/>
<path d="M330 196 L340 212 L350 196" fill="none" stroke="#ffffff" stroke-width="2"/>
<g><rect x="296" y="200" width="16" height="50" rx="7" fill="#ffffff"/><rect x="368" y="200" width="16" height="50" rx="7" fill="#ffffff"/></g>
<circle cx="340" cy="138" r="48" fill="#fde2cf"/>
<g><path d="M300 132 Q296 175 316 182 L312 132 Z" fill="#5a3a28"/><path d="M380 132 Q384 175 364 182 L368 132 Z" fill="#5a3a28"/><path d="M292 118 Q340 80 388 118 Z" fill="#5a3a28"/></g>
<rect x="286" y="110" width="108" height="14" rx="6" fill="#ffffff" stroke="#c9c9c9" stroke-width="1"/>
<g><ellipse cx="322" cy="144" rx="6" ry="8" fill="#4a3426"/><ellipse cx="358" cy="144" rx="6" ry="8" fill="#4a3426"/><circle cx="324" cy="141" r="2" fill="#ffffff"/><circle cx="360" cy="141" r="2" fill="#ffffff"/></g>
<path d="M326 166 Q333 162 340 166 Q347 170 354 165" fill="none" stroke="#8a5a44" stroke-width="2.5"/>
<g><ellipse cx="312" cy="158" rx="7" ry="4" fill="#f6b8a8" opacity="0.7"/><ellipse cx="368" cy="158" rx="7" ry="4" fill="#f6b8a8" opacity="0.7"/></g>
SWEAT
<rect x="0" y="287" width="680" height="96" fill="#1f2a22" opacity="0.55"/>
<text x="340" y="318" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="bold" font-size="18" fill="#ff6b6b">릴스에선 다들 웃고 있는데</text>
<text x="340" y="360" text-anchor="middle" font-family="Noto Sans CJK KR" font-weight="bold" font-size="30" fill="#ffffff">여자 골프 모임이 더 빡센 이유 7가지</text>'''.strip().split('\n')
def sweat(dy):
    return f'<path d="M390 {120+dy} Q398 {132+dy} 390 {138+dy} Q382 {132+dy} 390 {120+dy} Z" fill="#8fd3ff" stroke="#4da3d9" stroke-width="1"/>'
def svg(parts):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 680 383"><rect width="680" height="383" fill="#ffffff"/>{"".join(parts)}</svg>'
fps=30; per=5; n=0
def out(parts):
    global n
    cairosvg.svg2png(bytestring=svg(parts).encode(), write_to=f'frames/f{n:04d}.png'); n+=1
for i in range(len(E)):
    shown=[p if p!='SWEAT' else sweat(0) for p in E[:i+1]]
    for k in range(per): out(shown)
for t in range(90):
    dy=int(6*abs(math.sin(t/8)))
    out([p if p!='SWEAT' else sweat(dy) for p in E])
print(n)
