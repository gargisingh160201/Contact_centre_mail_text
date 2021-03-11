
recieved_string = " hello I am having issues in using hello. The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails."
string_to_be_removed = "The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails"
# removing substring from end
res=" "
if recieved_string.endswith(string_to_be_removed ):
    res = recieved_string [: (len(string_to_be_removed ))]
print(res)
