import unittest
import Agent1

class TestConnectingMethod(unittest.TestCase):
#        def test_payloadsend(self):
 #               self.assertEqual(True, taskCompleted)

	
	def check_retrieve_payload(self):
		url='https://jsonplaceholder.typicode.com'
		param='/posts/1'
		response = urllib.request.urlopen(url+param)
		payload = response.read()
		post = retrievePayload() 
		self.assertEqual(post,payload)

if __name__=='__main__':
        unittest.main()

