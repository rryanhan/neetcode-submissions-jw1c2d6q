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


        



# an airport is a graph node, ticket is directed edge
    # use each edge exactly once
# we cannot add each aiport to the result as soon as we visit it
    # only after there are no more conecting edges we add

# sort and reverse tickets
    # gives us alphabetical order, and puts the smallest destination at the end