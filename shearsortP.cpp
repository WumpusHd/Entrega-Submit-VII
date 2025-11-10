#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <omp.h>
using namespace std;

void sortRow(vector<vector<int>> &M, int row)
{
    if (row % 2 == 0)
        sort(M[row].begin(), M[row].end());
    else
        sort(M[row].rbegin(), M[row].rend());
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

void shearSortRoundParallel(vector<vector<int>> &M)
{
    int n = M.size();

#pragma omp parallel for
    for (int i = 0; i < n; ++i)
        sortRow(M, i);

#pragma omp parallel for
    for (int j = 0; j < n; ++j)
        sortColumn(M, j);
}

void shearSortParallel(vector<vector<int>> &M)
{
    int n = M.size();
    int rounds = static_cast<int>(log2(n)) + 1;
    for (int r = 0; r < rounds; ++r)
        shearSortRoundParallel(M);
}

int main()
{
    int n, threads;
    cout << "Ingrese tamaño de matriz n×n: ";
    cin >> n;
    cout << "Ingrese número de hilos: ";
    cin >> threads;

    omp_set_num_threads(threads);
    vector<vector<int>> M(n, vector<int>(n));
    srand(static_cast<unsigned>(time(0)));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            M[i][j] = rand() % 100;

    shearSortParallel(M);

    cout << "\nMatriz ordenada (paralelo) con " << threads << " hilos:\n";
    for (auto &row : M)
    {
        for (int val : row)
            cout << setw(4) << val;
        cout << endl;
    }
    return 0;
}
