import Utilities.List;
import Utilities.Node;
import Utilities.Stack;
import Utilities.Queue;
import java.util.Arrays;

/*
	TODO
		Test DFS
		Test BFS
		Fix dijkstraMax
*/
public class Graph
{
    // instance variables
	private Vertex[] vertices;
	private Edge[][] adj;
    private int numV;
    private Boolean directed;

    // constructor, accepts whether graph is directed or not
    public Graph(Boolean d)
    {
		vertices = new Vertex[35];
		adj = new Edge[35][35];
        numV = 0;
        directed = d;
    }

    // accessors and mutators
    public int getNumV()
    {
        return numV;
    }

    public void setNumV(int n)
    {
        numV = n;
    }

	public Vertex[] getVertices()
	{
		return vertices;
	}

    public Edge[][] getAdj()
    {
        return adj;
    }

    public Boolean getDirected()
    {
        return directed;
    }

    public void setDirected(Boolean d)
    {
        directed = d;
    }

    // traverses graph, printing all vertices
	// "s" parameter indicates starting vertex
	// "method" parameter indicates DFS - "depth" or BFS - "breadth"
    public Stack[] traversal(Vertex s, String method)
    {
		int[] path = new int[numV];
		Arrays.fill(path, -1);

		Boolean[] visited = new Boolean[numV];
		Arrays.fill(visited, false);

		Stack[] spanningTree = new Stack[numV];

        switch (method)
		{
        	case "depth":
				DFS(s.getIndex(), path, visited);
				break;
			case "breadth":
				BFS(s.getIndex(), path, visited);
				break;
        }

		int curr;
		for(int i = 0; i < path.length; i++)
		{
			spanningTree[i].push(i);
			curr = path[i];
			while(curr != -1)
			{
				spanningTree[i].push(curr);
				curr = path[i];
			}
		}
		return spanningTree;
    }

	private void DFS(int s, int[] path, Boolean[] visited)
	{
		for(int i = 0; i < numV; i++)
		{
			if((adj[s][i] != null) && !visited[i])
			{
				path[i] = s;
				visited[i] = true;
				DFS(i, path, visited);
			}
		}
		return;
	}

	private void BFS(int s, int[] path, Boolean[] visited)
	{
		int numVisited = 0, curr; // keeps track of how many vertices have been visited
		Queue<Integer> toVisit = new Queue<Integer>();

		// queue up starting vertex
		toVisit.enqueue(s);

		// loop while not all nodes have been visited
		while(numVisited < numV)
		{
			// set curr to vertex in front of queue, and mark vertex as visited
			curr = toVisit.dequeue();
			visited[curr] = true;
			numVisited++;

			// loop through adjacency matrix at index "curr"
			for(int i = 0; i < numV; i++)
			{
				// if adjacency exists between vertex curr and i, enqueue i
				if((adj[curr][i] != null) && !visited[i])
				{
					toVisit.enqueue(i);
					path[i] = curr;
				}
			}
		}

		return;
	}

    // returns edge that connects two vertices
    public Edge getEdge(Vertex s, Vertex d)
    {
        return adj[s.getIndex()][d.getIndex()];
    }

    // adds edge to adj
    public void addEdge(Edge e)
    {
		// gets endpoints of passed edge
		Vertex[] ends = e.endpoints();

		// if either vertex of edge is not in graph, exit method
		if(ends[0].getIndex() != -1)
			if(ends[0] != vertices[ends[0].getIndex()])
				return;
		if(ends[1].getIndex() != -1)
			if(ends[1] != vertices[ends[1].getIndex()])
				return;

		// modify adjacency matrix
		adj[ends[0].getIndex()][ends[1].getIndex()] = e;

		// if graph is not directed, add adjacency from dest to src
		if(!directed)
		{
			adj[ends[1].getIndex()][ends[0].getIndex()] = e;
		}
    }

    // removes edge from adj
    public void remEdge(Edge e)
    {
		// gets endpoints of passed edge
        Vertex[] ends = e.endpoints();

		// if edge is in adjacency matrix, modify adjacency matrix
		if(adj[ends[0].getIndex()][ends[1].getIndex()] == e)
			adj[ends[0].getIndex()][ends[1].getIndex()] = null;
		// if edge is not in adjacency matrix, exit method
		else
			return;

		// if graph is not directed, remove adjacency from dest to src
		if(!directed)
		{
			adj[ends[1].getIndex()][ends[0].getIndex()] = null;
		}
    }

    // add vertex to Graph
    public void addVertex(Vertex v)
    {
		// set index of vertex to current value of numV
		v.setIndex(numV);

		// add vertex to list of vertices
		vertices[numV] = v;

		// increment vertex counter
		numV++;
    }

    // returns degree of a vertex
    public int degree(Vertex v)
    {
        int count = 0;

		// loop through adjacency matrix at index of vertex
		// if adj[v.index][i] is not null, increment count
		for(int i = 0; i < adj[v.getIndex()].length; i++)
		{
			if(adj[v.getIndex()][i] !=  null)
				count++;
		}

		return count;
    }

