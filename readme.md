### CTF: Rimi Street

> This repo contains my submision for this specific ctf.



---

#### Objectives

> The main objective is to build an MVP that is essentially a clone of `cve.org` (a minimum viable version of it).

---

 **Demands**

1. An input that accepts one or more **CVEs** by the user.

2. A Dashboard that displays the main scores: CVSS, Impact, Exploitability, EPSS

    - The associated CWE (s) (if available)

    - Information about a possible active exploit (via KEV)

    - The technologies / components / versions affected.


3. Assisted data entry (via an assistant / auto-completion of CVEs)


4. Another tab in the app (or another page) must take as arguments a keyword (Oracle, Microsoft, etc..) as well as a duration (1, 3, 6 months) and 1 year no more

    - The tab should present:
        - Top 10 vulnerabilities with the highest CVSs score
        - Top vulnerabilities with the highest EPSS
        - Medium severity
        - CWE most frequent
        - Number of CVEs already exploited (via KEV)
        - CVSS score trend over the period
        - Average CVSS score
        - Average EPSS score


* Required Documentation

    * How it works
    * Data sources
    * The application architecture AKA Tech Stack