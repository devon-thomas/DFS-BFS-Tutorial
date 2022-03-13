#when making a DFS, we use a stack 
# note, BFS uses a queue
from collections import deque

#this is a recursive approach to DFS
def dfs(visited, graph, node):
	if node not in visited:
		print(node)
		visited.add(node)
		for neighbor in graph[node]:
			dfs(visited,graph,neighbor)


#for a BFS, we need to implement a queue using deque


def bfs(graph, node):
	visited = set()
	queue = deque()
	queue.append(node) #adds to last 
	while queue:
			current = queue.popleft() #removes from front, finish FIFO structure
			print(current)
			for neighbor in graph[current]:
				if neighbor not in visited:
					queue.append(neighbor)
					visited.add(neighbor)


		



#drive the dfs 
#graph represented as an adjanceny list
graph = {
	'5' : ['3','7'],
	'3' : ['2', '4'],
	'7' : ['8'],
	'2' : [],
	'4' : ['8'],
	'8' : []
}

visited = set() #use a set that doesnt double count, each item is unique
queue = deque()

startnode = '5'

print("here is a DFS starting at " + startnode)
dfs(visited,graph,startnode)

print("here is a BFS starting at " + startnode)
bfs(graph,startnode)


# print(visited)