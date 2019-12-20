import csv
import os

from clients.models import Client


class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, updated_client):
        clients_list = self.list_clients()
        updated_clients_list = []

        for client in clients_list:
            if updated_client.to_dict()['uid'] == client['uid']:
                updated_clients_list.append(updated_client.to_dict())
            else:
                updated_clients_list.append(client)
        self._save_to_disk(updated_clients_list)

    def _save_to_disk(self, clients_list):
        tmp_table_name = '{}.tmp'.format(self.table_name)
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients_list)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
