"""Generate the A4 print-ready CV in English, French and Arabic.

Writes cv/cv-<lang>.html. Each page is exactly one A4 sheet (210x297mm) with
@page rules, so printing from a browser — or `render_cv_pdf.py` — produces a
clean PDF with no margins or overflow. Arabic is rendered RTL with the whole
layout mirrored.
"""

import json
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cv")

# --- shared, language-independent data -------------------------------------

CONTACT = [
    ("EMAIL", "n.ettouzany@gmail.com"),
    ("PHONE", "+212 691 949 534"),
    ("WEBSITE", "www.ettouzany.me"),
    ("LINKEDIN", "in/noureddine-ettouzany"),
    ("GITHUB", "github.com/ettouzany"),
]

SKILL_VALUES = [
    "React, Next.js, TypeScript, Angular, Tailwind",
    "Node.js, NestJS, Express, Spring Boot, .NET Core",
    "AWS, Docker, Kubernetes, CI/CD, Terraform",
    "PostgreSQL, MySQL, Redis, MongoDB, Firebase",
    "React Native, Flutter, Ionic, Swift",
]

# (role, company, meta, description) per language; meta stays LTR everywhere.
EXPERIENCE_META = [
    "2026  ·  Next.js  ·  TypeScript",
    "2025  ·  React",
    "2024 — 2025  ·  Java",
    "2021 — 2026  ·  React  ·  .NET Core",
    "2023  ·  Angular",
    "2022  ·  Next.js",
    "2022  ·  Flutter",
    "2022  ·  Flutter",
    "2022  ·  PrestaShop",
    "2018  ·  Angular",
    "2017  ·  WordPress",
]

EDUCATION_YEARS = ["2019 — 2023", "2021 — 2022", "2018 — 2020"]

# --- per-language content ---------------------------------------------------

EN = {
    "code": "en",
    "dir": "ltr",
    "font": "'Inter', system-ui, sans-serif",
    "name": "NOUREDDINE ETTOUZANY",
    "role": "FULL STACK ENGINEER",
    "headings": {
        "contact": "CONTACT",
        "skills": "SKILLS",
        "education": "EDUCATION",
        "languages": "LANGUAGES",
        "profile": "PROFILE",
        "experience": "EXPERIENCE",
    },
    "contact_labels": ["EMAIL", "PHONE", "WEBSITE", "LINKEDIN", "GITHUB"],
    "skill_labels": ["Frontend", "Backend", "Cloud & DevOps", "Databases", "Mobile"],
    "profile": (
        "Full Stack Engineer with 8+ years of experience delivering high-quality web and "
        "mobile solutions. I transform and enhance web presence, lead engineering teams, and "
        "drive architecture and code-quality standards to fuel business growth."
    ),
    "education": [
        ("42 Network", "Master of Computer Science (MSCS)"),
        ("ENSA", "Bachelor — Big Data & Machine Learning"),
        ("OFPPT", "Diploma in Computer Science"),
    ],
    "languages": ["Arabic — Native", "French — Fluent", "English — Professional"],
    "experience": [
        (
            "Full Stack Engineer — Acorvo",
            "Built the front-end of a dental practice management SaaS: patient records, smart "
            "scheduling, billing and analytics dashboards, role-based access and a multilingual UI.",
        ),
        (
            "CTO — PUT",
            "Leading the technical vision and architecture of PUT, a real-estate platform for "
            "renting, selling and managing property.",
        ),
        (
            "Team Leader / Software Manager — Sahty",
            "Managing a cross-functional engineering team, driving architecture and code-quality "
            "standards, and delivering scalable systems.",
        ),
        (
            "Front-end Developer — Tygo.sa",
            "Built user-facing features for a SIM / eSIM comparison platform covering 250+ "
            "packages in Saudi Arabia.",
        ),
        (
            "Front-end Developer — Senaei (Ministry of Industry, SA)",
            "Developed Angular interfaces simplifying industrial licensing and compliance "
            "workflows for investors.",
        ),
        (
            "Project Manager — Derwork",
            "Led delivery of a Next.js jobs platform with listings, company reviews and "
            "dashboards, managing cross-functional teams.",
        ),
        (
            "App Developer — Edoc",
            "Designed and built 8 educational apps teaching programming languages with lessons "
            "and quizzes.",
        ),
        (
            "App / Web Developer — Havatar",
            "Independently built a full delivery platform (Glovo-style) for customers, drivers "
            "and merchants.",
        ),
        (
            "PrestaShop Developer — Lalic",
            "Developed and customized e-commerce stores with themes, modules and payment "
            "integrations.",
        ),
        (
            "Front-End Developer & Designer — fekrasystems",
            "Delivered 10+ Angular management systems with responsive, user-friendly UI/UX.",
        ),
        (
            "WordPress Front-End — lgaming.ma",
            "Started my career building responsive WordPress websites and front-end designs.",
        ),
    ],
}

