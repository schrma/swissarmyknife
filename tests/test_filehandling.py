import os
import pytest
from file_handling import get_all_files_from_folder, get_all_folders_from_folder


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
    [["Bash", "Git", "joplin", "Matlab", "MyScripts", "Powershell", "Shell"],
     ['test1', 'test2']]
)
def test___get_all_folders_from_folder___input_folder___equal_files(post_folder, tmpdir):
    for item in post_folder:
        tmpdir.mkdir(item)

    list_of_directories = get_all_folders_from_folder(tmpdir)

    assert list_of_directories == post_folder
