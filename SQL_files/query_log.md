```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
| Industry      |   Number_Of_Employees |
|:--------------|----------------------:|
| IT            |                   265 |
| Healthcare    |                   223 |
| Consulting    |                   210 |
| Education     |                   158 |
| Manufacturing |                   157 |
| Retail        |                   156 |
| Finance       |                   145 |
```

```sql
SELECT r1.Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN r2.Stress_Level = 'High' THEN 1 WHEN r2.Stress_Level = 'Medium' THEN 2 WHEN r2.Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 AS r1 JOIN remote_health2 AS r2 ON r1.Employee_ID = r2.Employee_ID GROUP BY r1.Industry ORDER BY count_of_employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT r1.Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN r2.Stress_Level = 'High' THEN 1 WHEN r2.Stress_Level = 'Medium' THEN 2 WHEN r2.Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 AS r1 JOIN remote_health2 AS r2 ON r1.Employee_ID = r2.Employee_ID GROUP BY r1.Industry ORDER BY count_of_employees DESC;
```

```response from databricks
| Industry      |   count_of_employees |   avg_hours_worked |   avg_stress_level |
|:--------------|---------------------:|-------------------:|-------------------:|
| IT            |                 3180 |            40.7623 |            2.1434  |
| Healthcare    |                 2676 |            35.7489 |            2.0583  |
| Consulting    |                 2520 |            35.1238 |            1.86667 |
| Education     |                 1896 |            40.4051 |            1.67089 |
| Manufacturing |                 1884 |            43.9809 |            2       |
| Retail        |                 1872 |            38.8333 |            1.83333 |
| Finance       |                 1740 |            41.1448 |            2.07586 |
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
| Employee_ID   |   count(1) |
|:--------------|-----------:|
| EMP0052       |         13 |
| EMP0081       |         13 |
| EMP0002       |         15 |
| EMP0009       |         13 |
| EMP0098       |         13 |
| EMP0065       |         13 |
| EMP0039       |         13 |
| EMP0057       |         13 |
| EMP0034       |         13 |
| EMP0036       |         13 |
| EMP0077       |         13 |
| EMP0005       |         15 |
| EMP0078       |         13 |
| EMP0061       |         13 |
| EMP0054       |         13 |
| EMP0073       |         13 |
| EMP0074       |         13 |
| EMP0055       |         13 |
| EMP0058       |         13 |
| EMP0015       |         13 |
| EMP0011       |         13 |
| EMP0067       |         13 |
| EMP0024       |         13 |
| EMP0060       |         13 |
| EMP0095       |         13 |
| EMP0025       |         13 |
| EMP0043       |         13 |
| EMP0028       |         13 |
| EMP0003       |         15 |
| EMP0075       |         13 |
| EMP0027       |         13 |
| EMP0029       |         13 |
| EMP0046       |         13 |
| EMP0020       |         13 |
| EMP0026       |         13 |
| EMP0001       |         15 |
| EMP0072       |         13 |
| EMP0045       |         13 |
| EMP0099       |         13 |
| EMP0048       |         13 |
| EMP0051       |         13 |
| EMP0013       |         13 |
| EMP0053       |         13 |
| EMP0079       |         13 |
| EMP0064       |         13 |
| EMP0006       |         15 |
| EMP0021       |         13 |
| EMP0047       |         13 |
| EMP0038       |         13 |
| EMP0035       |         13 |
| EMP0042       |         13 |
| EMP0010       |         13 |
| EMP0088       |         13 |
| EMP0012       |         13 |
| EMP0030       |         13 |
| EMP0089       |         13 |
| EMP0100       |         13 |
| EMP0018       |         13 |
| EMP0023       |         13 |
| EMP0049       |         13 |
| EMP0032       |         13 |
| EMP0022       |         13 |
| EMP0071       |         13 |
| EMP0093       |         13 |
| EMP0008       |         14 |
| EMP0017       |         13 |
| EMP0031       |         13 |
| EMP0019       |         13 |
| EMP0084       |         13 |
| EMP0080       |         13 |
| EMP0090       |         13 |
| EMP0066       |         13 |
| EMP0037       |         13 |
| EMP0086       |         13 |
| EMP0069       |         13 |
| EMP0083       |         13 |
| EMP0062       |         13 |
| EMP0070       |         13 |
| EMP0082       |         13 |
| EMP0094       |         13 |
| EMP0007       |         14 |
| EMP0056       |         13 |
| EMP0059       |         13 |
| EMP0014       |         13 |
| EMP0050       |         13 |
| EMP0068       |         13 |
| EMP0063       |         13 |
| EMP0091       |         13 |
| EMP0096       |         13 |
| EMP0040       |         13 |
| EMP0087       |         13 |
| EMP0041       |         13 |
| EMP0092       |         13 |
| EMP0085       |         13 |
| EMP0033       |         13 |
| EMP0076       |         13 |
| EMP0044       |         13 |
| EMP0097       |         13 |
| EMP0004       |         15 |
| EMP0016       |         13 |
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
| Industry      |   Number_Of_Employees |
|:--------------|----------------------:|
| IT            |                   265 |
| Healthcare    |                   223 |
| Consulting    |                   210 |
| Education     |                   158 |
| Manufacturing |                   157 |
| Retail        |                   156 |
| Finance       |                   145 |
```

