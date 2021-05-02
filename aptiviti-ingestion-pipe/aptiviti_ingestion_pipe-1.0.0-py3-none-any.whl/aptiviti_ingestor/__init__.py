import analytics

class aptiviti_data_ingestor:

    write_key = None

    def __init__(self, write_key, parameters = None):
        if write_key == None:
            raise Exception('No write key defined')
        self.write_key = write_key
        
        analytics.on_error = self.error_handler

        if parameters != None and 'debug' in parameters:
            analytics.debug = parameters.debug

    def set_write_key(self, write_key=None):
        write_key = write_key

    def identify(self, user_id=None, traits=None, context=None, timestamp=None, anonymous_id=None, integrations=None):
        analytics.identify(user_id, traits, context, timestamp, anonymous_id, integrations)

    def track(self, user_id=None, event=None, properties=None, context=None, timestamp=None, anonymous_id=None, integrations=None):
        analytics.track(user_id, event, properties, context, timestamp, anonymous_id, integrations)

    def page(self, user_id=None, category=None, name=None, properties=None, context=None, timestamp=None, anonymous_id=None, integrations=None):
        analytics.page(user_id, category, name, properties, context, timestamp, anonymous_id, integrations)

    def screen(self, user_id=None, category=None, name=None, properties=None, context=None, timestamp=None, anonymous_id=None, integrations=None):
        analytics.screen(user_id, category, name, properties, context, timestamp, anonymous_id, integrations)

    def group(self, user_id=None, group_id=None, traits=None, context=None, timestamp=None, anonymous_id=None, integrations=None):
        analytics.group(user_id, group_id, traits, context, timestamp, anonymous_id, integrations)

    def alias(self, previous_id=None, user_id=None, context=None, timestamp=None, integrations=None):
        analytics.alias(previous_id, user_id, context, timestamp, integrations)

    def flush(self):
        analytics.flush()

    def sync_mode(self, sync):
        # if sync isnt bool raise exception
        analytics.sync_mode = sync

    def error_handler(self, error, items):
        print('Error handler not implemented')