#!/usr/bin/env python3
"""Static-site generator for swapnilkumar.com — writes plain HTML files."""
import math, os, random

OUT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "Swapnil Kumar"
EMAIL = "swapnil.kumar22@alumni.imperial.ac.uk"
PHONE = "07543 756454"
GITHUB = "https://github.com/SwapnilMurat"
SCHOLAR = "https://scholar.google.com/citations?user=IYPVDYUAAAAJ&hl=en"

NAV = [
    ("index.html", "Home"),
    ("research.html", "Research"),
    ("ventures.html", "Ventures &amp; Innovation"),
    ("publications.html", "Publications"),
    ("news.html", "News"),
    ("contact.html", "Contact"),
]

# --------------------------------------------------------------------------
# generative SVG artwork (deterministic, no external assets)
# --------------------------------------------------------------------------

def art_flowfield(seed=1):
    rnd = random.Random(seed)
    paths = []
    for i in range(26):
        y = 20 + i * 15
        amp = 26 + rnd.random() * 34
        ph = rnd.random() * 6.28
        pts = []
        for x in range(0, 801, 20):
            yy = y + math.sin(x / 130 + ph) * amp * (0.35 + 0.65 * math.sin(x / 800 * math.pi))
            pts.append(f"{x},{yy:.1f}")
        op = 0.10 + 0.55 * (1 - abs(i - 13) / 14)
        col = "#e8873b" if 9 < i < 17 else "#7fb2a1"
        paths.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="1.1" opacity="{op:.2f}"/>')
    return f'''<svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Abstract flow-field illustration">
<rect width="800" height="420" fill="#12161d"/>{"".join(paths)}
<rect width="800" height="420" fill="url(#ff{seed})"/>
<defs><linearGradient id="ff{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0c10" stop-opacity="0.35"/><stop offset="1" stop-color="#0a0c10" stop-opacity="0.75"/></linearGradient></defs></svg>'''


def art_graph(seed=2):
    rnd = random.Random(seed)
    nodes = [(rnd.uniform(60, 740), rnd.uniform(50, 370)) for _ in range(30)]
    edges = []
    for i, (x1, y1) in enumerate(nodes):
        d = sorted(range(len(nodes)), key=lambda j: (nodes[j][0]-x1)**2 + (nodes[j][1]-y1)**2)[1:4]
        for j in d:
            if i < j:
                edges.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{nodes[j][0]:.0f}" y2="{nodes[j][1]:.0f}" stroke="#7fb2a1" stroke-width="0.8" opacity="0.30"/>')
    dots = []
    for i, (x, y) in enumerate(nodes):
        r = 2.4 + (i % 5)
        col = "#e8873b" if i % 4 == 0 else "#f4f1ea"
        op = 0.85 if i % 4 == 0 else 0.42
        dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{col}" opacity="{op}"/>')
    return f'''<svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Abstract knowledge-graph illustration">
<rect width="800" height="420" fill="#12161d"/>{"".join(edges)}{"".join(dots)}</svg>'''


def art_mesh(seed=3):
    lines = []
    for i in range(15):
        t = i / 14
        y = 420 - (1 - t) ** 2 * 340
        lines.append(f'<line x1="0" y1="{y:.0f}" x2="800" y2="{y:.0f}" stroke="#e8873b" stroke-width="0.7" opacity="{0.08 + t*0.30:.2f}"/>')
    for i in range(23):
        x = i * 800 / 22
        lines.append(f'<line x1="400" y1="80" x2="{x:.0f}" y2="420" stroke="#7fb2a1" stroke-width="0.7" opacity="0.16"/>')
    return f'''<svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Abstract perspective-mesh illustration">
<rect width="800" height="420" fill="#0e1116"/>{"".join(lines)}
<circle cx="400" cy="80" r="120" fill="url(#mg)"/>
<defs><radialGradient id="mg"><stop offset="0" stop-color="#e8873b" stop-opacity="0.35"/><stop offset="1" stop-color="#e8873b" stop-opacity="0"/></radialGradient></defs></svg>'''


def art_spectrum(seed=4):
    rnd = random.Random(seed)
    bars = []
    n = 54
    for i in range(n):
        h = 30 + abs(math.sin(i / 5.5)) * 250 * (0.4 + rnd.random() * 0.6)
        x = i * (800 / n)
        col = "#e8873b" if abs(i - n/2) < 12 else "#3a4453"
        bars.append(f'<rect x="{x:.1f}" y="{420-h:.0f}" width="{800/n - 4:.1f}" height="{h:.0f}" rx="2" fill="{col}" opacity="0.75"/>')
    return f'''<svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Abstract spectrum illustration">
<rect width="800" height="420" fill="#12161d"/>{"".join(bars)}</svg>'''


def art_rings(seed=5):
    rings = []
    for i in range(18):
        r = 24 + i * 22
        op = 0.5 - i * 0.024
        col = "#e8873b" if i % 3 == 0 else "#7fb2a1"
        rings.append(f'<circle cx="400" cy="210" r="{r}" fill="none" stroke="{col}" stroke-width="0.9" opacity="{max(op,0.05):.2f}" stroke-dasharray="{4 + i*3} {6 + i}"/>')
    return f'''<svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Abstract concentric-ring illustration">
<rect width="800" height="420" fill="#12161d"/>{"".join(rings)}</svg>'''


def art_portrait(seed=6, label=""):
    rnd = random.Random(seed)
    marks = []
    for i in range(40):
        x = rnd.uniform(0, 600); y = rnd.uniform(0, 800)
        w = rnd.uniform(20, 150)
        marks.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="1" fill="#f4f1ea" opacity="{rnd.uniform(0.03,0.13):.2f}"/>')
    return f'''<svg viewBox="0 0 600 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Photo placeholder">
<rect width="600" height="800" fill="#12161d"/>
<circle cx="300" cy="300" r="170" fill="url(#pg{seed})"/>
<path d="M300 470 C170 470 110 570 100 800 L500 800 C490 570 430 470 300 470 Z" fill="#1a1f28"/>
<circle cx="300" cy="300" r="115" fill="#1a1f28"/>
{"".join(marks)}
<defs><radialGradient id="pg{seed}"><stop offset="0" stop-color="#e8873b" stop-opacity="0.28"/><stop offset="1" stop-color="#e8873b" stop-opacity="0"/></radialGradient></defs></svg>'''


ART = {
    "flow": art_flowfield, "graph": art_graph, "mesh": art_mesh,
    "spectrum": art_spectrum, "rings": art_rings, "portrait": art_portrait,
}

