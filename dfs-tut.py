#when making a DFS, we use a stack 
# note, BFS uses a queue

graph = {
	'5' : ['3',' 7'],
	'3' : ['2', '4'],
	'7' : ['8'],
	'2' : [],
	'4' : ['8'],
	'8' : []
}

visited = set() #use a set that doesnt double count, each item is unique

def dfs(visited, graph, node):
	if node not in visited:
		print(node)
		visited.add(node)
		for neighbor in graph[node]:
			dfs(visited,graph,neighbor)


#drive the dfs 

print("here is a DFS")
dfs(visited,graph,'5')



