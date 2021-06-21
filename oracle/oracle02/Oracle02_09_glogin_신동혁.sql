--
-- Copyright (c) 1988, 2005, Oracle.  All Rights Reserved.
--
-- NAME
--   glogin.sql
--
-- DESCRIPTION
--   SQL*Plus global login "site profile" file
--
--   Add any SQL*Plus commands here that are to be executed when a
--   user starts SQL*Plus, or uses the SQL*Plus CONNECT command.
--
-- USAGE
--   This script is automatically run
--
set pagesize 30;
set linesize 200;

column mem_id format a15;
column mem_name format a15;
column mem_pwd format a15;
column mem_email format a15;
column mem_phone format a15;
column mem_address format a15;