def art(kind, cls="", cap="", seed=None):
    fn = ART[kind]
    svg = fn(seed) if seed is not None else fn()
    capel = f'<span class="art__cap">{cap}</span>' if cap else ""
    return f'<figure class="art {cls}">{svg}{capel}</figure>'


ARROW = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M1 7h11M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# --------------------------------------------------------------------------
# shell
# --------------------------------------------------------------------------

def header(active):
    links = ""
    for href, label in NAV[:-1]:
        cur = ' aria-current="page"' if href == active else ""
        links += f'<a href="{href}"{cur}>{label}</a>'
    cur = ' aria-current="page"' if active == "contact.html" else ""
    links += f'<a class="btn btn--primary" href="contact.html"{cur}>Get in touch {ARROW}</a>'
    return f'''<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html"><span class="dot"></span>Swapnil&nbsp;Kumar</a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><span></span></button>
    <nav class="nav-links">{links}</nav>
  </div>
</header>'''


def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <p class="h3" style="font-family:var(--serif);font-weight:400;font-size:1.7rem;">Let's build something<br>worth shipping.</p>
        <p class="body" style="margin-top:14px;max-width:34ch;font-size:0.95rem;">AI/ML engineering, applied research, and technical leadership — London, UK.</p>
        <a class="btn btn--ghost" style="margin-top:22px;" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <div>
        <p class="footer-h">Navigate</p>
        <ul class="footer-links">
          {"".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)}
        </ul>
      </div>
      <div>
        <p class="footer-h">Elsewhere</p>
        <ul class="footer-links">
          <li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
          <li><a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a></li>
          <li><a href="https://arxiv.org/abs/2503.08408" target="_blank" rel="noopener">arXiv</a></li>
          <li><a href="mailto:{EMAIL}">Email</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Swapnil Kumar. All rights reserved.</span>
      <span>London, United Kingdom</span>
    </div>
  </div>
</footer>'''


def page(filename, title, description, body, active=None):
    active = active or filename
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Swapnil Kumar">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='%230a0c10'/><circle cx='16' cy='16' r='6' fill='%23e8873b'/></svg>">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{footer()}
<script src="assets/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


def cta_band(heading, text, label="Get in touch", href="contact.html"):
    return f'''<section class="section section--tight"><div class="wrap">
  <div class="cta-band" data-reveal>
    <div>
      <h2 class="h2">{heading}</h2>
      <p class="lede" style="margin-top:14px;">{text}</p>
    </div>
    <a class="btn btn--primary" href="{href}">{label} {ARROW}</a>
  </div>
</div></section>'''


def page_hero(eyebrow, heading, lede, artkind="flow", seed=11):
    return f'''<section class="hero">
  <div class="hero__glow"></div><div class="hero__grid"></div>
  <div class="wrap">
    <p class="eyebrow" data-reveal>{eyebrow}</p>
    <h1 class="display" style="margin-top:20px;max-width:16ch;" data-reveal data-reveal-delay="80">{heading}</h1>
    <p class="lede" style="margin-top:26px;" data-reveal data-reveal-delay="160">{lede}</p>
  </div>
  <div class="wrap" style="margin-top:clamp(40px,6vw,72px);" data-reveal data-reveal-delay="240">
    {art(artkind, "art--wide", seed=seed)}
  </div>
</section>'''

# --------------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------------

home = f'''
<section class="hero">
  <div class="hero__glow"></div><div class="hero__grid"></div>
  <div class="wrap">
    <p class="eyebrow" data-reveal>AI/ML Engineer · Researcher · Director</p>
    <h1 class="display" style="margin-top:22px;" data-reveal data-reveal-delay="80">
      Engineering<br><em>Intelligence</em>
    </h1>
    <p class="lede" style="margin-top:28px;font-size:clamp(1.15rem,1.8vw,1.5rem);color:var(--bone);" data-reveal data-reveal-delay="140">
      From research to production.
    </p>
    <p class="lede" style="margin-top:20px;" data-reveal data-reveal-delay="200">
      I build production AI systems and the research that underpins them — LLM and RAG
      applications, semantic retrieval, knowledge graphs, physics-informed models and
      uncertainty quantification — across industry, healthcare and academia.
    </p>
    <div class="hero__cta" data-reveal data-reveal-delay="260">
      <a class="btn btn--primary" href="research.html">Explore the research {ARROW}</a>
      <a class="btn btn--ghost" href="ventures.html">Ventures &amp; innovation</a>
    </div>
    <div class="hero__meta" data-reveal data-reveal-delay="320">
      <span>Imperial College London</span><span>Harvard Medical School</span>
      <span>Stanford</span><span>ETH Zürich</span><span>MIT SPR</span><span>Oxford</span>
    </div>
  </div>
  <div class="wrap" style="margin-top:clamp(46px,6vw,84px);" data-reveal data-reveal-delay="200">
    {art("flow", "art--wide", "Multi-fidelity flow field · Nektar++", seed=7)}
  </div>
</section>

<hr class="rule">

