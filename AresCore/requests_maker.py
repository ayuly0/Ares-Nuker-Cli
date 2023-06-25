__import__('sys').append('../')
import queue, global_vars
from AresNuker import Console

console = Console()

requesting = url = headers = payload = ""
headers = global_vars.headers
concurrent = 100
q = Queue(concurrent * 2)

def RequestMaker():
	while True:
		requesting, url, headers, payload = q.get()
		try:
			r = requesting(url, data=json.dumps(payload), headers=headers, timeout=timeout)
			if r.status_code == 429:
				r = r.json()
				if want_log_request:
					if isinstance(r['retry_after'], int): # Discord will return all integer time if the retry after is less then 10 seconds which is in miliseconds.
						r['retry_after'] /= 1000
					if r['retry_after'] > 5:
						console.log(f'Rate limiting has been reached, and this request has been cancelled due to retry-after time is greater than 5 seconds: Wait {str(r["retry_after"])} more seconds.')
						q.task_done()
						continue
					console.log(f'Rate limiting has been reached: Wait {str(r["retry_after"])} more seconds.')
				q.put((requesting, url, headers, payload))
			elif want_log_request and 'code' in r:
				console.log('Request cancelled due to -> ' + r['message'])
		except json.decoder.JSONDecodeError:
			pass
		except requests.exceptions.ConnectTimeout:
			console.log(f'Reached maximum load time: timeout is {timeout} seconds long {proxy}')
			q.put((requesting, url, headers, payload))
		except Exception as e:
			console.log(f'Unexpected error: {str(e)}')

		q.task_done()

def StartRequestMaker():
	for i in range(concurrent):
		Thread(target=RequestMaker, daemon=True).start()