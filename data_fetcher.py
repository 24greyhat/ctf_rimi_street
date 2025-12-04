# this tool will fetch the dataset from the cisa.gov site and store it in dataset.csv
import requests


dataset_url = "https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv"


res = requests.get(dataset_url)


if res.ok:
    with open("dataset.csv", "w") as f:
        f.write(res.text)