""" The task6
"""

def delete_dublicate_in_tickets(tickets: dict) -> dict:
    list_tickets = list(tickets.values())
    for tickets_ in list_tickets:
        for i in range(list_tickets.index(tickets_) + 1, len(list_tickets)):
            for task in tickets_:
                if task in list_tickets[i]:
                    list_tickets[i].remove(task)
            
    return tickets


def update_tickets_by_type(types: dict, tickets: dict) -> dict:
    result: dict = dict()
    for (type, ticket) in tickets.items():
        result[types[type]] = ticket

    return result


types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 
print(delete_dublicate_in_tickets(tickets))
print(update_tickets_by_type(types, tickets))