    // returns all outgoing edges of a vertex
    public List<Edge> incidentEdges(Vertex v)
    {
        List<Edge> outEdges = new List<Edge>();

		// loop through adjacency matrix at index of vertex
		// if adj[v.index][i] is not null, append edge to list
		for(int i = 0; i < adj[v.getIndex()].length; i++)
		{
			if(adj[v.getIndex()][i] !=  null)
				outEdges.InsertAfter(adj[v.getIndex()][i]);
		}

		return outEdges;
    }

    // returns sum of weights of all edges
    public int edgeSum()
    {
        int sum = 0;

		for(int i = 0; i < adj.length; i++)
			for(int k = 0; k < adj[0].length; k++)
			{
				if(adj[i][k] !=  null)
					sum += adj[i][k].getWeight();
			}

		return sum;
    }

	// creates a shortest path tree using dijkstras algorithm
	public Stack[] dijkstra(Vertex start)
	{
        // variables
		Boolean known[] = new Boolean[numV];
		int cost[] = new int[numV];
		int path[] = new int[numV];
        int cheapest;

		// set all values in known to false
		Arrays.fill(known, false);

		// set all values in cost to "infinity"
		Arrays.fill(cost, Integer.MAX_VALUE);

		// set all values in path to -1
		Arrays.fill(path, -1);

		// cost from start vertex to itself is 0
		cost[start.getIndex()] = 0;

        // fill path array
        for(int j = 0; j < known.length; j++)
        {
			// reset cheapest index
			cheapest = -1;

            // find lowest cost unknown vertex
            for(int i = 0; i < cost.length; i++)
            {
				// if no cheapest index has been previously set, select first unknown vertex as cheapest
				if((cheapest == -1) && !known[i])
					cheapest = i;
				else if(cheapest != -1)
                	if((cost[i] < cost[cheapest]) && !known[i])
                    	cheapest = i;
            }

            // set cheapest node to known = true
            known[cheapest] = true;

            // iterate through adjacency matrix for cheapest node
            for(int i = 0; i < numV; i++)
            {
                // if element of adjacency array isn't null
                if(adj[cheapest][i] != null)
                {
                    // if cost[i] is greater than the combined cost of
                    // cost[cheapest] + edge weight, set cost[i] = cost[cheapest] + edge weight
                    // and update the path array at path[i] to the cheapest index
                    if(cost[i] > cost[cheapest] + adj[cheapest][i].getWeight())
                    {
                        cost[i] = cost[cheapest] + adj[cheapest][i].getWeight();
                        path[i] = cheapest;
                    }
                }
            }
        }

        // generate paths
		Stack[] shortPaths = new Stack[numV];
		Stack<Integer> stack;

		for (int i = 0; i < path.length; i++)
		{
			stack = new Stack<Integer>();

			// push vertex's index to the stack:
			stack.push(i);

			// then analize next vertex (which value is held in path array):
			int cur = path[i];
			while (cur != -1)
			{
				stack.push(cur);
				cur = path[cur];
			}

			// stack now has the path to vertices[i]
			shortPaths[i] = stack;
		}

		return shortPaths;
	}

	// creates a minimum spanning tree using the prim-jarnik algorithm
	// help from geeksforgeeks (https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)
	public Stack[] primJarnik(Vertex start)
	{
		int smallest = -1; // keeps track of index with smallest keyVal
		int numInTree = 0; // keeps track of the number of vertexes set to true in inTree

		// array keeps track of which vertices have been visited
		Boolean[] inTree = new Boolean[numV];
		Arrays.fill(inTree, false);

		// array keeps track of previous vertex in path
		int[] path = new int[numV];
		Arrays.fill(path, -1);

		// keeps track of key values for each vertex in graph
		int[] cost = new int[numV];
		Arrays.fill(cost, Integer.MAX_VALUE);

		// set values in inTree and cost for the starting vertex
		cost[start.getIndex()] = 0;

		// loop while not all vertexes have been added to MST
		while(numInTree < numV)
		{
			smallest = -1;
			// find vertex with smallest keyVal that is false in inTree
			for(int i = 0; i < cost.length; i++)
			{
				// if no smallest index has been set and the current vertex is not in tree, set as smallest
				if((smallest == -1) && !inTree[i])
					smallest = i;
				// if smallest index has been set, check if current index has lower keyVal than smallest
				else if(smallest != -1)
					if((cost[i] < cost[smallest]) && !inTree[i])
						smallest = i;
			}

			// set inTree[smallest] to true and increment numInTree counter
			inTree[smallest] = true;
			numInTree++;

			// update cost for adjacent vertexes of smallest
			for(int i = 0; i < numV; i++)
			{
				// if an edge exists between smallest and i and is less than weight in cost
				if((adj[smallest][i] != null) && (adj[smallest][i].getWeight() < cost[i]) && !inTree[i])
				{
					cost[i] = adj[smallest][i].getWeight();
					path[i] = smallest;
				}
			}
		}

		// generate paths
		Stack[] mstPaths = new Stack[numV];
		Stack<Integer> stack;

		for (int i = 0; i < path.length; i++)
		{
			stack = new Stack<Integer>();

			// push vertex's index to the stack:
			stack.push(i);

			// then analize next vertex (which value is held in path array):
			int cur = path[i];
			while (cur != -1)
			{
				stack.push(cur);
				cur = path[cur];
			}

			// stack now has the path to vertices[i]
			mstPaths[i] = stack;
		}

		return mstPaths;
	}

