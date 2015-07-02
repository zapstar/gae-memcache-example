from google.appengine.api import memcache
import webapp2
import time

class MainHandler(webapp2.RequestHandler):
    
    def generate_data(self):
        result = 0;
        for i in range(1000000):
            result += i*i
        return result
    
    def get_data(self):
        client = memcache.Client()
        result = client.get('result')
        if result is not None:
            pass
        else:
            result = self.generate_data()
            client.add('result', result, 120)
        return result
        
    
    def get(self):
        t1 = time.time()
        self.response.out.write('Generate Data: ' + str(self.generate_data()) + '<br>')
        t2 = time.time()
        self.response.out.write('Time Taken: ' + str(t2 - t1) + 's<br>')
        
        t3 = time.time()
        self.response.out.write('Memcached Data: ' + str(self.get_data()) + '<br>')
        t4 = time.time()
        self.response.out.write('Time Taken: ' + str(t4 - t3) + 's<br>')

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
