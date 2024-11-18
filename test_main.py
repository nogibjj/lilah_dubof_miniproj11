"""
Test goes here

"""
import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "extract.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert file_path in result.stdout


def test_describe():
    """tests transfrom"""
    stats_result_df = subprocess.run(
        [   
            "python", 
            "transform.py", 
            "query", 
            """SELECT Industry, 
        AVG(Hours_Worked_Per_Week) AS avg_hours_worked
        FROM remote_health1
        GROUP BY Industry
        ORDER BY avg_hours_worked DESC;""", "remote_health1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert stats_result_df.returncode == 0
    assert stats_result_df in stats_result_df.stdout


def test_query():
    """tests general_query"""
    query_result_df = subprocess.run(
        [
            "python",
            "transform.py",
            "query",
            """ SELECT Industry, COUNT(Employee_ID)
        AS Number_Of_Employees 
        FROM remote_health1 
        GROUP BY Industry 
        ORDER BY Number_Of_Employees DESC;""",
        "remote_health1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert query_result_df.returncode == 0
    assert query_result_df in query_result_df.stdout

   


if __name__ == "__main__":
    file_path = "./data/table_1_remote_work_mental_health_data.csv"
    url="https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv"
    test_extract()
    test_describe()
    test_query()