	// creates a mmaximum spanning tree using the prim-jarnik algorithm
	// help from geeksforgeeks (https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)
	public Stack[] primJarnikMax(Vertex start)
	{
		int largest = -1; // keeps track of index with largest keyVal
		int numInTree = 0; // keeps track of the number of vertexes set to true in inTree

		// array keeps track of which vertices have been visited
		Boolean[] inTree = new Boolean[numV];
		Arrays.fill(inTree, false);

		// array keeps track of previous vertex in path
		int[] path = new int[numV];
		Arrays.fill(path, -1);

		// keeps track of key values for each vertex in graph
		int[] cost = new int[numV];
		Arrays.fill(cost, 0);

		// set values in inTree and cost for the starting vertex
		cost[start.getIndex()] = Integer.MAX_VALUE;

		// loop while not all vertexes have been added to MST
		while(numInTree < numV)
		{
			largest = -1;
			// find vertex with largest keyVal that is false in inTree
			for(int i = 0; i < cost.length; i++)
			{
				// if no largest index has been set and the current vertex is not in tree, set as largest
				if((largest == -1) && !inTree[i])
					largest = i;
				// if largest index has been set, check if current index has higher keyVal than largest
				else if(largest != -1)
					if((cost[i] > cost[largest]) && !inTree[i])
						largest = i;
			}

			// set inTree[largest] to true and increment numInTree counter
			inTree[largest] = true;
			numInTree++;

			// update cost for adjacent vertexes of largest
			for(int i = 0; i < numV; i++)
			{
				// if an edge exists between largest and i and is greater than weight in cost
				if((adj[largest][i] != null) && (adj[largest][i].getWeight() > cost[i]) && !inTree[i])
				{
					cost[i] = adj[largest][i].getWeight();
					path[i] = largest;
				}
			}
		}

		// generate paths
		Stack[] mstPaths = new Stack[numV];
		Stack<Integer> stack;

		for (int i = 0; i < path.length; i++)
		{
			stack = new Stack<Integer>();

			// push vertex's index to the stack:
			stack.push(i);

			// then analize next vertex (which value is held in path array):
			int cur = path[i];
			while (cur != -1)
			{
				stack.push(cur);
				cur = path[cur];
			}

			// stack now has the path to vertices[i]
			mstPaths[i] = stack;
		}

		return mstPaths;
	}

	public int treeDistance(Stack[] paths)
	{
		int totalDist = 0, var;
		Stack<Integer> curr = new Stack<Integer>();
		Stack<Integer> goBack = new Stack<Integer>();
		Boolean[][] usedEdges = new Boolean[numV][numV];

		// fill usedEdges with false
		for(Boolean[] val : usedEdges)
			Arrays.fill(val, false);

		// loop through each path stack
		for(int i = 0; i < paths.length; i++)
		{
		    // set paths[i] = curr
			curr = paths[i];

			// while more than one index remains on path array
			while(curr.GetSize() != 1)
			{
				// get index from top of stack
				var = curr.pop();
				goBack.push(var);

				// if edge has not been previously added, add to total dist
				if(!usedEdges[var][curr.peek()])
				{
					totalDist += adj[var][curr.peek()].getWeight();
					usedEdges[var][curr.peek()] = true;
				}
			}

			while(!goBack.IsEmpty())
				curr.push(goBack.pop());
		}

		return totalDist;
	}

	public void printPath(Stack<Integer> path)
	{
		int dist = 0, var;
		String output = "";
		Stack<Integer> curr = path;
		Stack<Integer> goBack = new Stack<Integer>();

		// if only one element in path stack, then path is for starting vertex
		if(curr.GetSize() == 1)
			output = "Path: " + vertices[curr.pop()].getData() + " Total Distance: 0";
		else
		{
			output = "Path: ";
			while(!curr.IsEmpty())
			{
				// get index from top of stack
				var = curr.pop();
				goBack.push(var);
				output = output + vertices[var].getData();

				if(curr.peek() == null)
					break;

				output = output + " > ";

				// add weight of edge
				dist += adj[var][curr.peek()].getWeight();
			}
			output = output + " Total Distance: " + dist;
		}

		while(!goBack.IsEmpty())
			curr.push(goBack.pop());

		System.out.println(output + "\n");
		return;
	}
}
