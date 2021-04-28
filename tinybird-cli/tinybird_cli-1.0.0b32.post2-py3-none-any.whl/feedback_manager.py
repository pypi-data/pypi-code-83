from collections import namedtuple

FeedbackMessage = namedtuple('FeedbackMessage', 'message')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    CGREY = '\33[90m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_message(message, color=bcolors.ENDC):
    def formatter(**kwargs):
        return f"{color}{message.format(**kwargs)}{bcolors.ENDC}"
    return formatter


def error_message(message):
    return print_message(f"\n** {message}", bcolors.FAIL)


def simple_error_message(message):
    return print_message(f"{message}", bcolors.FAIL)


def warning_message(message):
    return print_message(message, bcolors.WARNING)


def info_message(message):
    return print_message(message)


def info_highlight_message(message):
    return print_message(message, bcolors.OKBLUE)


def success_message(message):
    return print_message(message, bcolors.OKGREEN)


class FeedbackManager:
    error_exception = error_message("{error}")
    error_exception_trace = error_message("{error}\n** Trace:\n{trace}")
    error_notoken = error_message("No auth token provided. Run 'tb auth' to configure them.")
    error_auth_config = error_message("{config_file} does not exist")
    error_file_config = error_message("{config_file} can't be written, check write permissions on this folder")
    error_load_file_config = error_message("{config_file} can't be loaded, remove it and run the command again")
    error_push_file_exception = error_message('Failed running {filename}: {error}')
    error_parsing_node = error_message("error parsing node \"{node}\"")
    error_request_threads = error_message("failed request with {threads} threads")
    error_check_pipe = error_message("check error: {error}")
    error_pipe_already_exists = error_message("{pipe} already exists")
    error_datasource_already_exists = error_message("{datasource} already exists")
    error_datasource_already_exists_and_alter_failed = error_message("{datasource} already exists and the migration can't be executed to match the new definition: {alter_error_message}")
    error_datasource_can_not_be_deleted = error_message("{datasource} can not be deleted:\n** {error}")
    error_removing_datasource = error_message("Failed removing data source {datasource}")
    error_creating_datasource = error_message("Failed creating data source: {error}")
    error_processing_blocks = error_message("{error} - FAIL")
    error_file_already_exists = error_message("{file} already exists, use --force to override")
    error_invalid_token = error_message("Invalid token for {host}")
    error_invalid_query = error_message("Only SELECT queries are supported")
    error_pipe_does_not_exist = error_message("'{pipe}' pipe does no exist")
    error_datasource_does_not_exist = error_message("'{datasource}' datasource does no exist")
    error_pull = error_message("there was a problem while pulling {error}")
    error_parsing_file = error_message("error parsing {filename}: {error}")
    error_parsing_schema = error_message("error parsing schema (line {line}): {error}")
    error_sorting_key = error_message("SORTING_KEY should be set with {engine}")
    error_unknown_resource = error_message("Unknown resource '{resource}'")
    error_file_extension = error_message("File extension for {filename} not supported. It should be one of .datasource or .pipe")
    error_remove_endpoint = error_message("Failed removing pipe endpoint {error}")
    error_updating_pipe = error_message("Failed updating pipe {error}")
    error_removing_node = error_message("Failed removing node from pipe {pipe}: {error}")
    error_creating_node = error_message("Failed creating node on pipe {pipe}: {error}")
    error_creating_endpoint = error_message("Failed creating endpoint in node {node} on pipe {pipe}: {error}")
    error_creating_pipe = error_message("Failed creating pipe {error}")
    error_removing_dummy_node = error_message("Failed removing node {error}")
    error_check_pipes_populate = error_message("You can't check pipes with populate=True")
    error_negative_version = error_message("VERSION gets one positive integer param")
    error_while_populating = error_message("Error while populating: {error}")
    error_auth = error_message("Check your local config")
    error_wrong_config_file = error_message("Wrong {config_file}, run 'tb auth' to initialize")
    error_workspace_not_in_local_config = error_message("Use 'tb auth add --ws {workspace}' to add this workspace to the local config")
    error_not_personal_auth = error_message("** You have to authenticate with a personal account")
    error_incremental_not_supported = error_message("The --incremental parameter is only supported when the `--connector` parameter is passed")
    error_invalid_connector = error_message("Invalid connector parameter: Use one of {connectors}")
    error_connector_not_configured = error_message("{connector} connector not properly configured. Please run `tb auth --connector {connector}` first")
    error_connector_not_installed = error_message("{connector} connector not properly installed. Please run `pip install tinybird-cli[{connector}]` first")
    error_option = error_message("{option} is not a valid option")
    error_job_does_not_exist = error_message("Job with id '{job_id}' doesn't exists")
    error_job_cancelled_but_status_unknown = error_message("Job with id '{job_id}' has started the cancellation process but its status is unknown.")
    error_skip_table_checks_path = simple_error_message("you can skip this error by running `tb push {path} --skip-table-checks`")

    warning_connector_not_installed = warning_message("Auth found for {connector} connector but it's not properly installed. Please run `pip install tinybird-cli[{connector}]` to use it")
    warning_deprecated = warning_message("** [DEPRECATED]: {warning}")
    warning_deprecated_command = warning_message("** [DEPRECATED]: The '{keyword}' keyword is deprecated, found at node '{node}', you must use 'ENGINE_{keyword}' instead. '{keyword}' will stop working after {deadline}.")
    warning_token_pipe = warning_message("** There's no read token for pipe {pipe}")
    warning_file_not_found_inside = warning_message("** Warning: {name} not found inside: \n   - {folder}\n   - {folder}/datasources\n   - {folder}/endpoints")
    warning_check_pipe = warning_message("** Warning: Failed removing checker pipe: {content}")
    warning_datasource_already_exists = warning_message(
        """** Warning: datasource {datasource} already exists and can't be migrated or replaced.
** This is a safety feature to avoid removing a datasource by mistake.
** Drop it using:
**    $ tb datasource rm {datasource}""")
    warning_name_already_exists = warning_message("** Warning: {name} already exists, skipping")
    warning_dry_name_already_exists = warning_message("** [DRY RUN] {name} already exists, skipping")
    warning_file_not_found = warning_message("** Warning: {name} file not found")
    warning_update_version = warning_message("** UPDATE AVAILABLE: please install tinybird-cli {latest_version}")
    warning_current_version = warning_message("** current: tinybird-cli {current_version}")
    warning_confirm_truncate_datasource = warning_message("Do you want to truncate {datasource}? Once truncated, your data can't be recovered")
    warning_confirm_delete_datasource = warning_message("Do you want to delete {datasource}? Once deleted, it can't be recovered")
    warning_confirm_delete_pipe = warning_message("Do you want to remove the pipe \"{pipe}\"?")
    warning_confirm_drop_prefix = warning_message("Do you want to remove all pipes and data sources with prefix \"{prefix}\"?")

    info_fetching_timing_url = info_message("** Fetching timing info for {url}")
    info_populate_job_url = info_message("** Populating job url {url}")
    info_create_not_found_token = info_message("** Token {token} not found, creating one")
    info_create_found_token = info_message("** Token {token} found, adding permissions")
    info_populate_job = info_message("** Populating job ({job}) {progress}- {status}")
    info_building_dependencies = info_message("** Building dependencies")
    info_creating_resource = info_message("** Creating {name} {version}")
    info_dry_creating_resource = info_message("** [DRY RUN] Creating {name}")
    info_processing_new_resource = info_message("** Running {name} {version}")
    info_processing_resource = info_message("** Running {name} => v{version} (remote latest version: v{latest_version})")
    info_pushing_fixtures = info_message("** Pushing fixtures")
    info_not_pushing_fixtures = info_message("** Not pushing fixtures")
    info_checking_file = info_message("** Checking {file}")
    info_checking_file_size = info_message("** Checking {filename} (appending {size})")
    info_no_rows = info_message("** No rows")
    info_processing_file = info_message("** Processing {filename}")
    info_skip_already_exists = print_message("    => skipping, already exists")
    info_dependency_list = info_message("** {dependency}")
    info_dependency_list_item = info_message("** --- {dependency}")
    info_admin_token = info_message("** Go to {host}/tokens, copy the admin token and paste it")
    info_append_data = info_message("** => If you want to insert data use: $ tb datasource append")
    info_datasources = info_message("** Data sources:")
    info_query_stats = print_message("** Query took {seconds} seconds\n** Rows read: {rows}\n** Bytes read: {bytes}")
    info_datasource_title = print_message("** {title}", bcolors.BOLD)
    info_datasource_row = info_message("{row}")
    info_pipes = info_message("** Pipes:")
    info_pipe_name = info_message("** - {pipe}")
    info_using_node = print_message("** Using last node {node} as endpoint")
    info_removing_datasource = info_message("** Removing data source {datasource}")
    info_removing_datasource_not_found = info_message("** {datasource} not found")
    info_dry_removing_datasource = info_message("** [DRY RUN] Removing data source {datasource}")
    info_removing_pipe = info_message("** Removing pipe {pipe}")
    info_removing_pipe_not_found = info_message("** {pipe} not found")
    info_dry_removing_pipe = info_message("** [DRY RUN] Removing pipe {pipe}")
    info_path_created = info_message("** - /{path} created")
    info_path_already_exists = info_message("** - /{path} already exists, skipping")
    info_writing_resource = info_message("** Writing {resource} {prefix}")
    info_skipping_resource = info_message("** Skipping {resource}")
    info_writing_datasource = info_message("[D] writing {datasource}")
    info_starting_import_process = info_message("** \N{egg} starting import process")
    info_progress_blocks = info_message("\N{egg} blocks")
    info_progress_current_blocks = info_message("\N{hatching chick} blocks")
    info_jobs = info_message("** Jobs")
    info_job = info_message("  ** Job: {job}")
    info_data_pushed = info_message("** Data pushed to {datasource}")
    info_materialized_datasource_created = info_message("** Materialized node '{node}' created the Data Source '{datasource}'")
    info_materialized_datasource_used = info_message("** Materialized node '{node}' used the Data Source '{datasource}'")
    info_no_pipes_stats = info_message("** No pipe stats")
    info_starting_export_process = info_message("** \N{Chicken} starting export process from {connector}")
    info_ask_for_datasource_confirmation = info_message('** Please type the data source name to be replaced')
    info_datasource_doesnt_match_current_schema = info_message("** The schema of '{datasource}' has changed.")
    info_ask_for_alter_confirmation = info_message('** Please confirm you want to apply the changes above y/N')

    success_test_endpoint = success_message("** => Test endpoint with:\n** $ curl {host}/v0/pipes/{pipe}.json?token={token}")
    success_test_endpoint_no_token = success_message("** => Test endpoint at {host}/v0/pipes/{pipe}.json")
    success_processing_blocks = success_message("**  OK ({num_blocks} blocks)")
    success_generated_file = success_message(
        """** Generated {file}
** => Create it on the server running: $ tb push {file}
** => Append data using: $ tb datasource append {stem} {filename}`
""")
    success_generated_pipe = success_message(
        """** Generated {file}
** => Create it on the server running: $ tb push {file}
""")
    success_generated_fixture = success_message("** => Generated fixture {fixture}")
    success_processing_file = success_message("** => File {filename} processed correctly")
    success_appended_rows = success_message("** Appended {appended_rows} new rows")
    success_total_rows = success_message("** Total rows in {datasource}: {total_rows}")
    success_appended_datasource = success_message("** Data appended to data source '{datasource}' successfully!")
    success_replaced_datasource = success_message("** Data replaced in data source '{datasource}' successfully!")
    success_auth = success_message("** Auth successful! \n** Configuration written to .tinyb file, consider adding it to .gitignore")
    success_auth_added = success_message("** Auth config added!")
    success_auth_removed = success_message("** Auth config removed")
    success_delete_datasource = success_message("** Data source '{datasource}' deleted")
    success_truncate_datasource = success_message("** Data source '{datasource}' truncated")
    success_delete_pipe = success_message("** Pipe '{pipe}' deleted")
    success_created_pipe = success_message(
        """** New pipe created!
** Node id: {node_id})
** Set node as endpoint with:
**   $ tb pipe set_endpoint {pipe} {node_id}
** Pipe URL: {host}/v0/pipes/{pipe}
""")
    success_node_changed = success_message("** New node: {node_id}")
    success_node_published = success_message(
        """** Node published!
** Node id: {node_id})
** Pipe URL: {host}/v0/pipes/{pipe}
""")
    success_print_pipe = success_message("** Pipe: {pipe}")
    success_create = success_message("** '{name}' created")
    success_progress_blocks = success_message("** \N{front-facing baby chick} done")
    success_now_using_config = success_message("** Now using {name} ({id})")
    success_connector_config = success_message("** {connector} configuration written to {file_name} file, consider adding it to .gitignore")
    success_job_cancellation_cancelled = success_message("** Job with id '{job_id}' has been cancelled")
    success_job_cancellation_cancelling = success_message(
        "** Job with id '{job_id}' is now in cancelling status and will be cancelled eventually")
    success_datasource_alter = success_message("** The data source has been correctly updated.")

    debug_running_file = print_message("** Running {file}", bcolors.CGREY)
