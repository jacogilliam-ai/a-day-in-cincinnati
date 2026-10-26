#!/usr/bin/env python3
"""Wrap the artifact source (no doctype/head/body) into a standalone page for GitHub Pages."""
import io, os, re

SRC = "index.html"
OUT = "docs/index.html"
BASE = "https://jacogilliam-ai.github.io/a-day-in-cincinnati/"
TITLE = "A day in Cincinnati"
DESC = "Six stops, one river crossing."

s = io.open(SRC, encoding="utf-8").read()
cut = s.index("</style>") + len("</style>")
head_src, body = s[:cut], s[cut:].strip()

style = head_src[head_src.index("<style>"):]
fonts = "\n".join(re.findall(r'<link rel="(?:preconnect|stylesheet)"[^>]*>', head_src))

icon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
        "%3Ctext y='.9em' font-size='90'%3E%F0%9F%8D%82%3C/text%3E%3C/svg%3E")

doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{BASE}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{BASE}og.png">
<link rel="icon" href="{icon}">
{fonts}
{style}
</head>
<body>
{body}
</body>
</html>
'''

os.makedirs("docs", exist_ok=True)
io.open(OUT, "w", encoding="utf-8").write(doc)
io.open("docs/robots.txt", "w", encoding="utf-8").write("User-agent: *\nDisallow: /\n")
io.open("docs/.nojekyll", "w", encoding="utf-8").write("")
print("wrote", OUT, os.path.getsize(OUT), "bytes")
