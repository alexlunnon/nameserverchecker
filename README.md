# Domain Name Server Checker
Simple multi-threaded python script which using `dig ns` to obtain NameServer records for domains provided. 

##Using NameServerChecker.py
1. Download nameserverchecker.py
2. Update line `33` to include the location of your CSV file of domains (one domain per line)
2. Run `python nameserverchecker.py domainlist.csv` 
3. You will see responses outputted to the console and can write to a file by running `python nameserverchecker.py domainlist.csv >> response.txt` 

##Settings
You can adjust concurrency by changing the `concurrent = 25` value on `line 7`
