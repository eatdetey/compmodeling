using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ZedGraph;

namespace lab1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private double[] xData = { 1, 2, 3, 4, 5 };
        private double[] yData = { 2.2, 2.8, 3.6, 4.5, 5.1 };

        private void Form1_Load(object sender, EventArgs e)
        {
            DrawGraph();
        }

        private void DrawGraph()
        {
            GraphPane pane = zedGraphControl1.GraphPane;

            // Очистка старого графика
            pane.CurveList.Clear();

            // Установка заголовков и осей
            pane.Title.Text = "Аппроксимация методом наименьших квадратов";
            pane.XAxis.Title.Text = "X";
            pane.YAxis.Title.Text = "Y";

            // Экспериментальные точки
            PointPairList points = new PointPairList(xData, yData);
            LineItem dataCurve = pane.AddCurve("Экспериментальные точки", points, System.Drawing.Color.Blue, SymbolType.Circle);
            dataCurve.Line.IsVisible = false;  // Показывать только точки

            // Линейная аппроксимация
            var linearCoeffs = LinearLeastSquares(xData, yData);
            AddFunction(pane, "Линейная аппроксимация", x => linearCoeffs.Item1 * x + linearCoeffs.Item2, System.Drawing.Color.Red);

            // Степенная аппроксимация
            var powerCoeffs = PowerLeastSquares(xData, yData);
            AddFunction(pane, "Степенная аппроксимация", x => powerCoeffs.Item1 * Math.Pow(x, powerCoeffs.Item2), System.Drawing.Color.Green);

            // Показательная аппроксимация
            var exponentialCoeffs = ExponentialLeastSquares(xData, yData);
            AddFunction(pane, "Показательная аппроксимация", x => exponentialCoeffs.Item1 * Math.Exp(exponentialCoeffs.Item2 * x), System.Drawing.Color.Purple);

            // Квадратичная аппроксимация
            var quadraticCoeffs = QuadraticLeastSquares(xData, yData);
            AddFunction(pane, "Квадратичная аппроксимация", x => quadraticCoeffs.Item1 * x * x + quadraticCoeffs.Item2 * x + quadraticCoeffs.Item3, System.Drawing.Color.Orange);

            // Обновление графика
            zedGraphControl1.AxisChange();
            zedGraphControl1.Invalidate();
        }

        private void AddFunction(GraphPane pane, string label, Func<double, double> func, System.Drawing.Color color)
        {
            PointPairList list = new PointPairList();
            for (double x = xData.Min(); x <= xData.Max(); x += 0.1)
            {
                double y = func(x);
                list.Add(x, y);
            }
            pane.AddCurve(label, list, color, SymbolType.None);
        }

        private Tuple<double, double> LinearLeastSquares(double[] x, double[] y)
        {
            int n = x.Length;
            double sumX = x.Sum();
            double sumY = y.Sum();
            double sumXY = x.Zip(y, (xi, yi) => xi * yi).Sum();
            double sumX2 = x.Select(xi => xi * xi).Sum();

            double a = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
            double b = (sumY - a * sumX) / n;
            return Tuple.Create(a, b);
        }

        private Tuple<double, double> PowerLeastSquares(double[] x, double[] y)
        {
            double[] logX = x.Select(xi => Math.Log(xi)).ToArray();
            double[] logY = y.Select(yi => Math.Log(yi)).ToArray();

            var linearCoeffs = LinearLeastSquares(logX, logY);
            double a = Math.Exp(linearCoeffs.Item2);
            double b = linearCoeffs.Item1;
            return Tuple.Create(a, b);
        }

        private Tuple<double, double> ExponentialLeastSquares(double[] x, double[] y)
        {
            double[] logY = y.Select(yi => Math.Log(yi)).ToArray();

            var linearCoeffs = LinearLeastSquares(x, logY);
            double a = Math.Exp(linearCoeffs.Item2);
            double b = linearCoeffs.Item1;
            return Tuple.Create(a, b);
        }

        private Tuple<double, double, double> QuadraticLeastSquares(double[] x, double[] y)
        {
            int n = x.Length;
            double sumX = x.Sum();
            double sumX2 = x.Select(xi => xi * xi).Sum();
            double sumX3 = x.Select(xi => xi * xi * xi).Sum();
            double sumX4 = x.Select(xi => xi * xi * xi * xi).Sum();
            double sumY = y.Sum();
            double sumXY = x.Zip(y, (xi, yi) => xi * yi).Sum();
            double sumX2Y = x.Zip(y, (xi, yi) => xi * xi * yi).Sum();

            double[,] matrix = {
               { n, sumX, sumX2 },
               { sumX, sumX2, sumX3 },
               { sumX2, sumX3, sumX4 }
            };

            double[] vector = { sumY, sumXY, sumX2Y };

            double[] result = GaussianElimination(matrix, vector);
            return Tuple.Create(result[0], result[1], result[2]);
        }

        private double[] GaussianElimination(double[,] matrix, double[] vector)
        {
            int n = vector.Length;
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    double ratio = matrix[j, i] / matrix[i, i];
                    for (int k = i; k < n; k++)
                    {
                        matrix[j, k] -= ratio * matrix[i, k];
                    }
                    vector[j] -= ratio * vector[i];
                }
            }

            double[] result = new double[n];
            for (int i = n - 1; i >= 0; i--)
            {
                result[i] = vector[i] / matrix[i, i];
                for (int j = i + 1; j < n; j++)
                {
                    result[i] -= matrix[i, j] * result[j] / matrix[i, i];
                }
            }
            return result;
        }
    }
}
