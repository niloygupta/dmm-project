all:    
	#chmod a+rwx `pwd`
	#python gm_main.py --file `pwd`/bigData.txt --dest_dir `pwd`/output --belief_file `pwd`/priorsbelief.txt --unweighted --undirected --index_type btree
	#python gm_main.py --file `pwd`/bigData.txt --dest_dir `pwd`/output --belief_file `pwd`/priorsbelief.txt --unweighted --undirected --index_type hash
	#python gm_main.py --file `pwd`/ca-AstroPhDelim.txt --dest_dir `pwd`/output --belief_file `pwd`/priorsbelief.txt  --unweighted --undirected --index_type btree
	python gm_main.py --file `pwd`/cit-HepPhDelim.txt --dest_dir `pwd`/cit-HepPhDelimoutput --belief_file `pwd`/priorsbelief.txt  --unweighted --undirected --index_type hash
	python gm_main.py --file `pwd`/cit-HepThDelim.txt --dest_dir `pwd`/cit-HepThDelimoutput --belief_file `pwd`/priorsbelief.txt  --unweighted --undirected --index_type hash
	python gm_main.py --file `pwd`/com-amazon.ungraph-75000.txt --dest_dir `pwd`/comAmazonoutput --belief_file `pwd`/priorsbelief.txt  --unweighted --undirected --index_type hash
	python gm_main.py --file `pwd`/as-skitter.ungraph-75000.txt --dest_dir `pwd`/skitteroutput --belief_file `pwd`/priorsbelief.txt  --unweighted --undirected --index_type hash
	
install:
	sudo apt-get install python-psycopg2

all.tar:
	tar -zcvf graphminer.tar.gz *.txt makefile *.py matlab output doc

clean:
	rm *.pyc


