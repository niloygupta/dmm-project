import unittest
import argparse
from gm_params import *
from gm_sql import *
from math import sqrt
import os
import time
from gm_main import *

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
        degreeDistListTest = {1:1,5:5,6:1}
        degreeDistCheck = True
        i = 0
        for row in rows:
            print row[0]," ",row[1]
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,2)
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
        degreeDistListTest = {129:5,195:7,106:3,120:6,8:111,305:1,80:15,551:1,318:3,1167:1,209:1,276:1,110:3,175:5,99:6,48:30,28:40,732:1,94:10,204:1,362:1,151:4,384:1,162:5,30:30,253:1,399:1,119:7,95:9,270:1,122:11,62:17,275:2,123:3,261:1,214:1,92:11,23:28,127:2,101:9,20:44,44:26,82:10,25:28,58:24,1:2315,484:1,26:36,213:5,189:4,137:6,117:6,185:2,233:1,111:7,206:1,292:2,168:1,136:4,226:2,86:5,218:1,13:66,49:22,309:2,22:38,91:9,363:1,70:20,45:28,238:2,743:2,27:30,225:1,199:3,286:1,230:4,409:1,293:1,543:1,60:25,165:3,618:1,149:3,422:1,93:8,105:5,21:43,97:8,152:2,75:15,124:9,205:1,5:165,281:2,197:1,301:1,187:2,245:1,181:1,114:7,43:22,191:2,156:5,11:85,166:2,386:1,135:3,126:7,228:1,298:1,39:31,537:1,291:1,132:1,254:3,112:10,3:388,131:2,431:1,61:24,176:3,96:7,178:2,67:17,87:12,169:2,14:66,255:3,241:2,464:1,107:7,352:1,17:47,472:1,319:1,66:20,142:3,224:2,147:4,221:1,89:16,160:6,121:11,284:1,50:26,33:26,210:1,161:3,19:36,108:8,157:4,398:1,154:2,109:8,57:31,51:24,215:2,31:33,35:22,65:12,288:1,52:28,76:15,69:15,317:1,334:3,37:25,203:1,173:6,385:1,85:6,34:26,81:16,219:4,32:28,12:91,375:1,188:4,273:1,282:1,10:110,79:12,428:1,42:27,164:1,90:15,481:1,18:54,134:5,146:6,59:15,78:11,139:4,773:1,143:5,192:2,338:1,98:9,193:3,436:1,271:2,279:2,150:7,100:9,243:2,331:1,250:4,158:2,116:8,113:5,172:1,63:14,9:89,183:3,24:37,411:1,184:1,260:1,64:18,170:3,403:1,832:1,55:21,68:17,248:5,84:11,88:7,118:6,145:4,244:1,130:5,38:21,240:2,128:6,223:2,283:2,300:1,207:1,74:11,104:5,163:1,217:2,231:1,6:159,102:9,538:1,212:2,463:1,71:16,29:39,2:640,159:3,72:17,267:1,354:1,41:33,186:4,216:1,177:2,202:1,141:2,266:1,144:5,7:139,402:1,171:3,227:1,280:3,138:2,242:1,297:1,419:1,314:2,190:2,16:52,444:1,274:1,54:23,320:1,426:1,47:28,103:6,115:5,148:2,208:4,322:2,211:3,46:27,368:1,83:6,36:19,15:57,174:1,361:2,77:20,125:5,140:4,4:245,153:2,257:1,200:1,73:15,40:21,182:1,56:17,53:15,277:1,}
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        gm_db_bubye(db_conn)
        self.assertEqual(num_components,24)
        print 'Testing KCore'
        gm_k_decomposition(0)
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("select count(*) from gm_node_degrees")
        cnt = cur.fetchone()[0]
        self.assertEqual(cnt,3513)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,3603)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()

    def testKCore3(self):
        print "\n\nRunning unittest for bipartite.txt...\n"
        initialize(os.getcwd() + '/bipartite.txt',',')
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeDistListTest = {6:1,1:3,2:1,3:1,4:3,5:2}
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        self.assertEqual(cnt,0)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,1)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()
    
    def testKCore4(self):
        print "\n\nRunning unittest for blosson.txt...\n"
        initialize(os.getcwd() + '/blossom.txt',',')
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeDistListTest = {3:6,6:1}
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        self.assertEqual(cnt,0)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,1)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()
        
    def testKCore5(self):
        print "\n\nRunning unittest for chain.txt...\n"
        initialize(os.getcwd() + '/chain.txt',',')
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeDistListTest = {2:8,1:2}
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        self.assertEqual(cnt,0)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,1)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()
        
    def testKCore6(self):
        print "\n\nRunning unittest for pentagon.txt...\n"
        initialize(os.getcwd() + '/pentagon.txt',',')
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeDistListTest = {4:2,5:2,2:1}
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        self.assertEqual(cnt,0)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,1)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()
        
    def testKCore7(self):
        print "\n\nRunning unittest for starfish.txt...\n"
        initialize(os.getcwd() + '/starfish.txt',',')
        db_test_conn = gm_db_initialize()
        cur = db_test_conn.cursor()
        cur.execute("SELECT count(*) from %s" % GM_NODES)
        num_nodes = cur.fetchone()[0] 
        print 'Testing Degree Distribution Components'
        gm_degree_distribution(1)
        cur.execute ("SELECT * FROM %s" % GM_DEGREE_DISTRIBUTION);
        rows = cur.fetchall()
        print "\nShow me the degree distribution:\n"
        degreeDistListTest = {14:1,2:1,3:14}
        degreeDistCheck = True
        i = 0
        for row in rows:
            if(degreeDistListTest.has_key(row[0])==0 or row[1]!=degreeDistListTest[row[0]]):
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
        self.assertEqual(cnt,0)
        cur.execute ("SELECT count(distinct component_id) FROM %s" % GM_CON_COMP)
        num_components = cur.fetchone()[0]
        self.assertEqual(num_components,1)
        cur.close()
        gm_db_bubye(db_test_conn)
        destroy_conn()

if __name__ == '__main__':
    unittest.main()