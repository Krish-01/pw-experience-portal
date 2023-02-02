# PW Skills Experience Portal

Dashboard of PW Skills Experience Portal which shows all the projects with their documentation link.

This app is made with `Streamlit` library (used for making Web-Apps) with `Python` programming language. This is a multi-page streamlit app.

> See my another PW Courses dashboard [here](https://github.com/arv-anshul/PW-courses-scrapper-app).

```bash
# Install streamlit
pip install streamlit

# Run the dashboard
streamlit run 🗒️_README.py
```

## Motivation :

When I saw the tutorial of this portal I realizes that I have to iterate through all the sections to see the description of projects. Then I decided that I would like to know all the projects from different **_techs and domains_** at one time. So I find the API and made a dashboard out of it by myself to analyse all the projects which are provided by them.

> Also this helps me to decide that which project is best for me.

# Process

## Fectching data from API

Data of PW Skills Experience Portal which includes :

1. Types of **technology** used for project building.
2. Different **domains** in which the projects asociated.
3. List of **projects** with its _Title, Description Link_.

> Python Script [Here](./utils/api_to_json_file.ipynb)

## Created by [arv-anshul](https://github.com/arv-anshul)

Also see my another dashboard which shows all the [PW Skills Courses Overview](https://github.com/arv-anshul/PW-courses-scrapper-app).