<section class="section">
  <div class="wrap split">
    <div data-reveal>
      <p class="eyebrow">About</p>
      <h2 class="h2" style="margin-top:18px;">Bridging rigorous<br>research and shipped<br>software.</h2>
    </div>
    <div data-reveal data-reveal-delay="120">
      <p class="lede">
        I'm <strong style="color:var(--bone)">Swapnil Kumar</strong>, an AI/ML engineer based in London.
        I've delivered production AI systems and machine-learning research across industry and
        academia — building LLM and RAG applications, semantic vector search, knowledge graphs,
        educational platforms and cloud automation, and leading a ten-person cross-functional team.
      </p>
      <p class="body" style="margin-top:22px;">
        My work runs from <strong>uncertainty quantification for multi-fidelity simulation</strong> at
        Imperial College London, to <strong>coaxial microfluidic bioprinting</strong> at Harvard Medical
        School, to <strong>physics-informed and generative machine learning</strong> at Stanford, to
        <strong>generative AI and public policy</strong> as Technology Director at the MIT Science Policy
        Review. Today I direct AI strategy and product architecture at XLAB Innovations.
      </p>
      <p class="body" style="margin-top:22px;">
        The common thread: taking hard technical problems — high-dimensional uncertainty, regulatory
        complexity, patient-specific modelling — and turning them into systems people can actually use,
        with evaluation, governance and traceability built in from the start.
      </p>
      <div class="card__tags" style="margin-top:26px;">
        <span class="tag">PyTorch</span><span class="tag">LLM / RAG</span><span class="tag">Knowledge graphs</span>
        <span class="tag">PINNs</span><span class="tag">Bayesian optimisation</span><span class="tag">React 18</span>
        <span class="tag">Supabase</span><span class="tag">AWS / GCP / Azure</span><span class="tag">HPC · MPI</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Impact in action</p>
    <h2 class="h2" style="margin-top:18px;max-width:18ch;" data-reveal data-reveal-delay="80">Measured in systems shipped and people taught.</h2>
    <div class="stats" style="margin-top:clamp(30px,4vw,50px);" data-reveal data-reveal-delay="140">
      <div class="stat">
        <p class="stat__figure"><span data-count="20" data-suffix="+">20+</span></p>
        <p class="stat__label">Projects delivered</p>
        <p class="stat__note">Manufacturing and machine-learning projects delivered to plan against agreed KPIs.</p>
      </div>
      <div class="stat">
        <p class="stat__figure"><span data-count="10" data-suffix="">10</span></p>
        <p class="stat__label">Engineers led</p>
        <p class="stat__note">Cross-functional team of AI, data and geospatial engineers taken to delivery.</p>
      </div>
      <div class="stat">
        <p class="stat__figure"><span data-count="1" data-suffix="M+">1M+</span></p>
        <p class="stat__label">Records handled</p>
        <p class="stat__note">Large-scale structured and unstructured datasets in production pipelines.</p>
      </div>
      <div class="stat">
        <p class="stat__figure"><span data-count="6" data-suffix="">6</span></p>
        <p class="stat__label">Research institutions</p>
        <p class="stat__note">Imperial, Harvard Medical School, Stanford, ETH Zürich, Oxford, MIT SPR.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div data-reveal>
        {art("graph", "", "Semantic retrieval · knowledge graph", seed=12)}
        <p class="eyebrow" style="margin-top:28px;">Research</p>
        <h3 class="h2" style="font-size:clamp(1.6rem,2.6vw,2.2rem);margin-top:14px;">Advancing the methods</h3>
        <p class="body" style="margin-top:14px;">
          Uncertainty quantification, multi-fidelity deep neural networks, physics-informed
          learning, quantum machine learning, reinforcement learning and control,
          microfluidic bioprinting, and spatiotemporal modelling — published across
          Imperial, Harvard, Stanford and Princeton communities.
        </p>
        <a class="btn btn--ghost" style="margin-top:24px;" href="research.html">See the research {ARROW}</a>
      </div>
      <div data-reveal data-reveal-delay="120">
        {art("mesh", "", "Product architecture", seed=13)}
        <p class="eyebrow" style="margin-top:28px;">Innovation</p>
        <h3 class="h2" style="font-size:clamp(1.6rem,2.6vw,2.2rem);margin-top:14px;">Turning it into product</h3>
        <p class="body" style="margin-top:14px;">
          AI-assisted organ printing, regulatory intelligence with full auditability,
          two production education platforms serving personalised revision and automated
          marking, and unified multi-LLM data platforms — architected, built and deployed.
        </p>
        <a class="btn btn--ghost" style="margin-top:24px;" href="ventures.html">See the ventures {ARROW}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Focus areas</p>
    <h2 class="h2" style="margin-top:18px;max-width:16ch;" data-reveal data-reveal-delay="80">Where I spend my time.</h2>
    <div class="grid grid--3" style="margin-top:clamp(30px,4vw,50px);">
      <article class="card" data-reveal>
        <p class="card__num">01</p>
        <h3 class="h3">Applied LLM systems</h3>
        <p>RAG pipelines, agentic workflows, semantic vector search and multi-model gateways — built with evaluation frameworks and citation-backed answers rather than demos.</p>
        <div class="card__tags"><span class="tag">RAG</span><span class="tag">Agents</span><span class="tag">Vector DB</span></div>
      </article>
      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">02</p>
        <h3 class="h3">Scientific machine learning</h3>
        <p>Physics-informed neural networks, surrogate modelling, Bayesian optimisation and multi-fidelity data fusion for problems where high-fidelity simulation is too expensive to brute-force.</p>
        <div class="card__tags"><span class="tag">PINNs</span><span class="tag">Co-Kriging</span><span class="tag">UQ</span></div>
      </article>
      <article class="card" data-reveal data-reveal-delay="160">
        <p class="card__num">03</p>
        <h3 class="h3">Knowledge &amp; governance</h3>
        <p>Knowledge graphs that map obligations and dependencies, change-impact assessment, and end-to-end traceability linking every interpretation back to its source document.</p>
        <div class="card__tags"><span class="tag">Graphs</span><span class="tag">Auditability</span><span class="tag">AI ethics</span></div>
      </article>
      <article class="card" data-reveal>
        <p class="card__num">04</p>
        <h3 class="h3">Biomedical engineering</h3>
        <p>Coaxial microfluidic bioprinting, patient-specific design for additive manufacturing, finite-element and thermo-mechanical simulation for surgical and implant applications.</p>
        <div class="card__tags"><span class="tag">Bioprinting</span><span class="tag">FEM</span><span class="tag">DfAM</span></div>
      </article>
      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">05</p>
        <h3 class="h3">Robotics &amp; control</h3>
        <p>Model predictive control, reinforcement learning and trajectory optimisation — from torque-vectoring miniature vehicles at ETH Zürich to connected-vehicle stability at Bosch R&amp;D.</p>
        <div class="card__tags"><span class="tag">MPC</span><span class="tag">RL</span><span class="tag">Trajectory opt.</span></div>
      </article>
      <article class="card" data-reveal data-reveal-delay="160">
        <p class="card__num">06</p>
        <h3 class="h3">Teaching &amp; mentorship</h3>
        <p>Graduate teaching at Imperial College London and the University of Oxford across machine learning, generative AI, optimisation, representation learning and AI alignment.</p>
        <div class="card__tags"><span class="tag">Oxford</span><span class="tag">Imperial</span><span class="tag">GenAI</span></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Trajectory</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">A short history.</h2>
    <div class="timeline" style="margin-top:clamp(28px,3.5vw,44px);" data-reveal data-reveal-delay="140">
      <div class="tl-item">
        <p class="tl-date">2025 — Present</p>
        <div><p class="tl-role">Director</p><p class="tl-org">XLAB Innovations Ltd</p></div>
        <p class="tl-desc">Product and technical strategy for AI-assisted organ printing; regulatory intelligence platform with semantic retrieval, knowledge graphs and full auditability.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">Feb — Jun 2026</p>
        <div><p class="tl-role">Full-Stack / AI Engineer</p><p class="tl-org">A-Team Academy</p></div>
        <p class="tl-desc">Built EconRev and Predicted Papers — two production education platforms with personalised revision, automated marking, diagram verification and grade estimation.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">2024 — 2026</p>
        <div><p class="tl-role">Technology Director</p><p class="tl-org">MIT Science Policy Review</p></div>
        <p class="tl-desc">Generative AI at the intersection of evidence synthesis and public policy; published research on equitable and ethical data and AI governance for LLMs.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">2024</p>
        <div><p class="tl-role">Machine Learning Specialist</p><p class="tl-org">Stanford University</p></div>
        <p class="tl-desc">Physics-informed and generative ML workflows for physical science and environmental applications on Stanford HPC and Google Cloud TPUs.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">2022 — 2024</p>
        <div><p class="tl-role">Project Trainee &amp; Research Collaborator</p><p class="tl-org">Harvard Medical School</p></div>
        <p class="tl-desc">Optimised coaxial microfluidic bioprinting flow conditions, improving structural stability by approximately 30%.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">2022 — 2024</p>
        <div><p class="tl-role">Researcher &amp; Graduate Teaching Assistant</p><p class="tl-org">Imperial College London</p></div>
        <p class="tl-desc">Multi-fidelity deep neural networks for uncertainty propagation; taught machine learning, digital health, optimisation and generative AI.</p>
      </div>
    </div>
    <a class="btn btn--ghost" style="margin-top:30px;" href="ventures.html" data-reveal>Full experience {ARROW}</a>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Life outside work</p>
    <h2 class="h2" style="margin-top:18px;max-width:20ch;" data-reveal data-reveal-delay="80">Cities, mountains, and long conversations.</h2>
    <p class="body" style="margin-top:16px;max-width:56ch;" data-reveal data-reveal-delay="120">
      Between London, Zurich and Boston — cycling, running, and the occasional attempt at
      photography. Replace these four placeholders with your own photographs.
    </p>
    <div class="gallery" style="margin-top:clamp(28px,3.5vw,44px);" data-reveal data-reveal-delay="160">
      {art("portrait", "", "Photo 01", seed=21)}
      {art("portrait", "", "Photo 02", seed=22)}
      {art("portrait", "", "Photo 03", seed=23)}
      {art("portrait", "", "Photo 04", seed=24)}
    </div>
  </div>
