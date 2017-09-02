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



import collections

def contactGroup(contact):

    def findRoot(unionSet, root):
        if root == unionSet[root]:
            return root
        unionSet[root] = findRoot(unionSet, unionSet[root])
        return unionSet[root]


    def union(unionSet, root1, root2):
        root1 = findRoot(unionSet, unionSet[root1])
        root2 = findRoot(unionSet, unionSet[root2])
        unionSet[root1] = root2
        return


    emailToPerson = {}
    unionSet = {}    # as need to group by keys

    for person in contact.keys():
        unionSet[person] = person
        curRoot = person

        for email in contact[person]:
            if not emailToPerson.has_key(email):
                emailToPerson[email] = person
                continue
                
            newRoot = findRoot(unionSet, emailToPerson[email])
            if newRoot != curRoot:
                union(unionSet, newRoot, curRoot)
                curRoot = newRoot


    emails = collections.defaultdict(set)
    names = collections.defaultdict(set)
    for person in unionSet.keys():
        root = findRoot(unionSet,person)
        emails[root] |= set(contact[person])
        names[root].add(person)
    return zip([tuple(elem) for elem in names.values()],
               [tuple(elem) for elem in emails.values()])
    

contact = {1:["a@a.com", "b@b.com"], 2:["b@b.com", "c@c.com"], 3:["e@e.com"], 4:["a@a.com"]}
print contactGroup(contact)

