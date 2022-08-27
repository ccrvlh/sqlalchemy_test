drop:
	curl -X DELETE http://localhost:8000/db | jq

create:
	curl -X POST http://localhost:8000/db | jq

get:
	curl http://localhost:8000/data | jq

init:
	curl -X POST http://localhost:8000/data | jq

locals:
	curl -X POST http://localhost:8000/locals | jq


all: drop create init