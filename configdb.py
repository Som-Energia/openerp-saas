ooop = dict( 
   dbname = 'destral_db', 
   port = 1234,
   user = 'admin', 
   uri = 'http://localhost', 
   pwd = 'admin', 
)
erppeek = dict( 
   server='{uri}:{port}'.format(**ooop), 
   db=ooop['dbname'], 
   user=ooop['user'], 
   password=ooop['pwd'], 
#    verbose = True, 
)
