```sql
<function query at 0x7fe148bb31a0>
```

```response from databricks
| col_name                     | data_type                                                                                                                                                                                                       | comment   |
|:-----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| _c0                          | string                                                                                                                                                                                                          |           |
| _c1                          | string                                                                                                                                                                                                          |           |
| _c2                          | string                                                                                                                                                                                                          |           |
| _c3                          | string                                                                                                                                                                                                          |           |
| _c4                          | string                                                                                                                                                                                                          |           |
| _c5                          | string                                                                                                                                                                                                          |           |
| _c6                          | string                                                                                                                                                                                                          |           |
| _c7                          | string                                                                                                                                                                                                          |           |
| _c8                          | string                                                                                                                                                                                                          |           |
| _c9                          | string                                                                                                                                                                                                          |           |
| Employee_ID                  | bigint                                                                                                                                                                                                          |           |
| Age                          | int                                                                                                                                                                                                             |           |
| Gender                       | string                                                                                                                                                                                                          |           |
| Job_Role                     | string                                                                                                                                                                                                          |           |
| Industry                     | string                                                                                                                                                                                                          |           |
| Years_of_Experience          | int                                                                                                                                                                                                             |           |
| Work_Location                | string                                                                                                                                                                                                          |           |
| Hours_Worked_Per_Week        | int                                                                                                                                                                                                             |           |
| Number_of_Virtual_Meetings   | int                                                                                                                                                                                                             |           |
| Work_Life_Balance_Rating     | int                                                                                                                                                                                                             |           |
|                              |                                                                                                                                                                                                                 |           |
| # Delta Statistics Columns   |                                                                                                                                                                                                                 |           |
| Column Names                 | Work_Life_Balance_Rating, Years_of_Experience, Number_of_Virtual_Meetings, _c3, _c5, _c0, Job_Role, _c4, _c9, Industry, _c8, _c1, Age, Hours_Worked_Per_Week, _c7, _c2, Gender, _c6, Work_Location, Employee_ID |           |
| Column Selection Method      | first-32                                                                                                                                                                                                        |           |
|                              |                                                                                                                                                                                                                 |           |
| # Detailed Table Information |                                                                                                                                                                                                                 |           |
| Catalog                      | ids706_data_engineering                                                                                                                                                                                         |           |
| Database                     | default                                                                                                                                                                                                         |           |
| Table                        | RemoteHealthTable                                                                                                                                                                                               |           |
| Created Time                 | Tue Nov 19 02:24:12 UTC 2024                                                                                                                                                                                    |           |
| Last Access                  | UNKNOWN                                                                                                                                                                                                         |           |
| Created By                   | Spark                                                                                                                                                                                                           |           |
| Type                         | MANAGED                                                                                                                                                                                                         |           |
| Location                     | s3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/49eeefc2-b6ba-49cc-9381-6d3aa764bff8                            |           |
| Provider                     | delta                                                                                                                                                                                                           |           |
| Owner                        | lilah.duboff@duke.edu                                                                                                                                                                                           |           |
| Is_managed_location          | true                                                                                                                                                                                                            |           |
| Table Properties             | [delta.enableDeletionVectors=true,delta.feature.appendOnly=supported,delta.feature.deletionVectors=supported,delta.feature.invariants=supported,delta.minReaderVersion=3,delta.minWriterVersion=7]              |           |
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM RemoteHealthTable
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM RemoteHealthTable
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;
```

```response from databricks
| Industry      |   Number_Of_Employees |
|:--------------|----------------------:|
| IT            |                    20 |
| Healthcare    |                    17 |
| Consulting    |                    16 |
| Education     |                    12 |
| Retail        |                    12 |
| Manufacturing |                    12 |
| Finance       |                    11 |
```

```sql
SELECT Industry, 
    AVG(Hours_Worked_Per_Week) AS avg_hours_worked
    FROM RemoteHealthTable
    GROUP BY Industry
    ORDER BY avg_hours_worked DESC;
```

```response from databricks
Query received, executing next...
```

```sql
SELECT Industry, 
    AVG(Hours_Worked_Per_Week) AS avg_hours_worked
    FROM RemoteHealthTable
    GROUP BY Industry
    ORDER BY avg_hours_worked DESC;
```

```response from databricks
| Industry      |   avg_hours_worked |
|:--------------|-------------------:|
| Manufacturing |            43.9167 |
| Finance       |            41.2727 |
| IT            |            40.65   |
| Education     |            40.3333 |
| Retail        |            38.8333 |
| Healthcare    |            35.6471 |
| Consulting    |            35.125  |
```

