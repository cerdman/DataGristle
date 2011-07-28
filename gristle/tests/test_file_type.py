#!/usr/bin/env python
#  See the file "LICENSE" for the full license governing this code. 

import sys
import os
import tempfile
import random
import unittest

sys.path.append('../')
import file_type  as mod


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestQuotedCSV))
    suite.addTest(unittest.makeSuite(TestNonQuotedCSV))
    suite.addTest(unittest.makeSuite(TestInternals))

    return suite



def generate_test_file1(delim, quoting, record_cnt):
    (fd, fqfn) = tempfile.mkstemp()
    fp = os.fdopen(fd,"w") 
    name_list = ['smith','jones','thompson','ritchie']
    role_list = ['pm','programmer','dba','sysadmin','qa','manager']
    proj_list = ['cads53','jefta','norma','us-cepa']
 
    for i in range(record_cnt):
        name = random.choice(name_list)
        role = random.choice(role_list)
        proj = random.choice(proj_list)
        if quoting is True:
           name = '"' + name + '"'
           role = '"' + role + '"'
           proj = '"' + proj + '"'
        record = '''%(i)s%(delim)s%(proj)s%(delim)s%(role)s%(delim)s%(name)s\n''' % locals()
        fp.write(record)

    fp.close()
    return fqfn



class TestQuotedCSV(unittest.TestCase):

    def setUp(self):
        self.record_cnt = 100
        self.delimiter     = '|'
        self.quoting       = True
        self.test1_fqfn = generate_test_file1(self.delimiter, self.quoting, self.record_cnt)
        self.MyTest     = mod.FileTyper(self.test1_fqfn, None, None, None)
        self.MyTest.analyze_file()

    def tearDown(self):
        os.remove(self.test1_fqfn)

    def test_file_a01_Misc(self):
        assert(self.MyTest.record_cnt == self.record_cnt)
        assert(self.MyTest.field_cnt == 4)
        assert(self.MyTest.format_type == 'csv')
        assert(self.MyTest.dialect.delimiter == self.delimiter)
        print 
        print 'csv quoting test: '
        print self.MyTest.csv_quoting 
        assert(self.MyTest.csv_quoting == self.quoting)


class TestNonQuotedCSV(unittest.TestCase):

    def setUp(self):
        self.record_cnt = 100
        self.delimiter     = '|'
        self.quoting       = True
        self.test1_fqfn = generate_test_file1(self.delimiter, self.quoting, 
                          self.record_cnt)
        self.MyTest     = mod.FileTyper(self.test1_fqfn, None, None, None)
        self.MyTest.analyze_file()

    def tearDown(self):
        os.remove(self.test1_fqfn)

    def test_file_b01_Misc(self):
        assert(self.MyTest.record_cnt == self.record_cnt)
        assert(self.MyTest.field_cnt == 4)
        assert(self.MyTest.format_type == 'csv')
        assert(self.MyTest.dialect.delimiter == self.delimiter)
        assert(self.MyTest.csv_quoting == self.quoting)


class TestInternals(unittest.TestCase):

    def setUp(self):
        self.record_cnt = 100
        self.delimiter     = '|'
        self.quoting       = False
        self.test1_fqfn = generate_test_file1(self.delimiter, self.quoting, 
                          self.record_cnt)
        self.MyTest     = mod.FileTyper(self.test1_fqfn, None, None, None)
        self.MyTest.analyze_file()

    def tearDown(self):
        os.remove(self.test1_fqfn)

    def test_file_c01_RecordNumber(self):
        assert(self.MyTest._count_records() == self.record_cnt)

    def test_file_c02_FormatType(self):
        assert(self.MyTest._get_format_type() == 'csv')


if __name__ == "__main__":
    unittest.main()