FR = {
    "code": "fr",
    "dir": "ltr",
    "font": "'Inter', system-ui, sans-serif",
    "name": "NOUREDDINE ETTOUZANY",
    "role": "INGÉNIEUR FULL STACK",
    "headings": {
        "contact": "CONTACT",
        "skills": "COMPÉTENCES",
        "education": "FORMATION",
        "languages": "LANGUES",
        "profile": "PROFIL",
        "experience": "EXPÉRIENCE",
    },
    "contact_labels": ["E-MAIL", "TÉLÉPHONE", "SITE WEB", "LINKEDIN", "GITHUB"],
    "skill_labels": ["Frontend", "Backend", "Cloud & DevOps", "Bases de données", "Mobile"],
    "profile": (
        "Ingénieur Full Stack avec plus de 8 ans d'expérience dans la livraison de solutions web "
        "et mobiles de haute qualité. Je transforme et renforce la présence web, dirige des "
        "équipes d'ingénierie et impose des standards d'architecture et de qualité de code au "
        "service de la croissance."
    ),
    "education": [
        ("42 Network", "Master en informatique (MSCS)"),
        ("ENSA", "Licence — Big Data & Machine Learning"),
        ("OFPPT", "Diplôme en informatique"),
    ],
    "languages": ["Arabe — Langue maternelle", "Français — Courant", "Anglais — Professionnel"],
    "experience": [
        (
            "Ingénieur Full Stack — Acorvo",
            "Développement du front-end d'un SaaS de gestion de cabinets dentaires : dossiers "
            "patients, planification intelligente, facturation, tableaux de bord analytiques, "
            "accès par rôle et interface multilingue.",
        ),
        (
            "CTO — PUT",
            "Direction de la vision technique et de l'architecture de PUT, plateforme immobilière "
            "de location, vente et gestion de biens.",
        ),
        (
            "Team Leader / Software Manager — Sahty",
            "Encadrement d'une équipe d'ingénierie pluridisciplinaire, définition de "
            "l'architecture et des standards de qualité, livraison de systèmes scalables.",
        ),
        (
            "Développeur Front-end — Tygo.sa",
            "Développement des fonctionnalités utilisateur d'une plateforme de comparaison SIM / "
            "eSIM couvrant plus de 250 forfaits en Arabie saoudite.",
        ),
        (
            "Développeur Front-end — Senaei (Ministère de l'Industrie, AS)",
            "Création d'interfaces Angular simplifiant les démarches de licences industrielles et "
            "de conformité pour les investisseurs.",
        ),
        (
            "Chef de projet — Derwork",
            "Pilotage de la livraison d'une plateforme d'emploi Next.js : annonces, avis "
            "d'entreprises et tableaux de bord, avec des équipes pluridisciplinaires.",
        ),
        (
            "Développeur d'applications — Edoc",
            "Conception et développement de 8 applications éducatives enseignant la programmation "
            "via des leçons et des quiz.",
        ),
        (
            "Développeur App / Web — Havatar",
            "Réalisation en autonomie d'une plateforme de livraison complète (type Glovo) pour "
            "clients, livreurs et commerçants.",
        ),
        (
            "Développeur PrestaShop — Lalic",
            "Développement et personnalisation de boutiques e-commerce : thèmes, modules et "
            "intégrations de paiement.",
        ),
        (
            "Développeur Front-End & Designer — fekrasystems",
            "Livraison de plus de 10 systèmes de gestion Angular avec une UI/UX responsive et "
            "ergonomique.",
        ),
        (
            "Front-End WordPress — lgaming.ma",
            "Débuts de carrière : création de sites WordPress responsives et de designs front-end.",
        ),
    ],
}

