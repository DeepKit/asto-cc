# asto.cc — 差异一元论理论展示站

> 定位：学术品牌，理论母库的对外展示窗口。
> 内容来源：`D:\_Progs\一元论\`（差异一元论理论母库）
> 托管：GitHub Pages，绑定域名 `asto.cc`

---

## 架构

静态站点。`build.py` 把 Jinja2 模板 + Markdown 内容预渲染成 `public/`，由 GitHub Actions 自动构建部署。

```
asto.cc/
├── content/            # Markdown 源（从理论母库同步）
│   ├── site.json       # 站点配置（标题/作者/链接）
│   ├── layers.json     # 11 层元数据（slug/DOI/上下游）
│   ├── overview.md     # 首页总览（来自 MOC-理论导航）
│   ├── walkthrough.md   # 八层统一走通
│   ├── citation.md      # 引用指南（CITATION.cff）
│   └── layers/*.md      # 各层单文件入口（来自 *-4AI.md）
├── templates/          # Jinja2 模板
├── static/             # CSS
├── build.py            # 静态构建器
├── main.py             # 本地开发服务器（FastAPI，可选）
└── .github/workflows/  # CI：push → build → deploy
```

## 本地开发

```bash
# 静态构建
python build.py          # 输出到 public/

# 或动态预览（可选）
pip install -r requirements.txt
python main.py           # http://localhost:8001
```

## 内容同步

内容从理论母库 `D:\_Progs\一元论\` 拉取：

| 站点文件 | 母库来源 |
|---------|---------|
| `content/layers/dm.md` | `10-哲学核心层（DM）/DM-4AI.md` |
| `content/layers/asto.md` | `20-应用框架层（ASTO）/ASTO-4AI.md` |
| `content/overview.md` | `MOC-理论导航.md` |
| `content/citation.md` | `CITATION.cff` |
| ... | 各层 `*-4AI.md` / `README.md` |

层元数据（DOI、上下游关系）维护在 `content/layers.json`，DOI 法源见母库 `.claude/ZENODO_SKILL.md`。

## 部署

push 到 `main` 分支 → GitHub Actions 自动构建 → 部署到 GitHub Pages。

域名 `asto.cc` 通过仓库根的 `public/CNAME`（构建时生成）绑定。
