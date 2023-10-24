def hanoi(n, begin, operate, end):
    if n == 1:
        print(f"Move disk 1 from {begin} to {end}")
        return
    hanoi(n-1, begin, end, operate)
    print(f"Move disk {n} from {begin} to {end}")
    hanoi(n-1, operate, begin, end)

n = 3
begin_peg = "A"
operate_peg = "B"
end_peg = "C"
hanoi(n, begin_peg, operate_peg, end_peg)