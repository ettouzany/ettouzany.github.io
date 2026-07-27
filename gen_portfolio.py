import json

nodes = []
_id = [0]
def nid():
    _id[0] += 1
    return f"pf{_id[0]:03d}"

def base(**kw):
    n = {
        "id": nid(),
        "type": "rect",
        "name": "n",
        "parentId": None,
        "x": 0, "y": 0, "width": 100, "height": 100,
        "rotation": 0, "opacity": 1,
        "fill": "#000000", "stroke": "#000000",
        "strokeWidth": 0, "radius": 0,
    }
    n.update(kw)
    nodes.append(n)
    return n["id"]

def rect(name, x, y, w, h, fill, radius=0, stroke="#000000", sw=0, opacity=1, gradient=None):
    n = {
        "id": nid(), "type": "rect", "name": name, "parentId": None,
        "x": x, "y": y, "width": w, "height": h, "rotation": 0, "opacity": opacity,
        "fill": fill, "stroke": stroke, "strokeWidth": sw, "radius": radius,
    }
    if gradient:
        n["gradient"] = gradient
    nodes.append(n)
    return n["id"]

def ellipse(name, x, y, w, h, fill, stroke="#000000", sw=0, opacity=1, gradient=None):
    n = {
        "id": nid(), "type": "ellipse", "name": name, "parentId": None,
        "x": x, "y": y, "width": w, "height": h, "rotation": 0, "opacity": opacity,
        "fill": fill, "stroke": stroke, "strokeWidth": sw, "radius": 0,
    }
    if gradient:
        n["gradient"] = gradient
    nodes.append(n)
    return n["id"]

def text(name, x, y, w, h, s, size, color, weight=400, align="left"):
    n = {
        "id": nid(), "type": "text", "name": name, "parentId": None,
        "x": x, "y": y, "width": w, "height": h, "rotation": 0, "opacity": 1,
        "fill": "transparent", "stroke": "#000000", "strokeWidth": 0, "radius": 0,
        "text": s, "fontSize": size, "fontFamily": "Inter", "fontWeight": weight,
        "align": align, "color": color,
    }
    nodes.append(n)
    return n["id"]

def line(name, x, y, w, h, fill):
    return rect(name, x, y, w, h, fill, radius=0)

# palette
BG      = "#17131f"
PANEL   = "#221d2e"
CARD    = "#241f31"
BORDER  = "#342c46"
GREEN   = "#16a34a"
GREENB  = "#22c55e"
WHITE   = "#ffffff"
TEXT    = "#c9c4d6"
MUTED   = "#8f88a6"
DIM     = "#6f6885"
GTINT   = "#1e3a2b"

W = 1440
H = 3700

# ============ BACKGROUND ============
base(type="frame", name="Frame", x=0, y=0, width=W, height=H,
     fill=BG, stroke=BORDER, strokeWidth=1, radius=0, clip=True)

# soft hero glow
ellipse("glow", 760, -120, 620, 620, GREEN, opacity=0.10)
ellipse("glow2", 120, 520, 380, 380, "#5b3fb0", opacity=0.08)

# ============ NAV ============
text("logo", 120, 46, 120, 34, "NE.", 26, WHITE, 800)
text("nav1", 900, 52, 90, 22, "About", 15, MUTED, 600, "center")
text("nav2", 1000, 52, 90, 22, "Skills", 15, MUTED, 600, "center")
text("nav3", 1100, 52, 90, 22, "Work", 15, MUTED, 600, "center")
rect("navcta", 1200, 42, 120, 42, GREEN, radius=10)
text("nav4", 1200, 53, 120, 22, "Contact", 15, WHITE, 700, "center")

# ============ HERO ============
# eyebrow
ellipse("dot", 120, 176, 10, 10, GREENB)
text("eyebrow", 142, 170, 400, 20, "AVAILABLE FOR NEW PROJECTS", 13, GREENB, 700)
# name
text("h1a", 118, 200, 640, 84, "Noureddine", 74, WHITE, 800)
text("h1b", 118, 284, 640, 84, "Ettouzany", 74, GREEN, 800)
# role
text("role", 120, 398, 640, 34, "Full Stack Engineer", 25, TEXT, 600)
# paragraph
text("p1", 120, 448, 600, 26, "8+ years building high-quality web and mobile", 17, MUTED, 400)
text("p2", 120, 476, 600, 26, "solutions — leading teams, architecture, and", 17, MUTED, 400)
text("p3", 120, 504, 600, 26, "code quality that fuels business growth.", 17, MUTED, 400)
# buttons
rect("btn1", 120, 566, 200, 56, GREEN, radius=12)
text("btn1t", 120, 583, 200, 24, "View My Work", 16, WHITE, 700, "center")
rect("btn2", 338, 566, 180, 56, "transparent", radius=12, stroke=BORDER, sw=1.5)
text("btn2t", 338, 583, 180, 24, "Get in Touch", 16, TEXT, 700, "center")

