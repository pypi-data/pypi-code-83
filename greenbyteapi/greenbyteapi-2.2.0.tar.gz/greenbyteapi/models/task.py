# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper
import greenbyteapi.models.user
import greenbyteapi.models.task_category
import greenbyteapi.models.task_comment
import greenbyteapi.models.recurrence
import greenbyteapi.models.metadata_field

class Task(object):

    """Implementation of the 'Task' model.

    A task.

    Attributes:
        task_id (int): The id of a task.
        title (string): TODO: type description here.
        created_by (User): TODO: type description here.
        description (string): TODO: type description here.
        category (TaskCategory): Basic information about a task category.
        priority (TaskPriorityEnum): The priority of a task.
        timestamp_start (datetime): The timestamp when the task is/was planned
            to start. The timestamp is in the time zone configured in the
            Greenbyte Platform without UTC offset.
        timestamp_end (datetime): The timestamp when the is/was planned to
            end. The timestamp is in the time zone configured in the Greenbyte
            Platform without UTC offset.
        state (TaskStateEnum): The state of a task.
        resolved (bool): TODO: type description here.
        timestamp_resolved (datetime): The timestamp when the task was
            resolved. The timestamp is in the time zone configured in the
            Greenbyte Platform without UTC offset.
        device_ids (list of int): Ids of the devices assigned to the task.
        site_ids (list of int): Ids of the sites assigned to the task.
        site_access_ids (list of int): Ids of the site accesses linked to the
            task.
        downtime_event_ids (list of int): Ids of the downtime events linked to
            the task.
        status_ids (list of int): Ids of the statuses linked to the task.
        number_of_comments (int): TODO: type description here.
        comments (list of TaskComment): The comments belonging to the task.
        recurrence (Recurrence): Recurrence settings for the task. To
            calculate when the task is recurring, use the `timestampStart`
            field and then add to it multiples of the specified interval; the
            `intervalType` field determines if the task is recurring on daily,
            weekly, monthly, or yearly basis.  If the task is not recurring,
            this field is null.  **Note:** Only the main (first) task in a
            recurring series have recurrence settings. For the other tasks in
            the series, the field `mainTaskId` can be used to find it.
        main_task_id (int): TODO: type description here.
        assignee (object): TODO: type description here.
        metadata (list of MetadataField): A list of metadata fields and their
            values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "task_id":'taskId',
        "title":'title',
        "created_by":'createdBy',
        "priority":'priority',
        "timestamp_start":'timestampStart',
        "timestamp_end":'timestampEnd',
        "state":'state',
        "resolved":'resolved',
        "number_of_comments":'numberOfComments',
        "description":'description',
        "category":'category',
        "timestamp_resolved":'timestampResolved',
        "device_ids":'deviceIds',
        "site_ids":'siteIds',
        "site_access_ids":'siteAccessIds',
        "downtime_event_ids":'downtimeEventIds',
        "status_ids":'statusIds',
        "comments":'comments',
        "recurrence":'recurrence',
        "main_task_id":'mainTaskId',
        "assignee":'assignee',
        "metadata":'metadata'
    }

    def __init__(self,
                 task_id=None,
                 title=None,
                 created_by=None,
                 priority='medium',
                 timestamp_start=None,
                 timestamp_end=None,
                 state=None,
                 resolved=None,
                 number_of_comments=None,
                 description=None,
                 category=None,
                 timestamp_resolved=None,
                 device_ids=None,
                 site_ids=None,
                 site_access_ids=None,
                 downtime_event_ids=None,
                 status_ids=None,
                 comments=None,
                 recurrence=None,
                 main_task_id=None,
                 assignee=None,
                 metadata=None):
        """Constructor for the Task class"""

        # Initialize members of the class
        self.task_id = task_id
        self.title = title
        self.created_by = created_by
        self.description = description
        self.category = category
        self.priority = priority
        self.timestamp_start = APIHelper.RFC3339DateTime(timestamp_start) if timestamp_start else None
        self.timestamp_end = APIHelper.RFC3339DateTime(timestamp_end) if timestamp_end else None
        self.state = state
        self.resolved = resolved
        self.timestamp_resolved = APIHelper.RFC3339DateTime(timestamp_resolved) if timestamp_resolved else None
        self.device_ids = device_ids
        self.site_ids = site_ids
        self.site_access_ids = site_access_ids
        self.downtime_event_ids = downtime_event_ids
        self.status_ids = status_ids
        self.number_of_comments = number_of_comments
        self.comments = comments
        self.recurrence = recurrence
        self.main_task_id = main_task_id
        self.assignee = assignee
        self.metadata = metadata


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        task_id = dictionary.get('taskId')
        title = dictionary.get('title')
        created_by = greenbyteapi.models.user.User.from_dictionary(dictionary.get('createdBy')) if dictionary.get('createdBy') else None
        priority = dictionary.get("priority") if dictionary.get("priority") else 'medium'
        timestamp_start = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampStart")).datetime if dictionary.get("timestampStart") else None
        timestamp_end = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampEnd")).datetime if dictionary.get("timestampEnd") else None
        state = dictionary.get('state')
        resolved = dictionary.get('resolved')
        number_of_comments = dictionary.get('numberOfComments')
        description = dictionary.get('description')
        category = greenbyteapi.models.task_category.TaskCategory.from_dictionary(dictionary.get('category')) if dictionary.get('category') else None
        timestamp_resolved = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampResolved")).datetime if dictionary.get("timestampResolved") else None
        device_ids = dictionary.get('deviceIds')
        site_ids = dictionary.get('siteIds')
        site_access_ids = dictionary.get('siteAccessIds')
        downtime_event_ids = dictionary.get('downtimeEventIds')
        status_ids = dictionary.get('statusIds')
        comments = None
        if dictionary.get('comments') != None:
            comments = list()
            for structure in dictionary.get('comments'):
                comments.append(greenbyteapi.models.task_comment.TaskComment.from_dictionary(structure))
        recurrence = greenbyteapi.models.recurrence.Recurrence.from_dictionary(dictionary.get('recurrence')) if dictionary.get('recurrence') else None
        main_task_id = dictionary.get('mainTaskId')
        assignee = dictionary.get('assignee')
        metadata = None
        if dictionary.get('metadata') != None:
            metadata = list()
            for structure in dictionary.get('metadata'):
                metadata.append(greenbyteapi.models.metadata_field.MetadataField.from_dictionary(structure))

        # Return an object of this model
        return cls(task_id,
                   title,
                   created_by,
                   priority,
                   timestamp_start,
                   timestamp_end,
                   state,
                   resolved,
                   number_of_comments,
                   description,
                   category,
                   timestamp_resolved,
                   device_ids,
                   site_ids,
                   site_access_ids,
                   downtime_event_ids,
                   status_ids,
                   comments,
                   recurrence,
                   main_task_id,
                   assignee,
                   metadata)


