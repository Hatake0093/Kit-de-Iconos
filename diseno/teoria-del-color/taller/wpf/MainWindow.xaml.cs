using System;
using System.Collections.ObjectModel;
using System.Windows;
using System.Windows.Controls;

namespace CorralNorte;

public record Movimiento(string Referencia, string Tipo, string Ocupacion);

public partial class MainWindow : Window
{
    private int animales = 50;
    private readonly ObservableCollection<Movimiento> movimientos = new()
    {
        new Movimiento("Conteo inicial", "Apertura", "50 de 50")
    };

    public MainWindow()
    {
        InitializeComponent();
        Tabla.ItemsSource = movimientos;
    }

    private void CambiarTema(object sender, RoutedEventArgs e)
    {
        bool oscuro = ModoOscuro.IsChecked == true;
        string archivo = oscuro ? "Oscuro" : "Claro";
        var paleta = new ResourceDictionary
        {
            Source = new Uri($"/CorralNorte;component/Temas/{archivo}.xaml", UriKind.Relative)
        };
        // En App.xaml la primera entrada es la paleta y la segunda contiene los estilos.
        Application.Current.Resources.MergedDictionaries[0] = paleta;
        // .NET 10 marca el cambio de ThemeMode desde C# como experimental.
#pragma warning disable WPF0001
        ThemeMode = oscuro ? System.Windows.ThemeMode.Dark : System.Windows.ThemeMode.Light;
#pragma warning restore WPF0001
    }

    private void RevisarReferencia(object sender, TextChangedEventArgs e)
    {
        if (Registrar is not null)
            Registrar.IsEnabled = animales > 0 && !string.IsNullOrWhiteSpace(Referencia.Text);
    }

    private void RegistrarSalida(object sender, RoutedEventArgs e)
    {
        if (animales == 0 || string.IsNullOrWhiteSpace(Referencia.Text)) return;

        animales--;
        movimientos.Insert(0, new Movimiento(Referencia.Text.Trim(), "Salida de 1", $"{animales} de 50"));
        Ocupacion.Text = $"{animales} de 50 animales";
        Estado.ClearValue(TextBlock.BackgroundProperty);
        Estado.SetResourceReference(TextBlock.ForegroundProperty, "Texto");
        Estado.Text = animales == 0 ? "Corral vacío" : "Hay espacio disponible";
        Referencia.Clear();
        Referencia.Focus();
    }

    private void AbrirHistorial(object sender, RoutedEventArgs e)
    {
        Ficha.Visibility = Visibility.Collapsed;
        Historial.Visibility = Visibility.Visible;
        Volver.Focus();
    }

    private void AbrirFicha(object sender, RoutedEventArgs e)
    {
        Historial.Visibility = Visibility.Collapsed;
        Ficha.Visibility = Visibility.Visible;
        VerHistorial.Focus();
    }
}
