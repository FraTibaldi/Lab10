from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None # dizionario
        self._edges = None # dizionario che ha come chiavi la tupla degli id delle filiali e come valori i pesi dei collegamenti
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        self.G.clear()
        if self._nodes is None:
            self._nodes = DAO.read_filiali()
        if self._edges is None:
            self._edges = self.get_all_edges()
        for node in self._nodes.values():
            self.G.add_node(node)
        for tupla in self._edges:
            if self._edges[tupla] >= threshold:
                u = self._nodes[tupla[0]]
                v = self._nodes[tupla[1]]
                self.G.add_edge(u, v, peso = self._edges[(u.id, v.id)])

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return len(self._nodes.values())

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return DAO.read_collegamenti_pesati()
