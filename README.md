# Alnaqib's Journey

**A Living Learning Archive — DevOps, Linux, Kubernetes and Cloud**

This repository is the working archive of an ongoing learning journey. Every folder here
represents something that was actually read, practiced, broken, fixed and written down —
not a curriculum designed in advance.

It is intentionally unfinished. New tools and topics are added as they are encountered in
real work, which means the structure grows over time rather than being frozen at a
"final" version.

---

## What this repository is

- A **structured archive** of study material, notes and references collected while learning DevOps.
- A record of the **order** things were learned in, so the path itself is visible — not just the end result.
- A place where each tool has its own space, including the small ones that only came up once in a real problem.

## What this repository is not

- Not a course, tutorial series, or teaching product.
- Not a portfolio of finished projects — hands-on project repositories live separately.
- Not a claim of mastery over anything listed here.

---

## Learning Architecture

The diagram below is a **knowledge map**, not an application architecture. It mirrors the
real folder tree: three top-level domains, and inside the main one, two different kinds of
learning — a sequential path, and a non-linear set of concepts that grew out of real work.

```mermaid
%%{init: {"flowchart": {"curve": "basis", "nodeSpacing": 22, "rankSpacing": 42}, "themeVariables": {"lineColor": "#8FA4B8"}}}%%
flowchart TD
    ROOT["<b>Alnaqib's Journey</b>"]
    ROOT --> DL["<b>DevOps-Learning</b>"]
    ROOT --> LX["<b>Linux</b>"]
    ROOT --> OS["<b>OpenShift</b>"]

    DL --> T1["<b>1-DevOps</b>"]
    DL --> T2["<b>2-DevOps-Tools<br/>-and-Concepts</b>"]

    T1 --> A1["Intro"] --> A2["Linux"] --> A3["NGINX"] --> A4["Docker"] --> A5["Kubernetes"] --> A6["Helm"] --> A7["Ansible"] --> A8["AWS"]

    T2 --> B1["AWS-Concepts"]
    T2 --> B2["Kubernetes-Concepts"]
    T2 --> B3["HAProxy"]
    T2 --> B4["Observability"]
    T2 --> B5["SonarQube + Trivy"]
    T2 --> B6["Vault"]
    T2 --> B7["Velero"]

    B1 --> B1a["DynamoDB-Locking"]
    B1 --> B1b["RDS+EBS"]
    B2 --> B2a["Pod-Types"]
    B2 --> B2b["Container-Types"]
    B2 --> B2c["Ingress"]
    B2 --> B2d["Network-Policy"]
    B2 --> B2e["Kubeadm-vs-EKS"]

    LX --> L1["Linux Admin I"] --> L2["Linux Admin II"]

    OS --> O1["1 Intro"] --> O2["2 Auth"] --> O3["3 Install"] --> O4["4 Permission & Role"] --> O5["5 Create Users"] --> O6["6 CLI & GUI"] --> O7["7 Routes"] --> O8["8 Limit Range"] --> O9["9 Project Template"]

    classDef root   fill:#101B2D,stroke:#4A6C8F,stroke-width:2px,color:#F2F6FA
    classDef domain fill:#123A63,stroke:#3E8FD0,stroke-width:2px,color:#EAF2FA
    classDef track  fill:#1E4030,stroke:#5FA377,stroke-width:2px,color:#E8F5EC
    classDef leaf   fill:#A9B9CC,stroke:#6A7E96,stroke-width:1.5px,color:#12202E
    classDef tool   fill:#C9BF9F,stroke:#9A8F6E,stroke-width:1.5px,color:#241F12
    class ROOT root
    class DL,LX,OS domain
    class T1,T2 track
    class A1,A2,A3,A4,A5,A6,A7,A8,L1,L2,O1,O2,O3,O4,O5,O6,O7,O8,O9 leaf
    class B1,B2,B3,B4,B5,B6,B7,B1a,B1b,B2a,B2b,B2c,B2d,B2e tool
```

### Reading the diagram

| Colour | Layer | Meaning |
|---|---|---|
| Navy | Root and domains | The archive itself, and the three top-level directories. |
| Green | Tracks | The two halves of `DevOps-Learning/` — the ordered path and the applied concepts. |
| Steel blue | Sequential modules | Material read in a fixed order. Arrows are the study order, not just links. |
| Sand | Tools and concepts | Standalone subjects. No order between them — only nesting where a topic has sub-topics. |

Every box is an actual directory or module on disk. Nothing in the diagram is planned-only.

The two tracks exist for a reason. `1-DevOps/` is **linear** — each folder builds on the one
before it, and the numbering is the study order. `2-DevOps-Tools-and-Concepts/` is
**non-linear** — those folders appeared because a specific tool or behaviour showed up
while working on something real, and it needed to be understood properly before moving on.

---

## Repository structure

