# build.py
"""
Build my resume!

This is a custom python script to parse the resume.json file and
output to different formats. The first one supported with build to Markdown.
"""

from argparse import ArgumentParser

import json

class Resume:
    def __init__(self, json_file):

        with open(json_file, 'r') as f:
            self.raw_data = json.load(f)

        for a in ['basics', 'profiles', 'work', 'education', 'skills', 'interests']:
            setattr(self, a, self.raw_data.get(a, None))

    def __repr__(self):
        s = [
            f"{self.basics.get('name')}",
            f"{self.basics.get('label')}",
            "-"*len(self.basics.get('label'))
        ]
        return '\n'.join(s)

def parse_arguments():
    parser = ArgumentParser(description = "Process your resume!")
    parser.add_argument('input_file', default='resume.json', type=str, help="path to the json input file")

    args = parser.parse_args()
    return args

if __name__ == "__main__":

    args = parse_arguments()
    resume = Resume(json_file = args.input_file)

    print(resume)