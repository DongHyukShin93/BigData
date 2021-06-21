SQL> start C:\_OracleEx\TableMember.sql

Table dropped.


Table created.


TNAME                                                        TABTYPE         CLUSTERID
------------------------------------------------------------ -------------- ----------
MEMBERT01                                                    TABLE

SQL> select * from memberT01;

no rows selected

SQL> desc membert01;
 Name
           Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME
                    VARCHAR2(20)
 MEM_ID
                    VARCHAR2(20)
 MEM_PWD
                    VARCHAR2(20)
 MEM_EMAIL
                    VARCHAR2(30)
 MEM_PHONE
                    VARCHAR2(20)
 MEM_ADDR
                    VARCHAR2(30)