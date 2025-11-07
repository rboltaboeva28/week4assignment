def receive_new_shipments(shipments, new_shipments):
    for element in new_shipments:
        shipments.append(element) 

def dispatch_shipments(shipments, num_to_dispatch):
    dispatched = []
    if num_to_dispatch >= len(shipments):
        dispatched = shipments[:]   
        shipments = []
    else:
        for i in range(num_to_dispatch):
            if len(shipments) == 0:
               break
            element = shipments.pop(0)
            dispatched.append(element)
    return dispatched


def recall_shipment(shipments, shipment_id):
    if shipment_id in shipments:
        shipments.remove(shipment_id)
        return True
    return False    
    

def manage_shipments(initial_shipments, new_shipments_to_receive, shipments_to_dispatch, shipment_to_recall):
    copy_of_initial_shipments = initial_shipments[:]
    receive_new_shipments(copy_of_initial_shipments, new_shipments_to_receive)
    recall_shipment(copy_of_initial_shipments, shipment_to_recall)
    dispatched_shipments_list = dispatch_shipments(copy_of_initial_shipments, shipments_to_dispatch)
    final_shipments_list = copy_of_initial_shipments
    return final_shipments_list, dispatched_shipments_list

initial = ["BOX-A1", "BOX-B2", "BOX-C3", "BOX-D4"]
new = ["BOX-E5", "BOX-F6"]
dispatch_count = 2
recall_id = "BOX-D4"

final_state, dispatched = manage_shipments(initial, new, dispatch_count, recall_id)

print()
print("Test Case 1 Results:")
print(f"final_state: {final_state}")
print(f"dispatched: {dispatched}\n")
print(f"Original list unchanged: {initial}\n")