# avatar cluster (right)
ellipse("av-ring", 946, 196, 340, 340, "transparent", stroke=GREEN, sw=2, opacity=0.5)
ellipse("av", 976, 226, 280, 280, GREEN, gradient={"angle":135,"stops":[
    {"color":"#22c55e","pos":0},{"color":"#15803d","pos":1}]})
text("av-init", 976, 300, 280, 130, "NE", 104, WHITE, 800, "center")
# floating badge
rect("badge", 900, 430, 190, 64, CARD, radius=14, stroke=BORDER, sw=1)
text("badge-n", 918, 442, 120, 26, "40+", 22, GREENB, 800)
text("badge-l", 918, 470, 160, 18, "Projects shipped", 12, MUTED, 500)

# ============ STATS BAR ============
line("stat-div", 120, 706, 1200, 1, BORDER)
stats = [("8+", "Years Experience"), ("40+", "Projects Delivered"),
         ("10+", "Companies"), ("3", "Languages")]
sx = 120
for num, lab in stats:
    text(f"stn", sx, 730, 200, 44, num, 38, WHITE, 800)
    text(f"stl", sx, 782, 220, 20, lab, 14, MUTED, 500)
    sx += 300

# ============ SKILLS ============
Y = 900
text("sk-tag", 120, Y, 300, 20, "WHAT I DO", 13, GREENB, 700)
text("sk-title", 120, Y+26, 700, 52, "Skills & Expertise", 44, WHITE, 800)

