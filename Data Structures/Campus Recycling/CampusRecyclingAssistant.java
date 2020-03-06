/*
    Breno Yamada Riquieri
    CSC325 Advanced Data Structures
    Assignment: Campus Recycling Program
*/

// imports
import java.util.Scanner;
import Utilities.Stack;
import java.text.DecimalFormat;

public class CampusRecyclingAssistant
{
    public static void main(String[] args)
    {
		DecimalFormat df = new DecimalFormat(".##");
        int dijkstraDist, primMinDist, primMaxDist, startVertex;
        long dijkstraDurr, primMinDurr, primMaxDurr, startTime, endTime;
        Scanner kb = new Scanner(System.in);
        Stack[] shortPathTree, minSpanTree, maxSpanTree;
        Graph campusGraph = new Graph(true);

        // create vertices for academic buildings
		Vertex v21 = new Vertex("F. Jay. Taylor ");
		Vertex v45 = new Vertex("Memorial Gym");
		Vertex v27_57 = new Vertex("Hale & Robinson Halls");
		Vertex v25 = new Vertex("George T Madison");
		Vertex v69 = new Vertex("University Hall");
		Vertex v13 = new Vertex("College of Business");
		Vertex v19 = new Vertex("Education Center");
		Vertex v10_v29 = new Vertex("Bogard & Howard Auditorium");
		Vertex v20_47 = new Vertex("Annex & Nethken");
		Vertex v11 = new Vertex("Carson-Taylor");
		Vertex v16 = new Vertex("Davison");
		Vertex v2 = new Vertex("Adams classroom");
		Vertex v30_9 = new Vertex("Micromanufacturing & Biomed");
		Vertex v75_7_51_1 = new Vertex("Woodard & Band & Planetarium & A.E. Phillips Lab School");

        // add vertices to graph
		campusGraph.addVertex(v21);
		campusGraph.addVertex(v45);
		campusGraph.addVertex(v27_57);
		campusGraph.addVertex(v25);
		campusGraph.addVertex(v69);
		campusGraph.addVertex(v13);
		campusGraph.addVertex(v19);
		campusGraph.addVertex(v10_v29);
		campusGraph.addVertex(v20_47);
		campusGraph.addVertex(v11);
		campusGraph.addVertex(v16);
		campusGraph.addVertex(v2);
		campusGraph.addVertex(v30_9);
		campusGraph.addVertex(v75_7_51_1);

        // add edges between "adjacent" buildings
        // F Jay Taylor <-> Micromanufacturing & Biomed
		campusGraph.addEdge((new Edge(v21, v30_9, 1562)));
		campusGraph.addEdge((new Edge(v30_9, v21, 1562)));

        // F Jay Taylor <-> Memorial Gym
		campusGraph.addEdge(new Edge(v21, v45, 1051));
		campusGraph.addEdge(new Edge(v45, v21, 1051));

        // Memorial Gym <-> Hale & Robinson Halls
		campusGraph.addEdge(new Edge(v45, v27_57, 270));
		campusGraph.addEdge(new Edge(v27_57, v45, 270));

        // Hale & Robinson Halls <-> George T Madison
		campusGraph.addEdge(new Edge(v27_57, v25, 460));
		campusGraph.addEdge(new Edge(v25, v27_57, 460));

        // George T Madison <-> University Hall
		campusGraph.addEdge(new Edge(v25, v69, 428));
		campusGraph.addEdge(new Edge(v69, v25, 428));

        // University Hall <-> College of Business
		campusGraph.addEdge(new Edge(v69, v13, 1584));
		campusGraph.addEdge(new Edge(v13, v69, 1056));

        // College of Business <-> Education Center
		campusGraph.addEdge(new Edge(v13, v19, 428));
		campusGraph.addEdge(new Edge(v19, v13, 428));

        // College of Business <-> Bogard & Howard Auditorium
		campusGraph.addEdge(new Edge(v13, v10_v29, 1032));
		campusGraph.addEdge(new Edge(v10_v29, v13, 1032));

        // Bogard & Howard Auditorium <-> Annex & Nethkin
		campusGraph.addEdge(new Edge(v10_v29, v20_47, 151));
		campusGraph.addEdge(new Edge(v20_47, v10_v29, 151));

        // Carson-Taylor <-> Bogard & Howard Auditorium
		campusGraph.addEdge(new Edge(v11, v10_v29, 72));
		campusGraph.addEdge(new Edge(v10_v29, v11, 72));

        // Carson-Taylor <-> Davison
		campusGraph.addEdge(new Edge(v11, v16, 1477));
		campusGraph.addEdge(new Edge(v16, v11, 1477));

        // Davison <-> Adams Classrooms
		campusGraph.addEdge(new Edge(v16, v2, 170));
		campusGraph.addEdge(new Edge(v2, v16, 170));

        // Davison <-> Micromanufacturing & Biomed
		campusGraph.addEdge(new Edge(v16, v30_9, 1844));
		campusGraph.addEdge(new Edge(v30_9, v16, 1844));

        // Davison <-> Woodard & Band & Planetarium & A.E. Phillips Lab School
		campusGraph.addEdge(new Edge(v16, v75_7_51_1, 1956));
		campusGraph.addEdge(new Edge(v75_7_51_1, v16, 1956));

        // Woodard & Band & Planetarium & A.E. Phillips Lab School -> George T Madison
		campusGraph.addEdge(new Edge(v75_7_51_1, v25, 997));
		campusGraph.addEdge(new Edge(v25, v75_7_51_1, 997));

        // print prompt
        System.out.println("Select start location for route:");

        // print list of vertices
        for(int i = 0; i < campusGraph.getNumV(); i++)
            System.out.println(i + ": " + campusGraph.getVertices()[i].getData());

        // get user input for starting vertex
        startVertex = kb.nextInt();

        // run graph analysis

		System.out.println("\nMinimun spanning tree results for:");

        // generate shortest path tree from starting vertex
        startTime = System.nanoTime();
        shortPathTree = campusGraph.dijkstra(campusGraph.getVertices()[startVertex]);
        endTime = System.nanoTime();
        dijkstraDurr = endTime - startTime;
		System.out.println("Dijkstra: " + df.format(dijkstraDurr/1000000.0) + " ms");
		dijkstraDist = campusGraph.treeDistance(shortPathTree);
		System.out.println("Dijkstra Distance: " + dijkstraDist + " ft.\n");

        // generate minimum spanning tree from starting vertex
        startTime = System.nanoTime();
        minSpanTree = campusGraph.primJarnik(campusGraph.getVertices()[startVertex]);
        endTime = System.nanoTime();
        primMinDurr = endTime - startTime;
		System.out.println("PrimJarnik: " + df.format(primMinDurr/1000000.0) + " ms");
		primMinDist = campusGraph.treeDistance(minSpanTree);
		System.out.println("Prim Distance: " + primMinDist + " ft.");

		System.out.println("\nMaximum spanning tree results for:");

        // generate maximum spanning tree from starting vertex
        startTime = System.nanoTime();
        maxSpanTree = campusGraph.primJarnikMax(campusGraph.getVertices()[startVertex]);
        endTime = System.nanoTime();
        primMaxDurr = endTime - startTime;
		System.out.println("PrimJarnik: " + df.format(primMaxDurr/1000000.0) + " ms");
		primMaxDist = campusGraph.treeDistance(maxSpanTree);
		System.out.println("Distance: " + primMaxDist + " ft.\n");

		System.out.println("\nShortest Paths From Start Building to All Others");
		for(int i = 0; i < shortPathTree.length; i++)
		{
			System.out.print(campusGraph.getVertices()[i].getData() + ":\n\t");
			campusGraph.printPath(shortPathTree[i]);
		}

		System.out.println("\nMinimum Spanning Tree Paths From Start Building to All Others");
		for(int i = 0; i < minSpanTree.length; i++)
		{
			System.out.print(campusGraph.getVertices()[i].getData() + ":\n\t");
			campusGraph.printPath(minSpanTree[i]);
		}

		System.out.println("\nMaximum Spanning Tree Paths From Start Building to All Others");
		for(int i = 0; i < maxSpanTree.length; i++)
		{
			System.out.print(campusGraph.getVertices()[i].getData() + ":\n\t");
			campusGraph.printPath(maxSpanTree[i]);
		}
    }
}
