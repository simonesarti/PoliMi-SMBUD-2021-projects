# PoliMi ***Systems and Methods for Big and Unstructure Data*** 2021 course projects

SCENARIO: Suppose you want to build an information system for managing pandemic information for a given country.

## Project 1: Neo4j

Design, store, and query a graph data structure in a NoSQL DB for supporting a contact tracing application for COVID-19.

You need to record:
* People and their connections:
    * Same-family contact by default
    * Contact tracing app and other devices
    * Explicit data collection (e.g., restaurant, theatre, hospital,…)
* Time and place of the contact (when possible depending on the cases above)
* Personal data of each person (including vaccines, tests, contagion date and place when possible) 

Tasks to perform:
* Write the specification and hypotheses of the problem and solution
* Design conceptual model (ER or similar)
* Store a sample dataset in Neo4J
* Write Queries and Commands useful for typical usage scenarios
* Implement also some application / UI or similar

## Project 2: MongoDB

You need to design, store and query data on a NoSQL DB supporting a certification app for COVID-19.
The data storage solution must keep track of people and information about their tests and vaccination status.
In particular, suppose you want to record in a document-based storage the certificate of vaccination /testing and the authorized bodies that can deliver them.

The certificate should include:
* who is vaccinated when and where (first and second doses, with which type of vaccine)
* The kind of vaccine issued (brand, type, lot, production date)
* The list of tests taken, when and where, and the respective results
* doctors and nurses attending the vaccination/tests
* demographic details of the vaccinated person
* Emergency contact person and details

The description of the authorized bodies should include the full description of the organization and location with all the relevant details (including but not limited to: GPS position, hospital or other health service name, type of entity, department issuing the vaccine, address, ...). Consider that your data will be used for checking the validity of the certificate (concerning expiration dates, evolution of the rules, and so on). Decide how to manage this requirement.

Tasks to perform:
* Write the specification and hypotheses of the problem and solution
* Design conceptual model (ER or similar)
* Store a sample dataset in MongoDB
* Write Queries and Commands useful for typical usage scenarios
* Implement also some application / UI or similar

## Project 3: ElasticSearch

You need to design, store and query data on a NoSQL DB supporting a data analysis scenario over data about COVID-19 vaccination statistics. The purpose is that of building a comprehensive database of vaccinations. 
We suggest you get and import the dataset available as open data [here](https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv).
(Pick a time interval of at least 3 months. The main website with the data description is available [here](https://github.com/italia/covid19-opendata-vaccini/).

By using an ElasticSearch installation: import the data of the dataset, apply the appropriate schema design choices, and implement some queries aiming at exploring the data statistics (evolution in time, multiple perspectives on the data for understanding the vaccine uptake by genre, region, etc.), and design a basic visualization dashboard of the results.

Tasks to perform:
* Write the specification and hypotheses of the problem and solution
* Report the schema of the data, including the types of the different fields. Make sure that the format/schema is correct and motivate it (even if you use the automatic mapping)
* Store the dataset in ElasticSearch
* Write Queries and data update commands useful for typical usage scenarios
* Implement a visualization dashboard using Kibana. Exploration, navigation and dynamicity of the dashboard will be considered
* You can integrate other datasets or implement some features in another nosql platform (different from Neo4J and MongoDB)


