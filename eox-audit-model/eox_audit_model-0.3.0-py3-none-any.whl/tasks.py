"""Tasks file.

Methods:
    create_audit_register: Create an AuditModel register with AuditNotes.
"""
from celery import shared_task


@shared_task
def create_audit_register(
    action,
    status,
    method_name,
    captured_logs,
    traceback_log,
    input_parameters,
    output_parameters,
    notes,
):
    """Allow to create an Audit model register asynchronously by using the given parameters

    Arguments:
        action: <Str> Action name identifier.
        status: <Status> Status constant from eox_audit_model.constants
        method_name: <Str> Method string name.
        captured_logs: <Str> Generated logs during the method execution.
        traceback_log: <Str> Traceback generated when the method fails,
        input_parameters: <Dict> Method input.
        output_parameters: <Dict> Method output.
        notes: <List> List of dict, with the notes information.
    """
    from eox_audit_model.models import AuditModel, AuditNote

    audit_register = AuditModel.objects.create(
        action=action,
        status=status,
        method_name=method_name,
        captured_logs=captured_logs,
        traceback_log=traceback_log,
        input_parameters=input_parameters,
        output_parameters=output_parameters,
    )

    if notes and isinstance(notes, list):
        for note in notes:
            AuditNote.objects.create(
                audit_register=audit_register,
                title=note.get('title', 'Missing Title'),
                description=note.get('description', 'Missing description'),
            )
