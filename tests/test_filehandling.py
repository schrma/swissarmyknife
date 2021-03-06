import os.path

import pytest
from swissarmyknife.file_handling import get_all_files_from_folder, get_all_folders_from_folder, read_file, write_file


def test___read_file___empty_string():
    content = read_file("hello.txt")

    assert content == ""


def test_write_read_file___text___correct_reading(test_folder):
    input_file = os.path.join(test_folder.output, "basic.txt")
    content_write = "hello world"

    write_file(input_file, content_write)
    content_read = read_file(input_file)

    assert content_read == content_write


@pytest.mark.parametrize(
    "file_list, nr_of_files",
    [(["test1.md", "test2.md", "test3.md", "test4.txt"], 3),
     (["test1.md", "test2.md", "test3.md", "test4.md"], 4)],
)
def test_get_all_files_from_folder___input_folder___equal_files(tmpdir, file_list, nr_of_files):
    for item in file_list:
        filehandle = tmpdir.join(item)
        filehandle.write("")

    list_of_files = get_all_files_from_folder(tmpdir, extension=".md")

    assert len(list_of_files) == nr_of_files


@pytest.mark.parametrize(
    "post_folder",
    [["Git", "Bash", "joplin", "Matlab", "MyScripts", "Powershell", "Shell"],
     ['test1', 'test2']]
)
def test___get_all_folders_from_folder___input_folder___equal_files(post_folder, tmpdir):
    for item in post_folder:
        tmpdir.mkdir(item)

    list_of_directories = get_all_folders_from_folder(tmpdir)
    list_of_directories.sort()
    post_folder.sort()

    assert list_of_directories == post_folder


def test__get_all_folders_from_folder___not_existing_path___empty():
    list_of_directories = get_all_folders_from_folder("not_existing_folder")

    assert list_of_directories == []
