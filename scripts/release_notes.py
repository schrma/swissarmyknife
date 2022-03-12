import argparse
from parse import parse
from datetime import datetime
import os
import sys
import inspect

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

CHANGELOG_FILE = '../CHANGELOG.md'
TMP_DIR = '../.tmprz'
TEMPLATE_FILE_RELEASE = '../.template/template_release_note.md'
TEMPLATE_FILE_CHANGELOG = '../.template/template_change_log.md'
RELEASE_NOTE_FILE = 'release_notes.md'
SCRIPT_VERSION = "1.0.0"


def get_parser():
    parser = argparse.ArgumentParser(description="Prepare release notes and changelog")
    parser.add_argument(
        '-i', '--input',
        required=False,
        metavar='filename',
        default="../CURRENT_RELEASE_NOTE.md",
        help='input file (release notes)'
    )
    parser.add_argument(
        '-c', '--command',
        required=False,
        default="create_changelog",
        metavar='string',
        help='Command'
    )
    return parser


def parse_release_note(filename):
    note = ''
    version = None

    with open(filename, 'r') as cf:
        for line in cf:
            if '!' in line:
                continue
            if '## ' in line:
                line_eol_spaces_removed = str(' '.join(line.splitlines()).strip())
                parse_result = parse("## v{}", line_eol_spaces_removed)
                if parse_result:
                    version = parse_result.fixed[0]
            note += line

    if version:
        return note, version
    else:
        raise ValueError("Version was not found")


def parse_changelog_note():
    note = ''
    collect = False

    with open(os.path.join(CURRENT_DIR, CHANGELOG_FILE), 'r') as cf:
        for line in cf:
            # Start collecting data at first occurence of '##'
            if '## ' in line:
                collect = True
                line_eol_spaces_removed = str(' '.join(line.splitlines()).strip())
                parse_result = parse("## {}", line_eol_spaces_removed)
                if parse_result:
                    version = parse_result.fixed[0]
            if '<hr' in line:
                collect = False
            if collect:
                note += line

    return note


def apply_to_release_template(note):
    md = ''
    today = datetime.today()
    with open(os.path.join(CURRENT_DIR, TEMPLATE_FILE_RELEASE), 'r') as tf:
        md = tf.read() \
            .replace('{SCRIPT_VERSION}', SCRIPT_VERSION) \
            .replace('{TIMESTAMP_DATE}', today.strftime('%Y-%m-%d')) \
            .replace('{TIMESTAMP_TIME}', today.strftime('%H:%M:%S')) \
            .replace('{RELEASE_NOTES}', note)
    return md


def apply_to_changelog_template(note_changelog, note_release):
    md = ''
    today = datetime.today()
    with open(os.path.join(CURRENT_DIR, TEMPLATE_FILE_CHANGELOG), 'r') as tf:
        md = tf.read() \
            .replace('{SCRIPT_VERSION}', SCRIPT_VERSION) \
            .replace('{TIMESTAMP_DATE}', today.strftime('%Y-%m-%d')) \
            .replace('{TIMESTAMP_TIME}', today.strftime('%H:%M:%S')) \
            .replace('{OLD_CHANGELOG}', note_changelog) \
            .replace('{RELEASE_NOTE}', note_release)
    return md


def get_version(filename):
    _, version = parse_release_note(filename)
    return version


def save_note(note, filename):
    with open(filename, 'w') as rf:
        rf.write(note)


def create_changelog(filename):
    note_changelog_old = parse_changelog_note()
    note_release, _ = parse_release_note(filename)
    note_changelog_new = apply_to_changelog_template(note_changelog_old, note_release)
    print(note_changelog_new)
    save_note(note_changelog_new, filename=os.path.join(CURRENT_DIR, CHANGELOG_FILE))


def create_release(filename):
    note_release, _ = parse_release_note(filename)
    note_release_new = apply_to_release_template(note_release)
    print(note_release_new)
    base_path = os.path.join(CURRENT_DIR, TMP_DIR)
    os.makedirs(base_path, exist_ok=True)
    save_note(note_release_new, os.path.join(base_path, RELEASE_NOTE_FILE))


def main(**kwargs) -> int:
    filename = kwargs["input"]
    command = kwargs["command"]

    if command == 'create_changelog':
        create_changelog(filename)

    if command == 'create_release':
        create_release(filename)

    if command == 'get_version':
        try:
            version = get_version(filename)
            print(version)
        except ValueError:
            print("Version was not found")
    return 0


def parse_command_line_args(args=None):
    try:
        parsed_args = get_parser().parse_args(args)
    except argparse.ArgumentError as error:
        print(error)

    return vars(parsed_args)


def run():
    main(**parse_command_line_args())


if __name__ == '__main__':
    sys.exit(run())
