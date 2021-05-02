import hashlib
from codeforces.request import codeforces_request
from tabulate import tabulate
from bs4 import BeautifulSoup
import datetime

class codeforces_method:
    def __init__(self):
        self.request = codeforces_request()
        self.help = "help"

    def form_request(self, str_, param):
        for key in param:
            str_ += f"{key}={param[key]}&"
        
        str_ +=  f"#{self.request.key}"

        result = hashlib.sha512(str_.encode())
        param['apisig'] = f"{self.request.ran_num}{result.hexdigest()}"
        json_data = self.request.make_request(self.request.url, param)
        return json_data

    def show_help(self):
        print("""
        --blog-comment, -bc                  To get data for blogEntry.comments
        Required Parameter:
        --blogEntryId, --bid         	     Id of the blog entry. It can be seen in blog entry URL. 
                                             For example: /blog/entry/79


        --blog-entry, -be                    To get data for blogEntry.view
        Required Parameter:
        --blogEntryId, --bid         	     Id of the blog entry. It can be seen in blog entry URL. 
                                             For example: /blog/entry/79


        --contest-hack, -ch                  To get data for contest.hacks
        Required Parameter:
        --contestId, --cid         	     Id of the contest. It is not the round number. 
                                             It can be seen in contest URL. For example: /contest/566/status


        --contest-list, -cl                  To get data for contest.list
        Optional Parameter:
        --gym, -g                            Boolean. If true — than gym contests are returned. Otherwide, 
                                             regular contests are returned.


        --contest-rating, -cr                To get data for contest.ratingChanges
        Required Parameter:
        --contestId, --cid         	     Id of the contest. It is not the round number. 
                                             It can be seen in contest URL. For example: /contest/566/status


        --contest-status, -cs                To get data for contest.status
        Required Parameter:
        --contestId, --cid         	     Id of the contest. It is not the round number. 
                                             It can be seen in contest URL. For example: /contest/566/status
        Optional Parameters:
        --handle, -h                         Codeforces user handle
        --from, -f                           1-based index of the first submission to return
        --count, -c                          Number of returned submissions


        --problems, -p                       To get data for problemset.problems
        Optional Parameter:
        --tags, -t	                     Semicilon-separated list of tags.        


        --problem-status, -ps                To get data for problemset.recentStatus
        Required Parameter:
        --count, -c	                     Number of submissions to return. Can be up to 1000.
        Optional Parameter:
        --problemsetName, -psname	     Custom problemset's short name, like 'acmsguru'


        --user-blog, -ub                     To get data for user.blogEntries
        Required Paramter:
        --handle, -h	                     Codeforces user handle.


        --user-info, -ui                     To get data for user.info
        Required Paramter:
        --handle, -h	                     Semicolon-separated list of handles. No more than 10000 handles is accepted.


        --user-rating, -ur                   To get data for user.rating
        Required Paramter:
        --handle, -h	                     Codeforces user handle.


        --user-status, -us                   To get data for user.status
        Required Paramter:
        --handle, -h	                     Codeforces user handle.
        Optional Parameter
        --from, -f	                     1-based index of the first submission to return.
        --count, -c	                     Number of returned submissions.
        """)

    def blog_comment(self, list_parameter):
        try:
            self.request.url += "blogEntry.comments"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            if '--blogEntryId' in list_parameter:
                pos = list_parameter.index('--blogEntryId')
                param['blogEntryId'] = list_parameter[pos+1]
            elif '-bid' in list_parameter:
                pos = list_parameter.index('-bid')
                param['blogEntryId'] = list_parameter[pos+1]
            else:
                return "Please provide blogEntryId.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/blogEntry.comments?"
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['id'])
                timestamp = datetime.datetime.fromtimestamp(item['creationTimeSeconds'])
                lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
                lst.append(item['commentatorHandle'])
                soup = BeautifulSoup(item['text'], 'html.parser')
                str_ = []
                ls = []
                for item in soup.find_all('div')[0].text.split():
                    if "http" in item:
                        ls.append('\n')
                    ls.append(item)
                    if len(ls) == 7:
                        str_.append(" ".join(ls))
                        ls = [] 
                lst.append("\n".join(str_))
                data.append(lst)

            return tabulate(data, headers=["ID", "Date & Time", "Commentator Handle", "Comment"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def blog_entry(self, list_parameter):
        try:
            self.request.url += "blogEntry.view"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            if '--blogEntryId' in list_parameter:
                pos = list_parameter.index('--blogEntryId')
                param['blogEntryId'] = list_parameter[pos+1]
            elif '-bid' in list_parameter:
                pos = list_parameter.index('-bid')
                param['blogEntryId'] = list_parameter[pos+1]
            else:
                return "Please provide blogEntryId.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/blogEntry.view?"
            
            json_data = self.form_request(str_, param)
            data = []
            lst = []
            lst.append(json_data['result']['id'])
            timestamp = datetime.datetime.fromtimestamp(json_data['result']['creationTimeSeconds'])
            lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
            lst.append(json_data['result']['authorHandle'])
            timestamp1 = datetime.datetime.fromtimestamp(json_data['result']['modificationTimeSeconds'])
            lst.append(timestamp1.strftime('%Y-%m-%d %H:%M:%S'))
            soup = BeautifulSoup(json_data['result']['title'], 'html.parser')
            lst.append(soup.find('p').text)
            lst.append(", ".join(json_data['result']['tags']))
            data.append(lst)

            return tabulate(data, headers=["ID", "Creation Time", "Author Handle","Modification Time", "Title", "Tags"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."
    
    def contest_hack(self, list_parameter):
        try:
            self.request.url += "contest.hacks"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            if '--contestId' in list_parameter:
                pos = list_parameter.index('--contestId')
                param['contestId'] = list_parameter[pos+1]
            elif '-cid' in list_parameter:
                pos = list_parameter.index('-cid')
                param['contestId'] = list_parameter[pos+1]
            else:
                return "Please provide contestId.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/contest.hacks?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(f"{item['problem']['contestId']}{item['problem']['index']}")
                timestamp = datetime.datetime.fromtimestamp(item['creationTimeSeconds'])
                lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
                lst.append(item['hacker']['members'][0]['handle'])
                lst.append(item['defender']['members'][0]['handle'])
                lst.append(item['problem']['name'])
                lst.append(", ".join(item['problem']['tags']))
                lst.append(item['judgeProtocol']['verdict'])
                data.append(lst)

            return tabulate(data, headers=["Contest ID", "Creation Time", "Hacker Handle", "Defender Handle", "Problem Name", "Tags", "Verdict"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def contest_list(self, list_parameter):
        try:
            self.request.url += "contest.list"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            if '--gym' in list_parameter:
                pos = list_parameter.index('--gym')
                param['gym'] = list_parameter[pos+1]
            elif '-g' in list_parameter:
                pos = list_parameter.index('-g')
                param['gym'] = list_parameter[pos+1]
            
            str_ = f"{self.request.ran_num}/contest.list?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['id'])
                lst.append(item['name'])
                lst.append(item['type'])
                lst.append(item['phase'])
                lst.append(f"{item['durationSeconds']//60} mins")
            return tabulate(data, headers=["ID", "Name", "Type", "Phase", "Duration"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def contest_rating(self, list_parameter):
        try:
            self.request.url += "contest.ratingChanges"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            if '--contestId' in list_parameter:
                pos = list_parameter.index('--contestId')
                param['contestId'] = list_parameter[pos+1]
            elif '-cid' in list_parameter:
                pos = list_parameter.index('-cid')
                param['contestId'] = list_parameter[pos+1]
            else:
                return "Please provide contestId.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/contest.ratingChanges?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['contestId'])
                lst.append(item['contestName'])
                lst.append(item['handle'])
                lst.append(item['rank'])
                lst.append(item['oldRating'])
                lst.append(item['newRating'])
                data.append(lst)
            
            return tabulate(data, headers=["contestID", "Contest Name", "Handle", "Rank", "Old Rating", "New Rating"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def contest_status(self, list_parameter):
        try:
            self.request.url += "contest.status"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            if '--contestId' in list_parameter:
                pos = list_parameter.index('--contestId')
                param['contestId'] = list_parameter[pos+1]
            elif '-cid' in list_parameter:
                pos = list_parameter.index('-cid')
                param['contestId'] = list_parameter[pos+1]
            else:
                return "Please provide contestId.\nType --help, -h for help"

            if '--handle' in list_parameter:
                pos = list_parameter.index('--handle')
                param['handle'] = list_parameter[pos+1]
            elif '-h' in list_parameter:
                pos = list_parameter.index('-h')
                param['handle'] = list_parameter[pos+1]
            
            if '--from' in list_parameter:
                pos = list_parameter.index('--from')
                param['from'] = list_parameter[pos+1]
            elif '-f' in list_parameter:
                pos = list_parameter.index('-f')
                param['from'] = list_parameter[pos+1]
            
            if '--count' in list_parameter:
                pos = list_parameter.index('--count')
                param['count'] = list_parameter[pos+1]
            elif '-c' in list_parameter:
                pos = list_parameter.index('-c')
                param['count'] = list_parameter[pos+1]
                
            str_ = f"{self.request.ran_num}/contest.status?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['id'])
                lst.append(item['problem']['name'])
                lst.append(item['problem']['tags'])
                lst.append(item['author']['members'][0]['handle'])
                lst.append(item['programmingLanguage'])
                lst.append(item['verdict'])
                lst.append(item['passedTestCount'])
                data.append(lst)
            
            return tabulate(data, headers=["ID", "Problem Name", "Tags", "Author Handle", "Programming Language", 'Verdict', 'Passed Testcases'], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def problems(self, list_parameter):
        try:
            self.request.url += "problemset.problems"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            
            if '--tags' in list_parameter:
                pos = list_parameter.index('--tags')
                param['tags'] = list_parameter[pos+1]
            elif '-t' in list_parameter:
                pos = list_parameter.index('-t')
                param['tags'] = list_parameter[pos+1]

            str_ = f"{self.request.ran_num}/problemset.problems?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item, item2 in zip(json_data['result']['problems'],json_data['result']['problemStatistics']):
                lst = []
                lst.append(item['name'])
                lst.append(", ".join(item['tags']))
                lst.append(item2['solvedCount'])
                data.append(lst)
            
            return tabulate(data, headers=["Problem Name", "Problem Tags", "Solved Count"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def problems_status(self, list_parameter):
        try:
            self.request.url += "problemset.recentStatus"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }
            
            if '--count' in list_parameter:
                pos = list_parameter.index('--count')
                param['count'] = list_parameter[pos+1]
            elif '-c' in list_parameter:
                pos = list_parameter.index('-c')
                param['count'] = list_parameter[pos+1]
            else:
                return "Please provide count for number of submissions(Max. value upto 100).\nType --help, -h for help"
            
            if '--problemsetName' in list_parameter:
                pos = list_parameter.index('--problemsetName')
                param['problemsetName'] = list_parameter[pos+1]
            elif '-psname' in list_parameter:
                pos = list_parameter.index('-psname')
                param['problemsetName'] = list_parameter[pos+1]

            str_ = f"{self.request.ran_num}/problemset.recentStatus?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['id'])
                lst.append(f"{item['problem']['contestId']}{item['problem']['index']}")
                lst.append(item['problem']['name'])
                lst.append(", ".join(item['problem']['tags']))
                lst.append(item['author']['members'][0]['handle'])
                lst.append(item['programmingLanguage'])
                data.append(lst)
            
            return tabulate(data, headers=["ID", "Problem Id", "Problem Name", "Problem Tags", "Handle", "Language"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."
            
    def user_blog(self, list_parameter):
        try:
            self.request.url += "user.blogEntries"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }

            if '--handle' in list_parameter:
                pos = list_parameter.index('--handle')
                param['handle'] = list_parameter[pos+1]
            elif '-h' in list_parameter:
                pos = list_parameter.index('-h')
                param['handle'] = list_parameter[pos+1]
            else:
                return "Please provide Codeforces user handle.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/user.blogEntries?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['id'])
                timestamp = datetime.datetime.fromtimestamp(item['creationTimeSeconds'])
                lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
                lst.append(item['authorHandle'])
                timestamp1 = datetime.datetime.fromtimestamp(item['modificationTimeSeconds'])
                lst.append(timestamp1.strftime('%Y-%m-%d %H:%M:%S'))
                if '<p' in item['title']:
                    soup = BeautifulSoup(item['title'], 'html.parser')
                    lst.append(soup.find('p').text)
                else:
                    lst.append(item['title'])
                lst.append(", ".join(item['tags']))
                data.append(lst)

            return tabulate(data, headers=["ID", "Creation Time", "Author Handle","Modification Time", "Title", "Tags"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def user_info(self, list_parameter):
        try:
            self.request.url += "user.info"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }

            if '--handle' in list_parameter:
                pos = list_parameter.index('--handle')
                param['handle'] = list_parameter[pos+1]
            elif '-h' in list_parameter:
                pos = list_parameter.index('-h')
                param['handle'] = list_parameter[pos+1]
            else:
                return "Please provide Codeforces user handle.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/user.info?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['lastName'])
                lst.append(item['firstName'])
                lastonline = datetime.datetime.fromtimestamp(item['lastOnlineTimeSeconds'])
                lst.append(lastonline.strftime('%Y-%m-%d %H:%M:%S'))
                lst.append(item['country'])
                lst.append(item['city'])
                lst.append(item['rating'])
                lst.append(item['friendOfCount'])
                lst.append(item['handle'])
                lst.append(item['organization'])
                Registered = datetime.datetime.fromtimestamp(item['registrationTimeSeconds'])
                lst.append(Registered.strftime('%Y-%m-%d %H:%M:%S'))
                lst.append(item['maxRank'])
                data.append(lst)

            return tabulate(data, headers=["Last Name", "First Name", "Last Online", "Country", "City", "Rating", 'Friends', 'Handle', 'Organization', 'Registered', 'Maximum Rank'], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def user_rating(self, list_parameter):
        try:
            self.request.url += "user.rating"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }

            if '--handle' in list_parameter:
                pos = list_parameter.index('--handle')
                param['handle'] = list_parameter[pos+1]
            elif '-h' in list_parameter:
                pos = list_parameter.index('-h')
                param['handle'] = list_parameter[pos+1]
            else:
                return "Please provide Codeforces user handle.\nType --help, -h for help"

            str_ = f"{self.request.ran_num}/user.rating?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['contestId'])
                lst.append(item['contestName'])
                lst.append(item['handle'])
                lst.append(item['rank'])
                lst.append(item['oldRating'])
                lst.append(item['newRating'])
                data.append(lst)
            
            return tabulate(data, headers=["Contest Id", "Contest Name", "Handle", "Rank", "Old Rating", "New Rating"], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."

    def user_status(self, list_parameter):
        try:
            self.request.url += "user.status"
            param = {
                "apikey": self.request.key,
                "time": self.request.time_now
            }

            if '--handle' in list_parameter:
                pos = list_parameter.index('--handle')
                param['handle'] = list_parameter[pos+1]
            elif '-h' in list_parameter:
                pos = list_parameter.index('-h')
                param['handle'] = list_parameter[pos+1]
            else:
                return "Please provide Codeforces user handle.\nType --help, -h for help"
            
            if '--from' in list_parameter:
                pos = list_parameter.index('--from')
                param['from'] = list_parameter[pos+1]
            elif '-f' in list_parameter:
                pos = list_parameter.index('-f')
                param['from'] = list_parameter[pos+1]
            
            if '--count' in list_parameter:
                pos = list_parameter.index('--count')
                param['count'] = list_parameter[pos+1]
            elif '-c' in list_parameter:
                pos = list_parameter.index('-c')
                param['count'] = list_parameter[pos+1]

            str_ = f"{self.request.ran_num}/user.status?"
            
            json_data = self.form_request(str_, param)
            data = []
            for item in json_data['result']:
                lst = []
                lst.append(item['id'])
                lst.append(item['problem']['name'])
                lst.append(item['problem']['tags'])
                lst.append(item['author']['members'][0]['handle'])
                lst.append(item['programmingLanguage'])
                lst.append(item['verdict'])
                lst.append(item['passedTestCount'])
                data.append(lst)
            
            return tabulate(data, headers=["ID", "Problem Name", "Tags", "Author Handle", "Programming Language", 'Verdict', 'Passed Testcases'], tablefmt="grid")
        except:
            return "Please enter correct format.\nType --help or -h for help."