AR = {
    "code": "ar",
    "dir": "rtl",
    "font": "'Cairo', 'Noto Sans Arabic', sans-serif",
    "name": "نور الدين التوزاني",
    "role": "مهندس تطوير متكامل Full Stack",
    "headings": {
        "contact": "التواصل",
        "skills": "المهارات",
        "education": "التعليم",
        "languages": "اللغات",
        "profile": "نبذة",
        "experience": "الخبرة المهنية",
    },
    "contact_labels": ["البريد الإلكتروني", "الهاتف", "الموقع الإلكتروني", "لينكد إن", "غيت هَب"],
    "skill_labels": ["الواجهة الأمامية", "الواجهة الخلفية", "السحابة و DevOps", "قواعد البيانات", "تطبيقات الموبايل"],
    "profile": (
        "مهندس تطوير متكامل بخبرة تفوق 8 سنوات في إنجاز حلول ويب وتطبيقات موبايل عالية الجودة. "
        "أطوّر الحضور الرقمي للشركات، وأقود فرق الهندسة، وأرسّخ معايير البنية البرمجية وجودة "
        "الكود بما يدعم نمو الأعمال."
    ),
    "education": [
        ("42 Network", "ماجستير في علوم الحاسوب (MSCS)"),
        ("ENSA", "إجازة — البيانات الضخمة وتعلّم الآلة"),
        ("OFPPT", "دبلوم في علوم الحاسوب"),
    ],
    "languages": ["العربية — اللغة الأم", "الفرنسية — بطلاقة", "الإنجليزية — مستوى مهني"],
    "experience": [
        (
            "مهندس تطوير متكامل — Acorvo",
            "تطوير الواجهة الأمامية لمنصة SaaS لإدارة عيادات الأسنان: ملفات المرضى، الجدولة "
            "الذكية، الفوترة، لوحات التحليلات، صلاحيات حسب الدور وواجهة متعددة اللغات.",
        ),
        (
            "مدير تقني (CTO) — PUT",
            "قيادة الرؤية التقنية والبنية البرمجية لمنصة PUT العقارية لكراء وبيع وإدارة العقارات.",
        ),
        (
            "قائد فريق / مدير برمجيات — Sahty",
            "إدارة فريق هندسي متعدد التخصصات، ووضع معايير البنية البرمجية وجودة الكود، وتسليم "
            "أنظمة قابلة للتوسّع.",
        ),
        (
            "مطوّر واجهات أمامية — Tygo.sa",
            "تطوير واجهات منصة لمقارنة شرائح SIM / eSIM تغطي أكثر من 250 باقة في السعودية.",
        ),
        (
            "مطوّر واجهات أمامية — Senaei (وزارة الصناعة، السعودية)",
            "بناء واجهات Angular لتبسيط مساطر التراخيص الصناعية والامتثال بالنسبة للمستثمرين.",
        ),
        (
            "مدير مشروع — Derwork",
            "قيادة تسليم منصة توظيف بـ Next.js تضم إعلانات الوظائف وتقييمات الشركات ولوحات "
            "التحكّم، مع إدارة فرق متعددة التخصصات.",
        ),
        (
            "مطوّر تطبيقات — Edoc",
            "تصميم وتطوير 8 تطبيقات تعليمية لتعلّم لغات البرمجة عبر الدروس والاختبارات.",
        ),
        (
            "مطوّر تطبيقات وويب — Havatar",
            "بناء منصة توصيل متكاملة (على غرار Glovo) للزبناء والسائقين والتجّار بشكل مستقل.",
        ),
        (
            "مطوّر PrestaShop — Lalic",
            "تطوير وتخصيص متاجر إلكترونية بالقوالب والوحدات وتكاملات الدفع.",
        ),
        (
            "مطوّر واجهات أمامية ومصمّم — fekrasystems",
            "تسليم أكثر من 10 أنظمة إدارة بـ Angular بواجهات متجاوبة وسهلة الاستخدام.",
        ),
        (
            "مطوّر واجهات WordPress — lgaming.ma",
            "بداية المسار المهني ببناء مواقع WordPress متجاوبة وتصاميم واجهات أمامية.",
        ),
    ],
}

LANGS = [EN, FR, AR]

