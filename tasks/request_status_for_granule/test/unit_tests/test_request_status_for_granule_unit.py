"""
Name: test_request_status_for_granule_unit.py

Description:  Unit tests for request_status_for_granule.py.
"""
import copy
import json
import unittest
import uuid
from http import HTTPStatus
from unittest import mock
from unittest.mock import MagicMock, patch, Mock
import fastjsonschema

import database
import requests_db

import request_status_for_granule


class TestRequestStatusForGranuleUnit(
    unittest.TestCase
):  # pylint: disable-msg=too-many-instance-attributes
    """
    TestRequestStatusForGranule.
    """

    # noinspection PyPep8Naming
    @patch("requests_db.get_dbconnect_info")
    @patch("request_status_for_granule.task")
    @patch("cumulus_logger.CumulusLogger.setMetadata")
    def test_handler_happy_path(
        self,
        mock_setMetadata: MagicMock,
        mock_task: MagicMock,
        mock_get_dbconnect_info: MagicMock,
    ):
        """
        Basic path with all information present.
        """
        granule_id = uuid.uuid4().__str__()
        async_operation_id = uuid.uuid4().__str__()

        event = {
            request_status_for_granule.INPUT_GRANULE_ID_KEY: granule_id,
            request_status_for_granule.INPUT_JOB_ID_KEY: async_operation_id,
        }
        context = Mock()
        result = request_status_for_granule.handler(event, context)

        mock_setMetadata.assert_called_once_with(event, context)
        mock_task.assert_called_once_with(
            granule_id,
            mock_get_dbconnect_info.return_value,
            context.aws_request_id,
            async_operation_id,
        )
        self.assertEqual(mock_task.return_value, result)

    @patch("request_status_for_granule.task")
    @patch("requests_db.get_dbconnect_info")
    def test_handler_async_operation_id_defaults_to_none(
        self, mock_get_dbconnect_info: MagicMock, mock_task: MagicMock
    ):
        """
        If asyncOperationId is missing, it should default to null.
        """
        granule_id = uuid.uuid4().__str__()

        event = {request_status_for_granule.INPUT_GRANULE_ID_KEY: granule_id}
        context = Mock()
        result = request_status_for_granule.handler(event, context)

        mock_task.assert_called_once_with(
            granule_id,
            mock_get_dbconnect_info.return_value,
            context.aws_request_id,
            None,
        )
        self.assertEqual(mock_task.return_value, result)

    # noinspection PyPep8Naming
    @patch("cumulus_logger.CumulusLogger.error")
    @patch("requests_db.get_dbconnect_info")
    @patch("cumulus_logger.CumulusLogger.setMetadata")
    def test_handler_missing_granule_id_returns_error_code(
        self,
        mock_setMetadata: MagicMock,
        mock_get_dbconnect_info: MagicMock,
        mock_cumulus_logger_error,
    ):
        """
        If granule_id is missing, error dictionary should be returned.
        """
        async_operation_id = uuid.uuid4().__str__()

        event = {request_status_for_granule.INPUT_JOB_ID_KEY: async_operation_id}
        context = Mock()
        context.aws_request_id = Mock()

        result = request_status_for_granule.handler(event, context)
        self.assertEqual(HTTPStatus.BAD_REQUEST, result["httpStatus"])

    # noinspection PyPep8Naming
    @patch("cumulus_logger.CumulusLogger.error")
    @patch("request_status_for_granule.task")
    @patch("requests_db.get_dbconnect_info")
    @patch("cumulus_logger.CumulusLogger.setMetadata")
    def test_handler_database_error_returns_error_code(
        self,
        mock_setMetadata: MagicMock,
        mock_get_dbconnect_info: MagicMock,
        mock_task: MagicMock,
        mock_cumulus_logger_error: MagicMock,
    ):
        """
        If database error is raised, it should be caught and returned in a dictionary.
        """
        async_operation_id = uuid.uuid4().__str__()
        granule_id = uuid.uuid4().__str__()

        event = {
            request_status_for_granule.INPUT_JOB_ID_KEY: async_operation_id,
            request_status_for_granule.INPUT_GRANULE_ID_KEY: granule_id,
        }
        context = Mock()
        mock_task.side_effect = requests_db.DatabaseError()

        result = request_status_for_granule.handler(event, context)
        self.assertEqual(HTTPStatus.INTERNAL_SERVER_ERROR, result["httpStatus"])

    def test_task_granule_id_cannot_be_none(self):
        """
        Raises error if granule_id is None.
        """
        try:
            request_status_for_granule.task(None, uuid.uuid4().__str__(), Mock())
        except ValueError:
            return
        self.fail("Error not raised.")

    @patch("request_status_for_granule.get_job_entry_for_granule")
    @patch("request_status_for_granule.get_file_entries_for_granule_in_job")
    def test_task_job_id_present_does_not_re_get(
        self,
        mock_get_file_entries_for_granule_in_job: MagicMock,
        mock_get_job_entry_for_granule: MagicMock,
    ):
        """
        If job_id is given, then it should not take a separate request to get it.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()
        request_id = uuid.uuid4().__str__()

        db_connect_info = Mock()

        job_entry = {
            request_status_for_granule.OUTPUT_JOB_ID_KEY: job_id,
            request_status_for_granule.OUTPUT_COMPLETION_TIME_KEY: "1999-01-31 09:26:56.66 +02:00",  # todo: utc?
        }
        mock_get_job_entry_for_granule.return_value = copy.deepcopy(job_entry)

        file_entries = [
            {
                request_status_for_granule.OUTPUT_ERROR_MESSAGE_KEY: "Something went boom."
            }
        ]
        mock_get_file_entries_for_granule_in_job.return_value = copy.deepcopy(
            file_entries
        )

        result = request_status_for_granule.task(
            granule_id, db_connect_info, request_id, job_id
        )

        mock_get_file_entries_for_granule_in_job.assert_called_once_with(
            granule_id, job_id, db_connect_info
        )
        mock_get_job_entry_for_granule.assert_called_once_with(
            granule_id, job_id, db_connect_info
        )

        expected = job_entry
        expected[request_status_for_granule.OUTPUT_FILES_KEY] = file_entries
        self.assertEqual(expected, result)

    @patch("request_status_for_granule.get_most_recent_job_id_for_granule")
    @patch("request_status_for_granule.get_job_entry_for_granule")
    @patch("request_status_for_granule.get_file_entries_for_granule_in_job")
    def test_task_no_job_id_gets(
        self,
        mock_get_file_entries_for_granule_in_job: MagicMock,
        mock_get_job_entry_for_granule: MagicMock,
        mock_get_most_recent_job_id_for_granule: MagicMock,
    ):
        """
        If job_id is not given, then it should take a separate request to get it.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()
        request_id = uuid.uuid4().__str__()

        db_connect_info = Mock()

        mock_get_most_recent_job_id_for_granule.return_value = job_id

        job_entry = {
            request_status_for_granule.OUTPUT_JOB_ID_KEY: job_id,
            request_status_for_granule.OUTPUT_COMPLETION_TIME_KEY: None,
        }
        mock_get_job_entry_for_granule.return_value = copy.deepcopy(job_entry)

        file_entries = [{request_status_for_granule.OUTPUT_ERROR_MESSAGE_KEY: None}]
        mock_get_file_entries_for_granule_in_job.return_value = copy.deepcopy(
            file_entries
        )

        result = request_status_for_granule.task(
            granule_id, db_connect_info, request_id, None
        )

        mock_get_most_recent_job_id_for_granule.assert_called_once_with(
            granule_id, db_connect_info
        )
        mock_get_file_entries_for_granule_in_job.assert_called_once_with(
            granule_id, job_id, db_connect_info
        )
        mock_get_job_entry_for_granule.assert_called_once_with(
            granule_id, job_id, db_connect_info
        )

        expected = job_entry
        del expected[request_status_for_granule.OUTPUT_COMPLETION_TIME_KEY]
        expected[request_status_for_granule.OUTPUT_FILES_KEY] = [
            {},
        ]
        self.assertEqual(expected, result)

    @patch("request_status_for_granule.create_http_error_dict")
    @patch("request_status_for_granule.get_most_recent_job_id_for_granule")
    def test_task_no_job_id_job_not_found_returns_error(
        self,
        mock_get_most_recent_job_id_for_granule: MagicMock,
        mock_create_http_error_dict: MagicMock,
    ):
        """
        If job_id is not given, and no valid job id is found, return 404.
        """
        granule_id = uuid.uuid4().__str__()
        request_id = uuid.uuid4().__str__()

        db_connect_info = Mock()

        mock_get_most_recent_job_id_for_granule.return_value = None

        result = request_status_for_granule.task(
            granule_id, db_connect_info, request_id, None
        )

        mock_get_most_recent_job_id_for_granule.assert_called_once_with(
            granule_id, db_connect_info
        )

        mock_create_http_error_dict.assert_called_once_with(
            "NotFound", HTTPStatus.NOT_FOUND, request_id, mock.ANY
        )
        self.assertEqual(mock_create_http_error_dict.return_value, result)

    @patch("request_status_for_granule.create_http_error_dict")
    @patch("request_status_for_granule.get_job_entry_for_granule")
    def test_task_job_for_granule_and_job_id_not_found_returns_error(
        self,
        mock_get_job_entry_for_granule: MagicMock,
        mock_create_http_error_dict: MagicMock,
    ):
        """
        If the job_id+granule_id does not point to an entry, return 404.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()
        request_id = uuid.uuid4().__str__()

        db_connect_info = Mock()

        mock_get_job_entry_for_granule.return_value = None

        result = request_status_for_granule.task(
            granule_id, db_connect_info, request_id, job_id
        )

        mock_get_job_entry_for_granule.assert_called_once_with(
            granule_id, job_id, db_connect_info
        )

        mock_create_http_error_dict.assert_called_once_with(
            "NotFound", HTTPStatus.NOT_FOUND, request_id, mock.ANY
        )
        self.assertEqual(mock_create_http_error_dict.return_value, result)

    @patch("database.result_to_json")
    @patch("database.single_query")
    def test_get_most_recent_job_id_for_granule_happy_path(
        self, mock_single_query: MagicMock, mock_result_to_json: MagicMock
    ):
        """
        Basic path with all information present.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()

        mock_result_to_json.return_value = {"job_id": job_id}
        db_connect_info = Mock()

        row = Mock()
        mock_single_query.return_value = [row]

        result = request_status_for_granule.get_most_recent_job_id_for_granule(
            granule_id, db_connect_info
        )

        mock_single_query.assert_called_once_with(
            f"""
            SELECT
                job_id
            FROM
                orca_recoveryjob
            WHERE
                granule_id = %s
            ORDER BY
                 request_time DESC
            LIMIT 1""",
            db_connect_info,
            (granule_id,),
        )
        mock_result_to_json.assert_called_once_with(row)

        self.assertEqual(job_id, result)

    @patch("database.single_query")
    def test_get_most_recent_job_id_for_granule_error_wrapped_in_database_error(
        self, mock_single_query: MagicMock
    ):
        """
        If error is raised when contacting DB, error should be raised as a DatabaseError.
        """
        granule_id = uuid.uuid4().__str__()
        db_connect_info = Mock()

        mock_single_query.side_effect = database.DbError()

        with self.assertRaises(request_status_for_granule.DatabaseError):
            request_status_for_granule.get_most_recent_job_id_for_granule(
                granule_id, db_connect_info
            )

    @patch("database.result_to_json")
    @patch("database.single_query")
    def test_get_job_entry_for_granule_happy_path(
        self, mock_single_query: MagicMock, mock_result_to_json: MagicMock
    ):
        """
        Basic path with all information present.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()

        db_connect_info = Mock()

        row = Mock()

        mock_single_query.return_value = [row]

        result = request_status_for_granule.get_job_entry_for_granule(
            granule_id, job_id, db_connect_info
        )

        mock_single_query.assert_called_once_with(
            f"""
            SELECT
                granule_id as "{request_status_for_granule.OUTPUT_GRANULE_ID_KEY}",
                job_id as "{request_status_for_granule.OUTPUT_JOB_ID_KEY}",
                request_time as "{request_status_for_granule.OUTPUT_REQUEST_TIME_KEY}",
                completion_time as "{request_status_for_granule.OUTPUT_COMPLETION_TIME_KEY}"
            FROM
                orca_recoveryjob
            WHERE
                granule_id = %s AND job_id = %s""",
            db_connect_info,
            (
                granule_id,
                job_id,
            ),
        )
        mock_result_to_json.assert_called_once_with(row)

        self.assertEqual(mock_result_to_json.return_value, result)

    @patch("database.single_query")
    def test_get_job_entry_for_granule_error_wrapped_in_database_error(
        self, mock_single_query: MagicMock
    ):
        """
        If error is raised when contacting DB, error should be raised as a DatabaseError.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()
        db_connect_info = Mock()

        mock_single_query.side_effect = database.DbError()

        with self.assertRaises(request_status_for_granule.DatabaseError):
            request_status_for_granule.get_job_entry_for_granule(
                granule_id, job_id, db_connect_info
            )

    @patch("database.result_to_json")
    @patch("database.single_query")
    def test_get_file_entries_for_granule_in_job_happy_path(
        self, mock_single_query: MagicMock, mock_result_to_json: MagicMock
    ):
        """
        Basic path with all information present.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()

        mock_result_to_json.return_value = {"job_id": job_id}
        db_connect_info = Mock()

        result = request_status_for_granule.get_file_entries_for_granule_in_job(
            granule_id, job_id, db_connect_info
        )

        mock_single_query.assert_called_once_with(
            f"""
            SELECT
                orca_recoverfile.filename AS "{request_status_for_granule.OUTPUT_FILENAME_KEY}",
                orca_recoverfile.restore_destination AS "{request_status_for_granule.OUTPUT_RESTORE_DESTINATION_KEY}",
                orca_status.value AS "{request_status_for_granule.OUTPUT_STATUS_KEY}",
                orca_recoverfile.error_message as "{request_status_for_granule.OUTPUT_ERROR_MESSAGE_KEY}"
            FROM
                orca_recoverfile
            JOIN orca_status ON orca_recoverfile.status_id=orca_status.id
            WHERE
                granule_id = %s AND job_id = %s
            ORDER BY filename desc""",
            db_connect_info,
            (
                granule_id,
                job_id,
            ),
        )
        mock_result_to_json.assert_called_once_with(mock_single_query.return_value)

        self.assertEqual(mock_result_to_json.return_value, result)

    @patch("database.single_query")
    def test_get_file_entries_for_granule_in_job_error_wrapped_in_database_error(
        self, mock_single_query: MagicMock
    ):
        """
        If error is raised when contacting DB, error should be raised as a DatabaseError
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()
        db_connect_info = Mock()

        mock_single_query.side_effect = database.DbError()

        with self.assertRaises(request_status_for_granule.DatabaseError):
            request_status_for_granule.get_file_entries_for_granule_in_job(
                granule_id, job_id, db_connect_info
            )

    # Multi-Function Tests:
    @patch("database.single_query")
    def test_task_output_json_schema(self, mock_single_query: MagicMock):
        """
        Checks a realistic output against the output.json.
        """
        granule_id = uuid.uuid4().__str__()
        job_id = uuid.uuid4().__str__()
        request_id = uuid.uuid4().__str__()

        db_connect_info = Mock()

        mock_single_query.side_effect = [
            # job
            [
                {
                    request_status_for_granule.OUTPUT_GRANULE_ID_KEY: granule_id,
                    request_status_for_granule.OUTPUT_JOB_ID_KEY: job_id,
                    request_status_for_granule.OUTPUT_REQUEST_TIME_KEY: "2019-07-17T17:36:38.494918+00:00",
                    request_status_for_granule.OUTPUT_COMPLETION_TIME_KEY: None,
                }
            ],
            # files
            [
                {
                    request_status_for_granule.OUTPUT_FILENAME_KEY: uuid.uuid4().__str__()
                    + ".ext",
                    request_status_for_granule.OUTPUT_RESTORE_DESTINATION_KEY: uuid.uuid4().__str__(),
                    request_status_for_granule.OUTPUT_STATUS_KEY: "failed",
                    request_status_for_granule.OUTPUT_ERROR_MESSAGE_KEY: "some error message",
                },
                {
                    request_status_for_granule.OUTPUT_FILENAME_KEY: uuid.uuid4().__str__()
                    + ".ext",
                    request_status_for_granule.OUTPUT_RESTORE_DESTINATION_KEY: uuid.uuid4().__str__(),
                    request_status_for_granule.OUTPUT_STATUS_KEY: "staged",
                    request_status_for_granule.OUTPUT_ERROR_MESSAGE_KEY: None,
                },
            ],
        ]

        result = request_status_for_granule.task(
            granule_id, db_connect_info, request_id, job_id
        )

        with open("schemas/output.json", "r") as raw_schema:
            schema = json.loads(raw_schema.read())

        validate = fastjsonschema.compile(schema)
        validate(result)
