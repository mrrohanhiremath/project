class Volunteer:
    def __init__(self, volunteer_id, name, email_id):
        self.volunteer_id = volunteer_id
        self.name = name
        self.email_id = email_id

class EventManager:
    def __init__(self):
        self.volunteers = {}

    def add_volunteer(self, volunteer_id, name, email_id):
        if volunteer_id in self.volunteers:
            raise ValueError("Volunteer ID already exists")
        self.volunteers[volunteer_id] = Volunteer(volunteer_id, name, email_id)

    def get_volunteer(self, volunteer_id):
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer ID does not exist")
        return self.volunteers[volunteer_id]

    def update_volunteer(self, volunteer_id, name=None, email_id=None):
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer ID does not exist")
        volunteer = self.volunteers[volunteer_id]
        if name:
            volunteer.name = name
        if email_id:
            volunteer.email_id = email_id

    def delete_volunteer(self, volunteer_id):
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer ID does not exist")
        del self.volunteers[volunteer_id]

# Unit tests
import unittest

class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.event_manager.add_volunteer(1, "John Doe", "john@example.com")
        self.event_manager.add_volunteer(2, "Jane Smith", "jane@example.com")

    def test_add_volunteer(self):
        self.event_manager.add_volunteer(3, "Alice Johnson", "alice@example.com")
        self.assertIn(3, self.event_manager.volunteers)

    def test_get_volunteer(self):
        volunteer = self.event_manager.get_volunteer(1)
        self.assertEqual(volunteer.name, "John Doe")

    def test_update_volunteer(self):
        self.event_manager.update_volunteer(1, name="Johnathan Doe")
        volunteer = self.event_manager.get_volunteer(1)
        self.assertEqual(volunteer.name, "Johnathan Doe")

    def test_delete_volunteer(self):
        self.event_manager.delete_volunteer(1)
        self.assertNotIn(1, self.event_manager.volunteers)

if __name__ == '__main__':
    unittest.main(verbosity=3)