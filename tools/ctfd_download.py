#!/usr/bin/env python3

import os
import sys
import json
import argparse
import requests
import string
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--download", help="Create folders and download files. Makes category/chall/README.md if none exists.", action="store_true", default=False)
parser.add_argument("-i", "--index", help="Write ./README.md with challenge summaries", action="store_true", default=False)
parser.add_argument("--index-file", help="Index filename. Default: README.md", default="README.md")
parser.add_argument("-s", "--scoreboard", help="Write file with scoreboard++", action="store_true", default=False)
parser.add_argument("--scoreboard-file", help="Filename for scoreboard (will append) Default: scoreboard.md", default="scoreboard.md")
parser.add_argument("--own-team", help="Team name for scoreboard", default="give cake")
parser.add_argument("-t", "--token", help="CTFd API key")
parser.add_argument("url", help="Base URL to the CTF. https://ctf.example.com", type=str)
args = parser.parse_args()

def safe_foldername(s):
    valid = string.ascii_lowercase + string.digits + "_-"
    s = s.lower().replace(" ", "_")
    s = s.replace("_-_", "-")
    return "".join([x for x in s if x in valid])

def number(num):
    return f"{num:,}".replace(",", ".")

def get_json(endpoint):
    global args
    url = f"{args.url}/api/v1{endpoint}"
    return requests.get(url, headers={
        "Authorization": "Token "+args.token,
        "Content-Type": "application/json"
        }).json().get("data", {})
    
def get_challenge_details(chall_id):
    return get_json(f"/challenges/{chall_id}")

def get_challenge_list():
    global args
    challs = get_json("/challenges")
    # Enrich the data with unique folder names. safe_foldername() might strip away too much uniqueness
    # Postfix challenge-id to the dirname if there are overlaps.  
    allfolders = []
    for chall in challs:
        name_part = safe_foldername(chall["name"])
        if not name_part: name_part = "mystery"
        dirname = safe_foldername(chall["category"]) + "/" + name_part
        if dirname in allfolders:
            dirname += f"_{chall["id"]}"
        allfolders.append(dirname)
        chall["dirname"] = dirname
    return challs

def get_ctf_name():
    global args
    soup = BeautifulSoup(requests.get(args.url).text, features="lxml")
    return soup.find("title").text

def write_main_readme():
    outf = open(args.index_file, "w")
    outf.write(f"# {get_ctf_name()}\n")
    challs = get_challenge_list()
    for c in sorted(set([x.get("category") for x in challs])):
        outf.write(f"## {c}\n")
        for chall in [x for x in challs if x.get("category")==c]:
            solved = chall["solved_by_me"] and "☑" or "" 
            outf.write(f"### [{chall["name"]}](./{chall["dirname"]}/) {solved}\n")
            details = get_challenge_details(chall["id"])
            chall["details"] = details # cache for later sync-job
            outf.write(f"```\n{details["description"]}\n```\n")
            outf.write(f"> Points: {number(chall["value"])}  Solves: {details["solves"]}")
            if details["tags"]:
                outf.write(f"Tags: {",".join(details["tags"])}")
            outf.write("\n\n")
        outf.write("\n")
    outf.close()
    return challs

def download_ctf(challs):
    global args
    if not challs: 
        challs = get_challenge_list()
    for chall in challs:
        if not "details" in chall.keys():
            chall["details"] = get_challenge_details(chall["id"])

        os.makedirs(chall["dirname"], exist_ok=True)
        handouts = []
        for fileurl in chall["details"]["files"]:
            # assuming /files/kvakk/handout.zip?token=asdasldkjasdlkj"
            download_fname = chall["dirname"] +"/"+ fileurl.split("?")[0].split("/")[-1]
            if os.path.isfile(download_fname):
                print(f"{download_fname} exists. Skipping")
                continue
            req = requests.get(f"{args.url}{fileurl}")
            if req.status_code == 200:
                print(f"Saved {download_fname} {open(download_fname, "wb").write(req.content)}b")
                handouts.append(download_fname)

        # Write chall/README.md if it doesn't exist
        outfname = f"{chall["dirname"]}/README.md"
        if os.path.isfile(outfname):
            print(f"{outfname} exists. Skipping.")
            continue
        outf = open(f"{chall["dirname"]}/README.md", "w")
        outf.write(f"# {chall["name"]}\n```\n{chall["details"]["description"]}\n```\n")
        if chall["details"]["connection_info"]:
            outf.write(f"### Connection info\n```\n{chall["details"]["connection_info"]}\n```\n\n")
        if handouts:
            outf.write("### Files\n")
            for f in handouts:
                shortname = f.split("/")[-1]
                outf.write(f"- [{shortname}](./{shortname})\n")
            outf.write("\n")
        outf.write("\n")
        outf.close()

def append_team(team):
    out = []
    if team["name"] == args.own_team:
        bold = "**"
    else:
        bold = ""
    players = ", ".join(f"{x["name"]} ({number(x["score"])})" for x in sorted(team["members"], key=lambda x: x['score'], reverse=True))
    out.append(f"| {team["pos"]} | {bold}{team["name"]}{bold} | {number(team["score"])} | {players} |")
    return out


def write_scoreboard():
    global args
    sboard = get_json("/scoreboard")
    own_team_printed = False
    out = ["## Scoreboard"]
    out += ["| # | Team | Score | Players |",
            "|:--:|:----------|----:| :-------------- |"]
    for pos in range(1, 11):
        team = [x for x in sboard if x["pos"]==pos][0]
        if team["name"] == args.own_team: own_team_printed = True
        out += append_team(team)

    if not own_team_printed:
        team = [x for x in sboard if x["name"]==args.own_team][0]
        if not team:
            print(f"Warning: Could not find {args.own_team} in scoreboard data")
        else:
            print(f"{args.own_team} wasn't on the top 10. Do better? Included for shame :)")
            out += append_team(team) 

    if os.path.isfile(args.scoreboard_file):
        out.insert(0, "\n")
    open(args.scoreboard_file, "a").writelines([f"{x}\n" for x in out])

if __name__ == "__main__":
    challs = None
    if args.index:
        challs = write_main_readme()
    if args.download:
        download_ctf(challs)
    if args.scoreboard:
        write_scoreboard()
    elif not challs:
        print("Nothing to do..")