</section>

{cta_band("Let's talk.", "Open to research collaborations, technical advisory, and building AI products that hold up in production.")}
'''

# --------------------------------------------------------------------------
# RESEARCH
# --------------------------------------------------------------------------

research = page_hero(
    "Research",
    "Pushing the frontier of applied intelligence",
    "Uncertainty quantification, physics-informed learning, quantum machine learning, "
    "microfluidic bioprinting, reinforcement learning and control — work that connects "
    "fundamental method development to problems in healthcare, engineering and policy.",
    "flow", seed=31,
) + f'''
<hr class="rule">

<section class="section">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Key research areas</p>
    <h2 class="h2" style="margin-top:18px;max-width:18ch;" data-reveal data-reveal-delay="80">Six threads, one method.</h2>
    <div class="grid grid--2" style="margin-top:clamp(30px,4vw,50px);">

      <article class="card" data-reveal>
        <p class="card__num">01 / Uncertainty quantification</p>
        <h3 class="h3">Multi-fidelity simulation without the compute bill</h3>
        <p>
          Combining Nektar++ high- and low-fidelity CFD data with Co-Kriging data fusion, adaptive
          sampling and Bayesian optimisation to predict NACA0012 lift and drag across a 1°–7° angle
          of attack — quantifying uncertainty while minimising the number of expensive HPC samples.
          Multi-fidelity deep neural networks were developed for 1D, 32D and 100D uncertainty-propagation
          benchmarks, outperforming Co-Kriging in high-dimensional settings.
        </p>
        <div class="card__tags"><span class="tag">Nektar++</span><span class="tag">Co-Kriging</span><span class="tag">Adaptive sampling</span><span class="tag">MF-DNN</span></div>
      </article>

      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">02 / Scientific machine learning</p>
        <h3 class="h3">Physics-informed and generative models</h3>
        <p>
          Physics-informed neural network architectures and surrogate models developed at Stanford
          for physical-science and environmental applications, running on Stanford HPC and Google
          Cloud TPUs. Includes Convolutional LSTM and PredRNN work for spatiotemporal modelling,
          published in 2024.
        </p>
        <div class="card__tags"><span class="tag">PINNs</span><span class="tag">ConvLSTM</span><span class="tag">PredRNN</span><span class="tag">TPU</span></div>
      </article>

      <article class="card" data-reveal>
        <p class="card__num">03 / Biofabrication</p>
        <h3 class="h3">Coaxial microfluidic bioprinting</h3>
        <p>
          At Harvard Medical School, optimising coaxial microfluidic flow conditions to produce stable
          single- and multi-walled structures, improving structural stability by roughly 30%. Genetic
          algorithms, uncertainty quantification, finite-element modelling and machine learning applied
          to molecular flow, absorption, blood-flow and multilayer-wrinkling problems.
        </p>
        <div class="card__tags"><span class="tag">Microfluidics</span><span class="tag">FEM</span><span class="tag">Genetic algorithms</span></div>
      </article>

      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">04 / Quantum machine learning</p>
        <h3 class="h3">Uncertainty in QML and fluid mechanics</h3>
        <p>
          Work presented through Princeton University and Imperial College London on quantifying
          uncertainty at the intersection of quantum machine learning and fluid mechanics — extending
          classical UQ methodology into quantum-native model families.
        </p>
        <div class="card__tags"><span class="tag">QML</span><span class="tag">Fluid mechanics</span><span class="tag">Princeton</span></div>
      </article>

      <article class="card" data-reveal>
        <p class="card__num">05 / Robotics, control &amp; RL</p>
        <h3 class="h3">Model predictive control and trajectory optimisation</h3>
        <p>
          At ETH Zürich: design evaluation and performance optimisation of an all-wheel-drive miniature
          vehicle capable of torque vectoring, with model predictive control, reinforcement learning and
          trajectory optimisation. Control-systems lead for Swissloop Tunnelling. Earlier work at Bosch
          R&amp;D on linear and nonlinear stability in connected-vehicle systems.
        </p>
        <div class="card__tags"><span class="tag">MPC</span><span class="tag">RL</span><span class="tag">Swissloop</span></div>
      </article>

      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">06 / AI governance</p>
        <h3 class="h3">Equitable and ethical AI for policy</h3>
        <p>
          As Technology Director at the MIT Science Policy Review: LLM workflows for evidence synthesis
          and editorial decision-making, plus published research on equitable, ethical and fair data and
          AI governance for large language models.
        </p>
        <div class="card__tags"><span class="tag">AI policy</span><span class="tag">Evidence synthesis</span><span class="tag">Governance</span></div>
      </article>

    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap split--even split">
    <div data-reveal>{art("spectrum", "art--wide", "Multi-fidelity error spectrum", seed=32)}</div>
    <div data-reveal data-reveal-delay="120">
      <p class="eyebrow">Method</p>
      <h2 class="h2" style="margin-top:18px;">Make the expensive thing cheap, then make it trustworthy.</h2>
      <p class="body" style="margin-top:18px;">
        Most of my research reduces to the same question: how do you get a reliable answer when the
        ground-truth simulation, experiment or annotation is too costly to run at the scale you need?
      </p>
      <p class="body" style="margin-top:16px;">
        The answer is usually a combination — a cheap surrogate that carries physical structure, an
        adaptive sampling strategy that spends the expensive budget where it matters, and an honest
        uncertainty estimate so downstream decisions know what the model doesn't know.
      </p>
      <p class="body" style="margin-top:16px;">
        The same pattern shows up in regulatory AI, where the expensive resource is expert review, and
        in bioprinting, where it's laboratory time.
      </p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Institutions &amp; affiliations</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">Where the work has happened.</h2>
    <ul class="affil" style="margin-top:28px;" data-reveal data-reveal-delay="120">
      <li>Imperial College London</li><li>Harvard Medical School</li><li>Stanford University</li>
      <li>ETH Zürich</li><li>University of Oxford — Mathematical Institute</li>
      <li>MIT Science Policy Review</li><li>Princeton University · PPPL</li>
      <li>University of Louisville</li><li>Grantham Institute</li>
      <li>Neuromatch Academy</li><li>Bühler</li><li>Vellore Institute of Technology &amp; ARAI</li>
    </ul>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Featured</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">Selected publications.</h2>
    <div class="grid grid--3" style="margin-top:clamp(30px,4vw,50px);">
      <article class="card" data-reveal>
        <p class="card__num">2025</p>
        <h3 class="h3">Uncertainty Quantification for Multi-Fidelity Simulations</h3>
        <p>Master's thesis, Imperial College London — multi-fidelity deep neural networks and data fusion for high-dimensional uncertainty propagation.</p>
        <a class="btn btn--ghost" style="margin-top:20px;" href="https://arxiv.org/abs/2503.08408" target="_blank" rel="noopener">arXiv {ARROW}</a>
      </article>
      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">2024</p>
        <h3 class="h3">Microfluidics for Co-axial Bioprinting</h3>
        <p>With Sushila Maharjan, Valerio Luca Mainardi and Y. Shrike Zhang — Harvard Medical School &amp; Imperial College London.</p>
        <a class="btn btn--ghost" style="margin-top:20px;" href="https://spiral.imperial.ac.uk/handle/10044/1/108549" target="_blank" rel="noopener">Spiral {ARROW}</a>
      </article>
      <article class="card" data-reveal data-reveal-delay="160">
        <p class="card__num">2024</p>
        <h3 class="h3">Reinforcement Learning Across Temporal Scales</h3>
        <p>With Leila Wehbe and Patrick Mineault — NeuroAI, Neuromatch Academy.</p>
        <a class="btn btn--ghost" style="margin-top:20px;" href="https://neuroai.neuromatch.io/tutorials/W1D2_ComparingTasks/student/W1D2_Tutorial3.html" target="_blank" rel="noopener">Read {ARROW}</a>
      </article>
    </div>
    <a class="btn btn--ghost" style="margin-top:30px;" href="publications.html" data-reveal>All publications {ARROW}</a>
  </div>
