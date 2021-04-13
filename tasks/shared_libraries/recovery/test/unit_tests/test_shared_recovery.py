"""
Name: test_shared_recovery.py
Description: Shared library that combines common functions and classes needed for recovery operations.
"""
import boto3
import json
from moto import mock_sqs
import shared_recovery
import unittest

# from unittest.mock import MagicMock, patch, Mock


class TestSharedRecoveryLibraries(unittest.TestCase):
    """
    Unit tests for the shared_recover library used by ORCA Recovery Lambdas.
    """

    # Create the mock for unit tests
    mock_sqs = mock_sqs()

    def setUp(self):
        """
        Perform initial setup for the tests.
        """
        self.mock_sqs.start()

    def tearDown(self):
        """
        Perform teardown for the tests
        """
        self.mock_sqs.stop()

    def test_post_entry_to_queue(self):
        """
        Test that sending a message to SQS queue using post_entry_to_queue() function returns the same expected message.
        """
        test_sqs = boto3.resource("sqs")
        queue = test_sqs.create_queue(QueueName="uni-test-queue.fifo")
        table_name = "unit_test_table"
        request_method = shared_recovery.RequestMethod.NEW
        db_queue_url = queue.url
        #this is the expected message body that should be received
        new_data = {"name": "unit_test"}
        
        shared_recovery.post_entry_to_queue(
            table_name, new_data, request_method, db_queue_url
        )
        #grabbing queue contents after the message is sent
        queue_contents = queue.receive_messages()
        self.assertEqual(queue_contents[0].body, json.dumps(new_data))
# ---------------------------------------------------------------------------------------------------------------------------------

    def test_post_status_for_file_to_queue_optional_none(self):
        """
        Test that sending a message to SQS queue using post_status_for_file_to_queue() function returns the same expected message.
        The optional variables are all set to None.
        """
        test_sqs = boto3.resource("sqs")
        queue = test_sqs.create_queue(QueueName="uni-test-queue.fifo")
        request_method = shared_recovery.RequestMethod.NEW
        job_id= '1234'
        granule_id= '6c8d0c8b-4f9a-4d87-ab7c-480b185a0250'
        filename= 'f1.doc'
        status_id = shared_recovery.OrcaStatus.PENDING
        request_method = shared_recovery.RequestMethod.NEW
        key_path= None
        restore_destination = None
        error_message = None
        request_time = None
        last_update =None
        completion_time = None
        db_queue_url = queue.url
        #this is the expected message body that should be received
        new_data = {"job_id": job_id, "granule_id": granule_id, "filename": filename}

        shared_recovery.post_status_for_file_to_queue(
            job_id,granule_id,filename,key_path,restore_destination,status_id,error_message,
            request_time,last_update,completion_time,request_method,db_queue_url
            )
        #grabbing queue contents after the message is sent
        queue_contents = queue.receive_messages()

        self.assertEqual(queue_contents[0].body, json.dumps(new_data))
# ---------------------------------------------------------------------------------------------------------------------------------

    def test_post_status_for_file_to_queue_no_null(self):
        """
        Test that sending a message to SQS queue using post_status_for_file_to_queue() function returns the same expected message.
        The optional variables are all set to non-null values.
        """
        test_sqs = boto3.resource("sqs")
        queue = test_sqs.create_queue(QueueName="uni-test-queue.fifo")
        request_method = shared_recovery.RequestMethod.NEW
        job_id= '1234'
        granule_id= '6c8d0c8b-4f9a-4d87-ab7c-480b185a0250'
        filename= 'f1.doc'
        status_id = shared_recovery.OrcaStatus.PENDING
        request_method = shared_recovery.RequestMethod.NEW
        key_path= key_path= 's3://dev-usgs'
        restore_destination = 'dev-usgs-bucket'
        error_message = 'Access Denied'
        request_time = '2019-07-17T17:36:38.494918'
        last_update = '2020-07-17T17:36:38.494918'
        completion_time = '2019-07-18T17:36:38.494918'
        db_queue_url = queue.url
        #this is the expected message body that should be received
        new_data = {"job_id": job_id, "granule_id": granule_id, "filename": filename, "key_path": key_path, 
                            "restore_destination": restore_destination, "error_message": error_message, "request_time": request_time, "last_update": last_update,
                            "completion_time": completion_time}

        shared_recovery.post_status_for_file_to_queue(
            job_id,granule_id,filename,key_path,restore_destination,status_id,error_message,request_time,last_update,completion_time,request_method,db_queue_url)
        #grabbing queue contents after the message is sent
        queue_contents = queue.receive_messages()

        self.assertEqual(queue_contents[0].body, json.dumps(new_data))

# ---------------------------------------------------------------------------------------------------------------------------------

    def test_post_status_for_job_to_queue_all_null(self):
            """
            Test that sending a message to SQS queue using post_status_for_job_to_queue() function returns the same expected message.
            The optional variables are all set to None.
            """
            test_sqs = boto3.resource("sqs")
            queue = test_sqs.create_queue(QueueName="uni-test-queue.fifo")
            request_method = shared_recovery.RequestMethod.NEW
            job_id= '1234'
            granule_id= '6c8d0c8b-4f9a-4d87-ab7c-480b185a0250'
            status_id = shared_recovery.OrcaStatus.PENDING
            request_method = shared_recovery.RequestMethod.NEW
            archive_destination = None
            request_time = None
            completion_time = None
            db_queue_url = queue.url
            #this is the expected message body that should be received
            new_data = {"job_id": job_id, "granule_id": granule_id}

            shared_recovery.post_status_for_job_to_queue(
                job_id,granule_id,status_id,
                request_time,completion_time,archive_destination,request_method,db_queue_url
                )
            #grabbing queue contents after the message is sent
            queue_contents = queue.receive_messages()

            self.assertEqual(queue_contents[0].body, json.dumps(new_data))

# ---------------------------------------------------------------------------------------------------------------------------------

    def test_post_status_for_job_to_queue_no_null(self):
            """
            Test that sending a message to SQS queue using post_status_for_job_to_queue() function returns the same expected message.
            The optional variables are all set to non-nullable values.
            """
            test_sqs = boto3.resource("sqs")
            queue = test_sqs.create_queue(QueueName="uni-test-queue.fifo")
            request_method = shared_recovery.RequestMethod.NEW
            job_id= '1234'
            granule_id= '6c8d0c8b-4f9a-4d87-ab7c-480b185a0250'
            status_id = shared_recovery.OrcaStatus.PENDING
            request_method = shared_recovery.RequestMethod.NEW
            archive_destination = 'archive-destination'
            request_time = '2019-07-17T17:36:38.494918'
            completion_time = '2019-07-18T17:36:38.494918'
            db_queue_url = queue.url
            #this is the expected message body that should be received
            new_data = {"job_id": job_id, "granule_id": granule_id, "request_time": request_time, 
                        "completion_time": completion_time, "archive_destination": archive_destination }

            shared_recovery.post_status_for_job_to_queue(
                job_id,granule_id,status_id,
                request_time,completion_time,archive_destination,request_method,db_queue_url
                )
            #grabbing queue contents after the message is sent
            queue_contents = queue.receive_messages()

            self.assertEqual(queue_contents[0].body, json.dumps(new_data))

if __name__ == "__main":
    unittest.main()