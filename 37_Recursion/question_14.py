# Question:
# Solve the Tower of Hanoi problem recursively.
# Move N disks from peg A to peg C using peg B as auxiliary.
# Print each move.

# Example (N=3):
# Move disk 1 from A to C
# Move disk 2 from A to B
# ...

def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print(f"Move disk 1 from {from_peg} to {to_peg}")
        return
    tower_of_hanoi(n - 1, from_peg, aux_peg, to_peg)
    print(f"Move disk {n} from {from_peg} to {to_peg}")
    tower_of_hanoi(n - 1, aux_peg, to_peg, from_peg)

n = int(input("Enter number of disks: "))
print(f"Tower of Hanoi with {n} disk(s):")
tower_of_hanoi(n, "A", "C", "B")
print(f"\nTotal moves: {2**n - 1}")
