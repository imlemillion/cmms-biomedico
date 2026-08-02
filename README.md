# ATLAS CMMS

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.60.0-red)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## Vision

A Computerized Maintenance Management System (CMMS) designed by a Biomedical Engineer to streamline the maintenance lifecycle of medical equipment across health care facilities. The long-term vision is to provide an integrated platform for managing preventive and corrective maintenance, calibration records, spare parts inventory, maintenance scheduling, service history, and equipment availability-from laboratory instruments and diagnostic devices to operating room and medical imaging systems.

Future versions will incorporate an AI-Powered troubleshooting assistant to support biomedical engineers and technicians in diagnosing complex equipment failures, documenting technical knowledge, and improving maintenance decision-making.

The platform is being developed with the needs of hospitals, clinics, and healthcare institutions in Honduras and Central America in mind, particularly those pursuing or maintaining quality and regulatory certifications.

## Current Status

The project is currently in active development.

The first module provides a functional equipment inventory system that allows users to register medical devices, store essential equipment information, track operational status, and generate basic inventory statistics.

The maintenance lifecycle module-including intervention history, equipment criticality, downtime tracking, and maintenance scheduling-is currently under active development.

## Engineering Philosophy

This project is not intended to be a tutorial implementation of a generic CMMS. Instead, every feature is designed to address real maintenance challenges identified through hands-on experience in biomedical engineering — with the goal of creating a practical and scalable solution for healthcare organizations.

## Why I Started This Project

Atlas CMMS was born from real-world experience rather than from a programming exercise.

After working as a Field Service Engineer, coordinating maintenance operations, and founding a biomedical engineering venture, I repeatedly encountered the same challenges: fragmented maintenance records, limited traceability, inefficient spare parts management, and the absence of affordable digital tools tailored to healthcare providers in the region.

Instead of accepting those limitations, I decided to build the solution I wished I had throughout my engineering career.

## Current Features

- Register medical equipment with basic data (name, brand, model, serial number)
- Track operational status per equipment
- Persist data in JSON
- View basic inventory statistics (% operational vs. requiring maintenance)
- Streamlit-based user interface

## Roadmap

- [x] Equipment registry module (Module 1)
- [ ] Maintenance lifecycle module — intervention history, criticality, downtime tracking, technovigilance (Module 2, in progress)
- [ ] Regulatory traceability — calibration history and audit trails aligned with applicable regional/international standards
- [ ] Warranty management and brand/model-specific maintenance checklists
- [ ] Migration from JSON to a relational database (SQL)
- [ ] REST API layer (FastAPI)
- [ ] ERP integration module (SAP and similar systems, via mock API for demonstration purposes)
- [ ] AI-powered troubleshooting assistant
- [ ] Containerization (Docker)

## Technology Stack

- **Python** — core language
- **Streamlit** — web interface
- **JSON** — current data persistence (see [ADR-0001](adr/0001-maintenance-cycle-data-model.md) and [ADR-0002](adr/0002-relative-path-handling.md) for related design decisions)
- **Git & GitHub** — version control

*Planned additions: SQL, FastAPI, Docker — see Roadmap above*

## How to Run It Locally

**1. Clone the repository**
```
git clone https://github.com/imlemillion/cmms-biomedico.git
cd cmms-biomedico
```

**2. Create and activate a virtual environment**
```
python -m venv venv
venv\Scripts\activate
```
*(On macOS/Linux: `source venv/bin/activate`)*

**3. Install dependencies**
```
pip install -r requirements.txt
```

**4. Run the application**
```
cd src
streamlit run app.py
```

## Architecture Decisions

Key technical decisions and the reasoning behind them are documented as Architecture Decision Records (ADRs) in the [`adr/`](adr/) folder:

- [ADR-0001](adr/0001-maintenance-cycle-data-model.md) — Maintenance cycle data model
- [ADR-0002](adr/0002-relative-path-handling.md) — Relative path handling (known technical debt)

## License

*TBD*

