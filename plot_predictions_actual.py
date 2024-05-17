
def plot_predictions_vs_actual(y_real, y_pred):
    """
    Función para graficar los valores reales vs. los valores predichos en una regresión.

    Args:
    y_real (array-like): Valores reales de la variable objetivo.
    y_pred (array-like): Valores predichos de la variable objetivo.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, y_real, alpha=0.5)
    plt.xlabel("Valores Predichos")
    plt.ylabel("Valores Reales")

    # Línea y=x
    #max_value = max(max(y_real), max(y_pred))
    #min_value = min(min(y_real), min(y_pred))
    #plt.plot([min_value, max_value], [min_value, max_value], 'r')
    plt.plot([8, 15], [8, 15], 'r')   # Una línea perfecta es una línea de pendiente uno y tiene la siguiente forma punto1 = (0,0) e punto2 = (15,15)
    plt.title("Comparación de Valores Reales vs. Predichos")
    plt.show()