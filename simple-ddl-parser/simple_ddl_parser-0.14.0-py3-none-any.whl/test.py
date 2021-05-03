from simple_ddl_parser import DDLParser

ddl = """
Create Table emp_table (
empno Number,
ename Varchar2(100),
sal Number,
photo Blob,

CONSTRAINT CHK_Person_Age_under CHECK (days_active<=18 AND user_city='New York'))
"""

result = DDLParser(ddl).run(group_by_type=True)
import pprint

pprint.pprint(result)
print(result['tables'][0]['constraints']['checks'][0]['statement'])