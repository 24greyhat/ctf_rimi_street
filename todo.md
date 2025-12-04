### TODO




1. Core Setup & Environment

- [x] Define & Install requirements

- [ ] Define app structure with two main pages/tabs.


2. Data Integration

- [ ] Implement CVEDB class that provides all the methods needed to fetch cve data from the cvedb pypi lib.


3. Individual CVE Analysis Page

- [ ] Create a text input for one or more CVEs.

- [ ] Implement assisted entry/autocomplete for CVEs.

- [ ] Display main scores: CVSS, Impact, Exploitability, EPSS.

- [ ] Display associated CWE(s).

- [ ] Display Active Exploit Status (KEV).

- [ ] Display Affected Technologies/Components/Versions.


4. Trends & Statistics Page

- [ ] Create input for keyword (e.g., Oracle).

- [ ] Create input for duration (1, 3, 6 months, 1 year).

- [ ] Display Top 10 highest CVSS vulnerabilities.

- [ ] Display Top highest EPSS vulnerabilities.

- [ ] Display count of Medium severity CVEs.

- [ ] Display chart for most frequent CWE.

- [ ] Display count of KEV exploited CVEs.

- [ ] Plot CVSS score trend over the period.

- [ ] Display Average CVSS score.

- [ ] Display Average EPSS score.


5. Documentation

- [ ] Write docs in README.md:

- [ ] How the app works.

- [ ] Data sources used.

- [ ] Application architecture (Tech Stack).

- [ ] Clean up code and add comments.

- [ ] Deploy to vercel.