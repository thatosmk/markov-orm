# Technocore Internship

# Day 1
## Credentials 
### database session manager credentials (heidisql)

* hostname: Replication.technocore.co.za
* user:     Thato
* pass:     Thato12345
* port:     3306



# wifi credentials
suck it!

#### error in wifi, keeps disconnecting - something like a timeout thing
#### solution is to check the files below

* look at the log files in /var/log/\* preferrably the sys and daemon logs


# Database Reports
> * write the sql query code to join data from different table and pull it through
> * use joins and also relate data from other datables as well, ones shown below

## Online database
pull the online database from [](https://lmc.technocore.co.za//report/)
#primary tables are from reach.axiom
bloom\_reach\_combined


# Day 2
> Wrapping up the database report for LMC targets v actuals 
> also looking into other database reports, **LMC Pivot**
> Continuing to learn SQL but understands most of the syntax now

# Day 3
I think the SQL code i wrote for the report is beautiful.
### Best Practices for writing good SQL code
* Always use **coalesce** 
* Specify a condition for the **else** in **case** statements to avoid
  confusing nulls that signify errors  with the kind of expected nulls from
  aggregates. 
### General Tips
* Use a **where** clause before a **group by** and/or **or** 
* Look into creating views instead of running same queries every time then
  write queries for the view you created.
* **Union** just updates the rows of a table with other tables from the other
  tables that you join them with or __union-ing__ them with. Whereas adding
  **ALL** keyword to it will append rows regardless of duplicates.

# Day 4
## Main Activity - Writing pivot queries

### Speeding up SQL queries
* One of the best tips is to limit the size of your working data set (use
  filtering clauses)
* Use only the fields you need
* Remove unnecessary tables
* Remove OUTER joins
* Remove calculated fields in joins and filtering clauses

#### <span style="color: red"> This is red</span>



# Day 5
## Optimising SQL code
### JOINs and their Elimination
