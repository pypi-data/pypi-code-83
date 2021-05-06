from handadoc_client import (
    _zip_docu_setup,
    DocuSetup,
    _zip_docu_folder,
    _get_project_setup,
    _make_docu_upload_zipfile,
    _package_project,
)
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from pathlib import Path


def test_archive_setup():
    text_with_non_ascii_chars = "German characters öäüß"

    test_setup = DocuSetup(
        name="test1", title="The first test", description="German characters öäüß"
    )

    with TemporaryDirectory() as temp_dir_path:
        root_path = Path(temp_dir_path)
        test_zip_file_path = root_path.joinpath("handadoc.zip")
        with ZipFile(test_zip_file_path, mode="w") as writing_archive:
            _zip_docu_setup(writing_archive, test_setup)

        with ZipFile(test_zip_file_path, mode="r") as reading_archive:
            content = DocuSetup.from_opened_zip(reading_archive)

        assert content[DocuSetup.NAME] == "test1"
        assert content[DocuSetup.TITLE] == "The first test"
        assert content[DocuSetup.DESCRIPTION] == text_with_non_ascii_chars


def test_archive_documentation():
    """

    >>> from doctestprinter import doctest_iter_print
    >>> archived_file_names = test_archive_documentation()
    >>> doctest_iter_print(archived_file_names)
    dummy_icon.png
    index.html
    subdir/
    subdir/.subfile.txt
    """

    with TemporaryDirectory() as temp_dir_path:
        root_path = Path(temp_dir_path)
        test_zip_file_path = root_path.joinpath("handadoc.zip")
        with ZipFile(test_zip_file_path, mode="w") as writing_archive:
            sample_path = Path("tests/resources/sample_1/html").resolve()
            _zip_docu_folder(
                opened_archive=writing_archive, documentation_path=sample_path
            )

        with ZipFile(test_zip_file_path, mode="r") as reading_archive:
            all_archive_file_names = reading_archive.namelist()

    return sorted(all_archive_file_names, key=str)


def test_zip_docu_setup():
    """
    >>> fake_setup = test_zip_docu_setup()
    >>> from doctestprinter import doctest_iter_print
    >>> doctest_iter_print(fake_setup, max_line_width=70)
    name:
      fake-setup
    title:
      A fake setup
    description:
      A fake docu setup test.
    doc_location:
      tests/resources/sample_1/html
    version:
      0.0.0
    server_url:
      http://whereever

    """
    fake_setup = DocuSetup(
        name="fake-setup",
        description="A fake docu setup test.",
        title="A fake setup",
        doc_location="tests/resources/sample_1/html",
        version="0.0.0",
        server_url="http://whereever",
    )
    with TemporaryDirectory() as temp_dir:
        zip_filepath = Path(temp_dir, "test.zip")
        with ZipFile(zip_filepath, "w") as zip_file:
            _zip_docu_setup(opened_archive=zip_file, archive_setup=fake_setup)
        with ZipFile(zip_filepath, "r") as zip_file:
            read_fake_setup = DocuSetup.from_opened_zip(zip_file)
    return read_fake_setup


def test_docu_folder():
    """

    >>> test_files = test_docu_folder()
    >>> from doctestprinter import doctest_iter_print
    >>> doctest_iter_print(test_files, max_line_width=70)
    subdir/
    index.html
    dummy_icon.png
    subdir/.subfile.txt
    """
    with TemporaryDirectory() as temp_dir:
        zip_filepath = Path(temp_dir, "test.zip")
        with ZipFile(zip_filepath, "w") as zip_file:
            _zip_docu_folder(
                opened_archive=zip_file,
                documentation_path=Path("tests/resources/sample_1/html"),
            )
        with ZipFile(zip_filepath, "r") as zip_file:
            file_list = zip_file.namelist()
    return file_list


def test_make_package():
    """

    >>> from doctestprinter import doctest_iter_print
    >>> archived_file_names = test_make_package()
    >>> doctest_iter_print(archived_file_names)
    dummy_icon.png
    handadoc.json
    index.html
    subdir/
    subdir/.subfile.txt

    """
    sample_setup = _get_project_setup(Path("./").resolve())
    sample_setup.doc_location = "tests/resources/sample_1/html"

    with TemporaryDirectory() as temp_dir_path:
        root_path = Path(temp_dir_path)
        test_zip_file_path = root_path.joinpath("handadoc.zip")
        _make_docu_upload_zipfile(
            zip_filepath=test_zip_file_path, docu_setup=sample_setup
        )

        with ZipFile(test_zip_file_path, mode="r") as reading_archive:
            all_archive_file_names = reading_archive.namelist()
            archived_setup = DocuSetup.from_opened_zip(reading_archive)

    assert sample_setup[DocuSetup.TITLE] == archived_setup[DocuSetup.TITLE]
    assert sample_setup[DocuSetup.NAME] == archived_setup[DocuSetup.NAME]
    assert sample_setup[DocuSetup.DESCRIPTION] == archived_setup[DocuSetup.DESCRIPTION]
    return sorted(all_archive_file_names, key=str)


def test_package_project():
    """
    >>> sample_zip_filepath = test_package_project()
    >>> from zipfile import ZipFile
    >>> with ZipFile(sample_zip_filepath) as sample_file:
    ...     sample_file_paths = sample_file.namelist()
    >>> from doctestprinter import doctest_iter_print
    >>> doctest_iter_print(sample_file_paths)
    handadoc.json
    subdir/
    index.html
    dummy_icon.png
    subdir/.subfile.txt
    """
    root_path = Path("tests/resources/sample_1").resolve()
    sample_setup = _get_project_setup(root_path)
    assert sample_setup.name == "handadoc-client-test1"

    with TemporaryDirectory() as temp_dir_path:
        temp_root_path = Path(temp_dir_path)
        resulting_archive_path = _package_project(
            work_path=temp_root_path, valid_docu_setup=sample_setup
        )
    return resulting_archive_path
