package Utilities;

public class PatternMatching
{
    public PatternMatching(){}

    // performs a brute force pattern match
    public static void bruteForce(List<Character> text, List<Character> pattern)
    {
        // variables
        int len = 0, matches = 0;
        List<Integer> indexes = new List<Integer>();

        // adds blank character to end of text list so that the last character
        // gets checked for match
        text.Last();
        text.InsertAfter(' ');

        // set curr of both lists to the first element
        text.First();
        pattern.First();
        do
        {
            if(text.GetValue().equals(pattern.GetValue()))
            {
                if(pattern.GetPos() == (pattern.GetSize() - 1))
                {
                    matches++;
                    len = 0;
                    indexes.InsertAfter(text.GetPos() - (pattern.GetSize() - 1));
                    pattern.First();
                    text.SetPos(text.GetPos() - (pattern.GetSize() - 1));
                }
                else
                {
                    pattern.Next();
                    len++;
                }
                text.Next();
            }
            else
            {
                text.SetPos(text.GetPos() - len);
                len = 0;
                pattern.First();
                text.Next();
            }
        } while (text.GetPos() != (text.GetSize() - 1)); // loop while curr of text is not at the tail

        // remove extra character from end of text list
        text.Last();
        text.Remove();

        System.out.println("Text contained " + matches + " matches at indexes:\n" + indexes);
    }

    // performs a kmp pattern match
    public static void KMP(List<Character> text, List<Character> pattern)
    {
        // variables
        int matches = 0, len = 0;
        List<Integer> indexes = new List<Integer>();

        // generate failure function
        int[] failFunc = genPartialMatchTable(pattern);

        // adds blank character to end of text list so that the last character
        // gets checked for match
        text.Last();
        text.InsertAfter(' ');

        // set curr of both text and pattern to their respective heads
        text.First();
        pattern.First();
        do
        {
            if(text.GetValue().equals(pattern.GetValue()))
            {
                if(pattern.GetPos() == (pattern.GetSize() - 1))
                {
                    matches++;
                    len = 0;
                    indexes.InsertAfter(text.GetPos() - (pattern.GetSize() - 1));
                    pattern.First();
                    text.SetPos(text.GetPos() - (pattern.GetSize() - 1));
                }
                else
                {
                    pattern.Next();
                    len++;
                }
                text.Next();
            }
            else
            {
                pattern.First();
                if(len > 0)
                {
                    text.SetPos(text.GetPos() - failFunc[len]);
                    len = 0;
                }
                text.Next();
            }
        } while (text.GetPos() != (text.GetSize() - 1)); // loop while curr of text is not at the tail

        // remove extra character from end of text list
        text.Last();
        text.Remove();

        System.out.println("Text contained " + matches + " matches at indexes:\n" + indexes);
    }

    // generates the partial match table (failure function) for
    // kmp algorithm
    private static int[] genPartialMatchTable(List<Character> pattern)
    {
        int max;
        String sub, prefix, suffix, string = "";
        int[] failFunc = new int[pattern.GetSize()];

        // converts List of characters back into string for failFunc generation
        pattern.First();
        for(int i = 0; i < pattern.GetSize(); i++, pattern.Next())
            string += pattern.GetValue();

        for(int i = 0; i < string.length(); i++)
        {
            max = 0;
            sub = string.substring(0,i+1);
            for(int k = 1; k < sub.length(); k++)
            {
                prefix = sub.substring(0,k);
                suffix = sub.substring(sub.length()-k, sub.length());
                if(prefix.equals(suffix) && (prefix.length() > max))
                    max = prefix.length();
            }
            failFunc[i] = max;
        }
        return failFunc;
    }

	// also performs a boyer-moore pattern match since my first one doesn't work
	public static void boyerMoore2(List<Character> text, List<Character> pattern)
	{
		// variables
		int matches = 0, badSymbol, goodSuffix, prevPos = 0;
		boolean	foundSuffix = false;
		List<Integer> indexes = new List<Integer>();
		List<Character> suffix;

		// adds blank character to end of text
		text.Last();
		text.InsertAfter(' ');

		// set text and pattern to appropraite indexes
		pattern.Last();
		text.SetPos(pattern.GetSize() - 1);
		do
		{
			if(pattern.GetValue().equals(text.GetValue()))
			{
				if(pattern.GetPos() == 0)
				{
					matches++;
					indexes.InsertAfter(text.GetPos());
					text.SetPos(text.GetPos() + pattern.GetSize());
					pattern.Last();
				}
				else
				{
					pattern.Prev();
					text.Prev();
				}
			}
			else
			{
				// reset prevPos
				prevPos = 0;

				// set both goodSuffix and badSymbol to default val
				badSymbol = pattern.GetSize();
				goodSuffix = pattern.GetSize();

				// good suffix heuristic
				if(pattern.GetPos() != (pattern.GetSize() - 1))
				{
					// reset suffix list
					suffix = new List<Character>();

					// store location of mismatch in pattern
					prevPos = pattern.GetPos();

					// fill suffix list
					do
					{
						pattern.Next();
						suffix.InsertAfter(pattern.GetValue());
					} while (pattern.GetPos() != (pattern.GetSize() - 1));

					// search for suffix in pattern
					do
					{
						// return pattern to location of mismatch
						pattern.SetPos(prevPos);

						// set suffix to tail
						suffix.Last();

						while (pattern.GetPos() != 0)
						{
							pattern.Prev();
							if(pattern.GetValue().equals(suffix.GetValue()))
							{
								if(suffix.GetPos() == 0)
								{
									goodSuffix = pattern.GetPos();
									foundSuffix = true;
									break;
								}
								else
									suffix.Prev();
							}
							else
							{
								suffix.Last();
							}
						}
						if(foundSuffix)
							break;

						// remove first element of suffix and try scan again
						suffix.First();
						suffix.Remove();
					} while ((suffix.GetSize() != 0) && !foundSuffix);
				}

				// bad symbol heuristic
				if(prevPos != 0)
					pattern.SetPos(prevPos);

				do
				{
					pattern.Prev();
					if(pattern.GetValue().equals(text.GetValue()))
					{
						badSymbol = pattern.GetPos();
						break;
					}
				} while (pattern.GetPos() != 0);

				if(goodSuffix < badSymbol)
					text.SetPos(text.GetPos() + ((pattern.GetSize() - 1) - goodSuffix));
				else if(badSymbol < goodSuffix)
					text.SetPos(text.GetPos() + ((pattern.GetSize() - 1) - badSymbol));
				else
					text.SetPos(text.GetPos() + pattern.GetSize());

				pattern.Last();
			}
		} while (text.GetPos() != (text.GetSize() - 1));

		// remove extra character from end of text list
        text.Last();
        text.Remove();


		System.out.println("Text contained " + matches + " matches at indexes:\n" + indexes);
	}
}
