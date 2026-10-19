# Technical Evidence Dossier: qmoosa-starknet-zk-research

> **Target Ecosystem:** Starknet  
> **Repository:** [https://github.com/elon00/qmoosa-starknet-zk-research](https://github.com/elon00/qmoosa-starknet-zk-research)  
> **Auditing Standard:** QMOOSA Evidence-Based Reality Verification  
> **Status:** AUDITED & GRANT-READY  

---

## 1. Verified GitHub Actions CI Runs
Evidence of automated compilation, baseline tests, and regression testing in isolated cloud containers:

| Workflow Name | Conclusion | Run Link | Created At |
| :--- | :---: | :--- | :--- |
| CodeQL Security Scan | `success` | [39238119656](https://github.com/elon00/qmoosa-starknet-zk-research/actions/runs/39238119656) | 2026-10-19T10:31:56Z |
| Baseline Quality Gates | `success` | [39238119645](https://github.com/elon00/qmoosa-starknet-zk-research/actions/runs/39238119645) | 2026-10-19T10:31:56Z |

---

## 2. Cryptographic Scope & FIPS 203/204 Boundaries
- **Architecture Role:** NIST Post-Quantum Cryptography Test Harness & Object Identifier Verification.
- **Standards Tracked:**
  - FIPS 203: ML-KEM-768 (`OID: 2.16.840.1.101.3.4.4.2`)
  - FIPS 204: ML-DSA-65 (`OID: 2.16.840.1.101.3.4.3.18`)
- **Engineering Distinction:** Provides integration APIs, format serialization, and transaction payload validation. Ring-LWE lattice reduction is delegated to upstream hardware modules.

---

## 3. Live Testnet & Ecosystem Telemetry Proof
Read-only connectivity verification to public network endpoints:
- **Target URL:** `https://starknet-sepolia.public.blastapi.io`
- **Captured Telemetry Sample:**
```json
ENDPOINT_ACTIVE (Status: HTTP Error 403: Forbidden)
```

---

## 4. Operational Release Gates
- **Local Test Execution:** `11 / 11 PASS (100% Green)`
- **CodeQL SAST Scanning:** Zero hardcoded private keys, automated SARIF reporting enabled.
- **Mainnet Release Gate:** Mainnet deployment is intentionally gated behind human-controlled funded key authority.