</section>

{cta_band("Collaborate on the research.", "Always interested in problems where uncertainty, physics and machine learning meet.")}
'''

# --------------------------------------------------------------------------
# VENTURES
# --------------------------------------------------------------------------

ventures = page_hero(
    "Ventures &amp; Innovation",
    "Ideas that make it into production",
    "Directing AI strategy for organ printing, building regulatory intelligence with full auditability, "
    "and shipping education platforms used by real students — plus a decade of engineering across "
    "manufacturing, real estate and automotive R&amp;D.",
    "mesh", seed=41,
) + f'''
<hr class="rule">

<section class="section">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Current</p>
    <h2 class="h2" style="margin-top:18px;max-width:20ch;" data-reveal data-reveal-delay="80">Building now.</h2>

    <div class="grid grid--2" style="margin-top:clamp(30px,4vw,50px);align-items:start;">
      <article class="card" data-reveal>
        <p class="card__num">Director · 2025 — Present</p>
        <h3 class="h3">XLAB Innovations Ltd</h3>
        <p>
          Product and technical strategy for <strong>AI-assisted organ printing</strong> — integrating
          microfluidic bioprinting, physics-informed modelling, uncertainty quantification and adaptive
          flow control. Surrogate models and PINN architectures accelerate patient-specific construct
          development, cutting simulation cost and improving experimental decision-making.
        </p>
        <p>
          A second strand builds <strong>regulatory intelligence</strong>: document ingestion pipelines for
          structured rule extraction and classification, scalable semantic retrieval, and knowledge
          graphs mapping obligations, rule dependencies and interconnected requirements. Every answer
          is evidence-backed with citations linked to source documentation, with change-impact
          assessment and end-to-end auditability.
        </p>
        <p>
          Alongside the technology: evaluation frameworks, governance principles and ethical guardrails
          for responsible, explainable deployment — and cross-functional work between product,
          engineering and design.
        </p>
        <div class="card__tags">
          <span class="tag">PINNs</span><span class="tag">Knowledge graphs</span><span class="tag">Semantic retrieval</span>
          <span class="tag">RegTech</span><span class="tag">AI governance</span>
        </div>
      </article>

      <div data-reveal data-reveal-delay="120">
        {art("graph", "art--wide", "Obligation graph · rule dependencies", seed=42)}
        <div class="card" style="margin-top:clamp(18px,2.4vw,30px);">
          <p class="card__num">Feb — Jun 2026</p>
          <h3 class="h3">A-Team Academy</h3>
          <p>
            Two production education platforms — <strong>EconRev</strong> and <strong>Predicted Papers</strong> —
            covering personalised revision, predicted examination papers, automated marking, model answers,
            diagram practice, grade estimation, dashboards, CRM workflows and payments.
          </p>
          <p>
            Front ends in React 18, Vite, TypeScript, Tailwind and shadcn/ui; back end on Supabase with
            PostgreSQL, Auth, Storage, Row-Level Security, Realtime and Edge Functions. Claude and OpenAI
            models integrated through an AI gateway, with RAG, semantic vector search, knowledge graphs
            and computer vision improving syllabus alignment, feedback quality and diagram verification.
          </p>
          <div class="card__tags">
            <span class="tag">React 18</span><span class="tag">Supabase</span><span class="tag">Claude / OpenAI</span>
            <span class="tag">Computer vision</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Selected engagements</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">Previously.</h2>
    <div class="grid grid--3" style="margin-top:clamp(30px,4vw,50px);">

      <article class="card" data-reveal>
        <p class="card__num">Jun — Sep 2025</p>
        <h3 class="h3">Propeterra — AI Engineer</h3>
        <p>
          Unified multiple LLMs into a single AI platform and designed end-to-end pipeline architecture:
          ingestion, model orchestration and automated workflows. Built a Selenium scraping framework,
          automated business-email discovery and outreach with hunter.io, and a custom data-collection
          framework for commercial real estate across Asia and UK council datasets.
        </p>
        <p>
          Time-series and heatmap-based geospatial analytics for market and policy insight; RAG over
          structured and unstructured sources including automated reasoning over PDF repositories.
          Managed GitHub infrastructure and CI/CD, worked with datasets exceeding one million records,
          and led a cross-functional team of ten across AI, data and geospatial engineering.
        </p>
        <div class="card__tags"><span class="tag">LLM platform</span><span class="tag">Geospatial</span><span class="tag">AWS</span><span class="tag">Team lead</span></div>
      </article>

      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">Aug 2020 — Sep 2022</p>
        <h3 class="h3">University of Louisville — Project Engineer</h3>
        <p>
          Design for additive manufacturing, FEM simulation in MATLAB, CFD, thermo-mechanical, process
          and performance simulation with uncertainty quantification. Evaluated thermomechanical
          behaviour of parts fabricated by Laser Powder Bed Fusion.
        </p>
        <p>
          Designed and analysed oral maxillofacial surgical applications and fracture mechanics of the
          tibia from patient CT scans — additive manufacturing for medical treatment of human tibia
          and skull.
        </p>
        <div class="card__tags"><span class="tag">L-PBF</span><span class="tag">FEM</span><span class="tag">CT-driven design</span></div>
      </article>

      <article class="card" data-reveal data-reveal-delay="160">
        <p class="card__num">2020 — 2022</p>
        <h3 class="h3">PQE Group &amp; Robert Bosch R&amp;D</h3>
        <p>
          <strong>PQE Group — Consultant.</strong> Delivered 20 manufacturing and machine-learning
          projects, managed a ten-member team, prepared delivery plans and coordinated with IT
          stakeholders against timelines and KPIs.
        </p>
        <p>
          <strong>Robert Bosch R&amp;D — Project Trainee.</strong> Analysed linear and nonlinear stability
          behaviour in connected-vehicle systems and developed microcontroller logic coordinating
          human-driven and autonomous operation.
        </p>
        <div class="card__tags"><span class="tag">Consulting</span><span class="tag">Connected vehicles</span><span class="tag">Embedded</span></div>
      </article>

    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Teaching &amp; technical leadership</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">Academic appointments.</h2>
    <div class="timeline" style="margin-top:clamp(28px,3.5vw,44px);" data-reveal data-reveal-delay="120">
      <div class="tl-item">
        <p class="tl-date">2024 — 2026</p>
        <div><p class="tl-role">Technology Director</p><p class="tl-org">MIT Science Policy Review · Cambridge, MA</p></div>
        <p class="tl-desc">Generative AI and public policy; LLM workflows for evidence synthesis and editorial process. Published on equitable, ethical and fair data and AI governance for LLMs.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">2025</p>
        <div><p class="tl-role">Graduate Teaching Assistant</p><p class="tl-org">University of Oxford — Machine Learning</p></div>
        <p class="tl-desc">Machine learning, AI, generative AI, ML in health and biology, representation learning, agentic AI, human–AI alignment, foundation and frontier models, DNNs, CNNs, optimisation, clustering and classification.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">Sep — Nov 2024</p>
        <div><p class="tl-role">Machine Learning Specialist</p><p class="tl-org">Stanford University · California</p></div>
        <p class="tl-desc">Physics-informed and generative ML workflows on Stanford HPC and Google Cloud TPUs; ConvLSTM and PredRNN research for spatiotemporal modelling.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">2022 — 2024</p>
        <div><p class="tl-role">Researcher · Graduate Teaching &amp; Research Assistant</p><p class="tl-org">Imperial College London</p></div>
        <p class="tl-desc">Multi-fidelity simulation and uncertainty quantification with Nektar++; taught machine learning, digital health, optimisation, deep learning, clustering, classification and generative AI.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">Mar 2022 — May 2024</p>
        <div><p class="tl-role">Project Trainee &amp; Research Collaborator</p><p class="tl-org">Harvard Medical School · Cambridge, MA</p></div>
        <p class="tl-desc">Coaxial microfluidic bioprinting; genetic algorithms, UQ, FEM and ML applied to molecular flow, absorption, blood flow and multilayer wrinkling.</p>
      </div>
      <div class="tl-item">
        <p class="tl-date">Jul — Sep 2022</p>
        <div><p class="tl-role">Research Fellow</p><p class="tl-org">ETH Zürich · Switzerland</p></div>
        <p class="tl-desc">Design, modelling, model predictive control, reinforcement learning and trajectory optimisation for an all-wheel-drive torque-vectoring miniature vehicle. Control lead, Swissloop Tunnelling.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Education</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">Training.</h2>
    <div class="grid grid--2" style="margin-top:clamp(30px,4vw,50px);">
      <article class="card" data-reveal>
        <p class="card__num">Graduated Sep 2024</p>
        <h3 class="h3">Imperial College London — MSc</h3>
        <p>
          Applied mathematics and machine learning, First-Class, Department of Computing &amp; Business
          School. Thesis: <em>Uncertainty Quantification for Multi-Fidelity Simulations</em>. Research focus
          spanning applied mathematics, scientific computing, machine learning and quantum computing.
        </p>
        <p>
          Staff Recognition for Teaching and Supervision · Application Evaluator, UK Commonwealth Startup
          Fellowship · Grantham Institute affiliate · Imperial President's Award nominee for societal
          engagement · Bühler project on AI-driven microbial growth kinetics with Bayesian hyperparameter
          optimisation.
        </p>
      </article>
      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">Completed Oct 2022</p>
        <h3 class="h3">ETH Zürich — Visiting Graduate Student</h3>
        <p>Robotics, control systems, reinforcement learning and ethics. Design and performance optimisation of a torque-vectoring all-wheel-drive miniature vehicle; control-systems lead for Swissloop Tunnelling.</p>
      </article>
      <article class="card" data-reveal>
        <p class="card__num">Completed Aug 2024</p>
        <h3 class="h3">University of Oxford — Mathematical Institute</h3>
        <p>Representation learning, agentic AI, human–AI alignment, building GenAI products, foundation and large frontier models in applied domains, factorization methods, advanced practical topics in ML, DNNs and optimisation.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="80">
        <p class="card__num">Graduated Sep 2020</p>
        <h3 class="h3">Vellore Institute of Technology &amp; ARAI — BTech</h3>
        <p>
          First Class, 91.3%, Department Rank 3. Second place for Best Research, bachelor's thesis
          (Purdue University). SAE-India Student of the Year 2019–20 and SAE-India Section Award. Best
          Outgoing Student, top 0.04% of 30,000. AWS Technical Essentials and Architecting.
        </p>
      </article>
    </div>
  </div>
