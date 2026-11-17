
import heapq
from itertools import count

PRIORITY_LABELS = {
    1: "Critical",
    2: "Serious",
    3: "Normal"
}


class HospitalQueue:

    def __init__(self):
        self.heap = []
        self.counter = count()
        self.ids = set()

    # 1. Add Patient (Enqueue)
    def enqueue(self, patient_id, name, priority):

        if priority not in PRIORITY_LABELS:
            print("Invalid priority! Enter 1, 2 or 3.")
            return

        if patient_id in self.ids:
            print("Patient ID already exists!")
            return

        heapq.heappush(
            self.heap,
            (priority, next(self.counter), patient_id, name)
        )

        self.ids.add(patient_id)

        print(f"Patient {name} added successfully as "
              f"{PRIORITY_LABELS[priority]}.")

    # 2. Display Next Patient
    def display_next(self):

        if not self.heap:
            print("No patients waiting.")
            return

        priority, _, pid, name = self.heap[0]

        print("\nNext Patient to be Treated:")
        print("Patient ID:", pid)
        print("Patient Name:", name)
        print("Priority:", priority,
              "-", PRIORITY_LABELS[priority])

    # 3. Remove Patient (Dequeue)
    def dequeue(self):

        if not self.heap:
            print("Queue is empty. No patients to treat.")
            return

        priority, _, pid, name = heapq.heappop(self.heap)

        self.ids.discard(pid)

        print("\nPatient Treated and Removed:")
        print("Patient ID:", pid)
        print("Patient Name:", name)
        print("Priority:", priority,
              "-", PRIORITY_LABELS[priority])

    # 4. Display All Waiting Patients
    def display_all(self):

        if not self.heap:
            print("No patients waiting.")
            return

        print("\n===== Waiting Patients =====")
        print(f"{'No.':<5}{'ID':<10}{'Name':<20}{'Priority'}")
        print("-" * 50)

        for i, (priority, _, pid, name) in enumerate(
                sorted(self.heap), 1):

            print(f"{i:<5}{pid:<10}{name:<20}"
                  f"{priority} ({PRIORITY_LABELS[priority]})")


# Main Function
def main():

    hospital = HospitalQueue()

    while True:

        print("\n===== Hospital Emergency Management =====")
        print("1. Add Patient")
        print("2. Display Next Patient")
        print("3. Treat / Remove Patient")
        print("4. Display All Waiting Patients")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            pid = input("Enter Patient ID: ").strip()
            name = input("Enter Patient Name: ").strip()

            try:
                priority = int(input(
                    "Enter Priority (1-Critical, 2-Serious, 3-Normal): "
                ))

                hospital.enqueue(pid, name, priority)

            except ValueError:
                print("Priority must be a number (1, 2 or 3).")

        elif choice == "2":
            hospital.display_next()

        elif choice == "3":
            hospital.dequeue()

        elif choice == "4":
            hospital.display_all()

        elif choice == "5":
            print("Exiting Hospital Emergency Management System.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

