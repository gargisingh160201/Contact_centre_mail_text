import doctest
def trim_the_mail(input_text_mail):
    n= len(input_text_mail)
    res=" "
    # We don't have the 'on' keyword in the ending ui generating text . So trying to get the index of that, but the input_text_mail can contain 'on' keyword so running from end.
    for i in range(n-1,-1,-2):
        if input_text_mail[i] =='o' and input_text_mail[i+1]=='n':
            first_ind=i
            break
     res=res+ input_text_mail[:i]
     word = 'reference'
     index = string.find ( word )
     

     end_string_to_be_removed = "The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails"
     # removing substring from end
    
    if input_text_mail.endswith(string_to_be_removed ):
          res = res + input_text_mail[index+10 : (len(string_to_be_removed ))]
    
    '''  (input_text_mail) -> res
    return the res ie the final clean string
    
    input_text_mail = " Gargi Singh
    On Mar 11 2021, at 10:24 pm, Gargi Singh <tcs_indore@hellomailtest.msg91.com> wrote:
    Your ticket id is #542 please use this for reference 
    The views and opinions included in this email belong to their author and do not necessarily mirror the views 
    and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. 
    Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees 
    are fully responsible for the content of their emails."
    >>> trim_the_mail(input_text_mail):
         Gargi Singh
         
    input_text_mail = " I am not available on monday"
    On Mar 11 2021, at 10:24 pm, Gargi Singh <tcs_indore@hellomailtest.msg91.com> wrote:
    Your ticket id is #542 please use this for reference 
    The views and opinions included in this email belong to their author and do not necessarily mirror the views 
    and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. 
    Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees 
    are fully responsible for the content of their emails."
    >>> trim_the_mail(input_text_mail):
         I am not available on monday
         
    >>> Doctest.testload()
     
     