CSS = """
@page { size: A4; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 210mm; }
body {
  font-family: %(font)s;
  color: #262138;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
  background: #e9e9ef;
}
.page {
  position: relative;
  width: 210mm; height: 297mm;
  background: #fff;
  display: grid;
  grid-template-columns: 72mm 1fr;
  overflow: hidden;
  margin: 0 auto;
}
/* sidebar */
.side { background: #262138; color: #fff; padding: 9mm 8mm; }
.avatar {
  width: 30mm; height: 30mm; border-radius: 50%%;
  margin: 1mm auto 7mm; display: block;
  object-fit: cover; border: 0.9mm solid rgba(255,255,255,.14);
  background: #16a34a;
}
.side h2, .main h2 {
  font-size: 8.4pt; font-weight: 800; letter-spacing: .12em;
  text-transform: uppercase;
}
.side h2 { color: #fff; }
.side h2::after, .main h2::after {
  content: ""; display: block; width: 9mm; height: 0.8mm;
  background: #16a34a; margin-top: 1.6mm;
}
.side section { margin-bottom: 6.4mm; }
.side section:last-child { margin-bottom: 0; }
.side ul { list-style: none; margin-top: 3.4mm; }
.side li { margin-bottom: 2.9mm; }
.side li:last-child { margin-bottom: 0; }
.lbl {
  font-size: 6.2pt; font-weight: 700; letter-spacing: .1em;
  text-transform: uppercase; color: #16a34a; margin-bottom: 0.5mm;
}
.val { font-size: 8pt; font-weight: 400; color: #e6e5ee; line-height: 1.32; word-break: break-word; }
.side .edu-school { font-size: 8.6pt; font-weight: 700; color: #fff; }
.side .edu-degree { font-size: 7.6pt; color: #c9c7d6; line-height: 1.3; margin-top: 0.3mm; }
.side .edu-years { font-size: 7pt; font-weight: 600; color: #16a34a; margin-top: 0.5mm; }
.side .lang { font-size: 8pt; color: #e6e5ee; margin-bottom: 1.9mm; }

/* main column */
.main { padding: 9mm 9mm 7mm; display: flex; flex-direction: column; }
.name {
  font-size: 21pt; font-weight: 800; letter-spacing: -.01em;
  line-height: 1.06; color: #262138;
}
.role {
  font-size: 9.6pt; font-weight: 700; letter-spacing: .16em;
  text-transform: uppercase; color: #16a34a; margin-top: 2.4mm;
}
.main section { margin-top: 6mm; }
.main h2 { color: #262138; }
.profile { font-size: 8.4pt; line-height: 1.5; color: #4a4560; margin-top: 3.4mm; }
.xp { margin-top: 3.4mm; }
.job { margin-bottom: 3.5mm; }
.job:last-child { margin-bottom: 0; }
.job-role { font-size: 9pt; font-weight: 700; color: #262138; line-height: 1.25; }
.job-meta { font-size: 7.4pt; font-weight: 600; color: #16a34a; margin-top: 0.4mm; }
.job-desc { font-size: 8pt; line-height: 1.42; color: #4a4560; margin-top: 0.7mm; }

/* Arabic: mirror the layout and keep latin runs (dates, tech, urls) LTR */
body[dir="rtl"] .page { grid-template-columns: 1fr 72mm; }
body[dir="rtl"] .side { order: 2; }
body[dir="rtl"] .main { order: 1; }
body[dir="rtl"] .name { letter-spacing: 0; line-height: 1.3; }
body[dir="rtl"] .role { letter-spacing: .02em; }
body[dir="rtl"] .lbl { letter-spacing: 0; }
.ltr { direction: ltr; unicode-bidi: isolate; display: inline-block; }
body[dir="rtl"] .val.ltr, body[dir="rtl"] .job-meta .ltr { text-align: right; }
/* Cairo sits taller than Inter, so the sidebar needs a tighter rhythm to
   keep all four blocks on the single sheet */
body[dir="rtl"] .side { padding: 7mm 8mm; }
body[dir="rtl"] .avatar { width: 24mm; height: 24mm; margin-bottom: 4mm; }
body[dir="rtl"] .side section { margin-bottom: 3.8mm; }
body[dir="rtl"] .side ul { margin-top: 2.6mm; }
body[dir="rtl"] .side li { margin-bottom: 1.7mm; }
body[dir="rtl"] .val { font-size: 7.6pt; line-height: 1.25; }
body[dir="rtl"] .lbl { font-size: 6.6pt; margin-bottom: 0.2mm; }
body[dir="rtl"] .edu-school { font-size: 8.2pt; }
body[dir="rtl"] .edu-degree { font-size: 7.2pt; }
body[dir="rtl"] .lang { font-size: 7.8pt; margin-bottom: 1.3mm; }

@media screen { body { padding: 10mm 0; } .page { box-shadow: 0 2mm 8mm rgba(0,0,0,.18); } }
"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def render(lang):
    rtl = lang["dir"] == "rtl"
    h = lang["headings"]

    contact_items = "\n".join(
        '      <li><div class="lbl">%s</div><div class="val ltr">%s</div></li>'
        % (esc(label), esc(value))
        for label, (_, value) in zip(lang["contact_labels"], CONTACT)
    )
    skill_items = "\n".join(
        '      <li><div class="lbl" style="color:#fff;font-size:7.4pt">%s</div>'
        '<div class="val">%s</div></li>' % (esc(label), esc(value))
        for label, value in zip(lang["skill_labels"], SKILL_VALUES)
    )
    edu_items = "\n".join(
        '      <li><div class="edu-school ltr">%s</div><div class="edu-degree">%s</div>'
        '<div class="edu-years ltr">%s</div></li>' % (esc(school), esc(degree), esc(years))
        for (school, degree), years in zip(lang["education"], EDUCATION_YEARS)
    )
    lang_items = "\n".join(
        '      <div class="lang">%s</div>' % esc(item) for item in lang["languages"]
    )
    jobs = "\n".join(
        '        <div class="job"><div class="job-role">%s</div>'
        '<div class="job-meta"><span class="ltr">%s</span></div>'
        '<div class="job-desc">%s</div></div>' % (esc(role), esc(meta), esc(desc))
        for (role, desc), meta in zip(lang["experience"], EXPERIENCE_META)
    )

    return """<!DOCTYPE html>
