"""Build the November postcard versions (A = proven headline, B = test headline) from postcard.template.html."""
from pathlib import Path

CHECK = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#0f4651"/><path d="M6.5 12.5l3.5 3.5 7.5-8" fill="none" stroke="#e6b04a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

VERSIONS = {
    "A": {
        "title": "Nov postcard A - Turning 65 soon",
        "headline": '<h1 class="headline big">Turning <span class="accent">65</span><br>soon?</h1>',
        "tagline": "Let's make Medicare simple.",
    },
    "B": {
        "title": "Nov postcard B - Medicare is confusing",
        "headline": '<h1 class="headline mid">Medicare is<br>confusing.<br><span class="accent">Lunch shouldn’t be.</span></h1>',
        "tagline": "Let's make it simple, over lunch.",
    },
}

template = Path("postcard.template.html").read_text()
for code, v in VERSIONS.items():
    html = (template.replace("{{TITLE}}", v["title"]).replace("{{HEADLINE}}", v["headline"])
            .replace("{{TAGLINE}}", v["tagline"]).replace("{{CHECK}}", CHECK).replace("{{CODE}}", code))
    Path(f"postcard-{code}.html").write_text(html)
    print("wrote", f"postcard-{code}.html")
