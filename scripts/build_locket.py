#!/usr/bin/env python3
"""Fetch upstream JS and change only promotional string values."""
from pathlib import Path
from urllib.request import urlopen, Request
import subprocess

SOURCE = 'https://raw.githubusercontent.com/duyvinh09/Module_IOS/refs/heads/main/js/Locket_Unlocked.js'
raw = urlopen(Request(SOURCE, headers={'User-Agent':'TuanPhong275-Builder'}), timeout=30).read()
text = raw.decode('utf-8')
replacements = {
 'title: "Nhớ follow kênh tiktok @duyvinh.09 ✨",': 'title: "Locket Gold by TuanPhong275 💛",',
 'body: "Một follow của bạn, một niềm vui của mình 💛",': 'body: "Nhớ follow TikTok @_tuanphong705 ❤️",',
 'imageURL: "https://i.ibb.co/gZ6HkyWT/L-n-Gold-R-i.png"': 'imageURL: "https://i.ibb.co/b5H0DL2p/L-n-Locket-Gold-R-i.png"',
 'settings_tiktok_url: "https://tiktok.com/@duyvinh.09"': 'settings_tiktok_url: "https://www.tiktok.com/@_tuanphong705"',
 'settings_instagram_url: "https://www.instagram.com/dvinh.09/"': 'settings_instagram_url: "https://www.instagram.com/"',
}
for before, after in replacements.items():
    count = text.count(before)
    if count != 1:
        raise SystemExit(f'STOP: expected 1 occurrence, found {count}: {before}')
    text=text.replace(before,after,1)
path=Path('js/Locket_Unlocked.js')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(text,encoding='utf-8')
subprocess.run(['node','--check',str(path)], check=True)
print(f'Created {path}; changed only {len(replacements)} promotional fields; JS syntax OK')
