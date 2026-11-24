#!/usr/bin/env python3
"""지원·개인정보 페이지는 gowoobro.com 으로 옮겼다. 여기에는 예전 주소로 들어온 사람을
새 주소로 보내는 페이지만 만든다. 실행: python3 tools/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://gowoobro.com"

# 폴더 이름 → (앱 이름, gowoobro.com 프로젝트 id)
APPS = {
    "cinema-seat": ("좌석 시야", 24),
    "flight-seat": ("창가 시야", 25),
    "locker-room": ("라커룸", 26),
}


def redirect(title, url):
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace("{url}")</script>
</head>
<body style="font:16px/1.7 -apple-system,sans-serif;margin:40px 16px">
<p>이 페이지는 옮겨졌습니다. <a href="{url}">{url}</a></p>
</body>
</html>
"""


def main():
    (ROOT / ".nojekyll").write_text("")
    (ROOT / "index.html").write_text(redirect("Gowoobro", f"{SITE}/ko"), encoding="utf-8")
    for slug, (name, pid) in APPS.items():
        d = ROOT / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(redirect(name, f"{SITE}/ko/app/{pid}"), encoding="utf-8")
        (d / "privacy.html").write_text(
            redirect(f"개인정보 처리방침 | {name}", f"{SITE}/ko/app/{pid}/privacy"), encoding="utf-8")
        print(f"{slug} → {SITE}/ko/app/{pid}")


if __name__ == "__main__":
    main()