</section>

{cta_band("Advisory, contract or collaboration.", "If you're building something at the edge of AI and a hard physical or regulatory domain, I'd like to hear about it.")}
'''

# --------------------------------------------------------------------------
# PUBLICATIONS
# --------------------------------------------------------------------------

PUBS = [
    ("Quantifying Uncertainty in Quantum Machine Learning &amp; Fluid Mechanics",
     "Swapnil Kumar · Princeton University &amp; Imperial College London",
     "2025", "https://gss.pppl.gov/2025/Tuesday_flash.pdf"),
    ("Uncertainty Quantification for Multi-Fidelity Simulations",
     "Swapnil Kumar · MSc thesis, Imperial College London · arXiv:2503.08408",
     "2025", "https://arxiv.org/abs/2503.08408"),
    ("Reinforcement Learning Across Temporal Scales",
     "Leila Wehbe, Swapnil Kumar, Patrick Mineault · NeuroAI, Neuromatch Academy",
     "2024", "https://neuroai.neuromatch.io/tutorials/W1D2_ComparingTasks/student/W1D2_Tutorial3.html"),
    ("Microfluidics for Co-axial Bioprinting",
     "Swapnil Kumar, Sushila Maharjan, Valerio Luca Mainardi, Y. Shrike Zhang · Harvard Medical School &amp; Imperial College London",
     "2024", "https://spiral.imperial.ac.uk/handle/10044/1/108549"),
    ("Coaxial Microfluidic Bioprinting — Spiral record",
     "Imperial College London research repository entry",
     "2024", "https://spiral.imperial.ac.uk/entities/publication/c1f9b71e-13cb-416f-bfdd-8834599d8508"),
    ("Computational Neuroscience: Calculus — Tutorial 2",
     "Neuromatch Academy · Computational Neuroscience curriculum",
     "2024", "https://compneuro.neuromatch.io/tutorials/W0D4_Calculus/student/W0D4_Tutorial2.html"),
    ("Computational Neuroscience: Calculus — Tutorial 3",
     "Neuromatch Academy · Computational Neuroscience curriculum",
     "2024", "https://compneuro.neuromatch.io/tutorials/W0D4_Calculus/student/W0D4_Tutorial3.html"),
    ("Neuro Video Series — Tutorial 3",
     "Neuromatch Academy · Computational Neuroscience curriculum",
     "2024", "https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial3.html"),
    ("Convolutional LSTM and PredRNN for Spatiotemporal Modelling",
     "Stanford University · physics-informed and generative ML for physical science",
     "2024", None),
    ("Equitable, Ethical and Fair Data and AI Governance for Large Language Models",
     "MIT Science Policy Review",
     "2024", None),
]

pub_rows = ""
for i, (title, meta, year, url) in enumerate(PUBS, 1):
    t = f'<a href="{url}" target="_blank" rel="noopener">{title} {ARROW}</a>' if url else title
    pub_rows += f'''<article class="pub" data-reveal>
      <p class="pub__idx">{i:02d}</p>
      <div><p class="pub__title">{t}</p><p class="pub__meta">{meta}</p></div>
      <p class="pub__year">{year}</p>
    </article>'''

publications = page_hero(
    "Publications",
    "Papers, theses and teaching material",
    "Peer-reviewed work, preprints, repository records and open curriculum contributions spanning "
    "uncertainty quantification, bioprinting, reinforcement learning and AI governance.",
    "rings", seed=51,
) + f'''
<hr class="rule">

