class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # builds adj list in order, with the smallest airports last in the list
        for source, destination in sorted(tickets)[::-1]:
            adj[source].append(destination)
        res = []
        def dfs(source):
            # while there are still connecting nodes
            while adj[source]:
                # get the next smallest destination
                destination = adj[source].pop()
                dfs(destination)
            res.append(source)
        dfs('JFK')
        return res[::-1]

#Input: tickets = [["BUF","HOU"],["HOU","SEA"] ["JFK","BUF"]]
# Output: ["JFK","BUF","HOU","SEA"]

# We append a node only after all of its outgoing edges have been consumed

# pop -> JFK : HOU, 
# JFK : HOU(1), SEA (3)
# HOU : JFK (2)
# SEA : JFK (4)

# res : JFK, SEA, 

# dfs(JFK) 
    # dfs(HOU) POP HOU(1)
        # dfs(JFK) POP JFK(2)
            #  dfs(SEA) POP SEA(3)
                # dfs(JFK) POP JFK(4)
                # NO MORE NEIGHBOURS

# an airport is a graph node, ticket is directed edge
    # use each edge exactly once
# we cannot add each aiport to the result as soon as we visit it
    # only after there are no more conecting edges we add

# sort and reverse tickets
    # gives us alphabetical order, and puts the smallest destination at the end

# JFK : SFO, ATL
# ATL : SFO, JFK
# SFO : ATL


# dfs(JFK)
    # dfs(ATL)
        # dfs(JFK)
            # dfs(SFO)
                # dfs(ATL)
                    # dfs(SFO)
                        # no more neighbours

# SFO, ATL, SFO, JFK, ATL, JFK[::-1]