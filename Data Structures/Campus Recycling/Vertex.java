public class Vertex
{
    // instance variables
    private String data;
	private int index;

    // default constructor
    public Vertex()
    {
        data = null;
		index = -1;
    }

    // constructor, accepts data and index
    public Vertex(String d)
    {
        data = d;
		index = -1;
    }

    // accessors and mutators
    public String getData()
    {
        return data;
    }

    public void setData(String d)
    {
        data = d;
    }

	public int getIndex()
	{
		return index;
	}

	public void setIndex(int i)
	{
		index = i;
	}
}
