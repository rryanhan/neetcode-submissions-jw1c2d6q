class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_Ids = {} # maps an email to an ID
        emails = [] # sets of emails of all accounts
        email_to_account = {} # maps email_id to account_index
            # this lets us find the name, or the big group we want to merge to

        m = 0
        for account_index, account in enumerate(accounts):
            for i in range(1, len(account)): # exclude the name
                email = account[i]
                if email in email_Ids:
                    continue
                email_Ids[email] = m
                emails.append(email)
                email_to_account[m] = account_index
                m += 1
        # next, we build a graph of emails that are connected
        adj = [[] for _ in range(m)]
            # email_id -> emails that it connects to
        for a in accounts:
            for i in range(2, len(a)): # ignore name, and we 
                id1 = email_Ids[a[i]]
                id2 = email_Ids[a[i - 1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
        
        emailGroup = defaultdict(list) # index of account -> list of emails
        visited = [False] * m

        def dfs(emailId, accountId):
            visited[emailId] = True
            emailGroup[accountId].append(emails[emailId]) # attach email to account Id
            for connected_emails in adj[emailId]:
                if not visited[connected_emails]:
                    dfs(connected_emails, accountId)
        
        for email_Id in range(m):
            if not visited[email_Id]:
                dfs(email_Id, email_to_account[email_Id])
        
        res = []
        for accountId in emailGroup:
            name = accounts[accountId][0]
            res.append([name] + sorted(emailGroup[accountId]))
        return res


        



#DFS SOLUTION
    # assign each email an ID
    # connect emails appearing in the same account
    # DFS each connected component
    # attach the owner's name

    # shared emails create indirect connections
# account -> email
# email -> account index