```
Alnaqib-s-Journey/
│
├── DevOps-Learning/
│   │
│   ├── 1-DevOps/                        # the ordered path
│   │   ├── 1-Intro-DevOps/
│   │   ├── 2-Book-Linux-Admi-1/         # 5 modules
│   │   ├── 3-NGINX/
│   │   ├── 4-Book-Docker/
│   │   ├── 5-k8s/
│   │   ├── 6-Helm/
│   │   ├── 7-Ansible/
│   │   └── 8-cloud_AWS/
│   │
│   └── 2-DevOps-Tools-and-Concepts/     # tools met through real work
│       ├── AWS-Concepts/
│       │   ├── DynamoDB-Locking/
│       │   └── RDS+EBS/
│       ├── HAProxy/
│       ├── Kubernetes-Concepts/
│       │   ├── Container-Types/
│       │   ├── Ingress/
│       │   ├── Kubeadm-vs-EKS/
│       │   ├── Network-Policy/
│       │   └── Pod-Types/
│       ├── Observability/
│       ├── SonarQube&Trivy/
│       ├── Vault/
│       └── Velero/
│
├── Linux/                               # standalone reference library
│   ├── 1-Book-Linux-Admi-1/
│   └── 2-Book-Linux-Admi-2/
│
└── OpenShift/                           # 9 sequential modules
```

The `OpenShift/` track is nine numbered modules, read in order:

1. Intro to OpenShift
2. Authentication and Authorization
3. Install
4. Permission and Role
5. Create Users
6. CLI and GUI
7. Routes
8. Limit Range
9. Project Template

**Current size:** 41 directories, 61 files.

---

## Working method

Every topic in this archive went through the same loop. Nothing gets a folder here until it
has at least been practiced — and the dotted line back means the loop never actually closes.

```mermaid
%%{init: {"flowchart": {"curve": "basis"}, "themeVariables": {"lineColor": "#8B9A9F"}}}%%
flowchart LR
    A["Learn"] --> B["Understand"] --> C["Practice"] --> D["Build"] --> E["Document"] --> F["Share"]
    F -.-> A

    classDef step fill:#63798A,stroke:#41535F,stroke-width:2px,color:#F4F7F9
    class A,B,C,D,E,F step
```

- **Learn / Understand** — read the source material properly instead of collecting commands.
- **Practice** — run it, break it, read the errors.
- **Build** — use it inside something real, not an isolated example.
- **Document** — write it down here, in a form that is still useful months later.
- **Share** — keep the repository public so the path is reviewable.

---

## Conventions

A few deliberate decisions worth knowing before browsing or cloning:

- **Numbering is the study order.** `1-`, `2-`, `3-` prefixes are not cosmetic. Folders are
  read in that sequence.
- **Filenames are normalized.** All spaces replaced with hyphens, no trailing spaces before
  extensions — so paths are safe to use in scripts and CI.
- **Linux Book 1 appears twice, on purpose.** Once inside `DevOps-Learning/1-DevOps/` to keep
  the learning path complete, and once under `Linux/` so the reference library stands on its
  own. This is not a duplication mistake.
- **Scanned material is compressed.** The archive was reduced from roughly 688 MB to about
  114 MB in the working tree, so a clone stays reasonable.
- **History is intentionally a single commit.** Older revisions carried the uncompressed
  files and were rewritten out; keeping them would have kept the repository heavy forever.
- **Oversized files are blocked at commit time** by a pre-commit hook, so the size problem
  does not come back.
- **The architecture diagram lives in this file.** It is written in Mermaid, not exported as
  an image, so adding a new tool means adding one line here — not regenerating a picture.

---

## How to use this repository

Clone it and read a track end to end rather than jumping between folders:

```bash
git clone https://github.com/yousefsalemW/Alnaqib-s-Journey.git
cd Alnaqib-s-Journey
```

- New to DevOps → start at `DevOps-Learning/1-DevOps/1-Intro-DevOps/` and follow the numbers.
- Looking for one specific tool → go straight to `DevOps-Learning/2-DevOps-Tools-and-Concepts/`.
- Working on Linux fundamentals → `Linux/`.
- Coming from a Kubernetes background → `OpenShift/`.

---

## About

**Yousef Salem** — Junior DevOps Engineer, Cairo.

I keep this archive public because the intermediate steps of learning are usually the part
that gets deleted, and they are the part worth keeping. It grows as I do.

- GitHub: [yousefsalemW](https://github.com/yousefsalemW)
- Docker Hub: [alnaqib](https://hub.docker.com/u/alnaqib)
- LinkedIn: [yousef-salem-1a5757401](https://www.linkedin.com/in/yousef-salem-1a5757401)

---

## Note on content

This archive contains study material and personal notes gathered from books, official
documentation and hands-on practice. Third-party material remains the property of its
original authors and is kept here for personal study and reference. The notes, structure and
documentation are my own work.
