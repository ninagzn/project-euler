#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>

class Problem18
{
  public:
	int getSolution()
	{
		int **m = constructSparseMatrix();
		for (int i = 13; i >= 0; --i)
		{
			for (int j = 0; j <= i; ++j)
			{
				m[i][j] = m[i][j] + std::max(m[i + 1][j], m[i + 1][j + 1]);
			}
		}

		return m[0][0];
	}

	int **constructSparseMatrix()
	{
		int **arr = new int *[15];
		std::ifstream inf("Problem18.in");
		for (int i = 0; i < 15; i++)
		{
			arr[i] = new int[i + 1];
			for (int k = 0; k <= i; k++)
			{
				std::string strInput;
				inf >> strInput;
				arr[i][k] = std::stoi(strInput);
			}
		}

		return arr;
	}
};

int main()
{
	Problem18 pr;
	std::cout << pr.getSolution() << std::endl;
	return 0;
}
