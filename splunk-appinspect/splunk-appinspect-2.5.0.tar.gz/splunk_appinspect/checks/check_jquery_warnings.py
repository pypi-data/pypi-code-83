"""
### jQuery vulnerabilities
"""
import os
import splunk_appinspect
import splunk_appinspect.check_routine.util as util

""" This function throws a warning message during app inspect if the app's
JS files import jquery inside them.

@param:
app: An app object
reporter: Reporter object """

@splunk_appinspect.tags("cloud", "check_jquery_usage")
@splunk_appinspect.cert_version(min="2.5.0")
def check_jquery_usage(app, reporter):
    """ Check that the app files are using jQuery. """

    # Making this a set as we can scale this solution to add other bad imports in the future.
    flagged_imports = {"jquery"}
    js_files = list(app.get_filepaths_of_files(types=[".js"]))

    # Get absolute paths of js files
    unpacked_js_files = util.unpack_absolute_path(js_files)

    for files, errors in util.validate_imports(unpacked_js_files, flagged_imports):
        message = (
            "Upgrade your JS file {} to jQuery version 3.5 or later." +
            "Older versions of jQuery will not be permitted in Splunk Cloud."
        ).format(files)
        reporter.warn(message, files)


""" This function throws a warning message during app inspect if the dashboards of the app
do not have a version attribute OR have the version attribute set to a value other than 1.1

@param:
app: An app object
reporter: Reporter object """

@splunk_appinspect.tags("cloud", "check_jquery_usage")
@splunk_appinspect.cert_version(min="2.5.0")
def check_simplexml_standards_version(app, reporter):
    """ Check that the dashboards in your app have a valid version attribute.
    """

    xml_files = list(app.get_filepaths_of_files(types=[".xml"]))
    nodes = [util.xml_node("dashboard"), util.xml_node("form")]
    query_nodes = util.find_xml_nodes_usages(xml_files, nodes)
    for query_node, relative_filepath in query_nodes:
        version = query_node.get('version')
        if version is None:
            message = (
                "Change the version attribute in the root node of your Simple XML dashboard {} to " +
                "`<version=1.1>`. Earlier dashboard versions introduce security vulnerabilities " +
                "into your apps and are not permitted in Splunk Cloud"
            ).format(relative_filepath)
            reporter.warn(message, relative_filepath)
        elif version.strip() == "2" or version.strip() == "1.1":    # If UDF or simple XML dashboard 1.1, continue
            continue
        else:
            message = (
                "Version attribute of the dashboard {} is set to {}.Change the version attribute " +
                "in the root node of your Simple XML dashboard to " +
                "`<version=1.1>`. Earlier dashboard versions introduce security vulnerabilities " +
                "into your apps and are not permitted in Splunk Cloud"
            ).format(relative_filepath, version)
            reporter.warn(message, relative_filepath)


""" This function throws a warning message during app inspect if the app's HTML and JS files
have unsupported imports

@param:
app: An app object
reporter: Reporter object """

@splunk_appinspect.tags("cloud", "check_jquery_usage")
@splunk_appinspect.cert_version(min="2.5.0")
def check_hotlinking_splunk_web_libraries(app, reporter):
    """ Check that the app files are not importing files directly from the
        search head.
    """

    html_files = list(app.get_filepaths_of_files(types=[".html"]))
    xml_files = list(app.get_filepaths_of_files(types=[".xml"]))
    js_files = list(app.get_filepaths_of_files(basedir="appserver", types=[".js"]))
    spa_referenced_files = []  # Single page application referenced files
    non_sxml_dashboards = []    # Non Simple XML dashboards

    # Only filter in SPA files
    view_nodes = [util.xml_node("view")]
    view_dashboard_nodes = util.find_xml_nodes_usages_absolute_path(xml_files, view_nodes)

    # Get dashboards
    dashboard_nodes = [util.xml_node("dashboard"), util.xml_node("form")]
    other_dashboard_nodes = util.find_xml_nodes_usages_absolute_path(xml_files, dashboard_nodes)

    non_exposed_modules_json_path = os.path.abspath(os.path.join(__file__, "../../splunk/jquery_checks_data/non_exposed_modules.json"))
    exposed_modules_json_path = os.path.abspath(os.path.join(__file__, "../../splunk/jquery_checks_data/exposed_modules.json"))

    with open(non_exposed_modules_json_path, 'r', encoding='utf-8', errors='ignore') as non_exposed_modules_file:
        non_exposed_modules_imports = util.populate_set_from_json(non_exposed_modules_file)

    with open(exposed_modules_json_path, 'r', encoding='utf-8', errors='ignore') as exposed_modules_file:
        exposed_modules_imports = util.populate_set_from_json(exposed_modules_file)

    # Get all template attributes in SPA  files
    for query_node, absolute_file_path in view_dashboard_nodes:
        reference_template = query_node.get('template')
        if reference_template is not None:
            spa_referenced_files.append(reference_template)

    # Check for scripts references in dashboards
    for query_node, absolute_file_path in other_dashboard_nodes:
        reference_script = query_node.get('script')
        if reference_script is not None:
            non_sxml_dashboards.append(reference_script)

    # Get absolute paths of js files
    unpacked_js_files = util.unpack_absolute_path(js_files)
    # paths to scripts referenced by simple xml dashboard script (Non simple xml dashboards)
    non_simple_xml_js_paths = util.get_spa_template_file_paths(unpacked_js_files, non_sxml_dashboards)
    # paths to templates referenced by SPA
    template_paths = util.get_spa_template_file_paths(util.unpack_absolute_path(html_files), spa_referenced_files)

    # Other scripts in the appserver directory (Classified as simple xml scripts)
    # These are not referenced by any dashboards but are present in the appserver directory
    # Though these will result in false positives if they have bad imports, they need to be checked
    # just because they might be referenced by templates.

    subset_of_non_simple_xml_js_paths = set(non_simple_xml_js_paths)

    simple_xml_js_paths = [a for a in unpacked_js_files if a not in subset_of_non_simple_xml_js_paths]

    message = ("Embed all your app's front-end JS dependencies in the /appserver directory. " +
               "If you import files from Splunk Web, your app might fail when Splunk Web updates."
               )
    for files, errors in util.validate_imports(template_paths, non_exposed_modules_imports):
        reporter.warn(message, files)

    for files, errors in util.validate_imports(non_simple_xml_js_paths, non_exposed_modules_imports):
        reporter.warn(message, files)

    # Filter only non exposed modules for simple XML dashboards.

    non_exposed_modules_set = set(a for a in non_exposed_modules_imports if a not in exposed_modules_imports)

    for files, errors in util.validate_imports(simple_xml_js_paths, non_exposed_modules_set):
        reporter.warn(message, files)
