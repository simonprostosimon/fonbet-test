# fonbet-test

Language: python 3.5 


## Docker

Build
```
docker build -t fonbet_test . 
```

Run
```
docker run -it -p YOUR_HOST:YOUR_PORT:80 fonbet
```

!Important: With default project configuration supported only only one container (because container creates it's own MongoDB)
