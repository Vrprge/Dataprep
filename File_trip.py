import csv
res={}
def number_of_trips(filename):

#	city = filename.split('-')[0].split('/')[-1]

	with open(filename, 'r') as fil_in:
		reader = csv.DictReader(fil_in)

		n_subscribers = 0
		n_customers = 0

		for row in reader:
			if city == 'Washington':
				if ( row['Member Type'] == 'Customer'):
					n_customers += 1
				else:
					n_subscribers += 1
			else:
				if ( row['usertype'] == 'Customer' or row['usertype'] == 'Casual'):
					n_customers += 1
				else:
					n_subscribers += 1

			n_total = n_subscribers + n_customers
 
		return(n_subscribers, n_customers, n_total)


datafile=['./Chicago-BS-2016.csv','./NYC-CitiBike-2016.csv','./Washington-CapitalBikeshare-2016.csv']
n=0
for file in datafile:

	city = file.split('-')[0].split('/')[-1]
	res[city]=number_of_trips(file)

	sub=int(res[city][0])
	cus=int(res[city][1])
	if sub > cus:
		print('In City {} Subscriber has made highest trips' .format(city,sub))
	else:
		print('In City {} Subscriber has made highest trips {}' .format(city,cus))


	l=(res[city][2])
	if l > n:
		n=l
		a=city

	
print(a,n)
 
