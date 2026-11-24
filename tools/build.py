#!/usr/bin/env python3
"""세 앱의 지원·개인정보 처리방침 페이지를 만든다. 실행: python3 tools/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://kobums.github.io/showticket-support"
ISSUES = "https://github.com/kobums/showticket-support/issues"
EFFECTIVE = "2026년 11월 24일"

APPS = [
    dict(
        slug="cinema-seat", name="좌석 시야", accent="#6B5BD6",
        summary="영화관·공연장 좌석을 고르기 전에, 그 자리에 앉았을 때 스크린이나 무대가 어떻게 보이는지 3D로 미리 보는 iPhone 앱입니다.",
        howto=[
            "첫 화면에서 작품과 상영(공연) 시간을 고릅니다.",
            "좌석 배치도에서 자리를 누르고 '시야 보기'를 누릅니다.",
            "화면을 끌어 주변을 둘러보고, 두 번 누르면 정면으로 돌아옵니다.",
            "스크린(무대)까지의 거리, 시야각, 중앙에서 벗어난 정도를 숫자로 확인합니다.",
            "'좌석 공유'로 고른 자리 정보를 다른 앱에 보낼 수 있습니다.",
        ],
        faq=[
            ("앱에 나오는 영화관과 작품은 실제인가요?", "아니요. 지금 들어 있는 상영관·공연장·작품·가격은 좌석 시야를 보여 주기 위한 예시입니다."),
            ("이 앱에서 예매할 수 있나요?", "예매 기능은 없습니다. 자리에서 보이는 모습을 미리 확인하는 용도입니다."),
        ],
        stored="서비스는 이용자의 기기에도 이용 기록을 저장하지 않습니다. 고른 좌석은 앱을 닫으면 사라집니다.",
        share="'좌석 공유'를 누르면 고른 좌석 이름과 거리 같은 문구가 이용자가 직접 고른 앱(메시지 등)으로 전달됩니다. 이 과정은 iOS 공유 기능이 처리하며 운영자에게는 아무것도 전송되지 않습니다.",
    ),
    dict(
        slug="flight-seat", name="창가 시야", accent="#0A64D0",
        summary="비행기 좌석을 고르기 전에, 그 창가에서 비행 중 무엇이 보일지(해가 드는 쪽, 날개 위치, 창문 유무) 미리 보는 iPhone 앱입니다.",
        howto=[
            "첫 화면에서 항공편을 고릅니다.",
            "좌석 배치도에서 창가 자리를 누르고 '창밖 보기'를 누릅니다.",
            "아래 막대를 끌거나 재생 버튼을 눌러 이륙부터 착륙까지 창밖이 어떻게 바뀌는지 봅니다.",
            "해가 창으로 드는 시간대, 날개에 가리는지, 창문이 없는 자리인지 확인합니다.",
            "'공유'로 고른 자리 정보를 다른 앱에 보낼 수 있습니다.",
        ],
        faq=[
            ("앱에 나오는 항공편은 실제인가요?", "아니요. 항공사·편명·기종·좌석 요금은 예시입니다. 공항과 지명은 실제 위치를 씁니다."),
            ("창밖 모습은 얼마나 정확한가요?", "두 공항을 잇는 대권 항로와 맑은 날을 기준으로 해의 위치를 계산한 예상입니다. 실제 항로·날씨·기체에 따라 달라집니다."),
            ("이 앱에서 좌석을 지정할 수 있나요?", "좌석 지정·예약 기능은 없습니다."),
        ],
        stored="서비스는 이용자의 기기에도 이용 기록을 저장하지 않습니다. 고른 좌석은 앱을 닫으면 사라집니다.",
        share="'공유'를 누르면 편명과 좌석 같은 문구가 이용자가 직접 고른 앱(메시지 등)으로 전달됩니다. 이 과정은 iOS 공유 기능이 처리하며 운영자에게는 아무것도 전송되지 않습니다.",
    ),
    dict(
        slug="locker-room", name="라커룸", accent="#177A4C",
        summary="라커룸 옷걸이에 걸린 유니폼을 넘겨 보며 선수단을 소개하는 iPhone 앱입니다.",
        howto=[
            "첫 화면에서 팀을 고릅니다.",
            "유니폼을 옆으로 밀어 넘기고, 위쪽 칩으로 포지션별로 모아 봅니다.",
            "가운데 유니폼을 누르면 선수 소개가 열립니다. 유니폼을 끌어 앞뒤로 돌려 볼 수 있습니다.",
            "오른쪽 위 목록 버튼으로 선수 명단에서 바로 찾아갈 수 있습니다.",
        ],
        faq=[
            ("앱에 나오는 팀과 선수는 실제인가요?", "아니요. 팀·선수·기록은 모두 지어낸 예시이며 실제 구단이나 선수와 관계가 없습니다."),
        ],
        stored="서비스는 이용자의 기기에도 이용 기록을 저장하지 않습니다.",
        share=None,
    ),
]

CSS = """
:root{--bg:#f6f6f8;--card:#fff;--text:#1c1c1e;--sub:#6b6b70;--line:#e3e3e8;--accent:#444}
@media (prefers-color-scheme:dark){:root{--bg:#0f0f11;--card:#1b1b1e;--text:#f2f2f4;--sub:#a0a0a8;--line:#2c2c31}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.7 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR",sans-serif}
main{max-width:720px;margin:0 auto;padding:40px 16px 64px}
h1{font-size:28px;line-height:1.3;margin:0 0 4px}
h2{font-size:19px;margin:36px 0 8px}
p,li{color:var(--text)} .sub{color:var(--sub);font-size:14px}
a{color:var(--accent)} ul,ol{padding-left:22px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0;display:block;text-decoration:none;color:inherit}
.card b{font-size:18px} .eyebrow{font-size:13px;font-weight:700;color:var(--accent);letter-spacing:.02em}
nav{margin-bottom:28px;font-size:14px} nav a{margin-right:14px}
footer{margin-top:48px;padding-top:16px;border-top:1px solid var(--line);font-size:13px;color:var(--sub)}
"""

def page(title, body, accent="#444", depth=0):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>{CSS}:root{{--accent:{accent}}}
@media (prefers-color-scheme:dark){{:root{{--accent:color-mix(in srgb,{accent} 55%,white)}}}}</style>
</head>
<body>
<main>
{body}
<footer>© 2026 Gowoobro · <a href="{up}index.html">앱 목록</a> · <a href="https://gowoobro.com">gowoobro.com</a></footer>
</main>
</body>
</html>
"""

def support(app):
    howto = "\n".join(f"<li>{x}</li>" for x in app["howto"])
    faq = "\n".join(f"<h3 style='font-size:16px;margin:18px 0 2px'>{q}</h3><p style='margin:0'>{a}</p>" for q, a in app["faq"])
    return page(f"{app['name']} 지원", f"""
<nav><a href="index.html">지원</a><a href="privacy.html">개인정보 처리방침</a></nav>
<div class="eyebrow">지원</div>
<h1>{app['name']}</h1>
<p>{app['summary']}</p>
<h2>사용 방법</h2>
<ol>{howto}</ol>
<h2>자주 묻는 질문</h2>
{faq}
<h2>문의</h2>
<p>오류 신고나 문의는 <a href="{ISSUES}">GitHub 문의 게시판</a>에 남겨 주세요. <a href="https://gowoobro.com">gowoobro.com</a>의 '문의하기'로도 연락할 수 있습니다.</p>
<p class="sub">iOS 26 이상 iPhone에서 쓸 수 있습니다.</p>
""", app["accent"], 1)

def privacy(app):
    n = app["name"]
    share = f"<p>{app['share']}</p>" if app["share"] else ""
    return page(f"개인정보 처리방침 | {n}", f"""
<nav><a href="index.html">지원</a><a href="privacy.html">개인정보 처리방침</a></nav>
<div class="eyebrow">{n}</div>
<h1>개인정보 처리방침</h1>
<p class="sub">시행일 {EFFECTIVE} · 버전 1</p>
<p>Gowoobro(개인 개발자, 이하 '운영자')는 {n}(이하 '서비스') 이용자의 개인정보를 소중히 다루며, 「개인정보 보호법」 등 관련 법령을 지킵니다. 이 방침은 서비스가 어떤 정보를 왜 수집하고 어떻게 다루는지 설명합니다.</p>
<h2>1. 수집하는 개인정보</h2>
<p>서비스는 개인정보를 수집하지 않습니다. 회원 가입이 없고, 앱은 인터넷으로 이용자에 관한 어떤 데이터도 보내지 않습니다.</p>
<p>{app['stored']}</p>
{share}
<h2>2. 개인정보의 이용 목적</h2>
<p>수집하는 개인정보가 없으므로 이용하는 목적도 없습니다. 운영자는 이용자의 정보를 광고·마케팅 목적으로 이용하거나 판매하지 않습니다.</p>
<h2>3. 보유 기간과 파기</h2>
<p>운영자가 보유하는 이용자 정보는 없습니다. 앱을 삭제하면 앱과 함께 기기에 있던 데이터가 모두 삭제됩니다.</p>
<h2>4. 개인정보의 제3자 제공</h2>
<p>운영자는 이용자의 개인정보를 제3자에게 제공하지 않습니다.</p>
<h2>5. 처리 위탁과 국외 이전</h2>
<p>운영자는 개인정보 처리를 외부에 위탁하지 않으며, 국외로 이전하지 않습니다.</p>
<h2>6. 자동으로 저장·수집되는 정보</h2>
<p>서비스는 방문 분석 도구, 충돌 보고 도구, 광고 도구, 푸시 알림을 쓰지 않으며 이용자를 추적하지 않습니다. 카메라·사진·위치 등 기기 권한도 요청하지 않습니다. App Store가 자체적으로 수집하는 다운로드·사용 통계는 Apple의 개인정보 처리방침에 따릅니다.</p>
<h2>7. 이용자의 권리와 행사 방법</h2>
<p>이용자는 언제든지 자신의 개인정보에 대해 열람·정정·삭제·처리 정지를 요구할 수 있습니다. 서비스는 개인정보를 수집하지 않으므로 운영자가 따로 보관하는 정보는 없습니다. 문의는 아래 연락처로 보내 주세요.</p>
<h2>8. 아동의 개인정보</h2>
<p>서비스는 개인정보를 수집하지 않으므로 아동의 개인정보도 수집하지 않습니다.</p>
<h2>9. 개인정보 보호책임자와 문의</h2>
<ul>
<li>책임자: Gowoobro 운영자</li>
<li>문의: <a href="{ISSUES}">GitHub 문의 게시판</a> 또는 <a href="https://gowoobro.com">gowoobro.com</a>의 '문의하기'</li>
</ul>
<p>개인정보 침해에 대한 상담이나 신고가 필요하면 아래 기관에 문의할 수 있습니다.</p>
<ul>
<li>개인정보침해신고센터: privacy.kisa.or.kr / 국번 없이 118</li>
<li>개인정보분쟁조정위원회: www.kopico.go.kr / 1833-6972</li>
<li>대검찰청 사이버수사과: www.spo.go.kr / 국번 없이 1301</li>
<li>경찰청 사이버수사국: ecrm.police.go.kr / 국번 없이 182</li>
</ul>
<h2>10. 방침의 변경</h2>
<p>이 방침은 {EFFECTIVE}부터 적용됩니다. 내용을 바꿀 때는 시행 7일 전(이용자에게 불리하거나 중요한 변경은 30일 전)에 이 페이지에 알립니다.</p>
""", app["accent"], 1)

def index():
    cards = "\n".join(
        f'<a class="card" href="{a["slug"]}/index.html"><b>{a["name"]}</b><br><span class="sub">{a["summary"]}</span></a>'
        for a in APPS)
    return page("Gowoobro 앱 지원", f"""
<div class="eyebrow">Gowoobro</div>
<h1>앱 지원</h1>
<p class="sub">앱을 골라 사용 방법과 개인정보 처리방침을 확인하세요.</p>
{cards}
""")

def main():
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("")
    for app in APPS:
        d = ROOT / app["slug"]; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(support(app), encoding="utf-8")
        (d / "privacy.html").write_text(privacy(app), encoding="utf-8")
        print(f"{BASE}/{app['slug']}/  ·  {BASE}/{app['slug']}/privacy.html")

if __name__ == "__main__":
    main()
