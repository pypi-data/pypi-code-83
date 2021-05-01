import unittest
from unittest import mock 
from .insinfo import Instanceinfo
from ..util import current_milli_time 


class InsinfoTest(unittest.TestCase):
    
    def setUp(self):
        self.insinfo = Instanceinfo()
    
    def test_update_instance_info(self):
        self.insinfo.update_instance_info(300)
        self.assertEqual(self.insinfo.status,300)
        self.insinfo.update_instance_info(None)
        self.assertEqual(self.insinfo.status,100)


    def test_update_status(self):
        self.insinfo.status = 300
        self.insinfo.update_status(300)
        self.assertEqual(self.insinfo.retry_counter,2)
        self.insinfo.retry_counter =  3*24*60
        self.insinfo.update_status(300)
        self.assertEqual(self.insinfo.status,0)
        

    def test_get_status(self):
        self.assertIn(self.insinfo.get_status(),[100,300,400,200,0])
        
    @mock.patch('pythonapm.collector.insinfo.current_milli_time')
    def test_update_last_reported(self,mock_time):
        time = current_milli_time()
        mock_time.return_value = time
        self.insinfo.update_last_reported()
        self.assertEqual(self.insinfo.last_reported,time)

    @mock.patch('pythonapm.collector.insinfo.current_milli_time')
    def test_get_modiefied_time(self,mock_time):
        time = current_milli_time()
        mock_time.return_value = time
        ins_info = Instanceinfo()
        self.assertEqual(ins_info.get_modiefied_time(),time)

        

    def test_get_retry_counter(self):
        self.insinfo.retry_counter = 1
        self.assertEqual(self.insinfo.get_retry_counter(),1)
    
    def get_last_reported(self):
        time = current_milli_time()
        self.insinfo.last_reported = time
        self.assertEqual(self.insinfo.get_last_reported(),time)