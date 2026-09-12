#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the vector architecture diagram for EasyIndie / EasyOPC.

Design: a compact, spec-sheet style layer diagram
        层名 (layer) | EasyIndie 自研 (self-built) | 第三方工具 / 集成 (third-party)

Output: assets/architecture.svg
Usage:  python3 tools/gen-diagrams.py
"""
import html
import os

W, H = 1120, 656

ML = 28
ROW_R = W - 44          # 1076  right edge of layer rows
ROW_W = ROW_R - ML      # 1048
RAIL_X = W - 18         # 1102  feedback return rail

COL_NAME_R = ML + 192   # 220   name column right edge (separator 1)
COL_SELF_X = ML + 212   # 240   self-built chips start
COL_THIRD_SEP = ML + 612  # 640 separator 2
COL_THIRD_X = ML + 628  # 656   third-party text

ROW_H = 72
ROW_GAP = 10

TITLE_Y = 46
SUB_Y = 72
COLHEAD_Y = 112
ROWS_Y0 = 128

FB_H = 48
FB_Y = 548

FOOT_Y = 628


def esc(s):
    return html.escape(str(s), quote=True)


def tw(s, size):
    """Rough text width estimate: CJK = 1.0em, latin = 0.58em."""
    w = 0.0
    for ch in s:
        w += size * (1.0 if ord(ch) > 0x2E7F else 0.58)
    return w


class Svg:
    def __init__(self):
        self.p = []

    def add(self, s):
        self.p.append(s)

    def rect(self, x, y, w, h, rx, cls):
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" class="{cls}"/>'
        )

    def text(self, x, y, s, cls, anchor=None, extra=""):
        a = f' text-anchor="{anchor}"' if anchor else ""
        e = f" {extra}" if extra else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}{e}>{esc(s)}</text>')

    def line(self, x1, y1, x2, y2, cls):
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"/>'
        )

    def path(self, d, cls):
        self.add(f'<path d="{d}" class="{cls}"/>')

    def dump(self):
        return "\n".join(self.p)


# --------------------------------------------------------------------------- #
# Content: 5 layers, each = layer name / self-built projects / third-party tools
# --------------------------------------------------------------------------- #
LAYERS = [
    dict(
        num="1", name="AI 员工", sub="数字员工 · 承担执行",
        self_built=["EasyTeam", "EasyProject"],
        third="Claude Code · Codex · OpenClaw · Hermes",
    ),
    dict(
        num="2", name="能力与数据", sub="模型 · 知识 · 存储",
        self_built=["EasyAI"],
        third="Claude / GPT / Gemini · Obsidian / Notion · NAS",
    ),
    dict(
        num="3", name="生产与自动化", sub="内容 · 工程 · 运营",
        self_built=["EasyContentCreator", "EasyIndieSkill", "EasyGithub"],
        third="HyperFrames · Runway · n8n / Make",
    ),
    dict(
        num="4", name="获客与变现", sub="流量 · 转化 · 收入",
        self_built=["EasyGate"],
        third="Cloudflare · Vercel · Stripe / PayPal · 分发平台",
    ),
    dict(
        num="5", name="基础环境", sub="设备 · 网络 · 运维",
        self_built=["EasyNet", "EasyWork", "EasyAndroid"],
        third="Mac / PC · 防火墙 / VPN · GitHub / Docker",
    ),
]


def build():
    s = Svg()

    # ---- self-contained background
    s.rect(0, 0, W, H, 0, "bgfill")

    # ---- header
    s.text(ML, TITLE_Y, "一人公司基础设施架构", "h1")
    s.text(ML, SUB_Y, "一个人 + 一群 AI 员工 + 一套自动化系统 = 可持续运营的公司", "h2")

    # ---- column headers
    s.text(COL_SELF_X, COLHEAD_Y, "EasyIndie 自研", "colhead-ac")
    s.text(COL_THIRD_X, COLHEAD_Y, "第三方工具 / 集成", "colhead")

    # ---- layer rows
    for i, ly in enumerate(LAYERS):
        y = ROWS_Y0 + i * (ROW_H + ROW_GAP)
        s.rect(ML, y, ROW_W, ROW_H, 12, "row")

        # number badge
        s.add(f'<circle cx="{ML + 26:.1f}" cy="{y + ROW_H / 2:.1f}" r="13" class="badge"/>')
        s.text(ML + 26, y + ROW_H / 2 + 4.5, ly["num"], "num", anchor="middle")

        # layer name + sub
        s.text(ML + 50, y + 30, ly["name"], "ly")
        s.text(ML + 50, y + 50, ly["sub"], "lys")

        # column separators
        s.line(COL_NAME_R, y + 14, COL_NAME_R, y + ROW_H - 14, "sep")
        s.line(COL_THIRD_SEP, y + 14, COL_THIRD_SEP, y + ROW_H - 14, "sep")

        # self-built chips
        cx = COL_SELF_X
        cy = y + (ROW_H - 22) / 2
        for name in ly["self_built"]:
            cw = tw(name, 11.5) + 18
            s.rect(cx, cy, cw, 22, 11, "chip")
            s.text(cx + 9, cy + 15, name, "chip-t")
            cx += cw + 8

        # third-party text
        s.text(COL_THIRD_X, y + ROW_H / 2 + 4.5, ly["third"], "third")

    # ---- feedback row
    s.rect(ML, FB_Y, ROW_W, FB_H, 12, "fb-row")
    fcx, fcy = ML + 26, FB_Y + FB_H / 2
    s.add(f'<circle cx="{fcx:.1f}" cy="{fcy:.1f}" r="8" class="fbico"/>')
    s.path(f"M {fcx:.1f} {fcy - 13:.1f} l 3.6 5.2 l -7.2 0 z", "fbico-head")
    s.text(ML + 50, FB_Y + 21, "数据反馈闭环", "fb-t")
    s.text(ML + 50, FB_Y + 39,
           "用户行为 · 内容表现 · 销售数据 → 持续优化 选题 / 内容 / 产品 / 营销", "fbs")

    # ---- return rail: feedback row -> layer 1
    l1cy = ROWS_Y0 + ROW_H / 2
    mid = (FB_Y + FB_H / 2 + l1cy) / 2
    s.path(
        f"M {ROW_R:.1f} {fcy:.1f} H {RAIL_X:.1f} V {l1cy:.1f} H {ROW_R + 14:.1f}",
        "rail",
    )
    s.path(f"M {ROW_R:.1f} {l1cy:.1f} l 10 -5 l 0 10 z", "rail-head")
    s.text(
        RAIL_X + 6, mid, "优化回流", "railtx",
        extra=f'transform="rotate(-90 {RAIL_X + 6:.1f} {mid:.1f})"',
    )

    # ---- footer
    s.text(ML, FOOT_Y, "EasyIndie · EasyOPC — 用一个人 + AI，做一支团队的事。", "foot")

    body = s.dump()
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-labelledby="dT dD" preserveAspectRatio="xMidYMid meet">
  <title id="dT">一人公司基础设施架构图（EasyOPC）</title>
  <desc id="dD">五层结构：AI 员工、能力与数据、生产与自动化、获客与变现、基础环境。
  每层标注 EasyIndie 自研项目与第三方工具 / 集成，底部为数据反馈闭环。</desc>
  <style>
    svg {{
      --tx:#0d1117; --tx2:#5b6678; --tx3:#79839a; --bd:#e7e9ee; --bd2:#d5d9e0;
      --row:#ffffff; --row-bd:#e7e9ee; --ac:#4f46e5; --acs:#eef1ff; --acsbd:#c7ccf7;
      --bg:#ffffff;
      font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",Roboto,sans-serif;
    }}
    @media (prefers-color-scheme: dark) {{
      svg {{
        --tx:#e9edf3; --tx2:#a4aebd; --tx3:#8b95a6; --bd:#232936; --bd2:#333b4a;
        --row:#12151c; --row-bd:#232936; --ac:#818cf8; --acs:#191e30; --acsbd:#3b447a;
        --bg:#0a0c10;
      }}
    }}
    text {{ fill: var(--tx); }}
    .bgfill {{ fill: var(--bg); }}
    .h1 {{ font-size:26px; font-weight:700; letter-spacing:-.4px; }}
    .h2 {{ font-size:14px; fill:var(--tx2); }}
    .colhead {{ font-size:11.5px; fill:var(--tx3); letter-spacing:.02em; }}
    .colhead-ac {{ font-size:11.5px; fill:var(--ac); font-weight:600; letter-spacing:.02em; }}
    .row {{ fill:var(--row); stroke:var(--row-bd); stroke-width:1; }}
    .badge {{ fill:var(--ac); }}
    .num {{ fill:#fff; font-size:13px; font-weight:700; }}
    .ly {{ font-size:15px; font-weight:700; }}
    .lys {{ font-size:11.5px; fill:var(--tx2); }}
    .sep {{ stroke:var(--bd2); stroke-width:1; }}
    .chip {{ fill:var(--acs); stroke:var(--acsbd); stroke-width:1; }}
    .chip-t {{ font-size:11.5px; font-weight:600; fill:var(--ac); }}
    .third {{ font-size:11.5px; fill:var(--tx2); }}
    .fb-row {{ fill:none; stroke:var(--ac); stroke-width:1.2; stroke-dasharray:5 4; }}
    .fbico {{ fill:none; stroke:var(--ac); stroke-width:1.5; }}
    .fbico-head {{ fill:var(--ac); }}
    .fb-t {{ font-size:14px; font-weight:700; fill:var(--ac); }}
    .fbs {{ font-size:11.5px; fill:var(--tx2); }}
    .rail {{ fill:none; stroke:var(--ac); stroke-width:1.3; stroke-dasharray:5 4; opacity:.65; }}
    .rail-head {{ fill:var(--ac); opacity:.65; }}
    .railtx {{ font-size:11px; fill:var(--ac); }}
    .foot {{ font-size:11.5px; fill:var(--tx3); }}
  </style>
{body}
</svg>
'''


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "assets", "architecture.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    svg = build()
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out} ({len(svg.encode('utf-8'))} bytes)")
