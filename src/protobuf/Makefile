
protoc:
	rm -rf generated/*.python
	python -m grpc_tools.protoc -I ./ --python_out=./generated/ --grpc_python_out=./generated/ *.proto
	sed -i 's/^\(import.*pb2\)/from . \1/g' ./generated/*.py
	cp -rf generated ../time_server/
	cp -rf generated ../edge_server/
	cp -rf generated ../revert_name_server/

