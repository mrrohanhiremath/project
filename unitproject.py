class Volunteer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.event = None  # Initialize event assignment to None

    def assign_event(self, event):
        self.event = event

class Event:
    def __init__(self, id, name, tracking_hours):
        self.id = id
        self.name = name
        self.tracking_hours = tracking_hours

class EventManager:
    def __init__(self):
        self.volunteers = []
        self.events = []
        
    def add_volunteer(self, volunteer):
        if self.get_volunteer(volunteer.id) is None:
            self.volunteers.append(volunteer)
            print(f"Volunteer {volunteer.name} added successfully")
        else:
            print("Volunteer with the same ID already exists,cannot add")

    def remove_volunteer(self, volunteer_id):
        removed_volunteer = None
        for volunteer in self.volunteers:
            if volunteer.id == volunteer_id:
                removed_volunteer = volunteer
                self.volunteers.remove(volunteer)
                print(f"Volunteer {volunteer.name} removed successfully")
                break
        if removed_volunteer is None:
            print("Volunteer not found")
    
    def add_event(self, event):
        if not self.get_event(event.id):
            self.events.append(event)
            print(f"Event {event.name} added successfully")
        else:
            print("Event with the same ID already exists. Please choose a different ID")

    def assign_volunteer_to_event(self, volunteer_id, event_id):
        volunteer = self.get_volunteer(volunteer_id)
        event = self.get_event(event_id)
        if volunteer and event:
            volunteer.assign_event(event)
            print(f"Volunteer {volunteer.name} assigned to event {event.name} successfully")
        else:
            print("Volunteer or event not found2")
    
    def get_volunteer(self, volunteer_id):
        volunteer = next((v for v in self.volunteers if v.id == volunteer_id), None)
        if volunteer:
            print(f"Volunteer ID: {volunteer.id}")
            print(f"Name: {volunteer.name}")
            print(f"Email: {volunteer.email}")
            return volunteer
        else:
            #print("Volunteer not found3")
            return None
 

    def update_volunteer(self, volunteer_id, new_name, new_email):
        volunteer = self.get_volunteer(volunteer_id)
        if volunteer:
            volunteer.name = new_name
            volunteer.email = new_email
            print(f"Volunteer {volunteer.name} updated successfully")
        else:
            print("Volunteer not found4")

    def get_event(self, event_id):
        return next((e for e in self.events if e.id == event_id), None)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for volunteer in self.volunteers:
                if volunteer.event:
                    file.write(f"{volunteer.name} is assigned to {volunteer.event.name} for {volunteer.event.tracking_hours} hours\n")
                else:
                    file.write(f"{volunteer.name} is not assigned to any event\n")
        print(f"Data saved to {filename}")

# Example usage:
event_manager = EventManager()

while True:
    print("\n1. Add Volunteer\n2. Remove Volunteer\n3. Add Event\n4. Assign Volunteer to Event\n5. Update Volunteer\n6. Get Volunteer\n7. Display Volunteer-Event Assignments\n8. Save to File\n9. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        id = int(input("Enter volunteer ID: "))
        name = input("Enter volunteer name: ")
        email = input("Enter volunteer email id: ")
        volunteer = Volunteer(id, name, email)
        event_manager.add_volunteer(volunteer)

    elif choice == "2":
        volunteer_id = int(input("Enter ID of volunteer to remove: "))
        event_manager.remove_volunteer(volunteer_id)

    elif choice == "3":
        id = int(input("Enter event ID: "))
        name = input("Enter event name: ")
        tracking_hours = int(input("Enter no. of hours: "))
        event = Event(id, name, tracking_hours)
        event_manager.add_event(event)

    elif choice == "4":
        volunteer_id = int(input("Enter volunteer ID: "))
        event_id = int(input("Enter event ID: "))
        event_manager.assign_volunteer_to_event(volunteer_id, event_id)

    elif choice == "5":
        volunteer_id = int(input("Enter volunteer ID: "))
        new_name = input("Enter new name for volunteer: ")
        new_email = input("Enter new email for volunteer: ")
        event_manager.update_volunteer(volunteer_id, new_name, new_email)

    elif choice == "6":
        volunteer_id = int(input("Enter volunteer ID: "))
        volunteer = event_manager.get_volunteer(volunteer_id)
        if volunteer:
            print(f"Volunteer {volunteer.name} found")
        else:
            print("Volunteer not found5")

    elif choice == "7":
        print("\nVolunteer-Event Assignments:")
        for volunteer in event_manager.volunteers:
            if volunteer.event:
                print(f"{volunteer.name} is assigned to {volunteer.event.name} for {volunteer.event.tracking_hours} hours")
            else:
                print(f"{volunteer.name} is not assigned to any event")

    elif choice == "8":
        filename = input("Enter filename to save data: ")
        event_manager.save_to_file(filename)

    elif choice == "9":
        print("Exit")
        break

    else:
        print("Invalid choice")

