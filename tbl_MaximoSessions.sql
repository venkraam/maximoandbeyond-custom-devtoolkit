--Created: 13th Feb 2023--
--Reference: Maximo Database--
--Credit: IBM Documentation--
--To Check Active Sessions in Maximo Database--
select * from maxsession where active = 1;
--To Check Active Sessions in Maximo Database belonging to app connections/system--
select * from maxsession where issystem= 1;
--To check maxsession for a specific Userid--
select * from maxsession where userid = '  ';