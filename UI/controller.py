import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        self._view.lista_visualizzazione.controls.clear()
        if self._view.importo_medio_minimo.value.isdigit():
            soglia = float(self._view.importo_medio_minimo.value)
            self._model.costruisci_grafo(soglia)
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di filiali: {self._model.get_num_nodes()}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di collegamenti: {self._model.get_num_edges()}"))
            count = 0
            for u, v, dati in self._model.G.edges(data=True):
                count += 1
                self._view.lista_visualizzazione.controls.append(ft.Text(f"{count}): {u} --> {v} -- importo medio per bonifico: {dati['peso']}"))
            self._view.update()
        else:
            self._view.show_alert("Inserire un importo medio valido")

