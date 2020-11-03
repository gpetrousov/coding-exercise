import requests
import json
import semantic_version

def main():

    return


if __name__ == "__main__":

    requirements_file = open('requirements.txt', 'r')
    file_lines = requirements_file.readlines()

    for each_package in file_lines:
        repo_name = each_package.split(' ')[0]
        repo_version = each_package.split(' ')[1]
        # strip to numbres only if necessary
        if repo_version[0] == 'v':
            repo_version = repo_version[1::]
        if not semantic_version.validate(repo_version):
            print("Invalid semantic version")
            continue
        local_version = semantic_version.Version(repo_version)

        r = requests.get('https://api.github.com/repos/{}/tags'.format(repo_name))
        repo_versions = json.loads(r.content)
        latest_version = repo_versions[0]['name'][1::]
        remote_version = semantic_version.Version(latest_version)

        if  local_version < remote_version:
            print("newer version available")