<section class="section">
  <div class="wrap">
    <div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:flex-end;" data-reveal>
      <div>
        <p class="eyebrow">Full list</p>
        <h2 class="h2" style="margin-top:18px;">Selected publications.</h2>
      </div>
      <a class="btn btn--ghost" href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar {ARROW}</a>
    </div>
    <div class="pub-list" style="margin-top:clamp(28px,3.5vw,44px);">
      {pub_rows}
    </div>
    <p class="form-note" style="margin-top:22px;">
      Citation counts and the complete record are maintained on
      <a href="{SCHOLAR}" target="_blank" rel="noopener" style="color:var(--ember);">Google Scholar</a>.
    </p>
  </div>
</section>

{cta_band("Looking for a preprint?", "Happy to share manuscripts, code or data behind any of the work listed here.")}
'''

# --------------------------------------------------------------------------
# NEWS
# --------------------------------------------------------------------------

NEWS = [
    ("2026", "Named to the Nova 111 UK List",
     "Recognised on the Nova 111 UK List 2026 for contributions to social impact, research and education."),
    ("2026", "EconRev and Predicted Papers go live",
     "Two production education platforms shipped at A-Team Academy, covering personalised revision, automated marking, diagram verification and grade estimation."),
    ("2025", "XLAB Innovations founded",
     "Took on the Director role, setting product and technical strategy for AI-assisted organ printing and regulatory intelligence."),
    ("2025", "Invited talks across the international academic community",
     "Talks delivered across the University of Oxford, University of Cambridge, Imperial College London, Princeton, and Tsinghua / GAUC communities."),
    ("2025", "Quantum machine learning and fluid mechanics presented at Princeton",
     "Work on quantifying uncertainty in quantum machine learning and fluid mechanics presented through Princeton University and Imperial College London."),
    ("2025", "Graduate teaching at the University of Oxford",
     "Joined the University of Oxford as a Graduate Teaching Assistant across machine learning, generative AI, agentic AI and human–AI alignment."),
    ("2025", "Multi-fidelity uncertainty quantification preprint released",
     "The MSc thesis <em>Uncertainty Quantification for Multi-Fidelity Simulations</em> published to arXiv (2503.08408)."),
    ("2024", "Technology Director, MIT Science Policy Review",
     "Appointed to direct technology initiatives at the intersection of generative AI and public policy."),
    ("2024", "Graduated Imperial College London with First-Class honours",
     "MSc in applied mathematics and machine learning, with Staff Recognition for Teaching and Supervision and an Imperial President's Award nomination."),
    ("2024", "Machine Learning Specialist at Stanford University",
     "Physics-informed and generative machine-learning workflows for physical science and environmental applications."),
]

news_rows = ""
for year, title, body in NEWS:
    news_rows += f'''<div class="tl-item" data-reveal>
      <p class="tl-date">{year}</p>
      <div><p class="tl-role">{title}</p></div>
      <p class="tl-desc">{body}</p>
    </div>'''

news = page_hero(
    "News",
    "Recognition, talks and milestones",
    "A running record of appointments, awards, releases and invited talks.",
    "spectrum", seed=61,
) + f'''
<hr class="rule">

