Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

### Steps:
Prerequisite: 
-need to install airbyte

1)create virtual environment:
-mkdir newdirectory
-python3 -m venv adventureworks_venv
-source adventureworks_venv/bin/activate

2)Install necessary libraries 
-need to install dbt core (using specifc database used)
	a) pip install dagster
	b) pip install dagster-dbt dagster-webserver dbt-postgres
-install dagster airbyte
	c) pip install dagster-airbyte

3)start airbyte services -  ./run-ab-platform.sh  (if already exist)
Else - run below command
# clone Airbyte from GitHub
git clone --depth=1 https://github.com/airbytehq/airbyte.git

# switch into Airbyte directory
cd airbyte

# start Airbyte
./run-ab-platform.sh

4)Move data from mssql(oltp) to postgres(olap)

5)Create a dbt project
a)create repository
b)use dbt init to initialize project
c)use dbt debug to test connection

6)wrap dagster on dbt project folder (that contains dbt_project.yml)
a)dagster-dbt project scaffold --project-name adventureworks_dagster --dbt-project-dir /home/akmalhafiz1771998/data_warehouse/adventureworks/adventureworks_dwh                        #directory need to be included if the dagster project not build at dbt directory

7)integrate dagster and airbytes