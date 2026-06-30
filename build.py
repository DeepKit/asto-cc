"""
asto.cc — 静态站点构建器

把 FastAPI + Jinja2 的动态路由预渲染成静态 HTML，输出到 public/，供 GitHub Pages 托管。
直接复用 main.py 的渲染逻辑，保证与开发服务器一致。
"""

import json
import re
import shutil
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = Path(__file__).parent
CONTENT_DIR = BASE_DIR / "content"
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
PUBLIC_DIR = BASE_DIR / "public"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=select_autoescape(["html"]),
)

GITHUB_BASE = "https://github.com/ODDFounder/difference-monism/blob/main"
STANDALONE_REPOS = {
    "odd": "https://github.com/ODDFounder/ODD/blob/main",
    "asto": "https://github.com/ODDFounder/ASTO/blob/main",
}

_FILE_PATH_RE = re.compile(
    r"<code>([^<]+\.(?:md|py|txt|json|sql|yaml|yml))</code>"
)


def _linkify_file_paths(html: str, source_dir: str = "", github_repo: str = "") -> str:
    base = github_repo or f"{GITHUB_BASE}/{source_dir}" if source_dir else GITHUB_BASE

    def _replace(m):
        path = m.group(1)
        if path.startswith("http") or path.startswith("/"):
            return m.group(0)
        if github_repo:
            full = path
        else:
            full = f"{source_dir}/{path}" if source_dir else path
        url = f"{base}/{full}"
        return f'<a href="{url}" target="_blank"><code>{path}</code></a>'

    return _FILE_PATH_RE.sub(_replace, html)


def read_md(rel_path: str, source_dir: str = "", slug: str = "") -> str:
    full = CONTENT_DIR / rel_path
    if not full.exists():
        return "<p>内容待补充</p>"
    text = full.read_text(encoding="utf-8")
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    github_repo = STANDALONE_REPOS.get(slug, "")
    return _linkify_file_paths(html, source_dir=source_dir, github_repo=github_repo)


def render(template_name: str, **context) -> str:
    tmpl = env.get_template(template_name)
    return tmpl.render(**context)


def load_layers() -> list[dict]:
    with open(CONTENT_DIR / "layers.json", encoding="utf-8") as f:
        return json.load(f)


def load_site_config() -> dict:
    with open(CONTENT_DIR / "site.json", encoding="utf-8") as f:
        return json.load(f)


def write_page(rel_path: str, html: str) -> None:
    """写到 public/，对子路径生成 dir/index.html，根路径生成 index.html。"""
    rel_path = rel_path.strip("/")
    if rel_path == "":
        target = PUBLIC_DIR / "index.html"
    elif rel_path.endswith(".html"):
        target = PUBLIC_DIR / rel_path
    else:
        target = PUBLIC_DIR / rel_path / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"  wrote {target.relative_to(PUBLIC_DIR)}")


def build() -> None:
    # 清空 public/
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir(parents=True)

    site = load_site_config()
    layers = load_layers()

    print("[build] rendering pages...")

    # 首页
    overview_html = read_md("overview.md")
    write_page("", render("index.html", site=site, layers=layers, overview=overview_html))

    # 关于
    citation_html = read_md("citation.md")
    write_page("about", render("about.html", site=site, citation=citation_html))

    # 走通
    body_html = read_md("walkthrough.md", source_dir="")
    write_page("walkthrough", render("walkthrough.html", site=site, layers=layers, body=body_html))

    # 各层
    for layer in layers:
        body_html = read_md(
            layer["overview_file"],
            source_dir=layer.get("github_dir", ""),
            slug=layer["slug"],
        )
        write_page(
            layer["slug"],
            render("layer.html", site=site, layers=layers, layer=layer, body=body_html),
        )

    # 静态资源
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, PUBLIC_DIR / "static")
        print("[build] copied static/")

    # CNAME（绑定 asto.cc）
    (PUBLIC_DIR / "CNAME").write_text("asto.cc\n", encoding="utf-8")
    print("[build] wrote CNAME")

    # .nojekyll（跳过 Jekyll 处理，保留目录结构）
    (PUBLIC_DIR / ".nojekyll").write_text("", encoding="utf-8")
    print("[build] wrote .nojekyll")

    print(f"[build] done → {PUBLIC_DIR}")


if __name__ == "__main__":
    build()
