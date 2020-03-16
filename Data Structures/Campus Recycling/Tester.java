/*
* 	I attempted to put our graph into code.
*/
import Utilities.Stack;
public class Tester
{
	public static void main(String[] args)
	{
/*		Graph graph1 = new Graph(false);
		Graph graph2 = new Graph(true);

		// create test vertices
		Vertex v0 = new Vertex("Vertex 0");
		graph1.addVertex(v0);
		graph2.addVertex(v0);
		Vertex v1 = new Vertex("Vertex 1");
		graph1.addVertex(v1);
		graph2.addVertex(v1);
		Vertex v2 = new Vertex("Vertex 2");
		graph1.addVertex(v2);
		graph2.addVertex(v2);
		Vertex v3 = new Vertex("Vertex 3");
		graph1.addVertex(v3);
		graph2.addVertex(v3);
		Vertex v4 = new Vertex("Vertex 4");
		graph1.addVertex(v4);
		graph2.addVertex(v4);
		Vertex v5 = new Vertex("Vertex 5");
		graph1.addVertex(v5);
		graph2.addVertex(v5);
		Vertex v6 = new Vertex("Vertex 6");
		graph1.addVertex(v6);
		graph2.addVertex(v6);
		Vertex v7 = new Vertex("Vertex 7");
		graph1.addVertex(v7);
		graph2.addVertex(v7);

		// create test edges
		// graph 1
		graph1.addEdge(new Edge(v0, v1, 3));
		graph1.addEdge(new Edge(v0, v3, 4));
		graph1.addEdge(new Edge(v1, v6, 5));
		graph1.addEdge(new Edge(v2, v5, 4));
		graph1.addEdge(new Edge(v2, v4, 4));
		graph1.addEdge(new Edge(v3, v5, 9));
		graph1.addEdge(new Edge(v3, v7, 4));
		graph1.addEdge(new Edge(v4, v6, 8));
		graph1.addEdge(new Edge(v5, v7, 2));
		graph1.addEdge(new Edge(v5, v6, 9));
		graph1.addEdge(new Edge(v6, v7, 4));

		// test diskstras
		Stack[] paths = graph1.primJarnikMax(v0);

		for(int i = 0; i < paths.length; i++)
		{
			System.out.println(paths[i]);
		}*/

		Graph draft = new Graph(true);

		Vertex v21 = new Vertex("F. Jay. Taylor ");
		Vertex v45 = new Vertex("Memorial Gym");
		Vertex v27_57 = new Vertex("Hale & Robinson Halls");
		Vertex v25 = new Vertex("GTM");
		Vertex v69 = new Vertex("University Hall");
		Vertex v13 = new Vertex("COB");
		Vertex v19 = new Vertex("Education Center");
		Vertex v10 = new Vertex("Bogard");
		Vertex v20_47 = new Vertex("Annex & Nethken");
		Vertex v29 = new Vertex("Howard Auditorium");
		Vertex v11 = new Vertex("Carson-Taylor");
		Vertex v16 = new Vertex("Davison");
		Vertex v2 = new Vertex("Adams classroom");
		Vertex v30_9 = new Vertex("Micromanufacturing & Biomed");
		Vertex v75_7_51_1 = new Vertex("Woodard & Band & Planetarium & A.E. Phillips Lab School");

		draft.addVertex(v21);
		draft.addVertex(v45);
		draft.addVertex(v27_57);
		draft.addVertex(v25);
		draft.addVertex(v69);
		draft.addVertex(v13);
		draft.addVertex(v19);
		draft.addVertex(v10);
		draft.addVertex(v20_47);
		draft.addVertex(v29);
		draft.addVertex(v11);
		draft.addVertex(v16);
		draft.addVertex(v2);
		draft.addVertex(v30_9);
		draft.addVertex(v75_7_51_1);

		draft.addEdge((new Edge(v21, v30_9, 1562)));
		draft.addEdge((new Edge(v30_9, v21, 1562)));

		draft.addEdge(new Edge(v21, v45, 1051));
		draft.addEdge(new Edge(v45, v21, 1051));

		draft.addEdge(new Edge(v45, v27_57, 270));
		draft.addEdge(new Edge(v27_57, v45, 270));

		draft.addEdge(new Edge(v27_57, v25, 460));
		draft.addEdge(new Edge(v25, v27_57, 460));

		draft.addEdge(new Edge(v25, v69, 428));
		draft.addEdge(new Edge(v69, v25, 428));

		draft.addEdge(new Edge(v69, v13, 1584));
		draft.addEdge(new Edge(v13, v69, 1056));

		draft.addEdge(new Edge(v13, v19, 428));
		draft.addEdge(new Edge(v19, v13, 428));

		draft.addEdge(new Edge(v13, v10, 1032));
		draft.addEdge(new Edge(v10, v13, 1032));

		draft.addEdge(new Edge(v10, v20_47, 150));
		draft.addEdge(new Edge(v20_47, v10, 150));

		draft.addEdge(new Edge(v10, v29, 260));

		draft.addEdge(new Edge(v29, v11, 160));

		draft.addEdge(new Edge(v11, v10, 72));

		draft.addEdge(new Edge(v11, v16, 1477));
		draft.addEdge(new Edge(v16, v11, 1477));

		draft.addEdge(new Edge(v16, v2, 170));
		draft.addEdge(new Edge(v2, v16, 170));

		draft.addEdge(new Edge(v16, v30_9, 1844));
		draft.addEdge(new Edge(v30_9, v16, 1844));

		draft.addEdge(new Edge(v16, v75_7_51_1, 1956));
		draft.addEdge(new Edge(v75_7_51_1, v16, 1956));

		draft.addEdge(new Edge(v75_7_51_1, v25, 997));

		// test diskstras
		Stack[] paths = draft.dijkstra(v21);

		for(int i = 0; i < paths.length; i++)
		{
			System.out.println(paths[i]);
		}
	}
}
