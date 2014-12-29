import time
from dateutil.parser import parse

print parse('Wed, 07-Oct-2012 12:08:00 GMT').strftime('%s')
print parse('Wed, 07-Oct-2012 12:08:00 GMT')

print time.time()
