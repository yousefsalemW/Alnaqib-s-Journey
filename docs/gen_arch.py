#!/usr/bin/env python3
"""Generate docs/architecture.svg - hand-laid knowledge map for Alnaqib's Journey."""

W, H = 1560, 1000

PALETTES = {
    "dark": {
        "bg":        "#0B1420",
        "line":      "#B9C8D6", "legend": "#9FB2C2",
        "root_f":    "#101B2D", "root_s": "#C9D6E2", "root_t": "#F4F8FB",
        "domain_f":  "#123A63", "domain_s": "#4FA3E3", "domain_t": "#EAF2FA",
        "track_f":   "#1E4030", "track_s": "#6FBF8B", "track_t": "#E9F6EE",
        "leaf_f":    "#A9B9CC", "leaf_s": "#8496AA", "leaf_t": "#101E2B",
        "tool_f":    "#C9BF9F", "tool_s": "#A99E7C", "tool_t": "#241F12",
    },
    "muted": {
        "bg":        "#4E5D67",
        "line":      "#DCE4EA", "legend": "#DCE4EA",
        "root_f":    "#26333B", "root_s": "#9BB0BD", "root_t": "#F2F6F8",
        "domain_f":  "#2F5B84", "domain_s": "#8FBEE4", "domain_t": "#EDF4FA",
        "track_f":   "#3F6B4E", "track_s": "#9CCFAE", "track_t": "#EDF7F1",
        "leaf_f":    "#B7C5D2", "leaf_s": "#8A9AA8", "leaf_t": "#16232E",
        "tool_f":    "#CFC5A8", "tool_s": "#A79C7E", "tool_t": "#241F12",
    },
}

