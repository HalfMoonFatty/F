'''
Problem: 合并邮件列表

Given some email ids, and a similarity function which says whether two email ids are similar, 
determine all the sets of email ids that are similar to each other.

Given 1 million email list:
list 1: a@a.com, b@b.com
list 2: b@b.com, c@c.com
list 3: e@e.com
list 4: a@a.com
...
Combine lists with identical emails, and output tuples:
(list 1, list 2, list 4) (a@a.com, b@b.com, c@c.com)
(list 3) (e@e.com)

'''
