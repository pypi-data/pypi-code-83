from sabi.api_client import ApiClient

class Sync(ApiClient):
    headers = None

    def __init__(self, logger, api_key, host, version):
        base = f'{version}/sync'
        self.headers = {'content-type': 'application/json','Authorization': f'Bearer {api_key}'}
        super().__init__(logger, host, base)

    def save_individuals(self, individuals):
        response = self.put('individuals',json=individuals)
        return response

    def save_states(self, states):
        response = self.put('status',json=states)
        return response
        
    def save_ticket_assignments(self, ticket_assignments):
        response = self.put('tickets','assignment',json=ticket_assignments)
        return response

    def save_ticket_status_changes(self, ticket_status_changes):
        response = self.put('tickets','status','changes',json=ticket_status_changes)
        
        return response

    def save_tickets(self, tickets):
        response = self.put('tickets',json=tickets)
        
    def delete_tickets(self, tickets):
        response = self.delete('tickets',json=tickets)
        return response

    def save_pagination(self, pagination_information):
        response = self.put('pagination',json=pagination_information)
        
        return response

    def get_pagination(self):
        response = self.get('pagination')
        
        return response

    def get_missing_individuals(self):
        response = self.get('individuals','missing')
        
        return response

    def get_missing_statuses(self):
        response = self.get('status','missing')
        
        return response
    