def build(theme, OUTFILE):
    global C, out
    C = PALETTES[theme]
    out = []


    def box(x, y, w, h, label, kind, bold=False, size=15):
        f, s, t = C[kind + "_f"], C[kind + "_s"], C[kind + "_t"]
        sw = 2 if kind in ("root", "domain", "track") else 1.2
        out.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" '
            f'fill="{f}" stroke="{s}" stroke-width="{sw}"/>'
        )
        lines = label.split("|")
        lh = size + 4
        start = y + h / 2 - (len(lines) - 1) * lh / 2 + size * 0.36
        weight = "700" if bold else "500"
        for i, ln in enumerate(lines):
            out.append(
                f'<text x="{x + w / 2}" y="{start + i * lh}" text-anchor="middle" '
                f'font-size="{size}" font-weight="{weight}" fill="{t}">{ln}</text>'
            )
        return (x, y, w, h)


    def path(d, arrow=True):
        marker = ' marker-end="url(#a)"' if arrow else ""
        out.append(
            f'<path d="{d}" fill="none" stroke="{C["line"]}" stroke-width="1.8" '
            f'stroke-linejoin="round"{marker}/>'
        )


    def cx(b):  return b[0] + b[2] / 2
    def cy(b):  return b[1] + b[3] / 2
    def bot(b): return b[1] + b[3]
    def rt(b):  return b[0] + b[2]


    # ---------------------------------------------------------------- root
    root = box(600, 34, 340, 58, "Alnaqib&#8217;s Journey", "root", bold=True, size=20)

    # ---------------------------------------------------------------- domains
    dl = box(150, 158, 300, 54, "DevOps-Learning", "domain", bold=True, size=17)
    lx = box(838, 158, 214, 54, "Linux", "domain", bold=True, size=17)
    osh = box(1160, 158, 300, 54, "OpenShift", "domain", bold=True, size=17)

    # root -> domains  (bus at y=126)
    path(f"M {cx(root)} {bot(root)} V 126", arrow=False)
    out.append(
        f'<path d="M {cx(dl)} 126 H {cx(osh)}" fill="none" '
        f'stroke="{C["line"]}" stroke-width="1.8"/>'
    )
    for b in (dl, lx, osh):
        path(f"M {cx(b)} 126 V {b[1]}")

    # ---------------------------------------------------------------- tracks
    t1 = box(46, 278, 196, 52, "1-DevOps", "track", bold=True, size=16)
    t2 = box(292, 278, 340, 52, "2-DevOps-Tools-and-Concepts", "track", bold=True, size=15)

    path(f"M {cx(dl)} {bot(dl)} V 248", arrow=False)
    out.append(
        f'<path d="M {cx(t1)} 248 H {cx(t2)}" fill="none" '
        f'stroke="{C["line"]}" stroke-width="1.8"/>'
    )
    for b in (t1, t2):
        path(f"M {cx(b)} 248 V {b[1]}")

    # ---------------------------------------------------------------- the path
    steps = ["Intro", "Linux", "NGINX", "Docker", "Kubernetes", "Helm", "Ansible", "AWS"]
    py, prev = 372, t1
    for name in steps:
        b = box(60, py, 168, 46, name, "leaf", size=15)
        path(f"M {cx(b)} {bot(prev)} V {b[1]}")
        prev, py = b, py + 74

    # ---------------------------------------------------------------- concepts spine
    concepts = [
        ("AWS-Concepts", 378),
        ("Kubernetes-Concepts", 500),
        ("HAProxy", 596),
        ("Observability", 666),
        ("SonarQube + Trivy", 736),
        ("Vault", 806),
        ("Velero", 876),
    ]
    cb = {}
    for name, y in concepts:
        size = 14 if len(name) > 17 else 15
        cb[name] = box(340, y, 210, 44, name, "tool", size=size)

    spine_x = 306
    last = cb["Velero"]
    path(f"M {cx(t2)} {bot(t2)} V 352 H {spine_x} V {cy(last)}", arrow=False)
    for name, _ in concepts:
        b = cb[name]
        path(f"M {spine_x} {cy(b)} H {b[0]}")

    # ---------------------------------------------------------------- AWS children
    aws = cb["AWS-Concepts"]
    aws_kids = [("DynamoDB-Locking", 352), ("RDS+EBS", 410)]
    ax = 596
    path(f"M {rt(aws)} {cy(aws)} H {ax}", arrow=False)
    for name, y in aws_kids:
        b = box(618, y, 196, 42, name, "tool", size=14)
        path(f"M {ax} {cy(aws)} V {cy(b)} H {b[0]}")

    # ---------------------------------------------------------------- k8s children
    k8 = cb["Kubernetes-Concepts"]
    k8_kids = ["Pod-Types", "Container-Types", "Ingress", "Network-Policy", "Kubeadm-vs-EKS"]
    kx = 580
    ky = 480
    kid_boxes = []
    for name in k8_kids:
        b = box(602, ky, 212, 42, name, "tool", size=14)
        kid_boxes.append(b)
        ky += 58
    path(f"M {rt(k8)} {cy(k8)} H {kx}", arrow=False)
    out.append(
        f'<path d="M {kx} {cy(kid_boxes[0])} V {cy(kid_boxes[-1])}" fill="none" '
        f'stroke="{C["line"]}" stroke-width="1.8"/>'
    )
    for b in kid_boxes:
        path(f"M {kx} {cy(b)} H {b[0]}")

    # ---------------------------------------------------------------- Linux
    l1 = box(846, 266, 198, 50, "Linux Admin I", "leaf", size=15)
    l2 = box(846, 348, 198, 50, "Linux Admin II", "leaf", size=15)
    path(f"M {cx(lx)} {bot(lx)} V {l1[1]}")
    path(f"M {cx(l1)} {bot(l1)} V {l2[1]}")

    # ---------------------------------------------------------------- OpenShift
    modules = [
        "1. Intro to OpenShift",
        "2. Authentication &#38; Authorization",
        "3. Install",
        "4. Permission &#38; Role",
        "5. Create Users",
        "6. CLI &#38; GUI",
        "7. Routes",
        "8. Limit Range",
        "9. Project Template",
    ]
    oy, prev = 266, osh
    for name in modules:
        b = box(1168, oy, 284, 50, name, "leaf", size=15)
        path(f"M {cx(b)} {bot(prev)} V {b[1]}")
        prev, oy = b, oy + 76

    # ---------------------------------------------------------------- legend
    lg = [("domain", "top-level directory"), ("track", "learning track"),
          ("leaf", "sequential module"), ("tool", "tool / concept")]
    lx0, ly0 = 60, 962
    for i, (kind, text) in enumerate(lg):
        x = lx0 + i * 250
        out.append(
            f'<rect x="{x}" y="{ly0}" width="22" height="16" rx="4" '
            f'fill="{C[kind + "_f"]}" stroke="{C[kind + "_s"]}" stroke-width="1.2"/>'
        )
        out.append(
            f'<text x="{x + 32}" y="{ly0 + 13}" font-size="14" fill="{C['legend']}">{text}</text>'
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
         font-family="Inter, Segoe UI, Helvetica, Arial, sans-serif">
      <defs>
        <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7"
                orient="auto-start-reverse">
          <path d="M 0 1 L 9 5 L 0 9 z" fill="{C["line"]}"/>
        </marker>
      </defs>
      <rect width="{W}" height="{H}" fill="{C["bg"]}"/>
    {chr(10).join("  " + l for l in out)}
    </svg>
    '''

    import os
    os.makedirs("docs", exist_ok=True)
    open(OUTFILE, "w").write(svg)
    print("written", OUTFILE, len(svg), "bytes")


build("dark", "docs/architecture.svg")
build("muted", "docs/architecture-muted.svg")
