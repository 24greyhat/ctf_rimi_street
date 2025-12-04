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




--- 

#### How the app works: 


The app is very simple and straightforward in tackling each of the demands listed above.

1. The dataset is downloaded from the Cyber Security and Infrastructure Security Agency's Website (CISA) in csv format.
    - ofcourse simple data preprocessing is done by filling in missing values and converting str datetime to pd.datetime fields.

<br/>

2. The app is split into 2 tabs:
    <br/>
    - **CVE Analysis**:
    
        This tab allows the user to input a CVE and receive all the necassry information predefined in the demands section above.

        <br/>

    - **Trend & Statistics**

        This tab  has 3 inputs that allow the user to filter the data by vendor, product or even search vulnerabilities by names and or return known ransomware campaign use only etc...


        For the data visualization streamlit provides all the tooling and pandas makes it super easy to filter and manipulate the dataset according to our needs.

        All the required features have been implemented, the app is fully functional and to keep it up to date all a user has to do is run the `data_fetcher.py` file.





---

### Data Sources

 - The sole data source i've used for this project is The CISA's Known Exploited Vulnerabilities dataset.


[The CISA's Known Exploited Vulnerabilities dataset](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=&field_date_added_wrapper=all&field_cve=&sort_by=field_date_added&items_per_page=20&url=)


---

### Tech Stack

* **Streamlit** To create and deploy the data app.
    https://streamlit.io/

* **Pandas** To preprocess and manipulate the dataset.
    https://pandas.pydata.org/
