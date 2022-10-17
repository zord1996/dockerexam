def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World!"]

def main():
  print("Hello World!")
if __name__== "__main__":
  main()
