public class Edge
{
    // instance variables
    private Vertex src, dest;
    private int weight;

    // default constructor
    public Edge()
    {
        src = null;
        dest = null;
        weight = 0;
    }

    // constructor, accepts source and destination vertex along with weight
    public Edge(Vertex s, Vertex d, int w)
    {
        src = s;
        dest = d;
        weight = w;
    }

    // accessors and mutators
    public Vertex getSrc()
    {
        return src;
    }

    public void setSrc(Vertex s)
    {
        src = s;
    }

    public Vertex getDest()
    {
        return dest;
    }

    public void setDest(Vertex d)
    {
        dest = d;
    }

    public int getWeight()
    {
        return weight;
    }

    public void setWeight(int w)
    {
        weight = w;
    }

    // returns array of both endpoints
    public Vertex[] endpoints()
    {
        Vertex[] endPts = {src, dest};
        return endPts;
    }

    // returns vertex opposite of the one passed,
    // or null if the vertex does not match the edge
    public Vertex opposite(Vertex v)
    {
        if(v == src)
            return dest;
        else if(v == dest)
            return src;
        else
            return null;
    }
}