<section class="section">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Recent</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">What's been happening.</h2>
    <div class="timeline" style="margin-top:clamp(28px,3.5vw,44px);">
      {news_rows}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Awards &amp; honours</p>
    <h2 class="h2" style="margin-top:18px;" data-reveal data-reveal-delay="80">Selected recognition.</h2>
    <div class="grid grid--3" style="margin-top:clamp(30px,4vw,50px);">
      <article class="card" data-reveal>
        <p class="card__num">2026</p><h3 class="h3">Nova 111 UK List</h3>
        <p>For social impact, research and education.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="60">
        <p class="card__num">2024</p><h3 class="h3">Staff Recognition Award</h3>
        <p>Imperial College London, for teaching and supervision as a Graduate Teaching &amp; Research Assistant.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="120">
        <p class="card__num">2024</p><h3 class="h3">President's Award nominee</h3>
        <p>Imperial College London — societal engagement and supporting student experience.</p>
      </article>
      <article class="card" data-reveal>
        <p class="card__num">2024</p><h3 class="h3">Commonwealth Startup Fellowship</h3>
        <p>Application evaluator, UK Commonwealth Startup Fellowship.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="60">
        <p class="card__num">2020</p><h3 class="h3">SAE-India Student of the Year</h3>
        <p>Awarded across all Indian students, 2019–20, alongside the SAE-India Section Award.</p>
      </article>
      <article class="card" data-reveal data-reveal-delay="120">
        <p class="card__num">2020</p><h3 class="h3">Best Outgoing Student</h3>
        <p>Top 0.04% of 30,000 students; Department Rank 3 and second place for Best Research (Purdue University).</p>
      </article>
    </div>
  </div>
</section>

{cta_band("Speaking or press enquiry?", "Available for invited talks, panels and technical workshops on applied AI, uncertainty and scientific machine learning.")}
'''

# --------------------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------------------

contact = f'''
<section class="hero" style="padding-block:clamp(60px,9vw,120px) clamp(30px,4vw,60px);">
  <div class="hero__glow"></div><div class="hero__grid"></div>
  <div class="wrap">
    <p class="eyebrow" data-reveal>Contact</p>
    <h1 class="display" style="margin-top:20px;max-width:14ch;" data-reveal data-reveal-delay="80">Get in <em>touch</em></h1>
    <p class="lede" style="margin-top:26px;" data-reveal data-reveal-delay="140">
      Research collaborations, technical advisory, speaking, or building something together —
      the fastest route is email, and I read everything.
    </p>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="wrap split">
    <div data-reveal>
      <h2 class="h3" style="font-size:1.2rem;">Direct</h2>
      <div class="contact-list" style="margin-top:20px;">
        <a class="contact-row" href="mailto:{EMAIL}"><span class="k">Email</span><span class="v">{EMAIL}</span></a>
        <a class="contact-row" href="tel:+447543756454"><span class="k">Phone</span><span class="v">{PHONE}</span></a>
        <div class="contact-row"><span class="k">Location</span><span class="v">London, United Kingdom</span></div>
        <a class="contact-row" href="{GITHUB}" target="_blank" rel="noopener"><span class="k">GitHub</span><span class="v">github.com/SwapnilMurat</span></a>
        <a class="contact-row" href="{SCHOLAR}" target="_blank" rel="noopener"><span class="k">Scholar</span><span class="v">Google Scholar profile</span></a>
        <a class="contact-row" href="https://arxiv.org/abs/2503.08408" target="_blank" rel="noopener"><span class="k">arXiv</span><span class="v">2503.08408</span></a>
      </div>
      <p class="form-note" style="margin-top:22px;">
        Add a LinkedIn or X handle here whenever you'd like — the row markup is already in place.
      </p>
    </div>

    <div data-reveal data-reveal-delay="120">
      <div class="card">
        <h2 class="h3">Send a message</h2>
        <p style="margin-top:10px;">Fill this in and it will open a pre-filled email addressed to me.</p>
        <form class="form" style="margin-top:26px;" novalidate>
          <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="organisation">Organisation</label><input id="organisation" name="organisation" type="text" autocomplete="organization"></div>
          <div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
          <div style="display:flex;align-items:center;gap:18px;flex-wrap:wrap;">
            <button class="btn btn--primary" type="submit">Send message {ARROW}</button>
            <span class="form-status" role="status"></span>
          </div>
          <p class="form-note">
            This form uses a mailto handoff so the site can be hosted anywhere with no backend.
            Swap in Formspree, Netlify Forms or a Supabase Edge Function when you want submissions
            stored server-side.
          </p>
        </form>
      </div>
    </div>
  </div>
</section>
'''

# --------------------------------------------------------------------------

page("index.html", "Swapnil Kumar — AI/ML Engineer, Researcher & Director",
     "Swapnil Kumar is an AI/ML engineer in London building production AI systems and applied research across LLMs, uncertainty quantification, physics-informed learning and biofabrication.",
     home)
page("research.html", "Research — Swapnil Kumar",
     "Uncertainty quantification, physics-informed machine learning, quantum ML, microfluidic bioprinting, reinforcement learning and AI governance.",
     research)
page("ventures.html", "Ventures & Innovation — Swapnil Kumar",
     "XLAB Innovations, A-Team Academy, Propeterra and a decade of engineering across manufacturing, real estate and automotive R&D.",
     ventures)
page("publications.html", "Publications — Swapnil Kumar",
     "Papers, preprints, theses and open curriculum contributions by Swapnil Kumar.",
     publications)
page("news.html", "News — Swapnil Kumar",
     "Appointments, awards, releases and invited talks.",
     news)
page("contact.html", "Contact — Swapnil Kumar",
     "Get in touch with Swapnil Kumar for research collaborations, advisory and speaking.",
     contact)
print("done")
