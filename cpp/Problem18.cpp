#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>

class Problem18
{
  public:
	int getSolution()
	{
		int **tr = readTriangle();
		for (int i = 13; i >= 0; --i)
		{
			for (int j = 0; j <= i; ++j)
			{
				tr[i][j] += std::max(tr[i + 1][j], tr[i + 1][j + 1]);
			}
		}

		return tr[0][0];
	}

	int **readTriangle()
	{
		int **tr = new int *[15];
		std::ifstream inf("Problem18.in");
		for (int i = 0; i < 15; i++)
		{
			tr[i] = new int[i + 1];
			for (int k = 0; k <= i; k++)
			{
				std::string strInput;
				inf >> strInput;
				tr[i][k] = std::stoi(strInput);
			}
		}

		return tr;
	}
};

int main()
{
	Problem18 pr;
	std::cout << pr.getSolution() << std::endl;
	return 0;
}
