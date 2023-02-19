--Created: 18th Feb 2023--
--Reference: Maximo Scripting--
--Credit: IBM Documentation--
--Contributor: Surender Balasundaram--
--To Check Active Sessions in Maximo Database--

connectionKey = ""
con = ""
stmt = ""

try:
    connectionKey = mbo.getThisMboSet().getUserInfo().getConnectionKey();
    con = mbo.getThisMboSet().getMboServer().getDBConnection(connectionKey)
    stmt = con.createStatement()
    
    file = open("./MeaGlobalDirs/CustomerFiles/Inbound/runfile.sql","r")
	
    for line in file:        
        rs = stmt.execute(line)
    con.commit()
	
finally:
    if stmt != "":
        stmt.close()		
    if connectionKey != "" and con != "":
        mbo.getThisMboSet().getMboServer().freeDBConnection(connectionKey)
    if file != null:
        file.close()
    
