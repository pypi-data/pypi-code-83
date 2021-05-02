from codeforces.methods import codeforces_method
import sys

def codeforces():
    code_method = codeforces_method()
    list_parameter = None
    switcher = {
        "--blog-comment": code_method.blog_comment,
        "-bc": code_method.blog_comment,
        "--blog-entry": code_method.blog_entry,
        "-be": code_method.blog_entry,
        "--contest-hack": code_method.contest_hack,
        "-ch": code_method.contest_hack,
        "--contest-list": code_method.contest_list,
        "-cl": code_method.contest_list,
        "--contest-rating": code_method.contest_rating,
        "-cr": code_method.contest_rating,
        "--contest-status": code_method.contest_status,
        "-cs": code_method.contest_status,
        "--problems": code_method.problems,
        "-p": code_method.problems,
        "--problem-status": code_method.problems_status,
        "-ps": code_method.problems_status,
        "--user-blog": code_method.user_blog,
        "-ub": code_method.user_blog,
        "--user-info": code_method.user_info,
        "-ui": code_method.user_info,
        "--user-rating": code_method.user_rating,
        "-ur": code_method.user_rating,
        "--user-status": code_method.user_status,
        "-us": code_method.user_status
    }
    if len(sys.argv) ==1  or sys.argv[-1] == '--help' or sys.argv[-1] == '-h':
        code_method.show_help()
    elif sys.argv[1] in switcher:
        list_parameter = sys.argv[1:]
        print(switcher[sys.argv[1]](list_parameter))
    else:
        print("Please enter the correct format to get the data.\nType --help, -h for help")

if __name__ == '__main__':
    codeforces()