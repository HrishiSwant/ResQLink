# ResQLink Infrastructure as Code

## 1. What is Infrastructure as Code?

Infrastructure as Code (IaC) is the practice of defining infrastructure configuration using files instead of manually configuring infrastructure.

Infrastructure configuration can be stored in version control and reviewed alongside application code.

## 2. ResQLink Infrastructure

ResQLink uses the following infrastructure components:

```text
ResQLink
├── Vercel
│   └── Frontend
│
├── Render
│   ├── Incident Service
│   └── Resource Service
│
└── MongoDB Atlas
    ├── Incident Database
    └── Resource Database