skills = [
    ("‹⁄›", "Frontend", "React, Next.js, TypeScript, Angular, Tailwind CSS"),
    ("⚡", "Backend", "Node.js, NestJS, Express, Spring Boot, .NET Core"),
    ("☁", "Cloud & DevOps", "AWS, Docker, Kubernetes, CI/CD, Terraform"),
    ("▤", "Databases", "PostgreSQL, MySQL, Redis, MongoDB, Firebase"),
    ("▢", "Mobile", "React Native, Flutter, Ionic, Swift"),
    ("⊕", "Languages", "Arabic (Native), French (Fluent), English (Pro)"),
]
cardW, cardH, gap = 380, 176, 30
cols = [120, 120+cardW+gap, 120+2*(cardW+gap)]
gridY = Y + 110
for i, (icon, tt, body) in enumerate(skills):
    cx = cols[i % 3]
    cy = gridY + (i // 3) * (cardH + gap)
    rect(f"c{i}", cx, cy, cardW, cardH, CARD, radius=18, stroke=BORDER, sw=1)
    rect(f"c{i}i", cx+28, cy+28, 52, 52, GTINT, radius=14)
    text(f"c{i}ig", cx+28, cy+40, 52, 30, icon, 22, GREENB, 700, "center")
    text(f"c{i}t", cx+28, cy+96, cardW-56, 26, tt, 20, WHITE, 700)
    text(f"c{i}b", cx+28, cy+128, cardW-56, 36, body, 14, MUTED, 400)

# ============ EXPERIENCE ============
EY = gridY + 2*(cardH+gap) + 90
text("ex-tag", 120, EY, 300, 20, "CAREER JOURNEY", 13, GREENB, 700)
text("ex-title", 120, EY+26, 700, 52, "Experience", 44, WHITE, 800)

exp = [
    ("2025  ·  React", "CTO — PUT",
     "Leading the technical vision and architecture of a real-estate platform."),
    ("2024 — 2025  ·  Java", "Team Leader / Software Manager — Sahty",
     "Managing a cross-functional team, driving architecture and scalable systems."),
    ("2021 — 2026  ·  React · .NET Core", "Front-end Developer — Tygo.sa",
     "SIM / eSIM comparison platform covering 250+ packages in Saudi Arabia."),
    ("2023  ·  Angular", "Front-end Developer — Senaei (Ministry of Industry, SA)",
     "Angular interfaces for industrial licensing and compliance workflows."),
    ("2022  ·  Next.js", "Project Manager — Derwork",
     "Next.js jobs platform with listings, company reviews and dashboards."),
    ("2022  ·  Flutter", "App Developer — Edoc",
     "Built 8 educational apps teaching programming with lessons and quizzes."),
    ("2022  ·  Flutter", "App / Web Developer — Havatar",
     "Independently built a full Glovo-style delivery platform end to end."),
    ("2022  ·  PrestaShop", "PrestaShop Developer — Lalic",
     "E-commerce stores with themes, modules and payment integrations."),
    ("2018  ·  Angular", "Front-End Developer & Designer — fekrasystems",
     "Delivered 10+ Angular management systems with responsive UI/UX."),
    ("2017  ·  WordPress", "WordPress Front-End — lgaming.ma",
     "Started my career building responsive WordPress sites and designs."),
]
rowY = EY + 110
rowH = 124
lineTop = rowY + 4
lineBot = rowY + (len(exp)-1)*rowH + 12
line("tl", 149, lineTop, 2, lineBot-lineTop, BORDER)
for i, (meta, title, desc) in enumerate(exp):
    ry = rowY + i*rowH
    ellipse(f"e{i}d", 140, ry, 20, 20, GREEN, stroke=BG, sw=4)
    text(f"e{i}m", 200, ry-2, 900, 20, meta, 13, GREENB, 700)
    text(f"e{i}t", 200, ry+20, 1000, 26, title, 20, WHITE, 700)
    text(f"e{i}x", 200, ry+50, 1000, 22, desc, 14, MUTED, 400)

# ============ EDUCATION strip ============
EDY = rowY + len(exp)*rowH + 30
text("ed-tag", 120, EDY, 300, 20, "EDUCATION", 13, GREENB, 700)
text("ed-title", 120, EDY+26, 700, 44, "Academic Background", 36, WHITE, 800)
edu = [
    ("42 Network", "Master of Computer Science (MSCS)", "2019 — 2023"),
    ("ENSA", "Bachelor — Big Data & Machine Learning", "2021 — 2022"),
    ("OFPPT", "Diploma in Computer Science", "2018 — 2020"),
]
edW = 380
edCols = [120, 120+edW+gap, 120+2*(edW+gap)]
edGY = EDY + 100
for i, (sch, deg, yr) in enumerate(edu):
    ex = edCols[i]
    rect(f"ed{i}", ex, edGY, edW, 150, CARD, radius=18, stroke=BORDER, sw=1)
    text(f"ed{i}y", ex+28, edGY+26, edW-56, 18, yr, 12, GREENB, 700)
    text(f"ed{i}s", ex+28, edGY+52, edW-56, 26, sch, 21, WHITE, 700)
    text(f"ed{i}d", ex+28, edGY+86, edW-56, 40, deg, 14, MUTED, 400)

# ============ CONTACT ============
CY = edGY + 150 + 90
rect("ct-card", 120, CY, 1200, 320, PANEL, radius=28, stroke=BORDER, sw=1)
ellipse("ct-glow", 980, CY+30, 360, 360, GREEN, opacity=0.10)
text("ct-tag", 168, CY+56, 400, 20, "LET'S WORK TOGETHER", 13, GREENB, 700)
text("ct-title", 166, CY+82, 800, 52, "Have a project in mind?", 42, WHITE, 800)
text("ct-sub", 168, CY+146, 640, 26,
     "I'm open to full-time roles, freelance and collaboration.", 17, MUTED, 400)
# contact rows
text("ct-e-l", 168, CY+204, 120, 16, "EMAIL", 11, DIM, 700)
text("ct-e-v", 168, CY+222, 360, 22, "n.ettouzany@gmail.com", 16, TEXT, 500)
text("ct-p-l", 168, CY+256, 120, 16, "PHONE", 11, DIM, 700)
text("ct-p-v", 168, CY+274, 360, 22, "+212 691 949 534", 16, TEXT, 500)
text("ct-w-l", 520, CY+204, 160, 16, "WEBSITE", 11, DIM, 700)
text("ct-w-v", 520, CY+222, 360, 22, "www.ettouzany.me", 16, TEXT, 500)
text("ct-in-l", 520, CY+256, 160, 16, "LINKEDIN", 11, DIM, 700)
text("ct-in-v", 520, CY+274, 360, 22, "in/noureddine-ettouzany", 16, TEXT, 500)
# CTA button in card
rect("ct-btn", 986, CY+150, 280, 60, GREEN, radius=14)
text("ct-btn-t", 986, CY+168, 280, 26, "Say Hello →", 17, WHITE, 700, "center")
text("ct-gh", 986, CY+240, 280, 20, "github.com/ettouzany", 14, MUTED, 500, "center")

# ============ FOOTER ============
FY = CY + 320 + 40
line("ft-div", 120, FY, 1200, 1, BORDER)
text("ft-c", 120, FY+24, 600, 20, "© 2026 Noureddine Ettouzany", 14, DIM, 500)
text("ft-r", 720, FY+24, 600, 20, "Built with passion · Full Stack Engineer", 14, DIM, 500, "right")

design = {
    "version": 2,
    "canvas": {"width": W, "height": H, "background": BG},
    "nodes": nodes,
}
with open("/Users/apple/Desktop/portffff/portfolio.dsx", "w") as f:
    json.dump(design, f, indent=2)
print("wrote", len(nodes), "nodes; canvas", W, "x", H, "; contact at", CY, "footer at", FY)