```sql
SELECT r1.Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN r1.Stress_Level = 'High' THEN 1 WHEN r1.Stress_Level = 'Medium' THEN 2 WHEN r1.Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 AS r1 ORDER BY count_of_employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT r1.Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN r1.Stress_Level = 'High' THEN 1 WHEN r1.Stress_Level = 'Medium' THEN 2 WHEN r1.Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 AS r1 ORDER BY count_of_employees DESC;
```

```response from databricks
Error occurred: [UNRESOLVED_COLUMN.WITH_SUGGESTION] A column, variable, or function parameter with name `r1`.`Stress_Level` cannot be resolved. Did you mean one of the following? [`r1`.`Gender`, `r1`.`Job_Role`, `r1`.`Age`, `r1`.`Industry`, `r1`.`Employee_ID`]. SQLSTATE: 42703; line 1 pos 130;
'Sort ['count_of_employees DESC NULLS LAST], true
+- 'Aggregate [Industry#266, count(Employee_ID#262) AS count_of_employees#249L, avg(Hours_Worked_Per_Week#269) AS avg_hours_worked#250, 'AVG(CASE WHEN ('r1.Stress_Level = High) THEN 1 WHEN ('r1.Stress_Level = Medium) THEN 2 WHEN ('r1.Stress_Level = Low) THEN 3 ELSE null END) AS avg_stress_level#251]
   +- SubqueryAlias r1
      +- SubqueryAlias ids706_data_engineering.default.remote_health1
         +- Relation ids706_data_engineering.default.remote_health1[Employee_ID#262,Age#263,Gender#264,Job_Role#265,Industry#266,Years_of_Experience#267,Work_Location#268,Hours_Worked_Per_Week#269,Number_of_Virtual_Meetings#270,Work_Life_Balance_Rating#271] parquet

```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
| Employee_ID   |   count(1) |
|:--------------|-----------:|
| EMP0052       |         13 |
| EMP0081       |         13 |
| EMP0002       |         15 |
| EMP0009       |         13 |
| EMP0098       |         13 |
| EMP0065       |         13 |
| EMP0039       |         13 |
| EMP0057       |         13 |
| EMP0034       |         13 |
| EMP0036       |         13 |
| EMP0077       |         13 |
| EMP0005       |         15 |
| EMP0078       |         13 |
| EMP0061       |         13 |
| EMP0054       |         13 |
| EMP0073       |         13 |
| EMP0074       |         13 |
| EMP0055       |         13 |
| EMP0058       |         13 |
| EMP0015       |         13 |
| EMP0011       |         13 |
| EMP0067       |         13 |
| EMP0024       |         13 |
| EMP0060       |         13 |
| EMP0095       |         13 |
| EMP0025       |         13 |
| EMP0043       |         13 |
| EMP0028       |         13 |
| EMP0003       |         15 |
| EMP0075       |         13 |
| EMP0027       |         13 |
| EMP0029       |         13 |
| EMP0046       |         13 |
| EMP0020       |         13 |
| EMP0026       |         13 |
| EMP0001       |         15 |
| EMP0072       |         13 |
| EMP0045       |         13 |
| EMP0099       |         13 |
| EMP0048       |         13 |
| EMP0051       |         13 |
| EMP0013       |         13 |
| EMP0053       |         13 |
| EMP0079       |         13 |
| EMP0064       |         13 |
| EMP0006       |         15 |
| EMP0021       |         13 |
| EMP0047       |         13 |
| EMP0038       |         13 |
| EMP0035       |         13 |
| EMP0042       |         13 |
| EMP0010       |         13 |
| EMP0088       |         13 |
| EMP0012       |         13 |
| EMP0030       |         13 |
| EMP0089       |         13 |
| EMP0100       |         13 |
| EMP0018       |         13 |
| EMP0023       |         13 |
| EMP0049       |         13 |
| EMP0032       |         13 |
| EMP0022       |         13 |
| EMP0071       |         13 |
| EMP0093       |         13 |
| EMP0008       |         14 |
| EMP0017       |         13 |
| EMP0031       |         13 |
| EMP0019       |         13 |
| EMP0084       |         13 |
| EMP0080       |         13 |
| EMP0090       |         13 |
| EMP0066       |         13 |
| EMP0037       |         13 |
| EMP0086       |         13 |
| EMP0069       |         13 |
| EMP0083       |         13 |
| EMP0062       |         13 |
| EMP0070       |         13 |
| EMP0082       |         13 |
| EMP0094       |         13 |
| EMP0007       |         14 |
| EMP0056       |         13 |
| EMP0059       |         13 |
| EMP0014       |         13 |
| EMP0050       |         13 |
| EMP0068       |         13 |
| EMP0063       |         13 |
| EMP0091       |         13 |
| EMP0096       |         13 |
| EMP0040       |         13 |
| EMP0087       |         13 |
| EMP0041       |         13 |
| EMP0092       |         13 |
| EMP0085       |         13 |
| EMP0033       |         13 |
| EMP0076       |         13 |
| EMP0044       |         13 |
| EMP0097       |         13 |
| EMP0004       |         15 |
| EMP0016       |         13 |
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
| Industry      |   Number_Of_Employees |
|:--------------|----------------------:|
| IT            |                   265 |
| Healthcare    |                   223 |
| Consulting    |                   210 |
| Education     |                   158 |
| Manufacturing |                   157 |
| Retail        |                   156 |
| Finance       |                   145 |
```

```sql
SELECT Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN Stress_Level = 'High' THEN 1 WHEN Stress_Level = 'Medium' THEN 2 WHEN Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 ORDER BY count_of_employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN Stress_Level = 'High' THEN 1 WHEN Stress_Level = 'Medium' THEN 2 WHEN Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 ORDER BY count_of_employees DESC;
```

```response from databricks
Error occurred: [UNRESOLVED_COLUMN.WITH_SUGGESTION] A column, variable, or function parameter with name `r1`.`Employee_ID` cannot be resolved. Did you mean one of the following? [`remote_health1`.`Employee_ID`, `remote_health1`.`Age`, `remote_health1`.`Gender`, `remote_health1`.`Industry`, `remote_health1`.`Job_Role`]. SQLSTATE: 42703; line 1 pos 23;
'Sort ['count_of_employees DESC NULLS LAST], true
+- 'Aggregate [Industry#395, 'COUNT('r1.Employee_ID) AS count_of_employees#378, avg(Hours_Worked_Per_Week#398) AS avg_hours_worked#379, 'AVG(CASE WHEN ('Stress_Level = High) THEN 1 WHEN ('Stress_Level = Medium) THEN 2 WHEN ('Stress_Level = Low) THEN 3 ELSE null END) AS avg_stress_level#380]
   +- SubqueryAlias ids706_data_engineering.default.remote_health1
      +- Relation ids706_data_engineering.default.remote_health1[Employee_ID#391,Age#392,Gender#393,Job_Role#394,Industry#395,Years_of_Experience#396,Work_Location#397,Hours_Worked_Per_Week#398,Number_of_Virtual_Meetings#399,Work_Life_Balance_Rating#400] parquet

```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
| Employee_ID   |   count(1) |
|:--------------|-----------:|
| EMP0052       |         13 |
| EMP0081       |         13 |
| EMP0002       |         15 |
| EMP0009       |         13 |
| EMP0098       |         13 |
| EMP0065       |         13 |
| EMP0039       |         13 |
| EMP0057       |         13 |
| EMP0034       |         13 |
| EMP0036       |         13 |
| EMP0077       |         13 |
| EMP0005       |         15 |
| EMP0078       |         13 |
| EMP0061       |         13 |
| EMP0054       |         13 |
| EMP0073       |         13 |
| EMP0074       |         13 |
| EMP0055       |         13 |
| EMP0058       |         13 |
| EMP0015       |         13 |
| EMP0011       |         13 |
| EMP0067       |         13 |
| EMP0024       |         13 |
| EMP0060       |         13 |
| EMP0095       |         13 |
| EMP0025       |         13 |
| EMP0043       |         13 |
| EMP0028       |         13 |
| EMP0003       |         15 |
| EMP0075       |         13 |
| EMP0027       |         13 |
| EMP0029       |         13 |
| EMP0046       |         13 |
| EMP0020       |         13 |
| EMP0026       |         13 |
| EMP0001       |         15 |
| EMP0072       |         13 |
| EMP0045       |         13 |
| EMP0099       |         13 |
| EMP0048       |         13 |
| EMP0051       |         13 |
| EMP0013       |         13 |
| EMP0053       |         13 |
| EMP0079       |         13 |
| EMP0064       |         13 |
| EMP0006       |         15 |
| EMP0021       |         13 |
| EMP0047       |         13 |
| EMP0038       |         13 |
| EMP0035       |         13 |
| EMP0042       |         13 |
| EMP0010       |         13 |
| EMP0088       |         13 |
| EMP0012       |         13 |
| EMP0030       |         13 |
| EMP0089       |         13 |
| EMP0100       |         13 |
| EMP0018       |         13 |
| EMP0023       |         13 |
| EMP0049       |         13 |
| EMP0032       |         13 |
| EMP0022       |         13 |
| EMP0071       |         13 |
| EMP0093       |         13 |
| EMP0008       |         14 |
| EMP0017       |         13 |
| EMP0031       |         13 |
| EMP0019       |         13 |
| EMP0084       |         13 |
| EMP0080       |         13 |
| EMP0090       |         13 |
| EMP0066       |         13 |
| EMP0037       |         13 |
| EMP0086       |         13 |
| EMP0069       |         13 |
| EMP0083       |         13 |
| EMP0062       |         13 |
| EMP0070       |         13 |
| EMP0082       |         13 |
| EMP0094       |         13 |
| EMP0007       |         14 |
| EMP0056       |         13 |
| EMP0059       |         13 |
| EMP0014       |         13 |
| EMP0050       |         13 |
| EMP0068       |         13 |
| EMP0063       |         13 |
| EMP0091       |         13 |
| EMP0096       |         13 |
| EMP0040       |         13 |
| EMP0087       |         13 |
| EMP0041       |         13 |
| EMP0092       |         13 |
| EMP0085       |         13 |
| EMP0033       |         13 |
| EMP0076       |         13 |
| EMP0044       |         13 |
| EMP0097       |         13 |
| EMP0004       |         15 |
| EMP0016       |         13 |
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
| Industry      |   Number_Of_Employees |
|:--------------|----------------------:|
| IT            |                   265 |
| Healthcare    |                   223 |
| Consulting    |                   210 |
| Education     |                   158 |
| Manufacturing |                   157 |
| Retail        |                   156 |
| Finance       |                   145 |
```

```sql
SELECT Industry, COUNT(Employee_ID) AS Number_Of_Employees, AVG(Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN Stress_Level = 'High' THEN 1 WHEN Stress_Level = 'Medium' THEN 2 WHEN Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID) AS Number_Of_Employees, AVG(Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN Stress_Level = 'High' THEN 1 WHEN Stress_Level = 'Medium' THEN 2 WHEN Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Error occurred: [UNRESOLVED_COLUMN.WITH_SUGGESTION] A column, variable, or function parameter with name `Stress_Level` cannot be resolved. Did you mean one of the following? [`Gender`, `Job_Role`, `Age`, `Industry`, `Employee_ID`]. SQLSTATE: 42703; line 1 pos 122;
'Sort ['Number_Of_Employees DESC NULLS LAST], true
+- 'Aggregate [Industry#522, count(Employee_ID#518) AS Number_Of_Employees#505L, avg(Hours_Worked_Per_Week#525) AS avg_hours_worked#506, 'AVG(CASE WHEN ('Stress_Level = High) THEN 1 WHEN ('Stress_Level = Medium) THEN 2 WHEN ('Stress_Level = Low) THEN 3 ELSE null END) AS avg_stress_level#507]
   +- SubqueryAlias ids706_data_engineering.default.remote_health1
      +- Relation ids706_data_engineering.default.remote_health1[Employee_ID#518,Age#519,Gender#520,Job_Role#521,Industry#522,Years_of_Experience#523,Work_Location#524,Hours_Worked_Per_Week#525,Number_of_Virtual_Meetings#526,Work_Life_Balance_Rating#527] parquet

```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
| Employee_ID   |   count(1) |
|:--------------|-----------:|
| EMP0052       |         13 |
| EMP0081       |         13 |
| EMP0002       |         15 |
| EMP0009       |         13 |
| EMP0098       |         13 |
| EMP0065       |         13 |
| EMP0039       |         13 |
| EMP0057       |         13 |
| EMP0034       |         13 |
| EMP0036       |         13 |
| EMP0077       |         13 |
| EMP0005       |         15 |
| EMP0078       |         13 |
| EMP0061       |         13 |
| EMP0054       |         13 |
| EMP0073       |         13 |
| EMP0074       |         13 |
| EMP0055       |         13 |
| EMP0058       |         13 |
| EMP0015       |         13 |
| EMP0011       |         13 |
| EMP0067       |         13 |
| EMP0024       |         13 |
| EMP0060       |         13 |
| EMP0095       |         13 |
| EMP0025       |         13 |
| EMP0043       |         13 |
| EMP0028       |         13 |
| EMP0003       |         15 |
| EMP0075       |         13 |
| EMP0027       |         13 |
| EMP0029       |         13 |
| EMP0046       |         13 |
| EMP0020       |         13 |
| EMP0026       |         13 |
| EMP0001       |         15 |
| EMP0072       |         13 |
| EMP0045       |         13 |
| EMP0099       |         13 |
| EMP0048       |         13 |
| EMP0051       |         13 |
| EMP0013       |         13 |
| EMP0053       |         13 |
| EMP0079       |         13 |
| EMP0064       |         13 |
| EMP0006       |         15 |
| EMP0021       |         13 |
| EMP0047       |         13 |
| EMP0038       |         13 |
| EMP0035       |         13 |
| EMP0042       |         13 |
| EMP0010       |         13 |
| EMP0088       |         13 |
| EMP0012       |         13 |
| EMP0030       |         13 |
| EMP0089       |         13 |
| EMP0100       |         13 |
| EMP0018       |         13 |
| EMP0023       |         13 |
| EMP0049       |         13 |
| EMP0032       |         13 |
| EMP0022       |         13 |
| EMP0071       |         13 |
| EMP0093       |         13 |
| EMP0008       |         14 |
| EMP0017       |         13 |
| EMP0031       |         13 |
| EMP0019       |         13 |
| EMP0084       |         13 |
| EMP0080       |         13 |
| EMP0090       |         13 |
| EMP0066       |         13 |
| EMP0037       |         13 |
| EMP0086       |         13 |
| EMP0069       |         13 |
| EMP0083       |         13 |
| EMP0062       |         13 |
| EMP0070       |         13 |
| EMP0082       |         13 |
| EMP0094       |         13 |
| EMP0007       |         14 |
| EMP0056       |         13 |
| EMP0059       |         13 |
| EMP0014       |         13 |
| EMP0050       |         13 |
| EMP0068       |         13 |
| EMP0063       |         13 |
| EMP0091       |         13 |
| EMP0096       |         13 |
| EMP0040       |         13 |
| EMP0087       |         13 |
| EMP0041       |         13 |
| EMP0092       |         13 |
| EMP0085       |         13 |
| EMP0033       |         13 |
| EMP0076       |         13 |
| EMP0044       |         13 |
| EMP0097       |         13 |
| EMP0004       |         15 |
| EMP0016       |         13 |
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
| Industry      |   Number_Of_Employees |
|:--------------|----------------------:|
| IT            |                   265 |
| Healthcare    |                   223 |
| Consulting    |                   210 |
| Education     |                   158 |
| Manufacturing |                   157 |
| Retail        |                   156 |
| Finance       |                   145 |
```

```sql
SELECT Industry, 
    AVG(Hours_Worked_Per_Week) AS avg_hours_worked
    FROM remote_health1
    GROUP BY Industry
    ORDER BY avg_hours_worked DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, 
    AVG(Hours_Worked_Per_Week) AS avg_hours_worked
    FROM remote_health1
    GROUP BY Industry
    ORDER BY avg_hours_worked DESC;
```

```response from databricks
| Industry      |   avg_hours_worked |
|:--------------|-------------------:|
| Manufacturing |            43.9809 |
| Finance       |            41.1448 |
| IT            |            40.7623 |
| Education     |            40.4051 |
| Retail        |            38.8333 |
| Healthcare    |            35.7489 |
| Consulting    |            35.1238 |
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Employee_ID, COUNT(*)
FROM remote_health1
GROUP BY Employee_ID
HAVING COUNT(*) > 1
```

```response from databricks
| Employee_ID   |   count(1) |
|:--------------|-----------:|
| EMP0052       |         13 |
| EMP0081       |         13 |
| EMP0002       |         15 |
| EMP0009       |         13 |
| EMP0098       |         13 |
| EMP0065       |         13 |
| EMP0039       |         13 |
| EMP0057       |         13 |
| EMP0034       |         13 |
| EMP0036       |         13 |
| EMP0077       |         13 |
| EMP0005       |         15 |
| EMP0078       |         13 |
| EMP0061       |         13 |
| EMP0054       |         13 |
| EMP0073       |         13 |
| EMP0074       |         13 |
| EMP0055       |         13 |
| EMP0058       |         13 |
| EMP0015       |         13 |
| EMP0011       |         13 |
| EMP0067       |         13 |
| EMP0024       |         13 |
| EMP0060       |         13 |
| EMP0095       |         13 |
| EMP0025       |         13 |
| EMP0043       |         13 |
| EMP0028       |         13 |
| EMP0003       |         15 |
| EMP0075       |         13 |
| EMP0027       |         13 |
| EMP0029       |         13 |
| EMP0046       |         13 |
| EMP0020       |         13 |
| EMP0026       |         13 |
| EMP0001       |         15 |
| EMP0072       |         13 |
| EMP0045       |         13 |
| EMP0099       |         13 |
| EMP0048       |         13 |
| EMP0051       |         13 |
| EMP0013       |         13 |
| EMP0053       |         13 |
| EMP0079       |         13 |
| EMP0064       |         13 |
| EMP0006       |         15 |
| EMP0021       |         13 |
| EMP0047       |         13 |
| EMP0038       |         13 |
| EMP0035       |         13 |
| EMP0042       |         13 |
| EMP0010       |         13 |
| EMP0088       |         13 |
| EMP0012       |         13 |
| EMP0030       |         13 |
| EMP0089       |         13 |
| EMP0100       |         13 |
| EMP0018       |         13 |
| EMP0023       |         13 |
| EMP0049       |         13 |
| EMP0032       |         13 |
| EMP0022       |         13 |
| EMP0071       |         13 |
| EMP0093       |         13 |
| EMP0008       |         14 |
| EMP0017       |         13 |
| EMP0031       |         13 |
| EMP0019       |         13 |
| EMP0084       |         13 |
| EMP0080       |         13 |
| EMP0090       |         13 |
| EMP0066       |         13 |
| EMP0037       |         13 |
| EMP0086       |         13 |
| EMP0069       |         13 |
| EMP0083       |         13 |
| EMP0062       |         13 |
| EMP0070       |         13 |
| EMP0082       |         13 |
| EMP0094       |         13 |
| EMP0007       |         14 |
| EMP0056       |         13 |
| EMP0059       |         13 |
| EMP0014       |         13 |
| EMP0050       |         13 |
| EMP0068       |         13 |
| EMP0063       |         13 |
| EMP0091       |         13 |
| EMP0096       |         13 |
| EMP0040       |         13 |
| EMP0087       |         13 |
| EMP0041       |         13 |
| EMP0092       |         13 |
| EMP0085       |         13 |
| EMP0033       |         13 |
| EMP0076       |         13 |
| EMP0044       |         13 |
| EMP0097       |         13 |
| EMP0004       |         15 |
| EMP0016       |         13 |
```

