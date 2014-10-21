from gm_main import *
import unittest
import argparse

from gm_params import *
from gm_sql import *
from math import sqrt
import os
import time

class TestGM_Main(unittest.TestCase):
    
    def testKCore1(self):
        print "\n\nRunning unittest for sampleGraph.txt...\n"
        initialize(os.getcwd() + '/samplegraph.txt',',')
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeListTest = [1,5,6]
        distributionListTest = [1,5,1]
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(row[0]!=degreeListTest[i] or row[1]!=distributionListTest[i]):
                degreeDistCheck = False
                break
            i = i+1
        self.assertEqual(True,degreeDistCheck)
        print 'Testing Connected Components'
        gm_connected_components(num_nodes)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        print num_components
        cur.close()
        gm_db_bubye(db_test_conn)
        self.assertEqual(num_components,1)
        print 'Testing KCore'
        gm_k_decomposition(0)
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("select count(*) from gm_node_degrees")
        cnt = cur.fetchone()[0]
        self.assertEqual(cnt,6)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()
        
    def testKCore2(self):
        print "\n\nRunning unittest for bigData.txt...\n"
        initialize(os.getcwd() + '/bigData.txt',',')
        db_conn = gm_db_initialize()
        cur = db_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeListTest = [1,5,6]
        distributionListTest = [1,5,1]
        degreeDistCheck = True
        i = 0
        """for row in rows:
            print " ",row[0]," ",row[1]
            if(row[0]!=degreeListTest[i] or row[1]!=distributionListTest[i]):
                degreeDistCheck = False
                break
            i = i+1
        self.assertEqual(True,degreeDistCheck)"""
        print 'Testing Connected Components'
        gm_connected_components(num_nodes)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        print num_components
        cur.close()
        gm_db_bubye(db_conn)
        self.assertEqual(num_components,24)
        print 'Testing KCore'
        gm_k_decomposition(0)
        db_conn = gm_db_initialize()
        cur = db_conn.cursor()
        cur.execute("select count(*) from gm_node_degrees")
        cnt = cur.fetchone()[0]
        self.assertEqual(cnt,3513)
        gm_db_bubye(db_conn)

if __name__ == '__main__':
    unittest.main()