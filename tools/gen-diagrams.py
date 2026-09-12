#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the vector architecture diagram for EasyIndie / EasyOPC.

Output: assets/architecture.svg  (1200x880 viewBox, responsive, light/dark aware)

Usage:  python3 tools/gen-diagrams.py
"""
import html
import os
import sys

W, H = 1120, 880
ML = 28            # left margin
LAYER_R = 1076     # right edge of layer bands
LAYER_W = LAYER_R - ML
RAIL_X = W - 20    # feedback return rail

LAYER_H = 112
LAYER_GAP = 18
L1_Y = 122
FB_Y, FB_H = 776, 44

ACCENT = "var(--ac)"


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

    def rect(self, x, y, w, h, rx, cls, extra=""):
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx:.1f}" class="{cls}"{(" " + extra) if extra else ""}/>'
        )

    def text(self, x, y, s, cls, anchor=None, extra=""):
        a = f' text-anchor="{anchor}"' if anchor else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}{(" " + extra) if extra else ""}>{esc(s)}</text>')

    def line(self, x1, y1, x2, y2, cls, extra=""):
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'class="{cls}"{(" " + extra) if extra else ""}/>'
        )

    def path(self, d, cls, extra=""):
        self.add(f'<path d="{d}" class="{cls}"{(" " + extra) if extra else ""}/>')

    def dump(self):
        return "\n".join(self.p)


# --------------------------------------------------------------------------- #
# Diagram content
# --------------------------------------------------------------------------- #
LAYERS = [
    dict(num="1", name="AI 员工层", sub="数字员工 · 承担执行", cards=[
        dict(t="开发 Agent", d="代码 · 调试 · 测试 · 部署"),
        dict(t="内容 / 研究 Agent", d="脚本 · 素材 · 调研 · 分析"),
        dict(t="团队编排", d="角色定义 · 工作流 · 协作", pills=[("EasyTeam", 1)]),
        dict(t="工程规范", d="AI Native 目录与协作标准", pills=[("EasyProject", 1)]),
    ]),
    dict(num="2", name="能力与数据层", sub="模型 · 知识 · 数据", cards=[
        dict(t="大模型能力", d="Claude / GPT / Gemini 统一接入", pills=[("EasyAI", 1)]),
        dict(t="知识库", d="Obsidian / Notion / Outline"),
        dict(t="共享存储 · SSOT", d="NAS · SMB/WebDAV/API · 单一事实源"),
    ]),
    dict(num="3", name="生产与自动化层", sub="内容 · 工程 · 运营", cards=[
        dict(t="内容生产流水线", d="选题→脚本→分镜→视频→发布",
             pills=[("EasyContentCreator", 1), ("EasyIndieSkill", 1)]),
        dict(t="工程自动化", d="Issue → Actions → Agent → PR", pills=[("EasyGithub", 1)]),
        dict(t="运营工作流", d="n8n / Make · 触发器与调度"),
    ]),
    dict(num="4", name="获客与变现层", sub="流量 · 转化 · 收入", cards=[
        dict(t="入口与官网", d="落地页 · 博客 · 登录", pills=[("EasyGate", 1)]),
        dict(t="触达与转化", d="邮件 · CRM · 数据分析"),
        dict(t="支付与结算", d="Stripe / PayPal · 订阅"),
        dict(t="分发与收入", d="内容 · 课程 · SaaS · 咨询"),
    ]),
    dict(num="5", name="基础环境", sub="设备 · 网络 · 运维", cards=[
        dict(t="设备", d="Mac / PC / 手机 / NAS", pills=[("EasyAndroid", 1)]),
        dict(t="网络与安全", d="防火墙 · VPN · 内网穿透 · 备份", pills=[("EasyNet", 1)]),
        dict(t="开发与运维", d="环境配置 · Docker · 监控告警", pills=[("EasyWork", 1)]),
    ]),
]


def build():
    s = Svg()

    # ---- self-contained background (keeps the SVG legible when opened directly)
    s.rect(0, 0, W, H, 0, "bgfill")

    # ---- header
    s.text(ML, 46, "一人公司基础设施架构", "h1")
    s.text(ML, 72, "一个人 + 一群 AI 员工 + 一套自动化系统 = 可持续运营的公司", "h2")

    # legend (right aligned)
    lx = LAYER_R
    t2 = "第三方工具 / 集成"
    w2 = 16 + tw(t2, 11.5)
    x2 = lx - w2
    s.add(f'<circle cx="{x2 + 5:.1f}" cy="{96 - 4:.1f}" r="5" class="sw-out"/>')
    s.text(x2 + 16, 100, t2, "leg")

    t1 = "EasyIndie 自研"
    w1 = 16 + tw(t1, 11.5)
    x1 = x2 - 22 - w1
    s.add(f'<circle cx="{x1 + 5:.1f}" cy="{96 - 4:.1f}" r="5" class="sw-in"/>')
    s.text(x1 + 16, 100, t1, "leg")

    # ---- layer bands
    for i, ly in enumerate(LAYERS):
        y = L1_Y + i * (LAYER_H + LAYER_GAP)
        s.rect(ML, y, LAYER_W, LAYER_H, 14, "band")

        # number badge
        s.add(f'<circle cx="{ML + 24:.1f}" cy="{y + 32:.1f}" r="13" class="badge"/>')
        s.text(ML + 24, y + 37, ly["num"], "num", anchor="middle")

        # layer name + sub
        s.text(ML + 48, y + 30, ly["name"], "ly")
        s.text(ML + 48, y + 52, ly["sub"], "lys")

        # separator
        s.line(ML + 156, y + 16, ML + 156, y + LAYER_H - 16, "sep")

        # cards
        cards = ly["cards"]
        n = len(cards)
        gap = 12.0
        cx0 = ML + 170
        cx1 = LAYER_R - 14
        region = cx1 - cx0
        cw = (region - gap * (n - 1)) / n

        for j, c in enumerate(cards):
            x = cx0 + j * (cw + gap)
            cy = y + 14
            ch = LAYER_H - 28
            s.rect(x, cy, cw, ch, 10, "card")
            s.text(x + 13, cy + 26, c["t"], "ct")
            s.text(x + 13, cy + 48, c["d"], "cd")

            # pills
            px = x + 13
            py = cy + ch - 17 - 11
            for label, is_self in c.get("pills", []):
                pw = tw(label, 10.5) + 14
                cls = "pill-s" if is_self else "pill-n"
                s.rect(px, py, pw, 17, 8.5, cls)
                s.text(px + 7, py + 12.4, label, "pill-t" if is_self else "pill-tn")
                px += pw + 6

    # ---- feedback band
    s.rect(ML, FB_Y, LAYER_W, FB_H, 12, "fb-band")
    fcx, fcy = ML + 26, FB_Y + FB_H / 2
    s.add(f'<circle cx="{fcx:.1f}" cy="{fcy:.1f}" r="8" class="fbico"/>')
    s.path(f"M {fcx:.1f} {fcy - 13:.1f} l 3.6 5.2 l -7.2 0 z", "fbico-head")
    s.text(ML + 50, FB_Y + 20, "数据反馈闭环", "fb-t")
    s.text(ML + 50, FB_Y + 36, "用户行为 · 内容表现 · 销售数据 → 持续优化 选题 / 内容 / 产品 / 营销", "fbs")

    # return rail: feedback band -> L1
    l1cy = L1_Y + LAYER_H / 2
    mid = (FB_Y + l1cy) / 2
    s.path(
        f"M {LAYER_R:.1f} {FB_Y + FB_H / 2:.1f} H {RAIL_X:.1f} V {l1cy:.1f} H {LAYER_R + 14:.1f}",
        "rail",
    )
    s.path(
        f"M {LAYER_R:.1f} {l1cy:.1f} l 10 -5 l 0 10 z",
        "rail-head",
    )
    s.text(
        RAIL_X + 6, mid, "优化回流", "railtx",
        extra=f' transform="rotate(-90 {RAIL_X + 6:.1f} {mid:.1f})"',
    )

    # ---- footer
    s.text(ML, 850, "EasyIndie · EasyOPC — 用一个人 + AI，做一支团队的事。", "foot")

    body = s.dump()
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-labelledby="diagramTitle diagramDesc" preserveAspectRatio="xMidYMid meet">
  <title id="diagramTitle">一人公司基础设施架构图（EasyOPC）</title>
  <desc id="diagramDesc">分五层展示 AI 员工层、能力与数据层、生产与自动化层、获客与变现层、基础环境，
  标注 EasyIndie 自研项目（EasyTeam、EasyProject、EasyAI、EasyContentCreator、EasyIndieSkill、
  EasyGithub、EasyGate、EasyAndroid、EasyNet、EasyWork）与第三方集成，并以数据反馈闭环收口。</desc>
  <style>
    svg {{
      --tx:#0d1117; --tx2:#59647a; --bd:#e7e9ee; --bd2:#d5d9e0;
      --band:#f8f9fb; --card:#ffffff; --ac:#4f46e5; --acs:#eef1ff; --rail:#b9c0cd; --bg:#ffffff;
      font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",Roboto,sans-serif;
    }}
    @media (prefers-color-scheme: dark) {{
      svg {{
        --tx:#e9edf3; --tx2:#a4aebd; --bd:#232936; --bd2:#333b4a;
        --band:#0e1116; --card:#12151c; --ac:#818cf8; --acs:#1c2033; --rail:#3a4253; --bg:#0a0c10;
      }}
    }}
    text {{ fill: var(--tx); }}
    .bgfill {{ fill: var(--bg); }}
    .h1 {{ font-size:26px; font-weight:700; letter-spacing:-.4px; }}
    .h2 {{ font-size:14px; fill:var(--tx2); }}
    .band {{ fill:var(--band); stroke:var(--bd); stroke-width:1; }}
    .card {{ fill:var(--card); stroke:var(--bd); stroke-width:1; }}
    .badge {{ fill:var(--ac); }}
    .num {{ fill:#fff; font-size:13px; font-weight:700; }}
    .ly {{ font-size:15px; font-weight:700; }}
    .lys {{ font-size:11.5px; fill:var(--tx2); }}
    .sep {{ stroke:var(--bd2); stroke-width:1; }}
    .ct {{ font-size:14px; font-weight:650; }}
    .cd {{ font-size:11.5px; fill:var(--tx2); }}
    .pill-s {{ fill:var(--acs); stroke:var(--ac); stroke-width:1; }}
    .pill-n {{ fill:var(--band); stroke:var(--bd2); stroke-width:1; }}
    .pill-t {{ font-size:10.5px; font-weight:600; fill:var(--ac); }}
    .pill-tn {{ font-size:10.5px; font-weight:600; fill:var(--tx2); }}
    .leg {{ font-size:11.5px; fill:var(--tx2); }}
    .sw-in {{ fill:var(--ac); }}
    .sw-out {{ fill:var(--card); stroke:var(--bd2); stroke-width:1.5; }}
    .fb-band {{ fill:var(--acs); stroke:var(--ac); stroke-width:1.2; stroke-dasharray:5 4; }}
    .fbico {{ fill:none; stroke:var(--ac); stroke-width:1.5; }}
    .fbico-head {{ fill:var(--ac); }}
    .fb-t {{ font-size:14px; font-weight:700; }}
    .fbs {{ font-size:11.5px; fill:var(--tx2); }}
    .rail {{ fill:none; stroke:var(--ac); stroke-width:1.4; stroke-dasharray:5 4; }}
    .rail-head {{ fill:var(--ac); }}
    .railtx {{ font-size:11px; fill:var(--ac); }}
    .foot {{ font-size:11.5px; fill:var(--tx2); }}
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