<html lang="%(code)s" dir="%(dir)s">
<head>
<meta charset="utf-8" />
<title>%(name)s — CV (%(code_up)s)</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet" />
<style>%(css)s</style>
</head>
<body dir="%(dir)s">
<div class="page">
  <aside class="side">
    <img class="avatar" src="../img/cv/avatar.png" alt="" />
    <section>
      <h2>%(h_contact)s</h2>
      <ul>
%(contact)s
      </ul>
    </section>
    <section>
      <h2>%(h_skills)s</h2>
      <ul>
%(skills)s
      </ul>
    </section>
    <section>
      <h2>%(h_education)s</h2>
      <ul>
%(education)s
      </ul>
    </section>
    <section>
      <h2>%(h_languages)s</h2>
      <div style="margin-top:3.4mm">
%(languages)s
      </div>
    </section>
  </aside>
  <main class="main">
    <div class="name">%(name)s</div>
    <div class="role">%(role)s</div>
    <section>
      <h2>%(h_profile)s</h2>
      <p class="profile">%(profile)s</p>
    </section>
    <section>
      <h2>%(h_experience)s</h2>
      <div class="xp">
%(jobs)s
      </div>
    </section>
  </main>
</div>
</body>
</html>
""" % {
        "code": lang["code"],
        "code_up": lang["code"].upper(),
        "dir": lang["dir"],
        "css": CSS % {"font": lang["font"]},
        "name": esc(lang["name"]),
        "role": esc(lang["role"]),
        "h_contact": esc(h["contact"]),
        "h_skills": esc(h["skills"]),
        "h_education": esc(h["education"]),
        "h_languages": esc(h["languages"]),
        "h_profile": esc(h["profile"]),
        "h_experience": esc(h["experience"]),
        "contact": contact_items,
        "skills": skill_items,
        "education": edu_items,
        "languages": lang_items,
        "profile": esc(lang["profile"]),
        "jobs": jobs,
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for lang in LANGS:
        path = os.path.join(OUT_DIR, "cv-%s.html" % lang["code"])
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(lang))
        print("wrote", path)


if __name__ == "__main__":
    main()
