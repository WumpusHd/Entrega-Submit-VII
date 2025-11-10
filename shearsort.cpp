// Implementación sequencial
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;

void sortRow(vector<vector<int>> &M, int row)
{
    if (row % 2 == 0)
        sort(M[row].begin(), M[row].end()); // ascendente
    else
        sort(M[row].rbegin(), M[row].rend()); // descendente
}

void sortColumn(vector<vector<int>> &M, int col)
{
    int n = M.size();
    vector<int> column(n);
    for (int i = 0; i < n; ++i)
        column[i] = M[i][col];

    sort(column.begin(), column.end());

    for (int i = 0; i < n; ++i)
        M[i][col] = column[i];
}

void shearSortRound(vector<vector<int>> &M)
{
    int n = M.size();
    // ordenar filas
    for (int i = 0; i < n; ++i)
        sortRow(M, i);
    // ordenar columnas
    for (int j = 0; j < n; ++j)
        sortColumn(M, j);
}

void shearSort(vector<vector<int>> &M)
{
    int n = M.size();
    int rounds = static_cast<int>(log2(n)) + 1;
    for (int r = 0; r < rounds; ++r)
        shearSortRound(M);
}

bool isSortedSnake(const vector<vector<int>> &M)
{
    int n = M.size();

    for (int i = 0; i < n; ++i)
    {
        for (int j = 1; j < n; ++j)
        {
            if (i % 2 == 0)
            {
                if (M[i][j - 1] > M[i][j])
                    return false;
            }
            else
            {
                if (M[i][j - 1] < M[i][j])
                    return false;
            }
        }
    }

    for (int j = 0; j < n; ++j)
    {
        for (int i = 1; i < n; ++i)
        {
            if (M[i - 1][j] > M[i][j])
                return false;
        }
    }
    return true;
}

int main()
{
    int n;
    cout << "Ingrese el tamaño de la matriz nxn: ";
    cin >> n;

    vector<vector<int>> M(n, vector<int>(n));

    srand(static_cast<unsigned>(time(0)));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            M[i][j] = rand() % 100;

    cout << "\nMatriz inicial:\n";
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
            cout << setw(4) << M[i][j];
        cout << endl;
    }

    shearSort(M);

    cout << "\nMatriz después de ShearSort:\n";
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
            cout << setw(4) << M[i][j];
        cout << endl;
    }
    if (isSortedSnake(M))
        cout << "\nLa matriz está ordenada en patrón serpiente.\n";
    else
        cout << "\nLa matriz NO está ordenada en patrón serpiente.\n";

    return 0;
}
